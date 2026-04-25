# Country


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The 2-letter ISO 3166-1 alpha-2 code of the country. | 
**name** | **str** | The common name of the country. | 
**capital** | **str** | The capital city of the country. | [optional] 
**region** | **str** | The region the country is located in. | [optional] 
**population** | **int** | The population of the country. | [optional] 

## Example

```python
from openapi_client import Country

# TODO update the JSON string below
json = "{}"
# create an instance of Country from a JSON string
country_instance = Country.from_json(json)
# print the JSON string representation of the object
print(Country.to_json())

# convert the object into a dict
country_dict = country_instance.to_dict()
# create an instance of Country from a dict
country_from_dict = Country.from_dict(country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


