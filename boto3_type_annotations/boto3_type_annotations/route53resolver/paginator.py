from typing import Dict
from botocore.paginate import Paginator


class ListTagsForResource(Paginator):
    def paginate(self, ResourceArn: str, PaginationConfig: Dict = None) -> Dict:
        pass
