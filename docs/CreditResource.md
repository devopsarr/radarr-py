# CreditResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**person_name** | **str** |  | [optional] 
**credit_tmdb_id** | **str** |  | [optional] 
**person_tmdb_id** | **int** |  | [optional] 
**movie_metadata_id** | **int** |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**department** | **str** |  | [optional] 
**job** | **str** |  | [optional] 
**character** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**type** | [**CreditType**](CreditType.md) |  | [optional] 

## Example

```python
from radarr.models.credit_resource import CreditResource

# TODO update the JSON string below
json = "{}"
# create an instance of CreditResource from a JSON string
credit_resource_instance = CreditResource.from_json(json)
# print the JSON string representation of the object
print CreditResource.to_json()

# convert the object into a dict
credit_resource_dict = credit_resource_instance.to_dict()
# create an instance of CreditResource from a dict
credit_resource_form_dict = credit_resource.from_dict(credit_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


