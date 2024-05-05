# ImportListResource


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
**presets** | [**List[ImportListResource]**](ImportListResource.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**enable_auto** | **bool** |  | [optional] 
**monitor** | [**MonitorTypes**](MonitorTypes.md) |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**search_on_add** | **bool** |  | [optional] 
**minimum_availability** | [**MovieStatusType**](MovieStatusType.md) |  | [optional] 
**list_type** | [**ImportListType**](ImportListType.md) |  | [optional] 
**list_order** | **int** |  | [optional] 
**min_refresh_interval** | **str** |  | [optional] 

## Example

```python
from radarr.models.import_list_resource import ImportListResource

# TODO update the JSON string below
json = "{}"
# create an instance of ImportListResource from a JSON string
import_list_resource_instance = ImportListResource.from_json(json)
# print the JSON string representation of the object
print(ImportListResource.to_json())

# convert the object into a dict
import_list_resource_dict = import_list_resource_instance.to_dict()
# create an instance of ImportListResource from a dict
import_list_resource_from_dict = ImportListResource.from_dict(import_list_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


