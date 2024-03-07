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

import fluid
from fluid import constants
from fluid import models

client_config = fluid.ClientConfig()
fluid_client = fluid.FluidClient(client_config)

fluid_client.create_dataset(dataset_name="vineyard")

dataset = fluid_client.get_dataset(dataset_name="vineyard")

dataset.bind_runtime(
    runtime_type=constants.VINEYARD_RUNTIME_KIND,
    replicas=2,
    cache_capacity_GiB=30,
    cache_medium="MEM",
    wait=True
)
