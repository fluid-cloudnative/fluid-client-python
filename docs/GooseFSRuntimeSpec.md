# GooseFSRuntimeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_gateway** | [**GooseFSCompTemplateSpec**](GooseFSCompTemplateSpec.md) | The component spec of GooseFS API Gateway | [optional] 
**data** | [**Data**](Data.md) | Management strategies for the dataset to which the runtime is bound | [optional] 
**disable_prometheus** | **bool** | Disable monitoring for GooseFS Runtime Prometheus is enabled by default | [optional] 
**fuse** | [**GooseFSFuseSpec**](GooseFSFuseSpec.md) | The component spec of GooseFS Fuse | [optional] 
**goosefs_version** | [**VersionSpec**](VersionSpec.md) | The version information that instructs fluid to orchestrate a particular version of GooseFS. | [optional] 
**hadoop_config** | **str** | Name of the configMap used to support HDFS configurations when using HDFS as GooseFS&#39;s UFS. The configMap must be in the same namespace with the GooseFSRuntime. The configMap should contain user-specific HDFS conf files in it. For now, only \&quot;hdfs-site.xml\&quot; and \&quot;core-site.xml\&quot; are supported. It must take the filename of the conf file as the key and content of the file as the value. | [optional] 
**init_users** | [**InitUsersSpec**](InitUsersSpec.md) | The spec of init users | [optional] 
**job_master** | [**GooseFSCompTemplateSpec**](GooseFSCompTemplateSpec.md) | The component spec of GooseFS job master | [optional] 
**job_worker** | [**GooseFSCompTemplateSpec**](GooseFSCompTemplateSpec.md) | The component spec of GooseFS job Worker | [optional] 
**jvm_options** | **list[str]** | Options for JVM | [optional] 
**master** | [**GooseFSCompTemplateSpec**](GooseFSCompTemplateSpec.md) | The component spec of GooseFS master | [optional] 
**properties** | **dict(str, str)** | Configurable properties for the GOOSEFS component. &lt;br&gt; Refer to &lt;a href&#x3D;\&quot;https://cloud.tencent.com/document/product/436/56415\&quot;&gt;GOOSEFS Configuration Properties&lt;/a&gt; for more info | [optional] 
**replicas** | **int** | The replicas of the worker, need to be specified | [optional] 
**run_as** | [**User**](User.md) | Manage the user to run GooseFS Runtime GooseFS support POSIX-ACL and Apache Ranger to manager authorization | [optional] 
**tieredstore** | [**TieredStore**](TieredStore.md) | Tiered storage used by GooseFS | [optional] 
**worker** | [**GooseFSCompTemplateSpec**](GooseFSCompTemplateSpec.md) | The component spec of GooseFS worker | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


