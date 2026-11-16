# NamingExampleResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movie_example** | **str** |  | [optional] 
**movie_folder_example** | **str** |  | [optional] 

## Example

```python
from radarr.models.naming_example_resource import NamingExampleResource

# TODO update the JSON string below
json = "{}"
# create an instance of NamingExampleResource from a JSON string
naming_example_resource_instance = NamingExampleResource.from_json(json)
# print the JSON string representation of the object
print(NamingExampleResource.to_json())

# convert the object into a dict
naming_example_resource_dict = naming_example_resource_instance.to_dict()
# create an instance of NamingExampleResource from a dict
naming_example_resource_from_dict = NamingExampleResource.from_dict(naming_example_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


