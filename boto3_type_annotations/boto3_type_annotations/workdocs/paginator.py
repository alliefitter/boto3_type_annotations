from typing import Dict
from botocore.paginate import Paginator


class DescribeDocumentVersions(Paginator):
    def paginate(self, DocumentId: str, AuthenticationToken: str = None, Include: str = None, Fields: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeFolderContents(Paginator):
    def paginate(self, FolderId: str, AuthenticationToken: str = None, Sort: str = None, Order: str = None, Type: str = None, Include: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeUsers(Paginator):
    def paginate(self, AuthenticationToken: str = None, OrganizationId: str = None, UserIds: str = None, Query: str = None, Include: str = None, Order: str = None, Sort: str = None, Fields: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
