from typing import Dict
from botocore.paginate import Paginator


class ListComplianceStatus(Paginator):
    def paginate(self, PolicyId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListMemberAccounts(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPolicies(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
