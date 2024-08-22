# ThinRuntimeSpec

ThinRuntimeSpec defines the desired state of ThinRuntime
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_prometheus** | **bool** | Disable monitoring for Runtime Prometheus is enabled by default | [optional] 
**fuse** | [**ThinFuseSpec**](ThinFuseSpec.md) |  | [optional] 
**management** | [**RuntimeManagement**](RuntimeManagement.md) |  | [optional] 
**profile_name** | **str** | The specific runtime profile name, empty value is used for handling datasets which mount another dataset | [optional] 
**replicas** | **int** | The replicas of the worker, need to be specified | [optional] 
**run_as** | [**User**](User.md) |  | [optional] 
**tieredstore** | [**TieredStore**](TieredStore.md) |  | [optional] 
**volumes** | [**list[V1Volume]**](V1Volume.md) | Volumes is the list of Kubernetes volumes that can be mounted by runtime components and/or fuses. | [optional] 
**worker** | [**ThinCompTemplateSpec**](ThinCompTemplateSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


