# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AppSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, mask_credit_card_numbers=None, use_animal_names=None, conversation_retention_seconds=None, echo_postback=None):
        """
        AppSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'mask_credit_card_numbers': 'bool',
            'use_animal_names': 'bool',
            'conversation_retention_seconds': 'int',
            'echo_postback': 'bool'
        }

        self.attribute_map = {
            'mask_credit_card_numbers': 'maskCreditCardNumbers',
            'use_animal_names': 'useAnimalNames',
            'conversation_retention_seconds': 'conversationRetentionSeconds',
            'echo_postback': 'echoPostback'
        }

        self._mask_credit_card_numbers = None
        self._use_animal_names = None
        self._conversation_retention_seconds = None
        self._echo_postback = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if mask_credit_card_numbers is not None:
          self.mask_credit_card_numbers = mask_credit_card_numbers
        if use_animal_names is not None:
          self.use_animal_names = use_animal_names
        if conversation_retention_seconds is not None:
          self.conversation_retention_seconds = conversation_retention_seconds
        if echo_postback is not None:
          self.echo_postback = echo_postback

    @property
    def mask_credit_card_numbers(self):
        """
        Gets the mask_credit_card_numbers of this AppSettings.
        Flag specifying whether credit card numbers will be automatically masked if sent through Smooch.

        :return: The mask_credit_card_numbers of this AppSettings.
        :rtype: bool
        """
        return self._mask_credit_card_numbers

    @mask_credit_card_numbers.setter
    def mask_credit_card_numbers(self, mask_credit_card_numbers):
        """
        Sets the mask_credit_card_numbers of this AppSettings.
        Flag specifying whether credit card numbers will be automatically masked if sent through Smooch.

        :param mask_credit_card_numbers: The mask_credit_card_numbers of this AppSettings.
        :type: bool
        """

        self._mask_credit_card_numbers = mask_credit_card_numbers

    @property
    def use_animal_names(self):
        """
        Gets the use_animal_names of this AppSettings.
        Flag specifying whether animal names should be used for anonymous users.

        :return: The use_animal_names of this AppSettings.
        :rtype: bool
        """
        return self._use_animal_names

    @use_animal_names.setter
    def use_animal_names(self, use_animal_names):
        """
        Sets the use_animal_names of this AppSettings.
        Flag specifying whether animal names should be used for anonymous users.

        :param use_animal_names: The use_animal_names of this AppSettings.
        :type: bool
        """

        self._use_animal_names = use_animal_names

    @property
    def conversation_retention_seconds(self):
        """
        Gets the conversation_retention_seconds of this AppSettings.
        Number of seconds of inactivity before a conversation’s messages will be automatically deleted.

        :return: The conversation_retention_seconds of this AppSettings.
        :rtype: int
        """
        return self._conversation_retention_seconds

    @conversation_retention_seconds.setter
    def conversation_retention_seconds(self, conversation_retention_seconds):
        """
        Sets the conversation_retention_seconds of this AppSettings.
        Number of seconds of inactivity before a conversation’s messages will be automatically deleted.

        :param conversation_retention_seconds: The conversation_retention_seconds of this AppSettings.
        :type: int
        """

        self._conversation_retention_seconds = conversation_retention_seconds

    @property
    def echo_postback(self):
        """
        Gets the echo_postback of this AppSettings.
        A boolean specifying whether a message should be added to the conversation history when a postback button is clicked.

        :return: The echo_postback of this AppSettings.
        :rtype: bool
        """
        return self._echo_postback

    @echo_postback.setter
    def echo_postback(self, echo_postback):
        """
        Sets the echo_postback of this AppSettings.
        A boolean specifying whether a message should be added to the conversation history when a postback button is clicked.

        :param echo_postback: The echo_postback of this AppSettings.
        :type: bool
        """

        self._echo_postback = echo_postback

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
        if not isinstance(other, AppSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
