from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def add_flow_outputs(self, FlowArn: str, Outputs: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_flow(self, Name: str, Source: Dict, AvailabilityZone: str = None, Entitlements: List = None, Outputs: List = None) -> Dict:
        pass

    def delete_flow(self, FlowArn: str) -> Dict:
        pass

    def describe_flow(self, FlowArn: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def grant_flow_entitlements(self, Entitlements: List, FlowArn: str) -> Dict:
        pass

    def list_entitlements(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_flows(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        pass

    def remove_flow_output(self, FlowArn: str, OutputArn: str) -> Dict:
        pass

    def revoke_flow_entitlement(self, EntitlementArn: str, FlowArn: str) -> Dict:
        pass

    def start_flow(self, FlowArn: str) -> Dict:
        pass

    def stop_flow(self, FlowArn: str) -> Dict:
        pass

    def tag_resource(self, ResourceArn: str, Tags: Dict):
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List):
        pass

    def update_flow_entitlement(self, EntitlementArn: str, FlowArn: str, Description: str = None, Encryption: Dict = None, Subscribers: List = None) -> Dict:
        pass

    def update_flow_output(self, FlowArn: str, OutputArn: str, Description: str = None, Destination: str = None, Encryption: Dict = None, MaxLatency: int = None, Port: int = None, Protocol: str = None, SmoothingLatency: int = None, StreamId: str = None) -> Dict:
        pass

    def update_flow_source(self, FlowArn: str, SourceArn: str, Decryption: Dict = None, Description: str = None, EntitlementArn: str = None, IngestPort: int = None, MaxBitrate: int = None, MaxLatency: int = None, Protocol: str = None, StreamId: str = None, WhitelistCidr: str = None) -> Dict:
        pass
