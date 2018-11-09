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


class AppSkuInfo(Model):
    """Information about the SKU of the IoT Central application.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SKU. Possible values include: 'F1',
     'S1'
    :type name: str or ~azure.mgmt.iotcentral.models.AppSku
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AppSkuInfo, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
