# QualityProfileQualityItemResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**quality** | [**Quality**](Quality.md) |  | [optional] 
**items** | [**List[QualityProfileQualityItemResource]**](QualityProfileQualityItemResource.md) |  | [optional] 
**allowed** | **bool** |  | [optional] 

## Example

```python
from radarr.models.quality_profile_quality_item_resource import QualityProfileQualityItemResource

# TODO update the JSON string below
json = "{}"
# create an instance of QualityProfileQualityItemResource from a JSON string
quality_profile_quality_item_resource_instance = QualityProfileQualityItemResource.from_json(json)
# print the JSON string representation of the object
print(QualityProfileQualityItemResource.to_json())

# convert the object into a dict
quality_profile_quality_item_resource_dict = quality_profile_quality_item_resource_instance.to_dict()
# create an instance of QualityProfileQualityItemResource from a dict
quality_profile_quality_item_resource_form_dict = quality_profile_quality_item_resource.from_dict(quality_profile_quality_item_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


