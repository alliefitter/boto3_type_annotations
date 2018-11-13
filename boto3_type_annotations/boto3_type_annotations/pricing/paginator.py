from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeServices(Paginator):
    def paginate(self, ServiceCode: str = None, FormatVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetAttributeValues(Paginator):
    def paginate(self, ServiceCode: str, AttributeName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class GetProducts(Paginator):
    def paginate(self, ServiceCode: str = None, Filters: List = None, FormatVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
