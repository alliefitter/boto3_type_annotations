from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeDomainControllers(Paginator):
    def paginate(self, DirectoryId: str, DomainControllerIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
