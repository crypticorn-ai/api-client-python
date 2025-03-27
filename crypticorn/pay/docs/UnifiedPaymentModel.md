# UnifiedPaymentModel

Combined payment model across all services

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** | Payment date in seconds | 
**amount** | **float** | Payment amount | 
**currency** | **str** | Payment currency | 
**status** | [**PaymentStatus**](PaymentStatus.md) |  | 
**service** | [**Services**](Services.md) | Payment service | 
**market** | **str** | Payment market | 

## Example

```python
from client.models.unified_payment_model import UnifiedPaymentModel

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedPaymentModel from a JSON string
unified_payment_model_instance = UnifiedPaymentModel.from_json(json)
# print the JSON string representation of the object
print(UnifiedPaymentModel.to_json())

# convert the object into a dict
unified_payment_model_dict = unified_payment_model_instance.to_dict()
# create an instance of UnifiedPaymentModel from a dict
unified_payment_model_from_dict = UnifiedPaymentModel.from_dict(unified_payment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


