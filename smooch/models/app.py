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


class App(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, app_token=None, name=None):
        """
        App - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'app_token': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'id': '_id',
            'app_token': 'appToken',
            'name': 'name'
        }

        self._id = id
        self._app_token = app_token
        self._name = name

    @property
    def id(self):
        """
        Gets the id of this App.
        The app's ID.

        :return: The id of this App.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this App.
        The app's ID.

        :param id: The id of this App.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def app_token(self):
        """
        Gets the app_token of this App.
        The appToken, used to initialize the Web, iOS and Android clients and to make calls to the app user facing API.

        :return: The app_token of this App.
        :rtype: str
        """
        return self._app_token

    @app_token.setter
    def app_token(self, app_token):
        """
        Sets the app_token of this App.
        The appToken, used to initialize the Web, iOS and Android clients and to make calls to the app user facing API.

        :param app_token: The app_token of this App.
        :type: str
        """
        if app_token is None:
            raise ValueError("Invalid value for `app_token`, must not be `None`")

        self._app_token = app_token

    @property
    def name(self):
        """
        Gets the name of this App.
        The app's name.

        :return: The name of this App.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this App.
        The app's name.

        :param name: The name of this App.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

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
        if not isinstance(other, App):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
