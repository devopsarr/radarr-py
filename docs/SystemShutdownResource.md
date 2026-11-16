# SystemShutdownResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shutting_down** | **bool** |  | [optional] 

## Example

```python
from radarr.models.system_shutdown_resource import SystemShutdownResource

# TODO update the JSON string below
json = "{}"
# create an instance of SystemShutdownResource from a JSON string
system_shutdown_resource_instance = SystemShutdownResource.from_json(json)
# print the JSON string representation of the object
print(SystemShutdownResource.to_json())

# convert the object into a dict
system_shutdown_resource_dict = system_shutdown_resource_instance.to_dict()
# create an instance of SystemShutdownResource from a dict
system_shutdown_resource_from_dict = SystemShutdownResource.from_dict(system_shutdown_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


