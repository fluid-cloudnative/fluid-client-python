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


class Mount(object):
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
        'mount_point': 'str',
        'name': 'str',
        'options': 'dict(str, str)',
        'path': 'str',
        'read_only': 'bool',
        'shared': 'bool'
    }

    attribute_map = {
        'encrypt_options': 'encryptOptions',
        'mount_point': 'mountPoint',
        'name': 'name',
        'options': 'options',
        'path': 'path',
        'read_only': 'readOnly',
        'shared': 'shared'
    }

    def __init__(self, encrypt_options=None, mount_point='', name=None, options=None, path=None, read_only=None, shared=None, local_vars_configuration=None):  # noqa: E501
        """Mount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._encrypt_options = None
        self._mount_point = None
        self._name = None
        self._options = None
        self._path = None
        self._read_only = None
        self._shared = None
        self.discriminator = None

        if encrypt_options is not None:
            self.encrypt_options = encrypt_options
        self.mount_point = mount_point
        if name is not None:
            self.name = name
        if options is not None:
            self.options = options
        if path is not None:
            self.path = path
        if read_only is not None:
            self.read_only = read_only
        if shared is not None:
            self.shared = shared

    @property
    def encrypt_options(self):
        """Gets the encrypt_options of this Mount.  # noqa: E501

        The secret information  # noqa: E501

        :return: The encrypt_options of this Mount.  # noqa: E501
        :rtype: list[EncryptOption]
        """
        return self._encrypt_options

    @encrypt_options.setter
    def encrypt_options(self, encrypt_options):
        """Sets the encrypt_options of this Mount.

        The secret information  # noqa: E501

        :param encrypt_options: The encrypt_options of this Mount.  # noqa: E501
        :type: list[EncryptOption]
        """

        self._encrypt_options = encrypt_options

    @property
    def mount_point(self):
        """Gets the mount_point of this Mount.  # noqa: E501

        MountPoint is the mount point of source.  # noqa: E501

        :return: The mount_point of this Mount.  # noqa: E501
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        """Sets the mount_point of this Mount.

        MountPoint is the mount point of source.  # noqa: E501

        :param mount_point: The mount_point of this Mount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mount_point is None:  # noqa: E501
            raise ValueError("Invalid value for `mount_point`, must not be `None`")  # noqa: E501

        self._mount_point = mount_point

    @property
    def name(self):
        """Gets the name of this Mount.  # noqa: E501

        The name of mount  # noqa: E501

        :return: The name of this Mount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Mount.

        The name of mount  # noqa: E501

        :param name: The name of this Mount.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def options(self):
        """Gets the options of this Mount.  # noqa: E501

        The Mount Options. <br> Refer to <a href=\"https://docs.alluxio.io/os/user/stable/en/reference/Properties-List.html\">Mount Options</a>.  <br> The option has Prefix 'fs.' And you can Learn more from <a href=\"https://docs.alluxio.io/os/user/stable/en/ufs/S3.html\">The Storage Integrations</a>  # noqa: E501

        :return: The options of this Mount.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Mount.

        The Mount Options. <br> Refer to <a href=\"https://docs.alluxio.io/os/user/stable/en/reference/Properties-List.html\">Mount Options</a>.  <br> The option has Prefix 'fs.' And you can Learn more from <a href=\"https://docs.alluxio.io/os/user/stable/en/ufs/S3.html\">The Storage Integrations</a>  # noqa: E501

        :param options: The options of this Mount.  # noqa: E501
        :type: dict(str, str)
        """

        self._options = options

    @property
    def path(self):
        """Gets the path of this Mount.  # noqa: E501

        The path of mount, if not set will be /{Name}  # noqa: E501

        :return: The path of this Mount.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Mount.

        The path of mount, if not set will be /{Name}  # noqa: E501

        :param path: The path of this Mount.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def read_only(self):
        """Gets the read_only of this Mount.  # noqa: E501

        Optional: Defaults to false (read-write).  # noqa: E501

        :return: The read_only of this Mount.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this Mount.

        Optional: Defaults to false (read-write).  # noqa: E501

        :param read_only: The read_only of this Mount.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def shared(self):
        """Gets the shared of this Mount.  # noqa: E501

        Optional: Defaults to false (shared).  # noqa: E501

        :return: The shared of this Mount.  # noqa: E501
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this Mount.

        Optional: Defaults to false (shared).  # noqa: E501

        :param shared: The shared of this Mount.  # noqa: E501
        :type: bool
        """

        self._shared = shared

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
        if not isinstance(other, Mount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Mount):
            return True

        return self.to_dict() != other.to_dict()
