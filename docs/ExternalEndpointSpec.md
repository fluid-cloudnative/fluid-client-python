# ExternalEndpointSpec

ExternalEndpointSpec defines the configurations for external etcd cluster
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypt_options** | [**list[EncryptOption]**](EncryptOption.md) | encrypt info for accessing the external etcd cluster | [optional] 
**options** | **dict(str, str)** | Configurable options for External Etcd cluster. | [optional] 
**uri** | **str** | URI specifies the endpoint of external Etcd cluster E,g. \&quot;etcd-svc.etcd-namespace.svc.cluster.local:2379\&quot; Default is not set and use http protocol to connect to external etcd cluster | [optional] [default to '']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


