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

DATA_LOAD_KIND = "DataLoad"
DATA_LOAD_PLURAL = "dataloads"
DATA_MIGRATE_KIND = "DataMigrate"
DATA_MIGRATE_PLURAL = "datamigrates"
DATA_PROCESS_KIND = "DataProcess"
DATA_PROCESS_PLURAL = "dataprocesses"


FLUID_CRD_PARAMETERS = {
    DATASET_KIND: {
        "plural": DATASET_PLURAL
    },
    ALLUXIO_RUNTIME_KIND: {
        "plural": ALLUXIO_RUNTIME_PLURAL
    },
    JINDO_RUNTIME_KIND: {
        "plural": JINDO_RUNTIME_PLURAL
    },
    JUICEFS_RUNTIME_KIND: {
        "plural": JUICEFS_RUNTIME_PLURAL
    },
    EFC_RUNTIME_KIND: {
        "plural": EFC_RUNTIME_PLURAL
    },
    THIN_RUNTIME_KIND: {
        "plural": THIN_RUNTIME_PLURAL
    },
    THIN_RUNTIME_PROFILE_KIND: {
        "plural": THIN_RUNTIME_PROFILE_PLURAL
    },
    DATA_LOAD_KIND: {
        "plural": DATA_LOAD_PLURAL
    },
    DATA_MIGRATE_KIND: {
        "plural": DATA_MIGRATE_PLURAL
    },
    DATA_PROCESS_KIND: {
        "plural": DATA_PROCESS_PLURAL
    }
}