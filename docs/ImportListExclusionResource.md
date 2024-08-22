# ImportListExclusionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**fields** | [**List[ContractField]**](ContractField.md) |  | [optional] 
**implementation_name** | **str** |  | [optional] 
**implementation** | **str** |  | [optional] 
**config_contract** | **str** |  | [optional] 
**info_link** | **str** |  | [optional] 
**message** | [**ProviderMessage**](ProviderMessage.md) |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**presets** | [**List[ImportListExclusionResource]**](ImportListExclusionResource.md) |  | [optional] 
**tmdb_id** | **int** |  | [optional] 
**movie_title** | **str** |  | [optional] 
**movie_year** | **int** |  | [optional] 

## Example

```python
from radarr.models.import_list_exclusion_resource import ImportListExclusionResource

# TODO update the JSON string below
json = "{}"
# create an instance of ImportListExclusionResource from a JSON string
import_list_exclusion_resource_instance = ImportListExclusionResource.from_json(json)
# print the JSON string representation of the object
print(ImportListExclusionResource.to_json())

# convert the object into a dict
import_list_exclusion_resource_dict = import_list_exclusion_resource_instance.to_dict()
# create an instance of ImportListExclusionResource from a dict
import_list_exclusion_resource_from_dict = ImportListExclusionResource.from_dict(import_list_exclusion_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


