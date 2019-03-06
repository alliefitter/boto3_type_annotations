from typing import Dict
from botocore.paginate import Paginator


class ListApps(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListBranches(Paginator):
    def paginate(self, appId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDomainAssociations(Paginator):
    def paginate(self, appId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListJobs(Paginator):
    def paginate(self, appId: str, branchName: str, PaginationConfig: Dict = None) -> Dict:
        pass
