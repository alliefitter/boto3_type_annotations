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

    def describe_job_execution(self, jobId: str, thingName: str, includeJobDocument: bool = None, executionNumber: int = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_pending_job_executions(self, thingName: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def start_next_pending_job_execution(self, thingName: str, statusDetails: Dict = None, stepTimeoutInMinutes: int = None) -> Dict:
        pass

    def update_job_execution(self, jobId: str, thingName: str, status: str, statusDetails: Dict = None, stepTimeoutInMinutes: int = None, expectedVersion: int = None, includeJobExecutionState: bool = None, includeJobDocument: bool = None, executionNumber: int = None) -> Dict:
        pass
