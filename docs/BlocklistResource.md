# BlocklistResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**movie_id** | **int** |  | [optional] 
**source_title** | **str** |  | [optional] 
**languages** | [**List[Language]**](Language.md) |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**custom_formats** | [**List[CustomFormatResource]**](CustomFormatResource.md) |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**protocol** | [**DownloadProtocol**](DownloadProtocol.md) |  | [optional] 
**indexer** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**movie** | [**MovieResource**](MovieResource.md) |  | [optional] 

## Example

```python
from radarr.models.blocklist_resource import BlocklistResource

# TODO update the JSON string below
json = "{}"
# create an instance of BlocklistResource from a JSON string
blocklist_resource_instance = BlocklistResource.from_json(json)
# print the JSON string representation of the object
print BlocklistResource.to_json()

# convert the object into a dict
blocklist_resource_dict = blocklist_resource_instance.to_dict()
# create an instance of BlocklistResource from a dict
blocklist_resource_form_dict = blocklist_resource.from_dict(blocklist_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


