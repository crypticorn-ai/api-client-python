# ListWallets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ListWallets200ResponseDataInner]**](ListWallets200ResponseDataInner.md) |  | 
**count** | **float** |  | 
**balances** | [**List[ListWallets200ResponseBalancesInner]**](ListWallets200ResponseBalancesInner.md) |  | 
**user_value** | [**ListWallets200ResponseUserValue**](ListWallets200ResponseUserValue.md) |  | 

## Example

```python
from client.models.list_wallets200_response import ListWallets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListWallets200Response from a JSON string
list_wallets200_response_instance = ListWallets200Response.from_json(json)
# print the JSON string representation of the object
print(ListWallets200Response.to_json())

# convert the object into a dict
list_wallets200_response_dict = list_wallets200_response_instance.to_dict()
# create an instance of ListWallets200Response from a dict
list_wallets200_response_from_dict = ListWallets200Response.from_dict(list_wallets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


