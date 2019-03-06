from typing import Dict
from botocore.paginate import Paginator


class GetEntitlements(Paginator):
    def paginate(self, ProductCode: str, Filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass
