# ResendVerificationEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from client.models.resend_verification_email_request import ResendVerificationEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResendVerificationEmailRequest from a JSON string
resend_verification_email_request_instance = ResendVerificationEmailRequest.from_json(json)
# print the JSON string representation of the object
print(ResendVerificationEmailRequest.to_json())

# convert the object into a dict
resend_verification_email_request_dict = resend_verification_email_request_instance.to_dict()
# create an instance of ResendVerificationEmailRequest from a dict
resend_verification_email_request_from_dict = ResendVerificationEmailRequest.from_dict(resend_verification_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


