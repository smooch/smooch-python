# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceInit(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, platform=None, push_notification_token=None, app_version=None, info=None):
        """
        DeviceInit - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'platform': 'str',
            'push_notification_token': 'str',
            'app_version': 'str',
            'info': 'ClientInfo'
        }

        self.attribute_map = {
            'id': 'id',
            'platform': 'platform',
            'push_notification_token': 'pushNotificationToken',
            'app_version': 'appVersion',
            'info': 'info'
        }

        self._id = id
        self._platform = platform
        self._push_notification_token = push_notification_token
        self._app_version = app_version
        self._info = info

    @property
    def id(self):
        """
        Gets the id of this DeviceInit.
        An identifier for the client. Must be globally unique.

        :return: The id of this DeviceInit.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeviceInit.
        An identifier for the client. Must be globally unique.

        :param id: The id of this DeviceInit.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def platform(self):
        """
        Gets the platform of this DeviceInit.
        The client's platform.

        :return: The platform of this DeviceInit.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """
        Sets the platform of this DeviceInit.
        The client's platform.

        :param platform: The platform of this DeviceInit.
        :type: str
        """
        allowed_values = ["ios", "android", "web", "other"]
        if platform not in allowed_values:
            raise ValueError(
                "Invalid value for `platform` ({0}), must be one of {1}"
                .format(platform, allowed_values)
            )

        self._platform = platform

    @property
    def push_notification_token(self):
        """
        Gets the push_notification_token of this DeviceInit.
        The GCM or APN token to be used for sending push notifications to the device. Applies to only *android* and *ios* clients. 

        :return: The push_notification_token of this DeviceInit.
        :rtype: str
        """
        return self._push_notification_token

    @push_notification_token.setter
    def push_notification_token(self, push_notification_token):
        """
        Sets the push_notification_token of this DeviceInit.
        The GCM or APN token to be used for sending push notifications to the device. Applies to only *android* and *ios* clients. 

        :param push_notification_token: The push_notification_token of this DeviceInit.
        :type: str
        """

        self._push_notification_token = push_notification_token

    @property
    def app_version(self):
        """
        Gets the app_version of this DeviceInit.
        A reserved string field for reporting the app version running on the device.

        :return: The app_version of this DeviceInit.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """
        Sets the app_version of this DeviceInit.
        A reserved string field for reporting the app version running on the device.

        :param app_version: The app_version of this DeviceInit.
        :type: str
        """

        self._app_version = app_version

    @property
    def info(self):
        """
        Gets the info of this DeviceInit.

        :return: The info of this DeviceInit.
        :rtype: ClientInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this DeviceInit.

        :param info: The info of this DeviceInit.
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
        if not isinstance(other, DeviceInit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
