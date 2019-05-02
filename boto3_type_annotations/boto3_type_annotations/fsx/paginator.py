from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeBackups(Paginator):
    def paginate(self, BackupIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeFileSystems(Paginator):
    def paginate(self, FileSystemIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTagsForResource(Paginator):
    def paginate(self, ResourceARN: str, PaginationConfig: Dict = None) -> Dict:
        pass
