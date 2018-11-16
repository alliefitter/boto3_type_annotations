from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def associate_role_to_group(self, GroupId: str, RoleArn: str = None) -> Dict:
        pass

    def associate_service_role_to_account(self, RoleArn: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_core_definition(self, AmznClientToken: str = None, InitialVersion: Dict = None, Name: str = None) -> Dict:
        pass

    def create_core_definition_version(self, CoreDefinitionId: str, AmznClientToken: str = None, Cores: List = None) -> Dict:
        pass

    def create_deployment(self, GroupId: str, AmznClientToken: str = None, DeploymentId: str = None, DeploymentType: str = None, GroupVersionId: str = None) -> Dict:
        pass

    def create_device_definition(self, AmznClientToken: str = None, InitialVersion: Dict = None, Name: str = None) -> Dict:
        pass

    def create_device_definition_version(self, DeviceDefinitionId: str, AmznClientToken: str = None, Devices: List = None) -> Dict:
        pass

    def create_function_definition(self, AmznClientToken: str = None, InitialVersion: Dict = None, Name: str = None) -> Dict:
        pass

    def create_function_definition_version(self, FunctionDefinitionId: str, AmznClientToken: str = None, Functions: List = None) -> Dict:
        pass

    def create_group(self, AmznClientToken: str = None, InitialVersion: Dict = None, Name: str = None) -> Dict:
        pass

    def create_group_certificate_authority(self, GroupId: str, AmznClientToken: str = None) -> Dict:
        pass

    def create_group_version(self, GroupId: str, AmznClientToken: str = None, CoreDefinitionVersionArn: str = None, DeviceDefinitionVersionArn: str = None, FunctionDefinitionVersionArn: str = None, LoggerDefinitionVersionArn: str = None, ResourceDefinitionVersionArn: str = None, SubscriptionDefinitionVersionArn: str = None) -> Dict:
        pass

    def create_logger_definition(self, AmznClientToken: str = None, InitialVersion: Dict = None, Name: str = None) -> Dict:
        pass

    def create_logger_definition_version(self, LoggerDefinitionId: str, AmznClientToken: str = None, Loggers: List = None) -> Dict:
        pass

    def create_resource_definition(self, AmznClientToken: str = None, InitialVersion: Dict = None, Name: str = None) -> Dict:
        pass

    def create_resource_definition_version(self, ResourceDefinitionId: str, AmznClientToken: str = None, Resources: List = None) -> Dict:
        pass

    def create_software_update_job(self, AmznClientToken: str = None, S3UrlSignerRole: str = None, SoftwareToUpdate: str = None, UpdateAgentLogLevel: str = None, UpdateTargets: List = None, UpdateTargetsArchitecture: str = None, UpdateTargetsOperatingSystem: str = None) -> Dict:
        pass

    def create_subscription_definition(self, AmznClientToken: str = None, InitialVersion: Dict = None, Name: str = None) -> Dict:
        pass

    def create_subscription_definition_version(self, SubscriptionDefinitionId: str, AmznClientToken: str = None, Subscriptions: List = None) -> Dict:
        pass

    def delete_core_definition(self, CoreDefinitionId: str) -> Dict:
        pass

    def delete_device_definition(self, DeviceDefinitionId: str) -> Dict:
        pass

    def delete_function_definition(self, FunctionDefinitionId: str) -> Dict:
        pass

    def delete_group(self, GroupId: str) -> Dict:
        pass

    def delete_logger_definition(self, LoggerDefinitionId: str) -> Dict:
        pass

    def delete_resource_definition(self, ResourceDefinitionId: str) -> Dict:
        pass

    def delete_subscription_definition(self, SubscriptionDefinitionId: str) -> Dict:
        pass

    def disassociate_role_from_group(self, GroupId: str) -> Dict:
        pass

    def disassociate_service_role_from_account(self) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_associated_role(self, GroupId: str) -> Dict:
        pass

    def get_bulk_deployment_status(self, BulkDeploymentId: str) -> Dict:
        pass

    def get_connectivity_info(self, ThingName: str) -> Dict:
        pass

    def get_core_definition(self, CoreDefinitionId: str) -> Dict:
        pass

    def get_core_definition_version(self, CoreDefinitionId: str, CoreDefinitionVersionId: str) -> Dict:
        pass

    def get_deployment_status(self, DeploymentId: str, GroupId: str) -> Dict:
        pass

    def get_device_definition(self, DeviceDefinitionId: str) -> Dict:
        pass

    def get_device_definition_version(self, DeviceDefinitionId: str, DeviceDefinitionVersionId: str, NextToken: str = None) -> Dict:
        pass

    def get_function_definition(self, FunctionDefinitionId: str) -> Dict:
        pass

    def get_function_definition_version(self, FunctionDefinitionId: str, FunctionDefinitionVersionId: str, NextToken: str = None) -> Dict:
        pass

    def get_group(self, GroupId: str) -> Dict:
        pass

    def get_group_certificate_authority(self, CertificateAuthorityId: str, GroupId: str) -> Dict:
        pass

    def get_group_certificate_configuration(self, GroupId: str) -> Dict:
        pass

    def get_group_version(self, GroupId: str, GroupVersionId: str) -> Dict:
        pass

    def get_logger_definition(self, LoggerDefinitionId: str) -> Dict:
        pass

    def get_logger_definition_version(self, LoggerDefinitionId: str, LoggerDefinitionVersionId: str, NextToken: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_resource_definition(self, ResourceDefinitionId: str) -> Dict:
        pass

    def get_resource_definition_version(self, ResourceDefinitionId: str, ResourceDefinitionVersionId: str) -> Dict:
        pass

    def get_service_role_for_account(self) -> Dict:
        pass

    def get_subscription_definition(self, SubscriptionDefinitionId: str) -> Dict:
        pass

    def get_subscription_definition_version(self, SubscriptionDefinitionId: str, SubscriptionDefinitionVersionId: str, NextToken: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_bulk_deployment_detailed_reports(self, BulkDeploymentId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_bulk_deployments(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_core_definition_versions(self, CoreDefinitionId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_core_definitions(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_deployments(self, GroupId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_device_definition_versions(self, DeviceDefinitionId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_device_definitions(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_function_definition_versions(self, FunctionDefinitionId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_function_definitions(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_group_certificate_authorities(self, GroupId: str) -> Dict:
        pass

    def list_group_versions(self, GroupId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_groups(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_logger_definition_versions(self, LoggerDefinitionId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_logger_definitions(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_resource_definition_versions(self, ResourceDefinitionId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_resource_definitions(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_subscription_definition_versions(self, SubscriptionDefinitionId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def list_subscription_definitions(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        pass

    def reset_deployments(self, GroupId: str, AmznClientToken: str = None, Force: bool = None) -> Dict:
        pass

    def start_bulk_deployment(self, AmznClientToken: str = None, ExecutionRoleArn: str = None, InputFileUri: str = None) -> Dict:
        pass

    def stop_bulk_deployment(self, BulkDeploymentId: str) -> Dict:
        pass

    def update_connectivity_info(self, ThingName: str, ConnectivityInfo: List = None) -> Dict:
        pass

    def update_core_definition(self, CoreDefinitionId: str, Name: str = None) -> Dict:
        pass

    def update_device_definition(self, DeviceDefinitionId: str, Name: str = None) -> Dict:
        pass

    def update_function_definition(self, FunctionDefinitionId: str, Name: str = None) -> Dict:
        pass

    def update_group(self, GroupId: str, Name: str = None) -> Dict:
        pass

    def update_group_certificate_configuration(self, GroupId: str, CertificateExpiryInMilliseconds: str = None) -> Dict:
        pass

    def update_logger_definition(self, LoggerDefinitionId: str, Name: str = None) -> Dict:
        pass

    def update_resource_definition(self, ResourceDefinitionId: str, Name: str = None) -> Dict:
        pass

    def update_subscription_definition(self, SubscriptionDefinitionId: str, Name: str = None) -> Dict:
        pass
