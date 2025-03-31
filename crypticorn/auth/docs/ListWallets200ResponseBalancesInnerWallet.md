# ListWallets200ResponseBalancesInnerWallet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**v** | **object** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**value_aic** | **float** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**vesting_wallets** | [**List[ListWallets200ResponseBalancesInnerWalletVestingWalletsInner]**](ListWallets200ResponseBalancesInnerWalletVestingWalletsInner.md) |  | 

## Example

```python
from client.models.list_wallets200_response_balances_inner_wallet import ListWallets200ResponseBalancesInnerWallet

# TODO update the JSON string below
json = "{}"
# create an instance of ListWallets200ResponseBalancesInnerWallet from a JSON string
list_wallets200_response_balances_inner_wallet_instance = ListWallets200ResponseBalancesInnerWallet.from_json(json)
# print the JSON string representation of the object
print(ListWallets200ResponseBalancesInnerWallet.to_json())

# convert the object into a dict
list_wallets200_response_balances_inner_wallet_dict = list_wallets200_response_balances_inner_wallet_instance.to_dict()
# create an instance of ListWallets200ResponseBalancesInnerWallet from a dict
list_wallets200_response_balances_inner_wallet_from_dict = ListWallets200ResponseBalancesInnerWallet.from_dict(list_wallets200_response_balances_inner_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


