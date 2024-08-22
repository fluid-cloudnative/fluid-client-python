# Fluid Python SDK
Fluid SDK in Python

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

## Requirements.
- Python >= 3.7

## Installation & Usage
### pip install

```sh
pip install git+https://github.com/fluid-cloudnative/fluid-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/fluid-cloudnative/fluid-client-python.git`)

Then import the package:
```python
import fluid
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import fluid
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

The following is a code sample which creates a dataset and get its status.

```python
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

    name = "demo"
    namespace = "default"

    dataset = models.Dataset(
        api_version=constants.API_VERSION,
        kind=constants.DATASET_KIND,
        metadata=client.V1ObjectMeta(
            name=name,
            namespace=namespace
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

    try:
        dataset = fluid_client.get_dataset(name, namespace)
    except Exception as e:
        raise RuntimeError(f"Error when getting dataset \"{namespace}/{name}\": {e}")

    assert type(dataset) == models.Dataset
    logger.info(f"Dataset \"{namespace}/{name}\"'s phase is: {dataset.status.phase}")


if __name__ == '__main__':
    main()
```

## Versioning

Fluid Python SDK's version **ALWAYS** follows the Fluid's version as long as they share the fully compatible APIs. For example, if a released version of Fluid is v1.0.1, Fluid Python SDK with version prefix "v1.0.1" is guaranteed to have 
same APIs as the released Fluid version. 

Fluid Python SDK may have "post" version that updates the inner code but keep the APIs untouched (e.g. hotfixes). For example, "v1.0.1.post1" is a post version of "v1.0.1" which includes the latest
changes.


## Documentation For Models

 - [APIGatewayStatus](docs/APIGatewayStatus.md)
 - [AlluxioCompTemplateSpec](docs/AlluxioCompTemplateSpec.md)
 - [AlluxioFuseSpec](docs/AlluxioFuseSpec.md)
 - [AlluxioRuntime](docs/AlluxioRuntime.md)
 - [AlluxioRuntimeList](docs/AlluxioRuntimeList.md)
 - [AlluxioRuntimeSpec](docs/AlluxioRuntimeSpec.md)
 - [CacheableNodeAffinity](docs/CacheableNodeAffinity.md)
 - [CleanCachePolicy](docs/CleanCachePolicy.md)
 - [Condition](docs/Condition.md)
 - [Data](docs/Data.md)
 - [DataBackup](docs/DataBackup.md)
 - [DataBackupList](docs/DataBackupList.md)
 - [DataBackupSpec](docs/DataBackupSpec.md)
 - [DataLoad](docs/DataLoad.md)
 - [DataLoadList](docs/DataLoadList.md)
 - [DataLoadSpec](docs/DataLoadSpec.md)
 - [DataMigrate](docs/DataMigrate.md)
 - [DataMigrateList](docs/DataMigrateList.md)
 - [DataMigrateSpec](docs/DataMigrateSpec.md)
 - [DataProcess](docs/DataProcess.md)
 - [DataProcessList](docs/DataProcessList.md)
 - [DataProcessSpec](docs/DataProcessSpec.md)
 - [DataRestoreLocation](docs/DataRestoreLocation.md)
 - [DataToMigrate](docs/DataToMigrate.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetCondition](docs/DatasetCondition.md)
 - [DatasetList](docs/DatasetList.md)
 - [DatasetSpec](docs/DatasetSpec.md)
 - [DatasetStatus](docs/DatasetStatus.md)
 - [DatasetToMigrate](docs/DatasetToMigrate.md)
 - [EFCCompTemplateSpec](docs/EFCCompTemplateSpec.md)
 - [EFCFuseSpec](docs/EFCFuseSpec.md)
 - [EFCRuntime](docs/EFCRuntime.md)
 - [EFCRuntimeList](docs/EFCRuntimeList.md)
 - [EFCRuntimeSpec](docs/EFCRuntimeSpec.md)
 - [EncryptOption](docs/EncryptOption.md)
 - [EncryptOptionSource](docs/EncryptOptionSource.md)
 - [ExternalEndpointSpec](docs/ExternalEndpointSpec.md)
 - [ExternalStorage](docs/ExternalStorage.md)
 - [GooseFSCompTemplateSpec](docs/GooseFSCompTemplateSpec.md)
 - [GooseFSFuseSpec](docs/GooseFSFuseSpec.md)
 - [GooseFSRuntime](docs/GooseFSRuntime.md)
 - [GooseFSRuntimeList](docs/GooseFSRuntimeList.md)
 - [GooseFSRuntimeSpec](docs/GooseFSRuntimeSpec.md)
 - [HCFSStatus](docs/HCFSStatus.md)
 - [InitFuseSpec](docs/InitFuseSpec.md)
 - [InitUsersSpec](docs/InitUsersSpec.md)
 - [JindoCompTemplateSpec](docs/JindoCompTemplateSpec.md)
 - [JindoFuseSpec](docs/JindoFuseSpec.md)
 - [JindoRuntime](docs/JindoRuntime.md)
 - [JindoRuntimeList](docs/JindoRuntimeList.md)
 - [JindoRuntimeSpec](docs/JindoRuntimeSpec.md)
 - [JobProcessor](docs/JobProcessor.md)
 - [JuiceFSCompTemplateSpec](docs/JuiceFSCompTemplateSpec.md)
 - [JuiceFSFuseSpec](docs/JuiceFSFuseSpec.md)
 - [JuiceFSRuntime](docs/JuiceFSRuntime.md)
 - [JuiceFSRuntimeList](docs/JuiceFSRuntimeList.md)
 - [JuiceFSRuntimeSpec](docs/JuiceFSRuntimeSpec.md)
 - [Level](docs/Level.md)
 - [MasterSpec](docs/MasterSpec.md)
 - [Metadata](docs/Metadata.md)
 - [MetadataSyncPolicy](docs/MetadataSyncPolicy.md)
 - [Mount](docs/Mount.md)
 - [OSAdvise](docs/OSAdvise.md)
 - [OperationRef](docs/OperationRef.md)
 - [OperationStatus](docs/OperationStatus.md)
 - [PodMetadata](docs/PodMetadata.md)
 - [Processor](docs/Processor.md)
 - [Runtime](docs/Runtime.md)
 - [RuntimeCondition](docs/RuntimeCondition.md)
 - [RuntimeManagement](docs/RuntimeManagement.md)
 - [RuntimeStatus](docs/RuntimeStatus.md)
 - [ScriptProcessor](docs/ScriptProcessor.md)
 - [SecretKeySelector](docs/SecretKeySelector.md)
 - [TargetDataset](docs/TargetDataset.md)
 - [TargetDatasetWithMountPath](docs/TargetDatasetWithMountPath.md)
 - [TargetPath](docs/TargetPath.md)
 - [ThinCompTemplateSpec](docs/ThinCompTemplateSpec.md)
 - [ThinFuseSpec](docs/ThinFuseSpec.md)
 - [ThinRuntime](docs/ThinRuntime.md)
 - [ThinRuntimeList](docs/ThinRuntimeList.md)
 - [ThinRuntimeProfile](docs/ThinRuntimeProfile.md)
 - [ThinRuntimeProfileList](docs/ThinRuntimeProfileList.md)
 - [ThinRuntimeProfileSpec](docs/ThinRuntimeProfileSpec.md)
 - [ThinRuntimeSpec](docs/ThinRuntimeSpec.md)
 - [TieredStore](docs/TieredStore.md)
 - [User](docs/User.md)
 - [VersionSpec](docs/VersionSpec.md)
 - [VineyardCompTemplateSpec](docs/VineyardCompTemplateSpec.md)
 - [VineyardRuntime](docs/VineyardRuntime.md)
 - [VineyardRuntimeList](docs/VineyardRuntimeList.md)
 - [VineyardRuntimeSpec](docs/VineyardRuntimeSpec.md)
 - [VineyardSockSpec](docs/VineyardSockSpec.md)
 - [VolumeSource](docs/VolumeSource.md)
 - [WaitingStatus](docs/WaitingStatus.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author



