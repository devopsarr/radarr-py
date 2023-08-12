# MovieFileResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**movie_id** | **int** |  | [optional] 
**relative_path** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**date_added** | **datetime** |  | [optional] 
**scene_name** | **str** |  | [optional] 
**indexer_flags** | **int** |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**custom_formats** | [**List[CustomFormatResource]**](CustomFormatResource.md) |  | [optional] 
**custom_format_score** | **int** |  | [optional] 
**media_info** | [**MediaInfoResource**](MediaInfoResource.md) |  | [optional] 
**original_file_path** | **str** |  | [optional] 
**quality_cutoff_not_met** | **bool** |  | [optional] 
**languages** | [**List[Language]**](Language.md) |  | [optional] 
**release_group** | **str** |  | [optional] 
**edition** | **str** |  | [optional] 

## Example

```python
from radarr.models.movie_file_resource import MovieFileResource

# TODO update the JSON string below
json = "{}"
# create an instance of MovieFileResource from a JSON string
movie_file_resource_instance = MovieFileResource.from_json(json)
# print the JSON string representation of the object
print MovieFileResource.to_json()

# convert the object into a dict
movie_file_resource_dict = movie_file_resource_instance.to_dict()
# create an instance of MovieFileResource from a dict
movie_file_resource_form_dict = movie_file_resource.from_dict(movie_file_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


