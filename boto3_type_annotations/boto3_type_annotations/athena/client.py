from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def batch_get_named_query(self, NamedQueryIds: List) -> Dict:
        pass

    def batch_get_query_execution(self, QueryExecutionIds: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_named_query(self, Name: str, Database: str, QueryString: str, Description: str = None, ClientRequestToken: str = None, WorkGroup: str = None) -> Dict:
        pass

    def create_work_group(self, Name: str, Configuration: Dict = None, Description: str = None, Tags: List = None) -> Dict:
        pass

    def delete_named_query(self, NamedQueryId: str) -> Dict:
        pass

    def delete_work_group(self, WorkGroup: str, RecursiveDeleteOption: bool = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_named_query(self, NamedQueryId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_query_execution(self, QueryExecutionId: str) -> Dict:
        pass

    def get_query_results(self, QueryExecutionId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def get_work_group(self, WorkGroup: str) -> Dict:
        pass

    def list_named_queries(self, NextToken: str = None, MaxResults: int = None, WorkGroup: str = None) -> Dict:
        pass

    def list_query_executions(self, NextToken: str = None, MaxResults: int = None, WorkGroup: str = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceARN: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_work_groups(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def start_query_execution(self, QueryString: str, ClientRequestToken: str = None, QueryExecutionContext: Dict = None, ResultConfiguration: Dict = None, WorkGroup: str = None) -> Dict:
        pass

    def stop_query_execution(self, QueryExecutionId: str) -> Dict:
        pass

    def tag_resource(self, ResourceARN: str, Tags: List) -> Dict:
        pass

    def untag_resource(self, ResourceARN: str, TagKeys: List) -> Dict:
        pass

    def update_work_group(self, WorkGroup: str, Description: str = None, ConfigurationUpdates: Dict = None, State: str = None) -> Dict:
        pass
