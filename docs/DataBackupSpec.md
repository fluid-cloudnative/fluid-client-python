# DataBackupSpec

DataBackupSpec defines the desired state of DataBackup
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_path** | **str** | BackupPath defines the target path to save data of the DataBackup | [optional] 
**dataset** | **str** | Dataset defines the target dataset of the DataBackup | [optional] 
**run_after** | [**OperationRef**](OperationRef.md) |  | [optional] 
**run_as** | [**User**](User.md) |  | [optional] 
**ttl_seconds_after_finished** | **int** | TTLSecondsAfterFinished is the time second to clean up data operations after finished or failed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


