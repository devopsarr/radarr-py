# ParsedMovieInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movie_titles** | **List[str]** |  | [optional] 
**original_title** | **str** |  | [optional] 
**release_title** | **str** |  | [optional] 
**simple_release_title** | **str** |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**languages** | [**List[Language]**](Language.md) |  | [optional] 
**release_group** | **str** |  | [optional] 
**release_hash** | **str** |  | [optional] 
**edition** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**imdb_id** | **str** |  | [optional] 
**tmdb_id** | **int** |  | [optional] 
**hardcoded_subs** | **str** |  | [optional] 
**movie_title** | **str** |  | [optional] [readonly] 
**primary_movie_title** | **str** |  | [optional] [readonly] 

## Example

```python
from radarr.models.parsed_movie_info import ParsedMovieInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParsedMovieInfo from a JSON string
parsed_movie_info_instance = ParsedMovieInfo.from_json(json)
# print the JSON string representation of the object
print ParsedMovieInfo.to_json()

# convert the object into a dict
parsed_movie_info_dict = parsed_movie_info_instance.to_dict()
# create an instance of ParsedMovieInfo from a dict
parsed_movie_info_form_dict = parsed_movie_info.from_dict(parsed_movie_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


