# coding: utf-8

"""
    fluid

    client for fluid  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from Fluid.io.fluid-cloudnative.module.secret_key_selector import SecretKeySelector  # noqa: F401,E501


class EncryptOptionSource(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'secret_key_ref': 'SecretKeySelector'
    }

    attribute_map = {
        'secret_key_ref': 'secretKeyRef'
    }

    def __init__(self, secret_key_ref=None):  # noqa: E501
        """EncryptOptionSource - a model defined in Swagger"""  # noqa: E501

        self._secret_key_ref = None
        self.discriminator = None

        if secret_key_ref is not None:
            self.secret_key_ref = secret_key_ref

    @property
    def secret_key_ref(self):
        """Gets the secret_key_ref of this EncryptOptionSource.  # noqa: E501

        The encryptInfo obtained from secret  # noqa: E501

        :return: The secret_key_ref of this EncryptOptionSource.  # noqa: E501
        :rtype: SecretKeySelector
        """
        return self._secret_key_ref

    @secret_key_ref.setter
    def secret_key_ref(self, secret_key_ref):
        """Sets the secret_key_ref of this EncryptOptionSource.

        The encryptInfo obtained from secret  # noqa: E501

        :param secret_key_ref: The secret_key_ref of this EncryptOptionSource.  # noqa: E501
        :type: SecretKeySelector
        """

        self._secret_key_ref = secret_key_ref

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(EncryptOptionSource, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EncryptOptionSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
