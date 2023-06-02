# MetadataBulkResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**apply_tags** | [**ApplyTags**](ApplyTags.md) |  | [optional] 

## Example

```python
from radarr.models.metadata_bulk_resource import MetadataBulkResource

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataBulkResource from a JSON string
metadata_bulk_resource_instance = MetadataBulkResource.from_json(json)
# print the JSON string representation of the object
print MetadataBulkResource.to_json()

# convert the object into a dict
metadata_bulk_resource_dict = metadata_bulk_resource_instance.to_dict()
# create an instance of MetadataBulkResource from a dict
metadata_bulk_resource_form_dict = metadata_bulk_resource.from_dict(metadata_bulk_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


