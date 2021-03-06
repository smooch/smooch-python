# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.29
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SubMenuItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, text=None, uri=None, type=None, payload=None):
        """
        SubMenuItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'text': 'str',
            'uri': 'str',
            'type': 'str',
            'payload': 'str'
        }

        self.attribute_map = {
            'text': 'text',
            'uri': 'uri',
            'type': 'type',
            'payload': 'payload'
        }

        self._text = None
        self._uri = None
        self._type = None
        self._payload = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if text is not None:
          self.text = text
        if uri is not None:
          self.uri = uri
        if type is not None:
          self.type = type
        if payload is not None:
          self.payload = payload

    @property
    def text(self):
        """
        Gets the text of this SubMenuItem.
        The button text of the menu item.

        :return: The text of this SubMenuItem.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this SubMenuItem.
        The button text of the menu item.

        :param text: The text of this SubMenuItem.
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")

        self._text = text

    @property
    def uri(self):
        """
        Gets the uri of this SubMenuItem.
        A valid address, like http://smooch.io. Required for a link type item.

        :return: The uri of this SubMenuItem.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this SubMenuItem.
        A valid address, like http://smooch.io. Required for a link type item.

        :param uri: The uri of this SubMenuItem.
        :type: str
        """

        self._uri = uri

    @property
    def type(self):
        """
        Gets the type of this SubMenuItem.
        Can either be link, postback, which correspond to Smooch’s link and postback actions, or submenu for nested menus. See [**MenuItemTypeEnum**](Enums.md#MenuItemTypeEnum) for available values.

        :return: The type of this SubMenuItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SubMenuItem.
        Can either be link, postback, which correspond to Smooch’s link and postback actions, or submenu for nested menus. See [**MenuItemTypeEnum**](Enums.md#MenuItemTypeEnum) for available values.

        :param type: The type of this SubMenuItem.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def payload(self):
        """
        Gets the payload of this SubMenuItem.
        A payload for a postback. Required for a postback type item.

        :return: The payload of this SubMenuItem.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this SubMenuItem.
        A payload for a postback. Required for a postback type item.

        :param payload: The payload of this SubMenuItem.
        :type: str
        """

        self._payload = payload

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
        if not isinstance(other, SubMenuItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
