from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def associate_kms_key(self, logGroupName: str, kmsKeyId: str) -> NoReturn:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def cancel_export_task(self, taskId: str) -> NoReturn:
        pass

    def create_export_task(self, logGroupName: str, fromTime: int, to: int, destination: str, taskName: str = None, logStreamNamePrefix: str = None, destinationPrefix: str = None) -> Dict:
        pass

    def create_log_group(self, logGroupName: str, kmsKeyId: str = None, tags: Dict = None) -> NoReturn:
        pass

    def create_log_stream(self, logGroupName: str, logStreamName: str) -> NoReturn:
        pass

    def delete_destination(self, destinationName: str) -> NoReturn:
        pass

    def delete_log_group(self, logGroupName: str) -> NoReturn:
        pass

    def delete_log_stream(self, logGroupName: str, logStreamName: str) -> NoReturn:
        pass

    def delete_metric_filter(self, logGroupName: str, filterName: str) -> NoReturn:
        pass

    def delete_resource_policy(self, policyName: str = None) -> NoReturn:
        pass

    def delete_retention_policy(self, logGroupName: str) -> NoReturn:
        pass

    def delete_subscription_filter(self, logGroupName: str, filterName: str) -> NoReturn:
        pass

    def describe_destinations(self, DestinationNamePrefix: str = None, nextToken: str = None, limit: int = None) -> Dict:
        pass

    def describe_export_tasks(self, taskId: str = None, statusCode: str = None, nextToken: str = None, limit: int = None) -> Dict:
        pass

    def describe_log_groups(self, logGroupNamePrefix: str = None, nextToken: str = None, limit: int = None) -> Dict:
        pass

    def describe_log_streams(self, logGroupName: str, logStreamNamePrefix: str = None, orderBy: str = None, descending: bool = None, nextToken: str = None, limit: int = None) -> Dict:
        pass

    def describe_metric_filters(self, logGroupName: str = None, filterNamePrefix: str = None, nextToken: str = None, limit: int = None, metricName: str = None, metricNamespace: str = None) -> Dict:
        pass

    def describe_resource_policies(self, nextToken: str = None, limit: int = None) -> Dict:
        pass

    def describe_subscription_filters(self, logGroupName: str, filterNamePrefix: str = None, nextToken: str = None, limit: int = None) -> Dict:
        pass

    def disassociate_kms_key(self, logGroupName: str) -> NoReturn:
        pass

    def filter_log_events(self, logGroupName: str, logStreamNames: List = None, logStreamNamePrefix: str = None, startTime: int = None, endTime: int = None, filterPattern: str = None, nextToken: str = None, limit: int = None, interleaved: bool = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_log_events(self, logGroupName: str, logStreamName: str, startTime: int = None, endTime: int = None, nextToken: str = None, limit: int = None, startFromHead: bool = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_tags_log_group(self, logGroupName: str) -> Dict:
        pass

    def put_destination(self, destinationName: str, targetArn: str, roleArn: str) -> Dict:
        pass

    def put_destination_policy(self, destinationName: str, accessPolicy: str) -> NoReturn:
        pass

    def put_log_events(self, logGroupName: str, logStreamName: str, logEvents: List, sequenceToken: str = None) -> Dict:
        pass

    def put_metric_filter(self, logGroupName: str, filterName: str, filterPattern: str, metricTransformations: List) -> NoReturn:
        pass

    def put_resource_policy(self, policyName: str = None, policyDocument: str = None) -> Dict:
        pass

    def put_retention_policy(self, logGroupName: str, retentionInDays: int) -> NoReturn:
        pass

    def put_subscription_filter(self, logGroupName: str, filterName: str, filterPattern: str, destinationArn: str, roleArn: str = None, distribution: str = None) -> NoReturn:
        pass

    def tag_log_group(self, logGroupName: str, tags: Dict) -> NoReturn:
        pass

    def test_metric_filter(self, filterPattern: str, logEventMessages: List) -> Dict:
        pass

    def untag_log_group(self, logGroupName: str, tags: List) -> NoReturn:
        pass
