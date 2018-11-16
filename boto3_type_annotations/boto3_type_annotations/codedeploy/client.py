from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def add_tags_to_on_premises_instances(self, tags: List, instanceNames: List):
        pass

    def batch_get_application_revisions(self, applicationName: str, revisions: List) -> Dict:
        pass

    def batch_get_applications(self, applicationNames: List) -> Dict:
        pass

    def batch_get_deployment_groups(self, applicationName: str, deploymentGroupNames: List) -> Dict:
        pass

    def batch_get_deployment_instances(self, deploymentId: str, instanceIds: List) -> Dict:
        pass

    def batch_get_deployments(self, deploymentIds: List) -> Dict:
        pass

    def batch_get_on_premises_instances(self, instanceNames: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def continue_deployment(self, deploymentId: str = None):
        pass

    def create_application(self, applicationName: str, computePlatform: str = None) -> Dict:
        pass

    def create_deployment(self, applicationName: str, deploymentGroupName: str = None, revision: Dict = None, deploymentConfigName: str = None, description: str = None, ignoreApplicationStopFailures: bool = None, targetInstances: Dict = None, autoRollbackConfiguration: Dict = None, updateOutdatedInstancesOnly: bool = None, fileExistsBehavior: str = None) -> Dict:
        pass

    def create_deployment_config(self, deploymentConfigName: str, minimumHealthyHosts: Dict = None, trafficRoutingConfig: Dict = None, computePlatform: str = None) -> Dict:
        pass

    def create_deployment_group(self, applicationName: str, deploymentGroupName: str, serviceRoleArn: str, deploymentConfigName: str = None, ec2TagFilters: List = None, onPremisesInstanceTagFilters: List = None, autoScalingGroups: List = None, triggerConfigurations: List = None, alarmConfiguration: Dict = None, autoRollbackConfiguration: Dict = None, deploymentStyle: Dict = None, blueGreenDeploymentConfiguration: Dict = None, loadBalancerInfo: Dict = None, ec2TagSet: Dict = None, onPremisesTagSet: Dict = None) -> Dict:
        pass

    def delete_application(self, applicationName: str):
        pass

    def delete_deployment_config(self, deploymentConfigName: str):
        pass

    def delete_deployment_group(self, applicationName: str, deploymentGroupName: str) -> Dict:
        pass

    def delete_git_hub_account_token(self, tokenName: str = None) -> Dict:
        pass

    def deregister_on_premises_instance(self, instanceName: str):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_application(self, applicationName: str) -> Dict:
        pass

    def get_application_revision(self, applicationName: str, revision: Dict) -> Dict:
        pass

    def get_deployment(self, deploymentId: str) -> Dict:
        pass

    def get_deployment_config(self, deploymentConfigName: str) -> Dict:
        pass

    def get_deployment_group(self, applicationName: str, deploymentGroupName: str) -> Dict:
        pass

    def get_deployment_instance(self, deploymentId: str, instanceId: str) -> Dict:
        pass

    def get_on_premises_instance(self, instanceName: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_application_revisions(self, applicationName: str, sortBy: str = None, sortOrder: str = None, s3Bucket: str = None, s3KeyPrefix: str = None, deployed: str = None, nextToken: str = None) -> Dict:
        pass

    def list_applications(self, nextToken: str = None) -> Dict:
        pass

    def list_deployment_configs(self, nextToken: str = None) -> Dict:
        pass

    def list_deployment_groups(self, applicationName: str, nextToken: str = None) -> Dict:
        pass

    def list_deployment_instances(self, deploymentId: str, nextToken: str = None, instanceStatusFilter: List = None, instanceTypeFilter: List = None) -> Dict:
        pass

    def list_deployments(self, applicationName: str = None, deploymentGroupName: str = None, includeOnlyStatuses: List = None, createTimeRange: Dict = None, nextToken: str = None) -> Dict:
        pass

    def list_git_hub_account_token_names(self, nextToken: str = None) -> Dict:
        pass

    def list_on_premises_instances(self, registrationStatus: str = None, tagFilters: List = None, nextToken: str = None) -> Dict:
        pass

    def put_lifecycle_event_hook_execution_status(self, deploymentId: str = None, lifecycleEventHookExecutionId: str = None, status: str = None) -> Dict:
        pass

    def register_application_revision(self, applicationName: str, revision: Dict, description: str = None):
        pass

    def register_on_premises_instance(self, instanceName: str, iamSessionArn: str = None, iamUserArn: str = None):
        pass

    def remove_tags_from_on_premises_instances(self, tags: List, instanceNames: List):
        pass

    def skip_wait_time_for_instance_termination(self, deploymentId: str = None):
        pass

    def stop_deployment(self, deploymentId: str, autoRollbackEnabled: bool = None) -> Dict:
        pass

    def update_application(self, applicationName: str = None, newApplicationName: str = None):
        pass

    def update_deployment_group(self, applicationName: str, currentDeploymentGroupName: str, newDeploymentGroupName: str = None, deploymentConfigName: str = None, ec2TagFilters: List = None, onPremisesInstanceTagFilters: List = None, autoScalingGroups: List = None, serviceRoleArn: str = None, triggerConfigurations: List = None, alarmConfiguration: Dict = None, autoRollbackConfiguration: Dict = None, deploymentStyle: Dict = None, blueGreenDeploymentConfiguration: Dict = None, loadBalancerInfo: Dict = None, ec2TagSet: Dict = None, onPremisesTagSet: Dict = None) -> Dict:
        pass
