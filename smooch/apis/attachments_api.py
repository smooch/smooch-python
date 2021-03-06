# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.29
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AttachmentsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def remove_attachment(self, app_id, attachment_remove_body, **kwargs):
        """
        Remove an attachment uploaded to Smooch.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_attachment(app_id, attachment_remove_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param AttachmentRemove attachment_remove_body: Body for a removeAttachment request.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.remove_attachment_with_http_info(app_id, attachment_remove_body, **kwargs)
        else:
            (data) = self.remove_attachment_with_http_info(app_id, attachment_remove_body, **kwargs)
            return data

    def remove_attachment_with_http_info(self, app_id, attachment_remove_body, **kwargs):
        """
        Remove an attachment uploaded to Smooch.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_attachment_with_http_info(app_id, attachment_remove_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param AttachmentRemove attachment_remove_body: Body for a removeAttachment request.  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'attachment_remove_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_attachment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params) or (params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `remove_attachment`")
        # verify the required parameter 'attachment_remove_body' is set
        if ('attachment_remove_body' not in params) or (params['attachment_remove_body'] is None):
            raise ValueError("Missing the required parameter `attachment_remove_body` when calling `remove_attachment`")


        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'attachment_remove_body' in params:
            body_params = params['attachment_remove_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basicAuth', 'jwt']

        return self.api_client.call_api('/v1.1/apps/{appId}/attachments/remove', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def upload_attachment(self, app_id, source, access, **kwargs):
        """
        Upload an attachment to Smooch to use in future messages.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.upload_attachment(app_id, source, access, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param file source: File to be uploaded (required)
        :param str access: Access level for the resulting file (required)
        :param str _for: The intended container for the attachment
        :param str app_user_id: The appUserId of the user that will receive the attachment Used in attachments for messages 
        :param str user_id: The userId of the user that will receive the attachment Used in attachments for messages 
        :return: AttachmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.upload_attachment_with_http_info(app_id, source, access, **kwargs)
        else:
            (data) = self.upload_attachment_with_http_info(app_id, source, access, **kwargs)
            return data

    def upload_attachment_with_http_info(self, app_id, source, access, **kwargs):
        """
        Upload an attachment to Smooch to use in future messages.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.upload_attachment_with_http_info(app_id, source, access, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param file source: File to be uploaded (required)
        :param str access: Access level for the resulting file (required)
        :param str _for: The intended container for the attachment
        :param str app_user_id: The appUserId of the user that will receive the attachment Used in attachments for messages 
        :param str user_id: The userId of the user that will receive the attachment Used in attachments for messages 
        :return: AttachmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'source', 'access', '_for', 'app_user_id', 'user_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_attachment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params) or (params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `upload_attachment`")
        # verify the required parameter 'source' is set
        if ('source' not in params) or (params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `upload_attachment`")
        # verify the required parameter 'access' is set
        if ('access' not in params) or (params['access'] is None):
            raise ValueError("Missing the required parameter `access` when calling `upload_attachment`")


        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']

        query_params = []
        if 'access' in params:
            query_params.append(('access', params['access']))
        if '_for' in params:
            query_params.append(('for', params['_for']))
        if 'app_user_id' in params:
            query_params.append(('appUserId', params['app_user_id']))
        if 'user_id' in params:
            query_params.append(('userId', params['user_id']))

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'source' in params:
            local_var_files['source'] = params['source']

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = ['basicAuth', 'jwt']

        return self.api_client.call_api('/v1.1/apps/{appId}/attachments', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AttachmentResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
