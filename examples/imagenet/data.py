#  Copyright 2023 The Fluid Authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  Copyright 2023 The Fluid Authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import os.path

from fluid.io import FluidFileSystem
from fluid import FluidK8sClient
import fluid.models
import fluid.constants
from torch.utils import data
from PIL import Image

from typing import Tuple, List, Dict, Optional, Callable, Any, Union, cast

import time


class FluidMapDataset(data.Dataset):
    _repr_indent = 4

    def __init__(
            self,
            dataset_name: str,
            root: str = "/",
            transform: Optional[Callable] = None,
            target_transform: Optional[Callable] = None
    ) -> None:
        if dataset_name is None or len(dataset_name) == 0:
            raise ValueError("dataset_name should not be empty")
        self.dataset_name = dataset_name
        self.root = root
        # self.filesystem = FluidFileSystem(dataset_name)
        self.transform = transform
        self.target_transform = target_transform
        self.data_filesystem = None

    def __getitem__(self, index):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __repr__(self) -> str:
        head = "Dataset " + self.__class__.__name__
        body = [f"Number of datapoints: {self.__len__()}"]
        if self.dataset_name is not None and self.root is not None:
            body.append(f"Dataset root directory: fluid://{self.dataset_name}:{os.path.join('/', self.root)}")
        body += self.extra_repr().splitlines()
        lines = [head] + [" " * self._repr_indent + line for line in body]
        return "\n".join(lines)

    def _format_transform_repr(self, transform: Callable, head: str) -> List[str]:
        lines = transform.__repr__().splitlines()
        return [f"{head}{lines[0]}"] + ["{}{}".format(" " * len(head), line) for line in lines[1:]]

    def extra_repr(self) -> str:
        return ""


class FluidDatasetFolder(FluidMapDataset):
    def __init__(
            self,
            dataset_name: str,
            root: str = "/",
            loader: Callable[[FluidFileSystem, str], Any] = None,
            extensions: Optional[Tuple[str, ...]] = None,
            transform: Optional[Callable] = None,
            target_transform: Optional[Callable] = None,
            is_valid_file: Optional[Callable[[str], bool]] = None,
            need_warmup: bool = False
    ) -> None:
        super().__init__(dataset_name, root, transform, target_transform)
        start_time = time.time()
        classes, class_to_idx = self.find_classes(self.root)
        print(f"find_classes: {time.time() - start_time}")
        samples = self.make_dataset(self.root, class_to_idx, extensions, is_valid_file)

        if need_warmup:
            fluid_client = FluidK8sClient()
            fluid_client.create_data_operation(fluid.models.DataLoad(
                api_version=fluid.constants.API_VERSION,
                kind=fluid.constants.DATA_LOAD_KIND,
                metadata=fluid.models.V1ObjectMeta(
                    name=f"{dataset_name}-warmup-{time.time()}"
                ),
                spec=fluid.models.DataLoadSpec(
                    dataset=fluid.models.TargetDataset(
                        namespace=fluid_client.namespace,
                        name=dataset_name,
                    ),
                    target=fluid.models.TargetPath(
                        path=root,
                        replicas=1
                    )
                )
            ), wait=False)

        self.loader = loader
        self.extension = extensions

        self.classes = classes
        self.class_to_idx = class_to_idx
        self.samples = samples
        self.targets = [s[1] for s in samples]

    def __getitem__(self, index: int) -> Tuple[Any, Any]:
        """
        Args:
            index (int): Index

        Returns:
            tuple: (sample, target) where target is class_index of the target class.
        """
        if self.data_filesystem is None:
            self.data_filesystem = FluidFileSystem(self.dataset_name)

        path, target = self.samples[index]
        sample = self.loader(self.data_filesystem, path)
        if self.transform is not None:
            sample = self.transform(sample)
        if self.target_transform is not None:
            target = self.target_transform(target)

        return sample, target

    def __len__(self) -> int:
        return len(self.samples)

    @staticmethod
    def _make_samples_for_target_class(filesystem, target_dir, target_class, is_valid_file):
        instances = []
        for path in sorted(filesystem.find(target_dir)):
            if is_valid_file(path):
                item = path, target_class
                instances.append(item)
        return instances

    def make_dataset(
            self,
            directory: str,
            class_to_idx: Dict[str, int],
            extensions: Optional[Tuple[str, ...]] = None,
            is_valid_file: Optional[Callable[[str], bool]] = None,
    ) -> List[Tuple[str, int]]:
        if class_to_idx is None:
            raise ValueError("The class_to_idx parameter cannot be None.")

        both_none = extensions is None and is_valid_file is None
        both_something = extensions is not None and is_valid_file is not None
        if both_none or both_something:
            raise ValueError("Both extensions and is_valid_file cannot be None or not None at the same time")

        if extensions is not None:
            def is_valid_file(filename: str) -> bool:
                return filename.lower().endswith(extensions if isinstance(extensions, str) else tuple(extensions))

        is_valid_file = cast(Callable[[str], bool], is_valid_file)

        filesystem = FluidFileSystem(dataset_name=self.dataset_name)
        instances = []
        available_classes = set()

        # result = await asyncio.gather(*[self._make_samples_for_target_class(filesystem, os.path.join(directory, target_class), target_class, is_valid_file) for target_class in class_to_idx.keys()])
        # for instance in result:
        #     for sample, target_class in instance:
        #         item = sample, target_class
        #         instances.append(item)
        #         if target_class not in available_classes:
        #             available_classes.add(target_class)

        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
            future_samples = {
                executor.submit(self._make_samples_for_target_class, filesystem, os.path.join(directory, target_class),
                                target_class, is_valid_file): target_class for target_class in class_to_idx.keys()}
            for future in concurrent.futures.as_completed(future_samples):
                try:
                    instance = future.result()
                    for sample, target_class in instance:
                        item = sample, class_to_idx[target_class]
                        instances.append(item)
                        if target_class not in available_classes:
                            available_classes.add(target_class)
                except Exception as exc:
                    print('%r generated an exception: %s' % (target_class, exc))

        # for target_class in sorted(class_to_idx.keys()):
        #     start_time = time.time()
        #
        #     class_index = class_to_idx[target_class]
        #     target_dir = os.path.join(directory, target_class)
        #     if not filesystem.isdir(target_dir):
        #         continue
        #     for path in sorted(filesystem.find(target_dir)):
        #         if is_valid_file(path):
        #             item = path, class_index
        #             instances.append(item)
        #             if target_class not in available_classes:
        #                 available_classes.add(target_class)
        #     # for root, _, fnames in sorted(filesystem.walk(target_dir)):  # how about using find ?
        #     #     for fname in sorted(fnames):
        #     #         path = os.path.join(root, fname)
        #     #         if is_valid_file(path):
        #     #             item = path, class_index
        #     #             instances.append(item)
        #     #
        #     #             if target_class not in available_classes:
        #     #                 available_classes.add(target_class)
        #     print(f"{target_class} ready: {time.time() - start_time}")

        empty_classes = set(class_to_idx.keys()) - available_classes
        if empty_classes:
            msg = f"Found no valid file for the classes {', '.join(sorted(empty_classes))}. "
            if extensions is not None:
                msg += f"Supported extensions are: {extensions if isinstance(extensions, str) else ', '.join(extensions)}"
            raise FileNotFoundError(msg)

        return instances

    def find_classes(self, directory: str) -> Tuple[List[str], Dict[str, int]]:
        classes = []
        filesystem = FluidFileSystem(dataset_name=self.dataset_name)
        for direntry in filesystem.listdir(directory):
            classes.append(direntry['name'].split("/")[-1])
        classes = sorted(classes)
        class_to_idx = {classes[i]: i for i in range(len(classes))}

        return classes, class_to_idx


IMG_EXTENSIONS = (".jpg", ".jpeg", ".png", ".ppm", ".bmp", ".pgm", ".tif", ".tiff", ".webp")


def pil_loader(filesystem: FluidFileSystem, path: str) -> Image.Image:
    with filesystem.open(path, "rb") as f:
        img = Image.open(f)
        return img.convert("RGB")


def default_loader(filesystem: FluidFileSystem, path: str) -> Any:
    return pil_loader(filesystem, path)


class FluidImageFolder(FluidDatasetFolder):
    def __init__(
            self,
            dataset_name: str,
            root: str,
            transform: Optional[Callable] = None,
            target_transform: Optional[Callable] = None,
            loader: Callable[[FluidFileSystem, str], Any] = default_loader,
            is_valid_file: Optional[Callable[[str], bool]] = None,
            need_warmup: bool = False
    ):
        super().__init__(
            dataset_name,
            root,
            loader,
            IMG_EXTENSIONS if is_valid_file is None else None,
            transform=transform,
            target_transform=target_transform,
            is_valid_file=is_valid_file,
            need_warmup=need_warmup
        )
        self.imgs = self.samples
