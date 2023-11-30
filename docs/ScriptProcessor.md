# ScriptProcessor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **list[str]** | Entrypoint command for ScriptProcessor. | [optional] 
**env** | [**list[V1EnvVar]**](V1EnvVar.md) | List of environment variables to set in the container. | [optional] 
**image** | **str** | Image (e.g. alluxio/alluxio) | [optional] 
**image_pull_policy** | **str** | One of the three policies: &#x60;Always&#x60;, &#x60;IfNotPresent&#x60;, &#x60;Never&#x60; | [optional] 
**image_tag** | **str** | Image tag (e.g. 2.3.0-SNAPSHOT) | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**restart_policy** | **str** | RestartPolicy specifies the processor job&#39;s restart policy. Only \&quot;Never\&quot;, \&quot;OnFailure\&quot; is allowed. | [optional] 
**source** | **str** | Script source for ScriptProcessor | [default to '']
**volume_mounts** | [**list[V1VolumeMount]**](V1VolumeMount.md) | Pod volumes to mount into the container&#39;s filesystem. | [optional] 
**volumes** | [**list[V1Volume]**](V1Volume.md) | List of volumes that can be mounted by containers belonging to the pod. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


