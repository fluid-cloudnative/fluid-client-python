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
from fluid.models.thin_comp_template_spec import ThinCompTemplateSpec  # noqa: E501
from fluid.rest import ApiException

class TestThinCompTemplateSpec(unittest.TestCase):
    """ThinCompTemplateSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ThinCompTemplateSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fluid.models.thin_comp_template_spec.ThinCompTemplateSpec()  # noqa: E501
        if include_optional :
            return ThinCompTemplateSpec(
                enabled = True, 
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
                ports = [
                    None
                    ], 
                readiness_probe = None, 
                replicas = 56, 
                resources = None, 
                volume_mounts = [
                    None
                    ]
            )
        else :
            return ThinCompTemplateSpec(
        )

    def testThinCompTemplateSpec(self):
        """Test ThinCompTemplateSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
