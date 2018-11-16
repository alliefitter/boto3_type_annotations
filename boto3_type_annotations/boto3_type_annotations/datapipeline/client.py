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
    def activate_pipeline(self, pipelineId: str, parameterValues: List = None, startTimestamp: datetime = None) -> Dict:
        pass

    def add_tags(self, pipelineId: str, tags: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_pipeline(self, name: str, uniqueId: str, description: str = None, tags: List = None) -> Dict:
        pass

    def deactivate_pipeline(self, pipelineId: str, cancelActive: bool = None) -> Dict:
        pass

    def delete_pipeline(self, pipelineId: str) -> NoReturn:
        pass

    def describe_objects(self, pipelineId: str, objectIds: List, evaluateExpressions: bool = None, marker: str = None) -> Dict:
        pass

    def describe_pipelines(self, pipelineIds: List) -> Dict:
        pass

    def evaluate_expression(self, pipelineId: str, objectId: str, expression: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_pipeline_definition(self, pipelineId: str, version: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_pipelines(self, marker: str = None) -> Dict:
        pass

    def poll_for_task(self, workerGroup: str, hostname: str = None, instanceIdentity: Dict = None) -> Dict:
        pass

    def put_pipeline_definition(self, pipelineId: str, pipelineObjects: List, parameterObjects: List = None, parameterValues: List = None) -> Dict:
        pass

    def query_objects(self, pipelineId: str, sphere: str, query: Dict = None, marker: str = None, limit: int = None) -> Dict:
        pass

    def remove_tags(self, pipelineId: str, tagKeys: List) -> Dict:
        pass

    def report_task_progress(self, taskId: str, fields: List = None) -> Dict:
        pass

    def report_task_runner_heartbeat(self, taskrunnerId: str, workerGroup: str = None, hostname: str = None) -> Dict:
        pass

    def set_status(self, pipelineId: str, objectIds: List, status: str) -> NoReturn:
        pass

    def set_task_status(self, taskId: str, taskStatus: str, errorId: str = None, errorMessage: str = None, errorStackTrace: str = None) -> Dict:
        pass

    def validate_pipeline_definition(self, pipelineId: str, pipelineObjects: List, parameterObjects: List = None, parameterValues: List = None) -> Dict:
        pass
