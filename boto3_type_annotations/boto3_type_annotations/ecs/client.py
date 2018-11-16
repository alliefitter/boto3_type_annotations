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
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_cluster(self, clusterName: str = None) -> Dict:
        pass

    def create_service(self, serviceName: str, taskDefinition: str, cluster: str = None, loadBalancers: List = None, serviceRegistries: List = None, desiredCount: int = None, clientToken: str = None, launchType: str = None, platformVersion: str = None, role: str = None, deploymentConfiguration: Dict = None, placementConstraints: List = None, placementStrategy: List = None, networkConfiguration: Dict = None, healthCheckGracePeriodSeconds: int = None, schedulingStrategy: str = None) -> Dict:
        pass

    def delete_attributes(self, attributes: List, cluster: str = None) -> Dict:
        pass

    def delete_cluster(self, cluster: str) -> Dict:
        pass

    def delete_service(self, service: str, cluster: str = None, force: bool = None) -> Dict:
        pass

    def deregister_container_instance(self, containerInstance: str, cluster: str = None, force: bool = None) -> Dict:
        pass

    def deregister_task_definition(self, taskDefinition: str) -> Dict:
        pass

    def describe_clusters(self, clusters: List = None, include: List = None) -> Dict:
        pass

    def describe_container_instances(self, containerInstances: List, cluster: str = None) -> Dict:
        pass

    def describe_services(self, services: List, cluster: str = None) -> Dict:
        pass

    def describe_task_definition(self, taskDefinition: str) -> Dict:
        pass

    def describe_tasks(self, tasks: List, cluster: str = None) -> Dict:
        pass

    def discover_poll_endpoint(self, containerInstance: str = None, cluster: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_attributes(self, targetType: str, cluster: str = None, attributeName: str = None, attributeValue: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_clusters(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_container_instances(self, cluster: str = None, filter: str = None, nextToken: str = None, maxResults: int = None, status: str = None) -> Dict:
        pass

    def list_services(self, cluster: str = None, nextToken: str = None, maxResults: int = None, launchType: str = None, schedulingStrategy: str = None) -> Dict:
        pass

    def list_task_definition_families(self, familyPrefix: str = None, status: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_task_definitions(self, familyPrefix: str = None, status: str = None, sort: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_tasks(self, cluster: str = None, containerInstance: str = None, family: str = None, nextToken: str = None, maxResults: int = None, startedBy: str = None, serviceName: str = None, desiredStatus: str = None, launchType: str = None) -> Dict:
        pass

    def put_attributes(self, attributes: List, cluster: str = None) -> Dict:
        pass

    def register_container_instance(self, cluster: str = None, instanceIdentityDocument: str = None, instanceIdentityDocumentSignature: str = None, totalResources: List = None, versionInfo: Dict = None, containerInstanceArn: str = None, attributes: List = None) -> Dict:
        pass

    def register_task_definition(self, family: str, containerDefinitions: List, taskRoleArn: str = None, executionRoleArn: str = None, networkMode: str = None, volumes: List = None, placementConstraints: List = None, requiresCompatibilities: List = None, cpu: str = None, memory: str = None) -> Dict:
        pass

    def run_task(self, taskDefinition: str, cluster: str = None, overrides: Dict = None, count: int = None, startedBy: str = None, group: str = None, placementConstraints: List = None, placementStrategy: List = None, launchType: str = None, platformVersion: str = None, networkConfiguration: Dict = None) -> Dict:
        pass

    def start_task(self, taskDefinition: str, containerInstances: List, cluster: str = None, overrides: Dict = None, startedBy: str = None, group: str = None, networkConfiguration: Dict = None) -> Dict:
        pass

    def stop_task(self, task: str, cluster: str = None, reason: str = None) -> Dict:
        pass

    def submit_container_state_change(self, cluster: str = None, task: str = None, containerName: str = None, status: str = None, exitCode: int = None, reason: str = None, networkBindings: List = None) -> Dict:
        pass

    def submit_task_state_change(self, cluster: str = None, task: str = None, status: str = None, reason: str = None, containers: List = None, attachments: List = None, pullStartedAt: datetime = None, pullStoppedAt: datetime = None, executionStoppedAt: datetime = None) -> Dict:
        pass

    def update_container_agent(self, containerInstance: str, cluster: str = None) -> Dict:
        pass

    def update_container_instances_state(self, containerInstances: List, status: str, cluster: str = None) -> Dict:
        pass

    def update_service(self, service: str, cluster: str = None, desiredCount: int = None, taskDefinition: str = None, deploymentConfiguration: Dict = None, networkConfiguration: Dict = None, platformVersion: str = None, forceNewDeployment: bool = None, healthCheckGracePeriodSeconds: int = None) -> Dict:
        pass
