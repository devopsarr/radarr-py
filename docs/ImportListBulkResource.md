# ImportListBulkResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**apply_tags** | [**ApplyTags**](ApplyTags.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**enable_auto** | **bool** |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**minimum_availability** | [**MovieStatusType**](MovieStatusType.md) |  | [optional] 

## Example

```python
from radarr.models.import_list_bulk_resource import ImportListBulkResource

# TODO update the JSON string below
json = "{}"
# create an instance of ImportListBulkResource from a JSON string
import_list_bulk_resource_instance = ImportListBulkResource.from_json(json)
# print the JSON string representation of the object
print(ImportListBulkResource.to_json())

# convert the object into a dict
import_list_bulk_resource_dict = import_list_bulk_resource_instance.to_dict()
# create an instance of ImportListBulkResource from a dict
import_list_bulk_resource_from_dict = ImportListBulkResource.from_dict(import_list_bulk_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


