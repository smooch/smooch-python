# coding: utf-8

"""
    Smooch

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AppUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, user_id=None, given_name=None, surname=None, properties=None, conversation_started=None, clients=None):
        """
        AppUser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'user_id': 'str',
            'given_name': 'str',
            'surname': 'str',
            'properties': 'object',
            'conversation_started': 'bool',
            'clients': 'list[Client]'
        }

        self.attribute_map = {
            'id': '_id',
            'user_id': 'userId',
            'given_name': 'givenName',
            'surname': 'surname',
            'properties': 'properties',
            'conversation_started': 'conversationStarted',
            'clients': 'clients'
        }

        self._id = id
        self._user_id = user_id
        self._given_name = given_name
        self._surname = surname
        self._properties = properties
        self._conversation_started = conversation_started
        self._clients = clients

    @property
    def id(self):
        """
        Gets the id of this AppUser.
        The app user's ID, generated automatically.

        :return: The id of this AppUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AppUser.
        The app user's ID, generated automatically.

        :param id: The id of this AppUser.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this AppUser.
        The app user's userId. This ID is specified by the appMaker. 

        :return: The user_id of this AppUser.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AppUser.
        The app user's userId. This ID is specified by the appMaker. 

        :param user_id: The user_id of this AppUser.
        :type: str
        """

        self._user_id = user_id

    @property
    def given_name(self):
        """
        Gets the given_name of this AppUser.
        The app user's given name.

        :return: The given_name of this AppUser.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """
        Sets the given_name of this AppUser.
        The app user's given name.

        :param given_name: The given_name of this AppUser.
        :type: str
        """

        self._given_name = given_name

    @property
    def surname(self):
        """
        Gets the surname of this AppUser.
        The app user's surname.

        :return: The surname of this AppUser.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """
        Sets the surname of this AppUser.
        The app user's surname.

        :param surname: The surname of this AppUser.
        :type: str
        """

        self._surname = surname

    @property
    def properties(self):
        """
        Gets the properties of this AppUser.
        Custom properties for the app user.

        :return: The properties of this AppUser.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this AppUser.
        Custom properties for the app user.

        :param properties: The properties of this AppUser.
        :type: object
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")

        self._properties = properties

    @property
    def conversation_started(self):
        """
        Gets the conversation_started of this AppUser.
        Flag specifying whether the conversation has started for the app user.

        :return: The conversation_started of this AppUser.
        :rtype: bool
        """
        return self._conversation_started

    @conversation_started.setter
    def conversation_started(self, conversation_started):
        """
        Sets the conversation_started of this AppUser.
        Flag specifying whether the conversation has started for the app user.

        :param conversation_started: The conversation_started of this AppUser.
        :type: bool
        """
        if conversation_started is None:
            raise ValueError("Invalid value for `conversation_started`, must not be `None`")

        self._conversation_started = conversation_started

    @property
    def clients(self):
        """
        Gets the clients of this AppUser.
        List of clients associated with the app user.

        :return: The clients of this AppUser.
        :rtype: list[Client]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """
        Sets the clients of this AppUser.
        List of clients associated with the app user.

        :param clients: The clients of this AppUser.
        :type: list[Client]
        """

        self._clients = clients

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
        if not isinstance(other, AppUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
