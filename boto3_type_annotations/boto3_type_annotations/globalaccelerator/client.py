from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_accelerator(self, Name: str, IdempotencyToken: str, IpAddressType: str = None, Enabled: bool = None) -> Dict:
        pass

    def create_endpoint_group(self, ListenerArn: str, EndpointGroupRegion: str, IdempotencyToken: str, EndpointConfigurations: List = None, TrafficDialPercentage: float = None, HealthCheckPort: int = None, HealthCheckProtocol: str = None, HealthCheckPath: str = None, HealthCheckIntervalSeconds: int = None, ThresholdCount: int = None) -> Dict:
        pass

    def create_listener(self, AcceleratorArn: str, PortRanges: List, Protocol: str, IdempotencyToken: str, ClientAffinity: str = None) -> Dict:
        pass

    def delete_accelerator(self, AcceleratorArn: str):
        pass

    def delete_endpoint_group(self, EndpointGroupArn: str):
        pass

    def delete_listener(self, ListenerArn: str):
        pass

    def describe_accelerator(self, AcceleratorArn: str) -> Dict:
        pass

    def describe_accelerator_attributes(self, AcceleratorArn: str = None) -> Dict:
        pass

    def describe_endpoint_group(self, EndpointGroupArn: str) -> Dict:
        pass

    def describe_listener(self, ListenerArn: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_accelerators(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_endpoint_groups(self, ListenerArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_listeners(self, AcceleratorArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def update_accelerator(self, AcceleratorArn: str, Name: str = None, IpAddressType: str = None, Enabled: bool = None) -> Dict:
        pass

    def update_accelerator_attributes(self, AcceleratorArn: str = None, FlowLogsEnabled: bool = None, FlowLogsS3Bucket: str = None, FlowLogsS3Prefix: str = None) -> Dict:
        pass

    def update_endpoint_group(self, EndpointGroupArn: str, EndpointConfigurations: List = None, TrafficDialPercentage: float = None, HealthCheckPort: int = None, HealthCheckProtocol: str = None, HealthCheckPath: str = None, HealthCheckIntervalSeconds: int = None, ThresholdCount: int = None) -> Dict:
        pass

    def update_listener(self, ListenerArn: str, PortRanges: List = None, Protocol: str = None, ClientAffinity: str = None) -> Dict:
        pass
