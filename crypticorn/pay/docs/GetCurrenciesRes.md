# GetCurrenciesRes

Response containing list of available cryptocurrencies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencies** | [**List[Currency]**](Currency.md) | List of supported cryptocurrencies | 

## Example

```python
from client.models.get_currencies_res import GetCurrenciesRes

# TODO update the JSON string below
json = "{}"
# create an instance of GetCurrenciesRes from a JSON string
get_currencies_res_instance = GetCurrenciesRes.from_json(json)
# print the JSON string representation of the object
print(GetCurrenciesRes.to_json())

# convert the object into a dict
get_currencies_res_dict = get_currencies_res_instance.to_dict()
# create an instance of GetCurrenciesRes from a dict
get_currencies_res_from_dict = GetCurrenciesRes.from_dict(get_currencies_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


