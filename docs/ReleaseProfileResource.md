# ReleaseProfileResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**required** | **object** |  | [optional] 
**ignored** | **object** |  | [optional] 
**indexer_id** | **int** |  | [optional] 
**tags** | **List[int]** |  | [optional] 

## Example

```python
from radarr.models.release_profile_resource import ReleaseProfileResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseProfileResource from a JSON string
release_profile_resource_instance = ReleaseProfileResource.from_json(json)
# print the JSON string representation of the object
print ReleaseProfileResource.to_json()

# convert the object into a dict
release_profile_resource_dict = release_profile_resource_instance.to_dict()
# create an instance of ReleaseProfileResource from a dict
release_profile_resource_form_dict = release_profile_resource.from_dict(release_profile_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


