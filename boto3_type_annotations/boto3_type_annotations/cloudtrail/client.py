from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def add_tags(self, ResourceId: str, TagsList: List = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_trail(self, Name: str, S3BucketName: str, S3KeyPrefix: str = None, SnsTopicName: str = None, IncludeGlobalServiceEvents: bool = None, IsMultiRegionTrail: bool = None, EnableLogFileValidation: bool = None, CloudWatchLogsLogGroupArn: str = None, CloudWatchLogsRoleArn: str = None, KmsKeyId: str = None) -> Dict:
        pass

    def delete_trail(self, Name: str) -> Dict:
        pass

    def describe_trails(self, trailNameList: List = None, includeShadowTrails: bool = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_event_selectors(self, TrailName: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_trail_status(self, Name: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_public_keys(self, StartTime: datetime = None, EndTime: datetime = None, NextToken: str = None) -> Dict:
        pass

    def list_tags(self, ResourceIdList: List, NextToken: str = None) -> Dict:
        pass

    def lookup_events(self, LookupAttributes: List = None, StartTime: datetime = None, EndTime: datetime = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def put_event_selectors(self, TrailName: str, EventSelectors: List) -> Dict:
        pass

    def remove_tags(self, ResourceId: str, TagsList: List = None) -> Dict:
        pass

    def start_logging(self, Name: str) -> Dict:
        pass

    def stop_logging(self, Name: str) -> Dict:
        pass

    def update_trail(self, Name: str, S3BucketName: str = None, S3KeyPrefix: str = None, SnsTopicName: str = None, IncludeGlobalServiceEvents: bool = None, IsMultiRegionTrail: bool = None, EnableLogFileValidation: bool = None, CloudWatchLogsLogGroupArn: str = None, CloudWatchLogsRoleArn: str = None, KmsKeyId: str = None) -> Dict:
        pass
