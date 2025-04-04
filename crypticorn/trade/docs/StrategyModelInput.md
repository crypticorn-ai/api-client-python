# StrategyModelInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**identifier** | **str** | Unique human readable identifier for the strategy e.g. &#39;daily_trend_momentum&#39; | 
**name** | **str** | Name of the strategy | 
**description** | **str** | Description of the strategy | 
**exchanges** | [**List[StrategyExchangeInfo]**](StrategyExchangeInfo.md) | Exchanges supported by the strategy. | 
**enabled** | **bool** | Whether the strategy is enabled. If false, no bots will be created or updated for this strategy, open trades will be rejected. Existing bots will be marked as stopping. | 
**leverage** | **int** | Leverage for the strategy | 
**performance_fee** | **float** | Performance fee for the strategy | 
**market_type** | [**MarketType**](MarketType.md) | Market of operation of the strategy | 

## Example

```python
from client.models.strategy_model_input import StrategyModelInput

# TODO update the JSON string below
json = "{}"
# create an instance of StrategyModelInput from a JSON string
strategy_model_input_instance = StrategyModelInput.from_json(json)
# print the JSON string representation of the object
print(StrategyModelInput.to_json())

# convert the object into a dict
strategy_model_input_dict = strategy_model_input_instance.to_dict()
# create an instance of StrategyModelInput from a dict
strategy_model_input_from_dict = StrategyModelInput.from_dict(strategy_model_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


