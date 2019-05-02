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

    def cancel_task_execution(self, TaskExecutionArn: str) -> Dict:
        pass

    def create_agent(self, ActivationKey: str, AgentName: str = None, Tags: List = None) -> Dict:
        pass

    def create_location_efs(self, Subdirectory: str, EfsFilesystemArn: str, Ec2Config: Dict, Tags: List = None) -> Dict:
        pass

    def create_location_nfs(self, Subdirectory: str, ServerHostname: str, OnPremConfig: Dict, Tags: List = None) -> Dict:
        pass

    def create_location_s3(self, Subdirectory: str, S3BucketArn: str, S3Config: Dict, Tags: List = None) -> Dict:
        pass

    def create_task(self, SourceLocationArn: str, DestinationLocationArn: str, CloudWatchLogGroupArn: str = None, Name: str = None, Options: Dict = None, Tags: List = None) -> Dict:
        pass

    def delete_agent(self, AgentArn: str) -> Dict:
        pass

    def delete_location(self, LocationArn: str) -> Dict:
        pass

    def delete_task(self, TaskArn: str) -> Dict:
        pass

    def describe_agent(self, AgentArn: str) -> Dict:
        pass

    def describe_location_efs(self, LocationArn: str) -> Dict:
        pass

    def describe_location_nfs(self, LocationArn: str) -> Dict:
        pass

    def describe_location_s3(self, LocationArn: str) -> Dict:
        pass

    def describe_task(self, TaskArn: str) -> Dict:
        pass

    def describe_task_execution(self, TaskExecutionArn: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_agents(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_locations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_task_executions(self, TaskArn: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_tasks(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def start_task_execution(self, TaskArn: str, OverrideOptions: Dict = None) -> Dict:
        pass

    def tag_resource(self, ResourceArn: str, Tags: List) -> Dict:
        pass

    def untag_resource(self, ResourceArn: str, Keys: List) -> Dict:
        pass

    def update_agent(self, AgentArn: str, Name: str = None) -> Dict:
        pass

    def update_task(self, TaskArn: str, Options: Dict = None, Name: str = None) -> Dict:
        pass
