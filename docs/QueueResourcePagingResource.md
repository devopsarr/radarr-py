# QueueResourcePagingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**sort_key** | **str** |  | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) |  | [optional] 
**total_records** | **int** |  | [optional] 
**records** | [**List[QueueResource]**](QueueResource.md) |  | [optional] 

## Example

```python
from radarr.models.queue_resource_paging_resource import QueueResourcePagingResource

# TODO update the JSON string below
json = "{}"
# create an instance of QueueResourcePagingResource from a JSON string
queue_resource_paging_resource_instance = QueueResourcePagingResource.from_json(json)
# print the JSON string representation of the object
print QueueResourcePagingResource.to_json()

# convert the object into a dict
queue_resource_paging_resource_dict = queue_resource_paging_resource_instance.to_dict()
# create an instance of QueueResourcePagingResource from a dict
queue_resource_paging_resource_form_dict = queue_resource_paging_resource.from_dict(queue_resource_paging_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


