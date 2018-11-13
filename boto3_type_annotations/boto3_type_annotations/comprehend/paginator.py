from typing import Dict
from botocore.paginate import Paginator


class ListTopicsDetectionJobs(Paginator):
    def paginate(self, Filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass
