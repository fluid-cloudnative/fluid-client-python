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


class Processor(object):
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
        'job': 'JobProcessor',
        'pod_metadata': 'PodMetadata',
        'script': 'ScriptProcessor',
        'service_account_name': 'str'
    }

    attribute_map = {
        'job': 'job',
        'pod_metadata': 'podMetadata',
        'script': 'script',
        'service_account_name': 'serviceAccountName'
    }

    def __init__(self, job=None, pod_metadata=None, script=None, service_account_name=None, local_vars_configuration=None):  # noqa: E501
        """Processor - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._job = None
        self._pod_metadata = None
        self._script = None
        self._service_account_name = None
        self.discriminator = None

        if job is not None:
            self.job = job
        if pod_metadata is not None:
            self.pod_metadata = pod_metadata
        if script is not None:
            self.script = script
        if service_account_name is not None:
            self.service_account_name = service_account_name

    @property
    def job(self):
        """Gets the job of this Processor.  # noqa: E501


        :return: The job of this Processor.  # noqa: E501
        :rtype: JobProcessor
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this Processor.


        :param job: The job of this Processor.  # noqa: E501
        :type: JobProcessor
        """

        self._job = job

    @property
    def pod_metadata(self):
        """Gets the pod_metadata of this Processor.  # noqa: E501


        :return: The pod_metadata of this Processor.  # noqa: E501
        :rtype: PodMetadata
        """
        return self._pod_metadata

    @pod_metadata.setter
    def pod_metadata(self, pod_metadata):
        """Sets the pod_metadata of this Processor.


        :param pod_metadata: The pod_metadata of this Processor.  # noqa: E501
        :type: PodMetadata
        """

        self._pod_metadata = pod_metadata

    @property
    def script(self):
        """Gets the script of this Processor.  # noqa: E501


        :return: The script of this Processor.  # noqa: E501
        :rtype: ScriptProcessor
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this Processor.


        :param script: The script of this Processor.  # noqa: E501
        :type: ScriptProcessor
        """

        self._script = script

    @property
    def service_account_name(self):
        """Gets the service_account_name of this Processor.  # noqa: E501

        ServiceAccountName defiens the serviceAccountName of the container  # noqa: E501

        :return: The service_account_name of this Processor.  # noqa: E501
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """Sets the service_account_name of this Processor.

        ServiceAccountName defiens the serviceAccountName of the container  # noqa: E501

        :param service_account_name: The service_account_name of this Processor.  # noqa: E501
        :type: str
        """

        self._service_account_name = service_account_name

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
        if not isinstance(other, Processor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Processor):
            return True

        return self.to_dict() != other.to_dict()
