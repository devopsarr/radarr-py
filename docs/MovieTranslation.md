# MovieTranslation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**movie_metadata_id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**clean_title** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 

## Example

```python
from radarr.models.movie_translation import MovieTranslation

# TODO update the JSON string below
json = "{}"
# create an instance of MovieTranslation from a JSON string
movie_translation_instance = MovieTranslation.from_json(json)
# print the JSON string representation of the object
print MovieTranslation.to_json()

# convert the object into a dict
movie_translation_dict = movie_translation_instance.to_dict()
# create an instance of MovieTranslation from a dict
movie_translation_form_dict = movie_translation.from_dict(movie_translation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


