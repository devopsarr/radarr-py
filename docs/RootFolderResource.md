# RootFolderResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**accessible** | **bool** |  | [optional] 
**free_space** | **int** |  | [optional] 
**unmapped_folders** | [**List[UnmappedFolder]**](UnmappedFolder.md) |  | [optional] 

## Example

```python
from radarr.models.root_folder_resource import RootFolderResource

# TODO update the JSON string below
json = "{}"
# create an instance of RootFolderResource from a JSON string
root_folder_resource_instance = RootFolderResource.from_json(json)
# print the JSON string representation of the object
print RootFolderResource.to_json()

# convert the object into a dict
root_folder_resource_dict = root_folder_resource_instance.to_dict()
# create an instance of RootFolderResource from a dict
root_folder_resource_form_dict = root_folder_resource.from_dict(root_folder_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


