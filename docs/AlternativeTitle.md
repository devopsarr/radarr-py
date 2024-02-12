# AlternativeTitle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**source_type** | [**SourceType**](SourceType.md) |  | [optional] 
**movie_metadata_id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**clean_title** | **str** |  | [optional] 

## Example

```python
from radarr.models.alternative_title import AlternativeTitle

# TODO update the JSON string below
json = "{}"
# create an instance of AlternativeTitle from a JSON string
alternative_title_instance = AlternativeTitle.from_json(json)
# print the JSON string representation of the object
print AlternativeTitle.to_json()

# convert the object into a dict
alternative_title_dict = alternative_title_instance.to_dict()
# create an instance of AlternativeTitle from a dict
alternative_title_form_dict = alternative_title.from_dict(alternative_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


