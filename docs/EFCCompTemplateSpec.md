# EFCCompTemplateSpec

EFCCompTemplateSpec is a description of the EFC components
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Enabled or Disabled for the components. Default enable. | [optional] 
**network_mode** | **str** | Whether to use host network or not. | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the component to fit on a node. | [optional] 
**pod_metadata** | [**PodMetadata**](PodMetadata.md) |  | [optional] 
**ports** | **dict(str, int)** | Ports used by EFC(e.g. rpc: 19998 for master). | [optional] 
**properties** | **dict(str, str)** | Configurable properties for the EFC component. | [optional] 
**replicas** | **int** | Replicas is the desired number of replicas of the given template. If unspecified, defaults to 1. replicas is the min replicas of dataset in the cluster | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**version** | [**VersionSpec**](VersionSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


