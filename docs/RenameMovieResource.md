# RenameMovieResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**movie_id** | **int** |  | [optional] 
**movie_file_id** | **int** |  | [optional] 
**existing_path** | **str** |  | [optional] 
**new_path** | **str** |  | [optional] 

## Example

```python
from radarr.models.rename_movie_resource import RenameMovieResource

# TODO update the JSON string below
json = "{}"
# create an instance of RenameMovieResource from a JSON string
rename_movie_resource_instance = RenameMovieResource.from_json(json)
# print the JSON string representation of the object
print RenameMovieResource.to_json()

# convert the object into a dict
rename_movie_resource_dict = rename_movie_resource_instance.to_dict()
# create an instance of RenameMovieResource from a dict
rename_movie_resource_form_dict = rename_movie_resource.from_dict(rename_movie_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


