# IosAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | To configure an ios integration, call the create integration endpoint with a base64 encoded Apple Push Notification certificate from the [Apple Developer Portal](https://developer.apple.com/).  | [optional] [default to 'ios']
**certificate** | **str** | The binary of your APN certificate base64 encoded. | [optional] 
**password** | **str** | The password for your APN certificate. | [optional] 
**production** | **bool** | The APN environment to connect to (Production, if true, or Sandbox). Defaults to value inferred from certificate if not specified. | [optional] 
**auto_update_badge** | **bool** | Use the unread count of the conversation as the application badge. | [optional] 
**can_user_create_more_conversations** | **bool** | Allows users to create more than one conversation on the iOS integration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


