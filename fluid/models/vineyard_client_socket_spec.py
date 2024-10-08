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


class VineyardClientSocketSpec(object):
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
        'clean_policy': 'str',
        'env': 'dict(str, str)',
        'image': 'str',
        'image_pull_policy': 'str',
        'image_tag': 'str',
        'network_mode': 'str',
        'options': 'dict(str, str)',
        'pod_metadata': 'PodMetadata',
        'resources': 'V1ResourceRequirements'
    }

    attribute_map = {
        'clean_policy': 'cleanPolicy',
        'env': 'env',
        'image': 'image',
        'image_pull_policy': 'imagePullPolicy',
        'image_tag': 'imageTag',
        'network_mode': 'networkMode',
        'options': 'options',
        'pod_metadata': 'podMetadata',
        'resources': 'resources'
    }

    def __init__(self, clean_policy=None, env=None, image=None, image_pull_policy=None, image_tag=None, network_mode=None, options=None, pod_metadata=None, resources=None, local_vars_configuration=None):  # noqa: E501
        """VineyardClientSocketSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._clean_policy = None
        self._env = None
        self._image = None
        self._image_pull_policy = None
        self._image_tag = None
        self._network_mode = None
        self._options = None
        self._pod_metadata = None
        self._resources = None
        self.discriminator = None

        if clean_policy is not None:
            self.clean_policy = clean_policy
        if env is not None:
            self.env = env
        if image is not None:
            self.image = image
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if image_tag is not None:
            self.image_tag = image_tag
        if network_mode is not None:
            self.network_mode = network_mode
        if options is not None:
            self.options = options
        if pod_metadata is not None:
            self.pod_metadata = pod_metadata
        if resources is not None:
            self.resources = resources

    @property
    def clean_policy(self):
        """Gets the clean_policy of this VineyardClientSocketSpec.  # noqa: E501

        CleanPolicy decides when to clean Vineyard Fuse pods. Currently Fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once th fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnRuntimeDeleted  # noqa: E501

        :return: The clean_policy of this VineyardClientSocketSpec.  # noqa: E501
        :rtype: str
        """
        return self._clean_policy

    @clean_policy.setter
    def clean_policy(self, clean_policy):
        """Sets the clean_policy of this VineyardClientSocketSpec.

        CleanPolicy decides when to clean Vineyard Fuse pods. Currently Fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once th fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnRuntimeDeleted  # noqa: E501

        :param clean_policy: The clean_policy of this VineyardClientSocketSpec.  # noqa: E501
        :type: str
        """

        self._clean_policy = clean_policy

    @property
    def env(self):
        """Gets the env of this VineyardClientSocketSpec.  # noqa: E501

        Environment variables that will be used by Vineyard Fuse. Default is not set.  # noqa: E501

        :return: The env of this VineyardClientSocketSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this VineyardClientSocketSpec.

        Environment variables that will be used by Vineyard Fuse. Default is not set.  # noqa: E501

        :param env: The env of this VineyardClientSocketSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._env = env

    @property
    def image(self):
        """Gets the image of this VineyardClientSocketSpec.  # noqa: E501

        Image for Vineyard Fuse Default is `registry.aliyuncs.com/vineyard/vineyard-fluid-fuse`  # noqa: E501

        :return: The image of this VineyardClientSocketSpec.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this VineyardClientSocketSpec.

        Image for Vineyard Fuse Default is `registry.aliyuncs.com/vineyard/vineyard-fluid-fuse`  # noqa: E501

        :param image: The image of this VineyardClientSocketSpec.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this VineyardClientSocketSpec.  # noqa: E501

        Image pull policy for Vineyard Fuse Default is `IfNotPresent` Available values are `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :return: The image_pull_policy of this VineyardClientSocketSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this VineyardClientSocketSpec.

        Image pull policy for Vineyard Fuse Default is `IfNotPresent` Available values are `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :param image_pull_policy: The image_pull_policy of this VineyardClientSocketSpec.  # noqa: E501
        :type: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def image_tag(self):
        """Gets the image_tag of this VineyardClientSocketSpec.  # noqa: E501

        Image Tag for Vineyard Fuse Default is `v0.22.2`  # noqa: E501

        :return: The image_tag of this VineyardClientSocketSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this VineyardClientSocketSpec.

        Image Tag for Vineyard Fuse Default is `v0.22.2`  # noqa: E501

        :param image_tag: The image_tag of this VineyardClientSocketSpec.  # noqa: E501
        :type: str
        """

        self._image_tag = image_tag

    @property
    def network_mode(self):
        """Gets the network_mode of this VineyardClientSocketSpec.  # noqa: E501

        Whether to use hostnetwork or not Default is HostNetwork  # noqa: E501

        :return: The network_mode of this VineyardClientSocketSpec.  # noqa: E501
        :rtype: str
        """
        return self._network_mode

    @network_mode.setter
    def network_mode(self, network_mode):
        """Sets the network_mode of this VineyardClientSocketSpec.

        Whether to use hostnetwork or not Default is HostNetwork  # noqa: E501

        :param network_mode: The network_mode of this VineyardClientSocketSpec.  # noqa: E501
        :type: str
        """

        self._network_mode = network_mode

    @property
    def options(self):
        """Gets the options of this VineyardClientSocketSpec.  # noqa: E501

        Options for configuring vineyardd parameters. Supported options are as follows.   reserve_memory: (Bool) Whether to reserving enough physical memory pages for vineyardd.                   Default is true.   allocator: (String) The allocator used by vineyardd, could be \"dlmalloc\" or \"mimalloc\".              Default is \"dlmalloc\".   compression: (Bool) Compress before migration or spilling.                Default is true.   coredump: (Bool) Enable coredump core dump when been aborted.             Default is false.   meta_timeout: (Int) Timeout period before waiting the metadata service to be ready, in seconds        Default is 60.   etcd_endpoint: (String) The endpoint of etcd.                  Default is same as the etcd endpoint of vineyard worker.   etcd_prefix: (String) Metadata path prefix in etcd.                Default is \"/vineyard\".   size: (String) shared memory size for vineyardd.                  1024M, 1024000, 1G, or 1Gi.                  Default is \"0\", which means no cache.                  When the size is not set to \"0\", it should be greater than the 2048 bytes(2K).   spill_path: (String) Path to spill temporary files, if not set, spilling will be disabled.               Default is \"\".   spill_lower_rate: (Double) The lower rate of memory usage to trigger spilling.         Default is 0.3.   spill_upper_rate: (Double) The upper rate of memory usage to stop spilling.         Default is 0.8. Default is as follows. fuse:   options:     size: \"0\"     etcd_endpoint: \"http://{{Name}}-master-0.{{Name}}-master.{{Namespace}}:{{EtcdClientPort}}\"     etcd_prefix: \"/vineyard\"  # noqa: E501

        :return: The options of this VineyardClientSocketSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this VineyardClientSocketSpec.

        Options for configuring vineyardd parameters. Supported options are as follows.   reserve_memory: (Bool) Whether to reserving enough physical memory pages for vineyardd.                   Default is true.   allocator: (String) The allocator used by vineyardd, could be \"dlmalloc\" or \"mimalloc\".              Default is \"dlmalloc\".   compression: (Bool) Compress before migration or spilling.                Default is true.   coredump: (Bool) Enable coredump core dump when been aborted.             Default is false.   meta_timeout: (Int) Timeout period before waiting the metadata service to be ready, in seconds        Default is 60.   etcd_endpoint: (String) The endpoint of etcd.                  Default is same as the etcd endpoint of vineyard worker.   etcd_prefix: (String) Metadata path prefix in etcd.                Default is \"/vineyard\".   size: (String) shared memory size for vineyardd.                  1024M, 1024000, 1G, or 1Gi.                  Default is \"0\", which means no cache.                  When the size is not set to \"0\", it should be greater than the 2048 bytes(2K).   spill_path: (String) Path to spill temporary files, if not set, spilling will be disabled.               Default is \"\".   spill_lower_rate: (Double) The lower rate of memory usage to trigger spilling.         Default is 0.3.   spill_upper_rate: (Double) The upper rate of memory usage to stop spilling.         Default is 0.8. Default is as follows. fuse:   options:     size: \"0\"     etcd_endpoint: \"http://{{Name}}-master-0.{{Name}}-master.{{Namespace}}:{{EtcdClientPort}}\"     etcd_prefix: \"/vineyard\"  # noqa: E501

        :param options: The options of this VineyardClientSocketSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._options = options

    @property
    def pod_metadata(self):
        """Gets the pod_metadata of this VineyardClientSocketSpec.  # noqa: E501


        :return: The pod_metadata of this VineyardClientSocketSpec.  # noqa: E501
        :rtype: PodMetadata
        """
        return self._pod_metadata

    @pod_metadata.setter
    def pod_metadata(self, pod_metadata):
        """Sets the pod_metadata of this VineyardClientSocketSpec.


        :param pod_metadata: The pod_metadata of this VineyardClientSocketSpec.  # noqa: E501
        :type: PodMetadata
        """

        self._pod_metadata = pod_metadata

    @property
    def resources(self):
        """Gets the resources of this VineyardClientSocketSpec.  # noqa: E501


        :return: The resources of this VineyardClientSocketSpec.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this VineyardClientSocketSpec.


        :param resources: The resources of this VineyardClientSocketSpec.  # noqa: E501
        :type: V1ResourceRequirements
        """

        self._resources = resources

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
        if not isinstance(other, VineyardClientSocketSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VineyardClientSocketSpec):
            return True

        return self.to_dict() != other.to_dict()
