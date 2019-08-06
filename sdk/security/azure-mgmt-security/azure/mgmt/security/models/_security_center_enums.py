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

from enum import Enum


class ResourceStatus(str, Enum):

    healthy = "Healthy"  #: This assessment on the resource is healthy
    not_applicable = "NotApplicable"  #: This assessment is not applicable to this resource
    off_by_policy = "OffByPolicy"  #: This assessment is turned off by policy on this subscription
    not_healthy = "NotHealthy"  #: This assessment on the resource is not healthy


class PricingTier(str, Enum):

    free = "Free"  #: Get free Azure security center experience with basic security features
    standard = "Standard"  #: Get the standard Azure security center experience with advanced security features


class ReportedSeverity(str, Enum):

    informational = "Informational"
    low = "Low"
    medium = "Medium"
    high = "High"


class SettingKind(str, Enum):

    data_export_setting = "DataExportSetting"
    alert_suppression_setting = "AlertSuppressionSetting"


class SecuritySolutionStatus(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class ExportData(str, Enum):

    raw_events = "RawEvents"  #: Agent raw events


class DataSource(str, Enum):

    twin_data = "TwinData"  #: Devices twin data


class RecommendationType(str, Enum):

    io_t_acrauthentication = "IoT_ACRAuthentication"  #: Authentication schema used for pull an edge module from an ACR repository does not use Service Principal Authentication.
    io_t_agent_sends_unutilized_messages = "IoT_AgentSendsUnutilizedMessages"  #: IoT agent message size capacity is currently underutilized, causing an increase in the number of sent messages. Adjust message intervals for better utilization.
    io_t_baseline = "IoT_Baseline"  #: Identified security related system configuration issues.
    io_t_edge_hub_mem_optimize = "IoT_EdgeHubMemOptimize"  #: You can optimize Edge Hub memory usage by turning off protocol heads for any protocols not used by Edge modules in your solution.
    io_t_edge_logging_options = "IoT_EdgeLoggingOptions"  #: Logging is disabled for this edge module.
    io_t_inconsistent_module_settings = "IoT_InconsistentModuleSettings"  #: A minority within a device security group has inconsistent Edge Module settings with the rest of their group.
    io_t_install_agent = "IoT_InstallAgent"  #: Install the Azure Security of Things Agent.
    io_t_ipfilter_deny_all = "IoT_IPFilter_DenyAll"  #: IP Filter Configuration should have rules defined for allowed traffic and should deny all other traffic by default.
    io_t_ipfilter_permissive_rule = "IoT_IPFilter_PermissiveRule"  #: An Allow IP Filter rules source IP range is too large. Overly permissive rules might expose your IoT hub to malicious intenders.
    io_t_open_ports = "IoT_OpenPorts"  #: A listening endpoint was found on the device.
    io_t_permissive_firewall_policy = "IoT_PermissiveFirewallPolicy"  #: An Allowed firewall policy was found (INPUT/OUTPUT). The policy should Deny all traffic by default and define rules to allow necessary communication to/from the device.
    io_t_permissive_input_firewall_rules = "IoT_PermissiveInputFirewallRules"  #: A rule in the firewall has been found that contains a permissive pattern for a wide range of IP addresses or Ports.
    io_t_permissive_output_firewall_rules = "IoT_PermissiveOutputFirewallRules"  #: A rule in the firewall has been found that contains a permissive pattern for a wide range of IP addresses or Ports.
    io_t_privileged_docker_options = "IoT_PrivilegedDockerOptions"  #: Edge module is configured to run in privileged mode, with extensive Linux capabilities or with host-level network access (send/receive data to host machine).
    io_t_shared_credentials = "IoT_SharedCredentials"  #: Same authentication credentials to the IoT Hub used by multiple devices. This could indicate an illegitimate device impersonating a legitimate device. It also exposes the risk of device impersonation by an attacker.
    io_t_vulnerable_tls_cipher_suite = "IoT_VulnerableTLSCipherSuite"  #: Insecure TLS configurations detected. Immediate upgrade recommended.


class RecommendationConfigStatus(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class SecurityFamily(str, Enum):

    waf = "Waf"
    ngfw = "Ngfw"
    saas_waf = "SaasWaf"
    va = "Va"


class AadConnectivityState(str, Enum):

    discovered = "Discovered"
    not_licensed = "NotLicensed"
    connected = "Connected"


class ExternalSecuritySolutionKind(str, Enum):

    cef = "CEF"
    ata = "ATA"
    aad = "AAD"


class Protocol(str, Enum):

    tcp = "TCP"
    udp = "UDP"
    all = "*"


class Status(str, Enum):

    revoked = "Revoked"
    initiated = "Initiated"


class StatusReason(str, Enum):

    expired = "Expired"
    user_requested = "UserRequested"
    newer_request_initiated = "NewerRequestInitiated"


class AutoProvision(str, Enum):

    on = "On"  #: Install missing security agent on VMs automatically
    off = "Off"  #: Do not install security agent on the VMs automatically


class AlertNotifications(str, Enum):

    on = "On"  #: Get notifications on new alerts
    off = "Off"  #: Don't get notifications on new alerts


class AlertsToAdmins(str, Enum):

    on = "On"  #: Send notification on new alerts to the subscription's admins
    off = "Off"  #: Don't send notification on new alerts to the subscription's admins


class State(str, Enum):

    passed = "Passed"  #: All supported regulatory compliance controls in the given standard have a passed state
    failed = "Failed"  #: At least one supported regulatory compliance control in the given standard has a state of failed
    skipped = "Skipped"  #: All supported regulatory compliance controls in the given standard have a state of skipped
    unsupported = "Unsupported"  #: No supported regulatory compliance data for the given standard


class ConnectionType(str, Enum):

    internal = "Internal"
    external = "External"