# MovieResourcePagingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**sort_key** | **str** |  | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) |  | [optional] 
**total_records** | **int** |  | [optional] 
**records** | [**List[MovieResource]**](MovieResource.md) |  | [optional] 

## Example

```python
from radarr.models.movie_resource_paging_resource import MovieResourcePagingResource

# TODO update the JSON string below
json = "{}"
# create an instance of MovieResourcePagingResource from a JSON string
movie_resource_paging_resource_instance = MovieResourcePagingResource.from_json(json)
# print the JSON string representation of the object
print(MovieResourcePagingResource.to_json())

# convert the object into a dict
movie_resource_paging_resource_dict = movie_resource_paging_resource_instance.to_dict()
# create an instance of MovieResourcePagingResource from a dict
movie_resource_paging_resource_from_dict = MovieResourcePagingResource.from_dict(movie_resource_paging_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


