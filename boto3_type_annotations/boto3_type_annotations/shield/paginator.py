from typing import Dict
from typing import List
from botocore.paginate import Paginator


class ListAttacks(Paginator):
    def paginate(self, ResourceArns: List = None, StartTime: Dict = None, EndTime: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListProtections(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
