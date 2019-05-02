from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class DescribeApplicationVersions(Paginator):
    def paginate(self, ApplicationName: str = None, VersionLabels: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEnvironmentManagedActionHistory(Paginator):
    def paginate(self, EnvironmentId: str = None, EnvironmentName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEnvironments(Paginator):
    def paginate(self, ApplicationName: str = None, VersionLabel: str = None, EnvironmentIds: List = None, EnvironmentNames: List = None, IncludeDeleted: bool = None, IncludedDeletedBackTo: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEvents(Paginator):
    def paginate(self, ApplicationName: str = None, VersionLabel: str = None, TemplateName: str = None, EnvironmentId: str = None, EnvironmentName: str = None, PlatformArn: str = None, RequestId: str = None, Severity: str = None, StartTime: datetime = None, EndTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPlatformVersions(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
