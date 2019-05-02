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

    def create_mesh(self, meshName: str, clientToken: str = None, spec: Dict = None, tags: List = None) -> Dict:
        pass

    def create_route(self, meshName: str, routeName: str, spec: Dict, virtualRouterName: str, clientToken: str = None, tags: List = None) -> Dict:
        pass

    def create_virtual_node(self, meshName: str, spec: Dict, virtualNodeName: str, clientToken: str = None, tags: List = None) -> Dict:
        pass

    def create_virtual_router(self, meshName: str, spec: Dict, virtualRouterName: str, clientToken: str = None, tags: List = None) -> Dict:
        pass

    def create_virtual_service(self, meshName: str, spec: Dict, virtualServiceName: str, clientToken: str = None, tags: List = None) -> Dict:
        pass

    def delete_mesh(self, meshName: str) -> Dict:
        pass

    def delete_route(self, meshName: str, routeName: str, virtualRouterName: str) -> Dict:
        pass

    def delete_virtual_node(self, meshName: str, virtualNodeName: str) -> Dict:
        pass

    def delete_virtual_router(self, meshName: str, virtualRouterName: str) -> Dict:
        pass

    def delete_virtual_service(self, meshName: str, virtualServiceName: str) -> Dict:
        pass

    def describe_mesh(self, meshName: str) -> Dict:
        pass

    def describe_route(self, meshName: str, routeName: str, virtualRouterName: str) -> Dict:
        pass

    def describe_virtual_node(self, meshName: str, virtualNodeName: str) -> Dict:
        pass

    def describe_virtual_router(self, meshName: str, virtualRouterName: str) -> Dict:
        pass

    def describe_virtual_service(self, meshName: str, virtualServiceName: str) -> Dict:
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

    def list_tags_for_resource(self, resourceArn: str, limit: int = None, nextToken: str = None) -> Dict:
        pass

    def list_virtual_nodes(self, meshName: str, limit: int = None, nextToken: str = None) -> Dict:
        pass

    def list_virtual_routers(self, meshName: str, limit: int = None, nextToken: str = None) -> Dict:
        pass

    def list_virtual_services(self, meshName: str, limit: int = None, nextToken: str = None) -> Dict:
        pass

    def tag_resource(self, resourceArn: str, tags: List) -> Dict:
        pass

    def untag_resource(self, resourceArn: str, tagKeys: List) -> Dict:
        pass

    def update_mesh(self, meshName: str, clientToken: str = None, spec: Dict = None) -> Dict:
        pass

    def update_route(self, meshName: str, routeName: str, spec: Dict, virtualRouterName: str, clientToken: str = None) -> Dict:
        pass

    def update_virtual_node(self, meshName: str, spec: Dict, virtualNodeName: str, clientToken: str = None) -> Dict:
        pass

    def update_virtual_router(self, meshName: str, spec: Dict, virtualRouterName: str, clientToken: str = None) -> Dict:
        pass

    def update_virtual_service(self, meshName: str, spec: Dict, virtualServiceName: str, clientToken: str = None) -> Dict:
        pass
