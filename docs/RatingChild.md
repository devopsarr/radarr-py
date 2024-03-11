# RatingChild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**votes** | **int** |  | [optional] 
**value** | **float** |  | [optional] 
**type** | [**RatingType**](RatingType.md) |  | [optional] 

## Example

```python
from radarr.models.rating_child import RatingChild

# TODO update the JSON string below
json = "{}"
# create an instance of RatingChild from a JSON string
rating_child_instance = RatingChild.from_json(json)
# print the JSON string representation of the object
print(RatingChild.to_json())

# convert the object into a dict
rating_child_dict = rating_child_instance.to_dict()
# create an instance of RatingChild from a dict
rating_child_form_dict = rating_child.from_dict(rating_child_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


