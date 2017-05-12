# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Integration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, type=None, page_access_token=None, app_id=None, app_secret=None, account_sid=None, auth_token=None, phone_number_sid=None, token=None, channel_access_token=None, encoding_aes_key=None, from_address=None, certificate=None, password=None, auto_update_badge=None, server_key=None, sender_id=None):
        """
        Integration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'page_access_token': 'str',
            'app_id': 'str',
            'app_secret': 'str',
            'account_sid': 'str',
            'auth_token': 'str',
            'phone_number_sid': 'str',
            'token': 'str',
            'channel_access_token': 'str',
            'encoding_aes_key': 'str',
            'from_address': 'str',
            'certificate': 'str',
            'password': 'str',
            'auto_update_badge': 'bool',
            'server_key': 'str',
            'sender_id': 'str'
        }

        self.attribute_map = {
            'id': '_id',
            'type': 'type',
            'page_access_token': 'pageAccessToken',
            'app_id': 'appId',
            'app_secret': 'appSecret',
            'account_sid': 'accountSid',
            'auth_token': 'authToken',
            'phone_number_sid': 'phoneNumberSid',
            'token': 'token',
            'channel_access_token': 'channelAccessToken',
            'encoding_aes_key': 'encodingAesKey',
            'from_address': 'fromAddress',
            'certificate': 'certificate',
            'password': 'password',
            'auto_update_badge': 'autoUpdateBadge',
            'server_key': 'serverKey',
            'sender_id': 'senderId'
        }

        self._id = None
        self._type = None
        self._page_access_token = None
        self._app_id = None
        self._app_secret = None
        self._account_sid = None
        self._auth_token = None
        self._phone_number_sid = None
        self._token = None
        self._channel_access_token = None
        self._encoding_aes_key = None
        self._from_address = None
        self._certificate = None
        self._password = None
        self._auto_update_badge = None
        self._server_key = None
        self._sender_id = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if id is not None:
          self.id = id
        if type is not None:
          self.type = type
        if page_access_token is not None:
          self.page_access_token = page_access_token
        if app_id is not None:
          self.app_id = app_id
        if app_secret is not None:
          self.app_secret = app_secret
        if account_sid is not None:
          self.account_sid = account_sid
        if auth_token is not None:
          self.auth_token = auth_token
        if phone_number_sid is not None:
          self.phone_number_sid = phone_number_sid
        if token is not None:
          self.token = token
        if channel_access_token is not None:
          self.channel_access_token = channel_access_token
        if encoding_aes_key is not None:
          self.encoding_aes_key = encoding_aes_key
        if from_address is not None:
          self.from_address = from_address
        if certificate is not None:
          self.certificate = certificate
        if password is not None:
          self.password = password
        if auto_update_badge is not None:
          self.auto_update_badge = auto_update_badge
        if server_key is not None:
          self.server_key = server_key
        if sender_id is not None:
          self.sender_id = sender_id

    @property
    def id(self):
        """
        Gets the id of this Integration.
        The integration ID, generated automatically.

        :return: The id of this Integration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Integration.
        The integration ID, generated automatically.

        :param id: The id of this Integration.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def type(self):
        """
        Gets the type of this Integration.
        The integration type.

        :return: The type of this Integration.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Integration.
        The integration type.

        :param type: The type of this Integration.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def page_access_token(self):
        """
        Gets the page_access_token of this Integration.
        Facebook Page Access Token. Required for *messenger* integrations. 

        :return: The page_access_token of this Integration.
        :rtype: str
        """
        return self._page_access_token

    @page_access_token.setter
    def page_access_token(self, page_access_token):
        """
        Sets the page_access_token of this Integration.
        Facebook Page Access Token. Required for *messenger* integrations. 

        :param page_access_token: The page_access_token of this Integration.
        :type: str
        """

        self._page_access_token = page_access_token

    @property
    def app_id(self):
        """
        Gets the app_id of this Integration.
        Facebook App ID OR WeChat App ID. Required for *messenger* and *wechat* integrations. 

        :return: The app_id of this Integration.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """
        Sets the app_id of this Integration.
        Facebook App ID OR WeChat App ID. Required for *messenger* and *wechat* integrations. 

        :param app_id: The app_id of this Integration.
        :type: str
        """

        self._app_id = app_id

    @property
    def app_secret(self):
        """
        Gets the app_secret of this Integration.
        Facebook Page App Secret OR WeChat App Secret. Required for *messenger* and *wechat* integrations. 

        :return: The app_secret of this Integration.
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """
        Sets the app_secret of this Integration.
        Facebook Page App Secret OR WeChat App Secret. Required for *messenger* and *wechat* integrations. 

        :param app_secret: The app_secret of this Integration.
        :type: str
        """

        self._app_secret = app_secret

    @property
    def account_sid(self):
        """
        Gets the account_sid of this Integration.
        Twilio Account SID. Required for *twilio* integrations. 

        :return: The account_sid of this Integration.
        :rtype: str
        """
        return self._account_sid

    @account_sid.setter
    def account_sid(self, account_sid):
        """
        Sets the account_sid of this Integration.
        Twilio Account SID. Required for *twilio* integrations. 

        :param account_sid: The account_sid of this Integration.
        :type: str
        """

        self._account_sid = account_sid

    @property
    def auth_token(self):
        """
        Gets the auth_token of this Integration.
        Twilio Auth Token. Required for *twilio* integrations. 

        :return: The auth_token of this Integration.
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """
        Sets the auth_token of this Integration.
        Twilio Auth Token. Required for *twilio* integrations. 

        :param auth_token: The auth_token of this Integration.
        :type: str
        """

        self._auth_token = auth_token

    @property
    def phone_number_sid(self):
        """
        Gets the phone_number_sid of this Integration.
        SID for specific phone number. Required for *twilio* integrations. 

        :return: The phone_number_sid of this Integration.
        :rtype: str
        """
        return self._phone_number_sid

    @phone_number_sid.setter
    def phone_number_sid(self, phone_number_sid):
        """
        Sets the phone_number_sid of this Integration.
        SID for specific phone number. Required for *twilio* integrations. 

        :param phone_number_sid: The phone_number_sid of this Integration.
        :type: str
        """

        self._phone_number_sid = phone_number_sid

    @property
    def token(self):
        """
        Gets the token of this Integration.
        Telegram Bot Token OR Viber Public Account token. Required for *twilio* and *viber* integrations. 

        :return: The token of this Integration.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this Integration.
        Telegram Bot Token OR Viber Public Account token. Required for *twilio* and *viber* integrations. 

        :param token: The token of this Integration.
        :type: str
        """

        self._token = token

    @property
    def channel_access_token(self):
        """
        Gets the channel_access_token of this Integration.
        LINE Channel Access Token. Required for *line* integrations. 

        :return: The channel_access_token of this Integration.
        :rtype: str
        """
        return self._channel_access_token

    @channel_access_token.setter
    def channel_access_token(self, channel_access_token):
        """
        Sets the channel_access_token of this Integration.
        LINE Channel Access Token. Required for *line* integrations. 

        :param channel_access_token: The channel_access_token of this Integration.
        :type: str
        """

        self._channel_access_token = channel_access_token

    @property
    def encoding_aes_key(self):
        """
        Gets the encoding_aes_key of this Integration.
        AES Encoding Key. (Optional) Used for *wechat* integrations. 

        :return: The encoding_aes_key of this Integration.
        :rtype: str
        """
        return self._encoding_aes_key

    @encoding_aes_key.setter
    def encoding_aes_key(self, encoding_aes_key):
        """
        Sets the encoding_aes_key of this Integration.
        AES Encoding Key. (Optional) Used for *wechat* integrations. 

        :param encoding_aes_key: The encoding_aes_key of this Integration.
        :type: str
        """

        self._encoding_aes_key = encoding_aes_key

    @property
    def from_address(self):
        """
        Gets the from_address of this Integration.
        Email will display as coming from this address. (Optional) Used for *frontendEmail* integrations. 

        :return: The from_address of this Integration.
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """
        Sets the from_address of this Integration.
        Email will display as coming from this address. (Optional) Used for *frontendEmail* integrations. 

        :param from_address: The from_address of this Integration.
        :type: str
        """

        self._from_address = from_address

    @property
    def certificate(self):
        """
        Gets the certificate of this Integration.
        The binary of your APN certificate base64 encoded. Required for *apn* integrations. 

        :return: The certificate of this Integration.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this Integration.
        The binary of your APN certificate base64 encoded. Required for *apn* integrations. 

        :param certificate: The certificate of this Integration.
        :type: str
        """

        self._certificate = certificate

    @property
    def password(self):
        """
        Gets the password of this Integration.
        The password for your APN certificate. (Optional) Used for *apn* integrations. 

        :return: The password of this Integration.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this Integration.
        The password for your APN certificate. (Optional) Used for *apn* integrations. 

        :param password: The password of this Integration.
        :type: str
        """

        self._password = password

    @property
    def auto_update_badge(self):
        """
        Gets the auto_update_badge of this Integration.
        Use the unread count of the conversation as the application badge. (Optional) Used for *apn* integrations. 

        :return: The auto_update_badge of this Integration.
        :rtype: bool
        """
        return self._auto_update_badge

    @auto_update_badge.setter
    def auto_update_badge(self, auto_update_badge):
        """
        Sets the auto_update_badge of this Integration.
        Use the unread count of the conversation as the application badge. (Optional) Used for *apn* integrations. 

        :param auto_update_badge: The auto_update_badge of this Integration.
        :type: bool
        """

        self._auto_update_badge = auto_update_badge

    @property
    def server_key(self):
        """
        Gets the server_key of this Integration.
        Your server key from the fcm console. Required for *fcm* integrations. 

        :return: The server_key of this Integration.
        :rtype: str
        """
        return self._server_key

    @server_key.setter
    def server_key(self, server_key):
        """
        Sets the server_key of this Integration.
        Your server key from the fcm console. Required for *fcm* integrations. 

        :param server_key: The server_key of this Integration.
        :type: str
        """

        self._server_key = server_key

    @property
    def sender_id(self):
        """
        Gets the sender_id of this Integration.
        Your sender id from the fcm console. Required for *fcm* integrations. 

        :return: The sender_id of this Integration.
        :rtype: str
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """
        Sets the sender_id of this Integration.
        Your sender id from the fcm console. Required for *fcm* integrations. 

        :param sender_id: The sender_id of this Integration.
        :type: str
        """

        self._sender_id = sender_id

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
        if not isinstance(other, Integration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
