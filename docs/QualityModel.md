# QualityModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quality** | [**Quality**](Quality.md) |  | [optional] 
**revision** | [**Revision**](Revision.md) |  | [optional] 

## Example

```python
from radarr.models.quality_model import QualityModel

# TODO update the JSON string below
json = "{}"
# create an instance of QualityModel from a JSON string
quality_model_instance = QualityModel.from_json(json)
# print the JSON string representation of the object
print(QualityModel.to_json())

# convert the object into a dict
quality_model_dict = quality_model_instance.to_dict()
# create an instance of QualityModel from a dict
quality_model_form_dict = quality_model.from_dict(quality_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


