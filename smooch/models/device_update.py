# coding: utf-8

"""
    Smooch

    The Smooch API allows you to craft entirely unique messaging experiences for your app and website as well as talk to any backend or external service. For more information, visit our [official documentation](https://docs.smooch.io/rest/). 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, push_notification_token=None, app_version=None, info=None):
        """
        DeviceUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'push_notification_token': 'str',
            'app_version': 'str',
            'info': 'ClientInfo'
        }

        self.attribute_map = {
            'push_notification_token': 'pushNotificationToken',
            'app_version': 'appVersion',
            'info': 'info'
        }

        self._push_notification_token = push_notification_token
        self._app_version = app_version
        self._info = info

    @property
    def push_notification_token(self):
        """
        Gets the push_notification_token of this DeviceUpdate.

        :return: The push_notification_token of this DeviceUpdate.
        :rtype: str
        """
        return self._push_notification_token

    @push_notification_token.setter
    def push_notification_token(self, push_notification_token):
        """
        Sets the push_notification_token of this DeviceUpdate.

        :param push_notification_token: The push_notification_token of this DeviceUpdate.
        :type: str
        """

        self._push_notification_token = push_notification_token

    @property
    def app_version(self):
        """
        Gets the app_version of this DeviceUpdate.

        :return: The app_version of this DeviceUpdate.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """
        Sets the app_version of this DeviceUpdate.

        :param app_version: The app_version of this DeviceUpdate.
        :type: str
        """

        self._app_version = app_version

    @property
    def info(self):
        """
        Gets the info of this DeviceUpdate.

        :return: The info of this DeviceUpdate.
        :rtype: ClientInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this DeviceUpdate.

        :param info: The info of this DeviceUpdate.
        :type: ClientInfo
        """

        self._info = info

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
        if not isinstance(other, DeviceUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
