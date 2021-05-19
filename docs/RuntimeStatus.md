# RuntimeStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_gateway** | [**APIGatewayStatus**](APIGatewayStatus.md) | APIGatewayStatus represents rest api gateway status | [optional] 
**cache_states** | **dict(str, str)** | CacheStatus represents the total resources of the dataset. | [optional] 
**conditions** | [**list[RuntimeCondition]**](RuntimeCondition.md) | Represents the latest available observations of a ddc runtime&#39;s current state. | [optional] 
**current_fuse_number_scheduled** | **int** | The total number of nodes that can be running the runtime Fuse pod (including nodes correctly running the runtime Fuse pod). | 
**current_master_number_scheduled** | **int** | The total number of nodes that should be running the runtime pod (including nodes correctly running the runtime master pod). | 
**current_worker_number_scheduled** | **int** | The total number of nodes that can be running the runtime worker pod (including nodes correctly running the runtime worker pod). | 
**desired_fuse_number_scheduled** | **int** | The total number of nodes that should be running the runtime Fuse pod (including nodes correctly running the runtime Fuse pod). | 
**desired_master_number_scheduled** | **int** | The total number of nodes that should be running the runtime pod (including nodes correctly running the runtime master pod). | 
**desired_worker_number_scheduled** | **int** | The total number of nodes that should be running the runtime worker pod (including nodes correctly running the runtime worker pod). | 
**fuse_number_available** | **int** | The number of nodes that should be running the runtime Fuse pod and have one or more of the runtime Fuse pod running and available (ready for at least spec.minReadySeconds) | [optional] 
**fuse_number_ready** | **int** | The number of nodes that should be running the runtime Fuse pod and have one or more of the runtime Fuse pod running and ready. | 
**fuse_number_unavailable** | **int** | The number of nodes that should be running the runtime fuse pod and have none of the runtime fuse pod running and available (ready for at least spec.minReadySeconds) | [optional] 
**fuse_phase** | **str** | FusePhase is the Fuse running phase | 
**fuse_reason** | **str** | Reason for the condition&#39;s last transition. | [optional] 
**master_number_ready** | **int** | The number of nodes that should be running the runtime worker pod and have zero or more of the runtime master pod running and ready. | 
**master_phase** | **str** | MasterPhase is the master running phase | 
**master_reason** | **str** | Reason for Master&#39;s condition transition | [optional] 
**selector** | **str** | Selector is used for auto-scaling | [optional] 
**setup_duration** | **str** | Duration tell user how much time was spent to setup the runtime | [optional] 
**value_file** | **str** | config map used to set configurations | 
**worker_number_available** | **int** | The number of nodes that should be running the runtime worker pod and have one or more of the runtime worker pod running and available (ready for at least spec.minReadySeconds) | [optional] 
**worker_number_ready** | **int** | The number of nodes that should be running the runtime worker pod and have one or more of the runtime worker pod running and ready. | 
**worker_number_unavailable** | **int** | The number of nodes that should be running the runtime worker pod and have none of the runtime worker pod running and available (ready for at least spec.minReadySeconds) | [optional] 
**worker_phase** | **str** | WorkerPhase is the worker running phase | 
**worker_reason** | **str** | Reason for Worker&#39;s condition transition | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


