# AppUserLink

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the channel to link. See [**IntegrationTypeEnum**](Enums.md#IntegrationTypeEnum) for available values. | 
**integration_id** | **str** | The id of the integration to link, it must match the provided type. | [optional] 
**phone_number** | **str** | A String of the appUser’s phone number. It must contain the + prefix and the country code. Required for *messenger*, *twilio*, *messagebird* and *whatsapp* linking.  | [optional] 
**address** | **str** | A String of the appUser’s email address. Required for *mailgun* linking.  | [optional] 
**given_name** | **str** | A String of the appUser’s given name. Used as additional criteria to increase the likelihood of a match. (Optional) Used for *messenger* linking.  | [optional] 
**surname** | **str** | A String of the appUser’s surname. Used as additional criteria to increase the likelihood of a match. (Optional) Used for *messenger* linking.  | [optional] 
**subject** | **str** | Subject for the outgoing email. (Optional) Used for *mailgun* linking.  | [optional] 
**confirmation** | [**Confirmation**](Confirmation.md) | Allows you to specify the strategy used to initiate a link with the target user. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


