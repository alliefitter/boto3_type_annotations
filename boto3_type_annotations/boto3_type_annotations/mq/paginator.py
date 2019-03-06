from typing import Dict
from botocore.paginate import Paginator


class ListBrokers(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
