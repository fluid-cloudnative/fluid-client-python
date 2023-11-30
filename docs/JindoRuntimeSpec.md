# JindoRuntimeSpec

JindoRuntimeSpec defines the desired state of JindoRuntime
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clean_cache_policy** | [**CleanCachePolicy**](CleanCachePolicy.md) |  | [optional] 
**fuse** | [**JindoFuseSpec**](JindoFuseSpec.md) |  | [optional] 
**hadoop_config** | **str** | Name of the configMap used to support HDFS configurations when using HDFS as Jindo&#39;s UFS. The configMap must be in the same namespace with the JindoRuntime. The configMap should contain user-specific HDFS conf files in it. For now, only \&quot;hdfs-site.xml\&quot; and \&quot;core-site.xml\&quot; are supported. It must take the filename of the conf file as the key and content of the file as the value. | [optional] 
**jindo_version** | [**VersionSpec**](VersionSpec.md) |  | [optional] 
**labels** | **dict(str, str)** | Labels will be added on all the JindoFS pods. DEPRECATED: this is a deprecated field. Please use PodMetadata.Labels instead. Note: this field is set to be exclusive with PodMetadata.Labels | [optional] 
**log_config** | **dict(str, str)** |  | [optional] 
**master** | [**JindoCompTemplateSpec**](JindoCompTemplateSpec.md) |  | [optional] 
**networkmode** | **str** | Whether to use hostnetwork or not | [optional] 
**pod_metadata** | [**PodMetadata**](PodMetadata.md) |  | [optional] 
**properties** | **dict(str, str)** | Configurable properties for Jindo system. &lt;br&gt; | [optional] 
**replicas** | **int** | The replicas of the worker, need to be specified | [optional] 
**run_as** | [**User**](User.md) |  | [optional] 
**secret** | **str** |  | [optional] 
**tieredstore** | [**TieredStore**](TieredStore.md) |  | [optional] 
**user** | **str** |  | [optional] 
**volumes** | [**list[V1Volume]**](V1Volume.md) | Volumes is the list of Kubernetes volumes that can be mounted by the jindo runtime components and/or fuses. | [optional] 
**worker** | [**JindoCompTemplateSpec**](JindoCompTemplateSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


