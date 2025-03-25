# FuturesBalance

Model for futures balance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** | API key ID | 
**asset** | **str** | Asset/Currency code | 
**balance** | **float** | Total balance/equity | 
**available** | **float** | Available balance for trading/withdrawal | 
**unrealized_pnl** | **float** | Unrealized profit and loss | 
**used_margin** | **float** |  | [optional] 
**frozen_amount** | **float** |  | [optional] 

## Example

```python
from client.models.futures_balance import FuturesBalance

# TODO update the JSON string below
json = "{}"
# create an instance of FuturesBalance from a JSON string
futures_balance_instance = FuturesBalance.from_json(json)
# print the JSON string representation of the object
print(FuturesBalance.to_json())

# convert the object into a dict
futures_balance_dict = futures_balance_instance.to_dict()
# create an instance of FuturesBalance from a dict
futures_balance_from_dict = FuturesBalance.from_dict(futures_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


