# AutoTaggingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**remove_tags_automatically** | **bool** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**specifications** | [**List[AutoTaggingSpecificationSchema]**](AutoTaggingSpecificationSchema.md) |  | [optional] 

## Example

```python
from radarr.models.auto_tagging_resource import AutoTaggingResource

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTaggingResource from a JSON string
auto_tagging_resource_instance = AutoTaggingResource.from_json(json)
# print the JSON string representation of the object
print(AutoTaggingResource.to_json())

# convert the object into a dict
auto_tagging_resource_dict = auto_tagging_resource_instance.to_dict()
# create an instance of AutoTaggingResource from a dict
auto_tagging_resource_from_dict = AutoTaggingResource.from_dict(auto_tagging_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


