# ExtraFileResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**movie_id** | **int** |  | [optional] 
**movie_file_id** | **int** |  | [optional] 
**relative_path** | **str** |  | [optional] 
**extension** | **str** |  | [optional] 
**type** | [**ExtraFileType**](ExtraFileType.md) |  | [optional] 

## Example

```python
from radarr.models.extra_file_resource import ExtraFileResource

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraFileResource from a JSON string
extra_file_resource_instance = ExtraFileResource.from_json(json)
# print the JSON string representation of the object
print(ExtraFileResource.to_json())

# convert the object into a dict
extra_file_resource_dict = extra_file_resource_instance.to_dict()
# create an instance of ExtraFileResource from a dict
extra_file_resource_form_dict = extra_file_resource.from_dict(extra_file_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


