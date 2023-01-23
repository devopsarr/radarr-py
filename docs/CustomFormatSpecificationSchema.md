# CustomFormatSpecificationSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**implementation** | **str** |  | [optional] 
**implementation_name** | **str** |  | [optional] 
**info_link** | **str** |  | [optional] 
**negate** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 
**fields** | [**List[Field]**](Field.md) |  | [optional] 
**presets** | [**List[CustomFormatSpecificationSchema]**](CustomFormatSpecificationSchema.md) |  | [optional] 

## Example

```python
from radarr.models.custom_format_specification_schema import CustomFormatSpecificationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFormatSpecificationSchema from a JSON string
custom_format_specification_schema_instance = CustomFormatSpecificationSchema.from_json(json)
# print the JSON string representation of the object
print CustomFormatSpecificationSchema.to_json()

# convert the object into a dict
custom_format_specification_schema_dict = custom_format_specification_schema_instance.to_dict()
# create an instance of CustomFormatSpecificationSchema from a dict
custom_format_specification_schema_form_dict = custom_format_specification_schema.from_dict(custom_format_specification_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


