# radarr.ManualImportApi

All URIs are relative to *http://localhost:7878*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_manual_import**](ManualImportApi.md#create_manual_import) | **POST** /api/v3/manualimport | 
[**list_manual_import**](ManualImportApi.md#list_manual_import) | **GET** /api/v3/manualimport | 


# **create_manual_import**
> create_manual_import(manual_import_reprocess_resource=manual_import_reprocess_resource)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.manual_import_reprocess_resource import ManualImportReprocessResource
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
    api_instance = radarr.ManualImportApi(api_client)
    manual_import_reprocess_resource = [radarr.ManualImportReprocessResource()] # List[ManualImportReprocessResource] |  (optional)

    try:
        api_instance.create_manual_import(manual_import_reprocess_resource=manual_import_reprocess_resource)
    except Exception as e:
        print("Exception when calling ManualImportApi->create_manual_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_import_reprocess_resource** | [**List[ManualImportReprocessResource]**](ManualImportReprocessResource.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_manual_import**
> List[ManualImportResource] list_manual_import(folder=folder, download_id=download_id, movie_id=movie_id, filter_existing_files=filter_existing_files)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.manual_import_resource import ManualImportResource
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
    api_instance = radarr.ManualImportApi(api_client)
    folder = 'folder_example' # str |  (optional)
    download_id = 'download_id_example' # str |  (optional)
    movie_id = 56 # int |  (optional)
    filter_existing_files = True # bool |  (optional) (default to True)

    try:
        api_response = api_instance.list_manual_import(folder=folder, download_id=download_id, movie_id=movie_id, filter_existing_files=filter_existing_files)
        print("The response of ManualImportApi->list_manual_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManualImportApi->list_manual_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**|  | [optional] 
 **download_id** | **str**|  | [optional] 
 **movie_id** | **int**|  | [optional] 
 **filter_existing_files** | **bool**|  | [optional] [default to True]

### Return type

[**List[ManualImportResource]**](ManualImportResource.md)

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

