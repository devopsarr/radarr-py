# ValidationFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**attempted_value** | **object** |  | [optional] 
**custom_state** | **object** |  | [optional] 
**severity** | [**Severity**](Severity.md) |  | [optional] 
**error_code** | **str** |  | [optional] 
**formatted_message_arguments** | **List[object]** |  | [optional] 
**formatted_message_placeholder_values** | **Dict[str, object]** |  | [optional] 

## Example

```python
from radarr.models.validation_failure import ValidationFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationFailure from a JSON string
validation_failure_instance = ValidationFailure.from_json(json)
# print the JSON string representation of the object
print(ValidationFailure.to_json())

# convert the object into a dict
validation_failure_dict = validation_failure_instance.to_dict()
# create an instance of ValidationFailure from a dict
validation_failure_from_dict = ValidationFailure.from_dict(validation_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


