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


class TargetDatasetWithMountPath(object):
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
        'mount_path': 'str',
        'name': 'str',
        'namespace': 'str',
        'sub_path': 'str'
    }

    attribute_map = {
        'mount_path': 'mountPath',
        'name': 'name',
        'namespace': 'namespace',
        'sub_path': 'subPath'
    }

    def __init__(self, mount_path='', name='', namespace=None, sub_path=None, local_vars_configuration=None):  # noqa: E501
        """TargetDatasetWithMountPath - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mount_path = None
        self._name = None
        self._namespace = None
        self._sub_path = None
        self.discriminator = None

        self.mount_path = mount_path
        self.name = name
        if namespace is not None:
            self.namespace = namespace
        if sub_path is not None:
            self.sub_path = sub_path

    @property
    def mount_path(self):
        """Gets the mount_path of this TargetDatasetWithMountPath.  # noqa: E501

        MountPath defines where the Dataset should be mounted in DataProcess's containers.  # noqa: E501

        :return: The mount_path of this TargetDatasetWithMountPath.  # noqa: E501
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        """Sets the mount_path of this TargetDatasetWithMountPath.

        MountPath defines where the Dataset should be mounted in DataProcess's containers.  # noqa: E501

        :param mount_path: The mount_path of this TargetDatasetWithMountPath.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mount_path is None:  # noqa: E501
            raise ValueError("Invalid value for `mount_path`, must not be `None`")  # noqa: E501

        self._mount_path = mount_path

    @property
    def name(self):
        """Gets the name of this TargetDatasetWithMountPath.  # noqa: E501

        Name defines name of the target dataset  # noqa: E501

        :return: The name of this TargetDatasetWithMountPath.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TargetDatasetWithMountPath.

        Name defines name of the target dataset  # noqa: E501

        :param name: The name of this TargetDatasetWithMountPath.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this TargetDatasetWithMountPath.  # noqa: E501

        Namespace defines namespace of the target dataset  # noqa: E501

        :return: The namespace of this TargetDatasetWithMountPath.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this TargetDatasetWithMountPath.

        Namespace defines namespace of the target dataset  # noqa: E501

        :param namespace: The namespace of this TargetDatasetWithMountPath.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def sub_path(self):
        """Gets the sub_path of this TargetDatasetWithMountPath.  # noqa: E501

        SubPath defines subpath of the target dataset to mount.  # noqa: E501

        :return: The sub_path of this TargetDatasetWithMountPath.  # noqa: E501
        :rtype: str
        """
        return self._sub_path

    @sub_path.setter
    def sub_path(self, sub_path):
        """Sets the sub_path of this TargetDatasetWithMountPath.

        SubPath defines subpath of the target dataset to mount.  # noqa: E501

        :param sub_path: The sub_path of this TargetDatasetWithMountPath.  # noqa: E501
        :type: str
        """

        self._sub_path = sub_path

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
        if not isinstance(other, TargetDatasetWithMountPath):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetDatasetWithMountPath):
            return True

        return self.to_dict() != other.to_dict()
