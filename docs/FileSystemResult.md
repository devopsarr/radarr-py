# FileSystemResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | **str** |  | [optional] 
**directories** | [**List[FileSystemModel]**](FileSystemModel.md) |  | [optional] 
**files** | [**List[FileSystemModel]**](FileSystemModel.md) |  | [optional] 

## Example

```python
from radarr.models.file_system_result import FileSystemResult

# TODO update the JSON string below
json = "{}"
# create an instance of FileSystemResult from a JSON string
file_system_result_instance = FileSystemResult.from_json(json)
# print the JSON string representation of the object
print(FileSystemResult.to_json())

# convert the object into a dict
file_system_result_dict = file_system_result_instance.to_dict()
# create an instance of FileSystemResult from a dict
file_system_result_from_dict = FileSystemResult.from_dict(file_system_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


