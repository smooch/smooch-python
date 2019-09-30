# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.18
    
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


class TemplateApi(object):
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

    def create_template(self, app_id, template_create_body, **kwargs):
        """
        Create a template for the specified app.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_template(app_id, template_create_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param TemplateCreate template_create_body: Body for a createTemplate request.  (required)
        :return: TemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_template_with_http_info(app_id, template_create_body, **kwargs)
        else:
            (data) = self.create_template_with_http_info(app_id, template_create_body, **kwargs)
            return data

    def create_template_with_http_info(self, app_id, template_create_body, **kwargs):
        """
        Create a template for the specified app.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_template_with_http_info(app_id, template_create_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param TemplateCreate template_create_body: Body for a createTemplate request.  (required)
        :return: TemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'template_create_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params) or (params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `create_template`")
        # verify the required parameter 'template_create_body' is set
        if ('template_create_body' not in params) or (params['template_create_body'] is None):
            raise ValueError("Missing the required parameter `template_create_body` when calling `create_template`")


        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'template_create_body' in params:
            body_params = params['template_create_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basicAuth', 'jwt']

        return self.api_client.call_api('/v1.1/apps/{appId}/templates', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TemplateResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_template(self, app_id, template_id, **kwargs):
        """
        Delete the specified template.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_template(app_id, template_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param str template_id: Identifies the template. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_template_with_http_info(app_id, template_id, **kwargs)
        else:
            (data) = self.delete_template_with_http_info(app_id, template_id, **kwargs)
            return data

    def delete_template_with_http_info(self, app_id, template_id, **kwargs):
        """
        Delete the specified template.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_template_with_http_info(app_id, template_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param str template_id: Identifies the template. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'template_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params) or (params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `delete_template`")
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params) or (params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `delete_template`")


        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']
        if 'template_id' in params:
            path_params['templateId'] = params['template_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basicAuth', 'jwt']

        return self.api_client.call_api('/v1.1/apps/{appId}/templates/{templateId}', 'DELETE',
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

    def get_template(self, app_id, template_id, **kwargs):
        """
        Get the specified template.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_template(app_id, template_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param str template_id: Identifies the template. (required)
        :return: TemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_template_with_http_info(app_id, template_id, **kwargs)
        else:
            (data) = self.get_template_with_http_info(app_id, template_id, **kwargs)
            return data

    def get_template_with_http_info(self, app_id, template_id, **kwargs):
        """
        Get the specified template.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_template_with_http_info(app_id, template_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param str template_id: Identifies the template. (required)
        :return: TemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'template_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params) or (params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `get_template`")
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params) or (params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `get_template`")


        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']
        if 'template_id' in params:
            path_params['templateId'] = params['template_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basicAuth', 'jwt']

        return self.api_client.call_api('/v1.1/apps/{appId}/templates/{templateId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TemplateResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_templates(self, app_id, **kwargs):
        """
        List templates for the specified app.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_templates(app_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param int limit: The number of records to return.
        :param int offset: The number of initial records to skip before picking records to return.
        :return: ListTemplatesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_templates_with_http_info(app_id, **kwargs)
        else:
            (data) = self.list_templates_with_http_info(app_id, **kwargs)
            return data

    def list_templates_with_http_info(self, app_id, **kwargs):
        """
        List templates for the specified app.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_templates_with_http_info(app_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param int limit: The number of records to return.
        :param int offset: The number of initial records to skip before picking records to return.
        :return: ListTemplatesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'limit', 'offset']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_templates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params) or (params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `list_templates`")


        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basicAuth', 'jwt']

        return self.api_client.call_api('/v1.1/apps/{appId}/templates', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListTemplatesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_template(self, app_id, template_id, template_update_body, **kwargs):
        """
        Update the specified template.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_template(app_id, template_id, template_update_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param str template_id: Identifies the template. (required)
        :param TemplateUpdate template_update_body: Body for an updateTemplate request.  (required)
        :return: TemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_template_with_http_info(app_id, template_id, template_update_body, **kwargs)
        else:
            (data) = self.update_template_with_http_info(app_id, template_id, template_update_body, **kwargs)
            return data

    def update_template_with_http_info(self, app_id, template_id, template_update_body, **kwargs):
        """
        Update the specified template.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_template_with_http_info(app_id, template_id, template_update_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_id: Identifies the app. (required)
        :param str template_id: Identifies the template. (required)
        :param TemplateUpdate template_update_body: Body for an updateTemplate request.  (required)
        :return: TemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'template_id', 'template_update_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params) or (params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `update_template`")
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params) or (params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `update_template`")
        # verify the required parameter 'template_update_body' is set
        if ('template_update_body' not in params) or (params['template_update_body'] is None):
            raise ValueError("Missing the required parameter `template_update_body` when calling `update_template`")


        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']
        if 'template_id' in params:
            path_params['templateId'] = params['template_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'template_update_body' in params:
            body_params = params['template_update_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basicAuth', 'jwt']

        return self.api_client.call_api('/v1.1/apps/{appId}/templates/{templateId}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TemplateResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
