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


class Client(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, status=None, external_id=None, active=None, last_seen=None, platform=None, integration_id=None, push_notification_token=None, app_version=None, display_name=None, info=None, raw=None):
        """
        Client - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'status': 'str',
            'external_id': 'str',
            'active': 'bool',
            'last_seen': 'str',
            'platform': 'str',
            'integration_id': 'str',
            'push_notification_token': 'str',
            'app_version': 'str',
            'display_name': 'str',
            'info': 'ClientInfo',
            'raw': 'object'
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status',
            'external_id': 'externalId',
            'active': 'active',
            'last_seen': 'lastSeen',
            'platform': 'platform',
            'integration_id': 'integrationId',
            'push_notification_token': 'pushNotificationToken',
            'app_version': 'appVersion',
            'display_name': 'displayName',
            'info': 'info',
            'raw': 'raw'
        }

        self._id = None
        self._status = None
        self._external_id = None
        self._active = None
        self._last_seen = None
        self._platform = None
        self._integration_id = None
        self._push_notification_token = None
        self._app_version = None
        self._display_name = None
        self._info = None
        self._raw = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if id is not None:
          self.id = id
        if status is not None:
          self.status = status
        if external_id is not None:
          self.external_id = external_id
        if active is not None:
          self.active = active
        if last_seen is not None:
          self.last_seen = last_seen
        if platform is not None:
          self.platform = platform
        if integration_id is not None:
          self.integration_id = integration_id
        if push_notification_token is not None:
          self.push_notification_token = push_notification_token
        if app_version is not None:
          self.app_version = app_version
        if display_name is not None:
          self.display_name = display_name
        if info is not None:
          self.info = info
        if raw is not None:
          self.raw = raw

    @property
    def id(self):
        """
        Gets the id of this Client.
        An identifier for the client. Must be globally unique.

        :return: The id of this Client.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Client.
        An identifier for the client. Must be globally unique.

        :param id: The id of this Client.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def status(self):
        """
        Gets the status of this Client.
        The client status. Indicates if the client is able to receive messages or not. See [**ClientStatusEnum**](Enums.md#ClientStatusEnum) for available values.

        :return: The status of this Client.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Client.
        The client status. Indicates if the client is able to receive messages or not. See [**ClientStatusEnum**](Enums.md#ClientStatusEnum) for available values.

        :param status: The status of this Client.
        :type: str
        """

        self._status = status

    @property
    def external_id(self):
        """
        Gets the external_id of this Client.
        The ID of the user on an external channel. For example, the user's phone number for Twilio, or their page-scoped user ID for Facebook Messenger. Applies only to non-SDK clients.

        :return: The external_id of this Client.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this Client.
        The ID of the user on an external channel. For example, the user's phone number for Twilio, or their page-scoped user ID for Facebook Messenger. Applies only to non-SDK clients.

        :param external_id: The external_id of this Client.
        :type: str
        """

        self._external_id = external_id

    @property
    def active(self):
        """
        Gets the active of this Client.
        Deprecated - use the status property instead.

        :return: The active of this Client.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Client.
        Deprecated - use the status property instead.

        :param active: The active of this Client.
        :type: bool
        """

        self._active = active

    @property
    def last_seen(self):
        """
        Gets the last_seen of this Client.
        The date time the client was last seen.

        :return: The last_seen of this Client.
        :rtype: str
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """
        Sets the last_seen of this Client.
        The date time the client was last seen.

        :param last_seen: The last_seen of this Client.
        :type: str
        """

        self._last_seen = last_seen

    @property
    def platform(self):
        """
        Gets the platform of this Client.
        The client's platform. See [**IntegrationTypeEnum**](Enums.md#IntegrationTypeEnum) for available values.

        :return: The platform of this Client.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """
        Sets the platform of this Client.
        The client's platform. See [**IntegrationTypeEnum**](Enums.md#IntegrationTypeEnum) for available values.

        :param platform: The platform of this Client.
        :type: str
        """
        if platform is None:
            raise ValueError("Invalid value for `platform`, must not be `None`")

        self._platform = platform

    @property
    def integration_id(self):
        """
        Gets the integration_id of this Client.
        The ID of the integration that the client was created for.

        :return: The integration_id of this Client.
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """
        Sets the integration_id of this Client.
        The ID of the integration that the client was created for.

        :param integration_id: The integration_id of this Client.
        :type: str
        """

        self._integration_id = integration_id

    @property
    def push_notification_token(self):
        """
        Gets the push_notification_token of this Client.
        The GCM or APN token to be used for sending push notifications to the device. Applies to only *android* and *ios* clients. 

        :return: The push_notification_token of this Client.
        :rtype: str
        """
        return self._push_notification_token

    @push_notification_token.setter
    def push_notification_token(self, push_notification_token):
        """
        Sets the push_notification_token of this Client.
        The GCM or APN token to be used for sending push notifications to the device. Applies to only *android* and *ios* clients. 

        :param push_notification_token: The push_notification_token of this Client.
        :type: str
        """

        self._push_notification_token = push_notification_token

    @property
    def app_version(self):
        """
        Gets the app_version of this Client.
        A reserved string field for reporting the app version running on the device.

        :return: The app_version of this Client.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """
        Sets the app_version of this Client.
        A reserved string field for reporting the app version running on the device.

        :param app_version: The app_version of this Client.
        :type: str
        """

        self._app_version = app_version

    @property
    def display_name(self):
        """
        Gets the display_name of this Client.
        The client's display name.

        :return: The display_name of this Client.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Client.
        The client's display name.

        :param display_name: The display_name of this Client.
        :type: str
        """

        self._display_name = display_name

    @property
    def info(self):
        """
        Gets the info of this Client.

        :return: The info of this Client.
        :rtype: ClientInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this Client.

        :param info: The info of this Client.
        :type: ClientInfo
        """

        self._info = info

    @property
    def raw(self):
        """
        Gets the raw of this Client.
        An Object with raw properties that vary for each client platform. All keys are optional and not guaranteed to be available.

        :return: The raw of this Client.
        :rtype: object
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """
        Sets the raw of this Client.
        An Object with raw properties that vary for each client platform. All keys are optional and not guaranteed to be available.

        :param raw: The raw of this Client.
        :type: object
        """

        self._raw = raw

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
        if not isinstance(other, Client):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
