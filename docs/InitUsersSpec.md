# InitUsersSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env** | **dict(str, str)** | Environment variables that will be used by initialize the users for runtime | [optional] 
**image** | **str** | Image for initialize the users for runtime(e.g. alluxio/alluxio-User init) | [optional] 
**image_pull_policy** | **str** | One of the three policies: &#x60;Always&#x60;, &#x60;IfNotPresent&#x60;, &#x60;Never&#x60; | [optional] 
**image_tag** | **str** | Image Tag for initialize the users for runtime(e.g. 2.3.0-SNAPSHOT) | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | Resources that will be requested by initialize the users for runtime. &lt;br&gt; &lt;br&gt; Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


