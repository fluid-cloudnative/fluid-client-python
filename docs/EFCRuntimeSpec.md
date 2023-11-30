# EFCRuntimeSpec

EFCRuntimeSpec defines the desired state of EFCRuntime
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clean_cache_policy** | [**CleanCachePolicy**](CleanCachePolicy.md) |  | [optional] 
**fuse** | [**EFCFuseSpec**](EFCFuseSpec.md) |  | [optional] 
**init_fuse** | [**InitFuseSpec**](InitFuseSpec.md) |  | [optional] 
**master** | [**EFCCompTemplateSpec**](EFCCompTemplateSpec.md) |  | [optional] 
**os_advise** | [**OSAdvise**](OSAdvise.md) |  | [optional] 
**pod_metadata** | [**PodMetadata**](PodMetadata.md) |  | [optional] 
**replicas** | **int** | The replicas of the worker, need to be specified | [optional] 
**tieredstore** | [**TieredStore**](TieredStore.md) |  | [optional] 
**worker** | [**EFCCompTemplateSpec**](EFCCompTemplateSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


