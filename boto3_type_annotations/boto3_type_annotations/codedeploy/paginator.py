from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListApplicationRevisions(Paginator):
    def paginate(self, applicationName: str, sortBy: str = None, sortOrder: str = None, s3Bucket: str = None, s3KeyPrefix: str = None, deployed: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListApplications(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDeploymentConfigs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDeploymentGroups(Paginator):
    def paginate(self, applicationName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDeploymentInstances(Paginator):
    def paginate(self, deploymentId: str, instanceStatusFilter: List = None, instanceTypeFilter: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDeployments(Paginator):
    def paginate(self, applicationName: str = None, deploymentGroupName: str = None, includeOnlyStatuses: List = None, createTimeRange: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass
