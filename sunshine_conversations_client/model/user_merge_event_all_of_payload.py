# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.4.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


from sunshine_conversations_client.configuration import Configuration
from sunshine_conversations_client.undefined import Undefined


class UserMergeEventAllOfPayload(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'merged_users': 'UserMergeEventAllOfPayloadMergedUsers',
        'merged_conversations': 'UserMergeEventAllOfPayloadMergedConversations',
        'discarded_metadata': 'object'
    }

    attribute_map = {
        'merged_users': 'mergedUsers',
        'merged_conversations': 'mergedConversations',
        'discarded_metadata': 'discardedMetadata'
    }

    nulls = set()

    def __init__(self, merged_users=None, merged_conversations=Undefined(), discarded_metadata=Undefined(), local_vars_configuration=None):  # noqa: E501
        """UserMergeEventAllOfPayload - a model defined in OpenAPI"""  # noqa: E501
        
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._merged_users = None
        self._merged_conversations = None
        self._discarded_metadata = None
        self.discriminator = None

        if merged_users is not None:
            self.merged_users = merged_users
        self.merged_conversations = merged_conversations
        self.discarded_metadata = discarded_metadata

    @property
    def merged_users(self):
        """Gets the merged_users of this UserMergeEventAllOfPayload.  # noqa: E501


        :return: The merged_users of this UserMergeEventAllOfPayload.  # noqa: E501
        :rtype: UserMergeEventAllOfPayloadMergedUsers
        """
        return self._merged_users

    @merged_users.setter
    def merged_users(self, merged_users):
        """Sets the merged_users of this UserMergeEventAllOfPayload.


        :param merged_users: The merged_users of this UserMergeEventAllOfPayload.  # noqa: E501
        :type: UserMergeEventAllOfPayloadMergedUsers
        """

        self._merged_users = merged_users

    @property
    def merged_conversations(self):
        """Gets the merged_conversations of this UserMergeEventAllOfPayload.  # noqa: E501


        :return: The merged_conversations of this UserMergeEventAllOfPayload.  # noqa: E501
        :rtype: UserMergeEventAllOfPayloadMergedConversations
        """
        return self._merged_conversations

    @merged_conversations.setter
    def merged_conversations(self, merged_conversations):
        """Sets the merged_conversations of this UserMergeEventAllOfPayload.


        :param merged_conversations: The merged_conversations of this UserMergeEventAllOfPayload.  # noqa: E501
        :type: UserMergeEventAllOfPayloadMergedConversations
        """
        if type(merged_conversations) is Undefined:
            merged_conversations = None
            self.nulls.discard("merged_conversations")
        elif merged_conversations is None:
            self.nulls.add("merged_conversations")
        else:
            self.nulls.discard("merged_conversations")

        self._merged_conversations = merged_conversations

    @property
    def discarded_metadata(self):
        """Gets the discarded_metadata of this UserMergeEventAllOfPayload.  # noqa: E501

        A flat object with the set of metadata properties that were discarded when merging the two users. This should contain values only if the combined metadata fields exceed the 4KB limit.  # noqa: E501

        :return: The discarded_metadata of this UserMergeEventAllOfPayload.  # noqa: E501
        :rtype: object
        """
        return self._discarded_metadata

    @discarded_metadata.setter
    def discarded_metadata(self, discarded_metadata):
        """Sets the discarded_metadata of this UserMergeEventAllOfPayload.

        A flat object with the set of metadata properties that were discarded when merging the two users. This should contain values only if the combined metadata fields exceed the 4KB limit.  # noqa: E501

        :param discarded_metadata: The discarded_metadata of this UserMergeEventAllOfPayload.  # noqa: E501
        :type: object
        """
        if type(discarded_metadata) is Undefined:
            discarded_metadata = None
            self.nulls.discard("discarded_metadata")
        elif discarded_metadata is None:
            self.nulls.add("discarded_metadata")
        else:
            self.nulls.discard("discarded_metadata")

        self._discarded_metadata = discarded_metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserMergeEventAllOfPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserMergeEventAllOfPayload):
            return True

        return self.to_dict() != other.to_dict()
