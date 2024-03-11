# IndexerFlagResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_lower** | **str** |  | [optional] [readonly] 

## Example

```python
from radarr.models.indexer_flag_resource import IndexerFlagResource

# TODO update the JSON string below
json = "{}"
# create an instance of IndexerFlagResource from a JSON string
indexer_flag_resource_instance = IndexerFlagResource.from_json(json)
# print the JSON string representation of the object
print(IndexerFlagResource.to_json())

# convert the object into a dict
indexer_flag_resource_dict = indexer_flag_resource_instance.to_dict()
# create an instance of IndexerFlagResource from a dict
indexer_flag_resource_form_dict = indexer_flag_resource.from_dict(indexer_flag_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


