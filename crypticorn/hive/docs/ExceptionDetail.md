# ExceptionDetail

This is the detail of the exception. It is used to enrich the exception with additional information by unwrapping the ApiError into its components.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**code** | [**ApiErrorIdentifier**](ApiErrorIdentifier.md) | The unique error code | 
**type** | [**ApiErrorType**](ApiErrorType.md) | The type of error | 
**level** | [**ApiErrorLevel**](ApiErrorLevel.md) | The level of the error | 
**status_code** | **int** | The HTTP status code | 
**details** | **object** |  | [optional] 

## Example

```python
from client.models.exception_detail import ExceptionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ExceptionDetail from a JSON string
exception_detail_instance = ExceptionDetail.from_json(json)
# print the JSON string representation of the object
print(ExceptionDetail.to_json())

# convert the object into a dict
exception_detail_dict = exception_detail_instance.to_dict()
# create an instance of ExceptionDetail from a dict
exception_detail_from_dict = ExceptionDetail.from_dict(exception_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


