from typing import Optional
from typing import Union
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient
from typing import IO


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_project(self, name: str = None, region: str = None, contents: Union[bytes, IO] = None, snapshotId: str = None) -> Dict:
        pass

    def delete_project(self, projectId: str) -> Dict:
        pass

    def describe_bundle(self, bundleId: str) -> Dict:
        pass

    def describe_project(self, projectId: str, syncFromResources: bool = None) -> Dict:
        pass

    def export_bundle(self, bundleId: str, projectId: str = None, platform: str = None) -> Dict:
        pass

    def export_project(self, projectId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_bundles(self, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def list_projects(self, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    def update_project(self, projectId: str, contents: Union[bytes, IO] = None) -> Dict:
        pass
