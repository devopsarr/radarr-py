# BackupRestoreResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restart_required** | **bool** |  | [optional] 

## Example

```python
from radarr.models.backup_restore_resource import BackupRestoreResource

# TODO update the JSON string below
json = "{}"
# create an instance of BackupRestoreResource from a JSON string
backup_restore_resource_instance = BackupRestoreResource.from_json(json)
# print the JSON string representation of the object
print(BackupRestoreResource.to_json())

# convert the object into a dict
backup_restore_resource_dict = backup_restore_resource_instance.to_dict()
# create an instance of BackupRestoreResource from a dict
backup_restore_resource_from_dict = BackupRestoreResource.from_dict(backup_restore_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


