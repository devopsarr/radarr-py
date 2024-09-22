# CustomFormatBulkResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**include_custom_format_when_renaming** | **bool** |  | [optional] 

## Example

```python
from radarr.models.custom_format_bulk_resource import CustomFormatBulkResource

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFormatBulkResource from a JSON string
custom_format_bulk_resource_instance = CustomFormatBulkResource.from_json(json)
# print the JSON string representation of the object
print(CustomFormatBulkResource.to_json())

# convert the object into a dict
custom_format_bulk_resource_dict = custom_format_bulk_resource_instance.to_dict()
# create an instance of CustomFormatBulkResource from a dict
custom_format_bulk_resource_from_dict = CustomFormatBulkResource.from_dict(custom_format_bulk_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


