# openapi_client.DefaultApi

All URIs are relative to *https://api.example.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_country**](DefaultApi.md#add_country) | **POST** /countries | Add a new country
[**delete_country**](DefaultApi.md#delete_country) | **DELETE** /countries/{code} | Delete a country
[**get_country_by_code**](DefaultApi.md#get_country_by_code) | **GET** /countries/{code} | Get a country by code
[**list_countries**](DefaultApi.md#list_countries) | **GET** /countries | List all countries
[**update_country**](DefaultApi.md#update_country) | **PUT** /countries/{code} | Update a country


# **add_country**
> Country add_country(country)

Add a new country

Adds a new country to the database.

### Example

```python
import openapi_client
from openapi_client import Country
from openapi_client import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="https://api.example.com/v1"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    country = openapi_client.Country()  # Country | 

    try:
        # Add a new country
        api_response = api_instance.add_country(country)
        print("The response of DefaultApi->add_country:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_country: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | [**Country**](Country.md)|  | 

### Return type

[**Country**](Country.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Country created successfully |  -  |
**400** | Invalid input |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_country**
> delete_country(code)

Delete a country

Deletes a country from the database.

### Example

```python
import openapi_client
from openapi_client import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="https://api.example.com/v1"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    code = 'code_example'  # str | The 2-letter ISO 3166-1 alpha-2 code of the country

    try:
        # Delete a country
        api_instance.delete_country(code)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_country: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The 2-letter ISO 3166-1 alpha-2 code of the country | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Country deleted successfully |  -  |
**404** | Country not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country_by_code**
> Country get_country_by_code(code)

Get a country by code

Returns details of a specific country by its ISO code.

### Example

```python
import openapi_client
from openapi_client import Country
from openapi_client import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="https://api.example.com/v1"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    code = 'code_example'  # str | The 2-letter ISO 3166-1 alpha-2 code of the country

    try:
        # Get a country by code
        api_response = api_instance.get_country_by_code(code)
        print("The response of DefaultApi->get_country_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_country_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The 2-letter ISO 3166-1 alpha-2 code of the country | 

### Return type

[**Country**](Country.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A country object |  -  |
**404** | Country not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_countries**
> List[Country] list_countries(region=region, limit=limit, offset=offset)

List all countries

Returns a list of all countries, optionally filtered by region.

### Example

```python
import openapi_client
from openapi_client import Country
from openapi_client import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="https://api.example.com/v1"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    region = 'region_example'  # str | Filter countries by region (optional)
    limit = 10  # int | Maximum number of countries to return (optional) (default to 10)
    offset = 0  # int | Number of countries to skip (optional) (default to 0)

    try:
        # List all countries
        api_response = api_instance.list_countries(region=region, limit=limit, offset=offset)
        print("The response of DefaultApi->list_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_countries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| Filter countries by region | [optional] 
 **limit** | **int**| Maximum number of countries to return | [optional] [default to 10]
 **offset** | **int**| Number of countries to skip | [optional] [default to 0]

### Return type

[**List[Country]**](Country.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of countries |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_country**
> Country update_country(code, country)

Update a country

Updates an existing country's information.

### Example

```python
import openapi_client
from openapi_client import Country
from openapi_client import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="https://api.example.com/v1"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    code = 'code_example'  # str | The 2-letter ISO 3166-1 alpha-2 code of the country
    country = openapi_client.Country()  # Country | 

    try:
        # Update a country
        api_response = api_instance.update_country(code, country)
        print("The response of DefaultApi->update_country:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_country: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The 2-letter ISO 3166-1 alpha-2 code of the country | 
 **country** | [**Country**](Country.md)|  | 

### Return type

[**Country**](Country.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Country updated successfully |  -  |
**400** | Invalid input |  -  |
**404** | Country not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

