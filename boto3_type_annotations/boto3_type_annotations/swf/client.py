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

    def count_closed_workflow_executions(self, domain: str, startTimeFilter: Dict = None, closeTimeFilter: Dict = None, executionFilter: Dict = None, typeFilter: Dict = None, tagFilter: Dict = None, closeStatusFilter: Dict = None) -> Dict:
        pass

    def count_open_workflow_executions(self, domain: str, startTimeFilter: Dict, typeFilter: Dict = None, tagFilter: Dict = None, executionFilter: Dict = None) -> Dict:
        pass

    def count_pending_activity_tasks(self, domain: str, taskList: Dict) -> Dict:
        pass

    def count_pending_decision_tasks(self, domain: str, taskList: Dict) -> Dict:
        pass

    def deprecate_activity_type(self, domain: str, activityType: Dict) -> NoReturn:
        pass

    def deprecate_domain(self, name: str) -> NoReturn:
        pass

    def deprecate_workflow_type(self, domain: str, workflowType: Dict) -> NoReturn:
        pass

    def describe_activity_type(self, domain: str, activityType: Dict) -> Dict:
        pass

    def describe_domain(self, name: str) -> Dict:
        pass

    def describe_workflow_execution(self, domain: str, execution: Dict) -> Dict:
        pass

    def describe_workflow_type(self, domain: str, workflowType: Dict) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def get_workflow_execution_history(self, domain: str, execution: Dict, nextPageToken: str = None, maximumPageSize: int = None, reverseOrder: bool = None) -> Dict:
        pass

    def list_activity_types(self, domain: str, registrationStatus: str, name: str = None, nextPageToken: str = None, maximumPageSize: int = None, reverseOrder: bool = None) -> Dict:
        pass

    def list_closed_workflow_executions(self, domain: str, startTimeFilter: Dict = None, closeTimeFilter: Dict = None, executionFilter: Dict = None, closeStatusFilter: Dict = None, typeFilter: Dict = None, tagFilter: Dict = None, nextPageToken: str = None, maximumPageSize: int = None, reverseOrder: bool = None) -> Dict:
        pass

    def list_domains(self, registrationStatus: str, nextPageToken: str = None, maximumPageSize: int = None, reverseOrder: bool = None) -> Dict:
        pass

    def list_open_workflow_executions(self, domain: str, startTimeFilter: Dict, typeFilter: Dict = None, tagFilter: Dict = None, nextPageToken: str = None, maximumPageSize: int = None, reverseOrder: bool = None, executionFilter: Dict = None) -> Dict:
        pass

    def list_workflow_types(self, domain: str, registrationStatus: str, name: str = None, nextPageToken: str = None, maximumPageSize: int = None, reverseOrder: bool = None) -> Dict:
        pass

    def poll_for_activity_task(self, domain: str, taskList: Dict, identity: str = None) -> Dict:
        pass

    def poll_for_decision_task(self, domain: str, taskList: Dict, identity: str = None, nextPageToken: str = None, maximumPageSize: int = None, reverseOrder: bool = None) -> Dict:
        pass

    def record_activity_task_heartbeat(self, taskToken: str, details: str = None) -> Dict:
        pass

    def register_activity_type(self, domain: str, name: str, version: str, description: str = None, defaultTaskStartToCloseTimeout: str = None, defaultTaskHeartbeatTimeout: str = None, defaultTaskList: Dict = None, defaultTaskPriority: str = None, defaultTaskScheduleToStartTimeout: str = None, defaultTaskScheduleToCloseTimeout: str = None) -> NoReturn:
        pass

    def register_domain(self, name: str, workflowExecutionRetentionPeriodInDays: str, description: str = None) -> NoReturn:
        pass

    def register_workflow_type(self, domain: str, name: str, version: str, description: str = None, defaultTaskStartToCloseTimeout: str = None, defaultExecutionStartToCloseTimeout: str = None, defaultTaskList: Dict = None, defaultTaskPriority: str = None, defaultChildPolicy: str = None, defaultLambdaRole: str = None) -> NoReturn:
        pass

    def request_cancel_workflow_execution(self, domain: str, workflowId: str, runId: str = None) -> NoReturn:
        pass

    def respond_activity_task_canceled(self, taskToken: str, details: str = None) -> NoReturn:
        pass

    def respond_activity_task_completed(self, taskToken: str, result: str = None) -> NoReturn:
        pass

    def respond_activity_task_failed(self, taskToken: str, reason: str = None, details: str = None) -> NoReturn:
        pass

    def respond_decision_task_completed(self, taskToken: str, decisions: List = None, executionContext: str = None) -> NoReturn:
        pass

    def signal_workflow_execution(self, domain: str, workflowId: str, signalName: str, runId: str = None, input: str = None) -> NoReturn:
        pass

    def start_workflow_execution(self, domain: str, workflowId: str, workflowType: Dict, taskList: Dict = None, taskPriority: str = None, input: str = None, executionStartToCloseTimeout: str = None, tagList: List = None, taskStartToCloseTimeout: str = None, childPolicy: str = None, lambdaRole: str = None) -> Dict:
        pass

    def terminate_workflow_execution(self, domain: str, workflowId: str, runId: str = None, reason: str = None, details: str = None, childPolicy: str = None) -> NoReturn:
        pass
