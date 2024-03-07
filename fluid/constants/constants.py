# Copyright 2023 Fluid Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Union

from fluid import models

# ------ Common Contants -------
DEFAULT_API_REQUEST_TIMEOUT = 300
DEFAULT_POLL_TIMEOUT = 600
DEFAULT_POLL_INTERVAL = 3
DEFAULT_DATAFLOW_TIME_TO_LIVE = 86400 * 3  # 3 days

# ------ Fluid Types -------
GROUP = "data.fluid.io"
VERSION = "v1alpha1"
API_VERSION = f"{GROUP}/{VERSION}"

DATASET_KIND = "Dataset"
DATASET_PLURAL = "datasets"

ALLUXIO_RUNTIME_KIND = "AlluxioRuntime"
ALLUXIO_RUNTIME_PLURAL = "alluxioruntimes"
JINDO_RUNTIME_KIND = "JindoRuntime"
JINDO_RUNTIME_PLURAL = "jindoruntimes"
JUICEFS_RUNTIME_KIND = "JuiceFSRuntime"
JUICEFS_RUNTIME_PLURAL = "juicefsruntimes"
EFC_RUNTIME_KIND = "EFCRuntime"
EFC_RUNTIME_PLURAL = "efcruntimes"
THIN_RUNTIME_KIND = "ThinRuntime"
THIN_RUNTIME_PLURAL = "thinruntimes"
THIN_RUNTIME_PROFILE_KIND = "ThinRuntimeProfile"
THIN_RUNTIME_PROFILE_PLURAL = "thinruntimeprofiles"
VINEYARD_RUNTIME_KIND = "VineyardRuntime"
VINEYARD_RUNTIME_PLURAL = "vineyardruntimes"

RUNTIME_PARAMETERS = {
    ALLUXIO_RUNTIME_KIND: {
        "plural": ALLUXIO_RUNTIME_PLURAL,
        "model": models.AlluxioRuntime
    },
    JINDO_RUNTIME_KIND: {
        "plural": JINDO_RUNTIME_PLURAL,
        "model": models.JindoRuntime
    },
    JUICEFS_RUNTIME_KIND: {
        "plural": JUICEFS_RUNTIME_PLURAL,
        "model": models.JuiceFSRuntime
    },
    EFC_RUNTIME_KIND: {
        "plural": EFC_RUNTIME_PLURAL,
        "model": models.EFCRuntime
    },
    THIN_RUNTIME_KIND: {
        "plural": THIN_RUNTIME_PLURAL,
        "model": models.ThinRuntime
    },
    VINEYARD_RUNTIME_KIND: {
        "plural": VINEYARD_RUNTIME_PLURAL,
        "model": models.VineyardRuntime
    }
}

RUNTIME_MODELS = tuple(x["model"] for x in list(RUNTIME_PARAMETERS.values()))
RUNTIME_MODELS_TYPE = Union[
    models.AlluxioRuntime,
    models.JindoRuntime,
    models.JuiceFSRuntime,
    models.EFCRuntime,
    models.ThinRuntime,
    models.VineyardRuntime
]

DATA_LOAD_KIND = "DataLoad"
DATA_LOAD_PLURAL = "dataloads"
DATA_MIGRATE_KIND = "DataMigrate"
DATA_MIGRATE_PLURAL = "datamigrates"
DATA_PROCESS_KIND = "DataProcess"
DATA_PROCESS_PLURAL = "dataprocesses"

DATA_OPERATION_PARAMETERS = {
    DATA_LOAD_KIND: {
        "plural": DATA_LOAD_PLURAL,
        "model": models.DataLoad
    },
    DATA_MIGRATE_KIND: {
        "plural": DATA_MIGRATE_PLURAL,
        "model": models.DataMigrate
    },
    DATA_PROCESS_KIND: {
        "plural": DATA_PROCESS_PLURAL,
        "model": models.DataProcess
    }
}

DATA_OPERATION_MODELS = tuple(x["model"] for x in list(DATA_OPERATION_PARAMETERS.values()))
DATA_OPERATION_MODELS_TYPE = Union[
    models.DataLoad,
    models.DataMigrate,
    models.DataProcess
]

FLUID_CRD_PARAMETERS = {
    DATASET_KIND: {
        "plural": DATASET_PLURAL
    },

    THIN_RUNTIME_PROFILE_KIND: {
        "plural": THIN_RUNTIME_PROFILE_PLURAL
    },
}

for kind, params in RUNTIME_PARAMETERS.items():
    FLUID_CRD_PARAMETERS[kind] = params

for kind, params in DATA_OPERATION_PARAMETERS.items():
    FLUID_CRD_PARAMETERS[kind] = params

# ------ DataMigrate Constants ------
DATA_MIGRATE_DIRECTION_FROM = "from"
DATA_MIGRATE_DIRECTION_TO = "to"
