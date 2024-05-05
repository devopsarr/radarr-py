# IndexerResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**fields** | [**List[ContractField]**](ContractField.md) |  | [optional] 
**implementation_name** | **str** |  | [optional] 
**implementation** | **str** |  | [optional] 
**config_contract** | **str** |  | [optional] 
**info_link** | **str** |  | [optional] 
**message** | [**ProviderMessage**](ProviderMessage.md) |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**presets** | [**List[IndexerResource]**](IndexerResource.md) |  | [optional] 
**enable_rss** | **bool** |  | [optional] 
**enable_automatic_search** | **bool** |  | [optional] 
**enable_interactive_search** | **bool** |  | [optional] 
**supports_rss** | **bool** |  | [optional] 
**supports_search** | **bool** |  | [optional] 
**protocol** | [**DownloadProtocol**](DownloadProtocol.md) |  | [optional] 
**priority** | **int** |  | [optional] 
**download_client_id** | **int** |  | [optional] 

## Example

```python
from radarr.models.indexer_resource import IndexerResource

# TODO update the JSON string below
json = "{}"
# create an instance of IndexerResource from a JSON string
indexer_resource_instance = IndexerResource.from_json(json)
# print the JSON string representation of the object
print(IndexerResource.to_json())

# convert the object into a dict
indexer_resource_dict = indexer_resource_instance.to_dict()
# create an instance of IndexerResource from a dict
indexer_resource_from_dict = IndexerResource.from_dict(indexer_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


