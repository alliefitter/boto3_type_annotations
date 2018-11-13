from typing import Dict
from botocore.paginate import Paginator


class ListAliases(Paginator):
    def paginate(self, KeyId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListGrants(Paginator):
    def paginate(self, KeyId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListKeyPolicies(Paginator):
    def paginate(self, KeyId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListKeys(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
