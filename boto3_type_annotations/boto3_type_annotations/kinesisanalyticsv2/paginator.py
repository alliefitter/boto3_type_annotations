from typing import Dict
from botocore.paginate import Paginator


class ListApplicationSnapshots(Paginator):
    def paginate(self, ApplicationName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListApplications(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
