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

    def cancel_job(self, jobId: str, reason: str) -> Dict:
        pass

    def create_compute_environment(self, computeEnvironmentName: str, type: str, serviceRole: str, state: str = None, computeResources: Dict = None) -> Dict:
        pass

    def create_job_queue(self, jobQueueName: str, priority: int, computeEnvironmentOrder: List, state: str = None) -> Dict:
        pass

    def delete_compute_environment(self, computeEnvironment: str) -> Dict:
        pass

    def delete_job_queue(self, jobQueue: str) -> Dict:
        pass

    def deregister_job_definition(self, jobDefinition: str) -> Dict:
        pass

    def describe_compute_environments(self, computeEnvironments: List = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def describe_job_definitions(self, jobDefinitions: List = None, maxResults: int = None, jobDefinitionName: str = None, status: str = None, nextToken: str = None) -> Dict:
        pass

    def describe_job_queues(self, jobQueues: List = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def describe_jobs(self, jobs: List) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_jobs(self, jobQueue: str = None, arrayJobId: str = None, jobStatus: str = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def register_job_definition(self, jobDefinitionName: str, type: str, parameters: Dict = None, containerProperties: Dict = None, retryStrategy: Dict = None, timeout: Dict = None) -> Dict:
        pass

    def submit_job(self, jobName: str, jobQueue: str, jobDefinition: str, arrayProperties: Dict = None, dependsOn: List = None, parameters: Dict = None, containerOverrides: Dict = None, retryStrategy: Dict = None, timeout: Dict = None) -> Dict:
        pass

    def terminate_job(self, jobId: str, reason: str) -> Dict:
        pass

    def update_compute_environment(self, computeEnvironment: str, state: str = None, computeResources: Dict = None, serviceRole: str = None) -> Dict:
        pass

    def update_job_queue(self, jobQueue: str, state: str = None, priority: int = None, computeEnvironmentOrder: List = None) -> Dict:
        pass
