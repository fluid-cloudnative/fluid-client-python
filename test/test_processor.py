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
from fluid.models.processor import Processor  # noqa: E501
from fluid.rest import ApiException

class TestProcessor(unittest.TestCase):
    """Processor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Processor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fluid.models.processor.Processor()  # noqa: E501
        if include_optional :
            return Processor(
                job = fluid.models./job_processor..JobProcessor(
                    pod_spec = None, ), 
                pod_metadata = fluid.models./pod_metadata..PodMetadata(
                    annotations = {
                        'key' : '0'
                        }, 
                    labels = {
                        'key' : '0'
                        }, ), 
                script = fluid.models./script_processor..ScriptProcessor(
                    command = [
                        '0'
                        ], 
                    env = [
                        None
                        ], 
                    image = '0', 
                    image_pull_policy = '0', 
                    image_tag = '0', 
                    resources = None, 
                    restart_policy = '0', 
                    source = '0', 
                    volume_mounts = [
                        None
                        ], 
                    volumes = [
                        None
                        ], ), 
                service_account_name = '0'
            )
        else :
            return Processor(
        )

    def testProcessor(self):
        """Test Processor"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
