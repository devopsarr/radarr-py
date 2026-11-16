# ReleaseHistoryResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grabbed** | **datetime** |  | [optional] 
**failed** | **datetime** |  | [optional] 

## Example

```python
from radarr.models.release_history_resource import ReleaseHistoryResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseHistoryResource from a JSON string
release_history_resource_instance = ReleaseHistoryResource.from_json(json)
# print the JSON string representation of the object
print(ReleaseHistoryResource.to_json())

# convert the object into a dict
release_history_resource_dict = release_history_resource_instance.to_dict()
# create an instance of ReleaseHistoryResource from a dict
release_history_resource_from_dict = ReleaseHistoryResource.from_dict(release_history_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


