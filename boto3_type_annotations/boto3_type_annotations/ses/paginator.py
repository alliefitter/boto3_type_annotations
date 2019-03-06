from typing import Dict
from botocore.paginate import Paginator


class ListConfigurationSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCustomVerificationEmailTemplates(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListIdentities(Paginator):
    def paginate(self, IdentityType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListReceiptRuleSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTemplates(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
