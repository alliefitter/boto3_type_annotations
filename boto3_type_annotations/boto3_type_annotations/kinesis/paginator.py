from typing import Dict
from botocore.paginate import Paginator


class DescribeStream(Paginator):
    def paginate(self, StreamName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStreams(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
