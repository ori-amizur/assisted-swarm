# coding: utf-8

"""
    AssistedSwarm

    Assisted swarm  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NewAgentParams(object):
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
        'service_url': 'str',
        'infra_env_id': 'str',
        'agent_version': 'str',
        'cacert': 'str',
        'pull_secret': 'str',
        'containers_conf': 'str',
        'containers_storage_conf': 'str',
        'dry_forced_host_id': 'str',
        'dry_forced_host_ipv4': 'str',
        'dry_forced_mac_address': 'str',
        'dry_forced_hostname': 'str',
        'dry_fake_reboot_marker_path': 'str',
        'dry_cluster_hosts_path': 'str'
    }

    attribute_map = {
        'service_url': 'service_url',
        'infra_env_id': 'infra_env_id',
        'agent_version': 'agent_version',
        'cacert': 'cacert',
        'pull_secret': 'pull_secret',
        'containers_conf': 'containers_conf',
        'containers_storage_conf': 'containers_storage_conf',
        'dry_forced_host_id': 'dry_forced_host_id',
        'dry_forced_host_ipv4': 'dry_forced_host_ipv4',
        'dry_forced_mac_address': 'dry_forced_mac_address',
        'dry_forced_hostname': 'dry_forced_hostname',
        'dry_fake_reboot_marker_path': 'dry_fake_reboot_marker_path',
        'dry_cluster_hosts_path': 'dry_cluster_hosts_path'
    }

    def __init__(self, service_url=None, infra_env_id=None, agent_version=None, cacert=None, pull_secret=None, containers_conf=None, containers_storage_conf=None, dry_forced_host_id=None, dry_forced_host_ipv4=None, dry_forced_mac_address=None, dry_forced_hostname=None, dry_fake_reboot_marker_path=None, dry_cluster_hosts_path=None):  # noqa: E501
        """NewAgentParams - a model defined in Swagger"""  # noqa: E501

        self._service_url = None
        self._infra_env_id = None
        self._agent_version = None
        self._cacert = None
        self._pull_secret = None
        self._containers_conf = None
        self._containers_storage_conf = None
        self._dry_forced_host_id = None
        self._dry_forced_host_ipv4 = None
        self._dry_forced_mac_address = None
        self._dry_forced_hostname = None
        self._dry_fake_reboot_marker_path = None
        self._dry_cluster_hosts_path = None
        self.discriminator = None

        if service_url is not None:
            self.service_url = service_url
        if infra_env_id is not None:
            self.infra_env_id = infra_env_id
        if agent_version is not None:
            self.agent_version = agent_version
        if cacert is not None:
            self.cacert = cacert
        if pull_secret is not None:
            self.pull_secret = pull_secret
        if containers_conf is not None:
            self.containers_conf = containers_conf
        if containers_storage_conf is not None:
            self.containers_storage_conf = containers_storage_conf
        if dry_forced_host_id is not None:
            self.dry_forced_host_id = dry_forced_host_id
        if dry_forced_host_ipv4 is not None:
            self.dry_forced_host_ipv4 = dry_forced_host_ipv4
        if dry_forced_mac_address is not None:
            self.dry_forced_mac_address = dry_forced_mac_address
        if dry_forced_hostname is not None:
            self.dry_forced_hostname = dry_forced_hostname
        if dry_fake_reboot_marker_path is not None:
            self.dry_fake_reboot_marker_path = dry_fake_reboot_marker_path
        if dry_cluster_hosts_path is not None:
            self.dry_cluster_hosts_path = dry_cluster_hosts_path

    @property
    def service_url(self):
        """Gets the service_url of this NewAgentParams.  # noqa: E501


        :return: The service_url of this NewAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._service_url

    @service_url.setter
    def service_url(self, service_url):
        """Sets the service_url of this NewAgentParams.


        :param service_url: The service_url of this NewAgentParams.  # noqa: E501
        :type: str
        """

        self._service_url = service_url

    @property
    def infra_env_id(self):
        """Gets the infra_env_id of this NewAgentParams.  # noqa: E501


        :return: The infra_env_id of this NewAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._infra_env_id

    @infra_env_id.setter
    def infra_env_id(self, infra_env_id):
        """Sets the infra_env_id of this NewAgentParams.


        :param infra_env_id: The infra_env_id of this NewAgentParams.  # noqa: E501
        :type: str
        """

        self._infra_env_id = infra_env_id

    @property
    def agent_version(self):
        """Gets the agent_version of this NewAgentParams.  # noqa: E501


        :return: The agent_version of this NewAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this NewAgentParams.


        :param agent_version: The agent_version of this NewAgentParams.  # noqa: E501
        :type: str
        """

        self._agent_version = agent_version

    @property
    def cacert(self):
        """Gets the cacert of this NewAgentParams.  # noqa: E501


        :return: The cacert of this NewAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._cacert

    @cacert.setter
    def cacert(self, cacert):
        """Sets the cacert of this NewAgentParams.


        :param cacert: The cacert of this NewAgentParams.  # noqa: E501
        :type: str
        """

        self._cacert = cacert

    @property
    def pull_secret(self):
        """Gets the pull_secret of this NewAgentParams.  # noqa: E501


        :return: The pull_secret of this NewAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._pull_secret

    @pull_secret.setter
    def pull_secret(self, pull_secret):
        """Sets the pull_secret of this NewAgentParams.


        :param pull_secret: The pull_secret of this NewAgentParams.  # noqa: E501
        :type: str
        """

        self._pull_secret = pull_secret

    @property
    def containers_conf(self):
        """Gets the containers_conf of this NewAgentParams.  # noqa: E501


        :return: The containers_conf of this NewAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._containers_conf

    @containers_conf.setter
    def containers_conf(self, containers_conf):
        """Sets the containers_conf of this NewAgentParams.


        :param containers_conf: The containers_conf of this NewAgentParams.  # noqa: E501
        :type: str
        """

        self._containers_conf = containers_conf

    @property
    def containers_storage_conf(self):
        """Gets the containers_storage_conf of this NewAgentParams.  # noqa: E501


        :return: The containers_storage_conf of this NewAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._containers_storage_conf

    @containers_storage_conf.setter
    def containers_storage_conf(self, containers_storage_conf):
        """Sets the containers_storage_conf of this NewAgentParams.


        :param containers_storage_conf: The containers_storage_conf of this NewAgentParams.  # noqa: E501
        :type: str
        """

        self._containers_storage_conf = containers_storage_conf

    @property
    def dry_forced_host_id(self):
        """Gets the dry_forced_host_id of this NewAgentParams.  # noqa: E501


        :return: The dry_forced_host_id of this NewAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._dry_forced_host_id

    @dry_forced_host_id.setter
    def dry_forced_host_id(self, dry_forced_host_id):
        """Sets the dry_forced_host_id of this NewAgentParams.


        :param dry_forced_host_id: The dry_forced_host_id of this NewAgentParams.  # noqa: E501
        :type: str
        """

        self._dry_forced_host_id = dry_forced_host_id

    @property
    def dry_forced_host_ipv4(self):
        """Gets the dry_forced_host_ipv4 of this NewAgentParams.  # noqa: E501


        :return: The dry_forced_host_ipv4 of this NewAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._dry_forced_host_ipv4

    @dry_forced_host_ipv4.setter
    def dry_forced_host_ipv4(self, dry_forced_host_ipv4):
        """Sets the dry_forced_host_ipv4 of this NewAgentParams.


        :param dry_forced_host_ipv4: The dry_forced_host_ipv4 of this NewAgentParams.  # noqa: E501
        :type: str
        """

        self._dry_forced_host_ipv4 = dry_forced_host_ipv4

    @property
    def dry_forced_mac_address(self):
        """Gets the dry_forced_mac_address of this NewAgentParams.  # noqa: E501


        :return: The dry_forced_mac_address of this NewAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._dry_forced_mac_address

    @dry_forced_mac_address.setter
    def dry_forced_mac_address(self, dry_forced_mac_address):
        """Sets the dry_forced_mac_address of this NewAgentParams.


        :param dry_forced_mac_address: The dry_forced_mac_address of this NewAgentParams.  # noqa: E501
        :type: str
        """

        self._dry_forced_mac_address = dry_forced_mac_address

    @property
    def dry_forced_hostname(self):
        """Gets the dry_forced_hostname of this NewAgentParams.  # noqa: E501


        :return: The dry_forced_hostname of this NewAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._dry_forced_hostname

    @dry_forced_hostname.setter
    def dry_forced_hostname(self, dry_forced_hostname):
        """Sets the dry_forced_hostname of this NewAgentParams.


        :param dry_forced_hostname: The dry_forced_hostname of this NewAgentParams.  # noqa: E501
        :type: str
        """

        self._dry_forced_hostname = dry_forced_hostname

    @property
    def dry_fake_reboot_marker_path(self):
        """Gets the dry_fake_reboot_marker_path of this NewAgentParams.  # noqa: E501


        :return: The dry_fake_reboot_marker_path of this NewAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._dry_fake_reboot_marker_path

    @dry_fake_reboot_marker_path.setter
    def dry_fake_reboot_marker_path(self, dry_fake_reboot_marker_path):
        """Sets the dry_fake_reboot_marker_path of this NewAgentParams.


        :param dry_fake_reboot_marker_path: The dry_fake_reboot_marker_path of this NewAgentParams.  # noqa: E501
        :type: str
        """

        self._dry_fake_reboot_marker_path = dry_fake_reboot_marker_path

    @property
    def dry_cluster_hosts_path(self):
        """Gets the dry_cluster_hosts_path of this NewAgentParams.  # noqa: E501


        :return: The dry_cluster_hosts_path of this NewAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._dry_cluster_hosts_path

    @dry_cluster_hosts_path.setter
    def dry_cluster_hosts_path(self, dry_cluster_hosts_path):
        """Sets the dry_cluster_hosts_path of this NewAgentParams.


        :param dry_cluster_hosts_path: The dry_cluster_hosts_path of this NewAgentParams.  # noqa: E501
        :type: str
        """

        self._dry_cluster_hosts_path = dry_cluster_hosts_path

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
        if issubclass(NewAgentParams, dict):
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
        if not isinstance(other, NewAgentParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
