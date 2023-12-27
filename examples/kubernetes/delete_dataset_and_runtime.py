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
import sys

from fluid import FluidClient
from fluid import constants

logger = logging.getLogger("fluidsdk")
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

# Output detailed debug message for fluidsdk
# logger.setLevel(logging.DEBUG)


def main():
    # Set default_runtime_kind to enable wait_until_cleaned_up=True when deleting dataset
    fluid_client = FluidClient(default_runtime_kind=constants.ALLUXIO_RUNTIME_KIND)

    name = "demo"
    namespace = "default"

    try:
        # Recommend using wait_until_cleaned_up=True wait for clean-up for the dataset and the bound Runtime.
        fluid_client.delete_dataset(name, namespace, wait_until_cleaned_up=True)
        # Dataset deletion cascades deletion of the bound Runtime and any other related Data Operations,
        # So you don't have to explicitly delete the Runtime at most cases.
        # fluid_client.delete_runtime(name, runtime_type=constants.ALLUXIO_RUNTIME_KIND, namespace=namespace, wait_until_cleaned_up=True)
    except Exception as e:
        raise RuntimeError(f"Failed to delete dataset: {e}")

    logger.info(f"Dataset \"{namespace}/{name}\" and Runtime \"{namespace}/{name}\" deleted successfully")


if __name__ == '__main__':
    main()
