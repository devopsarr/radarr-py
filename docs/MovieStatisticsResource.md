# MovieStatisticsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movie_file_count** | **int** |  | [optional] 
**size_on_disk** | **int** |  | [optional] 
**release_groups** | **List[str]** |  | [optional] 

## Example

```python
from radarr.models.movie_statistics_resource import MovieStatisticsResource

# TODO update the JSON string below
json = "{}"
# create an instance of MovieStatisticsResource from a JSON string
movie_statistics_resource_instance = MovieStatisticsResource.from_json(json)
# print the JSON string representation of the object
print(MovieStatisticsResource.to_json())

# convert the object into a dict
movie_statistics_resource_dict = movie_statistics_resource_instance.to_dict()
# create an instance of MovieStatisticsResource from a dict
movie_statistics_resource_form_dict = movie_statistics_resource.from_dict(movie_statistics_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


