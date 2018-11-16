from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def batch_get_resource_config(self, resourceKeys: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def delete_aggregation_authorization(self, AuthorizedAccountId: str, AuthorizedAwsRegion: str):
        pass

    def delete_config_rule(self, ConfigRuleName: str):
        pass

    def delete_configuration_aggregator(self, ConfigurationAggregatorName: str):
        pass

    def delete_configuration_recorder(self, ConfigurationRecorderName: str):
        pass

    def delete_delivery_channel(self, DeliveryChannelName: str):
        pass

    def delete_evaluation_results(self, ConfigRuleName: str) -> Dict:
        pass

    def delete_pending_aggregation_request(self, RequesterAccountId: str, RequesterAwsRegion: str):
        pass

    def delete_retention_configuration(self, RetentionConfigurationName: str):
        pass

    def deliver_config_snapshot(self, deliveryChannelName: str) -> Dict:
        pass

    def describe_aggregate_compliance_by_config_rules(self, ConfigurationAggregatorName: str, Filters: Dict = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_aggregation_authorizations(self, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_compliance_by_config_rule(self, ConfigRuleNames: List = None, ComplianceTypes: List = None, NextToken: str = None) -> Dict:
        pass

    def describe_compliance_by_resource(self, ResourceType: str = None, ResourceId: str = None, ComplianceTypes: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_config_rule_evaluation_status(self, ConfigRuleNames: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    def describe_config_rules(self, ConfigRuleNames: List = None, NextToken: str = None) -> Dict:
        pass

    def describe_configuration_aggregator_sources_status(self, ConfigurationAggregatorName: str, UpdateStatus: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    def describe_configuration_aggregators(self, ConfigurationAggregatorNames: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    def describe_configuration_recorder_status(self, ConfigurationRecorderNames: List = None) -> Dict:
        pass

    def describe_configuration_recorders(self, ConfigurationRecorderNames: List = None) -> Dict:
        pass

    def describe_delivery_channel_status(self, DeliveryChannelNames: List = None) -> Dict:
        pass

    def describe_delivery_channels(self, DeliveryChannelNames: List = None) -> Dict:
        pass

    def describe_pending_aggregation_requests(self, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_retention_configurations(self, RetentionConfigurationNames: List = None, NextToken: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_aggregate_compliance_details_by_config_rule(self, ConfigurationAggregatorName: str, ConfigRuleName: str, AccountId: str, AwsRegion: str, ComplianceType: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def get_aggregate_config_rule_compliance_summary(self, ConfigurationAggregatorName: str, Filters: Dict = None, GroupByKey: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def get_compliance_details_by_config_rule(self, ConfigRuleName: str, ComplianceTypes: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def get_compliance_details_by_resource(self, ResourceType: str, ResourceId: str, ComplianceTypes: List = None, NextToken: str = None) -> Dict:
        pass

    def get_compliance_summary_by_config_rule(self) -> Dict:
        pass

    def get_compliance_summary_by_resource_type(self, ResourceTypes: List = None) -> Dict:
        pass

    def get_discovered_resource_counts(self, resourceTypes: List = None, limit: int = None, nextToken: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_resource_config_history(self, resourceType: str, resourceId: str, laterTime: datetime = None, earlierTime: datetime = None, chronologicalOrder: str = None, limit: int = None, nextToken: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_discovered_resources(self, resourceType: str, resourceIds: List = None, resourceName: str = None, limit: int = None, includeDeletedResources: bool = None, nextToken: str = None) -> Dict:
        pass

    def put_aggregation_authorization(self, AuthorizedAccountId: str, AuthorizedAwsRegion: str) -> Dict:
        pass

    def put_config_rule(self, ConfigRule: Dict):
        pass

    def put_configuration_aggregator(self, ConfigurationAggregatorName: str, AccountAggregationSources: List = None, OrganizationAggregationSource: Dict = None) -> Dict:
        pass

    def put_configuration_recorder(self, ConfigurationRecorder: Dict):
        pass

    def put_delivery_channel(self, DeliveryChannel: Dict):
        pass

    def put_evaluations(self, ResultToken: str, Evaluations: List = None, TestMode: bool = None) -> Dict:
        pass

    def put_retention_configuration(self, RetentionPeriodInDays: int) -> Dict:
        pass

    def start_config_rules_evaluation(self, ConfigRuleNames: List = None) -> Dict:
        pass

    def start_configuration_recorder(self, ConfigurationRecorderName: str):
        pass

    def stop_configuration_recorder(self, ConfigurationRecorderName: str):
        pass
