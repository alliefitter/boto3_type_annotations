from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def accept_resource_share_invitation(self, resourceShareInvitationArn: str, clientToken: str = None) -> Dict:
        pass

    def associate_resource_share(self, resourceShareArn: str, resourceArns: List = None, principals: List = None, clientToken: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_resource_share(self, name: str, resourceArns: List = None, principals: List = None, tags: List = None, allowExternalPrincipals: bool = None, clientToken: str = None) -> Dict:
        pass

    def delete_resource_share(self, resourceShareArn: str, clientToken: str = None) -> Dict:
        pass

    def disassociate_resource_share(self, resourceShareArn: str, resourceArns: List = None, principals: List = None, clientToken: str = None) -> Dict:
        pass

    def enable_sharing_with_aws_organization(self) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_resource_policies(self, resourceArns: List, principal: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_resource_share_associations(self, associationType: str, resourceShareArns: List = None, resourceArn: str = None, principal: str = None, associationStatus: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_resource_share_invitations(self, resourceShareInvitationArns: List = None, resourceShareArns: List = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_resource_shares(self, resourceOwner: str, resourceShareArns: List = None, resourceShareStatus: str = None, name: str = None, tagFilters: List = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_principals(self, resourceOwner: str, resourceArn: str = None, principals: List = None, resourceType: str = None, resourceShareArns: List = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_resources(self, resourceOwner: str, principal: str = None, resourceType: str = None, resourceArns: List = None, resourceShareArns: List = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def reject_resource_share_invitation(self, resourceShareInvitationArn: str, clientToken: str = None) -> Dict:
        pass

    def tag_resource(self, resourceShareArn: str, tags: List) -> Dict:
        pass

    def untag_resource(self, resourceShareArn: str, tagKeys: List) -> Dict:
        pass

    def update_resource_share(self, resourceShareArn: str, name: str = None, allowExternalPrincipals: bool = None, clientToken: str = None) -> Dict:
        pass
