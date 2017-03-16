# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ClientInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, app_name=None, device_model=None, os=None, os_version=None, radio_access_technology=None, carrier=None, device_platform=None, wifi=None):
        """
        ClientInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'app_name': 'str',
            'device_model': 'str',
            'os': 'str',
            'os_version': 'str',
            'radio_access_technology': 'str',
            'carrier': 'str',
            'device_platform': 'str',
            'wifi': 'str'
        }

        self.attribute_map = {
            'app_name': 'appName',
            'device_model': 'deviceModel',
            'os': 'os',
            'os_version': 'osVersion',
            'radio_access_technology': 'radioAccessTechnology',
            'carrier': 'carrier',
            'device_platform': 'devicePlatform',
            'wifi': 'wifi'
        }

        self._app_name = app_name
        self._device_model = device_model
        self._os = os
        self._os_version = os_version
        self._radio_access_technology = radio_access_technology
        self._carrier = carrier
        self._device_platform = device_platform
        self._wifi = wifi

    @property
    def app_name(self):
        """
        Gets the app_name of this ClientInfo.
        Name of the app associated with the client.

        :return: The app_name of this ClientInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """
        Sets the app_name of this ClientInfo.
        Name of the app associated with the client.

        :param app_name: The app_name of this ClientInfo.
        :type: str
        """

        self._app_name = app_name

    @property
    def device_model(self):
        """
        Gets the device_model of this ClientInfo.
        The client's device model.

        :return: The device_model of this ClientInfo.
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """
        Sets the device_model of this ClientInfo.
        The client's device model.

        :param device_model: The device_model of this ClientInfo.
        :type: str
        """

        self._device_model = device_model

    @property
    def os(self):
        """
        Gets the os of this ClientInfo.
        The client's OS.

        :return: The os of this ClientInfo.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """
        Sets the os of this ClientInfo.
        The client's OS.

        :param os: The os of this ClientInfo.
        :type: str
        """

        self._os = os

    @property
    def os_version(self):
        """
        Gets the os_version of this ClientInfo.
        The client's OS version.

        :return: The os_version of this ClientInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """
        Sets the os_version of this ClientInfo.
        The client's OS version.

        :param os_version: The os_version of this ClientInfo.
        :type: str
        """

        self._os_version = os_version

    @property
    def radio_access_technology(self):
        """
        Gets the radio_access_technology of this ClientInfo.
        The client's radioAccessTechnology (Ex. HSDPA).

        :return: The radio_access_technology of this ClientInfo.
        :rtype: str
        """
        return self._radio_access_technology

    @radio_access_technology.setter
    def radio_access_technology(self, radio_access_technology):
        """
        Sets the radio_access_technology of this ClientInfo.
        The client's radioAccessTechnology (Ex. HSDPA).

        :param radio_access_technology: The radio_access_technology of this ClientInfo.
        :type: str
        """

        self._radio_access_technology = radio_access_technology

    @property
    def carrier(self):
        """
        Gets the carrier of this ClientInfo.
        The client's carrier.

        :return: The carrier of this ClientInfo.
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """
        Sets the carrier of this ClientInfo.
        The client's carrier.

        :param carrier: The carrier of this ClientInfo.
        :type: str
        """

        self._carrier = carrier

    @property
    def device_platform(self):
        """
        Gets the device_platform of this ClientInfo.
        The client's device platform.

        :return: The device_platform of this ClientInfo.
        :rtype: str
        """
        return self._device_platform

    @device_platform.setter
    def device_platform(self, device_platform):
        """
        Sets the device_platform of this ClientInfo.
        The client's device platform.

        :param device_platform: The device_platform of this ClientInfo.
        :type: str
        """

        self._device_platform = device_platform

    @property
    def wifi(self):
        """
        Gets the wifi of this ClientInfo.
        Whether or not the client has wifi.

        :return: The wifi of this ClientInfo.
        :rtype: str
        """
        return self._wifi

    @wifi.setter
    def wifi(self, wifi):
        """
        Sets the wifi of this ClientInfo.
        Whether or not the client has wifi.

        :param wifi: The wifi of this ClientInfo.
        :type: str
        """

        self._wifi = wifi

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ClientInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other