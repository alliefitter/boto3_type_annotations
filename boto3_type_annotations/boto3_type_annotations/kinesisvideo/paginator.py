from typing import Dict
from botocore.paginate import Paginator


class ListStreams(Paginator):
    def paginate(self, StreamNameCondition: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass
