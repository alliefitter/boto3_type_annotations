from typing import Dict
from botocore.paginate import Paginator


class ListContainers(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
