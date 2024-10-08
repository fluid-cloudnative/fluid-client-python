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


class VineyardRuntimeSpec(object):
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
        'disable_prometheus': 'bool',
        'fuse': 'VineyardClientSocketSpec',
        'master': 'MasterSpec',
        'pod_metadata': 'PodMetadata',
        'replicas': 'int',
        'tieredstore': 'TieredStore',
        'volumes': 'list[V1Volume]',
        'worker': 'VineyardCompTemplateSpec'
    }

    attribute_map = {
        'disable_prometheus': 'disablePrometheus',
        'fuse': 'fuse',
        'master': 'master',
        'pod_metadata': 'podMetadata',
        'replicas': 'replicas',
        'tieredstore': 'tieredstore',
        'volumes': 'volumes',
        'worker': 'worker'
    }

    def __init__(self, disable_prometheus=None, fuse=None, master=None, pod_metadata=None, replicas=None, tieredstore=None, volumes=None, worker=None, local_vars_configuration=None):  # noqa: E501
        """VineyardRuntimeSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._disable_prometheus = None
        self._fuse = None
        self._master = None
        self._pod_metadata = None
        self._replicas = None
        self._tieredstore = None
        self._volumes = None
        self._worker = None
        self.discriminator = None

        if disable_prometheus is not None:
            self.disable_prometheus = disable_prometheus
        if fuse is not None:
            self.fuse = fuse
        if master is not None:
            self.master = master
        if pod_metadata is not None:
            self.pod_metadata = pod_metadata
        if replicas is not None:
            self.replicas = replicas
        if tieredstore is not None:
            self.tieredstore = tieredstore
        if volumes is not None:
            self.volumes = volumes
        if worker is not None:
            self.worker = worker

    @property
    def disable_prometheus(self):
        """Gets the disable_prometheus of this VineyardRuntimeSpec.  # noqa: E501

        Disable monitoring metrics for Vineyard Runtime Default is false  # noqa: E501

        :return: The disable_prometheus of this VineyardRuntimeSpec.  # noqa: E501
        :rtype: bool
        """
        return self._disable_prometheus

    @disable_prometheus.setter
    def disable_prometheus(self, disable_prometheus):
        """Sets the disable_prometheus of this VineyardRuntimeSpec.

        Disable monitoring metrics for Vineyard Runtime Default is false  # noqa: E501

        :param disable_prometheus: The disable_prometheus of this VineyardRuntimeSpec.  # noqa: E501
        :type: bool
        """

        self._disable_prometheus = disable_prometheus

    @property
    def fuse(self):
        """Gets the fuse of this VineyardRuntimeSpec.  # noqa: E501


        :return: The fuse of this VineyardRuntimeSpec.  # noqa: E501
        :rtype: VineyardClientSocketSpec
        """
        return self._fuse

    @fuse.setter
    def fuse(self, fuse):
        """Sets the fuse of this VineyardRuntimeSpec.


        :param fuse: The fuse of this VineyardRuntimeSpec.  # noqa: E501
        :type: VineyardClientSocketSpec
        """

        self._fuse = fuse

    @property
    def master(self):
        """Gets the master of this VineyardRuntimeSpec.  # noqa: E501


        :return: The master of this VineyardRuntimeSpec.  # noqa: E501
        :rtype: MasterSpec
        """
        return self._master

    @master.setter
    def master(self, master):
        """Sets the master of this VineyardRuntimeSpec.


        :param master: The master of this VineyardRuntimeSpec.  # noqa: E501
        :type: MasterSpec
        """

        self._master = master

    @property
    def pod_metadata(self):
        """Gets the pod_metadata of this VineyardRuntimeSpec.  # noqa: E501


        :return: The pod_metadata of this VineyardRuntimeSpec.  # noqa: E501
        :rtype: PodMetadata
        """
        return self._pod_metadata

    @pod_metadata.setter
    def pod_metadata(self, pod_metadata):
        """Sets the pod_metadata of this VineyardRuntimeSpec.


        :param pod_metadata: The pod_metadata of this VineyardRuntimeSpec.  # noqa: E501
        :type: PodMetadata
        """

        self._pod_metadata = pod_metadata

    @property
    def replicas(self):
        """Gets the replicas of this VineyardRuntimeSpec.  # noqa: E501

        The replicas of the worker, need to be specified If worker.replicas and the field are both specified, the field will be respected  # noqa: E501

        :return: The replicas of this VineyardRuntimeSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this VineyardRuntimeSpec.

        The replicas of the worker, need to be specified If worker.replicas and the field are both specified, the field will be respected  # noqa: E501

        :param replicas: The replicas of this VineyardRuntimeSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def tieredstore(self):
        """Gets the tieredstore of this VineyardRuntimeSpec.  # noqa: E501


        :return: The tieredstore of this VineyardRuntimeSpec.  # noqa: E501
        :rtype: TieredStore
        """
        return self._tieredstore

    @tieredstore.setter
    def tieredstore(self, tieredstore):
        """Sets the tieredstore of this VineyardRuntimeSpec.


        :param tieredstore: The tieredstore of this VineyardRuntimeSpec.  # noqa: E501
        :type: TieredStore
        """

        self._tieredstore = tieredstore

    @property
    def volumes(self):
        """Gets the volumes of this VineyardRuntimeSpec.  # noqa: E501

        Volumes is the list of Kubernetes volumes that can be mounted by the vineyard components (Master and Worker). Default is null.  # noqa: E501

        :return: The volumes of this VineyardRuntimeSpec.  # noqa: E501
        :rtype: list[V1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this VineyardRuntimeSpec.

        Volumes is the list of Kubernetes volumes that can be mounted by the vineyard components (Master and Worker). Default is null.  # noqa: E501

        :param volumes: The volumes of this VineyardRuntimeSpec.  # noqa: E501
        :type: list[V1Volume]
        """

        self._volumes = volumes

    @property
    def worker(self):
        """Gets the worker of this VineyardRuntimeSpec.  # noqa: E501


        :return: The worker of this VineyardRuntimeSpec.  # noqa: E501
        :rtype: VineyardCompTemplateSpec
        """
        return self._worker

    @worker.setter
    def worker(self, worker):
        """Sets the worker of this VineyardRuntimeSpec.


        :param worker: The worker of this VineyardRuntimeSpec.  # noqa: E501
        :type: VineyardCompTemplateSpec
        """

        self._worker = worker

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
        if not isinstance(other, VineyardRuntimeSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VineyardRuntimeSpec):
            return True

        return self.to_dict() != other.to_dict()
