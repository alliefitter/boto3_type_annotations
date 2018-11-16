from typing import Union
from botocore.paginate import Paginator
from typing import IO
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
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

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
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
