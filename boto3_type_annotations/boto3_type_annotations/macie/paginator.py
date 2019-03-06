from typing import Dict
from botocore.paginate import Paginator


class ListMemberAccounts(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListS3Resources(Paginator):
    def paginate(self, memberAccountId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
