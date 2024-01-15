import logging
import sys

from kubernetes import client

from fluid import FluidK8sClient, FluidClient, ClientConfig
from fluid import constants
from fluid import models

logger = logging.getLogger("")


def init_logger(logger_name, logger_level):
    global logger
    logger = logging.getLogger(logger_name)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(stream_handler)
    logger.setLevel(logger_level)


# Example for data experts like data scientists and data engineers.
def main():
    global logger
    init_logger("fluidsdk", logging.INFO)

    client_config = ClientConfig()
    fluid_client = FluidClient(client_config)

    dataset_name = "demo"
    try:
        fluid_client.create_dataset(dataset_name, "https://mirrors.bit.edu.cn/apache/hbase/stable/", "/hbase")
    except Exception as e:
        raise RuntimeError("f""Failed to create dataset: {e}")

    logger.info(f"Dataset \"{dataset_name}\" created successfully")

    try:
        dataset = fluid_client.get_dataset(dataset_name)
    except Exception as e:
        raise RuntimeError(f"Failed to get dataset: {e}")

    logger.info(f"Binding AlluxioRuntime to dataset \"{dataset_name}\"...")
    dataset.bind_runtime(runtime_type="alluxio", replicas=1, cache_medium="MEM", cache_capacity_GiB=2, wait=True)
    logger.info(f"AlluxioRuntime created and bound to dataset \"{dataset_name}\", cache engine is now ready")


# Example for Kubernetes experts who is familiar with YAML-like APIs.
def main_k8s_client():
    global logger
    init_logger("FluidK8sClient", logging.INFO)

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
    # main_k8s_client()
