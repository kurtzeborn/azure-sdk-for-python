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


class RawCertificateData(Model):
    """Raw certificate data.

    :param auth_type: Specifies the authentication type. Possible values
     include: 'Invalid', 'ACS', 'AAD', 'AccessControlService',
     'AzureActiveDirectory'
    :type auth_type: str or ~azure.mgmt.recoveryservices.models.AuthType
    :param certificate: The base64 encoded certificate raw data string
    :type certificate: bytearray
    """

    _attribute_map = {
        'auth_type': {'key': 'authType', 'type': 'str'},
        'certificate': {'key': 'certificate', 'type': 'bytearray'},
    }

    def __init__(self, **kwargs):
        super(RawCertificateData, self).__init__(**kwargs)
        self.auth_type = kwargs.get('auth_type', None)
        self.certificate = kwargs.get('certificate', None)
