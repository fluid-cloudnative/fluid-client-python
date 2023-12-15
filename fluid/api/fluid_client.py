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
import logging
import multiprocessing
from typing import Optional

from kubernetes import config, client

from fluid import ApiClient
from fluid import models
from fluid.constants import constants
from fluid.utils import utils

logger = logging.getLogger("fluidsdk")


class FluidClient(object):
    def __init__(
            self,
            namespace: str = utils.get_default_target_namespace(),
            default_runtime_kind: str = constants.ALLUXIO_RUNTIME_KIND,
            kube_config_file: Optional[str] = None,
            kube_context: Optional[str] = None,
            kube_client_configuration: Optional[client.Configuration] = None
    ):
        if kube_config_file or not utils.is_running_in_k8s():
            config.load_kube_config(config_file=kube_config_file, context=kube_context)
        else:
            config.load_incluster_config()

        k8s_client = client.ApiClient(kube_client_configuration)
        self.custom_api = client.CustomObjectsApi(k8s_client)
        self.api_client = ApiClient()

        self.namespace = namespace
        if default_runtime_kind not in constants.RUNTIME_PARAMETERS:
            raise ValueError(
                f"Default runtime kind must be one of {list(constants.RUNTIME_PARAMETERS.keys())}"
            )
        self.default_runtime_kind = default_runtime_kind

    def create_dataset(self, dataset: models.Dataset, namespace=None):
        if not dataset:
            raise ValueError(f"dataset must be not None")

        if not isinstance(dataset, models.Dataset):
            raise ValueError(f"dataset must be of type models.Dataset")

        namespace = namespace or utils.get_obj_namespace(dataset.metadata) or self.namespace

        try:
            self.custom_api.create_namespaced_custom_object(
                constants.GROUP,
                constants.VERSION,
                namespace,
                constants.FLUID_CRD_PARAMETERS[constants.DATASET_KIND]["plural"],
                body=dataset
            )
        except multiprocessing.TimeoutError:
            raise TimeoutError(
                f"TimeoutError: Timed out when creating dataset \"{namespace}/{dataset.metadata.name}\""
            )
        except Exception as e:
            raise RuntimeError(
                f"RuntimeError: Failed to create dataset \"{namespace}/{dataset.metadata.name}\": {e}"
            )

        logger.debug(f"Dataset \"{namespace}/{dataset.metadata.name}\" created successfully")

    def create_runtime(self, runtime: constants.RUNTIME_MODELS_TYPE, namespace=None):
        if not runtime:
            raise ValueError(f"runtime must be not None")

        if not isinstance(runtime, constants.RUNTIME_MODELS):
            raise ValueError(f"runtime must be one of the types: {constants.RUNTIME_MODELS}")

        namespace = namespace or utils.get_obj_namespace(runtime.metadata) or self.namespace
        kind = runtime.kind or self.default_runtime_kind
        try:
            self.custom_api.create_namespaced_custom_object(
                constants.GROUP,
                constants.VERSION,
                namespace,
                constants.RUNTIME_PARAMETERS[kind]["plural"],
                body=runtime
            )
        except multiprocessing.TimeoutError:
            raise TimeoutError(
                f"TimeoutError: Timed out when creating runtime \"{namespace}/{runtime.metadata.name}\""
            )
        except Exception as e:
            raise RuntimeError(
                f"RuntimeError: Failed to create runtime \"{namespace}/{runtime.metadata.name}\": {e}"
            )

        logger.debug(f"{runtime.kind} \"{namespace}/{runtime.metadata.name}\" created successfully")

    def create_data_operation(self, data_op: constants.DATA_OPERATION_MODELS_TYPE, namespace=None):
        if not data_op:
            raise ValueError(f"data_op must be not None")
        if not isinstance(data_op, constants.DATA_OPERATION_MODELS):
            raise ValueError(f"data_op must be one of the types: {constants.DATA_OPERATION_MODELS}")
        if not data_op.kind or len(data_op.kind) == 0:
            raise ValueError(f"data_op.kind must be not None")

        namespace = namespace or utils.get_obj_namespace(data_op.metadata) or self.namespace
        kind = data_op.kind

        try:
            self.custom_api.create_namespaced_custom_object(
                constants.GROUP,
                constants.VERSION,
                namespace,
                constants.DATA_OPERATION_PARAMETERS[kind]["plural"],
                body=data_op
            )
        except multiprocessing.TimeoutError:
            raise TimeoutError(
                f"TimeoutError: Timed out when creating data operation \"{namespace}/{data_op.metadata.name}\""
            )
        except Exception as e:
            raise RuntimeError(
                f"RuntimeError: Failed to create data operation \"{namespace}/{data_op.metadata.name}\": {e}"
            )

        logger.debug(f"{data_op.kind} \"{namespace}/{data_op.metadata.name}\" created successfully")

    def get_dataset_status(self, name, namespace=None):
        pass

    def get_runtime_status(self, name, runtime_type, namespace=None):
        pass

    def get_data_operation_status(self, name, data_op_type, namespace=None):
        pass

    def delete(self, name, namespace=None, version=constants.VERSION):
        pass
