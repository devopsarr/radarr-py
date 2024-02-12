# MovieFileListResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movie_file_ids** | **List[int]** |  | [optional] 
**languages** | [**List[Language]**](Language.md) |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**edition** | **str** |  | [optional] 
**release_group** | **str** |  | [optional] 
**scene_name** | **str** |  | [optional] 
**indexer_flags** | **int** |  | [optional] 

## Example

```python
from radarr.models.movie_file_list_resource import MovieFileListResource

# TODO update the JSON string below
json = "{}"
# create an instance of MovieFileListResource from a JSON string
movie_file_list_resource_instance = MovieFileListResource.from_json(json)
# print the JSON string representation of the object
print MovieFileListResource.to_json()

# convert the object into a dict
movie_file_list_resource_dict = movie_file_list_resource_instance.to_dict()
# create an instance of MovieFileListResource from a dict
movie_file_list_resource_form_dict = movie_file_list_resource.from_dict(movie_file_list_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


