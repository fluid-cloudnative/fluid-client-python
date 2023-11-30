# GooseFSRuntimeSpec

GooseFSRuntimeSpec defines the desired state of GooseFSRuntime
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_gateway** | [**GooseFSCompTemplateSpec**](GooseFSCompTemplateSpec.md) |  | [optional] 
**clean_cache_policy** | [**CleanCachePolicy**](CleanCachePolicy.md) |  | [optional] 
**data** | [**Data**](Data.md) |  | [optional] 
**disable_prometheus** | **bool** | Disable monitoring for GooseFS Runtime Prometheus is enabled by default | [optional] 
**fuse** | [**GooseFSFuseSpec**](GooseFSFuseSpec.md) |  | [optional] 
**goosefs_version** | [**VersionSpec**](VersionSpec.md) |  | [optional] 
**hadoop_config** | **str** | Name of the configMap used to support HDFS configurations when using HDFS as GooseFS&#39;s UFS. The configMap must be in the same namespace with the GooseFSRuntime. The configMap should contain user-specific HDFS conf files in it. For now, only \&quot;hdfs-site.xml\&quot; and \&quot;core-site.xml\&quot; are supported. It must take the filename of the conf file as the key and content of the file as the value. | [optional] 
**init_users** | [**InitUsersSpec**](InitUsersSpec.md) |  | [optional] 
**job_master** | [**GooseFSCompTemplateSpec**](GooseFSCompTemplateSpec.md) |  | [optional] 
**job_worker** | [**GooseFSCompTemplateSpec**](GooseFSCompTemplateSpec.md) |  | [optional] 
**jvm_options** | **list[str]** | Options for JVM | [optional] 
**master** | [**GooseFSCompTemplateSpec**](GooseFSCompTemplateSpec.md) |  | [optional] 
**properties** | **dict(str, str)** | Configurable properties for the GOOSEFS component. &lt;br&gt; Refer to &lt;a href&#x3D;\&quot;https://cloud.tencent.com/document/product/436/56415\&quot;&gt;GOOSEFS Configuration Properties&lt;/a&gt; for more info | [optional] 
**replicas** | **int** | The replicas of the worker, need to be specified | [optional] 
**run_as** | [**User**](User.md) |  | [optional] 
**tieredstore** | [**TieredStore**](TieredStore.md) |  | [optional] 
**worker** | [**GooseFSCompTemplateSpec**](GooseFSCompTemplateSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


