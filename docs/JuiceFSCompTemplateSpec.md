# JuiceFSCompTemplateSpec

JuiceFSCompTemplateSpec is a description of the JuiceFS components
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enabled or Disabled for the components. | [optional] 
**env** | [**list[V1EnvVar]**](V1EnvVar.md) | Environment variables that will be used by JuiceFS component. | [optional] 
**network_mode** | **str** | Whether to use hostnetwork or not | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector | [optional] 
**options** | **dict(str, str)** | Options | [optional] 
**pod_metadata** | [**PodMetadata**](PodMetadata.md) |  | [optional] 
**ports** | [**list[V1ContainerPort]**](V1ContainerPort.md) | Ports used by JuiceFS | [optional] 
**replicas** | **int** | Replicas is the desired number of replicas of the given template. If unspecified, defaults to 1. replicas is the min replicas of dataset in the cluster | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**volume_mounts** | [**list[V1VolumeMount]**](V1VolumeMount.md) | VolumeMounts specifies the volumes listed in \&quot;.spec.volumes\&quot; to mount into runtime component&#39;s filesystem. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


