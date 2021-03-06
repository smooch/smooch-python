# FieldPost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The field type. See [**FieldTypeEnum**](Enums.md#FieldTypeEnum) for available values. | 
**name** | **str** | The name of the field. Each field name must be unique per form. | 
**label** | **str** | The label to be displayed with the field. | 
**placeholder** | **str** | The placeholder text of the field that will be rendered. Only for form messages  | [optional] 
**min_size** | **int** | The minimum possible length of the response. Defaults to 1 if not specified. Only for text fields in form messages.  | [optional] 
**max_size** | **int** | The maximum possible length of the response. Defaults to 128 if not specified. Only for text fields in form messages.  | [optional] 
**options** | [**list[Option]**](Option.md) | The field options that can be selected. The array is limited to 20 options. Only for select fields in form messages.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


