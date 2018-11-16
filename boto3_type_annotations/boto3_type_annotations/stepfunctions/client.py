from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_activity(self, name: str) -> Dict:
        pass

    def create_state_machine(self, name: str, definition: str, roleArn: str) -> Dict:
        pass

    def delete_activity(self, activityArn: str) -> Dict:
        pass

    def delete_state_machine(self, stateMachineArn: str) -> Dict:
        pass

    def describe_activity(self, activityArn: str) -> Dict:
        pass

    def describe_execution(self, executionArn: str) -> Dict:
        pass

    def describe_state_machine(self, stateMachineArn: str) -> Dict:
        pass

    def describe_state_machine_for_execution(self, executionArn: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_activity_task(self, activityArn: str, workerName: str = None) -> Dict:
        pass

    def get_execution_history(self, executionArn: str, maxResults: int = None, reverseOrder: bool = None, nextToken: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_activities(self, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def list_executions(self, stateMachineArn: str, statusFilter: str = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def list_state_machines(self, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def send_task_failure(self, taskToken: str, error: str = None, cause: str = None) -> Dict:
        pass

    def send_task_heartbeat(self, taskToken: str) -> Dict:
        pass

    def send_task_success(self, taskToken: str, output: str) -> Dict:
        pass

    def start_execution(self, stateMachineArn: str, name: str = None, input: str = None) -> Dict:
        pass

    def stop_execution(self, executionArn: str, error: str = None, cause: str = None) -> Dict:
        pass

    def update_state_machine(self, stateMachineArn: str, definition: str = None, roleArn: str = None) -> Dict:
        pass
