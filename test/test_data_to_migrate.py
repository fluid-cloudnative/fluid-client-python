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
from fluid.models.data_to_migrate import DataToMigrate  # noqa: E501
from fluid.rest import ApiException

class TestDataToMigrate(unittest.TestCase):
    """DataToMigrate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DataToMigrate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fluid.models.data_to_migrate.DataToMigrate()  # noqa: E501
        if include_optional :
            return DataToMigrate(
                dataset = fluid.models./dataset_to_migrate..DatasetToMigrate(
                    name = '0', 
                    namespace = '0', 
                    path = '0', ), 
                external_storage = fluid.models./external_storage..ExternalStorage(
                    encrypt_options = [
                        fluid.models./encrypt_option..EncryptOption(
                            name = '0', 
                            value_from = fluid.models./encrypt_option_source..EncryptOptionSource(
                                secret_key_ref = fluid.models./secret_key_selector..SecretKeySelector(
                                    key = '0', 
                                    name = '0', ), ), )
                        ], 
                    uri = '0', )
            )
        else :
            return DataToMigrate(
        )

    def testDataToMigrate(self):
        """Test DataToMigrate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
