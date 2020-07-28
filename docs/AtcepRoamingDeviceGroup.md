# AtcepRoamingDeviceGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **datetime** | The time when this Roaming Device Group object was created. | [optional] 
**description** | **str** | The brief description for the endpoint group. | [optional] 
**id** | **int** | The Roaming Device Group object identifier. | [optional] 
**internal_domain_lists** | **list[int]** | The list of identifiers of internal_domain_lists ids that are associated with this endpoint group | [optional] 
**is_default** | **bool** | Flag that indicates whether this is a default endpoint group. | [optional] 
**is_probe_enabled** | **bool** | Whether probe domain-response is enabled | [optional] 
**name** | **str** | The name of the endpoint group. | [optional] 
**policy_id** | **int** | The identifier of the security policy with which the endpoint group is associated. | [optional] 
**policy_name** | **str** | The name of the security policy with which the endpoint group is associated. Default is \&quot;Default Global Policy\&quot;. | [optional] 
**probe_domain** | **str** | User specified domain for FQDN, excluding this field inherits from default group&#39;s probe domain (when creating) or ignores field (when updating) | [optional] 
**probe_response** | **str** | The probe token for generating custom TXT record, excluding this field inherits from default group&#39;s probe response (when creating) or ignores field (when updating) | [optional] 
**roaming_device_count** | **int** | Count of roaming devices in this group; absence of this field is equivalent to a count of zero. Note: only GET operation on roaming device group collection resource populates this field. | [optional] 
**roaming_devices** | **list[str]** | The list of endpoint devices&#39; client identifiers that are associated to the endpoint group. | [optional] 
**updated_time** | **datetime** | The time when this Roaming Device Group object was last updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


