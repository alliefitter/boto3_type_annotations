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

    def create_server(self, EndpointDetails: Dict = None, EndpointType: str = None, HostKey: str = None, IdentityProviderDetails: Dict = None, IdentityProviderType: str = None, LoggingRole: str = None, Tags: List = None) -> Dict:
        pass

    def create_user(self, Role: str, ServerId: str, UserName: str, HomeDirectory: str = None, Policy: str = None, SshPublicKeyBody: str = None, Tags: List = None) -> Dict:
        pass

    def delete_server(self, ServerId: str):
        pass

    def delete_ssh_public_key(self, ServerId: str, SshPublicKeyId: str, UserName: str):
        pass

    def delete_user(self, ServerId: str, UserName: str):
        pass

    def describe_server(self, ServerId: str) -> Dict:
        pass

    def describe_user(self, ServerId: str, UserName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def import_ssh_public_key(self, ServerId: str, SshPublicKeyBody: str, UserName: str) -> Dict:
        pass

    def list_servers(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_tags_for_resource(self, Arn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_users(self, ServerId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def start_server(self, ServerId: str):
        pass

    def stop_server(self, ServerId: str):
        pass

    def tag_resource(self, Arn: str, Tags: List):
        pass

    def test_identity_provider(self, ServerId: str, UserName: str, UserPassword: str = None) -> Dict:
        pass

    def untag_resource(self, Arn: str, TagKeys: List):
        pass

    def update_server(self, ServerId: str, EndpointDetails: Dict = None, EndpointType: str = None, HostKey: str = None, IdentityProviderDetails: Dict = None, LoggingRole: str = None) -> Dict:
        pass

    def update_user(self, ServerId: str, UserName: str, HomeDirectory: str = None, Policy: str = None, Role: str = None) -> Dict:
        pass
