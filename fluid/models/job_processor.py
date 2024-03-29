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


class JobProcessor(object):
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
        'pod_spec': 'V1PodSpec'
    }

    attribute_map = {
        'pod_spec': 'podSpec'
    }

    def __init__(self, pod_spec=None, local_vars_configuration=None):  # noqa: E501
        """JobProcessor - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pod_spec = None
        self.discriminator = None

        if pod_spec is not None:
            self.pod_spec = pod_spec

    @property
    def pod_spec(self):
        """Gets the pod_spec of this JobProcessor.  # noqa: E501


        :return: The pod_spec of this JobProcessor.  # noqa: E501
        :rtype: V1PodSpec
        """
        return self._pod_spec

    @pod_spec.setter
    def pod_spec(self, pod_spec):
        """Sets the pod_spec of this JobProcessor.


        :param pod_spec: The pod_spec of this JobProcessor.  # noqa: E501
        :type: V1PodSpec
        """

        self._pod_spec = pod_spec

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
        if not isinstance(other, JobProcessor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobProcessor):
            return True

        return self.to_dict() != other.to_dict()
