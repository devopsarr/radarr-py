# radarr.AutoTaggingApi

All URIs are relative to *http://localhost:7878*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auto_tagging**](AutoTaggingApi.md#create_auto_tagging) | **POST** /api/v3/autotagging | 
[**delete_auto_tagging**](AutoTaggingApi.md#delete_auto_tagging) | **DELETE** /api/v3/autotagging/{id} | 
[**get_auto_tagging_by_id**](AutoTaggingApi.md#get_auto_tagging_by_id) | **GET** /api/v3/autotagging/{id} | 
[**list_auto_tagging**](AutoTaggingApi.md#list_auto_tagging) | **GET** /api/v3/autotagging | 
[**list_auto_tagging_schema**](AutoTaggingApi.md#list_auto_tagging_schema) | **GET** /api/v3/autotagging/schema | 
[**update_auto_tagging**](AutoTaggingApi.md#update_auto_tagging) | **PUT** /api/v3/autotagging/{id} | 


# **create_auto_tagging**
> AutoTaggingResource create_auto_tagging(auto_tagging_resource=auto_tagging_resource)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.auto_tagging_resource import AutoTaggingResource
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
    api_instance = radarr.AutoTaggingApi(api_client)
    auto_tagging_resource = radarr.AutoTaggingResource() # AutoTaggingResource |  (optional)

    try:
        api_response = api_instance.create_auto_tagging(auto_tagging_resource=auto_tagging_resource)
        print("The response of AutoTaggingApi->create_auto_tagging:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTaggingApi->create_auto_tagging: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_tagging_resource** | [**AutoTaggingResource**](AutoTaggingResource.md)|  | [optional] 

### Return type

[**AutoTaggingResource**](AutoTaggingResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auto_tagging**
> delete_auto_tagging(id)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
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
    api_instance = radarr.AutoTaggingApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_auto_tagging(id)
    except Exception as e:
        print("Exception when calling AutoTaggingApi->delete_auto_tagging: %s\n" % e)
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
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_tagging_by_id**
> AutoTaggingResource get_auto_tagging_by_id(id)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.auto_tagging_resource import AutoTaggingResource
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
    api_instance = radarr.AutoTaggingApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_auto_tagging_by_id(id)
        print("The response of AutoTaggingApi->get_auto_tagging_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTaggingApi->get_auto_tagging_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AutoTaggingResource**](AutoTaggingResource.md)

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

# **list_auto_tagging**
> List[AutoTaggingResource] list_auto_tagging()



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.auto_tagging_resource import AutoTaggingResource
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
    api_instance = radarr.AutoTaggingApi(api_client)

    try:
        api_response = api_instance.list_auto_tagging()
        print("The response of AutoTaggingApi->list_auto_tagging:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTaggingApi->list_auto_tagging: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AutoTaggingResource]**](AutoTaggingResource.md)

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

# **list_auto_tagging_schema**
> List[AutoTaggingSpecificationSchema] list_auto_tagging_schema()



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.auto_tagging_specification_schema import AutoTaggingSpecificationSchema
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
    api_instance = radarr.AutoTaggingApi(api_client)

    try:
        api_response = api_instance.list_auto_tagging_schema()
        print("The response of AutoTaggingApi->list_auto_tagging_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTaggingApi->list_auto_tagging_schema: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AutoTaggingSpecificationSchema]**](AutoTaggingSpecificationSchema.md)

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

# **update_auto_tagging**
> AutoTaggingResource update_auto_tagging(id, auto_tagging_resource=auto_tagging_resource)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.auto_tagging_resource import AutoTaggingResource
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
    api_instance = radarr.AutoTaggingApi(api_client)
    id = 'id_example' # str | 
    auto_tagging_resource = radarr.AutoTaggingResource() # AutoTaggingResource |  (optional)

    try:
        api_response = api_instance.update_auto_tagging(id, auto_tagging_resource=auto_tagging_resource)
        print("The response of AutoTaggingApi->update_auto_tagging:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTaggingApi->update_auto_tagging: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **auto_tagging_resource** | [**AutoTaggingResource**](AutoTaggingResource.md)|  | [optional] 

### Return type

[**AutoTaggingResource**](AutoTaggingResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

