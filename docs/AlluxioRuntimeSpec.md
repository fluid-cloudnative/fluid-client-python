# AlluxioRuntimeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alluxio_version** | [**VersionSpec**](VersionSpec.md) | The version information that instructs fluid to orchestrate a particular version of Alluxio. | [optional] 
**api_gateway** | [**AlluxioCompTemplateSpec**](AlluxioCompTemplateSpec.md) | Desired state for Alluxio API Gateway | [optional] 
**data** | [**Data**](Data.md) | Management strategies for the dataset to which the runtime is bound | [optional] 
**disable_prometheus** | **bool** | Disable monitoring for Alluxio Runtime Promethous is enabled by default | [optional] 
**fuse** | [**AlluxioFuseSpec**](AlluxioFuseSpec.md) | Desired state for Alluxio Fuse | [optional] 
**hadoop_config** | **str** | Name of the configMap used to support HDFS configurations when using HDFS as Alluxio&#39;s UFS. The configMap must be in the same namespace with the AlluxioRuntime. The configMap should contain user-specific HDFS conf files in it. For now, only \&quot;hdfs-site.xml\&quot; and \&quot;core-site.xml\&quot; are supported. It must take the filename of the conf file as the key and content of the file as the value. | [optional] 
**init_users** | [**InitUsersSpec**](InitUsersSpec.md) | The spec of init users | [optional] 
**job_master** | [**AlluxioCompTemplateSpec**](AlluxioCompTemplateSpec.md) | Desired state for Alluxio job master | [optional] 
**job_worker** | [**AlluxioCompTemplateSpec**](AlluxioCompTemplateSpec.md) | Desired state for Alluxio job Worker | [optional] 
**jvm_options** | **list[str]** | Options for JVM | [optional] 
**master** | [**AlluxioCompTemplateSpec**](AlluxioCompTemplateSpec.md) | Desired state for Alluxio master | [optional] 
**properties** | **dict(str, str)** | Configurable properties for Alluxio system. &lt;br&gt; Refer to &lt;a href&#x3D;\&quot;https://docs.alluxio.io/os/user/stable/en/reference/Properties-List.html\&quot;&gt;Alluxio Configuration Properties&lt;/a&gt; for more info | [optional] 
**replicas** | **int** | The replicas of the worker, need to be specified | [optional] 
**run_as** | [**User**](User.md) | Manage the user to run Alluxio Runtime | [optional] 
**tieredstore** | [**Tieredstore**](Tieredstore.md) | Tiered storage used by Alluxio | [optional] 
**worker** | [**AlluxioCompTemplateSpec**](AlluxioCompTemplateSpec.md) | Desired state for Alluxio worker | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


