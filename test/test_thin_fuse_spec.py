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
from fluid.models.thin_fuse_spec import ThinFuseSpec  # noqa: E501
from fluid.rest import ApiException

class TestThinFuseSpec(unittest.TestCase):
    """ThinFuseSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ThinFuseSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fluid.models.thin_fuse_spec.ThinFuseSpec()  # noqa: E501
        if include_optional :
            return ThinFuseSpec(
                args = [
                    '0'
                    ], 
                clean_policy = '0', 
                command = [
                    '0'
                    ], 
                env = [
                    None
                    ], 
                image = '0', 
                image_pull_policy = '0', 
                image_tag = '0', 
                liveness_probe = None, 
                network_mode = '0', 
                node_selector = {
                    'key' : '0'
                    }, 
                options = {
                    'key' : '0'
                    }, 
                ports = [
                    None
                    ], 
                readiness_probe = None, 
                resources = None, 
                volume_mounts = [
                    None
                    ]
            )
        else :
            return ThinFuseSpec(
        )

    def testThinFuseSpec(self):
        """Test ThinFuseSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
