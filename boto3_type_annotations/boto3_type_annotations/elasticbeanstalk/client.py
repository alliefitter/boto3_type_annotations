from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def abort_environment_update(self, EnvironmentId: str = None, EnvironmentName: str = None) -> NoReturn:
        pass

    def apply_environment_managed_action(self, ActionId: str, EnvironmentName: str = None, EnvironmentId: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def check_dns_availability(self, CNAMEPrefix: str) -> Dict:
        pass

    def compose_environments(self, ApplicationName: str = None, GroupName: str = None, VersionLabels: List = None) -> Dict:
        pass

    def create_application(self, ApplicationName: str, Description: str = None, ResourceLifecycleConfig: Dict = None) -> Dict:
        pass

    def create_application_version(self, ApplicationName: str, VersionLabel: str, Description: str = None, SourceBuildInformation: Dict = None, SourceBundle: Dict = None, BuildConfiguration: Dict = None, AutoCreateApplication: bool = None, Process: bool = None) -> Dict:
        pass

    def create_configuration_template(self, ApplicationName: str, TemplateName: str, SolutionStackName: str = None, PlatformArn: str = None, SourceConfiguration: Dict = None, EnvironmentId: str = None, Description: str = None, OptionSettings: List = None) -> Dict:
        pass

    def create_environment(self, ApplicationName: str, EnvironmentName: str = None, GroupName: str = None, Description: str = None, CNAMEPrefix: str = None, Tier: Dict = None, Tags: List = None, VersionLabel: str = None, TemplateName: str = None, SolutionStackName: str = None, PlatformArn: str = None, OptionSettings: List = None, OptionsToRemove: List = None) -> Dict:
        pass

    def create_platform_version(self, PlatformName: str, PlatformVersion: str, PlatformDefinitionBundle: Dict, EnvironmentName: str = None, OptionSettings: List = None) -> Dict:
        pass

    def create_storage_location(self) -> Dict:
        pass

    def delete_application(self, ApplicationName: str, TerminateEnvByForce: bool = None) -> NoReturn:
        pass

    def delete_application_version(self, ApplicationName: str, VersionLabel: str, DeleteSourceBundle: bool = None) -> NoReturn:
        pass

    def delete_configuration_template(self, ApplicationName: str, TemplateName: str) -> NoReturn:
        pass

    def delete_environment_configuration(self, ApplicationName: str, EnvironmentName: str) -> NoReturn:
        pass

    def delete_platform_version(self, PlatformArn: str = None) -> Dict:
        pass

    def describe_account_attributes(self) -> Dict:
        pass

    def describe_application_versions(self, ApplicationName: str = None, VersionLabels: List = None, MaxRecords: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_applications(self, ApplicationNames: List = None) -> Dict:
        pass

    def describe_configuration_options(self, ApplicationName: str = None, TemplateName: str = None, EnvironmentName: str = None, SolutionStackName: str = None, PlatformArn: str = None, Options: List = None) -> Dict:
        pass

    def describe_configuration_settings(self, ApplicationName: str, TemplateName: str = None, EnvironmentName: str = None) -> Dict:
        pass

    def describe_environment_health(self, EnvironmentName: str = None, EnvironmentId: str = None, AttributeNames: List = None) -> Dict:
        pass

    def describe_environment_managed_action_history(self, EnvironmentId: str = None, EnvironmentName: str = None, NextToken: str = None, MaxItems: int = None) -> Dict:
        pass

    def describe_environment_managed_actions(self, EnvironmentName: str = None, EnvironmentId: str = None, Status: str = None) -> Dict:
        pass

    def describe_environment_resources(self, EnvironmentId: str = None, EnvironmentName: str = None) -> Dict:
        pass

    def describe_environments(self, ApplicationName: str = None, VersionLabel: str = None, EnvironmentIds: List = None, EnvironmentNames: List = None, IncludeDeleted: bool = None, IncludedDeletedBackTo: datetime = None, MaxRecords: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_events(self, ApplicationName: str = None, VersionLabel: str = None, TemplateName: str = None, EnvironmentId: str = None, EnvironmentName: str = None, PlatformArn: str = None, RequestId: str = None, Severity: str = None, StartTime: datetime = None, EndTime: datetime = None, MaxRecords: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_instances_health(self, EnvironmentName: str = None, EnvironmentId: str = None, AttributeNames: List = None, NextToken: str = None) -> Dict:
        pass

    def describe_platform_version(self, PlatformArn: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_available_solution_stacks(self) -> Dict:
        pass

    def list_platform_versions(self, Filters: List = None, MaxRecords: int = None, NextToken: str = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        pass

    def rebuild_environment(self, EnvironmentId: str = None, EnvironmentName: str = None) -> NoReturn:
        pass

    def request_environment_info(self, InfoType: str, EnvironmentId: str = None, EnvironmentName: str = None) -> NoReturn:
        pass

    def restart_app_server(self, EnvironmentId: str = None, EnvironmentName: str = None) -> NoReturn:
        pass

    def retrieve_environment_info(self, InfoType: str, EnvironmentId: str = None, EnvironmentName: str = None) -> Dict:
        pass

    def swap_environment_cnames(self, SourceEnvironmentId: str = None, SourceEnvironmentName: str = None, DestinationEnvironmentId: str = None, DestinationEnvironmentName: str = None) -> NoReturn:
        pass

    def terminate_environment(self, EnvironmentId: str = None, EnvironmentName: str = None, TerminateResources: bool = None, ForceTerminate: bool = None) -> Dict:
        pass

    def update_application(self, ApplicationName: str, Description: str = None) -> Dict:
        pass

    def update_application_resource_lifecycle(self, ApplicationName: str, ResourceLifecycleConfig: Dict) -> Dict:
        pass

    def update_application_version(self, ApplicationName: str, VersionLabel: str, Description: str = None) -> Dict:
        pass

    def update_configuration_template(self, ApplicationName: str, TemplateName: str, Description: str = None, OptionSettings: List = None, OptionsToRemove: List = None) -> Dict:
        pass

    def update_environment(self, ApplicationName: str = None, EnvironmentId: str = None, EnvironmentName: str = None, GroupName: str = None, Description: str = None, Tier: Dict = None, VersionLabel: str = None, TemplateName: str = None, SolutionStackName: str = None, PlatformArn: str = None, OptionSettings: List = None, OptionsToRemove: List = None) -> Dict:
        pass

    def update_tags_for_resource(self, ResourceArn: str, TagsToAdd: List = None, TagsToRemove: List = None) -> NoReturn:
        pass

    def validate_configuration_settings(self, ApplicationName: str, OptionSettings: List, TemplateName: str = None, EnvironmentName: str = None) -> Dict:
        pass
