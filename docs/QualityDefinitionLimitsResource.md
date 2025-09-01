# QualityDefinitionLimitsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 

## Example

```python
from radarr.models.quality_definition_limits_resource import QualityDefinitionLimitsResource

# TODO update the JSON string below
json = "{}"
# create an instance of QualityDefinitionLimitsResource from a JSON string
quality_definition_limits_resource_instance = QualityDefinitionLimitsResource.from_json(json)
# print the JSON string representation of the object
print(QualityDefinitionLimitsResource.to_json())

# convert the object into a dict
quality_definition_limits_resource_dict = quality_definition_limits_resource_instance.to_dict()
# create an instance of QualityDefinitionLimitsResource from a dict
quality_definition_limits_resource_from_dict = QualityDefinitionLimitsResource.from_dict(quality_definition_limits_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


