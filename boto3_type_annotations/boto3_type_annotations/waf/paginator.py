from typing import Dict
from botocore.paginate import Paginator


class GetRateBasedRuleManagedKeys(Paginator):
    def paginate(self, RuleId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListActivatedRulesInRuleGroup(Paginator):
    def paginate(self, RuleGroupId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListByteMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListGeoMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListIPSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListLoggingConfigurations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRateBasedRules(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRegexMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRegexPatternSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRuleGroups(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRules(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSizeConstraintSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSqlInjectionMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSubscribedRuleGroups(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListWebACLs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListXssMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
