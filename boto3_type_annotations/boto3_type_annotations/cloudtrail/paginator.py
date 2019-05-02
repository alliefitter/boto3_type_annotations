from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class ListPublicKeys(Paginator):
    def paginate(self, StartTime: datetime = None, EndTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTags(Paginator):
    def paginate(self, ResourceIdList: List, PaginationConfig: Dict = None) -> Dict:
        pass


class LookupEvents(Paginator):
    def paginate(self, LookupAttributes: List = None, StartTime: datetime = None, EndTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass
