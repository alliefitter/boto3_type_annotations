from typing import Dict
from botocore.paginate import Paginator


class ListAccounts(Paginator):
    def paginate(self, Name: str = None, UserEmail: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListUsers(Paginator):
    def paginate(self, AccountId: str, UserEmail: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
