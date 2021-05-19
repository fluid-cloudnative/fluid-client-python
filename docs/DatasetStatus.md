# DatasetStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_states** | **dict(str, str)** | CacheStatus represents the total resources of the dataset. | [optional] 
**conditions** | [**list[DatasetCondition]**](DatasetCondition.md) | Conditions is an array of current observed conditions. | 
**data_backup_ref** | **str** | DataBackupRef specifies the running Backup job that targets this Dataset. This is mainly used as a lock to prevent concurrent DataBackup jobs. | [optional] 
**data_load_ref** | **str** | DataLoadRef specifies the running DataLoad job that targets this Dataset. This is mainly used as a lock to prevent concurrent DataLoad jobs. | [optional] 
**file_num** | **str** | FileNum represents the file numbers of the dataset | [optional] 
**hcfs** | [**HCFSStatus**](HCFSStatus.md) | HCFSStatus represents hcfs info | [optional] 
**phase** | **str** | Dataset Phase. One of the four phases: &#x60;Pending&#x60;, &#x60;Bound&#x60;, &#x60;NotBound&#x60; and &#x60;Failed&#x60; | [optional] 
**runtimes** | [**list[Runtime]**](Runtime.md) | Runtimes for supporting dataset | [optional] 
**ufs_total** | **str** | Total in GB of dataset in the cluster | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


