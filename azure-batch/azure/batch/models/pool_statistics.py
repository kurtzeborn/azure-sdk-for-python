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

from msrest.serialization import Model


class PoolStatistics(Model):
    """Contains utilization and resource usage statistics for the lifetime of a
    pool.

    All required parameters must be populated in order to send to Azure.

    :param url: Required. The URL for the statistics.
    :type url: str
    :param start_time: Required. The start time of the time range covered by
     the statistics.
    :type start_time: datetime
    :param last_update_time: Required. The time at which the statistics were
     last updated. All statistics are limited to the range between startTime
     and lastUpdateTime.
    :type last_update_time: datetime
    :param usage_stats: Statistics related to pool usage, such as the amount
     of core-time used.
    :type usage_stats: ~azure.batch.models.UsageStatistics
    :param resource_stats: Statistics related to resource consumption by
     compute nodes in the pool.
    :type resource_stats: ~azure.batch.models.ResourceStatistics
    """

    _validation = {
        'url': {'required': True},
        'start_time': {'required': True},
        'last_update_time': {'required': True},
    }

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'usage_stats': {'key': 'usageStats', 'type': 'UsageStatistics'},
        'resource_stats': {'key': 'resourceStats', 'type': 'ResourceStatistics'},
    }

    def __init__(self, **kwargs):
        super(PoolStatistics, self).__init__(**kwargs)
        self.url = kwargs.get('url', None)
        self.start_time = kwargs.get('start_time', None)
        self.last_update_time = kwargs.get('last_update_time', None)
        self.usage_stats = kwargs.get('usage_stats', None)
        self.resource_stats = kwargs.get('resource_stats', None)
