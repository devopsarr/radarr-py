# DelayProfileResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**enable_usenet** | **bool** |  | [optional] 
**enable_torrent** | **bool** |  | [optional] 
**preferred_protocol** | [**DownloadProtocol**](DownloadProtocol.md) |  | [optional] 
**usenet_delay** | **int** |  | [optional] 
**torrent_delay** | **int** |  | [optional] 
**bypass_if_highest_quality** | **bool** |  | [optional] 
**order** | **int** |  | [optional] 
**tags** | **List[int]** |  | [optional] 

## Example

```python
from radarr.models.delay_profile_resource import DelayProfileResource

# TODO update the JSON string below
json = "{}"
# create an instance of DelayProfileResource from a JSON string
delay_profile_resource_instance = DelayProfileResource.from_json(json)
# print the JSON string representation of the object
print DelayProfileResource.to_json()

# convert the object into a dict
delay_profile_resource_dict = delay_profile_resource_instance.to_dict()
# create an instance of DelayProfileResource from a dict
delay_profile_resource_form_dict = delay_profile_resource.from_dict(delay_profile_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


