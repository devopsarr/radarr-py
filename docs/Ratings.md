# Ratings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imdb** | [**RatingChild**](RatingChild.md) |  | [optional] 
**tmdb** | [**RatingChild**](RatingChild.md) |  | [optional] 
**metacritic** | [**RatingChild**](RatingChild.md) |  | [optional] 
**rotten_tomatoes** | [**RatingChild**](RatingChild.md) |  | [optional] 

## Example

```python
from radarr.models.ratings import Ratings

# TODO update the JSON string below
json = "{}"
# create an instance of Ratings from a JSON string
ratings_instance = Ratings.from_json(json)
# print the JSON string representation of the object
print Ratings.to_json()

# convert the object into a dict
ratings_dict = ratings_instance.to_dict()
# create an instance of Ratings from a dict
ratings_form_dict = ratings.from_dict(ratings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


