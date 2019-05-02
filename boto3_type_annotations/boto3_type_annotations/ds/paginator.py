from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeDirectories(Paginator):
    def paginate(self, DirectoryIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDomainControllers(Paginator):
    def paginate(self, DirectoryId: str, DomainControllerIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSharedDirectories(Paginator):
    def paginate(self, OwnerDirectoryId: str, SharedDirectoryIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSnapshots(Paginator):
    def paginate(self, DirectoryId: str = None, SnapshotIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTrusts(Paginator):
    def paginate(self, DirectoryId: str = None, TrustIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListIpRoutes(Paginator):
    def paginate(self, DirectoryId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListLogSubscriptions(Paginator):
    def paginate(self, DirectoryId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSchemaExtensions(Paginator):
    def paginate(self, DirectoryId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTagsForResource(Paginator):
    def paginate(self, ResourceId: str, PaginationConfig: Dict = None) -> Dict:
        pass
