# MetadataConfigResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**certification_country** | [**TMDbCountryCode**](TMDbCountryCode.md) |  | [optional] 

## Example

```python
from radarr.models.metadata_config_resource import MetadataConfigResource

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataConfigResource from a JSON string
metadata_config_resource_instance = MetadataConfigResource.from_json(json)
# print the JSON string representation of the object
print MetadataConfigResource.to_json()

# convert the object into a dict
metadata_config_resource_dict = metadata_config_resource_instance.to_dict()
# create an instance of MetadataConfigResource from a dict
metadata_config_resource_form_dict = metadata_config_resource.from_dict(metadata_config_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


