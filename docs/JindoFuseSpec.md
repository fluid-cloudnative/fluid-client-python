# JindoFuseSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **list[str]** | Arguments that will be passed to Jindo Fuse | [optional] 
**env** | **dict(str, str)** | Environment variables that will be used by Jindo Fuse | [optional] 
**_global** | **bool** | If the fuse client should be deployed in global mode, otherwise the affinity should be considered | [optional] 
**image** | **str** | Image for Jindo Fuse(e.g. jindo/jindo-fuse) | [optional] 
**image_pull_policy** | **str** | One of the three policies: &#x60;Always&#x60;, &#x60;IfNotPresent&#x60;, &#x60;Never&#x60; | [optional] 
**image_tag** | **str** | Image Tag for Jindo Fuse(e.g. 2.3.0-SNAPSHOT) | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled | [optional] 
**properties** | **dict(str, str)** | Configurable properties for Jindo System. &lt;br&gt; | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | Resources that will be requested by Jindo Fuse. &lt;br&gt; &lt;br&gt; Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


