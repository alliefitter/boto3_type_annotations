from typing import Dict
from typing import List
from botocore.paginate import Paginator


class GetResourcePolicies(Paginator):
    def paginate(self, resourceArns: List, principal: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetResourceShareAssociations(Paginator):
    def paginate(self, associationType: str, resourceShareArns: List = None, resourceArn: str = None, principal: str = None, associationStatus: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetResourceShareInvitations(Paginator):
    def paginate(self, resourceShareInvitationArns: List = None, resourceShareArns: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetResourceShares(Paginator):
    def paginate(self, resourceOwner: str, resourceShareArns: List = None, resourceShareStatus: str = None, name: str = None, tagFilters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPrincipals(Paginator):
    def paginate(self, resourceOwner: str, resourceArn: str = None, principals: List = None, resourceType: str = None, resourceShareArns: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListResources(Paginator):
    def paginate(self, resourceOwner: str, principal: str = None, resourceType: str = None, resourceArns: List = None, resourceShareArns: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
