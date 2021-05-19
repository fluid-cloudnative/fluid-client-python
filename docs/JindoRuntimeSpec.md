# JindoRuntimeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fuse** | [**JindoFuseSpec**](JindoFuseSpec.md) | Desired state for Jindo Fuse | [optional] 
**hadoop_config** | **str** | Name of the configMap used to support HDFS configurations when using HDFS as Jindo&#39;s UFS. The configMap must be in the same namespace with the JindoRuntime. The configMap should contain user-specific HDFS conf files in it. For now, only \&quot;hdfs-site.xml\&quot; and \&quot;core-site.xml\&quot; are supported. It must take the filename of the conf file as the key and content of the file as the value. | [optional] 
**jindo_version** | [**VersionSpec**](VersionSpec.md) | The version information that instructs fluid to orchestrate a particular version of Jindo. | [optional] 
**master** | [**JindoCompTemplateSpec**](JindoCompTemplateSpec.md) | Desired state for Jindo master | [optional] 
**properties** | **dict(str, str)** | Configurable properties for Jindo system. &lt;br&gt; | [optional] 
**replicas** | **int** | The replicas of the worker, need to be specified | [optional] 
**run_as** | [**User**](User.md) | Manage the user to run Jindo Runtime | [optional] 
**secret** | **str** |  | [optional] 
**tieredstore** | [**Tieredstore**](Tieredstore.md) | Tiered storage used by Jindo | [optional] 
**user** | **str** |  | [optional] 
**worker** | [**JindoCompTemplateSpec**](JindoCompTemplateSpec.md) | Desired state for Jindo worker | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


