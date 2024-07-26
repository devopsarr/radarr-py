# radarr.QualityDefinitionApi

All URIs are relative to *http://localhost:7878*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_quality_definition_by_id**](QualityDefinitionApi.md#get_quality_definition_by_id) | **GET** /api/v3/qualitydefinition/{id} | 
[**list_quality_definition**](QualityDefinitionApi.md#list_quality_definition) | **GET** /api/v3/qualitydefinition | 
[**put_quality_definition_update**](QualityDefinitionApi.md#put_quality_definition_update) | **PUT** /api/v3/qualitydefinition/update | 
[**update_quality_definition**](QualityDefinitionApi.md#update_quality_definition) | **PUT** /api/v3/qualitydefinition/{id} | 


# **get_quality_definition_by_id**
> QualityDefinitionResource get_quality_definition_by_id(id)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.quality_definition_resource import QualityDefinitionResource
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
    api_instance = radarr.QualityDefinitionApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_quality_definition_by_id(id)
        print("The response of QualityDefinitionApi->get_quality_definition_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityDefinitionApi->get_quality_definition_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**QualityDefinitionResource**](QualityDefinitionResource.md)

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

# **list_quality_definition**
> List[QualityDefinitionResource] list_quality_definition()



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.quality_definition_resource import QualityDefinitionResource
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
    api_instance = radarr.QualityDefinitionApi(api_client)

    try:
        api_response = api_instance.list_quality_definition()
        print("The response of QualityDefinitionApi->list_quality_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityDefinitionApi->list_quality_definition: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[QualityDefinitionResource]**](QualityDefinitionResource.md)

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

# **put_quality_definition_update**
> put_quality_definition_update(quality_definition_resource=quality_definition_resource)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.quality_definition_resource import QualityDefinitionResource
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
    api_instance = radarr.QualityDefinitionApi(api_client)
    quality_definition_resource = [radarr.QualityDefinitionResource()] # List[QualityDefinitionResource] |  (optional)

    try:
        api_instance.put_quality_definition_update(quality_definition_resource=quality_definition_resource)
    except Exception as e:
        print("Exception when calling QualityDefinitionApi->put_quality_definition_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quality_definition_resource** | [**List[QualityDefinitionResource]**](QualityDefinitionResource.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quality_definition**
> QualityDefinitionResource update_quality_definition(id, quality_definition_resource=quality_definition_resource)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.quality_definition_resource import QualityDefinitionResource
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
    api_instance = radarr.QualityDefinitionApi(api_client)
    id = 'id_example' # str | 
    quality_definition_resource = radarr.QualityDefinitionResource() # QualityDefinitionResource |  (optional)

    try:
        api_response = api_instance.update_quality_definition(id, quality_definition_resource=quality_definition_resource)
        print("The response of QualityDefinitionApi->update_quality_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityDefinitionApi->update_quality_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **quality_definition_resource** | [**QualityDefinitionResource**](QualityDefinitionResource.md)|  | [optional] 

### Return type

[**QualityDefinitionResource**](QualityDefinitionResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

