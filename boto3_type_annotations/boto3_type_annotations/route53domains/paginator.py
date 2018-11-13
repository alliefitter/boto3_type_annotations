from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class ListDomains(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListOperations(Paginator):
    def paginate(self, SubmittedSince: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass
