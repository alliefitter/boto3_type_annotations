from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_private_dns_namespace(self, Name: str, Vpc: str, CreatorRequestId: str = None, Description: str = None) -> Dict:
        pass

    def create_public_dns_namespace(self, Name: str, CreatorRequestId: str = None, Description: str = None) -> Dict:
        pass

    def create_service(self, Name: str, DnsConfig: Dict, CreatorRequestId: str = None, Description: str = None, HealthCheckConfig: Dict = None, HealthCheckCustomConfig: Dict = None) -> Dict:
        pass

    def delete_namespace(self, Id: str) -> Dict:
        pass

    def delete_service(self, Id: str) -> Dict:
        pass

    def deregister_instance(self, ServiceId: str, InstanceId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_instance(self, ServiceId: str, InstanceId: str) -> Dict:
        pass

    def get_instances_health_status(self, ServiceId: str, Instances: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def get_namespace(self, Id: str) -> Dict:
        pass

    def get_operation(self, OperationId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_service(self, Id: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_instances(self, ServiceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_namespaces(self, NextToken: str = None, MaxResults: int = None, Filters: List = None) -> Dict:
        pass

    def list_operations(self, NextToken: str = None, MaxResults: int = None, Filters: List = None) -> Dict:
        pass

    def list_services(self, NextToken: str = None, MaxResults: int = None, Filters: List = None) -> Dict:
        pass

    def register_instance(self, ServiceId: str, InstanceId: str, Attributes: Dict, CreatorRequestId: str = None) -> Dict:
        pass

    def update_instance_custom_health_status(self, ServiceId: str, InstanceId: str, Status: str):
        pass

    def update_service(self, Id: str, Service: Dict) -> Dict:
        pass
