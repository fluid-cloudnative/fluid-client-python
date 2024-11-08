# ClientMetrics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enabled decides whether to expose client metrics. | [optional] 
**scrape_target** | **str** | ScrapeTarget decides which fuse component will be scraped by Prometheus. It is a list separated by comma where supported items are [MountPod, Sidecar, All (indicates MountPod and Sidecar), None]. Defaults to None when it is not explicitly set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


