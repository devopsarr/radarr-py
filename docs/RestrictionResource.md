# RestrictionResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**required** | **str** |  | [optional] 
**preferred** | **str** |  | [optional] 
**ignored** | **str** |  | [optional] 
**tags** | **List[int]** |  | [optional] 

## Example

```python
from radarr.models.restriction_resource import RestrictionResource

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictionResource from a JSON string
restriction_resource_instance = RestrictionResource.from_json(json)
# print the JSON string representation of the object
print RestrictionResource.to_json()

# convert the object into a dict
restriction_resource_dict = restriction_resource_instance.to_dict()
# create an instance of RestrictionResource from a dict
restriction_resource_form_dict = restriction_resource.from_dict(restriction_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


