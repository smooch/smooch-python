# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 2.1
    
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
    def __init__(self, id=None, type=None, page_access_token=None, app_id=None, app_secret=None, webhook_secret=None, page_id=None, account_sid=None, auth_token=None, phone_number_sid=None, phone_number=None, name=None, token=None, uri=None, channel_access_token=None, bot_name=None, encoding_aes_key=None, from_address=None, certificate=None, password=None, auto_update_badge=None, production=None, server_key=None, sender_id=None, consumer_key=None, consumer_secret=None, access_token_key=None, access_token_secret=None, user_id=None, username=None, api_key=None, domain=None, incoming_address=None, access_key=None, originator=None):
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
            'webhook_secret': 'str',
            'page_id': 'str',
            'account_sid': 'str',
            'auth_token': 'str',
            'phone_number_sid': 'str',
            'phone_number': 'str',
            'name': 'str',
            'token': 'str',
            'uri': 'str',
            'channel_access_token': 'str',
            'bot_name': 'str',
            'encoding_aes_key': 'str',
            'from_address': 'str',
            'certificate': 'str',
            'password': 'str',
            'auto_update_badge': 'bool',
            'production': 'bool',
            'server_key': 'str',
            'sender_id': 'str',
            'consumer_key': 'str',
            'consumer_secret': 'str',
            'access_token_key': 'str',
            'access_token_secret': 'str',
            'user_id': 'str',
            'username': 'str',
            'api_key': 'str',
            'domain': 'str',
            'incoming_address': 'str',
            'access_key': 'str',
            'originator': 'str'
        }

        self.attribute_map = {
            'id': '_id',
            'type': 'type',
            'page_access_token': 'pageAccessToken',
            'app_id': 'appId',
            'app_secret': 'appSecret',
            'webhook_secret': 'webhookSecret',
            'page_id': 'pageId',
            'account_sid': 'accountSid',
            'auth_token': 'authToken',
            'phone_number_sid': 'phoneNumberSid',
            'phone_number': 'phoneNumber',
            'name': 'name',
            'token': 'token',
            'uri': 'uri',
            'channel_access_token': 'channelAccessToken',
            'bot_name': 'botName',
            'encoding_aes_key': 'encodingAesKey',
            'from_address': 'fromAddress',
            'certificate': 'certificate',
            'password': 'password',
            'auto_update_badge': 'autoUpdateBadge',
            'production': 'production',
            'server_key': 'serverKey',
            'sender_id': 'senderId',
            'consumer_key': 'consumerKey',
            'consumer_secret': 'consumerSecret',
            'access_token_key': 'accessTokenKey',
            'access_token_secret': 'accessTokenSecret',
            'user_id': 'userId',
            'username': 'username',
            'api_key': 'apiKey',
            'domain': 'domain',
            'incoming_address': 'incomingAddress',
            'access_key': 'accessKey',
            'originator': 'originator'
        }

        self._id = None
        self._type = None
        self._page_access_token = None
        self._app_id = None
        self._app_secret = None
        self._webhook_secret = None
        self._page_id = None
        self._account_sid = None
        self._auth_token = None
        self._phone_number_sid = None
        self._phone_number = None
        self._name = None
        self._token = None
        self._uri = None
        self._channel_access_token = None
        self._bot_name = None
        self._encoding_aes_key = None
        self._from_address = None
        self._certificate = None
        self._password = None
        self._auto_update_badge = None
        self._production = None
        self._server_key = None
        self._sender_id = None
        self._consumer_key = None
        self._consumer_secret = None
        self._access_token_key = None
        self._access_token_secret = None
        self._user_id = None
        self._username = None
        self._api_key = None
        self._domain = None
        self._incoming_address = None
        self._access_key = None
        self._originator = None

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
        if webhook_secret is not None:
          self.webhook_secret = webhook_secret
        if page_id is not None:
          self.page_id = page_id
        if account_sid is not None:
          self.account_sid = account_sid
        if auth_token is not None:
          self.auth_token = auth_token
        if phone_number_sid is not None:
          self.phone_number_sid = phone_number_sid
        if phone_number is not None:
          self.phone_number = phone_number
        if name is not None:
          self.name = name
        if token is not None:
          self.token = token
        if uri is not None:
          self.uri = uri
        if channel_access_token is not None:
          self.channel_access_token = channel_access_token
        if bot_name is not None:
          self.bot_name = bot_name
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
        if production is not None:
          self.production = production
        if server_key is not None:
          self.server_key = server_key
        if sender_id is not None:
          self.sender_id = sender_id
        if consumer_key is not None:
          self.consumer_key = consumer_key
        if consumer_secret is not None:
          self.consumer_secret = consumer_secret
        if access_token_key is not None:
          self.access_token_key = access_token_key
        if access_token_secret is not None:
          self.access_token_secret = access_token_secret
        if user_id is not None:
          self.user_id = user_id
        if username is not None:
          self.username = username
        if api_key is not None:
          self.api_key = api_key
        if domain is not None:
          self.domain = domain
        if incoming_address is not None:
          self.incoming_address = incoming_address
        if access_key is not None:
          self.access_key = access_key
        if originator is not None:
          self.originator = originator

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
    def webhook_secret(self):
        """
        Gets the webhook_secret of this Integration.
        Secret to verify webhooks. Returned on successful *wechat* and *messagebird* integrations. 

        :return: The webhook_secret of this Integration.
        :rtype: str
        """
        return self._webhook_secret

    @webhook_secret.setter
    def webhook_secret(self, webhook_secret):
        """
        Sets the webhook_secret of this Integration.
        Secret to verify webhooks. Returned on successful *wechat* and *messagebird* integrations. 

        :param webhook_secret: The webhook_secret of this Integration.
        :type: str
        """

        self._webhook_secret = webhook_secret

    @property
    def page_id(self):
        """
        Gets the page_id of this Integration.
        Facebook Page App ID. Returned on successful *messenger* integrations. 

        :return: The page_id of this Integration.
        :rtype: str
        """
        return self._page_id

    @page_id.setter
    def page_id(self, page_id):
        """
        Sets the page_id of this Integration.
        Facebook Page App ID. Returned on successful *messenger* integrations. 

        :param page_id: The page_id of this Integration.
        :type: str
        """

        self._page_id = page_id

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
    def phone_number(self):
        """
        Gets the phone_number of this Integration.
        Smooch will receive all messages sent to this phone number. Returned on successful *twilio* integrations. 

        :return: The phone_number of this Integration.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this Integration.
        Smooch will receive all messages sent to this phone number. Returned on successful *twilio* integrations. 

        :param phone_number: The phone_number of this Integration.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def name(self):
        """
        Gets the name of this Integration.
        Name on the account. Returned on successful *twilio* integrations. 

        :return: The name of this Integration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Integration.
        Name on the account. Returned on successful *twilio* integrations. 

        :param name: The name of this Integration.
        :type: str
        """

        self._name = name

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
    def uri(self):
        """
        Gets the uri of this Integration.
        The viber URI to find the account. Returned on successful *viber* integrations. 

        :return: The uri of this Integration.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Integration.
        The viber URI to find the account. Returned on successful *viber* integrations. 

        :param uri: The uri of this Integration.
        :type: str
        """

        self._uri = uri

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
    def bot_name(self):
        """
        Gets the bot_name of this Integration.
        The bot's name. Returned on successful *line* integrations. 

        :return: The bot_name of this Integration.
        :rtype: str
        """
        return self._bot_name

    @bot_name.setter
    def bot_name(self, bot_name):
        """
        Sets the bot_name of this Integration.
        The bot's name. Returned on successful *line* integrations. 

        :param bot_name: The bot_name of this Integration.
        :type: str
        """

        self._bot_name = bot_name

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
    def production(self):
        """
        Gets the production of this Integration.
        Flag specifying whether the certificate is production. Returned on successful *apn* integrations. 

        :return: The production of this Integration.
        :rtype: bool
        """
        return self._production

    @production.setter
    def production(self, production):
        """
        Sets the production of this Integration.
        Flag specifying whether the certificate is production. Returned on successful *apn* integrations. 

        :param production: The production of this Integration.
        :type: bool
        """

        self._production = production

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

    @property
    def consumer_key(self):
        """
        Gets the consumer_key of this Integration.
        The consumer key for your Twitter app. Required for *twitter* integrations. 

        :return: The consumer_key of this Integration.
        :rtype: str
        """
        return self._consumer_key

    @consumer_key.setter
    def consumer_key(self, consumer_key):
        """
        Sets the consumer_key of this Integration.
        The consumer key for your Twitter app. Required for *twitter* integrations. 

        :param consumer_key: The consumer_key of this Integration.
        :type: str
        """

        self._consumer_key = consumer_key

    @property
    def consumer_secret(self):
        """
        Gets the consumer_secret of this Integration.
        The consumer secret for your Twitter app. Required for *twitter* integrations. 

        :return: The consumer_secret of this Integration.
        :rtype: str
        """
        return self._consumer_secret

    @consumer_secret.setter
    def consumer_secret(self, consumer_secret):
        """
        Sets the consumer_secret of this Integration.
        The consumer secret for your Twitter app. Required for *twitter* integrations. 

        :param consumer_secret: The consumer_secret of this Integration.
        :type: str
        """

        self._consumer_secret = consumer_secret

    @property
    def access_token_key(self):
        """
        Gets the access_token_key of this Integration.
        The access token key obtained from your user via oauth. Required for *twitter* integrations. 

        :return: The access_token_key of this Integration.
        :rtype: str
        """
        return self._access_token_key

    @access_token_key.setter
    def access_token_key(self, access_token_key):
        """
        Sets the access_token_key of this Integration.
        The access token key obtained from your user via oauth. Required for *twitter* integrations. 

        :param access_token_key: The access_token_key of this Integration.
        :type: str
        """

        self._access_token_key = access_token_key

    @property
    def access_token_secret(self):
        """
        Gets the access_token_secret of this Integration.
        The access token secret obtained from your user via oauth. Required for *twitter* integrations. 

        :return: The access_token_secret of this Integration.
        :rtype: str
        """
        return self._access_token_secret

    @access_token_secret.setter
    def access_token_secret(self, access_token_secret):
        """
        Sets the access_token_secret of this Integration.
        The access token secret obtained from your user via oauth. Required for *twitter* integrations. 

        :param access_token_secret: The access_token_secret of this Integration.
        :type: str
        """

        self._access_token_secret = access_token_secret

    @property
    def user_id(self):
        """
        Gets the user_id of this Integration.
        The twitter userId. Returned on successful *twitter* integrations. 

        :return: The user_id of this Integration.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Integration.
        The twitter userId. Returned on successful *twitter* integrations. 

        :param user_id: The user_id of this Integration.
        :type: str
        """

        self._user_id = user_id

    @property
    def username(self):
        """
        Gets the username of this Integration.
        The username for the account. Returned on successful *twitter* and *telegram* integrations. 

        :return: The username of this Integration.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this Integration.
        The username for the account. Returned on successful *twitter* and *telegram* integrations. 

        :param username: The username of this Integration.
        :type: str
        """

        self._username = username

    @property
    def api_key(self):
        """
        Gets the api_key of this Integration.
        The public API key of your Mailgun account. Required for *mailgun* integrations. 

        :return: The api_key of this Integration.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """
        Sets the api_key of this Integration.
        The public API key of your Mailgun account. Required for *mailgun* integrations. 

        :param api_key: The api_key of this Integration.
        :type: str
        """

        self._api_key = api_key

    @property
    def domain(self):
        """
        Gets the domain of this Integration.
        The domain used to relay email. Required for *mailgun* integrations. 

        :return: The domain of this Integration.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this Integration.
        The domain used to relay email. Required for *mailgun* integrations. 

        :param domain: The domain of this Integration.
        :type: str
        """

        self._domain = domain

    @property
    def incoming_address(self):
        """
        Gets the incoming_address of this Integration.
        Smooch will receive all emails sent to this address. Required for *mailgun* integrations. 

        :return: The incoming_address of this Integration.
        :rtype: str
        """
        return self._incoming_address

    @incoming_address.setter
    def incoming_address(self, incoming_address):
        """
        Sets the incoming_address of this Integration.
        Smooch will receive all emails sent to this address. Required for *mailgun* integrations. 

        :param incoming_address: The incoming_address of this Integration.
        :type: str
        """

        self._incoming_address = incoming_address

    @property
    def access_key(self):
        """
        Gets the access_key of this Integration.
        The public API key of your MessageBird account. Required for *messagebird* integrations. 

        :return: The access_key of this Integration.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """
        Sets the access_key of this Integration.
        The public API key of your MessageBird account. Required for *messagebird* integrations. 

        :param access_key: The access_key of this Integration.
        :type: str
        """

        self._access_key = access_key

    @property
    def originator(self):
        """
        Gets the originator of this Integration.
        Smooch will receive all messages sent to this phone number. Required for *messagebird* integrations. 

        :return: The originator of this Integration.
        :rtype: str
        """
        return self._originator

    @originator.setter
    def originator(self, originator):
        """
        Sets the originator of this Integration.
        Smooch will receive all messages sent to this phone number. Required for *messagebird* integrations. 

        :param originator: The originator of this Integration.
        :type: str
        """

        self._originator = originator

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
