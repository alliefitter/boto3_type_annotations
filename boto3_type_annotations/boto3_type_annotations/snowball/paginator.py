from typing import Dict
from botocore.paginate import Paginator


class DescribeAddresses(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListClusterJobs(Paginator):
    def paginate(self, ClusterId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListClusters(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCompatibleImages(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListJobs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
