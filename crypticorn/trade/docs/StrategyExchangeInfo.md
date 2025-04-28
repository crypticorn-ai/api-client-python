# StrategyExchangeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange** | **str** | Supported exchanges for trading | 
**min_amount** | **float** | Minimum amount for the strategy on the exchange | 

## Example

```python
from client.models.strategy_exchange_info import StrategyExchangeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StrategyExchangeInfo from a JSON string
strategy_exchange_info_instance = StrategyExchangeInfo.from_json(json)
# print the JSON string representation of the object
print(StrategyExchangeInfo.to_json())

# convert the object into a dict
strategy_exchange_info_dict = strategy_exchange_info_instance.to_dict()
# create an instance of StrategyExchangeInfo from a dict
strategy_exchange_info_from_dict = StrategyExchangeInfo.from_dict(strategy_exchange_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


