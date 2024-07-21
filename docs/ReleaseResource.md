# ReleaseResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**guid** | **str** |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**custom_formats** | [**List[CustomFormatResource]**](CustomFormatResource.md) |  | [optional] 
**custom_format_score** | **int** |  | [optional] 
**quality_weight** | **int** |  | [optional] 
**age** | **int** |  | [optional] 
**age_hours** | **float** |  | [optional] 
**age_minutes** | **float** |  | [optional] 
**size** | **int** |  | [optional] 
**indexer_id** | **int** |  | [optional] 
**indexer** | **str** |  | [optional] 
**release_group** | **str** |  | [optional] 
**sub_group** | **str** |  | [optional] 
**release_hash** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**scene_source** | **bool** |  | [optional] 
**movie_titles** | **List[str]** |  | [optional] 
**languages** | [**List[Language]**](Language.md) |  | [optional] 
**mapped_movie_id** | **int** |  | [optional] 
**approved** | **bool** |  | [optional] 
**temporarily_rejected** | **bool** |  | [optional] 
**rejected** | **bool** |  | [optional] 
**tmdb_id** | **int** |  | [optional] 
**imdb_id** | **int** |  | [optional] 
**rejections** | **List[str]** |  | [optional] 
**publish_date** | **datetime** |  | [optional] 
**comment_url** | **str** |  | [optional] 
**download_url** | **str** |  | [optional] 
**info_url** | **str** |  | [optional] 
**download_allowed** | **bool** |  | [optional] 
**release_weight** | **int** |  | [optional] 
**edition** | **str** |  | [optional] 
**magnet_url** | **str** |  | [optional] 
**info_hash** | **str** |  | [optional] 
**seeders** | **int** |  | [optional] 
**leechers** | **int** |  | [optional] 
**protocol** | [**DownloadProtocol**](DownloadProtocol.md) |  | [optional] 
**indexer_flags** | **object** |  | [optional] 
**movie_id** | **int** |  | [optional] 
**download_client_id** | **int** |  | [optional] 
**download_client** | **str** |  | [optional] 
**should_override** | **bool** |  | [optional] 

## Example

```python
from radarr.models.release_resource import ReleaseResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseResource from a JSON string
release_resource_instance = ReleaseResource.from_json(json)
# print the JSON string representation of the object
print(ReleaseResource.to_json())

# convert the object into a dict
release_resource_dict = release_resource_instance.to_dict()
# create an instance of ReleaseResource from a dict
release_resource_from_dict = ReleaseResource.from_dict(release_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


