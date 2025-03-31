# ListWallets200ResponseBalancesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet** | [**ListWallets200ResponseBalancesInnerWallet**](ListWallets200ResponseBalancesInnerWallet.md) |  | 
**sale_round** | [**ListWallets200ResponseBalancesInnerSaleRound**](ListWallets200ResponseBalancesInnerSaleRound.md) |  | 
**value_usd** | **float** |  | 
**value_aic** | **float** |  | 

## Example

```python
from client.models.list_wallets200_response_balances_inner import ListWallets200ResponseBalancesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWallets200ResponseBalancesInner from a JSON string
list_wallets200_response_balances_inner_instance = ListWallets200ResponseBalancesInner.from_json(json)
# print the JSON string representation of the object
print(ListWallets200ResponseBalancesInner.to_json())

# convert the object into a dict
list_wallets200_response_balances_inner_dict = list_wallets200_response_balances_inner_instance.to_dict()
# create an instance of ListWallets200ResponseBalancesInner from a dict
list_wallets200_response_balances_inner_from_dict = ListWallets200ResponseBalancesInner.from_dict(list_wallets200_response_balances_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


