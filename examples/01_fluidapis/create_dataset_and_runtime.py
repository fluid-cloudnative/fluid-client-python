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


def create_dataset_with_alluxio(fluid_client: FluidClient):
    dataset_name = "demo"
    try:
        # Mounting WebUFS to Alluxio
        fluid_client.create_dataset(dataset_name, "hbase", "https://mirrors.tuna.tsinghua.edu.cn/apache/hbase/stable/", "/")
    except Exception as e:
        raise RuntimeError(f"Failed to create dataset: {e}")

    logger.info(f"Dataset \"{dataset_name}\" created successfully")

    try:
        dataset = fluid_client.get_dataset(dataset_name)
    except Exception as e:
        raise RuntimeError(f"Failed to get dataset: {e}")

    logger.info(f"Binding AlluxioRuntime to dataset \"{dataset_name}\"...")
    dataset.bind_runtime(runtime_type="alluxio", replicas=1, cache_medium="MEM", cache_capacity_GiB=2, wait=True)
    logger.info(f"AlluxioRuntime created and bound to dataset \"{dataset_name}\", cache engine is now ready")


def create_dataset_with_jindofs(fluid_client: FluidClient):
    dataset_name = "demo"
    try:
        # Mounting OSS Bucket to Jindo
        fluid_client.create_dataset(dataset_name,
                                    "mybucket", "oss://mybucket/subdir", "/",
                                    options={"fs.oss.endpoint": "oss-cn-beijing-internal.aliyuncs.com"},
                                    cred_secret_name="access-key",
                                    cred_secret_options={
                                        "fs.oss.accessKeyId": "fs.oss.accessKeyId",
                                        "fs.oss.accessKeySecret": "fs.oss.accessKeySecret"
                                    })
    except Exception as e:
        raise RuntimeError("f""Failed to create dataset: {e}")

    logger.info(f"Dataset \"{dataset_name}\" created successfully")

    try:
        dataset = fluid_client.get_dataset(dataset_name)
    except Exception as e:
        raise RuntimeError(f"Failed to get dataset: {e}")

    logger.info(f"Binding JindoRuntime to dataset \"{dataset_name}\"...")
    dataset.bind_runtime(runtime_type="jindo", replicas=1, cache_medium="MEM", cache_capacity_GiB=2, wait=True)
    logger.info(f"JindoRuntime created and bound to dataset \"{dataset_name}\", cache engine is now ready")


def create_dataset_with_juicefs(fluid_client: FluidClient):
    dataset_name = "demo"
    try:
        # Setting minio as JuiceFS's backend storage and redis as JuiceFS's meta server
        fluid_client.create_dataset(dataset_name,
                                    "minio", "juicefs:///", "/",
                                    options={"bucket": "http://minio:9000/minio/test", "storage": "minio"},
                                    cred_secret_name="jfs-secret",
                                    cred_secret_options={
                                        "metaurl": "metaurl",
                                        "access-key": "access-key",
                                        "secret-key": "secret-key"
                                    })
    except Exception as e:
        raise RuntimeError("f""Failed to create dataset: {e}")

    logger.info(f"Dataset \"{dataset_name}\" created successfully")

    try:
        dataset = fluid_client.get_dataset(dataset_name)
    except Exception as e:
        raise RuntimeError(f"Failed to get dataset: {e}")

    logger.info(f"Binding JuiceFSRuntime to dataset \"{dataset_name}\"...")
    dataset.bind_runtime(runtime_type="juicefs", replicas=1, cache_medium="MEM", cache_capacity_GiB=2, wait=True)
    logger.info(f"JuiceFSRuntime created and bound to dataset \"{dataset_name}\", cache engine is now ready")


def create_dataset_with_vineyard(fluid_client: FluidClient):
    dataset_name = "vineyard"
    try:
        fluid_client.create_dataset(dataset_name)
    except Exception as e:
        raise RuntimeError("f""Failed to create dataset: {e}")

    logger.info(f"Dataset \"{dataset_name}\" created successfully")

    try:
        dataset = fluid_client.get_dataset(dataset_name)
    except Exception as e:
        raise RuntimeError(f"Failed to get dataset: {e}")

    logger.info(f"Binding VineyardRuntime to dataset \"{dataset_name}\"...")
    dataset.bind_runtime(runtime_type="vineyard", replicas=1, cache_medium="MEM", cache_capacity_GiB=2, wait=True)
    logger.info(f"VineyardRuntime created and bound to dataset \"{dataset_name}\", cache engine is now ready")


# Examples for data experts like data scientists and data engineers.
def main():
    global logger
    init_logger("fluidsdk", logging.INFO)

    client_config = ClientConfig()
    fluid_client = FluidClient(client_config)

    cases = {
        "alluxio": create_dataset_with_alluxio,
        "jindofs": create_dataset_with_jindofs,
        "juicefs": create_dataset_with_juicefs,
        "vineyard": create_dataset_with_vineyard
    }

    # Change case_name to play with different cache engines
    case_name = "alluxio"
    cases[case_name](fluid_client)


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
                    mount_point="https://mirrors.tuna.tsinghua.edu.cn/apache/hbase/stable/",
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
                        volume_type="emptyDir",
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
