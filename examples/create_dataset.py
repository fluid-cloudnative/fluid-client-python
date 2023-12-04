from kubernetes import client, config
from fluid import Dataset, DatasetSpec, Mount
from fluid import constants

# Initialize kubernetes client
config.load_kube_config()
#config.load_incluster_config() # Load in-cluster kubeconfig
api_instance = client.CustomObjectsApi()

namespace = "default"
name = "demo"

dataset = Dataset(
    api_version=constants.API_VERSION,
    kind=constants.DATASET_KIND,
    metadata=client.V1ObjectMeta(
        name=name,
        namespace=namespace
    ),
    spec=DatasetSpec(
        mounts=[
            Mount(
                mount_point="https://mirrors.bit.edu.cn/apache/hbase/stable/",
                name="hbase",
                path="/",
            )
        ]
    )
)

try:
    api_instance.create_namespaced_custom_object(
        constants.GROUP,
        constants.VERSION,
        namespace,
        constants.DATASET_PLURAL,
        dataset
    )
except Exception as e:
    print("Error when creating dataset: ", e)
    exit(1)

print("Dataset %s/%s created." % (namespace, dataset.metadata.name))
