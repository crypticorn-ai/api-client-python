# ExchangeKeyModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**exchange** | [**Exchange**](Exchange.md) | Exchange name | 
**api_key** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 
**passphrase** | **str** |  | [optional] 
**label** | **str** | Label for the API key | 
**enabled** | **bool** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from client.models.exchange_key_model import ExchangeKeyModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeKeyModel from a JSON string
exchange_key_model_instance = ExchangeKeyModel.from_json(json)
# print the JSON string representation of the object
print(ExchangeKeyModel.to_json())

# convert the object into a dict
exchange_key_model_dict = exchange_key_model_instance.to_dict()
# create an instance of ExchangeKeyModel from a dict
exchange_key_model_from_dict = ExchangeKeyModel.from_dict(exchange_key_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


