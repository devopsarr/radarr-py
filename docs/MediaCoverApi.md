# radarr.MediaCoverApi

All URIs are relative to *http://localhost:7878*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_media_covermovie_id_by_filename**](MediaCoverApi.md#get_media_covermovie_id_by_filename) | **GET** /api/v3/mediacover/{movieId}/{filename} | 


# **get_media_covermovie_id_by_filename**
> get_media_covermovie_id_by_filename(movie_id, filename)



### Example

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
import radarr
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

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with radarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = radarr.MediaCoverApi(api_client)
    movie_id = 56 # int | 
    filename = 'filename_example' # str | 

    try:
        api_instance.get_media_covermovie_id_by_filename(movie_id, filename)
    except Exception as e:
        print("Exception when calling MediaCoverApi->get_media_covermovie_id_by_filename: %s\n" % e)
```

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
import radarr
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

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with radarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = radarr.MediaCoverApi(api_client)
    movie_id = 56 # int | 
    filename = 'filename_example' # str | 

    try:
        api_instance.get_media_covermovie_id_by_filename(movie_id, filename)
    except Exception as e:
        print("Exception when calling MediaCoverApi->get_media_covermovie_id_by_filename: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 
 **filename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

