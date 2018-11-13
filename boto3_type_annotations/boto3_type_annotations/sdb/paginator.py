from typing import Dict
from botocore.paginate import Paginator


class ListDomains(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class Select(Paginator):
    def paginate(self, SelectExpression: str, ConsistentRead: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass
