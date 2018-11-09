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


class DPMProtectedItemExtendedInfo(Model):
    """Additional information of DPM Protected item.

    :param protectable_object_load_path: Attribute to provide information on
     various DBs.
    :type protectable_object_load_path: dict[str, str]
    :param protected: To check if backup item is disk protected.
    :type protected: bool
    :param is_present_on_cloud: To check if backup item is cloud protected.
    :type is_present_on_cloud: bool
    :param last_backup_status: Last backup status information on backup item.
    :type last_backup_status: str
    :param last_refreshed_at: Last refresh time on backup item.
    :type last_refreshed_at: datetime
    :param oldest_recovery_point: Oldest cloud recovery point time.
    :type oldest_recovery_point: datetime
    :param recovery_point_count: cloud recovery point count.
    :type recovery_point_count: int
    :param on_premise_oldest_recovery_point: Oldest disk recovery point time.
    :type on_premise_oldest_recovery_point: datetime
    :param on_premise_latest_recovery_point: latest disk recovery point time.
    :type on_premise_latest_recovery_point: datetime
    :param on_premise_recovery_point_count: disk recovery point count.
    :type on_premise_recovery_point_count: int
    :param is_collocated: To check if backup item is collocated.
    :type is_collocated: bool
    :param protection_group_name: Protection group name of the backup item.
    :type protection_group_name: str
    :param disk_storage_used_in_bytes: Used Disk storage in bytes.
    :type disk_storage_used_in_bytes: str
    :param total_disk_storage_size_in_bytes: total Disk storage in bytes.
    :type total_disk_storage_size_in_bytes: str
    """

    _attribute_map = {
        'protectable_object_load_path': {'key': 'protectableObjectLoadPath', 'type': '{str}'},
        'protected': {'key': 'protected', 'type': 'bool'},
        'is_present_on_cloud': {'key': 'isPresentOnCloud', 'type': 'bool'},
        'last_backup_status': {'key': 'lastBackupStatus', 'type': 'str'},
        'last_refreshed_at': {'key': 'lastRefreshedAt', 'type': 'iso-8601'},
        'oldest_recovery_point': {'key': 'oldestRecoveryPoint', 'type': 'iso-8601'},
        'recovery_point_count': {'key': 'recoveryPointCount', 'type': 'int'},
        'on_premise_oldest_recovery_point': {'key': 'onPremiseOldestRecoveryPoint', 'type': 'iso-8601'},
        'on_premise_latest_recovery_point': {'key': 'onPremiseLatestRecoveryPoint', 'type': 'iso-8601'},
        'on_premise_recovery_point_count': {'key': 'onPremiseRecoveryPointCount', 'type': 'int'},
        'is_collocated': {'key': 'isCollocated', 'type': 'bool'},
        'protection_group_name': {'key': 'protectionGroupName', 'type': 'str'},
        'disk_storage_used_in_bytes': {'key': 'diskStorageUsedInBytes', 'type': 'str'},
        'total_disk_storage_size_in_bytes': {'key': 'totalDiskStorageSizeInBytes', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DPMProtectedItemExtendedInfo, self).__init__(**kwargs)
        self.protectable_object_load_path = kwargs.get('protectable_object_load_path', None)
        self.protected = kwargs.get('protected', None)
        self.is_present_on_cloud = kwargs.get('is_present_on_cloud', None)
        self.last_backup_status = kwargs.get('last_backup_status', None)
        self.last_refreshed_at = kwargs.get('last_refreshed_at', None)
        self.oldest_recovery_point = kwargs.get('oldest_recovery_point', None)
        self.recovery_point_count = kwargs.get('recovery_point_count', None)
        self.on_premise_oldest_recovery_point = kwargs.get('on_premise_oldest_recovery_point', None)
        self.on_premise_latest_recovery_point = kwargs.get('on_premise_latest_recovery_point', None)
        self.on_premise_recovery_point_count = kwargs.get('on_premise_recovery_point_count', None)
        self.is_collocated = kwargs.get('is_collocated', None)
        self.protection_group_name = kwargs.get('protection_group_name', None)
        self.disk_storage_used_in_bytes = kwargs.get('disk_storage_used_in_bytes', None)
        self.total_disk_storage_size_in_bytes = kwargs.get('total_disk_storage_size_in_bytes', None)
