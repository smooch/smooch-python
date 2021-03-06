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


class Destination(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, integration_id=None, integration_type=None):
        """
        Destination - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'integration_id': 'str',
            'integration_type': 'str'
        }

        self.attribute_map = {
            'integration_id': 'integrationId',
            'integration_type': 'integrationType'
        }

        self._integration_id = None
        self._integration_type = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if integration_id is not None:
          self.integration_id = integration_id
        if integration_type is not None:
          self.integration_type = integration_type

    @property
    def integration_id(self):
        """
        Gets the integration_id of this Destination.
        The ID of the target integration.

        :return: The integration_id of this Destination.
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """
        Sets the integration_id of this Destination.
        The ID of the target integration.

        :param integration_id: The integration_id of this Destination.
        :type: str
        """
        if integration_id is None:
            raise ValueError("Invalid value for `integration_id`, must not be `None`")

        self._integration_id = integration_id

    @property
    def integration_type(self):
        """
        Gets the integration_type of this Destination.
        The type of the target integration. See [**IntegrationTypeEnum**](Enums.md#IntegrationTypeEnum) for available values.

        :return: The integration_type of this Destination.
        :rtype: str
        """
        return self._integration_type

    @integration_type.setter
    def integration_type(self, integration_type):
        """
        Sets the integration_type of this Destination.
        The type of the target integration. See [**IntegrationTypeEnum**](Enums.md#IntegrationTypeEnum) for available values.

        :param integration_type: The integration_type of this Destination.
        :type: str
        """
        if integration_type is None:
            raise ValueError("Invalid value for `integration_type`, must not be `None`")

        self._integration_type = integration_type

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
        if not isinstance(other, Destination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
