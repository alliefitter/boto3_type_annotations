from typing import Union
from typing import NoReturn
from typing import Optional
from typing import List
from boto3.resources.collection import ResourceCollection
from typing import Dict
from boto3.resources import base


class ServiceResource(base.ServiceResource):
    queues: 'queues'

    def Message(self, queue_url: str = None, receipt_handle: str = None) -> 'Message':
        pass

    def Queue(self, url: str = None) -> 'Queue':
        pass

    def create_queue(self, QueueName: str, Attributes: Dict = None) -> 'Queue':
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def get_queue_by_name(self, QueueName: str, QueueOwnerAWSAccountId: str = None) -> 'Queue':
        pass


class Message(base.ServiceResource):
    message_id: str
    md5_of_body: str
    body: str
    attributes: Dict
    md5_of_message_attributes: str
    message_attributes: Dict
    queue_url: str
    receipt_handle: str

    def change_visibility(self, VisibilityTimeout: int) -> NoReturn:
        pass

    def delete(self) -> NoReturn:
        pass

    def get_available_subresources(self) -> List[str]:
        pass


class Queue(base.ServiceResource):
    attributes: Dict
    url: str
    dead_letter_source_queues: 'dead_letter_source_queues'

    def add_permission(self, Label: str, AWSAccountIds: List, Actions: List) -> NoReturn:
        pass

    def change_message_visibility_batch(self, Entries: List) -> Dict:
        pass

    def delete(self) -> NoReturn:
        pass

    def delete_messages(self, Entries: List) -> Dict:
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self) -> NoReturn:
        pass

    def purge(self) -> NoReturn:
        pass

    def receive_messages(self, AttributeNames: List = None, MessageAttributeNames: List = None, MaxNumberOfMessages: int = None, VisibilityTimeout: int = None, WaitTimeSeconds: int = None, ReceiveRequestAttemptId: str = None) -> List['Message']:
        pass

    def reload(self) -> NoReturn:
        pass

    def remove_permission(self, Label: str) -> NoReturn:
        pass

    def send_message(self, MessageBody: str, DelaySeconds: int = None, MessageAttributes: Dict = None, MessageDeduplicationId: str = None, MessageGroupId: str = None) -> Dict:
        pass

    def send_messages(self, Entries: List) -> Dict:
        pass

    def set_attributes(self, Attributes: Dict) -> NoReturn:
        pass


class queues(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Queue']:
        pass

    
    @classmethod
    def filter(cls, QueueNamePrefix: str = None) -> List['Queue']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Queue']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Queue']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass
