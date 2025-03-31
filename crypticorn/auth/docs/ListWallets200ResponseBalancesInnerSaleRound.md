# ListWallets200ResponseBalancesInnerSaleRound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**name** | **str** |  | 
**price_usd** | **float** |  | 
**recommended_usd** | **float** |  | [optional] 
**contract_sales_to_date** | **float** |  | [optional] 
**allocation** | **float** |  | 
**start** | **datetime** |  | 
**state** | **str** |  | 

## Example

```python
from client.models.list_wallets200_response_balances_inner_sale_round import ListWallets200ResponseBalancesInnerSaleRound

# TODO update the JSON string below
json = "{}"
# create an instance of ListWallets200ResponseBalancesInnerSaleRound from a JSON string
list_wallets200_response_balances_inner_sale_round_instance = ListWallets200ResponseBalancesInnerSaleRound.from_json(json)
# print the JSON string representation of the object
print(ListWallets200ResponseBalancesInnerSaleRound.to_json())

# convert the object into a dict
list_wallets200_response_balances_inner_sale_round_dict = list_wallets200_response_balances_inner_sale_round_instance.to_dict()
# create an instance of ListWallets200ResponseBalancesInnerSaleRound from a dict
list_wallets200_response_balances_inner_sale_round_from_dict = ListWallets200ResponseBalancesInnerSaleRound.from_dict(list_wallets200_response_balances_inner_sale_round_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


