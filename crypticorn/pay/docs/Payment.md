# Payment

Combined payment model across all services

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Payment ID | 
**product_id** | **str** | Product ID | 
**timestamp** | **int** | Payment timestamp in seconds | 
**amount** | **float** | Payment amount | 
**currency** | **str** | Payment currency | 
**status** | [**PaymentStatus**](PaymentStatus.md) |  | 
**provider** | [**Provider**](Provider.md) | Payment provider | 
**market** | **str** | Payment market | 

## Example

```python
from client.models.payment import Payment

# TODO update the JSON string below
json = "{}"
# create an instance of Payment from a JSON string
payment_instance = Payment.from_json(json)
# print the JSON string representation of the object
print(Payment.to_json())

# convert the object into a dict
payment_dict = payment_instance.to_dict()
# create an instance of Payment from a dict
payment_from_dict = Payment.from_dict(payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


