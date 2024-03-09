# QueueResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**movie_id** | **int** |  | [optional] 
**movie** | [**MovieResource**](MovieResource.md) |  | [optional] 
**languages** | [**List[Language]**](Language.md) |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**custom_formats** | [**List[CustomFormatResource]**](CustomFormatResource.md) |  | [optional] 
**custom_format_score** | **int** |  | [optional] 
**size** | **float** |  | [optional] 
**title** | **str** |  | [optional] 
**sizeleft** | **float** |  | [optional] 
**timeleft** | **str** |  | [optional] 
**estimated_completion_time** | **datetime** |  | [optional] 
**added** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**tracked_download_status** | [**TrackedDownloadStatus**](TrackedDownloadStatus.md) |  | [optional] 
**tracked_download_state** | [**TrackedDownloadState**](TrackedDownloadState.md) |  | [optional] 
**status_messages** | [**List[TrackedDownloadStatusMessage]**](TrackedDownloadStatusMessage.md) |  | [optional] 
**error_message** | **str** |  | [optional] 
**download_id** | **str** |  | [optional] 
**protocol** | [**DownloadProtocol**](DownloadProtocol.md) |  | [optional] 
**download_client** | **str** |  | [optional] 
**download_client_has_post_import_category** | **bool** |  | [optional] 
**indexer** | **str** |  | [optional] 
**output_path** | **str** |  | [optional] 

## Example

```python
from radarr.models.queue_resource import QueueResource

# TODO update the JSON string below
json = "{}"
# create an instance of QueueResource from a JSON string
queue_resource_instance = QueueResource.from_json(json)
# print the JSON string representation of the object
print QueueResource.to_json()

# convert the object into a dict
queue_resource_dict = queue_resource_instance.to_dict()
# create an instance of QueueResource from a dict
queue_resource_form_dict = queue_resource.from_dict(queue_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


