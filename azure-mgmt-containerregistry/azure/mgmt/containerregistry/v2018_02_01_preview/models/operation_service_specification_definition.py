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


class OperationServiceSpecificationDefinition(Model):
    """The definition of Azure Monitoring metrics list.

    :param metric_specifications: A list of Azure Monitoring metrics
     definition.
    :type metric_specifications:
     list[~azure.mgmt.containerregistry.v2018_02_01_preview.models.OperationMetricSpecificationDefinition]
    """

    _attribute_map = {
        'metric_specifications': {'key': 'metricSpecifications', 'type': '[OperationMetricSpecificationDefinition]'},
    }

    def __init__(self, **kwargs):
        super(OperationServiceSpecificationDefinition, self).__init__(**kwargs)
        self.metric_specifications = kwargs.get('metric_specifications', None)
