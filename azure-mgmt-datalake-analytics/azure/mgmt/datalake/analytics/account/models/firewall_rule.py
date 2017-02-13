# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .optional_sub_resource import OptionalSubResource


class FirewallRule(OptionalSubResource):
    """Data Lake Analytics firewall rule information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :param name: Resource name
    :type name: str
    :ivar type: Resource type
    :vartype type: str
    :param start_ip_address: the start IP address for the firewall rule. This
     can be either ipv4 or ipv6. Start and End should be in the same protocol.
    :type start_ip_address: str
    :param end_ip_address: the end IP address for the firewall rule. This can
     be either ipv4 or ipv6. Start and End should be in the same protocol.
    :type end_ip_address: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'start_ip_address': {'required': True},
        'end_ip_address': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'start_ip_address': {'key': 'properties.startIpAddress', 'type': 'str'},
        'end_ip_address': {'key': 'properties.endIpAddress', 'type': 'str'},
    }

    def __init__(self, start_ip_address, end_ip_address, name=None):
        super(FirewallRule, self).__init__(name=name)
        self.start_ip_address = start_ip_address
        self.end_ip_address = end_ip_address
