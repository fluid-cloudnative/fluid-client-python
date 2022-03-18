# JuiceFSRuntimeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_prometheus** | **bool** | Disable monitoring for JuiceFS Runtime Prometheus is enabled by default | [optional] 
**fuse** | [**JuiceFSFuseSpec**](JuiceFSFuseSpec.md) | Desired state for JuiceFS Fuse | [optional] 
**init_users** | [**InitUsersSpec**](InitUsersSpec.md) | The spec of init users | [optional] 
**job_worker** | [**JuiceFSCompTemplateSpec**](JuiceFSCompTemplateSpec.md) | The component spec of JuiceFS job Worker | [optional] 
**juicefs_version** | [**VersionSpec**](VersionSpec.md) | The version information that instructs fluid to orchestrate a particular version of JuiceFS. | [optional] 
**master** | [**JuiceFSCompTemplateSpec**](JuiceFSCompTemplateSpec.md) | The component spec of JuiceFS master | [optional] 
**replicas** | **int** | The replicas of the worker, need to be specified | [optional] 
**run_as** | [**User**](User.md) | Manage the user to run Juicefs Runtime | [optional] 
**tieredstore** | [**TieredStore**](TieredStore.md) | Tiered storage used by JuiceFS | [optional] 
**worker** | [**JuiceFSCompTemplateSpec**](JuiceFSCompTemplateSpec.md) | The component spec of JuiceFS worker | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


