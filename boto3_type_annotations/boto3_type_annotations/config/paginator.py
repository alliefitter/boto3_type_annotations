from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeComplianceByConfigRule(Paginator):
    def paginate(self, ConfigRuleNames: List = None, ComplianceTypes: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeComplianceByResource(Paginator):
    def paginate(self, ResourceType: str = None, ResourceId: str = None, ComplianceTypes: List = None, Limit: int = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeConfigRules(Paginator):
    def paginate(self, ConfigRuleNames: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetComplianceDetailsByConfigRule(Paginator):
    def paginate(self, ConfigRuleName: str, ComplianceTypes: List = None, Limit: int = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetComplianceDetailsByResource(Paginator):
    def paginate(self, ResourceType: str, ResourceId: str, ComplianceTypes: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetResourceConfigHistory(Paginator):
    def paginate(self, resourceType: str, resourceId: str, laterTime: datetime = None, earlierTime: datetime = None, chronologicalOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDiscoveredResources(Paginator):
    def paginate(self, resourceType: str, resourceIds: List = None, resourceName: str = None, limit: int = None, includeDeletedResources: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass
