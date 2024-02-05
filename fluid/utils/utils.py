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
import os
import json

from typing import Optional

from kubernetes import client

from fluid import constants


def is_running_in_k8s():
    return os.path.isdir("/var/run/secrets/kubernetes.io/")


def get_default_target_namespace():
    if not is_running_in_k8s():
        return "default"
    with open("/var/run/secrets/kubernetes.io/serviceaccount/namespace", "r") as f:
        return f.readline()


def get_obj_namespace(obj: client.V1ObjectMeta):
    if not isinstance(obj, client.V1ObjectMeta):
        raise ValueError("object is not of type kubernetes.client.V1ObjectMeta")

    if obj.namespace and len(obj.namespace) != 0:
        return obj.namespace

    return None


def infer_data_operation_kind(data_op_type: str) -> Optional[str]:
    if not data_op_type:
        return None

    data_op_type = data_op_type.lower()
    data_op_mapping = {
        "dataload": constants.DATA_LOAD_KIND,
        "dataloads": constants.DATA_LOAD_KIND,
        "datamigrate": constants.DATA_MIGRATE_KIND,
        "datamigrates": constants.DATA_MIGRATE_KIND,
        "dataprocess": constants.DATA_PROCESS_KIND,
        "dataprocesses": constants.DATA_PROCESS_KIND,
    }

    if data_op_type not in data_op_mapping:
        return None
    return data_op_mapping[data_op_type]


def infer_runtime_kind(runtime_type: str) -> Optional[str]:
    if not runtime_type:
        return None

    runtime_type = runtime_type.lower()

    runtime_mapping = {
        # infer alluxio
        "alluxio": constants.ALLUXIO_RUNTIME_KIND,
        "alluxioruntime": constants.ALLUXIO_RUNTIME_KIND,
        "alluxioruntimes": constants.ALLUXIO_RUNTIME_KIND,
        # infer jindo
        "jindo": constants.JINDO_RUNTIME_KIND,
        "jindofs": constants.JINDO_RUNTIME_KIND,
        "jindofsx": constants.JINDO_RUNTIME_KIND,
        "jindocache": constants.JINDO_RUNTIME_KIND,
        "jindoruntime": constants.JINDO_RUNTIME_KIND,
        "jindoruntimes": constants.JINDO_RUNTIME_KIND,
        # infer juicefs
        "juice": constants.JUICEFS_RUNTIME_KIND,
        "juicefs": constants.JUICEFS_RUNTIME_KIND,
        "juicefsruntime": constants.JUICEFS_RUNTIME_KIND,
        "juicefsruntimes": constants.JUICEFS_RUNTIME_KIND,
        # infer efc
        "efc": constants.EFC_RUNTIME_KIND,
        "efcruntime": constants.EFC_RUNTIME_KIND,
        "efcruntimes": constants.EFC_RUNTIME_KIND,
        # infer thin
        "thin": constants.THIN_RUNTIME_KIND,
        "thinruntime": constants.THIN_RUNTIME_KIND,
        "thinruntimes": constants.THIN_RUNTIME_KIND,
        # infer vineyard
        "vineyard": constants.VINEYARD_RUNTIME_KIND,
        "vineyardruntime": constants.VINEYARD_RUNTIME_KIND,
        "vineyardruntimes": constants.VINEYARD_RUNTIME_KIND,
    }

    if runtime_type not in runtime_mapping:
        return None

    return runtime_mapping[runtime_type]


# Credit to https://github.com/kubeflow/training-operator/blob/master/sdk/python/kubeflow/training/utils/utils.py to
# make deserialization work
class FakeResponse:
    """Fake object of RESTResponse to deserialize
    Ref) https://github.com/kubeflow/katib/pull/1630#discussion_r697877815
    Ref) https://github.com/kubernetes-client/python/issues/977#issuecomment-592030030
    """

    def __init__(self, obj):
        self.data = json.dumps(obj)
