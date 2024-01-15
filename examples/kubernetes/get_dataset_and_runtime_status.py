import logging
import sys

from fluid import models
from fluid import FluidK8sClient

logger = logging.getLogger("fluidsdk")
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

# Output detailed debug message for fluidsdk
# logger.setLevel(logging.DEBUG)

namespace = "default"
name = "demo"


def main():
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
