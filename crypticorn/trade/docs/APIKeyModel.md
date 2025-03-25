# APIKeyModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**exchange** | **str** | Exchange name | 
**api_key** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 
**passphrase** | **str** |  | [optional] 
**label** | **str** | Label for the API key | 
**enabled** | **bool** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from client.models.api_key_model import APIKeyModel

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyModel from a JSON string
api_key_model_instance = APIKeyModel.from_json(json)
# print the JSON string representation of the object
print(APIKeyModel.to_json())

# convert the object into a dict
api_key_model_dict = api_key_model_instance.to_dict()
# create an instance of APIKeyModel from a dict
api_key_model_from_dict = APIKeyModel.from_dict(api_key_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


