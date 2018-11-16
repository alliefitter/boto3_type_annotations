from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def associate_ip_groups(self, DirectoryId: str, GroupIds: List) -> Dict:
        pass

    def authorize_ip_rules(self, GroupId: str, UserRules: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_ip_group(self, GroupName: str, GroupDesc: str = None, UserRules: List = None) -> Dict:
        pass

    def create_tags(self, ResourceId: str, Tags: List) -> Dict:
        pass

    def create_workspaces(self, Workspaces: List) -> Dict:
        pass

    def delete_ip_group(self, GroupId: str) -> Dict:
        pass

    def delete_tags(self, ResourceId: str, TagKeys: List) -> Dict:
        pass

    def describe_ip_groups(self, GroupIds: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_tags(self, ResourceId: str) -> Dict:
        pass

    def describe_workspace_bundles(self, BundleIds: List = None, Owner: str = None, NextToken: str = None) -> Dict:
        pass

    def describe_workspace_directories(self, DirectoryIds: List = None, NextToken: str = None) -> Dict:
        pass

    def describe_workspaces(self, WorkspaceIds: List = None, DirectoryId: str = None, UserName: str = None, BundleId: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_workspaces_connection_status(self, WorkspaceIds: List = None, NextToken: str = None) -> Dict:
        pass

    def disassociate_ip_groups(self, DirectoryId: str, GroupIds: List) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def modify_workspace_properties(self, WorkspaceId: str, WorkspaceProperties: Dict) -> Dict:
        pass

    def modify_workspace_state(self, WorkspaceId: str, WorkspaceState: str) -> Dict:
        pass

    def reboot_workspaces(self, RebootWorkspaceRequests: List) -> Dict:
        pass

    def rebuild_workspaces(self, RebuildWorkspaceRequests: List) -> Dict:
        pass

    def revoke_ip_rules(self, GroupId: str, UserRules: List) -> Dict:
        pass

    def start_workspaces(self, StartWorkspaceRequests: List) -> Dict:
        pass

    def stop_workspaces(self, StopWorkspaceRequests: List) -> Dict:
        pass

    def terminate_workspaces(self, TerminateWorkspaceRequests: List) -> Dict:
        pass

    def update_rules_of_ip_group(self, GroupId: str, UserRules: List) -> Dict:
        pass
