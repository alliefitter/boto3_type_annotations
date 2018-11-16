from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def batch_get_named_query(self, NamedQueryIds: List) -> Dict:
        pass

    def batch_get_query_execution(self, QueryExecutionIds: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_named_query(self, Name: str, Database: str, QueryString: str, Description: str = None, ClientRequestToken: str = None) -> Dict:
        pass

    def delete_named_query(self, NamedQueryId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
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

    def list_named_queries(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_query_executions(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def start_query_execution(self, QueryString: str, ResultConfiguration: Dict, ClientRequestToken: str = None, QueryExecutionContext: Dict = None) -> Dict:
        pass

    def stop_query_execution(self, QueryExecutionId: str) -> Dict:
        pass
