# radarr.QueueDetailsApi

All URIs are relative to *http://localhost:7878*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_queue_details**](QueueDetailsApi.md#list_queue_details) | **GET** /api/v3/queue/details | 


# **list_queue_details**
> List[QueueResource] list_queue_details(movie_id=movie_id, include_movie=include_movie)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.queue_resource import QueueResource
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
    api_instance = radarr.QueueDetailsApi(api_client)
    movie_id = 56 # int |  (optional)
    include_movie = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.list_queue_details(movie_id=movie_id, include_movie=include_movie)
        print("The response of QueueDetailsApi->list_queue_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueDetailsApi->list_queue_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | [optional] 
 **include_movie** | **bool**|  | [optional] [default to False]

### Return type

[**List[QueueResource]**](QueueResource.md)

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

