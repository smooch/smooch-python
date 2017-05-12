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


class MessagePost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, role=None, type=None, name=None, email=None, avatar_url=None, metadata=None, payload=None, text=None, media_url=None, media_type=None, items=None, actions=None, destination=None):
        """
        MessagePost - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'role': 'str',
            'type': 'str',
            'name': 'str',
            'email': 'str',
            'avatar_url': 'str',
            'metadata': 'object',
            'payload': 'str',
            'text': 'str',
            'media_url': 'str',
            'media_type': 'str',
            'items': 'list[MessageItem]',
            'actions': 'list[Action]',
            'destination': 'Destination'
        }

        self.attribute_map = {
            'role': 'role',
            'type': 'type',
            'name': 'name',
            'email': 'email',
            'avatar_url': 'avatarUrl',
            'metadata': 'metadata',
            'payload': 'payload',
            'text': 'text',
            'media_url': 'mediaUrl',
            'media_type': 'mediaType',
            'items': 'items',
            'actions': 'actions',
            'destination': 'destination'
        }

        self._role = None
        self._type = None
        self._name = None
        self._email = None
        self._avatar_url = None
        self._metadata = None
        self._payload = None
        self._text = None
        self._media_url = None
        self._media_type = None
        self._items = None
        self._actions = None
        self._destination = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if role is not None:
          self.role = role
        if type is not None:
          self.type = type
        if name is not None:
          self.name = name
        if email is not None:
          self.email = email
        if avatar_url is not None:
          self.avatar_url = avatar_url
        if metadata is not None:
          self.metadata = metadata
        if payload is not None:
          self.payload = payload
        if text is not None:
          self.text = text
        if media_url is not None:
          self.media_url = media_url
        if media_type is not None:
          self.media_type = media_type
        if items is not None:
          self.items = items
        if actions is not None:
          self.actions = actions
        if destination is not None:
          self.destination = destination

    @property
    def role(self):
        """
        Gets the role of this MessagePost.
        The role of the individual posting the message. Can be either *appUser* or *appMaker*.

        :return: The role of this MessagePost.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this MessagePost.
        The role of the individual posting the message. Can be either *appUser* or *appMaker*.

        :param role: The role of this MessagePost.
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")

        self._role = role

    @property
    def type(self):
        """
        Gets the type of this MessagePost.
        The message type.

        :return: The type of this MessagePost.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MessagePost.
        The message type.

        :param type: The type of this MessagePost.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["text", "image", "carousel", "list"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """
        Gets the name of this MessagePost.
        The display name of the message author.

        :return: The name of this MessagePost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MessagePost.
        The display name of the message author.

        :param name: The name of this MessagePost.
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """
        Gets the email of this MessagePost.
        The email address of the message author.

        :return: The email of this MessagePost.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this MessagePost.
        The email address of the message author.

        :param email: The email of this MessagePost.
        :type: str
        """

        self._email = email

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this MessagePost.
        The URL of the desired message avatar image.

        :return: The avatar_url of this MessagePost.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this MessagePost.
        The URL of the desired message avatar image.

        :param avatar_url: The avatar_url of this MessagePost.
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def metadata(self):
        """
        Gets the metadata of this MessagePost.
        Flat JSON object containing any custom properties associated with the message.

        :return: The metadata of this MessagePost.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this MessagePost.
        Flat JSON object containing any custom properties associated with the message.

        :param metadata: The metadata of this MessagePost.
        :type: object
        """

        self._metadata = metadata

    @property
    def payload(self):
        """
        Gets the payload of this MessagePost.
        The payload of a reply action, if applicable.

        :return: The payload of this MessagePost.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this MessagePost.
        The payload of a reply action, if applicable.

        :param payload: The payload of this MessagePost.
        :type: str
        """

        self._payload = payload

    @property
    def text(self):
        """
        Gets the text of this MessagePost.
        The message text. Required for text messages. 

        :return: The text of this MessagePost.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this MessagePost.
        The message text. Required for text messages. 

        :param text: The text of this MessagePost.
        :type: str
        """

        self._text = text

    @property
    def media_url(self):
        """
        Gets the media_url of this MessagePost.
        The mediaUrl for the image. Required for image messages. 

        :return: The media_url of this MessagePost.
        :rtype: str
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url):
        """
        Sets the media_url of this MessagePost.
        The mediaUrl for the image. Required for image messages. 

        :param media_url: The media_url of this MessagePost.
        :type: str
        """

        self._media_url = media_url

    @property
    def media_type(self):
        """
        Gets the media_type of this MessagePost.
        The mediaType for the image. Required for image messages. 

        :return: The media_type of this MessagePost.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this MessagePost.
        The mediaType for the image. Required for image messages. 

        :param media_type: The media_type of this MessagePost.
        :type: str
        """

        self._media_type = media_type

    @property
    def items(self):
        """
        Gets the items of this MessagePost.
        The items in the message list. Required for carousel and list messages. 

        :return: The items of this MessagePost.
        :rtype: list[MessageItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this MessagePost.
        The items in the message list. Required for carousel and list messages. 

        :param items: The items of this MessagePost.
        :type: list[MessageItem]
        """

        self._items = items

    @property
    def actions(self):
        """
        Gets the actions of this MessagePost.
        The actions in the message.

        :return: The actions of this MessagePost.
        :rtype: list[Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this MessagePost.
        The actions in the message.

        :param actions: The actions of this MessagePost.
        :type: list[Action]
        """

        self._actions = actions

    @property
    def destination(self):
        """
        Gets the destination of this MessagePost.
        Specifies which channel to deliver a message to. See [list integrations](https://docs.smooch.io/rest/#list-integrations) to get integration ID and type.

        :return: The destination of this MessagePost.
        :rtype: Destination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this MessagePost.
        Specifies which channel to deliver a message to. See [list integrations](https://docs.smooch.io/rest/#list-integrations) to get integration ID and type.

        :param destination: The destination of this MessagePost.
        :type: Destination
        """

        self._destination = destination

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
        if not isinstance(other, MessagePost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
