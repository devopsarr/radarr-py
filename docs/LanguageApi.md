# radarr.LanguageApi

All URIs are relative to *http://localhost:7878*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_language_by_id**](LanguageApi.md#get_language_by_id) | **GET** /api/v3/language/{id} | 
[**list_language**](LanguageApi.md#list_language) | **GET** /api/v3/language | 


# **get_language_by_id**
> LanguageResource get_language_by_id(id)



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
    api_instance = radarr.LanguageApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_language_by_id(id)
        print("The response of LanguageApi->get_language_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LanguageApi->get_language_by_id: %s\n" % e)
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
    api_instance = radarr.LanguageApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_language_by_id(id)
        print("The response of LanguageApi->get_language_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LanguageApi->get_language_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**LanguageResource**](LanguageResource.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_language**
> List[LanguageResource] list_language()



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
    api_instance = radarr.LanguageApi(api_client)

    try:
        api_response = api_instance.list_language()
        print("The response of LanguageApi->list_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LanguageApi->list_language: %s\n" % e)
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
    api_instance = radarr.LanguageApi(api_client)

    try:
        api_response = api_instance.list_language()
        print("The response of LanguageApi->list_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LanguageApi->list_language: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[LanguageResource]**](LanguageResource.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

