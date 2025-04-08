# BodyHandleNowWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**NowWebhookPayload**](NowWebhookPayload.md) |  | 
**scopes** | [**List[Scope]**](Scope.md) |  | [optional] [default to []]

## Example

```python
from client.models.body_handle_now_webhook import BodyHandleNowWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of BodyHandleNowWebhook from a JSON string
body_handle_now_webhook_instance = BodyHandleNowWebhook.from_json(json)
# print the JSON string representation of the object
print(BodyHandleNowWebhook.to_json())

# convert the object into a dict
body_handle_now_webhook_dict = body_handle_now_webhook_instance.to_dict()
# create an instance of BodyHandleNowWebhook from a dict
body_handle_now_webhook_from_dict = BodyHandleNowWebhook.from_dict(body_handle_now_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


