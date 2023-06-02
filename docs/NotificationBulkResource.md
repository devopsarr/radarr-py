# NotificationBulkResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**apply_tags** | [**ApplyTags**](ApplyTags.md) |  | [optional] 

## Example

```python
from radarr.models.notification_bulk_resource import NotificationBulkResource

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationBulkResource from a JSON string
notification_bulk_resource_instance = NotificationBulkResource.from_json(json)
# print the JSON string representation of the object
print NotificationBulkResource.to_json()

# convert the object into a dict
notification_bulk_resource_dict = notification_bulk_resource_instance.to_dict()
# create an instance of NotificationBulkResource from a dict
notification_bulk_resource_form_dict = notification_bulk_resource.from_dict(notification_bulk_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


