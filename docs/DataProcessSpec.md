# DataProcessSpec

DataProcessSpec defines the desired state of DataProcess
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | [**TargetDatasetWithMountPath**](TargetDatasetWithMountPath.md) |  | 
**processor** | [**Processor**](Processor.md) |  | 
**run_after** | [**OperationRef**](OperationRef.md) |  | [optional] 
**ttl_seconds_after_finished** | **int** | TTLSecondsAfterFinished is the time second to clean up data operations after finished or failed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


