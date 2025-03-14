# radarr.AlternativeTitleApi

All URIs are relative to *http://localhost:7878*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alttitle_by_id**](AlternativeTitleApi.md#get_alttitle_by_id) | **GET** /api/v3/alttitle/{id} | 
[**list_alttitle**](AlternativeTitleApi.md#list_alttitle) | **GET** /api/v3/alttitle | 


# **get_alttitle_by_id**
> AlternativeTitleResource get_alttitle_by_id(id)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.alternative_title_resource import AlternativeTitleResource
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
    api_instance = radarr.AlternativeTitleApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_alttitle_by_id(id)
        print("The response of AlternativeTitleApi->get_alttitle_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlternativeTitleApi->get_alttitle_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AlternativeTitleResource**](AlternativeTitleResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alttitle**
> List[AlternativeTitleResource] list_alttitle(movie_id=movie_id, movie_metadata_id=movie_metadata_id)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.alternative_title_resource import AlternativeTitleResource
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
    api_instance = radarr.AlternativeTitleApi(api_client)
    movie_id = 56 # int |  (optional)
    movie_metadata_id = 56 # int |  (optional)

    try:
        api_response = api_instance.list_alttitle(movie_id=movie_id, movie_metadata_id=movie_metadata_id)
        print("The response of AlternativeTitleApi->list_alttitle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlternativeTitleApi->list_alttitle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | [optional] 
 **movie_metadata_id** | **int**|  | [optional] 

### Return type

[**List[AlternativeTitleResource]**](AlternativeTitleResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

