from typing import Dict
from botocore.paginate import Paginator


class ListSecrets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
