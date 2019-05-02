from typing import Dict
from datetime import datetime
from botocore.paginate import Paginator


class DescribeActivities(Paginator):
    def paginate(self, AuthenticationToken: str = None, StartTime: datetime = None, EndTime: datetime = None, OrganizationId: str = None, ActivityTypes: str = None, ResourceId: str = None, UserId: str = None, IncludeIndirectActivities: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeComments(Paginator):
    def paginate(self, DocumentId: str, VersionId: str, AuthenticationToken: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDocumentVersions(Paginator):
    def paginate(self, DocumentId: str, AuthenticationToken: str = None, Include: str = None, Fields: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeFolderContents(Paginator):
    def paginate(self, FolderId: str, AuthenticationToken: str = None, Sort: str = None, Order: str = None, Type: str = None, Include: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeGroups(Paginator):
    def paginate(self, SearchQuery: str, AuthenticationToken: str = None, OrganizationId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeNotificationSubscriptions(Paginator):
    def paginate(self, OrganizationId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeResourcePermissions(Paginator):
    def paginate(self, ResourceId: str, AuthenticationToken: str = None, PrincipalId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeRootFolders(Paginator):
    def paginate(self, AuthenticationToken: str, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeUsers(Paginator):
    def paginate(self, AuthenticationToken: str = None, OrganizationId: str = None, UserIds: str = None, Query: str = None, Include: str = None, Order: str = None, Sort: str = None, Fields: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
