from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def add_tags(self, ARN: str, TagList: List):
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def cancel_elasticsearch_service_software_update(self, DomainName: str) -> Dict:
        pass

    def create_elasticsearch_domain(self, DomainName: str, ElasticsearchVersion: str = None, ElasticsearchClusterConfig: Dict = None, EBSOptions: Dict = None, AccessPolicies: str = None, SnapshotOptions: Dict = None, VPCOptions: Dict = None, CognitoOptions: Dict = None, EncryptionAtRestOptions: Dict = None, NodeToNodeEncryptionOptions: Dict = None, AdvancedOptions: Dict = None, LogPublishingOptions: Dict = None) -> Dict:
        pass

    def delete_elasticsearch_domain(self, DomainName: str) -> Dict:
        pass

    def delete_elasticsearch_service_role(self):
        pass

    def describe_elasticsearch_domain(self, DomainName: str) -> Dict:
        pass

    def describe_elasticsearch_domain_config(self, DomainName: str) -> Dict:
        pass

    def describe_elasticsearch_domains(self, DomainNames: List) -> Dict:
        pass

    def describe_elasticsearch_instance_type_limits(self, InstanceType: str, ElasticsearchVersion: str, DomainName: str = None) -> Dict:
        pass

    def describe_reserved_elasticsearch_instance_offerings(self, ReservedElasticsearchInstanceOfferingId: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_reserved_elasticsearch_instances(self, ReservedElasticsearchInstanceId: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_compatible_elasticsearch_versions(self, DomainName: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_upgrade_history(self, DomainName: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def get_upgrade_status(self, DomainName: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_domain_names(self) -> Dict:
        pass

    def list_elasticsearch_instance_types(self, ElasticsearchVersion: str, DomainName: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_elasticsearch_versions(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_tags(self, ARN: str) -> Dict:
        pass

    def purchase_reserved_elasticsearch_instance_offering(self, ReservedElasticsearchInstanceOfferingId: str, ReservationName: str, InstanceCount: int = None) -> Dict:
        pass

    def remove_tags(self, ARN: str, TagKeys: List):
        pass

    def start_elasticsearch_service_software_update(self, DomainName: str) -> Dict:
        pass

    def update_elasticsearch_domain_config(self, DomainName: str, ElasticsearchClusterConfig: Dict = None, EBSOptions: Dict = None, SnapshotOptions: Dict = None, VPCOptions: Dict = None, CognitoOptions: Dict = None, AdvancedOptions: Dict = None, AccessPolicies: str = None, LogPublishingOptions: Dict = None) -> Dict:
        pass

    def upgrade_elasticsearch_domain(self, DomainName: str, TargetVersion: str, PerformCheckOnly: bool = None) -> Dict:
        pass
