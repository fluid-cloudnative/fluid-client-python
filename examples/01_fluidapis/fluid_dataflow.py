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

from fluid import constants
from fluid import models
from fluid import FluidClient, ClientConfig

logger = logging.getLogger("fluidsdk")
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


# Output detailed debug message for fluidsdk
# logger.setLevel(logging.DEBUG)


def get_encrypt_options():
    # Replace the following with your own secret references
    encrypt_options = []
    encrypt_options.append(models.EncryptOption(
        name="access-key",
        value_from=models.EncryptOptionSource(
            secret_key_ref=models.SecretKeySelector(
                name="<SECRET_NAME>",
                key="access-key"
            )
        )
    ))
    encrypt_options.append(models.EncryptOption(
        name="secret-key",
        value_from=models.EncryptOptionSource(
            secret_key_ref=models.SecretKeySelector(
                name="<SECRET_NAME>",
                key="secret-key"
            )
        )
    ))
    return encrypt_options


def build_data_processor():
    # Replace the following with a real data processor
    return models.Processor(
        script=models.ScriptProcessor(
            image="alpine",
            image_pull_policy="IfNotPresent",
            image_tag="3.10",
            command=["sh"],
            source="""
            size=$(du -sh /data)
            echo "Total size of /data is $size"
            """
        )
    )


def main():
    # Initialize Fluid client
    fluid_client = FluidClient(ClientConfig())
    # Get a bound dataset for later operations and dataflow
    dataset = fluid_client.get_dataset("demo-dataset")

    # Flow example 1: simply preload a dataset
    dataset.preload("/").run(run_id="testflow1")

    # Flow example 2: preload a dataset, process it, and return a flow handle to get its status.
    flow2 = dataset.preload("/mydata").process(dataset_mountpath="/data", processor=build_data_processor()).run(
        run_id="testflow2")
    for op_status in flow2.get_current_status():
        print(op_status)

    # Flow example 3: migrate some data to the dataset, preload it and finally process it.
    # The following code waits until the flow is completed.
    # After 24 hours, all the operations in the flow will be automatically garbage collected.
    flow3 = dataset \
        .migrate("/ossdata", constants.DATA_MIGRATE_DIRECTION_FROM,
                 models.ExternalStorage(uri="oss://my-bucket/my-data", encrypt_options=get_encrypt_options())) \
        .preload("/ossdata") \
        .process(dataset_mountpath="/data", processor=build_data_processor()) \
        .run(run_id="testflow3", ttl_seconds_after_finished=86400)
    flow3.wait()


if __name__ == '__main__':
    main()
