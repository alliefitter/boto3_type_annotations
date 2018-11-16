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

    def create_environment_ec2(self, name: str, instanceType: str, description: str = None, clientRequestToken: str = None, subnetId: str = None, automaticStopTimeMinutes: int = None, ownerArn: str = None) -> Dict:
        pass

    def create_environment_membership(self, environmentId: str, userArn: str, permissions: str) -> Dict:
        pass

    def delete_environment(self, environmentId: str) -> Dict:
        pass

    def delete_environment_membership(self, environmentId: str, userArn: str) -> Dict:
        pass

    def describe_environment_memberships(self, userArn: str = None, environmentId: str = None, permissions: List = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def describe_environment_status(self, environmentId: str) -> Dict:
        pass

    def describe_environments(self, environmentIds: List) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_environments(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def update_environment(self, environmentId: str, name: str = None, description: str = None) -> Dict:
        pass

    def update_environment_membership(self, environmentId: str, userArn: str, permissions: str) -> Dict:
        pass
