# TargetDatasetWithMountPath

TargetDataset defines which dataset will be processed by DataProcess. Under the hood, the dataset's pvc will be mounted to the given mountPath of the DataProcess's containers.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_path** | **str** | MountPath defines where the Dataset should be mounted in DataProcess&#39;s containers. | [default to '']
**name** | **str** | Name defines name of the target dataset | [default to '']
**namespace** | **str** | Namespace defines namespace of the target dataset | [optional] 
**sub_path** | **str** | SubPath defines subpath of the target dataset to mount. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


