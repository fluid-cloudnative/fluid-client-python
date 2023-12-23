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
import copy

import s3fs
from fluid.api.fluid_client import FluidClient
from fluid.utils import utils as fluidutils
from fluid import constants
from kubernetes import client

from typing import Dict

import os


class FluidFileSystem:
    def __init__(self, dataset_name: str, workdir=None, **kwargs):
        self.fluid_client = FluidClient()

        if workdir is None:
            workdir = "/"

        self.workdir = workdir

        try:
            namespace = self.fluid_client.namespace
            dataset = self.fluid_client.get_dataset(dataset_name, namespace=namespace)
        except client.ApiException as e:
            if e.status == 404:
                raise RuntimeError(f"Failed to init FluidFileSystem: Dataset {dataset_name} not found")
            else:
                raise RuntimeError(f"Failed to init FluidFileSystem: {e}")
        except Exception as e:
            raise RuntimeError(f"Failed to init FluidFileSystem: {e}")

        assert dataset is not None

        if dataset.status is None or dataset.status.phase != "Bound":
            raise RuntimeError(f"Failed to init FluidFileSystem: Dataset {dataset_name} not ready")

        if len(dataset.status.runtimes) == 0:
            raise RuntimeError(f"Failed to init FluidFileSystem: Dataset {dataset_name} has no bound runtime")

        self.runtime_kind = fluidutils.infer_runtime_kind(dataset.status.runtimes[0].type)
        if self.runtime_kind is None:
            raise RuntimeError(
                f"Failed to init FluidFileSystem: Dataset {dataset_name} has unsupported runtime type: {dataset.status.runtimes[0].type}")

        if kwargs is None:
            kwargs = {}

        if self.runtime_kind == constants.JUICEFS_RUNTIME_KIND:
            kwargs["key"] = "admin"
            kwargs["secret"] = "password"
            kwargs["endpoint_url"] = f"http://{dataset_name}-s3-gateway:9000"
            # kwargs["endpoint_url"] = f"http://127.0.0.1:9000"
            self.s3_client = s3fs.S3FileSystem(**kwargs)

            self.bucket_name = dataset.spec.mounts[0].name

            self.path_prefix_without_protocol = f"{self.bucket_name}{os.path.join('/', self.workdir)}"
            self.path_prefix = f"s3://{self.path_prefix_without_protocol}"
            if self.path_prefix.endswith("/"):
                self.path_prefix = self.path_prefix[:-1]

    def _expand_path(self, path):
        if path.startswith("/"):
            path = path[1:]
        return f"{self.path_prefix}/{path}"

    def _fold_path(self, path: str):
        return path[len(self.path_prefix_without_protocol):]

    def ls(self, path, detail=True, **kwargs):
        return self.s3_client.ls(self._expand_path(path), detail, **kwargs)

    def walk(self, path, maxdepth=None, topdown=True, on_error="omit", **kwargs):
        def generator():
            for root, dirs, fnames in self.s3_client.walk(self._expand_path(path), maxdepth, topdown, on_error,
                                                          **kwargs):
                yield self._fold_path(root), dirs, fnames

        return generator()

    def find(self, path, maxdepth=None, withdirs=False, detail=False, **kwargs):
        ret = self.s3_client.find(self._expand_path(path), maxdepth, withdirs, detail, **kwargs)
        return [self._fold_path(x) for x in ret]

    def du(self, path, total=True, maxdepth=None, **kwargs):
        res = self.s3_client.du(self._expand_path(path), total, maxdepth, **kwargs)
        if isinstance(res, Dict):
            return {self._fold_path(key): value for key, value in res.items()}

        return res

    def glob(self, path, **kwargs):
        ret = self.s3_client.glob(self._expand_path(path), **kwargs)
        return [self._fold_path(x) for x in ret]

    def exists(self, path, **kwargs):
        return self.s3_client.exists(self._expand_path(path), **kwargs)

    def info(self, path, **kwargs):
        return self.s3_client.info(self._expand_path(path), **kwargs)

    def isdir(self, path):
        return self.s3_client.isdir(self._expand_path(path))

    def isfile(self, path):
        return self.s3_client.isfile(self._expand_path(path))

    def read_text(self, path, encoding=None, errors=None, newline=None, **kwargs):
        return self.s3_client.read_text(self._expand_path(path), encoding, errors, newline, **kwargs)

    def cat(self, path, recursive=False, on_error="raise", **kwargs):
        return self.s3_client.cat(self._expand_path(path), recursive, on_error, **kwargs)

    def open(self, path, mode="rb", block_size=None, cache_options=None, compression=None, **kwargs):
        return self.s3_client.open(self._expand_path(path), mode, block_size, cache_options, compression, **kwargs)

    def listdir(self, path, detail=True, **kwargs):
        res = self.s3_client.listdir(self._expand_path(path), detail, **kwargs)
        ret = []
        for directory in res:
            x = copy.deepcopy(directory)
            x['Key'] = self._fold_path(x['Key'])
            x['name'] = self._fold_path(x['name'])
            ret.append(x)
        return ret

    def stat(self, path, **kwargs):
        res = self.s3_client.stat(self._expand_path(path), **kwargs)
        ret = copy.deepcopy(res)
        ret['name'] = self._fold_path(ret['name'])
        # For stating directory
        if 'Key' in ret:
            ret['Key'] = self._fold_path(ret['Key'])
        return ret


if __name__ == '__main__':
    fs = FluidFileSystem("sd-dataset", workdir="datasets")
