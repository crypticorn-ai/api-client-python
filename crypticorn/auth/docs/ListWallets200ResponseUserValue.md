# ListWallets200ResponseUserValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sum** | **float** |  | 
**usd** | **float** |  | 
**balances** | [**List[ListWallets200ResponseBalancesInner]**](ListWallets200ResponseBalancesInner.md) |  | 
**access_minimum_usd** | **float** |  | 
**has_access** | **bool** |  | 

## Example

```python
from client.models.list_wallets200_response_user_value import ListWallets200ResponseUserValue

# TODO update the JSON string below
json = "{}"
# create an instance of ListWallets200ResponseUserValue from a JSON string
list_wallets200_response_user_value_instance = ListWallets200ResponseUserValue.from_json(json)
# print the JSON string representation of the object
print(ListWallets200ResponseUserValue.to_json())

# convert the object into a dict
list_wallets200_response_user_value_dict = list_wallets200_response_user_value_instance.to_dict()
# create an instance of ListWallets200ResponseUserValue from a dict
list_wallets200_response_user_value_from_dict = ListWallets200ResponseUserValue.from_dict(list_wallets200_response_user_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


