# MovieFolderResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | **str** |  | [optional] 

## Example

```python
from radarr.models.movie_folder_resource import MovieFolderResource

# TODO update the JSON string below
json = "{}"
# create an instance of MovieFolderResource from a JSON string
movie_folder_resource_instance = MovieFolderResource.from_json(json)
# print the JSON string representation of the object
print(MovieFolderResource.to_json())

# convert the object into a dict
movie_folder_resource_dict = movie_folder_resource_instance.to_dict()
# create an instance of MovieFolderResource from a dict
movie_folder_resource_from_dict = MovieFolderResource.from_dict(movie_folder_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


