# ManualImportReprocessResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**movie_id** | **int** |  | [optional] 
**movie** | [**MovieResource**](MovieResource.md) |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**languages** | [**List[Language]**](Language.md) |  | [optional] 
**release_group** | **str** |  | [optional] 
**download_id** | **str** |  | [optional] 
**custom_formats** | [**List[CustomFormatResource]**](CustomFormatResource.md) |  | [optional] 
**custom_format_score** | **int** |  | [optional] 
**indexer_flags** | **int** |  | [optional] 
**rejections** | [**List[ImportRejectionResource]**](ImportRejectionResource.md) |  | [optional] 

## Example

```python
from radarr.models.manual_import_reprocess_resource import ManualImportReprocessResource

# TODO update the JSON string below
json = "{}"
# create an instance of ManualImportReprocessResource from a JSON string
manual_import_reprocess_resource_instance = ManualImportReprocessResource.from_json(json)
# print the JSON string representation of the object
print(ManualImportReprocessResource.to_json())

# convert the object into a dict
manual_import_reprocess_resource_dict = manual_import_reprocess_resource_instance.to_dict()
# create an instance of ManualImportReprocessResource from a dict
manual_import_reprocess_resource_from_dict = ManualImportReprocessResource.from_dict(manual_import_reprocess_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


