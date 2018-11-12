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


class NotificationSettingsCollection(Model):
    """Model for collection of notificationSettings.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar next_link: URL to the next set of results.
    :vartype next_link: str
    :ivar value: Collection of components.
    :vartype value:
     list[~azure.mgmt.workloadmonitor.models.NotificationSetting]
    """

    _validation = {
        'next_link': {'readonly': True},
        'value': {'readonly': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[NotificationSetting]'},
    }

    def __init__(self, **kwargs) -> None:
        super(NotificationSettingsCollection, self).__init__(**kwargs)
        self.next_link = None
        self.value = None
