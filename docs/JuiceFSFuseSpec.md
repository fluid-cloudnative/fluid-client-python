# JuiceFSFuseSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clean_policy** | **str** | CleanPolicy decides when to clean Juicefs Fuse pods. Currently fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once th fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnDemand | [optional] 
**env** | [**list[V1EnvVar]**](V1EnvVar.md) | Environment variables that will be used by JuiceFS Fuse | [optional] 
**_global** | **bool** | If the fuse client should be deployed in global mode, otherwise the affinity should be considered | [optional] 
**image** | **str** | Image for JuiceFS fuse | [optional] 
**image_pull_policy** | **str** | One of the three policies: &#x60;Always&#x60;, &#x60;IfNotPresent&#x60;, &#x60;Never&#x60; | [optional] 
**image_tag** | **str** | Image for JuiceFS fuse | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | Resources that will be requested by JuiceFS Fuse. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


