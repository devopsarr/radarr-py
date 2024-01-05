# MovieResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**original_title** | **str** |  | [optional] 
**original_language** | [**Language**](Language.md) |  | [optional] 
**alternate_titles** | [**List[AlternativeTitleResource]**](AlternativeTitleResource.md) |  | [optional] 
**secondary_year** | **int** |  | [optional] 
**secondary_year_source_id** | **int** |  | [optional] 
**sort_title** | **str** |  | [optional] 
**size_on_disk** | **int** |  | [optional] 
**status** | [**MovieStatusType**](MovieStatusType.md) |  | [optional] 
**overview** | **str** |  | [optional] 
**in_cinemas** | **datetime** |  | [optional] 
**physical_release** | **datetime** |  | [optional] 
**digital_release** | **datetime** |  | [optional] 
**physical_release_note** | **str** |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**website** | **str** |  | [optional] 
**remote_poster** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**has_file** | **bool** |  | [optional] 
**you_tube_trailer_id** | **str** |  | [optional] 
**studio** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**minimum_availability** | [**MovieStatusType**](MovieStatusType.md) |  | [optional] 
**is_available** | **bool** |  | [optional] 
**folder_name** | **str** |  | [optional] 
**runtime** | **int** |  | [optional] 
**clean_title** | **str** |  | [optional] 
**imdb_id** | **str** |  | [optional] 
**tmdb_id** | **int** |  | [optional] 
**title_slug** | **str** |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**folder** | **str** |  | [optional] 
**certification** | **str** |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**added** | **datetime** |  | [optional] 
**add_options** | [**AddMovieOptions**](AddMovieOptions.md) |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**movie_file** | [**MovieFileResource**](MovieFileResource.md) |  | [optional] 
**collection** | [**MovieCollectionResource**](MovieCollectionResource.md) |  | [optional] 
**popularity** | **float** |  | [optional] 

## Example

```python
from radarr.models.movie_resource import MovieResource

# TODO update the JSON string below
json = "{}"
# create an instance of MovieResource from a JSON string
movie_resource_instance = MovieResource.from_json(json)
# print the JSON string representation of the object
print MovieResource.to_json()

# convert the object into a dict
movie_resource_dict = movie_resource_instance.to_dict()
# create an instance of MovieResource from a dict
movie_resource_form_dict = movie_resource.from_dict(movie_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


