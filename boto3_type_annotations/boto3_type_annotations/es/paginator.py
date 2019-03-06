from typing import Dict
from botocore.paginate import Paginator


class DescribeReservedElasticsearchInstanceOfferings(Paginator):
    def paginate(self, ReservedElasticsearchInstanceOfferingId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeReservedElasticsearchInstances(Paginator):
    def paginate(self, ReservedElasticsearchInstanceId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetUpgradeHistory(Paginator):
    def paginate(self, DomainName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListElasticsearchInstanceTypes(Paginator):
    def paginate(self, ElasticsearchVersion: str, DomainName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListElasticsearchVersions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
