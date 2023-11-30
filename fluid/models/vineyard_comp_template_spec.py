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


class VineyardCompTemplateSpec(object):
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
        'env': 'dict(str, str)',
        'image': 'str',
        'image_pull_policy': 'str',
        'image_tag': 'str',
        'node_selector': 'dict(str, str)',
        'options': 'dict(str, str)',
        'ports': 'dict(str, int)',
        'replicas': 'int',
        'resources': 'V1ResourceRequirements',
        'volume_mounts': 'list[V1VolumeMount]'
    }

    attribute_map = {
        'env': 'env',
        'image': 'image',
        'image_pull_policy': 'imagePullPolicy',
        'image_tag': 'imageTag',
        'node_selector': 'nodeSelector',
        'options': 'options',
        'ports': 'ports',
        'replicas': 'replicas',
        'resources': 'resources',
        'volume_mounts': 'volumeMounts'
    }

    def __init__(self, env=None, image=None, image_pull_policy=None, image_tag=None, node_selector=None, options=None, ports=None, replicas=None, resources=None, volume_mounts=None, local_vars_configuration=None):  # noqa: E501
        """VineyardCompTemplateSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._env = None
        self._image = None
        self._image_pull_policy = None
        self._image_tag = None
        self._node_selector = None
        self._options = None
        self._ports = None
        self._replicas = None
        self._resources = None
        self._volume_mounts = None
        self.discriminator = None

        if env is not None:
            self.env = env
        if image is not None:
            self.image = image
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if image_tag is not None:
            self.image_tag = image_tag
        if node_selector is not None:
            self.node_selector = node_selector
        if options is not None:
            self.options = options
        if ports is not None:
            self.ports = ports
        if replicas is not None:
            self.replicas = replicas
        if resources is not None:
            self.resources = resources
        if volume_mounts is not None:
            self.volume_mounts = volume_mounts

    @property
    def env(self):
        """Gets the env of this VineyardCompTemplateSpec.  # noqa: E501

        Environment variables that will be used by Vineyard component. For Master, refer to <a href=\"https://etcd.io/docs/v3.5/op-guide/configuration/\">Etcd Configuration</a> for more info Default is not set.  # noqa: E501

        :return: The env of this VineyardCompTemplateSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this VineyardCompTemplateSpec.

        Environment variables that will be used by Vineyard component. For Master, refer to <a href=\"https://etcd.io/docs/v3.5/op-guide/configuration/\">Etcd Configuration</a> for more info Default is not set.  # noqa: E501

        :param env: The env of this VineyardCompTemplateSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._env = env

    @property
    def image(self):
        """Gets the image of this VineyardCompTemplateSpec.  # noqa: E501

        The image of Vineyard component. For Master, the default image is `bitnami/etcd` For Worker, the default image is `vineyardcloudnative/vineyardd` The default container registry is `docker.io`, you can change it by setting the image field  # noqa: E501

        :return: The image of this VineyardCompTemplateSpec.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this VineyardCompTemplateSpec.

        The image of Vineyard component. For Master, the default image is `bitnami/etcd` For Worker, the default image is `vineyardcloudnative/vineyardd` The default container registry is `docker.io`, you can change it by setting the image field  # noqa: E501

        :param image: The image of this VineyardCompTemplateSpec.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this VineyardCompTemplateSpec.  # noqa: E501

        The image pull policy of Vineyard component. Default is `IfNotPresent`.  # noqa: E501

        :return: The image_pull_policy of this VineyardCompTemplateSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this VineyardCompTemplateSpec.

        The image pull policy of Vineyard component. Default is `IfNotPresent`.  # noqa: E501

        :param image_pull_policy: The image_pull_policy of this VineyardCompTemplateSpec.  # noqa: E501
        :type: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def image_tag(self):
        """Gets the image_tag of this VineyardCompTemplateSpec.  # noqa: E501

        The image tag of Vineyard component. For Master, the default image tag is `3.5.10`. For Worker, the default image tag is `latest`.  # noqa: E501

        :return: The image_tag of this VineyardCompTemplateSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this VineyardCompTemplateSpec.

        The image tag of Vineyard component. For Master, the default image tag is `3.5.10`. For Worker, the default image tag is `latest`.  # noqa: E501

        :param image_tag: The image_tag of this VineyardCompTemplateSpec.  # noqa: E501
        :type: str
        """

        self._image_tag = image_tag

    @property
    def node_selector(self):
        """Gets the node_selector of this VineyardCompTemplateSpec.  # noqa: E501

        NodeSelector is a selector to choose which nodes to launch the Vineyard component. E,g. {\"disktype\": \"ssd\"}  # noqa: E501

        :return: The node_selector of this VineyardCompTemplateSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this VineyardCompTemplateSpec.

        NodeSelector is a selector to choose which nodes to launch the Vineyard component. E,g. {\"disktype\": \"ssd\"}  # noqa: E501

        :param node_selector: The node_selector of this VineyardCompTemplateSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def options(self):
        """Gets the options of this VineyardCompTemplateSpec.  # noqa: E501

        Configurable options for Vineyard component. For Master, there is no configurable options. For Worker, support the following options.    vineyardd.reserve.memory: (Bool) where to reserve memory for vineyardd                             If set to true, the memory quota will be counted to the vineyardd rather than the application.   etcd.prefix: (String) the prefix of etcd key for vineyard objects    Default value is as follows.      vineyardd.reserve.memory: \"true\"     etcd.prefix: \"/vineyard\"  # noqa: E501

        :return: The options of this VineyardCompTemplateSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this VineyardCompTemplateSpec.

        Configurable options for Vineyard component. For Master, there is no configurable options. For Worker, support the following options.    vineyardd.reserve.memory: (Bool) where to reserve memory for vineyardd                             If set to true, the memory quota will be counted to the vineyardd rather than the application.   etcd.prefix: (String) the prefix of etcd key for vineyard objects    Default value is as follows.      vineyardd.reserve.memory: \"true\"     etcd.prefix: \"/vineyard\"  # noqa: E501

        :param options: The options of this VineyardCompTemplateSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._options = options

    @property
    def ports(self):
        """Gets the ports of this VineyardCompTemplateSpec.  # noqa: E501

        Ports used by Vineyard component. For Master, the default client port is 2379 and peer port is 2380. For Worker, the default rpc port is 9600.  # noqa: E501

        :return: The ports of this VineyardCompTemplateSpec.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this VineyardCompTemplateSpec.

        Ports used by Vineyard component. For Master, the default client port is 2379 and peer port is 2380. For Worker, the default rpc port is 9600.  # noqa: E501

        :param ports: The ports of this VineyardCompTemplateSpec.  # noqa: E501
        :type: dict(str, int)
        """

        self._ports = ports

    @property
    def replicas(self):
        """Gets the replicas of this VineyardCompTemplateSpec.  # noqa: E501

        The replicas of Vineyard component. If not specified, defaults to 1. For worker, the replicas should not be greater than the number of nodes in the cluster  # noqa: E501

        :return: The replicas of this VineyardCompTemplateSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this VineyardCompTemplateSpec.

        The replicas of Vineyard component. If not specified, defaults to 1. For worker, the replicas should not be greater than the number of nodes in the cluster  # noqa: E501

        :param replicas: The replicas of this VineyardCompTemplateSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def resources(self):
        """Gets the resources of this VineyardCompTemplateSpec.  # noqa: E501


        :return: The resources of this VineyardCompTemplateSpec.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this VineyardCompTemplateSpec.


        :param resources: The resources of this VineyardCompTemplateSpec.  # noqa: E501
        :type: V1ResourceRequirements
        """

        self._resources = resources

    @property
    def volume_mounts(self):
        """Gets the volume_mounts of this VineyardCompTemplateSpec.  # noqa: E501

        VolumeMounts specifies the volumes listed in \".spec.volumes\" to mount into the vineyard runtime component's filesystem. It is useful for specifying a persistent storage. Default is not set.  # noqa: E501

        :return: The volume_mounts of this VineyardCompTemplateSpec.  # noqa: E501
        :rtype: list[V1VolumeMount]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts):
        """Sets the volume_mounts of this VineyardCompTemplateSpec.

        VolumeMounts specifies the volumes listed in \".spec.volumes\" to mount into the vineyard runtime component's filesystem. It is useful for specifying a persistent storage. Default is not set.  # noqa: E501

        :param volume_mounts: The volume_mounts of this VineyardCompTemplateSpec.  # noqa: E501
        :type: list[V1VolumeMount]
        """

        self._volume_mounts = volume_mounts

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
        if not isinstance(other, VineyardCompTemplateSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VineyardCompTemplateSpec):
            return True

        return self.to_dict() != other.to_dict()
