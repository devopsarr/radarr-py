# ManualImportResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**relative_path** | **str** |  | [optional] 
**folder_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**movie** | [**MovieResource**](MovieResource.md) |  | [optional] 
**movie_file_id** | **int** |  | [optional] 
**release_group** | **str** |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**languages** | [**List[Language]**](Language.md) |  | [optional] 
**quality_weight** | **int** |  | [optional] 
**download_id** | **str** |  | [optional] 
**custom_formats** | [**List[CustomFormatResource]**](CustomFormatResource.md) |  | [optional] 
**custom_format_score** | **int** |  | [optional] 
**indexer_flags** | **int** |  | [optional] 
**rejections** | [**List[ImportRejectionResource]**](ImportRejectionResource.md) |  | [optional] 

## Example

```python
from radarr.models.manual_import_resource import ManualImportResource

# TODO update the JSON string below
json = "{}"
# create an instance of ManualImportResource from a JSON string
manual_import_resource_instance = ManualImportResource.from_json(json)
# print the JSON string representation of the object
print(ManualImportResource.to_json())

# convert the object into a dict
manual_import_resource_dict = manual_import_resource_instance.to_dict()
# create an instance of ManualImportResource from a dict
manual_import_resource_from_dict = ManualImportResource.from_dict(manual_import_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


