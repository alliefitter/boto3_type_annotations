from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def batch_describe_simulation_job(self, jobs: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def cancel_simulation_job(self, job: str) -> Dict:
        pass

    def create_deployment_job(self, clientRequestToken: str, fleet: str, deploymentApplicationConfigs: List, deploymentConfig: Dict = None, tags: Dict = None) -> Dict:
        pass

    def create_fleet(self, name: str, tags: Dict = None) -> Dict:
        pass

    def create_robot(self, name: str, architecture: str, greengrassGroupId: str, tags: Dict = None) -> Dict:
        pass

    def create_robot_application(self, name: str, sources: List, robotSoftwareSuite: Dict, tags: Dict = None) -> Dict:
        pass

    def create_robot_application_version(self, application: str, currentRevisionId: str = None) -> Dict:
        pass

    def create_simulation_application(self, name: str, sources: List, simulationSoftwareSuite: Dict, robotSoftwareSuite: Dict, renderingEngine: Dict, tags: Dict = None) -> Dict:
        pass

    def create_simulation_application_version(self, application: str, currentRevisionId: str = None) -> Dict:
        pass

    def create_simulation_job(self, maxJobDurationInSeconds: int, iamRole: str, clientRequestToken: str = None, outputLocation: Dict = None, failureBehavior: str = None, robotApplications: List = None, simulationApplications: List = None, tags: Dict = None, vpcConfig: Dict = None) -> Dict:
        pass

    def delete_fleet(self, fleet: str) -> Dict:
        pass

    def delete_robot(self, robot: str) -> Dict:
        pass

    def delete_robot_application(self, application: str, applicationVersion: str = None) -> Dict:
        pass

    def delete_simulation_application(self, application: str, applicationVersion: str = None) -> Dict:
        pass

    def deregister_robot(self, fleet: str, robot: str) -> Dict:
        pass

    def describe_deployment_job(self, job: str) -> Dict:
        pass

    def describe_fleet(self, fleet: str) -> Dict:
        pass

    def describe_robot(self, robot: str) -> Dict:
        pass

    def describe_robot_application(self, application: str, applicationVersion: str = None) -> Dict:
        pass

    def describe_simulation_application(self, application: str, applicationVersion: str = None) -> Dict:
        pass

    def describe_simulation_job(self, job: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_deployment_jobs(self, filters: List = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_fleets(self, nextToken: str = None, maxResults: int = None, filters: List = None) -> Dict:
        pass

    def list_robot_applications(self, versionQualifier: str = None, nextToken: str = None, maxResults: int = None, filters: List = None) -> Dict:
        pass

    def list_robots(self, nextToken: str = None, maxResults: int = None, filters: List = None) -> Dict:
        pass

    def list_simulation_applications(self, versionQualifier: str = None, nextToken: str = None, maxResults: int = None, filters: List = None) -> Dict:
        pass

    def list_simulation_jobs(self, nextToken: str = None, maxResults: int = None, filters: List = None) -> Dict:
        pass

    def list_tags_for_resource(self, resourceArn: str) -> Dict:
        pass

    def register_robot(self, fleet: str, robot: str) -> Dict:
        pass

    def restart_simulation_job(self, job: str) -> Dict:
        pass

    def sync_deployment_job(self, clientRequestToken: str, fleet: str) -> Dict:
        pass

    def tag_resource(self, resourceArn: str, tags: Dict) -> Dict:
        pass

    def untag_resource(self, resourceArn: str, tagKeys: List) -> Dict:
        pass

    def update_robot_application(self, application: str, sources: List, robotSoftwareSuite: Dict, currentRevisionId: str = None) -> Dict:
        pass

    def update_simulation_application(self, application: str, sources: List, simulationSoftwareSuite: Dict, robotSoftwareSuite: Dict, renderingEngine: Dict, currentRevisionId: str = None) -> Dict:
        pass
