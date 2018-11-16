from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def associate_delegate_to_resource(self, OrganizationId: str, ResourceId: str, EntityId: str) -> Dict:
        pass

    def associate_member_to_group(self, OrganizationId: str, GroupId: str, MemberId: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_alias(self, OrganizationId: str, EntityId: str, Alias: str) -> Dict:
        pass

    def create_group(self, OrganizationId: str, Name: str) -> Dict:
        pass

    def create_resource(self, OrganizationId: str, Name: str, Type: str) -> Dict:
        pass

    def create_user(self, OrganizationId: str, Name: str, DisplayName: str, Password: str) -> Dict:
        pass

    def delete_alias(self, OrganizationId: str, EntityId: str, Alias: str) -> Dict:
        pass

    def delete_group(self, OrganizationId: str, GroupId: str) -> Dict:
        pass

    def delete_mailbox_permissions(self, OrganizationId: str, EntityId: str, GranteeId: str) -> Dict:
        pass

    def delete_resource(self, OrganizationId: str, ResourceId: str) -> Dict:
        pass

    def delete_user(self, OrganizationId: str, UserId: str) -> Dict:
        pass

    def deregister_from_work_mail(self, OrganizationId: str, EntityId: str) -> Dict:
        pass

    def describe_group(self, OrganizationId: str, GroupId: str) -> Dict:
        pass

    def describe_organization(self, OrganizationId: str) -> Dict:
        pass

    def describe_resource(self, OrganizationId: str, ResourceId: str) -> Dict:
        pass

    def describe_user(self, OrganizationId: str, UserId: str) -> Dict:
        pass

    def disassociate_delegate_from_resource(self, OrganizationId: str, ResourceId: str, EntityId: str) -> Dict:
        pass

    def disassociate_member_from_group(self, OrganizationId: str, GroupId: str, MemberId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_aliases(self, OrganizationId: str, EntityId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_group_members(self, OrganizationId: str, GroupId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_groups(self, OrganizationId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_mailbox_permissions(self, OrganizationId: str, EntityId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_organizations(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_resource_delegates(self, OrganizationId: str, ResourceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_resources(self, OrganizationId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_users(self, OrganizationId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def put_mailbox_permissions(self, OrganizationId: str, EntityId: str, GranteeId: str, PermissionValues: List) -> Dict:
        pass

    def register_to_work_mail(self, OrganizationId: str, EntityId: str, Email: str) -> Dict:
        pass

    def reset_password(self, OrganizationId: str, UserId: str, Password: str) -> Dict:
        pass

    def update_primary_email_address(self, OrganizationId: str, EntityId: str, Email: str) -> Dict:
        pass

    def update_resource(self, OrganizationId: str, ResourceId: str, Name: str = None, BookingOptions: Dict = None) -> Dict:
        pass
