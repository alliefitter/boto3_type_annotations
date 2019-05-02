from typing import Dict
from datetime import datetime
from typing import List
from botocore.paginate import Paginator


class DescribeAggregateComplianceByConfigRules(Paginator):
    def paginate(self, ConfigurationAggregatorName: str, Filters: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeAggregationAuthorizations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeComplianceByConfigRule(Paginator):
    def paginate(self, ConfigRuleNames: List = None, ComplianceTypes: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeComplianceByResource(Paginator):
    def paginate(self, ResourceType: str = None, ResourceId: str = None, ComplianceTypes: List = None, Limit: int = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeConfigRuleEvaluationStatus(Paginator):
    def paginate(self, ConfigRuleNames: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeConfigRules(Paginator):
    def paginate(self, ConfigRuleNames: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeConfigurationAggregatorSourcesStatus(Paginator):
    def paginate(self, ConfigurationAggregatorName: str, UpdateStatus: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeConfigurationAggregators(Paginator):
    def paginate(self, ConfigurationAggregatorNames: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribePendingAggregationRequests(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeRemediationExecutionStatus(Paginator):
    def paginate(self, ConfigRuleName: str, ResourceKeys: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeRetentionConfigurations(Paginator):
    def paginate(self, RetentionConfigurationNames: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetAggregateComplianceDetailsByConfigRule(Paginator):
    def paginate(self, ConfigurationAggregatorName: str, ConfigRuleName: str, AccountId: str, AwsRegion: str, ComplianceType: str = None, PaginationConfig: Dict = None) -> Dict:
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


class ListAggregateDiscoveredResources(Paginator):
    def paginate(self, ConfigurationAggregatorName: str, ResourceType: str, Filters: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDiscoveredResources(Paginator):
    def paginate(self, resourceType: str, resourceIds: List = None, resourceName: str = None, limit: int = None, includeDeletedResources: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass
