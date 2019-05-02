from typing import Dict
from datetime import datetime
from botocore.paginate import Paginator


class ListDomains(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListOperations(Paginator):
    def paginate(self, SubmittedSince: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ViewBilling(Paginator):
    def paginate(self, Start: datetime = None, End: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass
