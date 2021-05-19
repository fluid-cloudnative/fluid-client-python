# Level

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**high** | **str** | Ratio of high watermark of the tier (e.g. 0.9) | [optional] 
**low** | **str** | Ratio of low watermark of the tier (e.g. 0.7) | [optional] 
**mediumtype** | **str** | Medium Type of the tier. One of the three types: &#x60;MEM&#x60;, &#x60;SSD&#x60;, &#x60;HDD&#x60; | 
**path** | **str** | File paths to be used for the tier. Multiple paths are supported. Multiple paths should be separated with comma. For example: \&quot;/mnt/cache1,/mnt/cache2\&quot;. | [optional] 
**quota** | [**K8sIoApimachineryPkgApiResourceQuantity**](K8sIoApimachineryPkgApiResourceQuantity.md) | Quota for the whole tier. (e.g. 100Gi) Please note that if there&#39;re multiple paths used for this tierstore, the quota will be equally divided into these paths. If you&#39;d like to set quota for each, path, see QuotaList for more information. | [optional] 
**quota_list** | **str** | QuotaList are quotas used to set quota on multiple paths. Quotas should be separated with comma. Quotas in this list will be set to paths with the same order in Path. For example, with Path defined with \&quot;/mnt/cache1,/mnt/cache2\&quot; and QuotaList set to \&quot;100Gi, 50Gi\&quot;, then we get 100GiB cache storage under \&quot;/mnt/cache1\&quot; and 50GiB under \&quot;/mnt/cache2\&quot;. Also note that num of quotas must be consistent with the num of paths defined in Path. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


