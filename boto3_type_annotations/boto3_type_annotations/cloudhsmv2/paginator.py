from typing import Dict
from botocore.paginate import Paginator


class DescribeBackups(Paginator):
    def paginate(self, Filters: Dict = None, SortAscending: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClusters(Paginator):
    def paginate(self, Filters: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTags(Paginator):
    def paginate(self, ResourceId: str, PaginationConfig: Dict = None) -> Dict:
        pass
