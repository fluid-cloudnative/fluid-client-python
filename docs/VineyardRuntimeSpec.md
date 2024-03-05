# VineyardRuntimeSpec

VineyardRuntimeSpec defines the desired state of VineyardRuntime
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_prometheus** | **bool** | Disable monitoring metrics for Vineyard Runtime Default is false | [optional] 
**fuse** | [**VineyardSockSpec**](VineyardSockSpec.md) |  | [optional] 
**master** | [**MasterSpec**](MasterSpec.md) |  | [optional] 
**replicas** | **int** | The replicas of the worker, need to be specified If worker.replicas and the field are both specified, the field will be respected | [optional] 
**tieredstore** | [**TieredStore**](TieredStore.md) |  | [optional] 
**volumes** | [**list[V1Volume]**](V1Volume.md) | Volumes is the list of Kubernetes volumes that can be mounted by the vineyard components (Master and Worker). Default is null. | [optional] 
**worker** | [**VineyardCompTemplateSpec**](VineyardCompTemplateSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


