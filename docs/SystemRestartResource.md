# SystemRestartResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restarting** | **bool** |  | [optional] 

## Example

```python
from radarr.models.system_restart_resource import SystemRestartResource

# TODO update the JSON string below
json = "{}"
# create an instance of SystemRestartResource from a JSON string
system_restart_resource_instance = SystemRestartResource.from_json(json)
# print the JSON string representation of the object
print(SystemRestartResource.to_json())

# convert the object into a dict
system_restart_resource_dict = system_restart_resource_instance.to_dict()
# create an instance of SystemRestartResource from a dict
system_restart_resource_from_dict = SystemRestartResource.from_dict(system_restart_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


