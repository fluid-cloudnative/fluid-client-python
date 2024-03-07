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
import time
import multiprocessing
from typing import Optional

from kubernetes import config, client

from fluid import ApiClient
from fluid import models
from fluid.constants import constants
from fluid.utils import utils

logger = logging.getLogger("FluidK8sClient")


class FluidK8sClient(object):
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

    def create_data_operation(self, data_op: constants.DATA_OPERATION_MODELS_TYPE, namespace=None, wait=False):
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

        if wait:
            self.wait_data_operation_completed(data_op.metadata.name, data_op.kind, namespace)

    def get_dataset(self, name, namespace=None, timeout=constants.DEFAULT_API_REQUEST_TIMEOUT) -> models.Dataset:
        namespace = namespace or self.namespace

        try:
            thread = self.custom_api.get_namespaced_custom_object(
                constants.GROUP,
                constants.VERSION,
                namespace,
                constants.FLUID_CRD_PARAMETERS[constants.DATASET_KIND]["plural"],
                name,
                async_req=True
            )
            response = utils.FakeResponse(thread.get(timeout=timeout))
            dataset = self.api_client.deserialize(response, models.Dataset)
        except multiprocessing.TimeoutError:
            raise TimeoutError(
                f"TimeoutError: Timed out when getting dataset \"{namespace}/{name}\""
            )
        except client.ApiException as e:
            raise e
        except Exception as e:
            raise RuntimeError(
                f"RuntimeError: Failed to get dataset \"{namespace}/{name}\": {e}"
            )
        logger.debug(f"Dataset \"{namespace}/{dataset.metadata.name}\" retrieved successfully")
        return dataset

    def get_runtime(self, name, runtime_type=None, namespace=None,
                    timeout=constants.DEFAULT_API_REQUEST_TIMEOUT) -> constants.RUNTIME_MODELS_TYPE:
        namespace = namespace or self.namespace
        runtime_kind = utils.infer_runtime_kind(runtime_type) or self.default_runtime_kind
        if runtime_kind is None:
            raise ValueError(
                f"runtime_type is not supported, supported types: {list(constants.RUNTIME_PARAMETERS.keys())}")
        try:
            thread = self.custom_api.get_namespaced_custom_object(
                constants.GROUP,
                constants.VERSION,
                namespace,
                constants.RUNTIME_PARAMETERS[runtime_kind]["plural"],
                name,
                async_req=True
            )
            response = utils.FakeResponse(thread.get(timeout=timeout))
            runtime = self.api_client.deserialize(response, constants.RUNTIME_PARAMETERS[runtime_kind]["model"])
        except multiprocessing.TimeoutError:
            raise TimeoutError(
                f"TimeoutError: Timed out when getting runtime \"{namespace}/{name}\""
            )
        except client.ApiException as e:
            raise e
        except Exception as e:
            raise RuntimeError(
                f"RuntimeError: Failed to get runtime \"{namespace}/{name}\": {e}"
            )
        logger.debug(f"{runtime.kind} \"{namespace}/{runtime.metadata.name}\" retrieved successfully")

        return runtime

    def get_data_operation(self, name, data_op_type, namespace=None, timeout=constants.DEFAULT_API_REQUEST_TIMEOUT):
        namespace = namespace or self.namespace
        data_op_kind = utils.infer_data_operation_kind(data_op_type)
        if data_op_kind is None:
            raise ValueError(
                f"data_op_type is not supported, supported types: {list(constants.DATA_OPERATION_PARAMETERS.keys())}")

        try:
            thread = self.custom_api.get_namespaced_custom_object(
                constants.GROUP,
                constants.VERSION,
                namespace,
                constants.DATA_OPERATION_PARAMETERS[data_op_kind]["plural"],
                name,
                async_req=True
            )
            response = utils.FakeResponse(thread.get(timeout=timeout))
            data_op = self.api_client.deserialize(response, constants.DATA_OPERATION_PARAMETERS[data_op_kind]["model"])
        except multiprocessing.TimeoutError:
            raise TimeoutError(
                f"TimeoutError: Timed out when getting data operation \"{namespace}/{name}\""
            )
        except client.ApiException as e:
            raise e
        except Exception as e:
            raise RuntimeError(
                f"RuntimeError: Failed to get data operation \"{namespace}/{name}\": {e}"
            )
        logger.debug(f"{data_op.kind} \"{namespace}/{data_op.metadata.name}\" retrieved successfully")
        return data_op

    def wait_data_operation_completed(self, name, data_op_type, namespace=None,
                                      poll_timeout=constants.DEFAULT_POLL_TIMEOUT,
                                      poll_interval=constants.DEFAULT_POLL_INTERVAL):
        namespace = namespace or self.namespace
        data_op_kind = utils.infer_data_operation_kind(data_op_type)

        if data_op_kind is None:
            raise ValueError(
                f"data_op_type is not supported, supported types: {list(constants.DATA_OPERATION_PARAMETERS.keys())}")

        poll = 0
        while poll < poll_timeout:
            data_op = self.get_data_operation(name, data_op_type, namespace)
            if not data_op.status:
                logger.warning(f"{data_op.kind} \"{data_op.metadata.namespace}/{data_op.metadata.name}\"'s current "
                               f"status is None, this may happen when the {data_op.kind} is just created. Temporarily"
                               f" ignoring it.")
            else:
                phase = data_op.status.phase
                logger.debug(
                    f"{data_op.kind} \"{data_op.metadata.namespace}/{data_op.metadata.name}\"'s current phase: {phase}")
                if phase == "Complete":
                    logger.debug(
                        f"{data_op.kind} \"{data_op.metadata.namespace}/{data_op.metadata.name}\" completed successfully after {data_op.status.duration}")
                    break
                if phase == "Failed":
                    logger.debug(f"{data_op.kind} \"{data_op.metadata.namespace}/{data_op.metadata.name}\" failed.")
                    raise RuntimeError(
                        f"{data_op.kind} \"{data_op.metadata.namespace}/{data_op.metadata.name}\" failed.")

            poll += poll_interval
            time.sleep(poll_interval)

        if poll >= poll_timeout:
            raise TimeoutError(f"TimeoutError: Timed out when waiting data operation \"{namespace}/{name}\"")

    def wait_dataset_bound(self, name, namespace=None, poll_timeout=constants.DEFAULT_POLL_TIMEOUT,
                           poll_interval=constants.DEFAULT_POLL_INTERVAL):
        namespace = namespace or self.namespace
        poll = 0
        while poll < poll_timeout:
            dataset = self.get_dataset(name, namespace)
            if dataset.status is not None and dataset.status.phase == "Bound":
                logger.debug(f"Dataset \"{namespace}/{name}\" bound successfully")
                break
            poll += poll_interval
            time.sleep(poll_interval)
        if poll >= poll_timeout:
            raise TimeoutError(f"TimeoutError: Timed out when waiting dataset \"{namespace}/{name}\" bound")

    def delete_dataset(self, name, namespace=None, wait_until_cleaned_up=False,
                       timeout=constants.DEFAULT_API_REQUEST_TIMEOUT,
                       **kwargs):
        namespace = namespace or self.namespace

        runtime_type = None
        obj = self.get_dataset(name, namespace)
        if len(obj.status.runtimes) > 0:
            # For now, Fluid only supports one bounded runtime
            runtime_type = utils.infer_runtime_kind(obj.status.runtimes[0].type)

        try:
            self.custom_api.delete_namespaced_custom_object(
                constants.GROUP,
                constants.VERSION,
                namespace,
                constants.FLUID_CRD_PARAMETERS[constants.DATASET_KIND]["plural"],
                name,
                **kwargs
            )
        except multiprocessing.TimeoutError:
            raise TimeoutError(
                f"TimeoutError: Timed out when deleting dataset \"{namespace}/{name}\""
            )
        except client.ApiException as e:
            if e.status == 404:
                logger.warning(f"Dataset \"{namespace}/{name}\" not found. Maybe already deleted.")
        except Exception as e:
            raise RuntimeError(f"Failed to delete dataset \"{namespace}/{name}\": {e}.")

        if wait_until_cleaned_up:
            poll = 0
            while poll < timeout:
                try:
                    self.get_dataset(name, namespace)
                    poll += 1
                    time.sleep(1)
                except client.ApiException as e:
                    if e.status == 404:
                        break

            if poll >= timeout:
                raise TimeoutError(f"TimeoutError: Timed out when waiting dataset \"{namespace}/{name}\" deleted")

        logger.debug(f"Dataset \"{namespace}/{name}\" deleted successfully")

        if wait_until_cleaned_up:
            self.delete_runtime(name, runtime_type=runtime_type, namespace=namespace,
                                wait_until_cleaned_up=wait_until_cleaned_up, timeout=timeout, **kwargs)

    def delete_runtime(self, name, runtime_type=None, namespace=None, wait_until_cleaned_up=False,
                       timeout=constants.DEFAULT_API_REQUEST_TIMEOUT, **kwargs):
        namespace = namespace or self.namespace
        runtime_kind = utils.infer_runtime_kind(runtime_type) or self.default_runtime_kind
        if runtime_kind is None:
            raise ValueError(
                f"runtime_type is not supported, supported types: {list(constants.RUNTIME_PARAMETERS.keys())}")

        try:
            self.custom_api.delete_namespaced_custom_object(
                constants.GROUP,
                constants.VERSION,
                namespace,
                constants.RUNTIME_PARAMETERS[runtime_kind]["plural"],
                name,
                **kwargs
            )
        except multiprocessing.TimeoutError:
            raise TimeoutError(
                f"TimeoutError: Timed out when deleting runtime \"{namespace}/{name}\""
            )
        except client.ApiException as e:
            if e.status == 404:
                logger.warning(f"{runtime_kind} \"{namespace}/{name}\" not found. Maybe already deleted.")
        except Exception:
            raise RuntimeError(f"Failed to delete runtime \"{namespace}/{name}\".")

        if wait_until_cleaned_up:
            poll = 0
            while poll < timeout:
                try:
                    self.get_runtime(name, runtime_type=runtime_kind, namespace=namespace)
                    poll += 1
                    time.sleep(1)
                except client.ApiException as e:
                    if e.status == 404:
                        break
            if poll >= timeout:
                raise TimeoutError(f"TimeoutError: Timed out when waiting runtime \"{namespace}/{name}\" deleted")

        logger.debug(f"{runtime_kind} \"{namespace}/{name}\" deleted successfully")

    def delete_data_operation(self, name, data_op_type, namespace=None, **kwargs):
        namespace = namespace or self.namespace
        data_op_kind = utils.infer_data_operation_kind(data_op_type)
        if data_op_kind is None:
            raise ValueError(
                f"data_op_type is not supported, supported types: {list(constants.DATA_OPERATION_PARAMETERS.keys())}")

        try:
            self.custom_api.delete_namespaced_custom_object(
                constants.GROUP,
                constants.VERSION,
                namespace,
                constants.DATA_OPERATION_PARAMETERS[data_op_kind]["plural"],
                name,
                **kwargs
            )
        except multiprocessing.TimeoutError:
            raise TimeoutError(
                f"TimeoutError: Timed out when deleting data operation \"{namespace}/{name}\""
            )
        except client.ApiException as e:
            if e.status == 404:
                logger.warning(f"{data_op_kind} \"{namespace}/{name}\" not found. Maybe already deleted.")
        except Exception:
            raise RuntimeError(f"Failed to delete data operation \"{namespace}/{name}\".")
        logger.debug(f"{data_op_kind} \"{namespace}/{name}\" deleted successfully")
