from typing import Dict
from botocore.paginate import Paginator


class ListPlacements(Paginator):
    def paginate(self, projectName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListProjects(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
