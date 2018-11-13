from typing import Dict
from botocore.paginate import Paginator


class DescribeReportDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
