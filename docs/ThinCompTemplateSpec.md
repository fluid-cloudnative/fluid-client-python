# ThinCompTemplateSpec

ThinCompTemplateSpec is a description of the thinRuntime components
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enabled or Disabled for the components. | [optional] 
**env** | [**list[V1EnvVar]**](V1EnvVar.md) | Environment variables that will be used by thinRuntime component. | [optional] 
**image** | **str** | Image for thinRuntime fuse | [optional] 
**image_pull_policy** | **str** | One of the three policies: &#x60;Always&#x60;, &#x60;IfNotPresent&#x60;, &#x60;Never&#x60; | [optional] 
**image_tag** | **str** | Image for thinRuntime fuse | [optional] 
**liveness_probe** | [**V1Probe**](V1Probe.md) |  | [optional] 
**network_mode** | **str** | Whether to use hostnetwork or not | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector | [optional] 
**ports** | [**list[V1ContainerPort]**](V1ContainerPort.md) | Ports used thinRuntime | [optional] 
**readiness_probe** | [**V1Probe**](V1Probe.md) |  | [optional] 
**replicas** | **int** | Replicas is the desired number of replicas of the given template. If unspecified, defaults to 1. replicas is the min replicas of dataset in the cluster | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**volume_mounts** | [**list[V1VolumeMount]**](V1VolumeMount.md) | VolumeMounts specifies the volumes listed in \&quot;.spec.volumes\&quot; to mount into runtime component&#39;s filesystem. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


