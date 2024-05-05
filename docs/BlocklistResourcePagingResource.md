# BlocklistResourcePagingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**sort_key** | **str** |  | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) |  | [optional] 
**total_records** | **int** |  | [optional] 
**records** | [**List[BlocklistResource]**](BlocklistResource.md) |  | [optional] 

## Example

```python
from radarr.models.blocklist_resource_paging_resource import BlocklistResourcePagingResource

# TODO update the JSON string below
json = "{}"
# create an instance of BlocklistResourcePagingResource from a JSON string
blocklist_resource_paging_resource_instance = BlocklistResourcePagingResource.from_json(json)
# print the JSON string representation of the object
print(BlocklistResourcePagingResource.to_json())

# convert the object into a dict
blocklist_resource_paging_resource_dict = blocklist_resource_paging_resource_instance.to_dict()
# create an instance of BlocklistResourcePagingResource from a dict
blocklist_resource_paging_resource_from_dict = BlocklistResourcePagingResource.from_dict(blocklist_resource_paging_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


