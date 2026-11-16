# radarr.FileSystemApi

All URIs are relative to *http://localhost:7878*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file_system**](FileSystemApi.md#get_file_system) | **GET** /api/v3/filesystem | 
[**get_file_system_type**](FileSystemApi.md#get_file_system_type) | **GET** /api/v3/filesystem/type | 
[**list_file_system_mediafiles**](FileSystemApi.md#list_file_system_mediafiles) | **GET** /api/v3/filesystem/mediafiles | 


# **get_file_system**
> FileSystemResult get_file_system(path=path, include_files=include_files, allow_folders_without_trailing_slashes=allow_folders_without_trailing_slashes)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.file_system_result import FileSystemResult
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
    api_instance = radarr.FileSystemApi(api_client)
    path = 'path_example' # str |  (optional)
    include_files = False # bool |  (optional) (default to False)
    allow_folders_without_trailing_slashes = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.get_file_system(path=path, include_files=include_files, allow_folders_without_trailing_slashes=allow_folders_without_trailing_slashes)
        print("The response of FileSystemApi->get_file_system:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileSystemApi->get_file_system: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | [optional] 
 **include_files** | **bool**|  | [optional] [default to False]
 **allow_folders_without_trailing_slashes** | **bool**|  | [optional] [default to False]

### Return type

[**FileSystemResult**](FileSystemResult.md)

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

# **get_file_system_type**
> FileSystemTypeResource get_file_system_type(path=path)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.file_system_type_resource import FileSystemTypeResource
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
    api_instance = radarr.FileSystemApi(api_client)
    path = 'path_example' # str |  (optional)

    try:
        api_response = api_instance.get_file_system_type(path=path)
        print("The response of FileSystemApi->get_file_system_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileSystemApi->get_file_system_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | [optional] 

### Return type

[**FileSystemTypeResource**](FileSystemTypeResource.md)

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

# **list_file_system_mediafiles**
> List[FileSystemMediaFileResource] list_file_system_mediafiles(path=path)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.file_system_media_file_resource import FileSystemMediaFileResource
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
    api_instance = radarr.FileSystemApi(api_client)
    path = 'path_example' # str |  (optional)

    try:
        api_response = api_instance.list_file_system_mediafiles(path=path)
        print("The response of FileSystemApi->list_file_system_mediafiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileSystemApi->list_file_system_mediafiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | [optional] 

### Return type

[**List[FileSystemMediaFileResource]**](FileSystemMediaFileResource.md)

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

