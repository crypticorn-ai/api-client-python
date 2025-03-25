# BaseResponseOHLCVResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**message** | **str** |  | [optional] 
**data** | [**OHLCVResponse**](OHLCVResponse.md) |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from client.models.base_response_ohlcv_response import BaseResponseOHLCVResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseOHLCVResponse from a JSON string
base_response_ohlcv_response_instance = BaseResponseOHLCVResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponseOHLCVResponse.to_json())

# convert the object into a dict
base_response_ohlcv_response_dict = base_response_ohlcv_response_instance.to_dict()
# create an instance of BaseResponseOHLCVResponse from a dict
base_response_ohlcv_response_from_dict = BaseResponseOHLCVResponse.from_dict(base_response_ohlcv_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


