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


class VersionSpec(object):
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
        'image': 'str',
        'image_pull_policy': 'str',
        'image_tag': 'str'
    }

    attribute_map = {
        'image': 'image',
        'image_pull_policy': 'imagePullPolicy',
        'image_tag': 'imageTag'
    }

    def __init__(self, image=None, image_pull_policy=None, image_tag=None, local_vars_configuration=None):  # noqa: E501
        """VersionSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._image = None
        self._image_pull_policy = None
        self._image_tag = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if image_tag is not None:
            self.image_tag = image_tag

    @property
    def image(self):
        """Gets the image of this VersionSpec.  # noqa: E501

        Image (e.g. alluxio/alluxio)  # noqa: E501

        :return: The image of this VersionSpec.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this VersionSpec.

        Image (e.g. alluxio/alluxio)  # noqa: E501

        :param image: The image of this VersionSpec.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this VersionSpec.  # noqa: E501

        One of the three policies: `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :return: The image_pull_policy of this VersionSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this VersionSpec.

        One of the three policies: `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :param image_pull_policy: The image_pull_policy of this VersionSpec.  # noqa: E501
        :type: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def image_tag(self):
        """Gets the image_tag of this VersionSpec.  # noqa: E501

        Image tag (e.g. 2.3.0-SNAPSHOT)  # noqa: E501

        :return: The image_tag of this VersionSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this VersionSpec.

        Image tag (e.g. 2.3.0-SNAPSHOT)  # noqa: E501

        :param image_tag: The image_tag of this VersionSpec.  # noqa: E501
        :type: str
        """

        self._image_tag = image_tag

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
        if not isinstance(other, VersionSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VersionSpec):
            return True

        return self.to_dict() != other.to_dict()
