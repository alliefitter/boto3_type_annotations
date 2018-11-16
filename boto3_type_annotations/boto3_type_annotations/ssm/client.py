from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def add_tags_to_resource(self, ResourceType: str, ResourceId: str, Tags: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def cancel_command(self, CommandId: str, InstanceIds: List = None) -> Dict:
        pass

    def cancel_maintenance_window_execution(self, WindowExecutionId: str) -> Dict:
        pass

    def create_activation(self, IamRole: str, Description: str = None, DefaultInstanceName: str = None, RegistrationLimit: int = None, ExpirationDate: datetime = None) -> Dict:
        pass

    def create_association(self, Name: str, DocumentVersion: str = None, InstanceId: str = None, Parameters: Dict = None, Targets: List = None, ScheduleExpression: str = None, OutputLocation: Dict = None, AssociationName: str = None, MaxErrors: str = None, MaxConcurrency: str = None, ComplianceSeverity: str = None) -> Dict:
        pass

    def create_association_batch(self, Entries: List) -> Dict:
        pass

    def create_document(self, Content: str, Name: str, DocumentType: str = None, DocumentFormat: str = None, TargetType: str = None) -> Dict:
        pass

    def create_maintenance_window(self, Name: str, Schedule: str, Duration: int, Cutoff: int, AllowUnassociatedTargets: bool, Description: str = None, StartDate: str = None, EndDate: str = None, ScheduleTimezone: str = None, ClientToken: str = None) -> Dict:
        pass

    def create_patch_baseline(self, Name: str, OperatingSystem: str = None, GlobalFilters: Dict = None, ApprovalRules: Dict = None, ApprovedPatches: List = None, ApprovedPatchesComplianceLevel: str = None, ApprovedPatchesEnableNonSecurity: bool = None, RejectedPatches: List = None, RejectedPatchesAction: str = None, Description: str = None, Sources: List = None, ClientToken: str = None) -> Dict:
        pass

    def create_resource_data_sync(self, SyncName: str, S3Destination: Dict) -> Dict:
        pass

    def delete_activation(self, ActivationId: str) -> Dict:
        pass

    def delete_association(self, Name: str = None, InstanceId: str = None, AssociationId: str = None) -> Dict:
        pass

    def delete_document(self, Name: str) -> Dict:
        pass

    def delete_inventory(self, TypeName: str, SchemaDeleteOption: str = None, DryRun: bool = None, ClientToken: str = None) -> Dict:
        pass

    def delete_maintenance_window(self, WindowId: str) -> Dict:
        pass

    def delete_parameter(self, Name: str) -> Dict:
        pass

    def delete_parameters(self, Names: List) -> Dict:
        pass

    def delete_patch_baseline(self, BaselineId: str) -> Dict:
        pass

    def delete_resource_data_sync(self, SyncName: str) -> Dict:
        pass

    def deregister_managed_instance(self, InstanceId: str) -> Dict:
        pass

    def deregister_patch_baseline_for_patch_group(self, BaselineId: str, PatchGroup: str) -> Dict:
        pass

    def deregister_target_from_maintenance_window(self, WindowId: str, WindowTargetId: str, Safe: bool = None) -> Dict:
        pass

    def deregister_task_from_maintenance_window(self, WindowId: str, WindowTaskId: str) -> Dict:
        pass

    def describe_activations(self, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_association(self, Name: str = None, InstanceId: str = None, AssociationId: str = None, AssociationVersion: str = None) -> Dict:
        pass

    def describe_association_execution_targets(self, AssociationId: str, ExecutionId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_association_executions(self, AssociationId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_automation_executions(self, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_automation_step_executions(self, AutomationExecutionId: str, Filters: List = None, NextToken: str = None, MaxResults: int = None, ReverseOrder: bool = None) -> Dict:
        pass

    def describe_available_patches(self, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_document(self, Name: str, DocumentVersion: str = None) -> Dict:
        pass

    def describe_document_permission(self, Name: str, PermissionType: str) -> Dict:
        pass

    def describe_effective_instance_associations(self, InstanceId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_effective_patches_for_patch_baseline(self, BaselineId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_instance_associations_status(self, InstanceId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_instance_information(self, InstanceInformationFilterList: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_instance_patch_states(self, InstanceIds: List, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_instance_patch_states_for_patch_group(self, PatchGroup: str, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_instance_patches(self, InstanceId: str, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_inventory_deletions(self, DeletionId: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_maintenance_window_execution_task_invocations(self, WindowExecutionId: str, TaskId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_maintenance_window_execution_tasks(self, WindowExecutionId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_maintenance_window_executions(self, WindowId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_maintenance_window_schedule(self, WindowId: str = None, Targets: List = None, ResourceType: str = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_maintenance_window_targets(self, WindowId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_maintenance_window_tasks(self, WindowId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_maintenance_windows(self, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_maintenance_windows_for_target(self, Targets: List, ResourceType: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_parameters(self, Filters: List = None, ParameterFilters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_patch_baselines(self, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_patch_group_state(self, PatchGroup: str) -> Dict:
        pass

    def describe_patch_groups(self, MaxResults: int = None, Filters: List = None, NextToken: str = None) -> Dict:
        pass

    def describe_sessions(self, State: str, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_automation_execution(self, AutomationExecutionId: str) -> Dict:
        pass

    def get_command_invocation(self, CommandId: str, InstanceId: str, PluginName: str = None) -> Dict:
        pass

    def get_connection_status(self, Target: str) -> Dict:
        pass

    def get_default_patch_baseline(self, OperatingSystem: str = None) -> Dict:
        pass

    def get_deployable_patch_snapshot_for_instance(self, InstanceId: str, SnapshotId: str) -> Dict:
        pass

    def get_document(self, Name: str, DocumentVersion: str = None, DocumentFormat: str = None) -> Dict:
        pass

    def get_inventory(self, Filters: List = None, Aggregators: List = None, ResultAttributes: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_inventory_schema(self, TypeName: str = None, NextToken: str = None, MaxResults: int = None, Aggregator: bool = None, SubType: bool = None) -> Dict:
        pass

    def get_maintenance_window(self, WindowId: str) -> Dict:
        pass

    def get_maintenance_window_execution(self, WindowExecutionId: str) -> Dict:
        pass

    def get_maintenance_window_execution_task(self, WindowExecutionId: str, TaskId: str) -> Dict:
        pass

    def get_maintenance_window_execution_task_invocation(self, WindowExecutionId: str, TaskId: str, InvocationId: str) -> Dict:
        pass

    def get_maintenance_window_task(self, WindowId: str, WindowTaskId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_parameter(self, Name: str, WithDecryption: bool = None) -> Dict:
        pass

    def get_parameter_history(self, Name: str, WithDecryption: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def get_parameters(self, Names: List, WithDecryption: bool = None) -> Dict:
        pass

    def get_parameters_by_path(self, Path: str, Recursive: bool = None, ParameterFilters: List = None, WithDecryption: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def get_patch_baseline(self, BaselineId: str) -> Dict:
        pass

    def get_patch_baseline_for_patch_group(self, PatchGroup: str, OperatingSystem: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def label_parameter_version(self, Name: str, Labels: List, ParameterVersion: int = None) -> Dict:
        pass

    def list_association_versions(self, AssociationId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_associations(self, AssociationFilterList: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_command_invocations(self, CommandId: str = None, InstanceId: str = None, MaxResults: int = None, NextToken: str = None, Filters: List = None, Details: bool = None) -> Dict:
        pass

    def list_commands(self, CommandId: str = None, InstanceId: str = None, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        pass

    def list_compliance_items(self, Filters: List = None, ResourceIds: List = None, ResourceTypes: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_compliance_summaries(self, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_document_versions(self, Name: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_documents(self, DocumentFilterList: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_inventory_entries(self, InstanceId: str, TypeName: str, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_resource_compliance_summaries(self, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_resource_data_sync(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceType: str, ResourceId: str) -> Dict:
        pass

    def modify_document_permission(self, Name: str, PermissionType: str, AccountIdsToAdd: List = None, AccountIdsToRemove: List = None) -> Dict:
        pass

    def put_compliance_items(self, ResourceId: str, ResourceType: str, ComplianceType: str, ExecutionSummary: Dict, Items: List, ItemContentHash: str = None) -> Dict:
        pass

    def put_inventory(self, InstanceId: str, Items: List) -> Dict:
        pass

    def put_parameter(self, Name: str, Value: str, Type: str, Description: str = None, KeyId: str = None, Overwrite: bool = None, AllowedPattern: str = None) -> Dict:
        pass

    def register_default_patch_baseline(self, BaselineId: str) -> Dict:
        pass

    def register_patch_baseline_for_patch_group(self, BaselineId: str, PatchGroup: str) -> Dict:
        pass

    def register_target_with_maintenance_window(self, WindowId: str, ResourceType: str, Targets: List, OwnerInformation: str = None, Name: str = None, Description: str = None, ClientToken: str = None) -> Dict:
        pass

    def register_task_with_maintenance_window(self, WindowId: str, Targets: List, TaskArn: str, TaskType: str, MaxConcurrency: str, MaxErrors: str, ServiceRoleArn: str = None, TaskParameters: Dict = None, TaskInvocationParameters: Dict = None, Priority: int = None, LoggingInfo: Dict = None, Name: str = None, Description: str = None, ClientToken: str = None) -> Dict:
        pass

    def remove_tags_from_resource(self, ResourceType: str, ResourceId: str, TagKeys: List) -> Dict:
        pass

    def resume_session(self, SessionId: str) -> Dict:
        pass

    def send_automation_signal(self, AutomationExecutionId: str, SignalType: str, Payload: Dict = None) -> Dict:
        pass

    def send_command(self, DocumentName: str, InstanceIds: List = None, Targets: List = None, DocumentVersion: str = None, DocumentHash: str = None, DocumentHashType: str = None, TimeoutSeconds: int = None, Comment: str = None, Parameters: Dict = None, OutputS3Region: str = None, OutputS3BucketName: str = None, OutputS3KeyPrefix: str = None, MaxConcurrency: str = None, MaxErrors: str = None, ServiceRoleArn: str = None, NotificationConfig: Dict = None, CloudWatchOutputConfig: Dict = None) -> Dict:
        pass

    def start_associations_once(self, AssociationIds: List) -> Dict:
        pass

    def start_automation_execution(self, DocumentName: str, DocumentVersion: str = None, Parameters: Dict = None, ClientToken: str = None, Mode: str = None, TargetParameterName: str = None, Targets: List = None, TargetMaps: List = None, MaxConcurrency: str = None, MaxErrors: str = None) -> Dict:
        pass

    def start_session(self, Target: str, DocumentName: str = None, Parameters: Dict = None) -> Dict:
        pass

    def stop_automation_execution(self, AutomationExecutionId: str, Type: str = None) -> Dict:
        pass

    def terminate_session(self, SessionId: str) -> Dict:
        pass

    def update_association(self, AssociationId: str, Parameters: Dict = None, DocumentVersion: str = None, ScheduleExpression: str = None, OutputLocation: Dict = None, Name: str = None, Targets: List = None, AssociationName: str = None, AssociationVersion: str = None, MaxErrors: str = None, MaxConcurrency: str = None, ComplianceSeverity: str = None) -> Dict:
        pass

    def update_association_status(self, Name: str, InstanceId: str, AssociationStatus: Dict) -> Dict:
        pass

    def update_document(self, Content: str, Name: str, DocumentVersion: str = None, DocumentFormat: str = None, TargetType: str = None) -> Dict:
        pass

    def update_document_default_version(self, Name: str, DocumentVersion: str) -> Dict:
        pass

    def update_maintenance_window(self, WindowId: str, Name: str = None, Description: str = None, StartDate: str = None, EndDate: str = None, Schedule: str = None, ScheduleTimezone: str = None, Duration: int = None, Cutoff: int = None, AllowUnassociatedTargets: bool = None, Enabled: bool = None, Replace: bool = None) -> Dict:
        pass

    def update_maintenance_window_target(self, WindowId: str, WindowTargetId: str, Targets: List = None, OwnerInformation: str = None, Name: str = None, Description: str = None, Replace: bool = None) -> Dict:
        pass

    def update_maintenance_window_task(self, WindowId: str, WindowTaskId: str, Targets: List = None, TaskArn: str = None, ServiceRoleArn: str = None, TaskParameters: Dict = None, TaskInvocationParameters: Dict = None, Priority: int = None, MaxConcurrency: str = None, MaxErrors: str = None, LoggingInfo: Dict = None, Name: str = None, Description: str = None, Replace: bool = None) -> Dict:
        pass

    def update_managed_instance_role(self, InstanceId: str, IamRole: str) -> Dict:
        pass

    def update_patch_baseline(self, BaselineId: str, Name: str = None, GlobalFilters: Dict = None, ApprovalRules: Dict = None, ApprovedPatches: List = None, ApprovedPatchesComplianceLevel: str = None, ApprovedPatchesEnableNonSecurity: bool = None, RejectedPatches: List = None, RejectedPatchesAction: str = None, Description: str = None, Sources: List = None, Replace: bool = None) -> Dict:
        pass
