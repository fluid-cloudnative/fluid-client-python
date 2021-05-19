# AlluxioFuseSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **list[str]** | Arguments that will be passed to Alluxio Fuse | [optional] 
**env** | **dict(str, str)** | Environment variables that will be used by Alluxio Fuse | [optional] 
**_global** | **bool** | If the fuse client should be deployed in global mode, otherwise the affinity should be considered | [optional] 
**image** | **str** | Image for Alluxio Fuse(e.g. alluxio/alluxio-fuse) | [optional] 
**image_pull_policy** | **str** | One of the three policies: &#x60;Always&#x60;, &#x60;IfNotPresent&#x60;, &#x60;Never&#x60; | [optional] 
**image_tag** | **str** | Image Tag for Alluxio Fuse(e.g. 2.3.0-SNAPSHOT) | [optional] 
**jvm_options** | **list[str]** | Options for JVM | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled | [optional] 
**properties** | **dict(str, str)** | Configurable properties for Alluxio System. &lt;br&gt; Refer to &lt;a href&#x3D;\&quot;https://docs.alluxio.io/os/user/stable/en/reference/Properties-List.html\&quot;&gt;Alluxio Configuration Properties&lt;/a&gt; for more info | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | Resources that will be requested by Alluxio Fuse. &lt;br&gt; &lt;br&gt; Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


