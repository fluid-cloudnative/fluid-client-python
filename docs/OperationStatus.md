# OperationStatus

OperationStatus defines the observed state of operation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[Condition]**](Condition.md) | Conditions consists of transition information on operation&#39;s Phase | 
**duration** | **str** | Duration tell user how much time was spent to operation | [default to '']
**infos** | **dict(str, str)** | Infos operation customized name-value | [optional] 
**last_schedule_time** | [**datetime**](V1Time.md) |  | [optional] 
**last_successful_time** | [**datetime**](V1Time.md) |  | [optional] 
**node_affinity** | [**V1NodeAffinity**](V1NodeAffinity.md) |  | [optional] 
**phase** | **str** | Phase describes current phase of operation | [default to '']
**waiting_for** | [**WaitingStatus**](WaitingStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


