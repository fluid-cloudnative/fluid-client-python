# AlluxioCompTemplateSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enabled or Disabled for the components. For now, only  API Gateway is enabled or disabled. | [optional] 
**env** | **dict(str, str)** | Environment variables that will be used by Alluxio component. &lt;br&gt; | [optional] 
**jvm_options** | **list[str]** | Options for JVM | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the master to fit on a node | [optional] 
**ports** | **dict(str, int)** | Ports used by Alluxio(e.g. rpc: 19998 for master) | [optional] 
**properties** | **dict(str, str)** | Configurable properties for the Alluxio component. &lt;br&gt; Refer to &lt;a href&#x3D;\&quot;https://docs.alluxio.io/os/user/stable/en/reference/Properties-List.html\&quot;&gt;Alluxio Configuration Properties&lt;/a&gt; for more info | [optional] 
**replicas** | **int** | Replicas is the desired number of replicas of the given template. If unspecified, defaults to 1. replicas is the min replicas of dataset in the cluster | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | Resources that will be requested by the Alluxio component. &lt;br&gt; &lt;br&gt; Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


