from typing import Dict
from botocore.paginate import Paginator


class ListAliases(Paginator):
    def paginate(self, OrganizationId: str, EntityId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListGroupMembers(Paginator):
    def paginate(self, OrganizationId: str, GroupId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListGroups(Paginator):
    def paginate(self, OrganizationId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListOrganizations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListResources(Paginator):
    def paginate(self, OrganizationId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListUsers(Paginator):
    def paginate(self, OrganizationId: str, PaginationConfig: Dict = None) -> Dict:
        pass
