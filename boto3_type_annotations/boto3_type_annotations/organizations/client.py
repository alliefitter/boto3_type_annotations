from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def accept_handshake(self, HandshakeId: str) -> Dict:
        pass

    def attach_policy(self, PolicyId: str, TargetId: str):
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def cancel_handshake(self, HandshakeId: str) -> Dict:
        pass

    def create_account(self, Email: str, AccountName: str, RoleName: str = None, IamUserAccessToBilling: str = None) -> Dict:
        pass

    def create_organization(self, FeatureSet: str = None) -> Dict:
        pass

    def create_organizational_unit(self, ParentId: str, Name: str) -> Dict:
        pass

    def create_policy(self, Content: str, Description: str, Name: str, Type: str) -> Dict:
        pass

    def decline_handshake(self, HandshakeId: str) -> Dict:
        pass

    def delete_organization(self):
        pass

    def delete_organizational_unit(self, OrganizationalUnitId: str):
        pass

    def delete_policy(self, PolicyId: str):
        pass

    def describe_account(self, AccountId: str) -> Dict:
        pass

    def describe_create_account_status(self, CreateAccountRequestId: str) -> Dict:
        pass

    def describe_handshake(self, HandshakeId: str) -> Dict:
        pass

    def describe_organization(self) -> Dict:
        pass

    def describe_organizational_unit(self, OrganizationalUnitId: str) -> Dict:
        pass

    def describe_policy(self, PolicyId: str) -> Dict:
        pass

    def detach_policy(self, PolicyId: str, TargetId: str):
        pass

    def disable_aws_service_access(self, ServicePrincipal: str):
        pass

    def disable_policy_type(self, RootId: str, PolicyType: str) -> Dict:
        pass

    def enable_all_features(self) -> Dict:
        pass

    def enable_aws_service_access(self, ServicePrincipal: str):
        pass

    def enable_policy_type(self, RootId: str, PolicyType: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def invite_account_to_organization(self, Target: Dict, Notes: str = None) -> Dict:
        pass

    def leave_organization(self):
        pass

    def list_accounts(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_accounts_for_parent(self, ParentId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_aws_service_access_for_organization(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_children(self, ParentId: str, ChildType: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_create_account_status(self, States: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_handshakes_for_account(self, Filter: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_handshakes_for_organization(self, Filter: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_organizational_units_for_parent(self, ParentId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_parents(self, ChildId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_policies(self, Filter: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_policies_for_target(self, TargetId: str, Filter: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_roots(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_targets_for_policy(self, PolicyId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def move_account(self, AccountId: str, SourceParentId: str, DestinationParentId: str):
        pass

    def remove_account_from_organization(self, AccountId: str):
        pass

    def update_organizational_unit(self, OrganizationalUnitId: str, Name: str = None) -> Dict:
        pass

    def update_policy(self, PolicyId: str, Name: str = None, Description: str = None, Content: str = None) -> Dict:
        pass
