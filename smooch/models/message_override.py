# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.25
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class MessageOverride(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, whatsapp=None, line=None, messenger=None):
        """
        MessageOverride - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'whatsapp': 'MessageOverrideWhatsapp',
            'line': 'MessageOverrideLine',
            'messenger': 'MessageOverrideMessenger'
        }

        self.attribute_map = {
            'whatsapp': 'whatsapp',
            'line': 'line',
            'messenger': 'messenger'
        }

        self._whatsapp = None
        self._line = None
        self._messenger = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if whatsapp is not None:
          self.whatsapp = whatsapp
        if line is not None:
          self.line = line
        if messenger is not None:
          self.messenger = messenger

    @property
    def whatsapp(self):
        """
        Gets the whatsapp of this MessageOverride.

        :return: The whatsapp of this MessageOverride.
        :rtype: MessageOverrideWhatsapp
        """
        return self._whatsapp

    @whatsapp.setter
    def whatsapp(self, whatsapp):
        """
        Sets the whatsapp of this MessageOverride.

        :param whatsapp: The whatsapp of this MessageOverride.
        :type: MessageOverrideWhatsapp
        """

        self._whatsapp = whatsapp

    @property
    def line(self):
        """
        Gets the line of this MessageOverride.

        :return: The line of this MessageOverride.
        :rtype: MessageOverrideLine
        """
        return self._line

    @line.setter
    def line(self, line):
        """
        Sets the line of this MessageOverride.

        :param line: The line of this MessageOverride.
        :type: MessageOverrideLine
        """

        self._line = line

    @property
    def messenger(self):
        """
        Gets the messenger of this MessageOverride.

        :return: The messenger of this MessageOverride.
        :rtype: MessageOverrideMessenger
        """
        return self._messenger

    @messenger.setter
    def messenger(self, messenger):
        """
        Sets the messenger of this MessageOverride.

        :param messenger: The messenger of this MessageOverride.
        :type: MessageOverrideMessenger
        """

        self._messenger = messenger

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
        if not isinstance(other, MessageOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
