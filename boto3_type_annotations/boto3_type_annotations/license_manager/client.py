from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_license_configuration(self, Name: str, LicenseCountingType: str, Description: str = None, LicenseCount: int = None, LicenseCountHardLimit: bool = None, LicenseRules: List = None, Tags: List = None) -> Dict:
        pass

    def delete_license_configuration(self, LicenseConfigurationArn: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_license_configuration(self, LicenseConfigurationArn: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_service_settings(self) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_associations_for_license_configuration(self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_license_configurations(self, LicenseConfigurationArns: List = None, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        pass

    def list_license_specifications_for_resource(self, ResourceArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_resource_inventory(self, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        pass

    def list_usage_for_license_configuration(self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        pass

    def tag_resource(self, ResourceArn: str, Tags: List) -> Dict:
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List) -> Dict:
        pass

    def update_license_configuration(self, LicenseConfigurationArn: str, LicenseConfigurationStatus: str = None, LicenseRules: List = None, LicenseCount: int = None, LicenseCountHardLimit: bool = None, Name: str = None, Description: str = None) -> Dict:
        pass

    def update_license_specifications_for_resource(self, ResourceArn: str, AddLicenseSpecifications: List = None, RemoveLicenseSpecifications: List = None) -> Dict:
        pass

    def update_service_settings(self, S3BucketArn: str = None, SnsTopicArn: str = None, OrganizationConfiguration: Dict = None, EnableCrossAccountsDiscovery: bool = None) -> Dict:
        pass
