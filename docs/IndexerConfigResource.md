# IndexerConfigResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**minimum_age** | **int** |  | [optional] 
**maximum_size** | **int** |  | [optional] 
**retention** | **int** |  | [optional] 
**rss_sync_interval** | **int** |  | [optional] 
**prefer_indexer_flags** | **bool** |  | [optional] 
**availability_delay** | **int** |  | [optional] 
**allow_hardcoded_subs** | **bool** |  | [optional] 
**whitelisted_hardcoded_subs** | **str** |  | [optional] 

## Example

```python
from radarr.models.indexer_config_resource import IndexerConfigResource

# TODO update the JSON string below
json = "{}"
# create an instance of IndexerConfigResource from a JSON string
indexer_config_resource_instance = IndexerConfigResource.from_json(json)
# print the JSON string representation of the object
print(IndexerConfigResource.to_json())

# convert the object into a dict
indexer_config_resource_dict = indexer_config_resource_instance.to_dict()
# create an instance of IndexerConfigResource from a dict
indexer_config_resource_from_dict = IndexerConfigResource.from_dict(indexer_config_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


