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

    def create_group(self, Name: str, ResourceQuery: Dict, Description: str = None, Tags: Dict = None) -> Dict:
        pass

    def delete_group(self, GroupName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_group(self, GroupName: str) -> Dict:
        pass

    def get_group_query(self, GroupName: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_tags(self, Arn: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_group_resources(self, GroupName: str, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_groups(self, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def search_resources(self, ResourceQuery: Dict, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def tag(self, Arn: str, Tags: Dict) -> Dict:
        pass

    def untag(self, Arn: str, Keys: List) -> Dict:
        pass

    def update_group(self, GroupName: str, Description: str = None) -> Dict:
        pass

    def update_group_query(self, GroupName: str, ResourceQuery: Dict) -> Dict:
        pass
