# UnmappedFolder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from radarr.models.unmapped_folder import UnmappedFolder

# TODO update the JSON string below
json = "{}"
# create an instance of UnmappedFolder from a JSON string
unmapped_folder_instance = UnmappedFolder.from_json(json)
# print the JSON string representation of the object
print UnmappedFolder.to_json()

# convert the object into a dict
unmapped_folder_dict = unmapped_folder_instance.to_dict()
# create an instance of UnmappedFolder from a dict
unmapped_folder_form_dict = unmapped_folder.from_dict(unmapped_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


