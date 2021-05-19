# DatasetSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **list[str]** | AccessModes contains all ways the volume backing the PVC can be mounted | [optional] 
**data_restore_location** | [**DataRestoreLocation**](DataRestoreLocation.md) | DataRestoreLocation is the location to load data of dataset  been backuped | [optional] 
**mounts** | [**list[Mount]**](Mount.md) | Mount Points to be mounted on Alluxio. | [optional] 
**node_affinity** | [**CacheableNodeAffinity**](CacheableNodeAffinity.md) | NodeAffinity defines constraints that limit what nodes this dataset can be cached to. This field influences the scheduling of pods that use the cached dataset. | [optional] 
**owner** | [**User**](User.md) | The owner of the dataset | [optional] 
**placement** | **str** | Manage switch for opening Multiple datasets single node deployment or not | [optional] 
**runtimes** | [**list[Runtime]**](Runtime.md) | Runtimes for supporting dataset (e.g. AlluxioRuntime) | [optional] 
**tolerations** | [**list[V1Toleration]**](V1Toleration.md) | If specified, the pod&#39;s tolerations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


