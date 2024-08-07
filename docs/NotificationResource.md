# NotificationResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**fields** | [**List[ContractField]**](ContractField.md) |  | [optional] 
**implementation_name** | **str** |  | [optional] 
**implementation** | **str** |  | [optional] 
**config_contract** | **str** |  | [optional] 
**info_link** | **str** |  | [optional] 
**message** | [**ProviderMessage**](ProviderMessage.md) |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**presets** | [**List[NotificationResource]**](NotificationResource.md) |  | [optional] 
**link** | **str** |  | [optional] 
**on_grab** | **bool** |  | [optional] 
**on_download** | **bool** |  | [optional] 
**on_upgrade** | **bool** |  | [optional] 
**on_rename** | **bool** |  | [optional] 
**on_movie_added** | **bool** |  | [optional] 
**on_movie_delete** | **bool** |  | [optional] 
**on_movie_file_delete** | **bool** |  | [optional] 
**on_movie_file_delete_for_upgrade** | **bool** |  | [optional] 
**on_health_issue** | **bool** |  | [optional] 
**include_health_warnings** | **bool** |  | [optional] 
**on_health_restored** | **bool** |  | [optional] 
**on_application_update** | **bool** |  | [optional] 
**on_manual_interaction_required** | **bool** |  | [optional] 
**supports_on_grab** | **bool** |  | [optional] 
**supports_on_download** | **bool** |  | [optional] 
**supports_on_upgrade** | **bool** |  | [optional] 
**supports_on_rename** | **bool** |  | [optional] 
**supports_on_movie_added** | **bool** |  | [optional] 
**supports_on_movie_delete** | **bool** |  | [optional] 
**supports_on_movie_file_delete** | **bool** |  | [optional] 
**supports_on_movie_file_delete_for_upgrade** | **bool** |  | [optional] 
**supports_on_health_issue** | **bool** |  | [optional] 
**supports_on_health_restored** | **bool** |  | [optional] 
**supports_on_application_update** | **bool** |  | [optional] 
**supports_on_manual_interaction_required** | **bool** |  | [optional] 
**test_command** | **str** |  | [optional] 

## Example

```python
from radarr.models.notification_resource import NotificationResource

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationResource from a JSON string
notification_resource_instance = NotificationResource.from_json(json)
# print the JSON string representation of the object
print(NotificationResource.to_json())

# convert the object into a dict
notification_resource_dict = notification_resource_instance.to_dict()
# create an instance of NotificationResource from a dict
notification_resource_from_dict = NotificationResource.from_dict(notification_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


