# BaseResponseHealthCheckResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**message** | **str** |  | [optional] 
**data** | [**HealthCheckResponse**](HealthCheckResponse.md) |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from client.models.base_response_health_check_response import BaseResponseHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseHealthCheckResponse from a JSON string
base_response_health_check_response_instance = BaseResponseHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponseHealthCheckResponse.to_json())

# convert the object into a dict
base_response_health_check_response_dict = base_response_health_check_response_instance.to_dict()
# create an instance of BaseResponseHealthCheckResponse from a dict
base_response_health_check_response_from_dict = BaseResponseHealthCheckResponse.from_dict(base_response_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


