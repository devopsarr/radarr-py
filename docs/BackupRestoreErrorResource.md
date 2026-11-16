# BackupRestoreErrorResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 

## Example

```python
from radarr.models.backup_restore_error_resource import BackupRestoreErrorResource

# TODO update the JSON string below
json = "{}"
# create an instance of BackupRestoreErrorResource from a JSON string
backup_restore_error_resource_instance = BackupRestoreErrorResource.from_json(json)
# print the JSON string representation of the object
print(BackupRestoreErrorResource.to_json())

# convert the object into a dict
backup_restore_error_resource_dict = backup_restore_error_resource_instance.to_dict()
# create an instance of BackupRestoreErrorResource from a dict
backup_restore_error_resource_from_dict = BackupRestoreErrorResource.from_dict(backup_restore_error_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


