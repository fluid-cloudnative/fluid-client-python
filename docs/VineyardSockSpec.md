# VineyardSockSpec

VineyardSockSpec holds the configurations for vineyard client socket
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clean_policy** | **str** | CleanPolicy decides when to clean Vineyard Fuse pods. Currently Fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once th fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnRuntimeDeleted | [optional] 
**image** | **str** | Image for Vineyard Fuse Default is &#x60;vineyardcloudnative/vineyard-fluid-fuse&#x60; | [optional] 
**image_pull_policy** | **str** | Image pull policy for Vineyard Fuse Default is &#x60;IfNotPresent&#x60; Available values are &#x60;Always&#x60;, &#x60;IfNotPresent&#x60;, &#x60;Never&#x60; | [optional] 
**image_tag** | **str** | Image Tag for Vineyard Fuse Default is &#x60;latest&#x60; | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


