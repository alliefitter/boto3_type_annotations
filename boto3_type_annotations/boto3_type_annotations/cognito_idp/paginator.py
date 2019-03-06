from typing import Dict
from botocore.paginate import Paginator


class AdminListGroupsForUser(Paginator):
    def paginate(self, Username: str, UserPoolId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class AdminListUserAuthEvents(Paginator):
    def paginate(self, UserPoolId: str, Username: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListGroups(Paginator):
    def paginate(self, UserPoolId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListIdentityProviders(Paginator):
    def paginate(self, UserPoolId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListResourceServers(Paginator):
    def paginate(self, UserPoolId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListUserPoolClients(Paginator):
    def paginate(self, UserPoolId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListUserPools(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListUsersInGroup(Paginator):
    def paginate(self, UserPoolId: str, GroupName: str, PaginationConfig: Dict = None) -> Dict:
        pass
