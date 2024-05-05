# DiskSpaceResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**free_space** | **int** |  | [optional] 
**total_space** | **int** |  | [optional] 

## Example

```python
from radarr.models.disk_space_resource import DiskSpaceResource

# TODO update the JSON string below
json = "{}"
# create an instance of DiskSpaceResource from a JSON string
disk_space_resource_instance = DiskSpaceResource.from_json(json)
# print the JSON string representation of the object
print(DiskSpaceResource.to_json())

# convert the object into a dict
disk_space_resource_dict = disk_space_resource_instance.to_dict()
# create an instance of DiskSpaceResource from a dict
disk_space_resource_from_dict = DiskSpaceResource.from_dict(disk_space_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


