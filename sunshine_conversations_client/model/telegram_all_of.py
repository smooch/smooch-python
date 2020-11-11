# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class TelegramAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'token': 'str',
        'username': 'str',
        'bot_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'token': 'token',
        'username': 'username',
        'bot_id': 'botId'
    }

    nulls = set()

    def __init__(self, type='telegram', token=None, username=None, bot_id=None, local_vars_configuration=None):  # noqa: E501
        """TelegramAllOf - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._token = None
        self._username = None
        self._bot_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if token is not None:
            self.token = token
        if username is not None:
            self.username = username
        if bot_id is not None:
            self.bot_id = bot_id

    @property
    def type(self):
        """Gets the type of this TelegramAllOf.  # noqa: E501

        The type of integration.  # noqa: E501

        :return: The type of this TelegramAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TelegramAllOf.

        The type of integration.  # noqa: E501

        :param type: The type of this TelegramAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def token(self):
        """Gets the token of this TelegramAllOf.  # noqa: E501

        Telegram Bot Token.  # noqa: E501

        :return: The token of this TelegramAllOf.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this TelegramAllOf.

        Telegram Bot Token.  # noqa: E501

        :param token: The token of this TelegramAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and token is None:  # noqa: E501
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                token is not None and len(token) < 1):
            raise ValueError("Invalid value for `token`, length must be greater than or equal to `1`")  # noqa: E501

        self._token = token

    @property
    def username(self):
        """Gets the username of this TelegramAllOf.  # noqa: E501

        Username of the botId  # noqa: E501

        :return: The username of this TelegramAllOf.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this TelegramAllOf.

        Username of the botId  # noqa: E501

        :param username: The username of this TelegramAllOf.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def bot_id(self):
        """Gets the bot_id of this TelegramAllOf.  # noqa: E501

        A human-friendly name used to identify the integration.  # noqa: E501

        :return: The bot_id of this TelegramAllOf.  # noqa: E501
        :rtype: str
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """Sets the bot_id of this TelegramAllOf.

        A human-friendly name used to identify the integration.  # noqa: E501

        :param bot_id: The bot_id of this TelegramAllOf.  # noqa: E501
        :type: str
        """

        self._bot_id = bot_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TelegramAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TelegramAllOf):
            return True

        return self.to_dict() != other.to_dict()