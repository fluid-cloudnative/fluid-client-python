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
from fluid.models.operation_status import OperationStatus  # noqa: E501
from fluid.rest import ApiException

class TestOperationStatus(unittest.TestCase):
    """OperationStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OperationStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fluid.models.operation_status.OperationStatus()  # noqa: E501
        if include_optional :
            return OperationStatus(
                conditions = [
                    fluid.models./condition..Condition(
                        last_probe_time = None, 
                        last_transition_time = None, 
                        message = '0', 
                        reason = '0', 
                        status = '0', 
                        type = '0', )
                    ], 
                duration = '0', 
                infos = {
                    'key' : '0'
                    }, 
                last_schedule_time = None, 
                last_successful_time = None, 
                phase = '0', 
                waiting_for = fluid.models./waiting_status..WaitingStatus(
                    operation_complete = True, )
            )
        else :
            return OperationStatus(
                conditions = [
                    fluid.models./condition..Condition(
                        last_probe_time = None, 
                        last_transition_time = None, 
                        message = '0', 
                        reason = '0', 
                        status = '0', 
                        type = '0', )
                    ],
                duration = '0',
                phase = '0',
        )

    def testOperationStatus(self):
        """Test OperationStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
