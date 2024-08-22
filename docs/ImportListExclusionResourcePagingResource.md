# ImportListExclusionResourcePagingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**sort_key** | **str** |  | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) |  | [optional] 
**total_records** | **int** |  | [optional] 
**records** | [**List[ImportListExclusionResource]**](ImportListExclusionResource.md) |  | [optional] 

## Example

```python
from radarr.models.import_list_exclusion_resource_paging_resource import ImportListExclusionResourcePagingResource

# TODO update the JSON string below
json = "{}"
# create an instance of ImportListExclusionResourcePagingResource from a JSON string
import_list_exclusion_resource_paging_resource_instance = ImportListExclusionResourcePagingResource.from_json(json)
# print the JSON string representation of the object
print(ImportListExclusionResourcePagingResource.to_json())

# convert the object into a dict
import_list_exclusion_resource_paging_resource_dict = import_list_exclusion_resource_paging_resource_instance.to_dict()
# create an instance of ImportListExclusionResourcePagingResource from a dict
import_list_exclusion_resource_paging_resource_from_dict = ImportListExclusionResourcePagingResource.from_dict(import_list_exclusion_resource_paging_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


