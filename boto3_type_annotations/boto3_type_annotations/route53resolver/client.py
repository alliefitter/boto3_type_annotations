from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def associate_resolver_endpoint_ip_address(self, ResolverEndpointId: str, IpAddress: Dict) -> Dict:
        pass

    def associate_resolver_rule(self, ResolverRuleId: str, VPCId: str, Name: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_resolver_endpoint(self, CreatorRequestId: str, SecurityGroupIds: List, Direction: str, IpAddresses: List, Name: str = None, Tags: List = None) -> Dict:
        pass

    def create_resolver_rule(self, CreatorRequestId: str, RuleType: str, DomainName: str, Name: str = None, TargetIps: List = None, ResolverEndpointId: str = None, Tags: List = None) -> Dict:
        pass

    def delete_resolver_endpoint(self, ResolverEndpointId: str) -> Dict:
        pass

    def delete_resolver_rule(self, ResolverRuleId: str) -> Dict:
        pass

    def disassociate_resolver_endpoint_ip_address(self, ResolverEndpointId: str, IpAddress: Dict) -> Dict:
        pass

    def disassociate_resolver_rule(self, VPCId: str, ResolverRuleId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_resolver_endpoint(self, ResolverEndpointId: str) -> Dict:
        pass

    def get_resolver_rule(self, ResolverRuleId: str) -> Dict:
        pass

    def get_resolver_rule_association(self, ResolverRuleAssociationId: str) -> Dict:
        pass

    def get_resolver_rule_policy(self, Arn: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_resolver_endpoint_ip_addresses(self, ResolverEndpointId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_resolver_endpoints(self, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        pass

    def list_resolver_rule_associations(self, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        pass

    def list_resolver_rules(self, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def put_resolver_rule_policy(self, Arn: str, ResolverRulePolicy: str) -> Dict:
        pass

    def tag_resource(self, ResourceArn: str, Tags: List) -> Dict:
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List) -> Dict:
        pass

    def update_resolver_endpoint(self, ResolverEndpointId: str, Name: str = None) -> Dict:
        pass

    def update_resolver_rule(self, ResolverRuleId: str, Config: Dict) -> Dict:
        pass
