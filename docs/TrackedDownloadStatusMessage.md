# TrackedDownloadStatusMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**messages** | **List[str]** |  | [optional] 

## Example

```python
from radarr.models.tracked_download_status_message import TrackedDownloadStatusMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedDownloadStatusMessage from a JSON string
tracked_download_status_message_instance = TrackedDownloadStatusMessage.from_json(json)
# print the JSON string representation of the object
print(TrackedDownloadStatusMessage.to_json())

# convert the object into a dict
tracked_download_status_message_dict = tracked_download_status_message_instance.to_dict()
# create an instance of TrackedDownloadStatusMessage from a dict
tracked_download_status_message_form_dict = tracked_download_status_message.from_dict(tracked_download_status_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


