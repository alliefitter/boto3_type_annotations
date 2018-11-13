from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListAWSServiceAccessForOrganization(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAccounts(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAccountsForParent(Paginator):
    def paginate(self, ParentId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListChildren(Paginator):
    def paginate(self, ParentId: str, ChildType: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCreateAccountStatus(Paginator):
    def paginate(self, States: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListHandshakesForAccount(Paginator):
    def paginate(self, Filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListHandshakesForOrganization(Paginator):
    def paginate(self, Filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListOrganizationalUnitsForParent(Paginator):
    def paginate(self, ParentId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListParents(Paginator):
    def paginate(self, ChildId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPolicies(Paginator):
    def paginate(self, Filter: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPoliciesForTarget(Paginator):
    def paginate(self, TargetId: str, Filter: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRoots(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTargetsForPolicy(Paginator):
    def paginate(self, PolicyId: str, PaginationConfig: Dict = None) -> Dict:
        pass
