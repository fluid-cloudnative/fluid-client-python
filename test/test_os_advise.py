# coding: utf-8

"""
    fluid

    client for fluid  # noqa: E501

    The version of the OpenAPI document: v0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import fluid
from fluid.models.os_advise import OSAdvise  # noqa: E501
from fluid.rest import ApiException

class TestOSAdvise(unittest.TestCase):
    """OSAdvise unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OSAdvise
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fluid.models.os_advise.OSAdvise()  # noqa: E501
        if include_optional :
            return OSAdvise(
                enabled = True, 
                os_version = '0'
            )
        else :
            return OSAdvise(
        )

    def testOSAdvise(self):
        """Test OSAdvise"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
