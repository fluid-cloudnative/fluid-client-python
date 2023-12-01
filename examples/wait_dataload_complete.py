from kubernetes import client, config
from fluid import constants

# Initialize kubernetes client
config.load_kube_config()
api_instance = client.CustomObjectsApi()

namespace = "default"
name = "demo-dataset-dataload"

wait_timeout = 300
polling_interval = 5

for _ in range(round(wait_timeout / polling_interval)):
    try:
       resp = api_instance.get_namespaced_custom_object(
               constants.GROUP,
               constants.VERSION,
               namespace,
               constants.DATA_LOAD_PLURAL,
               name)
    except Exception as e:
        print("Error when getting dataset {}/{}:".format(namespace, name), e)
        continue
    else:
        if "status" in resp and "phase" in resp['status']:
            if resp['status']['phase'] == 'Complete' or resp['status']['phase'] == 'Failed':
                print(f"DataLoad finished with phase: {resp['status']['phase']}")
                break
