from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeAccountModifications(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeIpGroups(Paginator):
    def paginate(self, GroupIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeWorkspaceBundles(Paginator):
    def paginate(self, BundleIds: List = None, Owner: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeWorkspaceDirectories(Paginator):
    def paginate(self, DirectoryIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeWorkspaceImages(Paginator):
    def paginate(self, ImageIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeWorkspaces(Paginator):
    def paginate(self, WorkspaceIds: List = None, DirectoryId: str = None, UserName: str = None, BundleId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeWorkspacesConnectionStatus(Paginator):
    def paginate(self, WorkspaceIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAvailableManagementCidrRanges(Paginator):
    def paginate(self, ManagementCidrRangeConstraint: str, PaginationConfig: Dict = None) -> Dict:
        pass
