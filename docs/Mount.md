# Mount

Mount describes a mounting. <br> Refer to <a href=\"https://docs.alluxio.io/os/user/stable/en/ufs/S3.html\">Alluxio Storage Integrations</a> for more info
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypt_options** | [**list[EncryptOption]**](EncryptOption.md) | The secret information | [optional] 
**mount_point** | **str** | MountPoint is the mount point of source. | [default to '']
**name** | **str** | The name of mount | [optional] 
**options** | **dict(str, str)** | The Mount Options. &lt;br&gt; Refer to &lt;a href&#x3D;\&quot;https://docs.alluxio.io/os/user/stable/en/reference/Properties-List.html\&quot;&gt;Mount Options&lt;/a&gt;.  &lt;br&gt; The option has Prefix &#39;fs.&#39; And you can Learn more from &lt;a href&#x3D;\&quot;https://docs.alluxio.io/os/user/stable/en/ufs/S3.html\&quot;&gt;The Storage Integrations&lt;/a&gt; | [optional] 
**path** | **str** | The path of mount, if not set will be /{Name} | [optional] 
**read_only** | **bool** | Optional: Defaults to false (read-write). | [optional] 
**shared** | **bool** | Optional: Defaults to false (shared). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


