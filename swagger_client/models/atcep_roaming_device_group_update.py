# coding: utf-8

"""
    BloxOne Cloud EP API

    BloxOne Endpoint is a lightweight mobile agent that redirects DNS traffic from your remote devices to the BloxOne Cloud. It allows you to apply applicable security policies to your roaming end users in remote sites and branch offices.  In order for end users to connect to Infoblox cloud services, you must download and install BloxOne Endpoint on their devices. The client enforces security policies that you apply to the remote networks, regardless of where your end users are and which networks they are connected to. BloxOne Endpoint listens on port 53 of the device. If other software listens on the same port, DNS traffic cannot be redirected to BloxOne Cloud, and your device will not be protected by BloxOne Endpoint.  When you use the BloxOne Endpoint, DNS queries are sent to BloxOne Cloud directly except for (1) queries that target the bypassed domains and (2) internal domains collected through the DHCP server. If you have internal domains that are served by your local DNS servers and you want to reach them without interruptions, you should consider adding them to the bypassed internal domains list so that DNS queries for these internal domains are sent to the local DNS servers instead of BloxOne Cloud.  BloxOne Endpoint supports dual-stack IPv4 and IPv6 DNS configurations, thereby protecting all devices regardless of their network environments. BloxOne Endpoint in a dual-stack environment is able to proxy IPv6 DNS queries and forward them to BloxOne Cloud over IPv4.   # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AtcepRoamingDeviceGroupUpdate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'description': 'str',
        'id': 'int',
        'internal_domain_lists': 'list[int]',
        'is_probe_enabled': 'bool',
        'name': 'str',
        'probe_domain': 'str',
        'probe_response': 'str',
        'roaming_devices_added': 'list[str]',
        'roaming_devices_deleted': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'internal_domain_lists': 'internal_domain_lists',
        'is_probe_enabled': 'is_probe_enabled',
        'name': 'name',
        'probe_domain': 'probe_domain',
        'probe_response': 'probe_response',
        'roaming_devices_added': 'roaming_devices_added',
        'roaming_devices_deleted': 'roaming_devices_deleted'
    }

    def __init__(self, description=None, id=None, internal_domain_lists=None, is_probe_enabled=None, name=None, probe_domain=None, probe_response=None, roaming_devices_added=None, roaming_devices_deleted=None):  # noqa: E501
        """AtcepRoamingDeviceGroupUpdate - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._id = None
        self._internal_domain_lists = None
        self._is_probe_enabled = None
        self._name = None
        self._probe_domain = None
        self._probe_response = None
        self._roaming_devices_added = None
        self._roaming_devices_deleted = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if internal_domain_lists is not None:
            self.internal_domain_lists = internal_domain_lists
        if is_probe_enabled is not None:
            self.is_probe_enabled = is_probe_enabled
        if name is not None:
            self.name = name
        if probe_domain is not None:
            self.probe_domain = probe_domain
        if probe_response is not None:
            self.probe_response = probe_response
        if roaming_devices_added is not None:
            self.roaming_devices_added = roaming_devices_added
        if roaming_devices_deleted is not None:
            self.roaming_devices_deleted = roaming_devices_deleted

    @property
    def description(self):
        """Gets the description of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501

        The brief description for the endpoint group.  # noqa: E501

        :return: The description of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AtcepRoamingDeviceGroupUpdate.

        The brief description for the endpoint group.  # noqa: E501

        :param description: The description of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501

        The Roaming Device Group object identifier.  # noqa: E501

        :return: The id of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AtcepRoamingDeviceGroupUpdate.

        The Roaming Device Group object identifier.  # noqa: E501

        :param id: The id of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def internal_domain_lists(self):
        """Gets the internal_domain_lists of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501

        The list of identifiers of internal_domain_lists ids that are supposed to be associated with this endpoint group  # noqa: E501

        :return: The internal_domain_lists of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :rtype: list[int]
        """
        return self._internal_domain_lists

    @internal_domain_lists.setter
    def internal_domain_lists(self, internal_domain_lists):
        """Sets the internal_domain_lists of this AtcepRoamingDeviceGroupUpdate.

        The list of identifiers of internal_domain_lists ids that are supposed to be associated with this endpoint group  # noqa: E501

        :param internal_domain_lists: The internal_domain_lists of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :type: list[int]
        """

        self._internal_domain_lists = internal_domain_lists

    @property
    def is_probe_enabled(self):
        """Gets the is_probe_enabled of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501

        Whether probe domain-response is enabled  # noqa: E501

        :return: The is_probe_enabled of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._is_probe_enabled

    @is_probe_enabled.setter
    def is_probe_enabled(self, is_probe_enabled):
        """Sets the is_probe_enabled of this AtcepRoamingDeviceGroupUpdate.

        Whether probe domain-response is enabled  # noqa: E501

        :param is_probe_enabled: The is_probe_enabled of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :type: bool
        """

        self._is_probe_enabled = is_probe_enabled

    @property
    def name(self):
        """Gets the name of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501

        The name of the endpoint group.  # noqa: E501

        :return: The name of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AtcepRoamingDeviceGroupUpdate.

        The name of the endpoint group.  # noqa: E501

        :param name: The name of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def probe_domain(self):
        """Gets the probe_domain of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501

        User specified domain for FQDN, excluding this field inherits from default group's probe domain (when creating) or ignores field (when updating)  # noqa: E501

        :return: The probe_domain of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :rtype: str
        """
        return self._probe_domain

    @probe_domain.setter
    def probe_domain(self, probe_domain):
        """Sets the probe_domain of this AtcepRoamingDeviceGroupUpdate.

        User specified domain for FQDN, excluding this field inherits from default group's probe domain (when creating) or ignores field (when updating)  # noqa: E501

        :param probe_domain: The probe_domain of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :type: str
        """

        self._probe_domain = probe_domain

    @property
    def probe_response(self):
        """Gets the probe_response of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501

        The probe token for generating custom TXT record, excluding this field inherits from default group's probe response (when creating) or ignores field (when updating)  # noqa: E501

        :return: The probe_response of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :rtype: str
        """
        return self._probe_response

    @probe_response.setter
    def probe_response(self, probe_response):
        """Sets the probe_response of this AtcepRoamingDeviceGroupUpdate.

        The probe token for generating custom TXT record, excluding this field inherits from default group's probe response (when creating) or ignores field (when updating)  # noqa: E501

        :param probe_response: The probe_response of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :type: str
        """

        self._probe_response = probe_response

    @property
    def roaming_devices_added(self):
        """Gets the roaming_devices_added of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501

        The list of endpoint devices' client identifiers that will be disassociated from the group they are currently associated with and associated with this group..  # noqa: E501

        :return: The roaming_devices_added of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :rtype: list[str]
        """
        return self._roaming_devices_added

    @roaming_devices_added.setter
    def roaming_devices_added(self, roaming_devices_added):
        """Sets the roaming_devices_added of this AtcepRoamingDeviceGroupUpdate.

        The list of endpoint devices' client identifiers that will be disassociated from the group they are currently associated with and associated with this group..  # noqa: E501

        :param roaming_devices_added: The roaming_devices_added of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :type: list[str]
        """

        self._roaming_devices_added = roaming_devices_added

    @property
    def roaming_devices_deleted(self):
        """Gets the roaming_devices_deleted of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501

        The list of endpoint devices' client identifiers that will be disassociated from this group and associated with the default roaming clients group for the account.  # noqa: E501

        :return: The roaming_devices_deleted of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :rtype: list[str]
        """
        return self._roaming_devices_deleted

    @roaming_devices_deleted.setter
    def roaming_devices_deleted(self, roaming_devices_deleted):
        """Sets the roaming_devices_deleted of this AtcepRoamingDeviceGroupUpdate.

        The list of endpoint devices' client identifiers that will be disassociated from this group and associated with the default roaming clients group for the account.  # noqa: E501

        :param roaming_devices_deleted: The roaming_devices_deleted of this AtcepRoamingDeviceGroupUpdate.  # noqa: E501
        :type: list[str]
        """

        self._roaming_devices_deleted = roaming_devices_deleted

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AtcepRoamingDeviceGroupUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AtcepRoamingDeviceGroupUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
