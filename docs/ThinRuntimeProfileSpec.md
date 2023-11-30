# ThinRuntimeProfileSpec

ThinRuntimeProfileSpec defines the desired state of ThinRuntimeProfile
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_system_type** | **str** | file system of thinRuntime | [default to '']
**fuse** | [**ThinFuseSpec**](ThinFuseSpec.md) |  | [optional] 
**node_publish_secret_policy** | **str** | NodePublishSecretPolicy describes the policy to decide which to do with node publish secret when mounting an existing persistent volume. | [optional] 
**volumes** | [**list[V1Volume]**](V1Volume.md) | Volumes is the list of Kubernetes volumes that can be mounted by runtime components and/or fuses. | [optional] 
**worker** | [**ThinCompTemplateSpec**](ThinCompTemplateSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


