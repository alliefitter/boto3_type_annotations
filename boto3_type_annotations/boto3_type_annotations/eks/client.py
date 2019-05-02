from typing import Optional
from botocore.client import BaseClient
from botocore.waiter import Waiter
from typing import Union
from typing import Dict
from botocore.paginate import Paginator


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_cluster(self, name: str, roleArn: str, resourcesVpcConfig: Dict, version: str = None, logging: Dict = None, clientRequestToken: str = None) -> Dict:
        pass

    def delete_cluster(self, name: str) -> Dict:
        pass

    def describe_cluster(self, name: str) -> Dict:
        pass

    def describe_update(self, name: str, updateId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_clusters(self, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def list_updates(self, name: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def update_cluster_config(self, name: str, resourcesVpcConfig: Dict = None, logging: Dict = None, clientRequestToken: str = None) -> Dict:
        pass

    def update_cluster_version(self, name: str, version: str, clientRequestToken: str = None) -> Dict:
        pass
