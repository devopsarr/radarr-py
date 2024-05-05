# QueueBulkResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 

## Example

```python
from radarr.models.queue_bulk_resource import QueueBulkResource

# TODO update the JSON string below
json = "{}"
# create an instance of QueueBulkResource from a JSON string
queue_bulk_resource_instance = QueueBulkResource.from_json(json)
# print the JSON string representation of the object
print(QueueBulkResource.to_json())

# convert the object into a dict
queue_bulk_resource_dict = queue_bulk_resource_instance.to_dict()
# create an instance of QueueBulkResource from a dict
queue_bulk_resource_from_dict = QueueBulkResource.from_dict(queue_bulk_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


