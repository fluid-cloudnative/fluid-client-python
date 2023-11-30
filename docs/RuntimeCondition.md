# RuntimeCondition

Condition describes the state of the cache at a certain point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_probe_time** | [**V1Time**](V1Time.md) |  | [optional] 
**last_transition_time** | [**V1Time**](V1Time.md) |  | [optional] 
**message** | **str** | A human readable message indicating details about the transition. | [optional] 
**reason** | **str** | The reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. | [default to '']
**type** | **str** | Type of cache condition. | [default to '']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


