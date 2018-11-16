from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def accept_certificate_transfer(self, certificateId: str, setAsActive: bool = None):
        pass

    def add_thing_to_thing_group(self, thingGroupName: str = None, thingGroupArn: str = None, thingName: str = None, thingArn: str = None) -> Dict:
        pass

    def associate_targets_with_job(self, targets: List, jobId: str, comment: str = None) -> Dict:
        pass

    def attach_policy(self, policyName: str, target: str):
        pass

    def attach_principal_policy(self, policyName: str, principal: str):
        pass

    def attach_security_profile(self, securityProfileName: str, securityProfileTargetArn: str) -> Dict:
        pass

    def attach_thing_principal(self, thingName: str, principal: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def cancel_audit_task(self, taskId: str) -> Dict:
        pass

    def cancel_certificate_transfer(self, certificateId: str):
        pass

    def cancel_job(self, jobId: str, comment: str = None, force: bool = None) -> Dict:
        pass

    def cancel_job_execution(self, jobId: str, thingName: str, force: bool = None, expectedVersion: int = None, statusDetails: Dict = None):
        pass

    def clear_default_authorizer(self) -> Dict:
        pass

    def create_authorizer(self, authorizerName: str, authorizerFunctionArn: str, tokenKeyName: str, tokenSigningPublicKeys: Dict, status: str = None) -> Dict:
        pass

    def create_certificate_from_csr(self, certificateSigningRequest: str, setAsActive: bool = None) -> Dict:
        pass

    def create_job(self, jobId: str, targets: List, documentSource: str = None, document: str = None, description: str = None, presignedUrlConfig: Dict = None, targetSelection: str = None, jobExecutionsRolloutConfig: Dict = None, timeoutConfig: Dict = None) -> Dict:
        pass

    def create_keys_and_certificate(self, setAsActive: bool = None) -> Dict:
        pass

    def create_ota_update(self, otaUpdateId: str, targets: List, files: List, roleArn: str, description: str = None, targetSelection: str = None, awsJobExecutionsRolloutConfig: Dict = None, additionalParameters: Dict = None) -> Dict:
        pass

    def create_policy(self, policyName: str, policyDocument: str) -> Dict:
        pass

    def create_policy_version(self, policyName: str, policyDocument: str, setAsDefault: bool = None) -> Dict:
        pass

    def create_role_alias(self, roleAlias: str, roleArn: str, credentialDurationSeconds: int = None) -> Dict:
        pass

    def create_scheduled_audit(self, frequency: str, targetCheckNames: List, scheduledAuditName: str, dayOfMonth: str = None, dayOfWeek: str = None) -> Dict:
        pass

    def create_security_profile(self, securityProfileName: str, behaviors: List, securityProfileDescription: str = None, alertTargets: Dict = None) -> Dict:
        pass

    def create_stream(self, streamId: str, files: List, roleArn: str, description: str = None) -> Dict:
        pass

    def create_thing(self, thingName: str, thingTypeName: str = None, attributePayload: Dict = None) -> Dict:
        pass

    def create_thing_group(self, thingGroupName: str, parentGroupName: str = None, thingGroupProperties: Dict = None) -> Dict:
        pass

    def create_thing_type(self, thingTypeName: str, thingTypeProperties: Dict = None) -> Dict:
        pass

    def create_topic_rule(self, ruleName: str, topicRulePayload: Dict):
        pass

    def delete_account_audit_configuration(self, deleteScheduledAudits: bool = None) -> Dict:
        pass

    def delete_authorizer(self, authorizerName: str) -> Dict:
        pass

    def delete_ca_certificate(self, certificateId: str) -> Dict:
        pass

    def delete_certificate(self, certificateId: str, forceDelete: bool = None):
        pass

    def delete_job(self, jobId: str, force: bool = None):
        pass

    def delete_job_execution(self, jobId: str, thingName: str, executionNumber: int, force: bool = None):
        pass

    def delete_ota_update(self, otaUpdateId: str, deleteStream: bool = None, forceDeleteAWSJob: bool = None) -> Dict:
        pass

    def delete_policy(self, policyName: str):
        pass

    def delete_policy_version(self, policyName: str, policyVersionId: str):
        pass

    def delete_registration_code(self) -> Dict:
        pass

    def delete_role_alias(self, roleAlias: str) -> Dict:
        pass

    def delete_scheduled_audit(self, scheduledAuditName: str) -> Dict:
        pass

    def delete_security_profile(self, securityProfileName: str, expectedVersion: int = None) -> Dict:
        pass

    def delete_stream(self, streamId: str) -> Dict:
        pass

    def delete_thing(self, thingName: str, expectedVersion: int = None) -> Dict:
        pass

    def delete_thing_group(self, thingGroupName: str, expectedVersion: int = None) -> Dict:
        pass

    def delete_thing_type(self, thingTypeName: str) -> Dict:
        pass

    def delete_topic_rule(self, ruleName: str):
        pass

    def delete_v2_logging_level(self, targetType: str, targetName: str):
        pass

    def deprecate_thing_type(self, thingTypeName: str, undoDeprecate: bool = None) -> Dict:
        pass

    def describe_account_audit_configuration(self) -> Dict:
        pass

    def describe_audit_task(self, taskId: str) -> Dict:
        pass

    def describe_authorizer(self, authorizerName: str) -> Dict:
        pass

    def describe_ca_certificate(self, certificateId: str) -> Dict:
        pass

    def describe_certificate(self, certificateId: str) -> Dict:
        pass

    def describe_default_authorizer(self) -> Dict:
        pass

    def describe_endpoint(self, endpointType: str = None) -> Dict:
        pass

    def describe_event_configurations(self) -> Dict:
        pass

    def describe_index(self, indexName: str) -> Dict:
        pass

    def describe_job(self, jobId: str) -> Dict:
        pass

    def describe_job_execution(self, jobId: str, thingName: str, executionNumber: int = None) -> Dict:
        pass

    def describe_role_alias(self, roleAlias: str) -> Dict:
        pass

    def describe_scheduled_audit(self, scheduledAuditName: str) -> Dict:
        pass

    def describe_security_profile(self, securityProfileName: str) -> Dict:
        pass

    def describe_stream(self, streamId: str) -> Dict:
        pass

    def describe_thing(self, thingName: str) -> Dict:
        pass

    def describe_thing_group(self, thingGroupName: str) -> Dict:
        pass

    def describe_thing_registration_task(self, taskId: str) -> Dict:
        pass

    def describe_thing_type(self, thingTypeName: str) -> Dict:
        pass

    def detach_policy(self, policyName: str, target: str):
        pass

    def detach_principal_policy(self, policyName: str, principal: str):
        pass

    def detach_security_profile(self, securityProfileName: str, securityProfileTargetArn: str) -> Dict:
        pass

    def detach_thing_principal(self, thingName: str, principal: str) -> Dict:
        pass

    def disable_topic_rule(self, ruleName: str):
        pass

    def enable_topic_rule(self, ruleName: str):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_effective_policies(self, principal: str = None, cognitoIdentityPoolId: str = None, thingName: str = None) -> Dict:
        pass

    def get_indexing_configuration(self) -> Dict:
        pass

    def get_job_document(self, jobId: str) -> Dict:
        pass

    def get_logging_options(self) -> Dict:
        pass

    def get_ota_update(self, otaUpdateId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_policy(self, policyName: str) -> Dict:
        pass

    def get_policy_version(self, policyName: str, policyVersionId: str) -> Dict:
        pass

    def get_registration_code(self) -> Dict:
        pass

    def get_topic_rule(self, ruleName: str) -> Dict:
        pass

    def get_v2_logging_options(self) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_active_violations(self, thingName: str = None, securityProfileName: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_attached_policies(self, target: str, recursive: bool = None, marker: str = None, pageSize: int = None) -> Dict:
        pass

    def list_audit_findings(self, taskId: str = None, checkName: str = None, resourceIdentifier: Dict = None, maxResults: int = None, nextToken: str = None, startTime: datetime = None, endTime: datetime = None) -> Dict:
        pass

    def list_audit_tasks(self, startTime: datetime, endTime: datetime, taskType: str = None, taskStatus: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_authorizers(self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None, status: str = None) -> Dict:
        pass

    def list_ca_certificates(self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None) -> Dict:
        pass

    def list_certificates(self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None) -> Dict:
        pass

    def list_certificates_by_ca(self, caCertificateId: str, pageSize: int = None, marker: str = None, ascendingOrder: bool = None) -> Dict:
        pass

    def list_indices(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_job_executions_for_job(self, jobId: str, status: str = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def list_job_executions_for_thing(self, thingName: str, status: str = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def list_jobs(self, status: str = None, targetSelection: str = None, maxResults: int = None, nextToken: str = None, thingGroupName: str = None, thingGroupId: str = None) -> Dict:
        pass

    def list_ota_updates(self, maxResults: int = None, nextToken: str = None, otaUpdateStatus: str = None) -> Dict:
        pass

    def list_outgoing_certificates(self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None) -> Dict:
        pass

    def list_policies(self, marker: str = None, pageSize: int = None, ascendingOrder: bool = None) -> Dict:
        pass

    def list_policy_principals(self, policyName: str, marker: str = None, pageSize: int = None, ascendingOrder: bool = None) -> Dict:
        pass

    def list_policy_versions(self, policyName: str) -> Dict:
        pass

    def list_principal_policies(self, principal: str, marker: str = None, pageSize: int = None, ascendingOrder: bool = None) -> Dict:
        pass

    def list_principal_things(self, principal: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_role_aliases(self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None) -> Dict:
        pass

    def list_scheduled_audits(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_security_profiles(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_security_profiles_for_target(self, securityProfileTargetArn: str, nextToken: str = None, maxResults: int = None, recursive: bool = None) -> Dict:
        pass

    def list_streams(self, maxResults: int = None, nextToken: str = None, ascendingOrder: bool = None) -> Dict:
        pass

    def list_targets_for_policy(self, policyName: str, marker: str = None, pageSize: int = None) -> Dict:
        pass

    def list_targets_for_security_profile(self, securityProfileName: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_thing_groups(self, nextToken: str = None, maxResults: int = None, parentGroup: str = None, namePrefixFilter: str = None, recursive: bool = None) -> Dict:
        pass

    def list_thing_groups_for_thing(self, thingName: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_thing_principals(self, thingName: str) -> Dict:
        pass

    def list_thing_registration_task_reports(self, taskId: str, reportType: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_thing_registration_tasks(self, nextToken: str = None, maxResults: int = None, status: str = None) -> Dict:
        pass

    def list_thing_types(self, nextToken: str = None, maxResults: int = None, thingTypeName: str = None) -> Dict:
        pass

    def list_things(self, nextToken: str = None, maxResults: int = None, attributeName: str = None, attributeValue: str = None, thingTypeName: str = None) -> Dict:
        pass

    def list_things_in_thing_group(self, thingGroupName: str, recursive: bool = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_topic_rules(self, topic: str = None, maxResults: int = None, nextToken: str = None, ruleDisabled: bool = None) -> Dict:
        pass

    def list_v2_logging_levels(self, targetType: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_violation_events(self, startTime: datetime, endTime: datetime, thingName: str = None, securityProfileName: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def register_ca_certificate(self, caCertificate: str, verificationCertificate: str, setAsActive: bool = None, allowAutoRegistration: bool = None, registrationConfig: Dict = None) -> Dict:
        pass

    def register_certificate(self, certificatePem: str, caCertificatePem: str = None, setAsActive: bool = None, status: str = None) -> Dict:
        pass

    def register_thing(self, templateBody: str, parameters: Dict = None) -> Dict:
        pass

    def reject_certificate_transfer(self, certificateId: str, rejectReason: str = None):
        pass

    def remove_thing_from_thing_group(self, thingGroupName: str = None, thingGroupArn: str = None, thingName: str = None, thingArn: str = None) -> Dict:
        pass

    def replace_topic_rule(self, ruleName: str, topicRulePayload: Dict):
        pass

    def search_index(self, queryString: str, indexName: str = None, nextToken: str = None, maxResults: int = None, queryVersion: str = None) -> Dict:
        pass

    def set_default_authorizer(self, authorizerName: str) -> Dict:
        pass

    def set_default_policy_version(self, policyName: str, policyVersionId: str):
        pass

    def set_logging_options(self, loggingOptionsPayload: Dict):
        pass

    def set_v2_logging_level(self, logTarget: Dict, logLevel: str):
        pass

    def set_v2_logging_options(self, roleArn: str = None, defaultLogLevel: str = None, disableAllLogs: bool = None):
        pass

    def start_on_demand_audit_task(self, targetCheckNames: List) -> Dict:
        pass

    def start_thing_registration_task(self, templateBody: str, inputFileBucket: str, inputFileKey: str, roleArn: str) -> Dict:
        pass

    def stop_thing_registration_task(self, taskId: str) -> Dict:
        pass

    def test_authorization(self, authInfos: List, principal: str = None, cognitoIdentityPoolId: str = None, clientId: str = None, policyNamesToAdd: List = None, policyNamesToSkip: List = None) -> Dict:
        pass

    def test_invoke_authorizer(self, authorizerName: str, token: str, tokenSignature: str) -> Dict:
        pass

    def transfer_certificate(self, certificateId: str, targetAwsAccount: str, transferMessage: str = None) -> Dict:
        pass

    def update_account_audit_configuration(self, roleArn: str = None, auditNotificationTargetConfigurations: Dict = None, auditCheckConfigurations: Dict = None) -> Dict:
        pass

    def update_authorizer(self, authorizerName: str, authorizerFunctionArn: str = None, tokenKeyName: str = None, tokenSigningPublicKeys: Dict = None, status: str = None) -> Dict:
        pass

    def update_ca_certificate(self, certificateId: str, newStatus: str = None, newAutoRegistrationStatus: str = None, registrationConfig: Dict = None, removeAutoRegistration: bool = None):
        pass

    def update_certificate(self, certificateId: str, newStatus: str):
        pass

    def update_event_configurations(self, eventConfigurations: Dict = None) -> Dict:
        pass

    def update_indexing_configuration(self, thingIndexingConfiguration: Dict = None, thingGroupIndexingConfiguration: Dict = None) -> Dict:
        pass

    def update_role_alias(self, roleAlias: str, roleArn: str = None, credentialDurationSeconds: int = None) -> Dict:
        pass

    def update_scheduled_audit(self, scheduledAuditName: str, frequency: str = None, dayOfMonth: str = None, dayOfWeek: str = None, targetCheckNames: List = None) -> Dict:
        pass

    def update_security_profile(self, securityProfileName: str, securityProfileDescription: str = None, behaviors: List = None, alertTargets: Dict = None, expectedVersion: int = None) -> Dict:
        pass

    def update_stream(self, streamId: str, description: str = None, files: List = None, roleArn: str = None) -> Dict:
        pass

    def update_thing(self, thingName: str, thingTypeName: str = None, attributePayload: Dict = None, expectedVersion: int = None, removeThingType: bool = None) -> Dict:
        pass

    def update_thing_group(self, thingGroupName: str, thingGroupProperties: Dict, expectedVersion: int = None) -> Dict:
        pass

    def update_thing_groups_for_thing(self, thingName: str = None, thingGroupsToAdd: List = None, thingGroupsToRemove: List = None) -> Dict:
        pass

    def validate_security_profile_behaviors(self, behaviors: List) -> Dict:
        pass
