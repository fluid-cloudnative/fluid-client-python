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


class ExternalStorage(object):
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
        'encrypt_options': 'list[EncryptOption]',
        'uri': 'str'
    }

    attribute_map = {
        'encrypt_options': 'encryptOptions',
        'uri': 'uri'
    }

    def __init__(self, encrypt_options=None, uri='', local_vars_configuration=None):  # noqa: E501
        """ExternalStorage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._encrypt_options = None
        self._uri = None
        self.discriminator = None

        if encrypt_options is not None:
            self.encrypt_options = encrypt_options
        self.uri = uri

    @property
    def encrypt_options(self):
        """Gets the encrypt_options of this ExternalStorage.  # noqa: E501

        encrypt info for external storage  # noqa: E501

        :return: The encrypt_options of this ExternalStorage.  # noqa: E501
        :rtype: list[EncryptOption]
        """
        return self._encrypt_options

    @encrypt_options.setter
    def encrypt_options(self, encrypt_options):
        """Sets the encrypt_options of this ExternalStorage.

        encrypt info for external storage  # noqa: E501

        :param encrypt_options: The encrypt_options of this ExternalStorage.  # noqa: E501
        :type: list[EncryptOption]
        """

        self._encrypt_options = encrypt_options

    @property
    def uri(self):
        """Gets the uri of this ExternalStorage.  # noqa: E501

        type of external storage, including s3, oss, gcs, ceph, nfs, pvc, etc. (related to runtime)  # noqa: E501

        :return: The uri of this ExternalStorage.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ExternalStorage.

        type of external storage, including s3, oss, gcs, ceph, nfs, pvc, etc. (related to runtime)  # noqa: E501

        :param uri: The uri of this ExternalStorage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uri is None:  # noqa: E501
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

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
        if not isinstance(other, ExternalStorage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalStorage):
            return True

        return self.to_dict() != other.to_dict()
