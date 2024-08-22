# VineyardCompTemplateSpec

VineyardCompTemplateSpec is the common configurations for vineyard components including Master and Worker.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env** | **dict(str, str)** | Environment variables that will be used by Vineyard component. For Master, refer to &lt;a href&#x3D;\&quot;https://etcd.io/docs/v3.5/op-guide/configuration/\&quot;&gt;Etcd Configuration&lt;/a&gt; for more info Default is not set. | [optional] 
**image** | **str** | The image of Vineyard component. For Master, the default image is &#x60;registry.aliyuncs.com/vineyard/vineyardd&#x60; For Worker, the default image is &#x60;registry.aliyuncs.com/vineyard/vineyardd&#x60; The default container registry is &#x60;docker.io&#x60;, you can change it by setting the image field | [optional] 
**image_pull_policy** | **str** | The image pull policy of Vineyard component. Default is &#x60;IfNotPresent&#x60;. | [optional] 
**image_tag** | **str** | The image tag of Vineyard component. For Master, the default image tag is &#x60;v0.22.2&#x60;. For Worker, the default image tag is &#x60;v0.22.2&#x60;. | [optional] 
**network_mode** | **str** | Whether to use hostnetwork or not Default is HostNetwork | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector to choose which nodes to launch the Vineyard component. E,g. {\&quot;disktype\&quot;: \&quot;ssd\&quot;} | [optional] 
**options** | **dict(str, str)** | Configurable options for Vineyard component. For Master, there is no configurable options. For Worker, support the following options.    vineyardd.reserve.memory: (Bool) where to reserve memory for vineyardd                             If set to true, the memory quota will be counted to the vineyardd rather than the application.   etcd.prefix: (String) the prefix of etcd key for vineyard objects   wait.etcd.timeout: (String) the timeout period before waiting the etcd to be ready, in seconds    Default value is as follows.      vineyardd.reserve.memory: \&quot;true\&quot;     etcd.prefix: \&quot;/vineyard\&quot;     wait.etcd.timeout: \&quot;120\&quot; | [optional] 
**pod_metadata** | [**PodMetadata**](PodMetadata.md) |  | [optional] 
**ports** | **dict(str, int)** | Ports used by Vineyard component. For Master, the default client port is 2379 and peer port is 2380. For Worker, the default rpc port is 9600 and the default exporter port is 9144. | [optional] 
**replicas** | **int** | The replicas of Vineyard component. If not specified, defaults to 1. For worker, the replicas should not be greater than the number of nodes in the cluster | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**volume_mounts** | [**list[V1VolumeMount]**](V1VolumeMount.md) | VolumeMounts specifies the volumes listed in \&quot;.spec.volumes\&quot; to mount into the vineyard runtime component&#39;s filesystem. It is useful for specifying a persistent storage. Default is not set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


