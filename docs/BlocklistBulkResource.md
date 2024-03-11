# BlocklistBulkResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 

## Example

```python
from radarr.models.blocklist_bulk_resource import BlocklistBulkResource

# TODO update the JSON string below
json = "{}"
# create an instance of BlocklistBulkResource from a JSON string
blocklist_bulk_resource_instance = BlocklistBulkResource.from_json(json)
# print the JSON string representation of the object
print(BlocklistBulkResource.to_json())

# convert the object into a dict
blocklist_bulk_resource_dict = blocklist_bulk_resource_instance.to_dict()
# create an instance of BlocklistBulkResource from a dict
blocklist_bulk_resource_form_dict = blocklist_bulk_resource.from_dict(blocklist_bulk_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


