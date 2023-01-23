# CollectionMovieResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tmdb_id** | **int** |  | [optional] 
**imdb_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**clean_title** | **str** |  | [optional] 
**sort_title** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**runtime** | **int** |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**year** | **int** |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**folder** | **str** |  | [optional] 

## Example

```python
from radarr.models.collection_movie_resource import CollectionMovieResource

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionMovieResource from a JSON string
collection_movie_resource_instance = CollectionMovieResource.from_json(json)
# print the JSON string representation of the object
print CollectionMovieResource.to_json()

# convert the object into a dict
collection_movie_resource_dict = collection_movie_resource_instance.to_dict()
# create an instance of CollectionMovieResource from a dict
collection_movie_resource_form_dict = collection_movie_resource.from_dict(collection_movie_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


