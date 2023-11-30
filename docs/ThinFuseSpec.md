# ThinFuseSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **list[str]** | Arguments that will be passed to thinRuntime Fuse | [optional] 
**clean_policy** | **str** | CleanPolicy decides when to clean thinRuntime Fuse pods. Currently Fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once the fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnDemand | [optional] 
**command** | **list[str]** | Command that will be passed to thinRuntime Fuse | [optional] 
**env** | [**list[V1EnvVar]**](V1EnvVar.md) | Environment variables that will be used by thinRuntime Fuse | [optional] 
**image** | **str** | Image for thinRuntime fuse | [optional] 
**image_pull_policy** | **str** | One of the three policies: &#x60;Always&#x60;, &#x60;IfNotPresent&#x60;, &#x60;Never&#x60; | [optional] 
**image_tag** | **str** | Image for thinRuntime fuse | [optional] 
**liveness_probe** | [**V1Probe**](V1Probe.md) |  | [optional] 
**network_mode** | **str** | Whether to use hostnetwork or not | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled | [optional] 
**options** | **dict(str, str)** | Options configurable options of FUSE client, performance parameters usually. will be merged with Dataset.spec.mounts.options into fuse pod. | [optional] 
**ports** | [**list[V1ContainerPort]**](V1ContainerPort.md) | Ports used thinRuntime | [optional] 
**readiness_probe** | [**V1Probe**](V1Probe.md) |  | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**volume_mounts** | [**list[V1VolumeMount]**](V1VolumeMount.md) | VolumeMounts specifies the volumes listed in \&quot;.spec.volumes\&quot; to mount into the thinruntime component&#39;s filesystem. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


