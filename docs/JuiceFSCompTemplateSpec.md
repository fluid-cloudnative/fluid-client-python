# JuiceFSCompTemplateSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enabled or Disabled for the components. | [optional] 
**env** | [**list[V1EnvVar]**](V1EnvVar.md) | Environment variables that will be used by JuiceFS component. | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector | [optional] 
**ports** | [**list[V1ContainerPort]**](V1ContainerPort.md) | Ports used by JuiceFS | [optional] 
**replicas** | **int** | Replicas is the desired number of replicas of the given template. If unspecified, defaults to 1. replicas is the min replicas of dataset in the cluster | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | Resources that will be requested by the JuiceFS component. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


