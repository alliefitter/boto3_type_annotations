from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def add_permission(self, QueueUrl: str, Label: str, AWSAccountIds: List, Actions: List):
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def change_message_visibility(self, QueueUrl: str, ReceiptHandle: str, VisibilityTimeout: int):
        pass

    def change_message_visibility_batch(self, QueueUrl: str, Entries: List) -> Dict:
        pass

    def create_queue(self, QueueName: str, Attributes: Dict = None) -> Dict:
        pass

    def delete_message(self, QueueUrl: str, ReceiptHandle: str):
        pass

    def delete_message_batch(self, QueueUrl: str, Entries: List) -> Dict:
        pass

    def delete_queue(self, QueueUrl: str):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_queue_attributes(self, QueueUrl: str, AttributeNames: List = None) -> Dict:
        pass

    def get_queue_url(self, QueueName: str, QueueOwnerAWSAccountId: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_dead_letter_source_queues(self, QueueUrl: str) -> Dict:
        pass

    def list_queue_tags(self, QueueUrl: str) -> Dict:
        pass

    def list_queues(self, QueueNamePrefix: str = None) -> Dict:
        pass

    def purge_queue(self, QueueUrl: str):
        pass

    def receive_message(self, QueueUrl: str, AttributeNames: List = None, MessageAttributeNames: List = None, MaxNumberOfMessages: int = None, VisibilityTimeout: int = None, WaitTimeSeconds: int = None, ReceiveRequestAttemptId: str = None) -> Dict:
        pass

    def remove_permission(self, QueueUrl: str, Label: str):
        pass

    def send_message(self, QueueUrl: str, MessageBody: str, DelaySeconds: int = None, MessageAttributes: Dict = None, MessageDeduplicationId: str = None, MessageGroupId: str = None) -> Dict:
        pass

    def send_message_batch(self, QueueUrl: str, Entries: List) -> Dict:
        pass

    def set_queue_attributes(self, QueueUrl: str, Attributes: Dict):
        pass

    def tag_queue(self, QueueUrl: str, Tags: Dict):
        pass

    def untag_queue(self, QueueUrl: str, TagKeys: List):
        pass
