from typing import Dict
from botocore.paginate import Paginator


class ListProjects(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListResources(Paginator):
    def paginate(self, projectId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTeamMembers(Paginator):
    def paginate(self, projectId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListUserProfiles(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
