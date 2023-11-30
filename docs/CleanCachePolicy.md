# CleanCachePolicy

CleanCachePolicy defines policies when cleaning cache
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grace_period_seconds** | **int** | Optional duration in seconds the cache needs to clean gracefully. May be decreased in delete runtime request. Value must be non-negative integer. The value zero indicates clean immediately via the timeout command (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with timeout command. Set this value longer than the expected cleanup time for your process. | [optional] 
**max_retry_attempts** | **int** | Optional max retry Attempts when cleanCache function returns an error after execution, runtime attempts to run it three more times by default. With Maximum Retry Attempts, you can customize the maximum number of retries. This gives you the option to continue processing retries. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


