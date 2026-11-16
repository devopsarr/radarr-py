# ImportListMoviesResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**sort_title** | **str** |  | [optional] 
**original_language** | [**Language**](Language.md) |  | [optional] 
**status** | [**MovieStatusType**](MovieStatusType.md) |  | [optional] 
**overview** | **str** |  | [optional] 
**in_cinemas** | **datetime** |  | [optional] 
**physical_release** | **datetime** |  | [optional] 
**digital_release** | **datetime** |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**website** | **str** |  | [optional] 
**remote_poster** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**you_tube_trailer_id** | **str** |  | [optional] 
**studio** | **str** |  | [optional] 
**runtime** | **int** |  | [optional] 
**imdb_id** | **str** |  | [optional] 
**tmdb_id** | **int** |  | [optional] 
**folder** | **str** |  | [optional] 
**certification** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**collection** | [**MovieCollection**](MovieCollection.md) |  | [optional] 
**is_excluded** | **bool** |  | [optional] 
**is_existing** | **bool** |  | [optional] 
**is_trending** | **bool** |  | [optional] 
**is_popular** | **bool** |  | [optional] 
**is_recommendation** | **bool** |  | [optional] 
**lists** | **List[int]** |  | [optional] 

## Example

```python
from radarr.models.import_list_movies_resource import ImportListMoviesResource

# TODO update the JSON string below
json = "{}"
# create an instance of ImportListMoviesResource from a JSON string
import_list_movies_resource_instance = ImportListMoviesResource.from_json(json)
# print the JSON string representation of the object
print(ImportListMoviesResource.to_json())

# convert the object into a dict
import_list_movies_resource_dict = import_list_movies_resource_instance.to_dict()
# create an instance of ImportListMoviesResource from a dict
import_list_movies_resource_from_dict = ImportListMoviesResource.from_dict(import_list_movies_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


