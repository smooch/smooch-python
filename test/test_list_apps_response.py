# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import smooch
from smooch.rest import ApiException
from smooch.models.list_apps_response import ListAppsResponse


class TestListAppsResponse(unittest.TestCase):
    """ ListAppsResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListAppsResponse(self):
        """
        Test ListAppsResponse
        """
        model = smooch.models.list_apps_response.ListAppsResponse()


if __name__ == '__main__':
    unittest.main()