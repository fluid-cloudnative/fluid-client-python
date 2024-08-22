# VineyardClientSocketSpec

VineyardClientSocketSpec holds the configurations for vineyard client socket
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clean_policy** | **str** | CleanPolicy decides when to clean Vineyard Fuse pods. Currently Fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once th fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnRuntimeDeleted | [optional] 
**env** | **dict(str, str)** | Environment variables that will be used by Vineyard Fuse. Default is not set. | [optional] 
**image** | **str** | Image for Vineyard Fuse Default is &#x60;registry.aliyuncs.com/vineyard/vineyard-fluid-fuse&#x60; | [optional] 
**image_pull_policy** | **str** | Image pull policy for Vineyard Fuse Default is &#x60;IfNotPresent&#x60; Available values are &#x60;Always&#x60;, &#x60;IfNotPresent&#x60;, &#x60;Never&#x60; | [optional] 
**image_tag** | **str** | Image Tag for Vineyard Fuse Default is &#x60;v0.22.2&#x60; | [optional] 
**network_mode** | **str** | Whether to use hostnetwork or not Default is HostNetwork | [optional] 
**options** | **dict(str, str)** | Options for configuring vineyardd parameters. Supported options are as follows.   reserve_memory: (Bool) Whether to reserving enough physical memory pages for vineyardd.                   Default is true.   allocator: (String) The allocator used by vineyardd, could be \&quot;dlmalloc\&quot; or \&quot;mimalloc\&quot;.              Default is \&quot;dlmalloc\&quot;.   compression: (Bool) Compress before migration or spilling.                Default is true.   coredump: (Bool) Enable coredump core dump when been aborted.             Default is false.   meta_timeout: (Int) Timeout period before waiting the metadata service to be ready, in seconds        Default is 60.   etcd_endpoint: (String) The endpoint of etcd.                  Default is same as the etcd endpoint of vineyard worker.   etcd_prefix: (String) Metadata path prefix in etcd.                Default is \&quot;/vineyard\&quot;.   size: (String) shared memory size for vineyardd.                  1024M, 1024000, 1G, or 1Gi.                  Default is \&quot;0\&quot;, which means no cache.                  When the size is not set to \&quot;0\&quot;, it should be greater than the 2048 bytes(2K).   spill_path: (String) Path to spill temporary files, if not set, spilling will be disabled.               Default is \&quot;\&quot;.   spill_lower_rate: (Double) The lower rate of memory usage to trigger spilling.         Default is 0.3.   spill_upper_rate: (Double) The upper rate of memory usage to stop spilling.         Default is 0.8. Default is as follows. fuse:   options:     size: \&quot;0\&quot;     etcd_endpoint: \&quot;http://{{Name}}-master-0.{{Name}}-master.{{Namespace}}:{{EtcdClientPort}}\&quot;     etcd_prefix: \&quot;/vineyard\&quot; | [optional] 
**pod_metadata** | [**PodMetadata**](PodMetadata.md) |  | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


