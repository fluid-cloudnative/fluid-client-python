import logging
import sys

from fluid import models
from fluid import FluidK8sClient, FluidClient, ClientConfig

logger = logging.getLogger("fluidsdk")
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

# Output detailed debug message for fluidsdk
# logger.setLevel(logging.DEBUG)

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
        dataset = fluid_client.get_dataset(dataset_name)
    except Exception as e:
        raise RuntimeError(f"Error when getting dataset \"{dataset_name}\": {e}")
    else:
        print(f"Dataset's cache status is:\n{dataset.report_status()}\n")  # default status_type is 'cache'
        print(f"Dataset's mount status is:\n{dataset.report_status(status_type='mount')}\n")
        print(f"Dataset's binding status is:\n{dataset.report_status(status_type='binding_status')}\n")
        print(f"Dataset's full status:\n{dataset.report_status(status_type='full')}\n")


# Example for Kubernetes experts who is familiar with YAML-like APIs.
def main_k8s_client():
    global logger
    init_logger("FluidK8sClient", logging.INFO)

    namespace = "default"
    name = "demo"

    fluid_client = FluidK8sClient()
    try:
        dataset = fluid_client.get_dataset(name, namespace)
    except Exception as e:
        raise RuntimeError(f"Error when getting dataset \"{namespace}/{name}\": {e}")

    assert type(dataset) == models.Dataset
    logger.info(f"Dataset \"{namespace}/{name}\"'s phase is: {dataset.status.phase}")

    try:
        runtime = fluid_client.get_runtime(name, "alluxio", namespace)
    except Exception as e:
        raise RuntimeError(f"Error when getting runtime \"{namespace}/{name}\": {e}")
    assert type(runtime) == models.AlluxioRuntime
    logger.info(f"AlluxioRuntime \"{namespace}/{name}\"'s Master Phase is: {runtime.status.master_phase}")
    logger.info(f"AlluxioRuntime \"{namespace}/{name}\"'s Worker Phase is: {runtime.status.worker_phase}")
    logger.info(f"AlluxioRuntime \"{namespace}/{name}\"'s Fuse Phase is: {runtime.status.fuse_phase}")


if __name__ == '__main__':
    main()
    # main_k8s_client()
