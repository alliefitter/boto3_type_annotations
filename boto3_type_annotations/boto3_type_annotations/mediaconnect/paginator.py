from typing import Dict
from botocore.paginate import Paginator


class ListEntitlements(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListFlows(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
