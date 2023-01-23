# MovieCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**clean_title** | **str** |  | [optional] 
**sort_title** | **str** |  | [optional] 
**tmdb_id** | **int** |  | [optional] 
**overview** | **str** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**search_on_add** | **bool** |  | [optional] 
**minimum_availability** | [**MovieStatusType**](MovieStatusType.md) |  | [optional] 
**last_info_sync** | **datetime** |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**added** | **datetime** |  | [optional] 
**movies** | [**List[MovieMetadata]**](MovieMetadata.md) |  | [optional] 

## Example

```python
from radarr.models.movie_collection import MovieCollection

# TODO update the JSON string below
json = "{}"
# create an instance of MovieCollection from a JSON string
movie_collection_instance = MovieCollection.from_json(json)
# print the JSON string representation of the object
print MovieCollection.to_json()

# convert the object into a dict
movie_collection_dict = movie_collection_instance.to_dict()
# create an instance of MovieCollection from a dict
movie_collection_form_dict = movie_collection.from_dict(movie_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


