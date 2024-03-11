# MovieEditorResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movie_ids** | **List[int]** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**minimum_availability** | [**MovieStatusType**](MovieStatusType.md) |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**apply_tags** | [**ApplyTags**](ApplyTags.md) |  | [optional] 
**move_files** | **bool** |  | [optional] 
**delete_files** | **bool** |  | [optional] 
**add_import_exclusion** | **bool** |  | [optional] 

## Example

```python
from radarr.models.movie_editor_resource import MovieEditorResource

# TODO update the JSON string below
json = "{}"
# create an instance of MovieEditorResource from a JSON string
movie_editor_resource_instance = MovieEditorResource.from_json(json)
# print the JSON string representation of the object
print(MovieEditorResource.to_json())

# convert the object into a dict
movie_editor_resource_dict = movie_editor_resource_instance.to_dict()
# create an instance of MovieEditorResource from a dict
movie_editor_resource_form_dict = movie_editor_resource.from_dict(movie_editor_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


