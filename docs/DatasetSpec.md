# DatasetSpec

DatasetSpec defines the desired state of Dataset
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **list[str]** | AccessModes contains all ways the volume backing the PVC can be mounted | [optional] 
**data_restore_location** | [**DataRestoreLocation**](DataRestoreLocation.md) |  | [optional] 
**mounts** | [**list[Mount]**](Mount.md) | Mount Points to be mounted on cache runtime. &lt;br&gt; This field can be empty because some runtimes don&#39;t need to mount external storage (e.g. &lt;a href&#x3D;\&quot;https://v6d.io/\&quot;&gt;Vineyard&lt;/a&gt;). | [optional] 
**node_affinity** | [**CacheableNodeAffinity**](CacheableNodeAffinity.md) |  | [optional] 
**owner** | [**User**](User.md) |  | [optional] 
**placement** | **str** | Manage switch for opening Multiple datasets single node deployment or not | [optional] 
**runtimes** | [**list[Runtime]**](Runtime.md) | Runtimes for supporting dataset (e.g. AlluxioRuntime) | [optional] 
**shared_encrypt_options** | [**list[EncryptOption]**](EncryptOption.md) | SharedEncryptOptions is the encryptOption to all mount | [optional] 
**shared_options** | **dict(str, str)** | SharedOptions is the options to all mount | [optional] 
**tolerations** | [**list[V1Toleration]**](V1Toleration.md) | If specified, the pod&#39;s tolerations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


