from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListCertificates(Paginator):
    def paginate(self, CertificateStatuses: List = None, Includes: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass
