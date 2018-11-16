from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def associate_device_with_placement(self, projectName: str, placementName: str, deviceId: str, deviceTemplateName: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_placement(self, placementName: str, projectName: str, attributes: Dict = None) -> Dict:
        pass

    def create_project(self, projectName: str, description: str = None, placementTemplate: Dict = None) -> Dict:
        pass

    def delete_placement(self, placementName: str, projectName: str) -> Dict:
        pass

    def delete_project(self, projectName: str) -> Dict:
        pass

    def describe_placement(self, placementName: str, projectName: str) -> Dict:
        pass

    def describe_project(self, projectName: str) -> Dict:
        pass

    def disassociate_device_from_placement(self, projectName: str, placementName: str, deviceTemplateName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_devices_in_placement(self, projectName: str, placementName: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_placements(self, projectName: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_projects(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def update_placement(self, placementName: str, projectName: str, attributes: Dict = None) -> Dict:
        pass

    def update_project(self, projectName: str, description: str = None, placementTemplate: Dict = None) -> Dict:
        pass
