#  Copyright 2024 The Fluid Authors.
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

import logging
from typing import Optional

from kubernetes import client

from fluid.utils import utils
from fluid.constants import constants
from fluid import models
from fluid.api.fluid_k8s_client import FluidK8sClient
from fluid.api.fluid_dataflow import FluidDataFlow

logger = logging.getLogger("fluidsdk")


class ClientConfig(object):
    def __init__(self,
                 namespace: str = utils.get_default_target_namespace(),
                 runtime_kind: str = constants.ALLUXIO_RUNTIME_KIND,
                 kube_config_file: Optional[str] = None,
                 kube_context: Optional[str] = None,
                 kube_client_configuration: Optional[client.Configuration] = None):
        self.namespace = namespace
        self.runtime_kind = utils.infer_runtime_kind(runtime_kind)
        self.kube_config_file = kube_config_file
        self.kube_context = kube_context
        self.kube_client_configuration = kube_client_configuration


class FluidClient(object):
    def __init__(self, config: ClientConfig):
        if not config:
            raise ValueError("config should not be None")
        if not config.namespace:
            raise ValueError("namespace should not be None")
        self.config = config
        self.k8s_client = FluidK8sClient(config.namespace, config.runtime_kind, config.kube_config_file,
                                         config.kube_context, config.kube_client_configuration)

    def create_dataset(self, dataset_name: str, mount_name: str = None, mount_point: str = None, mount_path="",
                       mode="ReadOnly",
                       options=None,
                       cred_secret_name=None,
                       cred_secret_options=None, namespace=None,
                       **kwargs):
        if options is None:
            options = {}
        if cred_secret_options is None:
            cred_secret_options = {}
        if mode not in ["ReadWrite", "ReadOnly"]:
            raise ValueError("mode must be ReadOnly or ReadWrite")
        if (not cred_secret_name and len(cred_secret_options) != 0) and (
                cred_secret_name and len(cred_secret_options) == 0):
            raise ValueError("cred_secret_name and cred_secret_options must be set together")

        encrypt_options = []
        for opt_key, secret_key in cred_secret_options.items():
            encrypt_options.append(
                models.EncryptOption(opt_key, models.EncryptOptionSource(
                    models.SecretKeySelector(secret_key, cred_secret_name))))

        if (mount_name is None) != (mount_point is None):
            raise ValueError("mount_name and mount_point must be set together")

        if mount_name is None:
            mount_items = None
        else:
            mount_items = [models.Mount(
                mount_point=mount_point,
                path=mount_path,
                name=mount_name,
                options=options,
                encrypt_options=encrypt_options
            )]

        access_mode = "ReadOnlyMany" if mode == "ReadOnly" else "ReadWriteMany"

        ds = models.Dataset(
            api_version=constants.API_VERSION,
            kind=constants.DATASET_KIND,
            metadata=client.V1ObjectMeta(
                name=dataset_name,
                namespace=namespace or self.config.namespace,
            ),
            spec=models.DatasetSpec(
                mounts=mount_items,
                access_modes=[access_mode],
                **kwargs
            )
        )
        self.k8s_client.create_dataset(ds)
        logger.debug(f"Dataset \"{namespace or self.config.namespace}/{dataset_name}\" created")

    def get_dataset(self, dataset_name: str, namespace=None):
        obj = self.k8s_client.get_dataset(dataset_name, namespace or self.config.namespace)
        return FluidDataset(obj.metadata.name, obj.metadata.namespace, obj, self)

    def cleanup_dataset(self, dataset_name: str, namespace=None, wait=True):
        try:
            obj = self.k8s_client.get_dataset(dataset_name, namespace or self.config.namespace)
        except client.ApiException as e:
            if e.status == 404:
                return
        except Exception as e:
            raise e
        else:
            FluidDataset(dataset_name, obj.metadata.namespace, obj, self).clean_up(wait)


class FluidDataset(object):
    def __init__(self, name: str, namespace: str, dataset_obj: models.Dataset, client: FluidClient):
        self.name = name
        self.namespace = namespace
        self.obj = dataset_obj
        self.fluid_client = client

    def bind_runtime(self, runtime_type=None, replicas=2, cache_capacity_GiB=10, cache_medium="MEM", wait=True,
                     **kwargs):
        real_runtime_kind = utils.infer_runtime_kind(runtime_type)
        if not real_runtime_kind:
            real_runtime_kind = self.fluid_client.config.runtime_kind
            logger.warning(
                f"No runtime_type is given to bind_runtime(), implicitly using {self.fluid_client.config.runtime_kind} from FluidClient")
        assert real_runtime_kind is not None

        if real_runtime_kind == constants.ALLUXIO_RUNTIME_KIND:
            runtime = self.__default_alluxio_runtime(replicas, cache_capacity_GiB, cache_medium, **kwargs)
        elif real_runtime_kind == constants.JINDO_RUNTIME_KIND:
            runtime = self.__default_jindo_runtime(replicas, cache_capacity_GiB, cache_medium, **kwargs)
        elif real_runtime_kind == constants.JUICEFS_RUNTIME_KIND:
            runtime = self.__default_juicefs_runtime(replicas, cache_capacity_GiB, cache_medium, **kwargs)
        elif real_runtime_kind == constants.EFC_RUNTIME_KIND:
            runtime = self.__default_efc_runtime(replicas, cache_capacity_GiB, cache_medium, **kwargs)
        elif real_runtime_kind == constants.VINEYARD_RUNTIME_KIND:
            runtime = self.__default_vineyard_runtime(replicas, cache_capacity_GiB, cache_medium, **kwargs)
        else:
            raise ValueError(f"Unsupported runtime kind {real_runtime_kind}")

        ds = self.fluid_client.k8s_client.get_dataset(self.obj.metadata.name, self.obj.metadata.namespace)
        assert ds is not None
        if ds.metadata.uid != self.obj.metadata.uid:
            raise RuntimeError(f"Dataset {self.name} has a different UID, the dataset may already been cleaned up")

        self.fluid_client.k8s_client.create_runtime(runtime, namespace=self.obj.metadata.namespace)
        if wait:
            self.fluid_client.k8s_client.wait_dataset_bound(self.name, self.obj.metadata.namespace)

    def report_status(self, status_type: str = "cache"):
        pass
        available_status_type = ["mount", "cache", "binding_status", "full"]
        if status_type not in available_status_type:
            raise ValueError(f"status_type must be one of {available_status_type}")

        self.obj = self.fluid_client.k8s_client.get_dataset(self.obj.metadata.name, self.obj.metadata.namespace)
        if not self.obj.status:
            return None

        if status_type == "mount":
            return self.obj.spec.mounts
        if status_type == "cache":
            cache_states = self.obj.status.cache_states
            cache_states["dataset total size"] = self.obj.status.ufs_total or ""
            cache_states["dataset file num"] = self.obj.status.file_num or ""
            return cache_states
        if status_type == "binding_status":
            binding_status = {
                "phase": self.obj.status.phase,
                "runtimes": self.obj.status.runtimes or []
            }
            return binding_status
        if status_type == "full":
            return self.obj.status

    def clean_up(self, wait=True):
        try:
            ds = self.fluid_client.k8s_client.get_dataset(self.obj.metadata.name, self.obj.metadata.namespace)
        except client.ApiException as e:
            if e.status == 404:
                return
        else:
            if ds.metadata.uid != self.obj.metadata.uid:
                return
            try:
                self.fluid_client.k8s_client.delete_dataset(self.obj.metadata.name, self.obj.metadata.namespace,
                                                            wait_until_cleaned_up=wait)
            except TimeoutError:
                logger.warning(f"Timeout when cleaning up dataset {self.name}, there may be some pods relying on the "
                               f"dataset that blocks the deletion, please check")

    def preload(self, target_path="/", load_metadata=False):
        flow = FluidDataFlow(self.name, self.namespace)
        return flow.preload(target_path, load_metadata)

    def migrate(self, path, migrate_direction, external_storage):
        flow = FluidDataFlow(self.name, self.namespace)
        return flow.migrate(path, migrate_direction, external_storage)

    def process(self, dataset_mountpath, processor, sub_path=None):
        flow = FluidDataFlow(self.name, self.namespace)
        return flow.process(dataset_mountpath, processor, sub_path)

    def __default_alluxio_runtime(self, replicas, cache_capacity_GiB, cache_medium, **kwargs):
        runtime = models.AlluxioRuntime(
            api_version=constants.API_VERSION,
            kind=constants.ALLUXIO_RUNTIME_KIND,
            metadata=client.V1ObjectMeta(
                name=self.name,
                namespace=self.namespace,
            ),
            spec=models.AlluxioRuntimeSpec(
                replicas=replicas,
                tieredstore=models.TieredStore(
                    levels=[
                        models.Level(
                            mediumtype=cache_medium,
                            path="/var/lib/fluid/cache",
                            quota=f"{cache_capacity_GiB}Gi",
                            volume_type="emptyDir",
                            high="0.99",
                            low="0.95"
                        )
                    ]
                ),
                **kwargs
            )
        )

        return runtime

    def __default_jindo_runtime(self, replicas, cache_capacity_GiB, cache_medium, **kwargs):
        runtime = models.JindoRuntime(
            api_version=constants.API_VERSION,
            kind=constants.JINDO_RUNTIME_KIND,
            metadata=client.V1ObjectMeta(
                name=self.name,
                namespace=self.namespace,
            ),
            spec=models.JindoRuntimeSpec(
                replicas=replicas,
                tieredstore=models.TieredStore(
                    levels=[
                        models.Level(
                            mediumtype=cache_medium,
                            path="/var/lib/fluid/cache",
                            quota=f"{cache_capacity_GiB}Gi",
                            volume_type="emptyDir",
                            high="0.99",
                            low="0.95"
                        )
                    ]
                ),
                **kwargs
            )
        )

        return runtime

    def __default_juicefs_runtime(self, replicas, cache_capacity_GiB, cache_medium, **kwargs):
        runtime = models.JuiceFSRuntime(
            api_version=constants.API_VERSION,
            kind=constants.JUICEFS_RUNTIME_KIND,
            metadata=client.V1ObjectMeta(
                name=self.name,
                namespace=self.namespace,
            ),
            spec=models.JuiceFSRuntimeSpec(
                replicas=replicas,
                tieredstore=models.TieredStore(
                    levels=[
                        models.Level(
                            mediumtype=cache_medium,
                            path="/var/lib/fluid/cache",
                            quota=f"{cache_capacity_GiB}Gi",
                            volume_type="emptyDir",
                            low="0.05"
                        )
                    ]
                ),
                **kwargs
            )
        )

        return runtime

    def __default_efc_runtime(self, replicas, cache_capacity_GiB, cache_medium, **kwargs):
        runtime = models.EFCRuntime(
            api_version=constants.API_VERSION,
            kind=constants.EFC_RUNTIME_KIND,
            metadata=client.V1ObjectMeta(
                name=self.name,
                namespace=self.namespace,
            ),
            spec=models.EFCRuntimeSpec(
                replicas=replicas,
                tieredstore=models.TieredStore(
                    levels=[
                        models.Level(
                            mediumtype=cache_medium,
                            path="/var/lib/fluid/cache",
                            quota=f"{cache_capacity_GiB}Gi",
                            volume_type="emptyDir"
                        )
                    ]
                ),
                **kwargs
            )
        )
        return runtime

    def __default_vineyard_runtime(self, replicas, cache_capacity_GiB, cache_medium, **kwargs):
        runtime = models.VineyardRuntime(
            api_version=constants.API_VERSION,
            kind=constants.VINEYARD_RUNTIME_KIND,
            metadata=client.V1ObjectMeta(
                name=self.name,
                namespace=self.namespace,
            ),
            spec=models.VineyardRuntimeSpec(
                replicas=replicas,
                tieredstore=models.TieredStore(
                    levels=[
                        models.Level(
                            mediumtype=cache_medium,
                            quota=f"{cache_capacity_GiB}Gi",
                            volume_type="emptyDir",
                        )
                    ]
                ),
                **kwargs
            )
        )
        return runtime
