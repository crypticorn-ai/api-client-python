# ExchangeMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_name** | **str** |  | 
**symbol** | **str** |  | 
**quote_currency** | **str** |  | 
**pair** | **str** |  | 
**first_trade_timestamp** | **datetime** |  | 
**last_trade_timestamp** | **datetime** |  | 
**status** | [**TradingStatus**](TradingStatus.md) |  | 
**market_type** | [**MarketType**](MarketType.md) |  | 

## Example

```python
from client.models.exchange_mapping import ExchangeMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeMapping from a JSON string
exchange_mapping_instance = ExchangeMapping.from_json(json)
# print the JSON string representation of the object
print(ExchangeMapping.to_json())

# convert the object into a dict
exchange_mapping_dict = exchange_mapping_instance.to_dict()
# create an instance of ExchangeMapping from a dict
exchange_mapping_from_dict = ExchangeMapping.from_dict(exchange_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


