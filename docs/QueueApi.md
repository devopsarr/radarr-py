# radarr.QueueApi

All URIs are relative to *http://localhost:7878*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_queue**](QueueApi.md#delete_queue) | **DELETE** /api/v3/queue/{id} | 
[**delete_queue_bulk**](QueueApi.md#delete_queue_bulk) | **DELETE** /api/v3/queue/bulk | 
[**get_queue**](QueueApi.md#get_queue) | **GET** /api/v3/queue | 


# **delete_queue**
> delete_queue(id, remove_from_client=remove_from_client, blocklist=blocklist, skip_redownload=skip_redownload, change_category=change_category)

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
    api_instance = radarr.QueueApi(api_client)
    id = 56 # int | 
    remove_from_client = True # bool |  (optional) (default to True)
    blocklist = False # bool |  (optional) (default to False)
    skip_redownload = False # bool |  (optional) (default to False)
    change_category = False # bool |  (optional) (default to False)

    try:
        api_instance.delete_queue(id, remove_from_client=remove_from_client, blocklist=blocklist, skip_redownload=skip_redownload, change_category=change_category)
    except Exception as e:
        print("Exception when calling QueueApi->delete_queue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **remove_from_client** | **bool**|  | [optional] [default to True]
 **blocklist** | **bool**|  | [optional] [default to False]
 **skip_redownload** | **bool**|  | [optional] [default to False]
 **change_category** | **bool**|  | [optional] [default to False]

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

# **delete_queue_bulk**
> delete_queue_bulk(remove_from_client=remove_from_client, blocklist=blocklist, skip_redownload=skip_redownload, change_category=change_category, queue_bulk_resource=queue_bulk_resource)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.queue_bulk_resource import QueueBulkResource
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
    api_instance = radarr.QueueApi(api_client)
    remove_from_client = True # bool |  (optional) (default to True)
    blocklist = False # bool |  (optional) (default to False)
    skip_redownload = False # bool |  (optional) (default to False)
    change_category = False # bool |  (optional) (default to False)
    queue_bulk_resource = radarr.QueueBulkResource() # QueueBulkResource |  (optional)

    try:
        api_instance.delete_queue_bulk(remove_from_client=remove_from_client, blocklist=blocklist, skip_redownload=skip_redownload, change_category=change_category, queue_bulk_resource=queue_bulk_resource)
    except Exception as e:
        print("Exception when calling QueueApi->delete_queue_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_from_client** | **bool**|  | [optional] [default to True]
 **blocklist** | **bool**|  | [optional] [default to False]
 **skip_redownload** | **bool**|  | [optional] [default to False]
 **change_category** | **bool**|  | [optional] [default to False]
 **queue_bulk_resource** | [**QueueBulkResource**](QueueBulkResource.md)|  | [optional] 

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

# **get_queue**
> QueueResourcePagingResource get_queue(page=page, page_size=page_size, sort_key=sort_key, sort_direction=sort_direction, include_unknown_movie_items=include_unknown_movie_items, include_movie=include_movie, movie_ids=movie_ids, protocol=protocol, languages=languages, quality=quality, status=status)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import radarr
from radarr.models.download_protocol import DownloadProtocol
from radarr.models.queue_resource_paging_resource import QueueResourcePagingResource
from radarr.models.queue_status import QueueStatus
from radarr.models.sort_direction import SortDirection
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
    api_instance = radarr.QueueApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)
    sort_key = 'sort_key_example' # str |  (optional)
    sort_direction = radarr.SortDirection() # SortDirection |  (optional)
    include_unknown_movie_items = False # bool |  (optional) (default to False)
    include_movie = False # bool |  (optional) (default to False)
    movie_ids = [56] # List[int] |  (optional)
    protocol = radarr.DownloadProtocol() # DownloadProtocol |  (optional)
    languages = [56] # List[int] |  (optional)
    quality = [56] # List[int] |  (optional)
    status = [radarr.QueueStatus()] # List[QueueStatus] |  (optional)

    try:
        api_response = api_instance.get_queue(page=page, page_size=page_size, sort_key=sort_key, sort_direction=sort_direction, include_unknown_movie_items=include_unknown_movie_items, include_movie=include_movie, movie_ids=movie_ids, protocol=protocol, languages=languages, quality=quality, status=status)
        print("The response of QueueApi->get_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueApi->get_queue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]
 **sort_key** | **str**|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **include_unknown_movie_items** | **bool**|  | [optional] [default to False]
 **include_movie** | **bool**|  | [optional] [default to False]
 **movie_ids** | [**List[int]**](int.md)|  | [optional] 
 **protocol** | [**DownloadProtocol**](.md)|  | [optional] 
 **languages** | [**List[int]**](int.md)|  | [optional] 
 **quality** | [**List[int]**](int.md)|  | [optional] 
 **status** | [**List[QueueStatus]**](QueueStatus.md)|  | [optional] 

### Return type

[**QueueResourcePagingResource**](QueueResourcePagingResource.md)

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

