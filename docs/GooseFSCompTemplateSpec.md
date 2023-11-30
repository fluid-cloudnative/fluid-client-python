# GooseFSCompTemplateSpec

GooseFSCompTemplateSpec is a description of the GooseFS commponents
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations | [optional] 
**enabled** | **bool** | Enabled or Disabled for the components. For now, only  API Gateway is enabled or disabled. | [optional] 
**env** | **dict(str, str)** | Environment variables that will be used by GooseFS component. &lt;br&gt; | [optional] 
**jvm_options** | **list[str]** | Options for JVM | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the master to fit on a node | [optional] 
**ports** | **dict(str, int)** | Ports used by GooseFS(e.g. rpc: 19998 for master) | [optional] 
**properties** | **dict(str, str)** | Configurable properties for the GOOSEFS component. &lt;br&gt; Refer to &lt;a href&#x3D;\&quot;https://cloud.tencent.com/document/product/436/56415\&quot;&gt;GOOSEFS Configuration Properties&lt;/a&gt; for more info | [optional] 
**replicas** | **int** | Replicas is the desired number of replicas of the given template. If unspecified, defaults to 1. replicas is the min replicas of dataset in the cluster | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


