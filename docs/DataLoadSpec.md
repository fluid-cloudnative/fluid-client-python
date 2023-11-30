# DataLoadSpec

DataLoadSpec defines the desired state of DataLoad
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**V1Affinity**](V1Affinity.md) |  | [optional] 
**dataset** | [**TargetDataset**](TargetDataset.md) |  | [optional] 
**load_metadata** | **bool** | LoadMetadata specifies if the dataload job should load metadata | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector defiens node selector for DataLoad pod | [optional] 
**options** | **dict(str, str)** | Options specifies the extra dataload properties for runtime | [optional] 
**pod_metadata** | [**PodMetadata**](PodMetadata.md) |  | [optional] 
**policy** | **str** | including Once, Cron, OnEvent | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**run_after** | [**OperationRef**](OperationRef.md) |  | [optional] 
**schedule** | **str** | The schedule in Cron format, only set when policy is cron, see https://en.wikipedia.org/wiki/Cron. | [optional] 
**scheduler_name** | **str** | SchedulerName sets the scheduler to be used for DataLoad pod | [optional] 
**target** | [**list[TargetPath]**](TargetPath.md) | Target defines target paths that needs to be loaded | [optional] 
**tolerations** | [**list[V1Toleration]**](V1Toleration.md) | Tolerations defines tolerations for DataLoad pod | [optional] 
**ttl_seconds_after_finished** | **int** | TTLSecondsAfterFinished is the time second to clean up data operations after finished or failed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


