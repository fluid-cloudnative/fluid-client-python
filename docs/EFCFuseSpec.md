# EFCFuseSpec

EFCFuseSpec is a description of the EFC Fuse
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clean_policy** | **str** | CleanPolicy decides when to clean EFC Fuse pods. Currently Fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once th fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnRuntimeDeleted | [optional] 
**network_mode** | **str** | Whether to use hostnetwork or not | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled | [optional] 
**pod_metadata** | [**PodMetadata**](PodMetadata.md) |  | [optional] 
**properties** | **dict(str, str)** | Configurable properties for EFC fuse | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**version** | [**VersionSpec**](VersionSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


