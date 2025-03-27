# NowCreateInvoiceRes

Response model for created invoice. https://documenter.getpostman.com/view/7907941/2s93JusNJt#f5e4e645-dce2-4b06-b2ca-2a29aaa5e845

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Invoice ID | 
**token_id** | **str** | Internal identifier | 
**order_id** | **str** |  | [optional] 
**order_description** | **str** |  | [optional] 
**price_amount** | **str** | Base price in fiat | 
**price_currency** | **str** | Ticker of base fiat currency | 
**pay_currency** | **str** |  | [optional] 
**ipn_callback_url** | **str** |  | [optional] 
**invoice_url** | **str** | Link to the payment page | 
**success_url** | **str** |  | [optional] 
**cancel_url** | **str** |  | [optional] 
**partially_paid_url** | **str** |  | [optional] 
**payout_currency** | **str** |  | [optional] 
**created_at** | **str** | Time of invoice creation | 
**updated_at** | **str** | Time of latest invoice update | 
**is_fixed_rate** | **bool** | Fixed Rate option status | 
**is_fee_paid_by_user** | **bool** | Fee Paid By User option status | 

## Example

```python
from client.models.now_create_invoice_res import NowCreateInvoiceRes

# TODO update the JSON string below
json = "{}"
# create an instance of NowCreateInvoiceRes from a JSON string
now_create_invoice_res_instance = NowCreateInvoiceRes.from_json(json)
# print the JSON string representation of the object
print(NowCreateInvoiceRes.to_json())

# convert the object into a dict
now_create_invoice_res_dict = now_create_invoice_res_instance.to_dict()
# create an instance of NowCreateInvoiceRes from a dict
now_create_invoice_res_from_dict = NowCreateInvoiceRes.from_dict(now_create_invoice_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


