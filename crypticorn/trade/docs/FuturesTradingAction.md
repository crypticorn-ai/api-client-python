# FuturesTradingAction

Model for futures trading actions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**execution_id** | **str** |  | [optional] 
**open_order_execution_id** | **str** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**action_type** | [**TradingActionType**](TradingActionType.md) | The type of action. | 
**market_type** | **str** | Market types | 
**strategy_id** | **str** | UID for the strategy. | 
**symbol** | **str** | Trading symbol or asset pair in format: &#39;symbol/quote_currency&#39; (see market service for valid symbols) | 
**is_limit** | **bool** |  | [optional] 
**limit_price** | **float** |  | [optional] 
**allocation** | **float** | How much of bot&#39;s balance to use for the order (for open actions). How much of the reference open order (open_order_execution_id) to close (for close actions). 0&#x3D;0%, 1&#x3D;100%. | [optional] 
**take_profit** | [**List[TPSL]**](TPSL.md) |  | [optional] 
**stop_loss** | [**List[TPSL]**](TPSL.md) |  | [optional] 
**expiry_timestamp** | **int** |  | [optional] 
**position_id** | **str** |  | [optional] 
**leverage** | **int** |  | [default to 1]
**margin_mode** | [**MarginMode**](MarginMode.md) |  | [optional] 

## Example

```python
from client.models.futures_trading_action import FuturesTradingAction

# TODO update the JSON string below
json = "{}"
# create an instance of FuturesTradingAction from a JSON string
futures_trading_action_instance = FuturesTradingAction.from_json(json)
# print the JSON string representation of the object
print(FuturesTradingAction.to_json())

# convert the object into a dict
futures_trading_action_dict = futures_trading_action_instance.to_dict()
# create an instance of FuturesTradingAction from a dict
futures_trading_action_from_dict = FuturesTradingAction.from_dict(futures_trading_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


