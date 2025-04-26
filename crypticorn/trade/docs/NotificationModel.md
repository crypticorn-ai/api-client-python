# NotificationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**identifier** | **str** | API error identifiers | 
**level** | **str** | API error levels | 
**type** | **str** | Type of API error | 
**user_id** | **str** |  | [optional] 
**viewed** | **bool** | Whether the notification has been marked as seen | [optional] [default to False]
**sent** | **bool** | Whether the notification has been sent as an email | [optional] [default to False]

## Example

```python
from client.models.notification_model import NotificationModel

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationModel from a JSON string
notification_model_instance = NotificationModel.from_json(json)
# print the JSON string representation of the object
print(NotificationModel.to_json())

# convert the object into a dict
notification_model_dict = notification_model_instance.to_dict()
# create an instance of NotificationModel from a dict
notification_model_from_dict = NotificationModel.from_dict(notification_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


