# LanguageResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_lower** | **str** |  | [optional] [readonly] 

## Example

```python
from radarr.models.language_resource import LanguageResource

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageResource from a JSON string
language_resource_instance = LanguageResource.from_json(json)
# print the JSON string representation of the object
print(LanguageResource.to_json())

# convert the object into a dict
language_resource_dict = language_resource_instance.to_dict()
# create an instance of LanguageResource from a dict
language_resource_form_dict = language_resource.from_dict(language_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


