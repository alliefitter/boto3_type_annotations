from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def associate_vpc_with_hosted_zone(self, HostedZoneId: str, VPC: Dict, Comment: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def change_resource_record_sets(self, HostedZoneId: str, ChangeBatch: Dict) -> Dict:
        pass

    def change_tags_for_resource(self, ResourceType: str, ResourceId: str, AddTags: List = None, RemoveTagKeys: List = None) -> Dict:
        pass

    def create_health_check(self, CallerReference: str, HealthCheckConfig: Dict) -> Dict:
        pass

    def create_hosted_zone(self, Name: str, CallerReference: str, VPC: Dict = None, HostedZoneConfig: Dict = None, DelegationSetId: str = None) -> Dict:
        pass

    def create_query_logging_config(self, HostedZoneId: str, CloudWatchLogsLogGroupArn: str) -> Dict:
        pass

    def create_reusable_delegation_set(self, CallerReference: str, HostedZoneId: str = None) -> Dict:
        pass

    def create_traffic_policy(self, Name: str, Document: str, Comment: str = None) -> Dict:
        pass

    def create_traffic_policy_instance(self, HostedZoneId: str, Name: str, TTL: int, TrafficPolicyId: str, TrafficPolicyVersion: int) -> Dict:
        pass

    def create_traffic_policy_version(self, Id: str, Document: str, Comment: str = None) -> Dict:
        pass

    def create_vpc_association_authorization(self, HostedZoneId: str, VPC: Dict) -> Dict:
        pass

    def delete_health_check(self, HealthCheckId: str) -> Dict:
        pass

    def delete_hosted_zone(self, Id: str) -> Dict:
        pass

    def delete_query_logging_config(self, Id: str) -> Dict:
        pass

    def delete_reusable_delegation_set(self, Id: str) -> Dict:
        pass

    def delete_traffic_policy(self, Id: str, Version: int) -> Dict:
        pass

    def delete_traffic_policy_instance(self, Id: str) -> Dict:
        pass

    def delete_vpc_association_authorization(self, HostedZoneId: str, VPC: Dict) -> Dict:
        pass

    def disassociate_vpc_from_hosted_zone(self, HostedZoneId: str, VPC: Dict, Comment: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_account_limit(self, Type: str) -> Dict:
        pass

    def get_change(self, Id: str) -> Dict:
        pass

    def get_checker_ip_ranges(self) -> Dict:
        pass

    def get_geo_location(self, ContinentCode: str = None, CountryCode: str = None, SubdivisionCode: str = None) -> Dict:
        pass

    def get_health_check(self, HealthCheckId: str) -> Dict:
        pass

    def get_health_check_count(self) -> Dict:
        pass

    def get_health_check_last_failure_reason(self, HealthCheckId: str) -> Dict:
        pass

    def get_health_check_status(self, HealthCheckId: str) -> Dict:
        pass

    def get_hosted_zone(self, Id: str) -> Dict:
        pass

    def get_hosted_zone_count(self) -> Dict:
        pass

    def get_hosted_zone_limit(self, Type: str, HostedZoneId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_query_logging_config(self, Id: str) -> Dict:
        pass

    def get_reusable_delegation_set(self, Id: str) -> Dict:
        pass

    def get_reusable_delegation_set_limit(self, Type: str, DelegationSetId: str) -> Dict:
        pass

    def get_traffic_policy(self, Id: str, Version: int) -> Dict:
        pass

    def get_traffic_policy_instance(self, Id: str) -> Dict:
        pass

    def get_traffic_policy_instance_count(self) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_geo_locations(self, StartContinentCode: str = None, StartCountryCode: str = None, StartSubdivisionCode: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_health_checks(self, Marker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_hosted_zones(self, Marker: str = None, MaxItems: str = None, DelegationSetId: str = None) -> Dict:
        pass

    def list_hosted_zones_by_name(self, DNSName: str = None, HostedZoneId: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_query_logging_configs(self, HostedZoneId: str = None, NextToken: str = None, MaxResults: str = None) -> Dict:
        pass

    def list_resource_record_sets(self, HostedZoneId: str, StartRecordName: str = None, StartRecordType: str = None, StartRecordIdentifier: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_reusable_delegation_sets(self, Marker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceType: str, ResourceId: str) -> Dict:
        pass

    def list_tags_for_resources(self, ResourceType: str, ResourceIds: List) -> Dict:
        pass

    def list_traffic_policies(self, TrafficPolicyIdMarker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_traffic_policy_instances(self, HostedZoneIdMarker: str = None, TrafficPolicyInstanceNameMarker: str = None, TrafficPolicyInstanceTypeMarker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_traffic_policy_instances_by_hosted_zone(self, HostedZoneId: str, TrafficPolicyInstanceNameMarker: str = None, TrafficPolicyInstanceTypeMarker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_traffic_policy_instances_by_policy(self, TrafficPolicyId: str, TrafficPolicyVersion: int, HostedZoneIdMarker: str = None, TrafficPolicyInstanceNameMarker: str = None, TrafficPolicyInstanceTypeMarker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_traffic_policy_versions(self, Id: str, TrafficPolicyVersionMarker: str = None, MaxItems: str = None) -> Dict:
        pass

    def list_vpc_association_authorizations(self, HostedZoneId: str, NextToken: str = None, MaxResults: str = None) -> Dict:
        pass

    def test_dns_answer(self, HostedZoneId: str, RecordName: str, RecordType: str, ResolverIP: str = None, EDNS0ClientSubnetIP: str = None, EDNS0ClientSubnetMask: str = None) -> Dict:
        pass

    def update_health_check(self, HealthCheckId: str, HealthCheckVersion: int = None, IPAddress: str = None, Port: int = None, ResourcePath: str = None, FullyQualifiedDomainName: str = None, SearchString: str = None, FailureThreshold: int = None, Inverted: bool = None, Disabled: bool = None, HealthThreshold: int = None, ChildHealthChecks: List = None, EnableSNI: bool = None, Regions: List = None, AlarmIdentifier: Dict = None, InsufficientDataHealthStatus: str = None, ResetElements: List = None) -> Dict:
        pass

    def update_hosted_zone_comment(self, Id: str, Comment: str = None) -> Dict:
        pass

    def update_traffic_policy_comment(self, Id: str, Version: int, Comment: str) -> Dict:
        pass

    def update_traffic_policy_instance(self, Id: str, TTL: int, TrafficPolicyId: str, TrafficPolicyVersion: int) -> Dict:
        pass
