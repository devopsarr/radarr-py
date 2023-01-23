# ImportExclusionsResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**fields** | [**List[Field]**](Field.md) |  | [optional] 
**implementation_name** | **str** |  | [optional] 
**implementation** | **str** |  | [optional] 
**config_contract** | **str** |  | [optional] 
**info_link** | **str** |  | [optional] 
**message** | [**ProviderMessage**](ProviderMessage.md) |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**presets** | [**List[ImportExclusionsResource]**](ImportExclusionsResource.md) |  | [optional] 
**tmdb_id** | **int** |  | [optional] 
**movie_title** | **str** |  | [optional] 
**movie_year** | **int** |  | [optional] 

## Example

```python
from radarr.models.import_exclusions_resource import ImportExclusionsResource

# TODO update the JSON string below
json = "{}"
# create an instance of ImportExclusionsResource from a JSON string
import_exclusions_resource_instance = ImportExclusionsResource.from_json(json)
# print the JSON string representation of the object
print ImportExclusionsResource.to_json()

# convert the object into a dict
import_exclusions_resource_dict = import_exclusions_resource_instance.to_dict()
# create an instance of ImportExclusionsResource from a dict
import_exclusions_resource_form_dict = import_exclusions_resource.from_dict(import_exclusions_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


