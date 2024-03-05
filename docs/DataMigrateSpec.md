# DataMigrateSpec

DataMigrateSpec defines the desired state of DataMigrate
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**V1Affinity**](V1Affinity.md) |  | [optional] 
**block** | **bool** | if dataMigrate blocked dataset usage, default is false | [optional] 
**_from** | [**DataToMigrate**](DataToMigrate.md) |  | 
**image** | **str** | Image (e.g. alluxio/alluxio) | [optional] 
**image_pull_policy** | **str** | One of the three policies: &#x60;Always&#x60;, &#x60;IfNotPresent&#x60;, &#x60;Never&#x60; | [optional] 
**image_tag** | **str** | Image tag (e.g. 2.3.0-SNAPSHOT) | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector defiens node selector for DataMigrate pod | [optional] 
**options** | **dict(str, str)** | options for migrate, different for each runtime | [optional] 
**parallel_options** | **dict(str, str)** | ParallelOptions defines options like ssh port and ssh secret name when parallelism is greater than 1. | [optional] 
**parallelism** | **int** | Parallelism defines the parallelism tasks numbers for DataMigrate. If the value is greater than 1, the job acts as a launcher, and users should define the WorkerSpec. | [optional] 
**pod_metadata** | [**PodMetadata**](PodMetadata.md) |  | [optional] 
**policy** | **str** | policy for migrate, including Once, Cron, OnEvent | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**run_after** | [**OperationRef**](OperationRef.md) |  | [optional] 
**runtime_type** | **str** | using which runtime to migrate data; if none, take dataset runtime as default | [optional] 
**schedule** | **str** | The schedule in Cron format, only set when policy is cron, see https://en.wikipedia.org/wiki/Cron. | [optional] 
**scheduler_name** | **str** | SchedulerName sets the scheduler to be used for DataMigrate pod | [optional] 
**to** | [**DataToMigrate**](DataToMigrate.md) |  | 
**tolerations** | [**list[V1Toleration]**](V1Toleration.md) | Tolerations defines tolerations for DataMigrate pod | [optional] 
**ttl_seconds_after_finished** | **int** | TTLSecondsAfterFinished is the time second to clean up data operations after finished or failed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


