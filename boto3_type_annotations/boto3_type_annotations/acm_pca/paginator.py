from typing import Dict
from botocore.paginate import Paginator


class ListCertificateAuthorities(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPermissions(Paginator):
    def paginate(self, CertificateAuthorityArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTags(Paginator):
    def paginate(self, CertificateAuthorityArn: str, PaginationConfig: Dict = None) -> Dict:
        pass
