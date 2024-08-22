# AlluxioRuntimeSpec

AlluxioRuntimeSpec defines the desired state of AlluxioRuntime
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alluxio_version** | [**VersionSpec**](VersionSpec.md) |  | [optional] 
**api_gateway** | [**AlluxioCompTemplateSpec**](AlluxioCompTemplateSpec.md) |  | [optional] 
**data** | [**Data**](Data.md) |  | [optional] 
**disable_prometheus** | **bool** | Disable monitoring for Alluxio Runtime Prometheus is enabled by default | [optional] 
**fuse** | [**AlluxioFuseSpec**](AlluxioFuseSpec.md) |  | [optional] 
**hadoop_config** | **str** | Name of the configMap used to support HDFS configurations when using HDFS as Alluxio&#39;s UFS. The configMap must be in the same namespace with the AlluxioRuntime. The configMap should contain user-specific HDFS conf files in it. For now, only \&quot;hdfs-site.xml\&quot; and \&quot;core-site.xml\&quot; are supported. It must take the filename of the conf file as the key and content of the file as the value. | [optional] 
**image_pull_secrets** | [**list[V1LocalObjectReference]**](V1LocalObjectReference.md) | ImagePullSecrets that will be used to pull images | [optional] 
**init_users** | [**InitUsersSpec**](InitUsersSpec.md) |  | [optional] 
**job_master** | [**AlluxioCompTemplateSpec**](AlluxioCompTemplateSpec.md) |  | [optional] 
**job_worker** | [**AlluxioCompTemplateSpec**](AlluxioCompTemplateSpec.md) |  | [optional] 
**jvm_options** | **list[str]** | Options for JVM | [optional] 
**management** | [**RuntimeManagement**](RuntimeManagement.md) |  | [optional] 
**master** | [**AlluxioCompTemplateSpec**](AlluxioCompTemplateSpec.md) |  | [optional] 
**pod_metadata** | [**PodMetadata**](PodMetadata.md) |  | [optional] 
**properties** | **dict(str, str)** | Configurable properties for Alluxio system. &lt;br&gt; Refer to &lt;a href&#x3D;\&quot;https://docs.alluxio.io/os/user/stable/en/reference/Properties-List.html\&quot;&gt;Alluxio Configuration Properties&lt;/a&gt; for more info | [optional] 
**replicas** | **int** | The replicas of the worker, need to be specified | [optional] 
**run_as** | [**User**](User.md) |  | [optional] 
**tieredstore** | [**TieredStore**](TieredStore.md) |  | [optional] 
**volumes** | [**list[V1Volume]**](V1Volume.md) | Volumes is the list of Kubernetes volumes that can be mounted by the alluxio runtime components and/or fuses. | [optional] 
**worker** | [**AlluxioCompTemplateSpec**](AlluxioCompTemplateSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


