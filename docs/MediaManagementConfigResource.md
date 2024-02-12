# MediaManagementConfigResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**auto_unmonitor_previously_downloaded_movies** | **bool** |  | [optional] 
**recycle_bin** | **str** |  | [optional] 
**recycle_bin_cleanup_days** | **int** |  | [optional] 
**download_propers_and_repacks** | [**ProperDownloadTypes**](ProperDownloadTypes.md) |  | [optional] 
**create_empty_movie_folders** | **bool** |  | [optional] 
**delete_empty_folders** | **bool** |  | [optional] 
**file_date** | [**FileDateType**](FileDateType.md) |  | [optional] 
**rescan_after_refresh** | [**RescanAfterRefreshType**](RescanAfterRefreshType.md) |  | [optional] 
**auto_rename_folders** | **bool** |  | [optional] 
**paths_default_static** | **bool** |  | [optional] 
**set_permissions_linux** | **bool** |  | [optional] 
**chmod_folder** | **str** |  | [optional] 
**chown_group** | **str** |  | [optional] 
**skip_free_space_check_when_importing** | **bool** |  | [optional] 
**minimum_free_space_when_importing** | **int** |  | [optional] 
**copy_using_hardlinks** | **bool** |  | [optional] 
**use_script_import** | **bool** |  | [optional] 
**script_import_path** | **str** |  | [optional] 
**import_extra_files** | **bool** |  | [optional] 
**extra_file_extensions** | **str** |  | [optional] 
**enable_media_info** | **bool** |  | [optional] 

## Example

```python
from radarr.models.media_management_config_resource import MediaManagementConfigResource

# TODO update the JSON string below
json = "{}"
# create an instance of MediaManagementConfigResource from a JSON string
media_management_config_resource_instance = MediaManagementConfigResource.from_json(json)
# print the JSON string representation of the object
print MediaManagementConfigResource.to_json()

# convert the object into a dict
media_management_config_resource_dict = media_management_config_resource_instance.to_dict()
# create an instance of MediaManagementConfigResource from a dict
media_management_config_resource_form_dict = media_management_config_resource.from_dict(media_management_config_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


