from typing import Dict
from botocore.paginate import Paginator


class DescribeFileSystems(Paginator):
    def paginate(self, CreationToken: str = None, FileSystemId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeMountTargets(Paginator):
    def paginate(self, FileSystemId: str = None, MountTargetId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTags(Paginator):
    def paginate(self, FileSystemId: str, PaginationConfig: Dict = None) -> Dict:
        pass
