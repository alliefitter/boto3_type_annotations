from typing import Dict
from botocore.paginate import Paginator


class ListApplicationDependencies(Paginator):
    def paginate(self, ApplicationId: str, SemanticVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListApplicationVersions(Paginator):
    def paginate(self, ApplicationId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListApplications(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
