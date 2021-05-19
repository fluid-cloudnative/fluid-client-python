# JindoCompTemplateSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env** | **dict(str, str)** | Environment variables that will be used by Jindo component. &lt;br&gt; | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the master to fit on a node | [optional] 
**ports** | **dict(str, int)** |  | [optional] 
**properties** | **dict(str, str)** | Configurable properties for the Jindo component. &lt;br&gt; | [optional] 
**replicas** | **int** | Replicas is the desired number of replicas of the given template. If unspecified, defaults to 1. replicas is the min replicas of dataset in the cluster | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | Resources that will be requested by the Jindo component. &lt;br&gt; &lt;br&gt; Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


