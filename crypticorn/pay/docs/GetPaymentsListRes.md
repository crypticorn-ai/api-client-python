# GetPaymentsListRes

Response model for the list of payments. https://documenter.getpostman.com/view/7907941/2s93JusNJt#c38d2410-1523-4313-8764-0043ba1cb24f

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Payment]**](Payment.md) | List of payments | 
**limit** | **int** | Number of records per page | 
**page** | **int** | Current page number | 
**pages_count** | **int** | Total number of pages | 
**total** | **int** | Total number of records | 

## Example

```python
from client.models.get_payments_list_res import GetPaymentsListRes

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentsListRes from a JSON string
get_payments_list_res_instance = GetPaymentsListRes.from_json(json)
# print the JSON string representation of the object
print(GetPaymentsListRes.to_json())

# convert the object into a dict
get_payments_list_res_dict = get_payments_list_res_instance.to_dict()
# create an instance of GetPaymentsListRes from a dict
get_payments_list_res_from_dict = GetPaymentsListRes.from_dict(get_payments_list_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


