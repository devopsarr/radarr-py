# CustomFormatResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**include_custom_format_when_renaming** | **bool** |  | [optional] 
**specifications** | [**List[CustomFormatSpecificationSchema]**](CustomFormatSpecificationSchema.md) |  | [optional] 

## Example

```python
from radarr.models.custom_format_resource import CustomFormatResource

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFormatResource from a JSON string
custom_format_resource_instance = CustomFormatResource.from_json(json)
# print the JSON string representation of the object
print CustomFormatResource.to_json()

# convert the object into a dict
custom_format_resource_dict = custom_format_resource_instance.to_dict()
# create an instance of CustomFormatResource from a dict
custom_format_resource_form_dict = custom_format_resource.from_dict(custom_format_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


