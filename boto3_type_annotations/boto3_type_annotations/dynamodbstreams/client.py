from typing import Optional
from typing import Union
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def describe_stream(self, StreamArn: str, Limit: int = None, ExclusiveStartShardId: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_records(self, ShardIterator: str, Limit: int = None) -> Dict:
        pass

    def get_shard_iterator(self, StreamArn: str, ShardId: str, ShardIteratorType: str, SequenceNumber: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_streams(self, TableName: str = None, Limit: int = None, ExclusiveStartStreamArn: str = None) -> Dict:
        pass
