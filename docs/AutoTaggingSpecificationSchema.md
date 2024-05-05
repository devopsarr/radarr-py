# AutoTaggingSpecificationSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**implementation** | **str** |  | [optional] 
**implementation_name** | **str** |  | [optional] 
**negate** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 
**fields** | [**List[ContractField]**](ContractField.md) |  | [optional] 

## Example

```python
from radarr.models.auto_tagging_specification_schema import AutoTaggingSpecificationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTaggingSpecificationSchema from a JSON string
auto_tagging_specification_schema_instance = AutoTaggingSpecificationSchema.from_json(json)
# print the JSON string representation of the object
print(AutoTaggingSpecificationSchema.to_json())

# convert the object into a dict
auto_tagging_specification_schema_dict = auto_tagging_specification_schema_instance.to_dict()
# create an instance of AutoTaggingSpecificationSchema from a dict
auto_tagging_specification_schema_from_dict = AutoTaggingSpecificationSchema.from_dict(auto_tagging_specification_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


