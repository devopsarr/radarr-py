# ImportRejectionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**type** | [**RejectionType**](RejectionType.md) |  | [optional] 

## Example

```python
from radarr.models.import_rejection_resource import ImportRejectionResource

# TODO update the JSON string below
json = "{}"
# create an instance of ImportRejectionResource from a JSON string
import_rejection_resource_instance = ImportRejectionResource.from_json(json)
# print the JSON string representation of the object
print(ImportRejectionResource.to_json())

# convert the object into a dict
import_rejection_resource_dict = import_rejection_resource_instance.to_dict()
# create an instance of ImportRejectionResource from a dict
import_rejection_resource_from_dict = ImportRejectionResource.from_dict(import_rejection_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


