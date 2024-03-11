# RemotePathMappingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**host** | **str** |  | [optional] 
**remote_path** | **str** |  | [optional] 
**local_path** | **str** |  | [optional] 

## Example

```python
from radarr.models.remote_path_mapping_resource import RemotePathMappingResource

# TODO update the JSON string below
json = "{}"
# create an instance of RemotePathMappingResource from a JSON string
remote_path_mapping_resource_instance = RemotePathMappingResource.from_json(json)
# print the JSON string representation of the object
print(RemotePathMappingResource.to_json())

# convert the object into a dict
remote_path_mapping_resource_dict = remote_path_mapping_resource_instance.to_dict()
# create an instance of RemotePathMappingResource from a dict
remote_path_mapping_resource_form_dict = remote_path_mapping_resource.from_dict(remote_path_mapping_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


