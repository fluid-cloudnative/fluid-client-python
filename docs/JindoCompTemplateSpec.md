# JindoCompTemplateSpec

JindoCompTemplateSpec is a description of the Jindo commponents
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | If disable JindoFS master or worker | [optional] 
**env** | **dict(str, str)** | Environment variables that will be used by Jindo component. &lt;br&gt; | [optional] 
**labels** | **dict(str, str)** | Labels will be added on JindoFS Master or Worker pods. DEPRECATED: This is a deprecated field. Please use PodMetadata instead. Note: this field is set to be exclusive with PodMetadata.Labels | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the master to fit on a node | [optional] 
**pod_metadata** | [**PodMetadata**](PodMetadata.md) |  | [optional] 
**ports** | **dict(str, int)** |  | [optional] 
**properties** | **dict(str, str)** | Configurable properties for the Jindo component. &lt;br&gt; | [optional] 
**replicas** | **int** | Replicas is the desired number of replicas of the given template. If unspecified, defaults to 1. replicas is the min replicas of dataset in the cluster | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**tolerations** | [**list[V1Toleration]**](V1Toleration.md) | If specified, the pod&#39;s tolerations. | [optional] 
**volume_mounts** | [**list[V1VolumeMount]**](V1VolumeMount.md) | VolumeMounts specifies the volumes listed in \&quot;.spec.volumes\&quot; to mount into the jindo runtime component&#39;s filesystem. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


