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

from kubernetes.client import V1ResourceRequirements  # noqa: F401,E501


class AlluxioFuseSpec(object):
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
        'args': 'list[str]',
        'env': 'dict(str, str)',
        '_global': 'bool',
        'image': 'str',
        'image_pull_policy': 'str',
        'image_tag': 'str',
        'jvm_options': 'list[str]',
        'node_selector': 'dict(str, str)',
        'properties': 'dict(str, str)',
        'resources': 'V1ResourceRequirements'
    }

    attribute_map = {
        'args': 'args',
        'env': 'env',
        '_global': 'global',
        'image': 'image',
        'image_pull_policy': 'imagePullPolicy',
        'image_tag': 'imageTag',
        'jvm_options': 'jvmOptions',
        'node_selector': 'nodeSelector',
        'properties': 'properties',
        'resources': 'resources'
    }

    def __init__(self, args=None, env=None, _global=None, image=None, image_pull_policy=None, image_tag=None, jvm_options=None, node_selector=None, properties=None, resources=None):  # noqa: E501
        """AlluxioFuseSpec - a model defined in Swagger"""  # noqa: E501

        self._args = None
        self._env = None
        self.__global = None
        self._image = None
        self._image_pull_policy = None
        self._image_tag = None
        self._jvm_options = None
        self._node_selector = None
        self._properties = None
        self._resources = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if env is not None:
            self.env = env
        if _global is not None:
            self._global = _global
        if image is not None:
            self.image = image
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if image_tag is not None:
            self.image_tag = image_tag
        if jvm_options is not None:
            self.jvm_options = jvm_options
        if node_selector is not None:
            self.node_selector = node_selector
        if properties is not None:
            self.properties = properties
        if resources is not None:
            self.resources = resources

    @property
    def args(self):
        """Gets the args of this AlluxioFuseSpec.  # noqa: E501

        Arguments that will be passed to Alluxio Fuse  # noqa: E501

        :return: The args of this AlluxioFuseSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this AlluxioFuseSpec.

        Arguments that will be passed to Alluxio Fuse  # noqa: E501

        :param args: The args of this AlluxioFuseSpec.  # noqa: E501
        :type: list[str]
        """

        self._args = args

    @property
    def env(self):
        """Gets the env of this AlluxioFuseSpec.  # noqa: E501

        Environment variables that will be used by Alluxio Fuse  # noqa: E501

        :return: The env of this AlluxioFuseSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this AlluxioFuseSpec.

        Environment variables that will be used by Alluxio Fuse  # noqa: E501

        :param env: The env of this AlluxioFuseSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._env = env

    @property
    def _global(self):
        """Gets the _global of this AlluxioFuseSpec.  # noqa: E501

        If the fuse client should be deployed in global mode, otherwise the affinity should be considered  # noqa: E501

        :return: The _global of this AlluxioFuseSpec.  # noqa: E501
        :rtype: bool
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this AlluxioFuseSpec.

        If the fuse client should be deployed in global mode, otherwise the affinity should be considered  # noqa: E501

        :param _global: The _global of this AlluxioFuseSpec.  # noqa: E501
        :type: bool
        """

        self.__global = _global

    @property
    def image(self):
        """Gets the image of this AlluxioFuseSpec.  # noqa: E501

        Image for Alluxio Fuse(e.g. alluxio/alluxio-fuse)  # noqa: E501

        :return: The image of this AlluxioFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this AlluxioFuseSpec.

        Image for Alluxio Fuse(e.g. alluxio/alluxio-fuse)  # noqa: E501

        :param image: The image of this AlluxioFuseSpec.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this AlluxioFuseSpec.  # noqa: E501

        One of the three policies: `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :return: The image_pull_policy of this AlluxioFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this AlluxioFuseSpec.

        One of the three policies: `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :param image_pull_policy: The image_pull_policy of this AlluxioFuseSpec.  # noqa: E501
        :type: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def image_tag(self):
        """Gets the image_tag of this AlluxioFuseSpec.  # noqa: E501

        Image Tag for Alluxio Fuse(e.g. 2.3.0-SNAPSHOT)  # noqa: E501

        :return: The image_tag of this AlluxioFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this AlluxioFuseSpec.

        Image Tag for Alluxio Fuse(e.g. 2.3.0-SNAPSHOT)  # noqa: E501

        :param image_tag: The image_tag of this AlluxioFuseSpec.  # noqa: E501
        :type: str
        """

        self._image_tag = image_tag

    @property
    def jvm_options(self):
        """Gets the jvm_options of this AlluxioFuseSpec.  # noqa: E501

        Options for JVM  # noqa: E501

        :return: The jvm_options of this AlluxioFuseSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._jvm_options

    @jvm_options.setter
    def jvm_options(self, jvm_options):
        """Sets the jvm_options of this AlluxioFuseSpec.

        Options for JVM  # noqa: E501

        :param jvm_options: The jvm_options of this AlluxioFuseSpec.  # noqa: E501
        :type: list[str]
        """

        self._jvm_options = jvm_options

    @property
    def node_selector(self):
        """Gets the node_selector of this AlluxioFuseSpec.  # noqa: E501

        NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled  # noqa: E501

        :return: The node_selector of this AlluxioFuseSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this AlluxioFuseSpec.

        NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled  # noqa: E501

        :param node_selector: The node_selector of this AlluxioFuseSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def properties(self):
        """Gets the properties of this AlluxioFuseSpec.  # noqa: E501

        Configurable properties for Alluxio System. <br> Refer to <a href=\"https://docs.alluxio.io/os/user/stable/en/reference/Properties-List.html\">Alluxio Configuration Properties</a> for more info  # noqa: E501

        :return: The properties of this AlluxioFuseSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this AlluxioFuseSpec.

        Configurable properties for Alluxio System. <br> Refer to <a href=\"https://docs.alluxio.io/os/user/stable/en/reference/Properties-List.html\">Alluxio Configuration Properties</a> for more info  # noqa: E501

        :param properties: The properties of this AlluxioFuseSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def resources(self):
        """Gets the resources of this AlluxioFuseSpec.  # noqa: E501

        Resources that will be requested by Alluxio Fuse. <br> <br> Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod.  # noqa: E501

        :return: The resources of this AlluxioFuseSpec.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this AlluxioFuseSpec.

        Resources that will be requested by Alluxio Fuse. <br> <br> Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod.  # noqa: E501

        :param resources: The resources of this AlluxioFuseSpec.  # noqa: E501
        :type: V1ResourceRequirements
        """

        self._resources = resources

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
        if issubclass(AlluxioFuseSpec, dict):
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
        if not isinstance(other, AlluxioFuseSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
