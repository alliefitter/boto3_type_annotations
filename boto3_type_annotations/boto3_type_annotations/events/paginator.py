from typing import Dict
from botocore.paginate import Paginator


class ListRuleNamesByTarget(Paginator):
    def paginate(self, TargetArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRules(Paginator):
    def paginate(self, NamePrefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTargetsByRule(Paginator):
    def paginate(self, Rule: str, PaginationConfig: Dict = None) -> Dict:
        pass
