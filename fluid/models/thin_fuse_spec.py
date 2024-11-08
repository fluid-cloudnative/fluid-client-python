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


class ThinFuseSpec(object):
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
        'args': 'list[str]',
        'clean_policy': 'str',
        'command': 'list[str]',
        'env': 'list[V1EnvVar]',
        'image': 'str',
        'image_pull_policy': 'str',
        'image_pull_secrets': 'list[V1LocalObjectReference]',
        'image_tag': 'str',
        'liveness_probe': 'V1Probe',
        'network_mode': 'str',
        'node_selector': 'dict(str, str)',
        'options': 'dict(str, str)',
        'ports': 'list[V1ContainerPort]',
        'readiness_probe': 'V1Probe',
        'resources': 'V1ResourceRequirements',
        'volume_mounts': 'list[V1VolumeMount]'
    }

    attribute_map = {
        'args': 'args',
        'clean_policy': 'cleanPolicy',
        'command': 'command',
        'env': 'env',
        'image': 'image',
        'image_pull_policy': 'imagePullPolicy',
        'image_pull_secrets': 'imagePullSecrets',
        'image_tag': 'imageTag',
        'liveness_probe': 'livenessProbe',
        'network_mode': 'networkMode',
        'node_selector': 'nodeSelector',
        'options': 'options',
        'ports': 'ports',
        'readiness_probe': 'readinessProbe',
        'resources': 'resources',
        'volume_mounts': 'volumeMounts'
    }

    def __init__(self, args=None, clean_policy=None, command=None, env=None, image=None, image_pull_policy=None, image_pull_secrets=None, image_tag=None, liveness_probe=None, network_mode=None, node_selector=None, options=None, ports=None, readiness_probe=None, resources=None, volume_mounts=None, local_vars_configuration=None):  # noqa: E501
        """ThinFuseSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._args = None
        self._clean_policy = None
        self._command = None
        self._env = None
        self._image = None
        self._image_pull_policy = None
        self._image_pull_secrets = None
        self._image_tag = None
        self._liveness_probe = None
        self._network_mode = None
        self._node_selector = None
        self._options = None
        self._ports = None
        self._readiness_probe = None
        self._resources = None
        self._volume_mounts = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if clean_policy is not None:
            self.clean_policy = clean_policy
        if command is not None:
            self.command = command
        if env is not None:
            self.env = env
        if image is not None:
            self.image = image
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if image_pull_secrets is not None:
            self.image_pull_secrets = image_pull_secrets
        if image_tag is not None:
            self.image_tag = image_tag
        if liveness_probe is not None:
            self.liveness_probe = liveness_probe
        if network_mode is not None:
            self.network_mode = network_mode
        if node_selector is not None:
            self.node_selector = node_selector
        if options is not None:
            self.options = options
        if ports is not None:
            self.ports = ports
        if readiness_probe is not None:
            self.readiness_probe = readiness_probe
        if resources is not None:
            self.resources = resources
        if volume_mounts is not None:
            self.volume_mounts = volume_mounts

    @property
    def args(self):
        """Gets the args of this ThinFuseSpec.  # noqa: E501

        Arguments that will be passed to thinRuntime Fuse  # noqa: E501

        :return: The args of this ThinFuseSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this ThinFuseSpec.

        Arguments that will be passed to thinRuntime Fuse  # noqa: E501

        :param args: The args of this ThinFuseSpec.  # noqa: E501
        :type: list[str]
        """

        self._args = args

    @property
    def clean_policy(self):
        """Gets the clean_policy of this ThinFuseSpec.  # noqa: E501

        CleanPolicy decides when to clean thinRuntime Fuse pods. Currently Fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once the fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnDemand  # noqa: E501

        :return: The clean_policy of this ThinFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._clean_policy

    @clean_policy.setter
    def clean_policy(self, clean_policy):
        """Sets the clean_policy of this ThinFuseSpec.

        CleanPolicy decides when to clean thinRuntime Fuse pods. Currently Fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once the fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnDemand  # noqa: E501

        :param clean_policy: The clean_policy of this ThinFuseSpec.  # noqa: E501
        :type: str
        """

        self._clean_policy = clean_policy

    @property
    def command(self):
        """Gets the command of this ThinFuseSpec.  # noqa: E501

        Command that will be passed to thinRuntime Fuse  # noqa: E501

        :return: The command of this ThinFuseSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ThinFuseSpec.

        Command that will be passed to thinRuntime Fuse  # noqa: E501

        :param command: The command of this ThinFuseSpec.  # noqa: E501
        :type: list[str]
        """

        self._command = command

    @property
    def env(self):
        """Gets the env of this ThinFuseSpec.  # noqa: E501

        Environment variables that will be used by thinRuntime Fuse  # noqa: E501

        :return: The env of this ThinFuseSpec.  # noqa: E501
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this ThinFuseSpec.

        Environment variables that will be used by thinRuntime Fuse  # noqa: E501

        :param env: The env of this ThinFuseSpec.  # noqa: E501
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def image(self):
        """Gets the image of this ThinFuseSpec.  # noqa: E501

        Image for thinRuntime fuse  # noqa: E501

        :return: The image of this ThinFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ThinFuseSpec.

        Image for thinRuntime fuse  # noqa: E501

        :param image: The image of this ThinFuseSpec.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this ThinFuseSpec.  # noqa: E501

        One of the three policies: `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :return: The image_pull_policy of this ThinFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this ThinFuseSpec.

        One of the three policies: `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :param image_pull_policy: The image_pull_policy of this ThinFuseSpec.  # noqa: E501
        :type: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def image_pull_secrets(self):
        """Gets the image_pull_secrets of this ThinFuseSpec.  # noqa: E501

        ImagePullSecrets that will be used to pull images  # noqa: E501

        :return: The image_pull_secrets of this ThinFuseSpec.  # noqa: E501
        :rtype: list[V1LocalObjectReference]
        """
        return self._image_pull_secrets

    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets):
        """Sets the image_pull_secrets of this ThinFuseSpec.

        ImagePullSecrets that will be used to pull images  # noqa: E501

        :param image_pull_secrets: The image_pull_secrets of this ThinFuseSpec.  # noqa: E501
        :type: list[V1LocalObjectReference]
        """

        self._image_pull_secrets = image_pull_secrets

    @property
    def image_tag(self):
        """Gets the image_tag of this ThinFuseSpec.  # noqa: E501

        Image for thinRuntime fuse  # noqa: E501

        :return: The image_tag of this ThinFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this ThinFuseSpec.

        Image for thinRuntime fuse  # noqa: E501

        :param image_tag: The image_tag of this ThinFuseSpec.  # noqa: E501
        :type: str
        """

        self._image_tag = image_tag

    @property
    def liveness_probe(self):
        """Gets the liveness_probe of this ThinFuseSpec.  # noqa: E501


        :return: The liveness_probe of this ThinFuseSpec.  # noqa: E501
        :rtype: V1Probe
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """Sets the liveness_probe of this ThinFuseSpec.


        :param liveness_probe: The liveness_probe of this ThinFuseSpec.  # noqa: E501
        :type: V1Probe
        """

        self._liveness_probe = liveness_probe

    @property
    def network_mode(self):
        """Gets the network_mode of this ThinFuseSpec.  # noqa: E501

        Whether to use hostnetwork or not  # noqa: E501

        :return: The network_mode of this ThinFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._network_mode

    @network_mode.setter
    def network_mode(self, network_mode):
        """Sets the network_mode of this ThinFuseSpec.

        Whether to use hostnetwork or not  # noqa: E501

        :param network_mode: The network_mode of this ThinFuseSpec.  # noqa: E501
        :type: str
        """

        self._network_mode = network_mode

    @property
    def node_selector(self):
        """Gets the node_selector of this ThinFuseSpec.  # noqa: E501

        NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled  # noqa: E501

        :return: The node_selector of this ThinFuseSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this ThinFuseSpec.

        NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled  # noqa: E501

        :param node_selector: The node_selector of this ThinFuseSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def options(self):
        """Gets the options of this ThinFuseSpec.  # noqa: E501

        Options configurable options of FUSE client, performance parameters usually. will be merged with Dataset.spec.mounts.options into fuse pod.  # noqa: E501

        :return: The options of this ThinFuseSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ThinFuseSpec.

        Options configurable options of FUSE client, performance parameters usually. will be merged with Dataset.spec.mounts.options into fuse pod.  # noqa: E501

        :param options: The options of this ThinFuseSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._options = options

    @property
    def ports(self):
        """Gets the ports of this ThinFuseSpec.  # noqa: E501

        Ports used thinRuntime  # noqa: E501

        :return: The ports of this ThinFuseSpec.  # noqa: E501
        :rtype: list[V1ContainerPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this ThinFuseSpec.

        Ports used thinRuntime  # noqa: E501

        :param ports: The ports of this ThinFuseSpec.  # noqa: E501
        :type: list[V1ContainerPort]
        """

        self._ports = ports

    @property
    def readiness_probe(self):
        """Gets the readiness_probe of this ThinFuseSpec.  # noqa: E501


        :return: The readiness_probe of this ThinFuseSpec.  # noqa: E501
        :rtype: V1Probe
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """Sets the readiness_probe of this ThinFuseSpec.


        :param readiness_probe: The readiness_probe of this ThinFuseSpec.  # noqa: E501
        :type: V1Probe
        """

        self._readiness_probe = readiness_probe

    @property
    def resources(self):
        """Gets the resources of this ThinFuseSpec.  # noqa: E501


        :return: The resources of this ThinFuseSpec.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ThinFuseSpec.


        :param resources: The resources of this ThinFuseSpec.  # noqa: E501
        :type: V1ResourceRequirements
        """

        self._resources = resources

    @property
    def volume_mounts(self):
        """Gets the volume_mounts of this ThinFuseSpec.  # noqa: E501

        VolumeMounts specifies the volumes listed in \".spec.volumes\" to mount into the thinruntime component's filesystem.  # noqa: E501

        :return: The volume_mounts of this ThinFuseSpec.  # noqa: E501
        :rtype: list[V1VolumeMount]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts):
        """Sets the volume_mounts of this ThinFuseSpec.

        VolumeMounts specifies the volumes listed in \".spec.volumes\" to mount into the thinruntime component's filesystem.  # noqa: E501

        :param volume_mounts: The volume_mounts of this ThinFuseSpec.  # noqa: E501
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
        if not isinstance(other, ThinFuseSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ThinFuseSpec):
            return True

        return self.to_dict() != other.to_dict()
