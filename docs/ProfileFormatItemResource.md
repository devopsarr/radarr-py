# ProfileFormatItemResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**format** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**score** | **int** |  | [optional] 

## Example

```python
from radarr.models.profile_format_item_resource import ProfileFormatItemResource

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileFormatItemResource from a JSON string
profile_format_item_resource_instance = ProfileFormatItemResource.from_json(json)
# print the JSON string representation of the object
print(ProfileFormatItemResource.to_json())

# convert the object into a dict
profile_format_item_resource_dict = profile_format_item_resource_instance.to_dict()
# create an instance of ProfileFormatItemResource from a dict
profile_format_item_resource_form_dict = profile_format_item_resource.from_dict(profile_format_item_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


