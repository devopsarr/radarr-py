# QueueStatusResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**unknown_count** | **int** |  | [optional] 
**errors** | **bool** |  | [optional] 
**warnings** | **bool** |  | [optional] 
**unknown_errors** | **bool** |  | [optional] 
**unknown_warnings** | **bool** |  | [optional] 

## Example

```python
from radarr.models.queue_status_resource import QueueStatusResource

# TODO update the JSON string below
json = "{}"
# create an instance of QueueStatusResource from a JSON string
queue_status_resource_instance = QueueStatusResource.from_json(json)
# print the JSON string representation of the object
print QueueStatusResource.to_json()

# convert the object into a dict
queue_status_resource_dict = queue_status_resource_instance.to_dict()
# create an instance of QueueStatusResource from a dict
queue_status_resource_form_dict = queue_status_resource.from_dict(queue_status_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


