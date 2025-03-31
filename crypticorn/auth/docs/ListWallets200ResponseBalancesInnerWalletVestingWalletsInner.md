# ListWallets200ResponseBalancesInnerWalletVestingWalletsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**address** | **str** |  | [optional] 
**value_aic** | **float** |  | [optional] 
**round** | **float** |  | [optional] 
**released** | **float** |  | [optional] 
**vested_amount** | **float** |  | [optional] 
**start_at** | **str** |  | [optional] 
**end_at** | **str** |  | [optional] 
**cliff_at** | **str** |  | [optional] 
**started** | **bool** |  | [optional] 
**claimable_amount** | **float** |  | [optional] 

## Example

```python
from client.models.list_wallets200_response_balances_inner_wallet_vesting_wallets_inner import ListWallets200ResponseBalancesInnerWalletVestingWalletsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWallets200ResponseBalancesInnerWalletVestingWalletsInner from a JSON string
list_wallets200_response_balances_inner_wallet_vesting_wallets_inner_instance = ListWallets200ResponseBalancesInnerWalletVestingWalletsInner.from_json(json)
# print the JSON string representation of the object
print(ListWallets200ResponseBalancesInnerWalletVestingWalletsInner.to_json())

# convert the object into a dict
list_wallets200_response_balances_inner_wallet_vesting_wallets_inner_dict = list_wallets200_response_balances_inner_wallet_vesting_wallets_inner_instance.to_dict()
# create an instance of ListWallets200ResponseBalancesInnerWalletVestingWalletsInner from a dict
list_wallets200_response_balances_inner_wallet_vesting_wallets_inner_from_dict = ListWallets200ResponseBalancesInnerWalletVestingWalletsInner.from_dict(list_wallets200_response_balances_inner_wallet_vesting_wallets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


