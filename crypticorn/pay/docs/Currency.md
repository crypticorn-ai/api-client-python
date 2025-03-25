# Currency

Model representing a single cryptocurrency supported by the API.  This model contains detailed information about each cryptocurrency available for payments, including its identifiers, network details, validation patterns, and configuration settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the currency | 
**code** | **str** | Currency code/ticker symbol | 
**name** | **str** | Full name of the currency | 
**enable** | **bool** | Whether the currency is currently enabled | 
**wallet_regex** | **str** | Regex pattern for valid wallet addresses | 
**priority** | **int** | Priority ranking of the currency | 
**extra_id_exists** | **bool** | Whether the currency requires an extra ID/memo/tag | 
**extra_id_regex** | **str** |  | [optional] 
**logo_url** | **str** | URL path to currency logo image | 
**track** | **bool** | Whether the currency is being tracked | 
**cg_id** | **str** |  | [optional] 
**is_maxlimit** | **bool** | Whether the currency has a maximum limit | 
**network** | **str** |  | [optional] 
**smart_contract** | **str** |  | [optional] 
**network_precision** | **int** |  | [optional] 

## Example

```python
from client.models.currency import Currency

# TODO update the JSON string below
json = "{}"
# create an instance of Currency from a JSON string
currency_instance = Currency.from_json(json)
# print the JSON string representation of the object
print(Currency.to_json())

# convert the object into a dict
currency_dict = currency_instance.to_dict()
# create an instance of Currency from a dict
currency_from_dict = Currency.from_dict(currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


