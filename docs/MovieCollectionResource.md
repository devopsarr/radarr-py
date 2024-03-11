# MovieCollectionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**tmdb_id** | **int** |  | [optional] 

## Example

```python
from radarr.models.movie_collection_resource import MovieCollectionResource

# TODO update the JSON string below
json = "{}"
# create an instance of MovieCollectionResource from a JSON string
movie_collection_resource_instance = MovieCollectionResource.from_json(json)
# print the JSON string representation of the object
print(MovieCollectionResource.to_json())

# convert the object into a dict
movie_collection_resource_dict = movie_collection_resource_instance.to_dict()
# create an instance of MovieCollectionResource from a dict
movie_collection_resource_form_dict = movie_collection_resource.from_dict(movie_collection_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


