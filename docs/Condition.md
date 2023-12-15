# Condition

Condition explains the transitions on phase
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_probe_time** | [**datetime**](V1Time.md) |  | [optional] 
**last_transition_time** | [**datetime**](V1Time.md) |  | [optional] 
**message** | **str** | Message is a human-readable message indicating details about the transition | [optional] 
**reason** | **str** | Reason for the condition&#39;s last transition | [optional] 
**status** | **str** | Status of the condition, one of &#x60;True&#x60;, &#x60;False&#x60; or &#x60;Unknown&#x60; | [default to '']
**type** | **str** | Type of condition, either &#x60;Complete&#x60; or &#x60;Failed&#x60; | [default to '']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


