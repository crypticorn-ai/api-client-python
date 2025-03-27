# NowPaymentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Product ID | 
**payment_id** | **int** | Unique payment identifier | 
**invoice_id** | **int** | Associated invoice ID | 
**product_id** | **str** | Product ID | 
**user_id** | **str** | User ID | 
**order_id** | **str** | Internal order ID | 
**paid_amount** | **float** | Actually paid amount | 
**pay_amount** | **float** | Amount to pay | 
**pay_currency** | **str** | Payment currency | 
**status** | [**NowPaymentStatus**](NowPaymentStatus.md) | Current payment status | 
**updated_at** | **int** | Payment last update timestamp in milliseconds | 

## Example

```python
from client.models.now_payment_model import NowPaymentModel

# TODO update the JSON string below
json = "{}"
# create an instance of NowPaymentModel from a JSON string
now_payment_model_instance = NowPaymentModel.from_json(json)
# print the JSON string representation of the object
print(NowPaymentModel.to_json())

# convert the object into a dict
now_payment_model_dict = now_payment_model_instance.to_dict()
# create an instance of NowPaymentModel from a dict
now_payment_model_from_dict = NowPaymentModel.from_dict(now_payment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


