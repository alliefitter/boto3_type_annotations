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

    def create_identity_pool(self, IdentityPoolName: str, AllowUnauthenticatedIdentities: bool, SupportedLoginProviders: Dict = None, DeveloperProviderName: str = None, OpenIdConnectProviderARNs: List = None, CognitoIdentityProviders: List = None, SamlProviderARNs: List = None) -> Dict:
        pass

    def delete_identities(self, IdentityIdsToDelete: List) -> Dict:
        pass

    def delete_identity_pool(self, IdentityPoolId: str):
        pass

    def describe_identity(self, IdentityId: str) -> Dict:
        pass

    def describe_identity_pool(self, IdentityPoolId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_credentials_for_identity(self, IdentityId: str, Logins: Dict = None, CustomRoleArn: str = None) -> Dict:
        pass

    def get_id(self, IdentityPoolId: str, AccountId: str = None, Logins: Dict = None) -> Dict:
        pass

    def get_identity_pool_roles(self, IdentityPoolId: str) -> Dict:
        pass

    def get_open_id_token(self, IdentityId: str, Logins: Dict = None) -> Dict:
        pass

    def get_open_id_token_for_developer_identity(self, IdentityPoolId: str, Logins: Dict, IdentityId: str = None, TokenDuration: int = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_identities(self, IdentityPoolId: str, MaxResults: int, NextToken: str = None, HideDisabled: bool = None) -> Dict:
        pass

    def list_identity_pools(self, MaxResults: int, NextToken: str = None) -> Dict:
        pass

    def lookup_developer_identity(self, IdentityPoolId: str, IdentityId: str = None, DeveloperUserIdentifier: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def merge_developer_identities(self, SourceUserIdentifier: str, DestinationUserIdentifier: str, DeveloperProviderName: str, IdentityPoolId: str) -> Dict:
        pass

    def set_identity_pool_roles(self, IdentityPoolId: str, Roles: Dict, RoleMappings: Dict = None):
        pass

    def unlink_developer_identity(self, IdentityId: str, IdentityPoolId: str, DeveloperProviderName: str, DeveloperUserIdentifier: str):
        pass

    def unlink_identity(self, IdentityId: str, Logins: Dict, LoginsToRemove: List):
        pass

    def update_identity_pool(self, IdentityPoolId: str, IdentityPoolName: str, AllowUnauthenticatedIdentities: bool, SupportedLoginProviders: Dict = None, DeveloperProviderName: str = None, OpenIdConnectProviderARNs: List = None, CognitoIdentityProviders: List = None, SamlProviderARNs: List = None) -> Dict:
        pass
