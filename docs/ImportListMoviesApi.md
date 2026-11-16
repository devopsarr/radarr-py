# radarr.ImportListMoviesApi

All URIs are relative to *http://localhost:7878*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_importlist_movie**](ImportListMoviesApi.md#create_importlist_movie) | **POST** /api/v3/importlist/movie | 
[**list_importlist_movie**](ImportListMoviesApi.md#list_importlist_movie) | **GET** /api/v3/importlist/movie | 


# **create_importlist_movie**
> List[MovieResource] create_importlist_movie(movie_resource=movie_resource)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.movie_resource import MovieResource
from radarr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:7878
# See configuration.py for a list of all supported configuration parameters.
configuration = radarr.Configuration(
    host = "http://localhost:7878"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with radarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = radarr.ImportListMoviesApi(api_client)
    movie_resource = [radarr.MovieResource()] # List[MovieResource] |  (optional)

    try:
        api_response = api_instance.create_importlist_movie(movie_resource=movie_resource)
        print("The response of ImportListMoviesApi->create_importlist_movie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportListMoviesApi->create_importlist_movie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_resource** | [**List[MovieResource]**](MovieResource.md)|  | [optional] 

### Return type

[**List[MovieResource]**](MovieResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_importlist_movie**
> List[ImportListMoviesResource] list_importlist_movie(include_recommendations=include_recommendations, include_trending=include_trending, include_popular=include_popular)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.import_list_movies_resource import ImportListMoviesResource
from radarr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:7878
# See configuration.py for a list of all supported configuration parameters.
configuration = radarr.Configuration(
    host = "http://localhost:7878"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with radarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = radarr.ImportListMoviesApi(api_client)
    include_recommendations = False # bool |  (optional) (default to False)
    include_trending = False # bool |  (optional) (default to False)
    include_popular = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.list_importlist_movie(include_recommendations=include_recommendations, include_trending=include_trending, include_popular=include_popular)
        print("The response of ImportListMoviesApi->list_importlist_movie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportListMoviesApi->list_importlist_movie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_recommendations** | **bool**|  | [optional] [default to False]
 **include_trending** | **bool**|  | [optional] [default to False]
 **include_popular** | **bool**|  | [optional] [default to False]

### Return type

[**List[ImportListMoviesResource]**](ImportListMoviesResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

