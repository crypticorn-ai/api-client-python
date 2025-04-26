# OrderModel

Response model for orders. All optional as the model is built step by step.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**trading_action_id** | **str** |  | [optional] 
**execution_id** | **str** |  | [optional] 
**exchange_order_id** | **str** |  | [optional] 
**position_id** | **str** |  | [optional] 
**api_key_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**bot_id** | **str** |  | [optional] 
**client_order_id** | **str** |  | [optional] 
**exchange** | [**Exchange**](Exchange.md) |  | [optional] 
**symbol** | **str** |  | [optional] 
**common_symbol** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**action_type** | [**TradingActionType**](TradingActionType.md) |  | [optional] 
**market_type** | [**MarketType**](MarketType.md) |  | [optional] 
**margin_mode** | [**MarginMode**](MarginMode.md) |  | [optional] 
**status_code** | **str** | API error identifiers | [optional] 
**status** | [**OrderStatus**](OrderStatus.md) |  | [optional] 
**filled_perc** | **float** |  | [optional] 
**filled_qty** | **float** |  | [optional] 
**fee** | **float** |  | [optional] 
**leverage** | **float** |  | [optional] 
**order_details** | [**AnyOf**](AnyOf.md) | Exchange specific details of the order | [optional] 
**pnl** | **float** |  | [optional] 
**order_time** | **int** |  | [optional] 

## Example

```python
from client.models.order_model import OrderModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModel from a JSON string
order_model_instance = OrderModel.from_json(json)
# print the JSON string representation of the object
print(OrderModel.to_json())

# convert the object into a dict
order_model_dict = order_model_instance.to_dict()
# create an instance of OrderModel from a dict
order_model_from_dict = OrderModel.from_dict(order_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


