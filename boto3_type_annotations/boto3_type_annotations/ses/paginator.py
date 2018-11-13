from typing import Dict
from botocore.paginate import Paginator


class ListCustomVerificationEmailTemplates(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListIdentities(Paginator):
    def paginate(self, IdentityType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
