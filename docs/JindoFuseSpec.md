# JindoFuseSpec

JindoFuseSpec is a description of the Jindo Fuse
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **list[str]** | Arguments that will be passed to Jindo Fuse | [optional] 
**clean_policy** | **str** | CleanPolicy decides when to clean JindoFS Fuse pods. Currently Fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once th fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnRuntimeDeleted | [optional] 
**disabled** | **bool** | If disable JindoFS fuse | [optional] 
**env** | **dict(str, str)** | Environment variables that will be used by Jindo Fuse | [optional] 
**image** | **str** | Image for Jindo Fuse(e.g. jindo/jindo-fuse) | [optional] 
**image_pull_policy** | **str** | One of the three policies: &#x60;Always&#x60;, &#x60;IfNotPresent&#x60;, &#x60;Never&#x60; | [optional] 
**image_tag** | **str** | Image Tag for Jindo Fuse(e.g. 2.3.0-SNAPSHOT) | [optional] 
**labels** | **dict(str, str)** | Labels will be added on all the JindoFS pods. DEPRECATED: this is a deprecated field. Please use PodMetadata.Labels instead. Note: this field is set to be exclusive with PodMetadata.Labels | [optional] 
**log_config** | **dict(str, str)** |  | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled | [optional] 
**pod_metadata** | [**PodMetadata**](PodMetadata.md) |  | [optional] 
**properties** | **dict(str, str)** | Configurable properties for Jindo System. &lt;br&gt; | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**tolerations** | [**list[V1Toleration]**](V1Toleration.md) | If specified, the pod&#39;s tolerations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


