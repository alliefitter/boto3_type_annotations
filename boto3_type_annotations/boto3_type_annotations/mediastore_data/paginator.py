from typing import Dict
from botocore.paginate import Paginator


class ListItems(Paginator):
    def paginate(self, Path: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
