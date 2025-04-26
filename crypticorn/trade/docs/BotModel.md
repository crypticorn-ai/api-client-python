# BotModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** | Name of the bot | 
**strategy_id** | **str** | UID for the trading strategy used by the bot | 
**api_key_id** | **str** | UID for the API key | 
**allocation** | **int** | Initial allocation for the bot | 
**status** | [**BotStatus**](BotStatus.md) | Status of the bot | 
**status_code** | **str** | API error identifiers | [optional] 
**user_id** | **str** |  | [optional] 
**current_allocation** | **float** |  | [optional] 
**current_exposure** | **float** |  | [optional] 

## Example

```python
from client.models.bot_model import BotModel

# TODO update the JSON string below
json = "{}"
# create an instance of BotModel from a JSON string
bot_model_instance = BotModel.from_json(json)
# print the JSON string representation of the object
print(BotModel.to_json())

# convert the object into a dict
bot_model_dict = bot_model_instance.to_dict()
# create an instance of BotModel from a dict
bot_model_from_dict = BotModel.from_dict(bot_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


