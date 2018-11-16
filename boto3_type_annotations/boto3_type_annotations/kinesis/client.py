from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def add_tags_to_stream(self, StreamName: str, Tags: Dict):
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_stream(self, StreamName: str, ShardCount: int):
        pass

    def decrease_stream_retention_period(self, StreamName: str, RetentionPeriodHours: int):
        pass

    def delete_stream(self, StreamName: str, EnforceConsumerDeletion: bool = None):
        pass

    def deregister_stream_consumer(self, StreamARN: str = None, ConsumerName: str = None, ConsumerARN: str = None):
        pass

    def describe_limits(self) -> Dict:
        pass

    def describe_stream(self, StreamName: str, Limit: int = None, ExclusiveStartShardId: str = None) -> Dict:
        pass

    def describe_stream_consumer(self, StreamARN: str = None, ConsumerName: str = None, ConsumerARN: str = None) -> Dict:
        pass

    def describe_stream_summary(self, StreamName: str) -> Dict:
        pass

    def disable_enhanced_monitoring(self, StreamName: str, ShardLevelMetrics: List) -> Dict:
        pass

    def enable_enhanced_monitoring(self, StreamName: str, ShardLevelMetrics: List) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_records(self, ShardIterator: str, Limit: int = None) -> Dict:
        pass

    def get_shard_iterator(self, StreamName: str, ShardId: str, ShardIteratorType: str, StartingSequenceNumber: str = None, Timestamp: datetime = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def increase_stream_retention_period(self, StreamName: str, RetentionPeriodHours: int):
        pass

    def list_shards(self, StreamName: str = None, NextToken: str = None, ExclusiveStartShardId: str = None, MaxResults: int = None, StreamCreationTimestamp: datetime = None) -> Dict:
        pass

    def list_stream_consumers(self, StreamARN: str, NextToken: str = None, MaxResults: int = None, StreamCreationTimestamp: datetime = None) -> Dict:
        pass

    def list_streams(self, Limit: int = None, ExclusiveStartStreamName: str = None) -> Dict:
        pass

    def list_tags_for_stream(self, StreamName: str, ExclusiveStartTagKey: str = None, Limit: int = None) -> Dict:
        pass

    def merge_shards(self, StreamName: str, ShardToMerge: str, AdjacentShardToMerge: str):
        pass

    def put_record(self, StreamName: str, Data: bytes, PartitionKey: str, ExplicitHashKey: str = None, SequenceNumberForOrdering: str = None) -> Dict:
        pass

    def put_records(self, Records: List, StreamName: str) -> Dict:
        pass

    def register_stream_consumer(self, StreamARN: str, ConsumerName: str) -> Dict:
        pass

    def remove_tags_from_stream(self, StreamName: str, TagKeys: List):
        pass

    def split_shard(self, StreamName: str, ShardToSplit: str, NewStartingHashKey: str):
        pass

    def start_stream_encryption(self, StreamName: str, EncryptionType: str, KeyId: str):
        pass

    def stop_stream_encryption(self, StreamName: str, EncryptionType: str, KeyId: str):
        pass

    def update_shard_count(self, StreamName: str, TargetShardCount: int, ScalingType: str) -> Dict:
        pass
