from typing import Optional
from typing import Union
from botocore.waiter import Waiter
from botocore.client import BaseClient
from botocore.paginate import Paginator
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_mesh(self, meshName: str, clientToken: str = None) -> Dict:
        pass

    def create_route(self, meshName: str, routeName: str, spec: Dict, virtualRouterName: str, clientToken: str = None) -> Dict:
        pass

    def create_virtual_node(self, meshName: str, spec: Dict, virtualNodeName: str, clientToken: str = None) -> Dict:
        pass

    def create_virtual_router(self, meshName: str, spec: Dict, virtualRouterName: str, clientToken: str = None) -> Dict:
        pass

    def delete_mesh(self, meshName: str) -> Dict:
        pass

    def delete_route(self, meshName: str, routeName: str, virtualRouterName: str) -> Dict:
        pass

    def delete_virtual_node(self, meshName: str, virtualNodeName: str) -> Dict:
        pass

    def delete_virtual_router(self, meshName: str, virtualRouterName: str) -> Dict:
        pass

    def describe_mesh(self, meshName: str) -> Dict:
        pass

    def describe_route(self, meshName: str, routeName: str, virtualRouterName: str) -> Dict:
        pass

    def describe_virtual_node(self, meshName: str, virtualNodeName: str) -> Dict:
        pass

    def describe_virtual_router(self, meshName: str, virtualRouterName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_meshes(self, limit: int = None, nextToken: str = None) -> Dict:
        pass

    def list_routes(self, meshName: str, virtualRouterName: str, limit: int = None, nextToken: str = None) -> Dict:
        pass

    def list_virtual_nodes(self, meshName: str, limit: int = None, nextToken: str = None) -> Dict:
        pass

    def list_virtual_routers(self, meshName: str, limit: int = None, nextToken: str = None) -> Dict:
        pass

    def update_route(self, meshName: str, routeName: str, spec: Dict, virtualRouterName: str, clientToken: str = None) -> Dict:
        pass

    def update_virtual_node(self, meshName: str, spec: Dict, virtualNodeName: str, clientToken: str = None) -> Dict:
        pass

    def update_virtual_router(self, meshName: str, spec: Dict, virtualRouterName: str, clientToken: str = None) -> Dict:
        pass
