from typing import Dict
from botocore.paginate import Paginator


class ListBuilds(Paginator):
    def paginate(self, sortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListBuildsForProject(Paginator):
    def paginate(self, projectName: str, sortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListProjects(Paginator):
    def paginate(self, sortBy: str = None, sortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
