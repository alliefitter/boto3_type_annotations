from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def add_tags(self, LoadBalancerNames: List, Tags: List) -> Dict:
        pass

    def apply_security_groups_to_load_balancer(self, LoadBalancerName: str, SecurityGroups: List) -> Dict:
        pass

    def attach_load_balancer_to_subnets(self, LoadBalancerName: str, Subnets: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def configure_health_check(self, LoadBalancerName: str, HealthCheck: Dict) -> Dict:
        pass

    def create_app_cookie_stickiness_policy(self, LoadBalancerName: str, PolicyName: str, CookieName: str) -> Dict:
        pass

    def create_lb_cookie_stickiness_policy(self, LoadBalancerName: str, PolicyName: str, CookieExpirationPeriod: int = None) -> Dict:
        pass

    def create_load_balancer(self, LoadBalancerName: str, Listeners: List, AvailabilityZones: List = None, Subnets: List = None, SecurityGroups: List = None, Scheme: str = None, Tags: List = None) -> Dict:
        pass

    def create_load_balancer_listeners(self, LoadBalancerName: str, Listeners: List) -> Dict:
        pass

    def create_load_balancer_policy(self, LoadBalancerName: str, PolicyName: str, PolicyTypeName: str, PolicyAttributes: List = None) -> Dict:
        pass

    def delete_load_balancer(self, LoadBalancerName: str) -> Dict:
        pass

    def delete_load_balancer_listeners(self, LoadBalancerName: str, LoadBalancerPorts: List) -> Dict:
        pass

    def delete_load_balancer_policy(self, LoadBalancerName: str, PolicyName: str) -> Dict:
        pass

    def deregister_instances_from_load_balancer(self, LoadBalancerName: str, Instances: List) -> Dict:
        pass

    def describe_account_limits(self, Marker: str = None, PageSize: int = None) -> Dict:
        pass

    def describe_instance_health(self, LoadBalancerName: str, Instances: List = None) -> Dict:
        pass

    def describe_load_balancer_attributes(self, LoadBalancerName: str) -> Dict:
        pass

    def describe_load_balancer_policies(self, LoadBalancerName: str = None, PolicyNames: List = None) -> Dict:
        pass

    def describe_load_balancer_policy_types(self, PolicyTypeNames: List = None) -> Dict:
        pass

    def describe_load_balancers(self, LoadBalancerNames: List = None, Marker: str = None, PageSize: int = None) -> Dict:
        pass

    def describe_tags(self, LoadBalancerNames: List) -> Dict:
        pass

    def detach_load_balancer_from_subnets(self, LoadBalancerName: str, Subnets: List) -> Dict:
        pass

    def disable_availability_zones_for_load_balancer(self, LoadBalancerName: str, AvailabilityZones: List) -> Dict:
        pass

    def enable_availability_zones_for_load_balancer(self, LoadBalancerName: str, AvailabilityZones: List) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def modify_load_balancer_attributes(self, LoadBalancerName: str, LoadBalancerAttributes: Dict) -> Dict:
        pass

    def register_instances_with_load_balancer(self, LoadBalancerName: str, Instances: List) -> Dict:
        pass

    def remove_tags(self, LoadBalancerNames: List, Tags: List) -> Dict:
        pass

    def set_load_balancer_listener_ssl_certificate(self, LoadBalancerName: str, LoadBalancerPort: int, SSLCertificateId: str) -> Dict:
        pass

    def set_load_balancer_policies_for_backend_server(self, LoadBalancerName: str, InstancePort: int, PolicyNames: List) -> Dict:
        pass

    def set_load_balancer_policies_of_listener(self, LoadBalancerName: str, LoadBalancerPort: int, PolicyNames: List) -> Dict:
        pass
