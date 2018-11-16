from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def cancel_update_stack(self, StackName: str, ClientRequestToken: str = None):
        pass

    def continue_update_rollback(self, StackName: str, RoleARN: str = None, ResourcesToSkip: List = None, ClientRequestToken: str = None) -> Dict:
        pass

    def create_change_set(self, StackName: str, ChangeSetName: str, TemplateBody: str = None, TemplateURL: str = None, UsePreviousTemplate: bool = None, Parameters: List = None, Capabilities: List = None, ResourceTypes: List = None, RoleARN: str = None, RollbackConfiguration: Dict = None, NotificationARNs: List = None, Tags: List = None, ClientToken: str = None, Description: str = None, ChangeSetType: str = None) -> Dict:
        pass

    def create_stack(self, StackName: str, TemplateBody: str = None, TemplateURL: str = None, Parameters: List = None, DisableRollback: bool = None, RollbackConfiguration: Dict = None, TimeoutInMinutes: int = None, NotificationARNs: List = None, Capabilities: List = None, ResourceTypes: List = None, RoleARN: str = None, OnFailure: str = None, StackPolicyBody: str = None, StackPolicyURL: str = None, Tags: List = None, ClientRequestToken: str = None, EnableTerminationProtection: bool = None) -> Dict:
        pass

    def create_stack_instances(self, StackSetName: str, Accounts: List, Regions: List, ParameterOverrides: List = None, OperationPreferences: Dict = None, OperationId: str = None) -> Dict:
        pass

    def create_stack_set(self, StackSetName: str, Description: str = None, TemplateBody: str = None, TemplateURL: str = None, Parameters: List = None, Capabilities: List = None, Tags: List = None, AdministrationRoleARN: str = None, ExecutionRoleName: str = None, ClientRequestToken: str = None) -> Dict:
        pass

    def delete_change_set(self, ChangeSetName: str, StackName: str = None) -> Dict:
        pass

    def delete_stack(self, StackName: str, RetainResources: List = None, RoleARN: str = None, ClientRequestToken: str = None):
        pass

    def delete_stack_instances(self, StackSetName: str, Accounts: List, Regions: List, RetainStacks: bool, OperationPreferences: Dict = None, OperationId: str = None) -> Dict:
        pass

    def delete_stack_set(self, StackSetName: str) -> Dict:
        pass

    def describe_account_limits(self, NextToken: str = None) -> Dict:
        pass

    def describe_change_set(self, ChangeSetName: str, StackName: str = None, NextToken: str = None) -> Dict:
        pass

    def describe_stack_drift_detection_status(self, StackDriftDetectionId: str) -> Dict:
        pass

    def describe_stack_events(self, StackName: str = None, NextToken: str = None) -> Dict:
        pass

    def describe_stack_instance(self, StackSetName: str, StackInstanceAccount: str, StackInstanceRegion: str) -> Dict:
        pass

    def describe_stack_resource(self, StackName: str, LogicalResourceId: str) -> Dict:
        pass

    def describe_stack_resource_drifts(self, StackName: str, StackResourceDriftStatusFilters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_stack_resources(self, StackName: str = None, LogicalResourceId: str = None, PhysicalResourceId: str = None) -> Dict:
        pass

    def describe_stack_set(self, StackSetName: str) -> Dict:
        pass

    def describe_stack_set_operation(self, StackSetName: str, OperationId: str) -> Dict:
        pass

    def describe_stacks(self, StackName: str = None, NextToken: str = None) -> Dict:
        pass

    def detect_stack_drift(self, StackName: str, LogicalResourceIds: List = None) -> Dict:
        pass

    def detect_stack_resource_drift(self, StackName: str, LogicalResourceId: str) -> Dict:
        pass

    def estimate_template_cost(self, TemplateBody: str = None, TemplateURL: str = None, Parameters: List = None) -> Dict:
        pass

    def execute_change_set(self, ChangeSetName: str, StackName: str = None, ClientRequestToken: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_stack_policy(self, StackName: str) -> Dict:
        pass

    def get_template(self, StackName: str = None, ChangeSetName: str = None, TemplateStage: str = None) -> Dict:
        pass

    def get_template_summary(self, TemplateBody: str = None, TemplateURL: str = None, StackName: str = None, StackSetName: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_change_sets(self, StackName: str, NextToken: str = None) -> Dict:
        pass

    def list_exports(self, NextToken: str = None) -> Dict:
        pass

    def list_imports(self, ExportName: str, NextToken: str = None) -> Dict:
        pass

    def list_stack_instances(self, StackSetName: str, NextToken: str = None, MaxResults: int = None, StackInstanceAccount: str = None, StackInstanceRegion: str = None) -> Dict:
        pass

    def list_stack_resources(self, StackName: str, NextToken: str = None) -> Dict:
        pass

    def list_stack_set_operation_results(self, StackSetName: str, OperationId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_stack_set_operations(self, StackSetName: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_stack_sets(self, NextToken: str = None, MaxResults: int = None, Status: str = None) -> Dict:
        pass

    def list_stacks(self, NextToken: str = None, StackStatusFilter: List = None) -> Dict:
        pass

    def set_stack_policy(self, StackName: str, StackPolicyBody: str = None, StackPolicyURL: str = None):
        pass

    def signal_resource(self, StackName: str, LogicalResourceId: str, UniqueId: str, Status: str):
        pass

    def stop_stack_set_operation(self, StackSetName: str, OperationId: str) -> Dict:
        pass

    def update_stack(self, StackName: str, TemplateBody: str = None, TemplateURL: str = None, UsePreviousTemplate: bool = None, StackPolicyDuringUpdateBody: str = None, StackPolicyDuringUpdateURL: str = None, Parameters: List = None, Capabilities: List = None, ResourceTypes: List = None, RoleARN: str = None, RollbackConfiguration: Dict = None, StackPolicyBody: str = None, StackPolicyURL: str = None, NotificationARNs: List = None, Tags: List = None, ClientRequestToken: str = None) -> Dict:
        pass

    def update_stack_instances(self, StackSetName: str, Accounts: List, Regions: List, ParameterOverrides: List = None, OperationPreferences: Dict = None, OperationId: str = None) -> Dict:
        pass

    def update_stack_set(self, StackSetName: str, Description: str = None, TemplateBody: str = None, TemplateURL: str = None, UsePreviousTemplate: bool = None, Parameters: List = None, Capabilities: List = None, Tags: List = None, OperationPreferences: Dict = None, AdministrationRoleARN: str = None, ExecutionRoleName: str = None, OperationId: str = None, Accounts: List = None, Regions: List = None) -> Dict:
        pass

    def update_termination_protection(self, EnableTerminationProtection: bool, StackName: str) -> Dict:
        pass

    def validate_template(self, TemplateBody: str = None, TemplateURL: str = None) -> Dict:
        pass
