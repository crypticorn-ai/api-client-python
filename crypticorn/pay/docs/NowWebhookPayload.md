# NowWebhookPayload

Model for NOWPayments webhook (IPN) payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actually_paid** | **float** | Actually paid amount | 
**actually_paid_at_fiat** | **float** | Actually paid amount in fiat currency | 
**fee** | [**NowFeeStructure**](NowFeeStructure.md) | Fee structure for the payment | 
**invoice_id** | **int** | Associated invoice ID | 
**order_description** | **str** | Order description | 
**order_id** | **str** | Internal order ID | 
**outcome_amount** | **float** | Outcome amount | 
**outcome_currency** | **str** | Outcome currency | 
**parent_payment_id** | **int** |  | [optional] 
**pay_address** | **str** | Payment destination address | 
**pay_amount** | **float** | Amount to pay | 
**pay_currency** | **str** | Payment currency | 
**payment_id** | **int** | Unique payment identifier | 
**payment_status** | [**NowPaymentStatus**](NowPaymentStatus.md) | Current payment status | 
**price_amount** | **float** | Original price amount | 
**price_currency** | **str** | Original price currency | 
**purchase_id** | **str** | Purchase ID | 
**updated_at** | **int** | Payment last update timestamp in milliseconds | 

## Example

```python
from client.models.now_webhook_payload import NowWebhookPayload

# TODO update the JSON string below
json = "{}"
# create an instance of NowWebhookPayload from a JSON string
now_webhook_payload_instance = NowWebhookPayload.from_json(json)
# print the JSON string representation of the object
print(NowWebhookPayload.to_json())

# convert the object into a dict
now_webhook_payload_dict = now_webhook_payload_instance.to_dict()
# create an instance of NowWebhookPayload from a dict
now_webhook_payload_from_dict = NowWebhookPayload.from_dict(now_webhook_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


