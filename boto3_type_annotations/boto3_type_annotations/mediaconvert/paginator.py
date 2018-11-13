from typing import Dict
from botocore.paginate import Paginator


class DescribeEndpoints(Paginator):
    def paginate(self, Mode: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListJobTemplates(Paginator):
    def paginate(self, Category: str = None, ListBy: str = None, Order: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListJobs(Paginator):
    def paginate(self, Order: str = None, Queue: str = None, Status: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPresets(Paginator):
    def paginate(self, Category: str = None, ListBy: str = None, Order: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListQueues(Paginator):
    def paginate(self, ListBy: str = None, Order: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
