# ImportListConfigResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**list_sync_level** | **str** |  | [optional] 
**import_exclusions** | **str** |  | [optional] 

## Example

```python
from radarr.models.import_list_config_resource import ImportListConfigResource

# TODO update the JSON string below
json = "{}"
# create an instance of ImportListConfigResource from a JSON string
import_list_config_resource_instance = ImportListConfigResource.from_json(json)
# print the JSON string representation of the object
print ImportListConfigResource.to_json()

# convert the object into a dict
import_list_config_resource_dict = import_list_config_resource_instance.to_dict()
# create an instance of ImportListConfigResource from a dict
import_list_config_resource_form_dict = import_list_config_resource.from_dict(import_list_config_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


