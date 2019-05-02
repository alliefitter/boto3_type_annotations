from typing import Dict
from typing import List
from botocore.paginate import Paginator


class ListDeploymentJobs(Paginator):
    def paginate(self, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListFleets(Paginator):
    def paginate(self, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRobotApplications(Paginator):
    def paginate(self, versionQualifier: str = None, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRobots(Paginator):
    def paginate(self, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSimulationApplications(Paginator):
    def paginate(self, versionQualifier: str = None, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSimulationJobs(Paginator):
    def paginate(self, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
