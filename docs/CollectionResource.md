# CollectionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**sort_title** | **str** |  | [optional] 
**tmdb_id** | **int** |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**overview** | **str** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**search_on_add** | **bool** |  | [optional] 
**minimum_availability** | [**MovieStatusType**](MovieStatusType.md) |  | [optional] 
**movies** | [**List[CollectionMovieResource]**](CollectionMovieResource.md) |  | [optional] 
**missing_movies** | **int** |  | [optional] 
**tags** | **List[int]** |  | [optional] 

## Example

```python
from radarr.models.collection_resource import CollectionResource

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionResource from a JSON string
collection_resource_instance = CollectionResource.from_json(json)
# print the JSON string representation of the object
print CollectionResource.to_json()

# convert the object into a dict
collection_resource_dict = collection_resource_instance.to_dict()
# create an instance of CollectionResource from a dict
collection_resource_form_dict = collection_resource.from_dict(collection_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


