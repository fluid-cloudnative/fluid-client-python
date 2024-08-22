import logging
import sys

from kubernetes import client

from fluid import FluidK8sClient
from fluid import constants
from fluid import models

logger = logging.getLogger("fluidsdk")
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


# Output detailed debug message for fluidsdk
# logger.setLevel(logging.DEBUG)


def create_dataload():
    fluid_client = FluidK8sClient()

    dataload = models.DataLoad(
        api_version=constants.API_VERSION,
        kind=constants.DATA_LOAD_KIND,
        metadata=client.V1ObjectMeta(
            namespace="default",
            name="demo-dataload"
        ),
        spec=models.DataLoadSpec(
            load_metadata=True,
            dataset=models.TargetDataset(
                namespace="default",
                name="demo"
            ),
            target=[
                models.TargetPath(path="/", replicas=1),
            ]
        )
    )

    try:
        fluid_client.create_data_operation(dataload)
    except Exception as e:
        raise RuntimeError(f"Error when creating DataLoad: {e}")

    logger.info(f"DataLoad \"{dataload.metadata.namespace}/{dataload.metadata.name}\" created.")


def create_dataload_and_wait_for_completion():
    fluid_client = FluidK8sClient()

    dataload = models.DataLoad(
        api_version=constants.API_VERSION,
        kind=constants.DATA_LOAD_KIND,
        metadata=client.V1ObjectMeta(
            namespace="default",
            name="demo-dataload-wait"
        ),
        spec=models.DataLoadSpec(
            load_metadata=True,
            dataset=models.TargetDataset(
                namespace="default",
                name="demo"
            ),
            target=[
                models.TargetPath(path="/", replicas=1),
            ]
        )
    )

    try:
        fluid_client.create_data_operation(dataload, wait=True)
    except Exception as e:
        raise RuntimeError(f"Error when creating DataLoad: {e}")

    logger.info(f"DataLoad \"{dataload.metadata.namespace}/{dataload.metadata.name}\" created and succeeded")


if __name__ == '__main__':
    # create_dataload()
    create_dataload_and_wait_for_completion()
