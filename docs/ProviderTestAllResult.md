# ProviderTestAllResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**is_valid** | **bool** |  | [optional] [readonly] 
**validation_failures** | [**List[ValidationFailure]**](ValidationFailure.md) |  | [optional] 

## Example

```python
from radarr.models.provider_test_all_result import ProviderTestAllResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderTestAllResult from a JSON string
provider_test_all_result_instance = ProviderTestAllResult.from_json(json)
# print the JSON string representation of the object
print(ProviderTestAllResult.to_json())

# convert the object into a dict
provider_test_all_result_dict = provider_test_all_result_instance.to_dict()
# create an instance of ProviderTestAllResult from a dict
provider_test_all_result_from_dict = ProviderTestAllResult.from_dict(provider_test_all_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


