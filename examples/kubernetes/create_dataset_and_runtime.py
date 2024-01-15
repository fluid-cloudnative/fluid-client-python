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

def main():
    fluid_client = FluidK8sClient()

    dataset = models.Dataset(
        api_version=constants.API_VERSION,
        kind=constants.DATASET_KIND,
        metadata=client.V1ObjectMeta(
            name="demo",
            namespace="default"
        ),
        spec=models.DatasetSpec(
            mounts=[
                models.Mount(
                    mount_point="https://mirrors.bit.edu.cn/apache/hbase/stable/",
                    name="hbase",
                    path="/",
                )
            ]
        )
    )

    try:
        fluid_client.create_dataset(dataset)
    except Exception as e:
        raise RuntimeError(f"Failed to create dataset: {e}")

    logger.info(f"Dataset \"{dataset.metadata.namespace}/{dataset.metadata.name}\" created successfully")

    alluxio_runtime = models.AlluxioRuntime(
        api_version=constants.API_VERSION,
        kind=constants.ALLUXIO_RUNTIME_KIND,
        metadata=client.V1ObjectMeta(
            name="demo",
            namespace="default"
        ),
        spec=models.AlluxioRuntimeSpec(
            replicas=1,
            tieredstore=models.TieredStore(
                levels=[
                    models.Level(
                        mediumtype="MEM",
                        volume_type="hostPath",
                        path="/dev/shm",
                        quota="2Gi",
                        high="0.95",
                        low="0.7"
                    ),
                ]
            )
        )
    )

    try:
        fluid_client.create_runtime(alluxio_runtime)
    except Exception as e:
        raise RuntimeError(f"Failed to create AlluxioRuntime: {e}")

    logger.info(
        f"AlluxioRuntime \"{alluxio_runtime.metadata.namespace}/{alluxio_runtime.metadata.name}\" created successfully")


if __name__ == '__main__':
    main()
