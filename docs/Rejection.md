# Rejection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**type** | [**RejectionType**](RejectionType.md) |  | [optional] 

## Example

```python
from radarr.models.rejection import Rejection

# TODO update the JSON string below
json = "{}"
# create an instance of Rejection from a JSON string
rejection_instance = Rejection.from_json(json)
# print the JSON string representation of the object
print Rejection.to_json()

# convert the object into a dict
rejection_dict = rejection_instance.to_dict()
# create an instance of Rejection from a dict
rejection_form_dict = rejection.from_dict(rejection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


