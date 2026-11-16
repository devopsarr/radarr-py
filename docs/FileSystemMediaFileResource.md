# FileSystemMediaFileResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**relative_path** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from radarr.models.file_system_media_file_resource import FileSystemMediaFileResource

# TODO update the JSON string below
json = "{}"
# create an instance of FileSystemMediaFileResource from a JSON string
file_system_media_file_resource_instance = FileSystemMediaFileResource.from_json(json)
# print the JSON string representation of the object
print(FileSystemMediaFileResource.to_json())

# convert the object into a dict
file_system_media_file_resource_dict = file_system_media_file_resource_instance.to_dict()
# create an instance of FileSystemMediaFileResource from a dict
file_system_media_file_resource_from_dict = FileSystemMediaFileResource.from_dict(file_system_media_file_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


