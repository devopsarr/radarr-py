# FileSystemTypeResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FileSystemEntityType**](FileSystemEntityType.md) |  | [optional] 

## Example

```python
from radarr.models.file_system_type_resource import FileSystemTypeResource

# TODO update the JSON string below
json = "{}"
# create an instance of FileSystemTypeResource from a JSON string
file_system_type_resource_instance = FileSystemTypeResource.from_json(json)
# print the JSON string representation of the object
print(FileSystemTypeResource.to_json())

# convert the object into a dict
file_system_type_resource_dict = file_system_type_resource_instance.to_dict()
# create an instance of FileSystemTypeResource from a dict
file_system_type_resource_from_dict = FileSystemTypeResource.from_dict(file_system_type_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


