# coding: utf-8

"""
    fluid

    client for fluid  # noqa: E501

    The version of the OpenAPI document: v0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from fluid.configuration import Configuration


class DatasetToMigrate(object):
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
        'name': 'str',
        'namespace': 'str',
        'path': 'str'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'path': 'path'
    }

    def __init__(self, name='', namespace='', path=None, local_vars_configuration=None):  # noqa: E501
        """DatasetToMigrate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._namespace = None
        self._path = None
        self.discriminator = None

        self.name = name
        self.namespace = namespace
        if path is not None:
            self.path = path

    @property
    def name(self):
        """Gets the name of this DatasetToMigrate.  # noqa: E501

        name of dataset  # noqa: E501

        :return: The name of this DatasetToMigrate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatasetToMigrate.

        name of dataset  # noqa: E501

        :param name: The name of this DatasetToMigrate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this DatasetToMigrate.  # noqa: E501

        namespace of dataset  # noqa: E501

        :return: The namespace of this DatasetToMigrate.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this DatasetToMigrate.

        namespace of dataset  # noqa: E501

        :param namespace: The namespace of this DatasetToMigrate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and namespace is None:  # noqa: E501
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501

        self._namespace = namespace

    @property
    def path(self):
        """Gets the path of this DatasetToMigrate.  # noqa: E501

        path to migrate  # noqa: E501

        :return: The path of this DatasetToMigrate.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DatasetToMigrate.

        path to migrate  # noqa: E501

        :param path: The path of this DatasetToMigrate.  # noqa: E501
        :type: str
        """

        self._path = path

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
        if not isinstance(other, DatasetToMigrate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatasetToMigrate):
            return True

        return self.to_dict() != other.to_dict()