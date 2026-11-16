# FileSystemModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FileSystemEntityType**](FileSystemEntityType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**extension** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from radarr.models.file_system_model import FileSystemModel

# TODO update the JSON string below
json = "{}"
# create an instance of FileSystemModel from a JSON string
file_system_model_instance = FileSystemModel.from_json(json)
# print the JSON string representation of the object
print(FileSystemModel.to_json())

# convert the object into a dict
file_system_model_dict = file_system_model_instance.to_dict()
# create an instance of FileSystemModel from a dict
file_system_model_from_dict = FileSystemModel.from_dict(file_system_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


