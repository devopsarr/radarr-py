# radarr.RestrictionApi

All URIs are relative to *http://localhost:7878*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_restriction**](RestrictionApi.md#create_restriction) | **POST** /api/v3/restriction | 
[**delete_restriction**](RestrictionApi.md#delete_restriction) | **DELETE** /api/v3/restriction/{id} | 
[**get_restriction_by_id**](RestrictionApi.md#get_restriction_by_id) | **GET** /api/v3/restriction/{id} | 
[**list_restriction**](RestrictionApi.md#list_restriction) | **GET** /api/v3/restriction | 
[**update_restriction**](RestrictionApi.md#update_restriction) | **PUT** /api/v3/restriction/{id} | 


# **create_restriction**
> RestrictionResource create_restriction(restriction_resource=restriction_resource)



### Example

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
    api_instance = radarr.RestrictionApi(api_client)
    restriction_resource = radarr.RestrictionResource() # RestrictionResource |  (optional)

    try:
        api_response = api_instance.create_restriction(restriction_resource=restriction_resource)
        print("The response of RestrictionApi->create_restriction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestrictionApi->create_restriction: %s\n" % e)
```

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
    api_instance = radarr.RestrictionApi(api_client)
    restriction_resource = radarr.RestrictionResource() # RestrictionResource |  (optional)

    try:
        api_response = api_instance.create_restriction(restriction_resource=restriction_resource)
        print("The response of RestrictionApi->create_restriction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestrictionApi->create_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restriction_resource** | [**RestrictionResource**](RestrictionResource.md)|  | [optional] 

### Return type

[**RestrictionResource**](RestrictionResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_restriction**
> delete_restriction(id)



### Example

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
    api_instance = radarr.RestrictionApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_restriction(id)
    except Exception as e:
        print("Exception when calling RestrictionApi->delete_restriction: %s\n" % e)
```

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
    api_instance = radarr.RestrictionApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_restriction(id)
    except Exception as e:
        print("Exception when calling RestrictionApi->delete_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_restriction_by_id**
> RestrictionResource get_restriction_by_id(id)



### Example

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
    api_instance = radarr.RestrictionApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_restriction_by_id(id)
        print("The response of RestrictionApi->get_restriction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestrictionApi->get_restriction_by_id: %s\n" % e)
```

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
    api_instance = radarr.RestrictionApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_restriction_by_id(id)
        print("The response of RestrictionApi->get_restriction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestrictionApi->get_restriction_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RestrictionResource**](RestrictionResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_restriction**
> List[RestrictionResource] list_restriction()



### Example

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
    api_instance = radarr.RestrictionApi(api_client)

    try:
        api_response = api_instance.list_restriction()
        print("The response of RestrictionApi->list_restriction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestrictionApi->list_restriction: %s\n" % e)
```

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
    api_instance = radarr.RestrictionApi(api_client)

    try:
        api_response = api_instance.list_restriction()
        print("The response of RestrictionApi->list_restriction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestrictionApi->list_restriction: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[RestrictionResource]**](RestrictionResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_restriction**
> RestrictionResource update_restriction(id, restriction_resource=restriction_resource)



### Example

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
    api_instance = radarr.RestrictionApi(api_client)
    id = 'id_example' # str | 
    restriction_resource = radarr.RestrictionResource() # RestrictionResource |  (optional)

    try:
        api_response = api_instance.update_restriction(id, restriction_resource=restriction_resource)
        print("The response of RestrictionApi->update_restriction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestrictionApi->update_restriction: %s\n" % e)
```

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
    api_instance = radarr.RestrictionApi(api_client)
    id = 'id_example' # str | 
    restriction_resource = radarr.RestrictionResource() # RestrictionResource |  (optional)

    try:
        api_response = api_instance.update_restriction(id, restriction_resource=restriction_resource)
        print("The response of RestrictionApi->update_restriction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestrictionApi->update_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **restriction_resource** | [**RestrictionResource**](RestrictionResource.md)|  | [optional] 

### Return type

[**RestrictionResource**](RestrictionResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

