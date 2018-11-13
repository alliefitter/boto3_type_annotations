from typing import Dict
from botocore.paginate import Paginator


class DescribeAddresses(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListJobs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
