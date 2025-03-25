# BaseResponseListFundingRateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**message** | **str** |  | [optional] 
**data** | [**List[FundingRateResponse]**](FundingRateResponse.md) |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from client.models.base_response_list_funding_rate_response import BaseResponseListFundingRateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseListFundingRateResponse from a JSON string
base_response_list_funding_rate_response_instance = BaseResponseListFundingRateResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponseListFundingRateResponse.to_json())

# convert the object into a dict
base_response_list_funding_rate_response_dict = base_response_list_funding_rate_response_instance.to_dict()
# create an instance of BaseResponseListFundingRateResponse from a dict
base_response_list_funding_rate_response_from_dict = BaseResponseListFundingRateResponse.from_dict(base_response_list_funding_rate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


