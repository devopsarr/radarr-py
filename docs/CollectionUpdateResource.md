# CollectionUpdateResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_ids** | **List[int]** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**monitor_movies** | **bool** |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**minimum_availability** | [**MovieStatusType**](MovieStatusType.md) |  | [optional] 

## Example

```python
from radarr.models.collection_update_resource import CollectionUpdateResource

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionUpdateResource from a JSON string
collection_update_resource_instance = CollectionUpdateResource.from_json(json)
# print the JSON string representation of the object
print CollectionUpdateResource.to_json()

# convert the object into a dict
collection_update_resource_dict = collection_update_resource_instance.to_dict()
# create an instance of CollectionUpdateResource from a dict
collection_update_resource_form_dict = collection_update_resource.from_dict(collection_update_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


