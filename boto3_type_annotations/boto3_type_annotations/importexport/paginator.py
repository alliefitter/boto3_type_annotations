from typing import Dict
from botocore.paginate import Paginator


class ListJobs(Paginator):
    def paginate(self, APIVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
