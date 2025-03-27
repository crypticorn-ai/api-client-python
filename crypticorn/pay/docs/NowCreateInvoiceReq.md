# NowCreateInvoiceReq

Request model for creating a payment invoice.  Creates a payment link where the customer can complete the payment. With this method, the customer is required to follow the generated url to complete the payment.  https://documenter.getpostman.com/view/7907941/2s93JusNJt#f5e4e645-dce2-4b06-b2ca-2a29aaa5e845

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_amount** | **float** | Amount to pay in fiat currency | 
**price_currency** | **str** | Fiat currency for the price (usd, eur, etc) | 
**pay_currency** | **str** |  | [optional] 
**ipn_callback_url** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**order_description** | **str** |  | [optional] 
**success_url** | **str** |  | [optional] 
**cancel_url** | **str** |  | [optional] 
**partially_paid_url** | **str** |  | [optional] 
**is_fixed_rate** | **bool** |  | [optional] 
**is_fee_paid_by_user** | **bool** |  | [optional] 

## Example

```python
from client.models.now_create_invoice_req import NowCreateInvoiceReq

# TODO update the JSON string below
json = "{}"
# create an instance of NowCreateInvoiceReq from a JSON string
now_create_invoice_req_instance = NowCreateInvoiceReq.from_json(json)
# print the JSON string representation of the object
print(NowCreateInvoiceReq.to_json())

# convert the object into a dict
now_create_invoice_req_dict = now_create_invoice_req_instance.to_dict()
# create an instance of NowCreateInvoiceReq from a dict
now_create_invoice_req_from_dict = NowCreateInvoiceReq.from_dict(now_create_invoice_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


