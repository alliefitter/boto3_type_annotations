from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def add_listener_certificates(self, ListenerArn: str, Certificates: List) -> Dict:
        pass

    def add_tags(self, ResourceArns: List, Tags: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_listener(self, LoadBalancerArn: str, Protocol: str, Port: int, DefaultActions: List, SslPolicy: str = None, Certificates: List = None) -> Dict:
        pass

    def create_load_balancer(self, Name: str, Subnets: List = None, SubnetMappings: List = None, SecurityGroups: List = None, Scheme: str = None, Tags: List = None, Type: str = None, IpAddressType: str = None) -> Dict:
        pass

    def create_rule(self, ListenerArn: str, Conditions: List, Priority: int, Actions: List) -> Dict:
        pass

    def create_target_group(self, Name: str, Protocol: str, Port: int, VpcId: str, HealthCheckProtocol: str = None, HealthCheckPort: str = None, HealthCheckPath: str = None, HealthCheckIntervalSeconds: int = None, HealthCheckTimeoutSeconds: int = None, HealthyThresholdCount: int = None, UnhealthyThresholdCount: int = None, Matcher: Dict = None, TargetType: str = None) -> Dict:
        pass

    def delete_listener(self, ListenerArn: str) -> Dict:
        pass

    def delete_load_balancer(self, LoadBalancerArn: str) -> Dict:
        pass

    def delete_rule(self, RuleArn: str) -> Dict:
        pass

    def delete_target_group(self, TargetGroupArn: str) -> Dict:
        pass

    def deregister_targets(self, TargetGroupArn: str, Targets: List) -> Dict:
        pass

    def describe_account_limits(self, Marker: str = None, PageSize: int = None) -> Dict:
        pass

    def describe_listener_certificates(self, ListenerArn: str, Marker: str = None, PageSize: int = None) -> Dict:
        pass

    def describe_listeners(self, LoadBalancerArn: str = None, ListenerArns: List = None, Marker: str = None, PageSize: int = None) -> Dict:
        pass

    def describe_load_balancer_attributes(self, LoadBalancerArn: str) -> Dict:
        pass

    def describe_load_balancers(self, LoadBalancerArns: List = None, Names: List = None, Marker: str = None, PageSize: int = None) -> Dict:
        pass

    def describe_rules(self, ListenerArn: str = None, RuleArns: List = None, Marker: str = None, PageSize: int = None) -> Dict:
        pass

    def describe_ssl_policies(self, Names: List = None, Marker: str = None, PageSize: int = None) -> Dict:
        pass

    def describe_tags(self, ResourceArns: List) -> Dict:
        pass

    def describe_target_group_attributes(self, TargetGroupArn: str) -> Dict:
        pass

    def describe_target_groups(self, LoadBalancerArn: str = None, TargetGroupArns: List = None, Names: List = None, Marker: str = None, PageSize: int = None) -> Dict:
        pass

    def describe_target_health(self, TargetGroupArn: str, Targets: List = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def modify_listener(self, ListenerArn: str, Port: int = None, Protocol: str = None, SslPolicy: str = None, Certificates: List = None, DefaultActions: List = None) -> Dict:
        pass

    def modify_load_balancer_attributes(self, LoadBalancerArn: str, Attributes: List) -> Dict:
        pass

    def modify_rule(self, RuleArn: str, Conditions: List = None, Actions: List = None) -> Dict:
        pass

    def modify_target_group(self, TargetGroupArn: str, HealthCheckProtocol: str = None, HealthCheckPort: str = None, HealthCheckPath: str = None, HealthCheckIntervalSeconds: int = None, HealthCheckTimeoutSeconds: int = None, HealthyThresholdCount: int = None, UnhealthyThresholdCount: int = None, Matcher: Dict = None) -> Dict:
        pass

    def modify_target_group_attributes(self, TargetGroupArn: str, Attributes: List) -> Dict:
        pass

    def register_targets(self, TargetGroupArn: str, Targets: List) -> Dict:
        pass

    def remove_listener_certificates(self, ListenerArn: str, Certificates: List) -> Dict:
        pass

    def remove_tags(self, ResourceArns: List, TagKeys: List) -> Dict:
        pass

    def set_ip_address_type(self, LoadBalancerArn: str, IpAddressType: str) -> Dict:
        pass

    def set_rule_priorities(self, RulePriorities: List) -> Dict:
        pass

    def set_security_groups(self, LoadBalancerArn: str, SecurityGroups: List) -> Dict:
        pass

    def set_subnets(self, LoadBalancerArn: str, Subnets: List = None, SubnetMappings: List = None) -> Dict:
        pass
