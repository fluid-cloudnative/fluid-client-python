from kubernetes import client, config
from fluid import DataLoad, DataLoadSpec, TargetDataset, TargetPath
from fluid import constants

# Initialize kubernetes client
config.load_kube_config()
api_instance = client.CustomObjectsApi()

namespace = "default"
name = "demo-dataset-dataload"

target_dataset_name = "demo-dataset"

dataload = DataLoad(
    api_version=constants.API_VERSION,
    kind=constants.DATA_LOAD_KIND,
    metadata=client.V1ObjectMeta(
        namespace=namespace,
        name=name
    ),
    spec=DataLoadSpec(
        load_metadata=True,
        dataset=TargetDataset(
            namespace=namespace,
            name=target_dataset_name
        ),
        target=[
            TargetPath(path="/ckpt", replicas=1),
        ]
    )
)

try:
    api_instance.create_namespaced_custom_object(
        constants.GROUP,
        constants.VERSION,
        namespace,
        constants.DATA_LOAD_PLURAL,
        dataload
    )
except Exception as e:
    print("Error when creating DataLoad: ", e)
    exit(1)
else:
    print(f"DataLoad {namespace}/{name} created.")