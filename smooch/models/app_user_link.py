# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 3.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AppUserLink(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, phone_number=None, address=None, given_name=None, surname=None, subject=None, skip_confirmation=None, confirmation=None):
        """
        AppUserLink - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'phone_number': 'str',
            'address': 'str',
            'given_name': 'str',
            'surname': 'str',
            'subject': 'str',
            'skip_confirmation': 'str',
            'confirmation': 'Confirmation'
        }

        self.attribute_map = {
            'type': 'type',
            'phone_number': 'phoneNumber',
            'address': 'address',
            'given_name': 'givenName',
            'surname': 'surname',
            'subject': 'subject',
            'skip_confirmation': 'skipConfirmation',
            'confirmation': 'confirmation'
        }

        self._type = None
        self._phone_number = None
        self._address = None
        self._given_name = None
        self._surname = None
        self._subject = None
        self._skip_confirmation = None
        self._confirmation = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if type is not None:
          self.type = type
        if phone_number is not None:
          self.phone_number = phone_number
        if address is not None:
          self.address = address
        if given_name is not None:
          self.given_name = given_name
        if surname is not None:
          self.surname = surname
        if subject is not None:
          self.subject = subject
        if skip_confirmation is not None:
          self.skip_confirmation = skip_confirmation
        if confirmation is not None:
          self.confirmation = confirmation

    @property
    def type(self):
        """
        Gets the type of this AppUserLink.
        The type of the channel to link.

        :return: The type of this AppUserLink.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AppUserLink.
        The type of the channel to link.

        :param type: The type of this AppUserLink.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def phone_number(self):
        """
        Gets the phone_number of this AppUserLink.
        A String of the appUser’s phone number. It must contain the + prefix and the country code. Required for *messenger*, *twilio* and *messagebird* linking. 

        :return: The phone_number of this AppUserLink.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this AppUserLink.
        A String of the appUser’s phone number. It must contain the + prefix and the country code. Required for *messenger*, *twilio* and *messagebird* linking. 

        :param phone_number: The phone_number of this AppUserLink.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def address(self):
        """
        Gets the address of this AppUserLink.
        A String of the appUser’s email address. Required for *mailgun* linking. 

        :return: The address of this AppUserLink.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this AppUserLink.
        A String of the appUser’s email address. Required for *mailgun* linking. 

        :param address: The address of this AppUserLink.
        :type: str
        """

        self._address = address

    @property
    def given_name(self):
        """
        Gets the given_name of this AppUserLink.
        A String of the appUser’s given name. Used as additional criteria to increase the likelihood of a match. (Optional) Used for *messenger* linking. 

        :return: The given_name of this AppUserLink.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """
        Sets the given_name of this AppUserLink.
        A String of the appUser’s given name. Used as additional criteria to increase the likelihood of a match. (Optional) Used for *messenger* linking. 

        :param given_name: The given_name of this AppUserLink.
        :type: str
        """

        self._given_name = given_name

    @property
    def surname(self):
        """
        Gets the surname of this AppUserLink.
        A String of the appUser’s surname. Used as additional criteria to increase the likelihood of a match. (Optional) Used for *messenger* linking. 

        :return: The surname of this AppUserLink.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """
        Sets the surname of this AppUserLink.
        A String of the appUser’s surname. Used as additional criteria to increase the likelihood of a match. (Optional) Used for *messenger* linking. 

        :param surname: The surname of this AppUserLink.
        :type: str
        """

        self._surname = surname

    @property
    def subject(self):
        """
        Gets the subject of this AppUserLink.
        Subject for the outgoing email. (Optional) Used for *mailgun* linking. 

        :return: The subject of this AppUserLink.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this AppUserLink.
        Subject for the outgoing email. (Optional) Used for *mailgun* linking. 

        :param subject: The subject of this AppUserLink.
        :type: str
        """

        self._subject = subject

    @property
    def skip_confirmation(self):
        """
        Gets the skip_confirmation of this AppUserLink.
        (Deprecated, use confirmation instead) Flag indicating if the linking confirmation should be skipped.

        :return: The skip_confirmation of this AppUserLink.
        :rtype: str
        """
        return self._skip_confirmation

    @skip_confirmation.setter
    def skip_confirmation(self, skip_confirmation):
        """
        Sets the skip_confirmation of this AppUserLink.
        (Deprecated, use confirmation instead) Flag indicating if the linking confirmation should be skipped.

        :param skip_confirmation: The skip_confirmation of this AppUserLink.
        :type: str
        """

        self._skip_confirmation = skip_confirmation

    @property
    def confirmation(self):
        """
        Gets the confirmation of this AppUserLink.
        Allows you to specify the strategy used to initiate a link with the target user.

        :return: The confirmation of this AppUserLink.
        :rtype: Confirmation
        """
        return self._confirmation

    @confirmation.setter
    def confirmation(self, confirmation):
        """
        Sets the confirmation of this AppUserLink.
        Allows you to specify the strategy used to initiate a link with the target user.

        :param confirmation: The confirmation of this AppUserLink.
        :type: Confirmation
        """
        if confirmation is None:
            raise ValueError("Invalid value for `confirmation`, must not be `None`")

        self._confirmation = confirmation

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
        if not isinstance(other, AppUserLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
