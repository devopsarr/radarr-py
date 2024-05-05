# NamingConfigResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**rename_movies** | **bool** |  | [optional] 
**replace_illegal_characters** | **bool** |  | [optional] 
**colon_replacement_format** | [**ColonReplacementFormat**](ColonReplacementFormat.md) |  | [optional] 
**standard_movie_format** | **str** |  | [optional] 
**movie_folder_format** | **str** |  | [optional] 

## Example

```python
from radarr.models.naming_config_resource import NamingConfigResource

# TODO update the JSON string below
json = "{}"
# create an instance of NamingConfigResource from a JSON string
naming_config_resource_instance = NamingConfigResource.from_json(json)
# print the JSON string representation of the object
print(NamingConfigResource.to_json())

# convert the object into a dict
naming_config_resource_dict = naming_config_resource_instance.to_dict()
# create an instance of NamingConfigResource from a dict
naming_config_resource_from_dict = NamingConfigResource.from_dict(naming_config_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


