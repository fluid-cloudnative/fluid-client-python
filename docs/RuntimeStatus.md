# RuntimeStatus

RuntimeStatus defines the observed state of Runtime
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_gateway** | [**APIGatewayStatus**](APIGatewayStatus.md) |  | [optional] 
**cache_affinity** | [**V1NodeAffinity**](V1NodeAffinity.md) |  | [optional] 
**cache_states** | **dict(str, str)** | CacheStatus represents the total resources of the dataset. | [optional] 
**conditions** | [**list[RuntimeCondition]**](RuntimeCondition.md) | Represents the latest available observations of a ddc runtime&#39;s current state. | [optional] 
**current_fuse_number_scheduled** | **int** | The total number of nodes that can be running the runtime Fuse pod (including nodes correctly running the runtime Fuse pod). | [default to 0]
**current_master_number_scheduled** | **int** | The total number of nodes that should be running the runtime pod (including nodes correctly running the runtime master pod). | [default to 0]
**current_worker_number_scheduled** | **int** | The total number of nodes that can be running the runtime worker pod (including nodes correctly running the runtime worker pod). | [default to 0]
**desired_fuse_number_scheduled** | **int** | The total number of nodes that should be running the runtime Fuse pod (including nodes correctly running the runtime Fuse pod). | [default to 0]
**desired_master_number_scheduled** | **int** | The total number of nodes that should be running the runtime pod (including nodes correctly running the runtime master pod). | [default to 0]
**desired_worker_number_scheduled** | **int** | The total number of nodes that should be running the runtime worker pod (including nodes correctly running the runtime worker pod). | [default to 0]
**fuse_number_available** | **int** | The number of nodes that should be running the runtime Fuse pod and have one or more of the runtime Fuse pod running and available (ready for at least spec.minReadySeconds) | [optional] 
**fuse_number_ready** | **int** | The number of nodes that should be running the runtime Fuse pod and have one or more of the runtime Fuse pod running and ready. | [default to 0]
**fuse_number_unavailable** | **int** | The number of nodes that should be running the runtime fuse pod and have none of the runtime fuse pod running and available (ready for at least spec.minReadySeconds) | [optional] 
**fuse_phase** | **str** | FusePhase is the Fuse running phase | [default to '']
**fuse_reason** | **str** | Reason for the condition&#39;s last transition. | [optional] 
**master_number_ready** | **int** | The number of nodes that should be running the runtime worker pod and have zero or more of the runtime master pod running and ready. | [default to 0]
**master_phase** | **str** | MasterPhase is the master running phase | [default to '']
**master_reason** | **str** | Reason for Master&#39;s condition transition | [optional] 
**mount_time** | [**datetime**](V1Time.md) |  | [optional] 
**mounts** | [**list[Mount]**](Mount.md) | MountPoints represents the mount points specified in the bounded dataset | [optional] 
**selector** | **str** | Selector is used for auto-scaling | [optional] 
**setup_duration** | **str** | Duration tell user how much time was spent to setup the runtime | [optional] 
**value_file** | **str** | config map used to set configurations | [default to '']
**worker_number_available** | **int** | The number of nodes that should be running the runtime worker pod and have one or more of the runtime worker pod running and available (ready for at least spec.minReadySeconds) | [optional] 
**worker_number_ready** | **int** | The number of nodes that should be running the runtime worker pod and have one or more of the runtime worker pod running and ready. | [default to 0]
**worker_number_unavailable** | **int** | The number of nodes that should be running the runtime worker pod and have none of the runtime worker pod running and available (ready for at least spec.minReadySeconds) | [optional] 
**worker_phase** | **str** | WorkerPhase is the worker running phase | [default to '']
**worker_reason** | **str** | Reason for Worker&#39;s condition transition | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


