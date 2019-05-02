from typing import Dict
from datetime import datetime
from botocore.paginate import Paginator


class DescribeStream(Paginator):
    def paginate(self, StreamName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListShards(Paginator):
    def paginate(self, StreamName: str = None, ExclusiveStartShardId: str = None, StreamCreationTimestamp: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStreamConsumers(Paginator):
    def paginate(self, StreamARN: str, StreamCreationTimestamp: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStreams(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
