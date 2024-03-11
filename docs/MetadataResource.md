# MetadataResource


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
**presets** | [**List[MetadataResource]**](MetadataResource.md) |  | [optional] 
**enable** | **bool** |  | [optional] 

## Example

```python
from radarr.models.metadata_resource import MetadataResource

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataResource from a JSON string
metadata_resource_instance = MetadataResource.from_json(json)
# print the JSON string representation of the object
print(MetadataResource.to_json())

# convert the object into a dict
metadata_resource_dict = metadata_resource_instance.to_dict()
# create an instance of MetadataResource from a dict
metadata_resource_form_dict = metadata_resource.from_dict(metadata_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


