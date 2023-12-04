from kubernetes import client, config
from fluid import constants

# Initialize kubernetes client
config.load_kube_config()
#config.load_incluster_config() # Load in-cluster kubeconfig
api_instance = client.CustomObjectsApi()

namespace = "default"
name = "demo-dataset"

try:
   resp = api_instance.get_namespaced_custom_object(
           constants.GROUP,
           constants.VERSION,
           namespace,
           constants.DATASET_PLURAL,
           name)
except Exception as e:
    print("Error when getting dataset {}/{}:".format(namespace, name), e)
    exit(1)
else:
    if "status" in resp:
        print(resp)
        print(f"Dataset phase: {resp['status']['phase']}")
