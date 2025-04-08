# BodyCreateNowInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**NowCreateInvoiceReq**](NowCreateInvoiceReq.md) |  | 
**scopes** | [**List[Scope]**](Scope.md) |  | [optional] [default to []]

## Example

```python
from client.models.body_create_now_invoice import BodyCreateNowInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of BodyCreateNowInvoice from a JSON string
body_create_now_invoice_instance = BodyCreateNowInvoice.from_json(json)
# print the JSON string representation of the object
print(BodyCreateNowInvoice.to_json())

# convert the object into a dict
body_create_now_invoice_dict = body_create_now_invoice_instance.to_dict()
# create an instance of BodyCreateNowInvoice from a dict
body_create_now_invoice_from_dict = BodyCreateNowInvoice.from_dict(body_create_now_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


