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

    def create_container(self, ContainerName: str) -> Dict:
        pass

    def delete_container(self, ContainerName: str) -> Dict:
        pass

    def delete_container_policy(self, ContainerName: str) -> Dict:
        pass

    def delete_cors_policy(self, ContainerName: str) -> Dict:
        pass

    def describe_container(self, ContainerName: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_container_policy(self, ContainerName: str) -> Dict:
        pass

    def get_cors_policy(self, ContainerName: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_containers(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def put_container_policy(self, ContainerName: str, Policy: str) -> Dict:
        pass

    def put_cors_policy(self, ContainerName: str, CorsPolicy: List) -> Dict:
        pass
