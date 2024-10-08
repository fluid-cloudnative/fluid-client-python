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


class OperationStatus(object):
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
        'conditions': 'list[Condition]',
        'duration': 'str',
        'infos': 'dict(str, str)',
        'last_schedule_time': 'datetime',
        'last_successful_time': 'datetime',
        'node_affinity': 'V1NodeAffinity',
        'phase': 'str',
        'waiting_for': 'WaitingStatus'
    }

    attribute_map = {
        'conditions': 'conditions',
        'duration': 'duration',
        'infos': 'infos',
        'last_schedule_time': 'lastScheduleTime',
        'last_successful_time': 'lastSuccessfulTime',
        'node_affinity': 'nodeAffinity',
        'phase': 'phase',
        'waiting_for': 'waitingFor'
    }

    def __init__(self, conditions=None, duration='', infos=None, last_schedule_time=None, last_successful_time=None, node_affinity=None, phase='', waiting_for=None, local_vars_configuration=None):  # noqa: E501
        """OperationStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self._duration = None
        self._infos = None
        self._last_schedule_time = None
        self._last_successful_time = None
        self._node_affinity = None
        self._phase = None
        self._waiting_for = None
        self.discriminator = None

        self.conditions = conditions
        self.duration = duration
        if infos is not None:
            self.infos = infos
        if last_schedule_time is not None:
            self.last_schedule_time = last_schedule_time
        if last_successful_time is not None:
            self.last_successful_time = last_successful_time
        if node_affinity is not None:
            self.node_affinity = node_affinity
        self.phase = phase
        if waiting_for is not None:
            self.waiting_for = waiting_for

    @property
    def conditions(self):
        """Gets the conditions of this OperationStatus.  # noqa: E501

        Conditions consists of transition information on operation's Phase  # noqa: E501

        :return: The conditions of this OperationStatus.  # noqa: E501
        :rtype: list[Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this OperationStatus.

        Conditions consists of transition information on operation's Phase  # noqa: E501

        :param conditions: The conditions of this OperationStatus.  # noqa: E501
        :type: list[Condition]
        """
        if self.local_vars_configuration.client_side_validation and conditions is None:  # noqa: E501
            raise ValueError("Invalid value for `conditions`, must not be `None`")  # noqa: E501

        self._conditions = conditions

    @property
    def duration(self):
        """Gets the duration of this OperationStatus.  # noqa: E501

        Duration tell user how much time was spent to operation  # noqa: E501

        :return: The duration of this OperationStatus.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this OperationStatus.

        Duration tell user how much time was spent to operation  # noqa: E501

        :param duration: The duration of this OperationStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and duration is None:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def infos(self):
        """Gets the infos of this OperationStatus.  # noqa: E501

        Infos operation customized name-value  # noqa: E501

        :return: The infos of this OperationStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._infos

    @infos.setter
    def infos(self, infos):
        """Sets the infos of this OperationStatus.

        Infos operation customized name-value  # noqa: E501

        :param infos: The infos of this OperationStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._infos = infos

    @property
    def last_schedule_time(self):
        """Gets the last_schedule_time of this OperationStatus.  # noqa: E501


        :return: The last_schedule_time of this OperationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_schedule_time

    @last_schedule_time.setter
    def last_schedule_time(self, last_schedule_time):
        """Sets the last_schedule_time of this OperationStatus.


        :param last_schedule_time: The last_schedule_time of this OperationStatus.  # noqa: E501
        :type: datetime
        """

        self._last_schedule_time = last_schedule_time

    @property
    def last_successful_time(self):
        """Gets the last_successful_time of this OperationStatus.  # noqa: E501


        :return: The last_successful_time of this OperationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_successful_time

    @last_successful_time.setter
    def last_successful_time(self, last_successful_time):
        """Sets the last_successful_time of this OperationStatus.


        :param last_successful_time: The last_successful_time of this OperationStatus.  # noqa: E501
        :type: datetime
        """

        self._last_successful_time = last_successful_time

    @property
    def node_affinity(self):
        """Gets the node_affinity of this OperationStatus.  # noqa: E501


        :return: The node_affinity of this OperationStatus.  # noqa: E501
        :rtype: V1NodeAffinity
        """
        return self._node_affinity

    @node_affinity.setter
    def node_affinity(self, node_affinity):
        """Sets the node_affinity of this OperationStatus.


        :param node_affinity: The node_affinity of this OperationStatus.  # noqa: E501
        :type: V1NodeAffinity
        """

        self._node_affinity = node_affinity

    @property
    def phase(self):
        """Gets the phase of this OperationStatus.  # noqa: E501

        Phase describes current phase of operation  # noqa: E501

        :return: The phase of this OperationStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this OperationStatus.

        Phase describes current phase of operation  # noqa: E501

        :param phase: The phase of this OperationStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and phase is None:  # noqa: E501
            raise ValueError("Invalid value for `phase`, must not be `None`")  # noqa: E501

        self._phase = phase

    @property
    def waiting_for(self):
        """Gets the waiting_for of this OperationStatus.  # noqa: E501


        :return: The waiting_for of this OperationStatus.  # noqa: E501
        :rtype: WaitingStatus
        """
        return self._waiting_for

    @waiting_for.setter
    def waiting_for(self, waiting_for):
        """Sets the waiting_for of this OperationStatus.


        :param waiting_for: The waiting_for of this OperationStatus.  # noqa: E501
        :type: WaitingStatus
        """

        self._waiting_for = waiting_for

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
        if not isinstance(other, OperationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OperationStatus):
            return True

        return self.to_dict() != other.to_dict()
