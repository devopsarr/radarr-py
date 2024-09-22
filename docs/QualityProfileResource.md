# QualityProfileResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**upgrade_allowed** | **bool** |  | [optional] 
**cutoff** | **int** |  | [optional] 
**items** | [**List[QualityProfileQualityItemResource]**](QualityProfileQualityItemResource.md) |  | [optional] 
**min_format_score** | **int** |  | [optional] 
**cutoff_format_score** | **int** |  | [optional] 
**min_upgrade_format_score** | **int** |  | [optional] 
**format_items** | [**List[ProfileFormatItemResource]**](ProfileFormatItemResource.md) |  | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 

## Example

```python
from radarr.models.quality_profile_resource import QualityProfileResource

# TODO update the JSON string below
json = "{}"
# create an instance of QualityProfileResource from a JSON string
quality_profile_resource_instance = QualityProfileResource.from_json(json)
# print the JSON string representation of the object
print(QualityProfileResource.to_json())

# convert the object into a dict
quality_profile_resource_dict = quality_profile_resource_instance.to_dict()
# create an instance of QualityProfileResource from a dict
quality_profile_resource_from_dict = QualityProfileResource.from_dict(quality_profile_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


