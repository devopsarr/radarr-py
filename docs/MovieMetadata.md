# MovieMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**tmdb_id** | **int** |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**in_cinemas** | **datetime** |  | [optional] 
**physical_release** | **datetime** |  | [optional] 
**digital_release** | **datetime** |  | [optional] 
**certification** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**collection_tmdb_id** | **int** |  | [optional] 
**collection_title** | **str** |  | [optional] 
**last_info_sync** | **datetime** |  | [optional] 
**runtime** | **int** |  | [optional] 
**website** | **str** |  | [optional] 
**imdb_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**clean_title** | **str** |  | [optional] 
**sort_title** | **str** |  | [optional] 
**status** | [**MovieStatusType**](MovieStatusType.md) |  | [optional] 
**overview** | **str** |  | [optional] 
**alternative_titles** | [**List[AlternativeTitle]**](AlternativeTitle.md) |  | [optional] 
**translations** | [**List[MovieTranslation]**](MovieTranslation.md) |  | [optional] 
**secondary_year** | **int** |  | [optional] 
**you_tube_trailer_id** | **str** |  | [optional] 
**studio** | **str** |  | [optional] 
**original_title** | **str** |  | [optional] 
**clean_original_title** | **str** |  | [optional] 
**original_language** | [**Language**](Language.md) |  | [optional] 
**recommendations** | **List[int]** |  | [optional] 
**popularity** | **float** |  | [optional] 
**is_recent_movie** | **bool** |  | [optional] [readonly] 

## Example

```python
from radarr.models.movie_metadata import MovieMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of MovieMetadata from a JSON string
movie_metadata_instance = MovieMetadata.from_json(json)
# print the JSON string representation of the object
print MovieMetadata.to_json()

# convert the object into a dict
movie_metadata_dict = movie_metadata_instance.to_dict()
# create an instance of MovieMetadata from a dict
movie_metadata_form_dict = movie_metadata.from_dict(movie_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


