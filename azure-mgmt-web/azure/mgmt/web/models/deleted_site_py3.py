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

from .proxy_only_resource_py3 import ProxyOnlyResource


class DeletedSite(ProxyOnlyResource):
    """A deleted app.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar deleted_site_id: Numeric id for the deleted site
    :vartype deleted_site_id: int
    :ivar deleted_timestamp: Time in UTC when the app was deleted.
    :vartype deleted_timestamp: str
    :ivar subscription: Subscription containing the deleted site
    :vartype subscription: str
    :ivar resource_group: ResourceGroup that contained the deleted site
    :vartype resource_group: str
    :ivar deleted_site_name: Name of the deleted site
    :vartype deleted_site_name: str
    :ivar slot: Slot of the deleted site
    :vartype slot: str
    :ivar deleted_site_kind: Kind of site that was deleted
    :vartype deleted_site_kind: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'deleted_site_id': {'readonly': True},
        'deleted_timestamp': {'readonly': True},
        'subscription': {'readonly': True},
        'resource_group': {'readonly': True},
        'deleted_site_name': {'readonly': True},
        'slot': {'readonly': True},
        'deleted_site_kind': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'deleted_site_id': {'key': 'properties.deletedSiteId', 'type': 'int'},
        'deleted_timestamp': {'key': 'properties.deletedTimestamp', 'type': 'str'},
        'subscription': {'key': 'properties.subscription', 'type': 'str'},
        'resource_group': {'key': 'properties.resourceGroup', 'type': 'str'},
        'deleted_site_name': {'key': 'properties.deletedSiteName', 'type': 'str'},
        'slot': {'key': 'properties.slot', 'type': 'str'},
        'deleted_site_kind': {'key': 'properties.kind', 'type': 'str'},
    }

    def __init__(self, *, kind: str=None, **kwargs) -> None:
        super(DeletedSite, self).__init__(kind=kind, **kwargs)
        self.deleted_site_id = None
        self.deleted_timestamp = None
        self.subscription = None
        self.resource_group = None
        self.deleted_site_name = None
        self.slot = None
        self.deleted_site_kind = None
