from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class LookupEvents(Paginator):
    def paginate(self, LookupAttributes: List = None, StartTime: datetime = None, EndTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass
