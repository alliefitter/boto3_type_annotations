from typing import Dict
from botocore.paginate import Paginator


class ListFragments(Paginator):
    def paginate(self, StreamName: str, FragmentSelector: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass
