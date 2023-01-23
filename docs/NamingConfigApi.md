# radarr.NamingConfigApi

All URIs are relative to *http://localhost:7878*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_naming_config**](NamingConfigApi.md#get_naming_config) | **GET** /api/v3/config/naming | 
[**get_naming_config_by_id**](NamingConfigApi.md#get_naming_config_by_id) | **GET** /api/v3/config/naming/{id} | 
[**get_naming_config_examples**](NamingConfigApi.md#get_naming_config_examples) | **GET** /api/v3/config/naming/examples | 
[**update_naming_config**](NamingConfigApi.md#update_naming_config) | **PUT** /api/v3/config/naming/{id} | 


# **get_naming_config**
> NamingConfigResource get_naming_config()



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
    api_instance = radarr.NamingConfigApi(api_client)

    try:
        api_response = api_instance.get_naming_config()
        print("The response of NamingConfigApi->get_naming_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamingConfigApi->get_naming_config: %s\n" % e)
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
    api_instance = radarr.NamingConfigApi(api_client)

    try:
        api_response = api_instance.get_naming_config()
        print("The response of NamingConfigApi->get_naming_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamingConfigApi->get_naming_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NamingConfigResource**](NamingConfigResource.md)

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

# **get_naming_config_by_id**
> NamingConfigResource get_naming_config_by_id(id)



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
    api_instance = radarr.NamingConfigApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_naming_config_by_id(id)
        print("The response of NamingConfigApi->get_naming_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamingConfigApi->get_naming_config_by_id: %s\n" % e)
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
    api_instance = radarr.NamingConfigApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_naming_config_by_id(id)
        print("The response of NamingConfigApi->get_naming_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamingConfigApi->get_naming_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**NamingConfigResource**](NamingConfigResource.md)

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

# **get_naming_config_examples**
> get_naming_config_examples(rename_movies=rename_movies, replace_illegal_characters=replace_illegal_characters, colon_replacement_format=colon_replacement_format, standard_movie_format=standard_movie_format, movie_folder_format=movie_folder_format, include_quality=include_quality, replace_spaces=replace_spaces, separator=separator, number_style=number_style, id=id, resource_name=resource_name)



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
    api_instance = radarr.NamingConfigApi(api_client)
    rename_movies = True # bool |  (optional)
    replace_illegal_characters = True # bool |  (optional)
    colon_replacement_format = radarr.ColonReplacementFormat() # ColonReplacementFormat |  (optional)
    standard_movie_format = 'standard_movie_format_example' # str |  (optional)
    movie_folder_format = 'movie_folder_format_example' # str |  (optional)
    include_quality = True # bool |  (optional)
    replace_spaces = True # bool |  (optional)
    separator = 'separator_example' # str |  (optional)
    number_style = 'number_style_example' # str |  (optional)
    id = 56 # int |  (optional)
    resource_name = 'resource_name_example' # str |  (optional)

    try:
        api_instance.get_naming_config_examples(rename_movies=rename_movies, replace_illegal_characters=replace_illegal_characters, colon_replacement_format=colon_replacement_format, standard_movie_format=standard_movie_format, movie_folder_format=movie_folder_format, include_quality=include_quality, replace_spaces=replace_spaces, separator=separator, number_style=number_style, id=id, resource_name=resource_name)
    except Exception as e:
        print("Exception when calling NamingConfigApi->get_naming_config_examples: %s\n" % e)
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
    api_instance = radarr.NamingConfigApi(api_client)
    rename_movies = True # bool |  (optional)
    replace_illegal_characters = True # bool |  (optional)
    colon_replacement_format = radarr.ColonReplacementFormat() # ColonReplacementFormat |  (optional)
    standard_movie_format = 'standard_movie_format_example' # str |  (optional)
    movie_folder_format = 'movie_folder_format_example' # str |  (optional)
    include_quality = True # bool |  (optional)
    replace_spaces = True # bool |  (optional)
    separator = 'separator_example' # str |  (optional)
    number_style = 'number_style_example' # str |  (optional)
    id = 56 # int |  (optional)
    resource_name = 'resource_name_example' # str |  (optional)

    try:
        api_instance.get_naming_config_examples(rename_movies=rename_movies, replace_illegal_characters=replace_illegal_characters, colon_replacement_format=colon_replacement_format, standard_movie_format=standard_movie_format, movie_folder_format=movie_folder_format, include_quality=include_quality, replace_spaces=replace_spaces, separator=separator, number_style=number_style, id=id, resource_name=resource_name)
    except Exception as e:
        print("Exception when calling NamingConfigApi->get_naming_config_examples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rename_movies** | **bool**|  | [optional] 
 **replace_illegal_characters** | **bool**|  | [optional] 
 **colon_replacement_format** | [**ColonReplacementFormat**](.md)|  | [optional] 
 **standard_movie_format** | **str**|  | [optional] 
 **movie_folder_format** | **str**|  | [optional] 
 **include_quality** | **bool**|  | [optional] 
 **replace_spaces** | **bool**|  | [optional] 
 **separator** | **str**|  | [optional] 
 **number_style** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **resource_name** | **str**|  | [optional] 

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

# **update_naming_config**
> NamingConfigResource update_naming_config(id, naming_config_resource=naming_config_resource)



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
    api_instance = radarr.NamingConfigApi(api_client)
    id = 'id_example' # str | 
    naming_config_resource = radarr.NamingConfigResource() # NamingConfigResource |  (optional)

    try:
        api_response = api_instance.update_naming_config(id, naming_config_resource=naming_config_resource)
        print("The response of NamingConfigApi->update_naming_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamingConfigApi->update_naming_config: %s\n" % e)
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
    api_instance = radarr.NamingConfigApi(api_client)
    id = 'id_example' # str | 
    naming_config_resource = radarr.NamingConfigResource() # NamingConfigResource |  (optional)

    try:
        api_response = api_instance.update_naming_config(id, naming_config_resource=naming_config_resource)
        print("The response of NamingConfigApi->update_naming_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamingConfigApi->update_naming_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **naming_config_resource** | [**NamingConfigResource**](NamingConfigResource.md)|  | [optional] 

### Return type

[**NamingConfigResource**](NamingConfigResource.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

