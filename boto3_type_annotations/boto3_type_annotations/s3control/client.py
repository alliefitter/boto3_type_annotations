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

    def create_job(self, AccountId: str, Operation: Dict, Report: Dict, ClientRequestToken: str, Manifest: Dict, Priority: int, RoleArn: str, ConfirmationRequired: bool = None, Description: str = None) -> Dict:
        pass

    def delete_public_access_block(self, AccountId: str):
        pass

    def describe_job(self, AccountId: str, JobId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_public_access_block(self, AccountId: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_jobs(self, AccountId: str, JobStatuses: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def put_public_access_block(self, PublicAccessBlockConfiguration: Dict, AccountId: str):
        pass

    def update_job_priority(self, AccountId: str, JobId: str, Priority: int) -> Dict:
        pass

    def update_job_status(self, AccountId: str, JobId: str, RequestedJobStatus: str, StatusUpdateReason: str = None) -> Dict:
        pass
