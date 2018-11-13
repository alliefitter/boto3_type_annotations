from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeWorkspaceBundles(Paginator):
    def paginate(self, BundleIds: List = None, Owner: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeWorkspaceDirectories(Paginator):
    def paginate(self, DirectoryIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeWorkspaces(Paginator):
    def paginate(self, WorkspaceIds: List = None, DirectoryId: str = None, UserName: str = None, BundleId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
