# JuiceFSRuntimeSpec

JuiceFSRuntimeSpec defines the desired state of JuiceFSRuntime
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clean_cache_policy** | [**CleanCachePolicy**](CleanCachePolicy.md) |  | [optional] 
**configs** | **list[str]** | Configs of JuiceFS | [optional] 
**disable_prometheus** | **bool** | Disable monitoring for JuiceFS Runtime Prometheus is enabled by default | [optional] 
**fuse** | [**JuiceFSFuseSpec**](JuiceFSFuseSpec.md) |  | [optional] 
**init_users** | [**InitUsersSpec**](InitUsersSpec.md) |  | [optional] 
**job_worker** | [**JuiceFSCompTemplateSpec**](JuiceFSCompTemplateSpec.md) |  | [optional] 
**juicefs_version** | [**VersionSpec**](VersionSpec.md) |  | [optional] 
**master** | [**JuiceFSCompTemplateSpec**](JuiceFSCompTemplateSpec.md) |  | [optional] 
**pod_metadata** | [**PodMetadata**](PodMetadata.md) |  | [optional] 
**replicas** | **int** | The replicas of the worker, need to be specified | [optional] 
**run_as** | [**User**](User.md) |  | [optional] 
**tieredstore** | [**TieredStore**](TieredStore.md) |  | [optional] 
**volumes** | [**list[V1Volume]**](V1Volume.md) | Volumes is the list of Kubernetes volumes that can be mounted by the alluxio runtime components and/or fuses. | [optional] 
**worker** | [**JuiceFSCompTemplateSpec**](JuiceFSCompTemplateSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


