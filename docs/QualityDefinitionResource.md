# QualityDefinitionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**quality** | [**Quality**](Quality.md) |  | [optional] 
**title** | **str** |  | [optional] 
**weight** | **int** |  | [optional] 
**min_size** | **float** |  | [optional] 
**max_size** | **float** |  | [optional] 
**preferred_size** | **float** |  | [optional] 

## Example

```python
from radarr.models.quality_definition_resource import QualityDefinitionResource

# TODO update the JSON string below
json = "{}"
# create an instance of QualityDefinitionResource from a JSON string
quality_definition_resource_instance = QualityDefinitionResource.from_json(json)
# print the JSON string representation of the object
print(QualityDefinitionResource.to_json())

# convert the object into a dict
quality_definition_resource_dict = quality_definition_resource_instance.to_dict()
# create an instance of QualityDefinitionResource from a dict
quality_definition_resource_from_dict = QualityDefinitionResource.from_dict(quality_definition_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


