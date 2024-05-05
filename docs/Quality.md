# Quality


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**source** | [**QualitySource**](QualitySource.md) |  | [optional] 
**resolution** | **int** |  | [optional] 
**modifier** | [**Modifier**](Modifier.md) |  | [optional] 

## Example

```python
from radarr.models.quality import Quality

# TODO update the JSON string below
json = "{}"
# create an instance of Quality from a JSON string
quality_instance = Quality.from_json(json)
# print the JSON string representation of the object
print(Quality.to_json())

# convert the object into a dict
quality_dict = quality_instance.to_dict()
# create an instance of Quality from a dict
quality_from_dict = Quality.from_dict(quality_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


