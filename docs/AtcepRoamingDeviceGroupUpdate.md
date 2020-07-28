# AtcepRoamingDeviceGroupUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The brief description for the endpoint group. | [optional] 
**id** | **int** | The Roaming Device Group object identifier. | [optional] 
**internal_domain_lists** | **list[int]** | The list of identifiers of internal_domain_lists ids that are supposed to be associated with this endpoint group | [optional] 
**is_probe_enabled** | **bool** | Whether probe domain-response is enabled | [optional] 
**name** | **str** | The name of the endpoint group. | [optional] 
**probe_domain** | **str** | User specified domain for FQDN, excluding this field inherits from default group&#39;s probe domain (when creating) or ignores field (when updating) | [optional] 
**probe_response** | **str** | The probe token for generating custom TXT record, excluding this field inherits from default group&#39;s probe response (when creating) or ignores field (when updating) | [optional] 
**roaming_devices_added** | **list[str]** | The list of endpoint devices&#39; client identifiers that will be disassociated from the group they are currently associated with and associated with this group.. | [optional] 
**roaming_devices_deleted** | **list[str]** | The list of endpoint devices&#39; client identifiers that will be disassociated from this group and associated with the default roaming clients group for the account. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


