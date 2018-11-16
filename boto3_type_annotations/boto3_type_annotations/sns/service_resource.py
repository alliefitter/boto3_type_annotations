from typing import Optional
from typing import Union
from boto3.resources.collection import ResourceCollection
from typing import List
from typing import Dict
from boto3.resources import base


class ServiceResource(base.ServiceResource):
    platform_applications: 'platform_applications'
    subscriptions: 'subscriptions'
    topics: 'topics'

    def PlatformApplication(self, arn: str = None) -> 'PlatformApplication':
        pass

    def PlatformEndpoint(self, arn: str = None) -> 'PlatformEndpoint':
        pass

    def Subscription(self, arn: str = None) -> 'Subscription':
        pass

    def Topic(self, arn: str = None) -> 'Topic':
        pass

    def create_platform_application(self, Name: str, Platform: str, Attributes: Dict) -> 'PlatformApplication':
        pass

    def create_topic(self, Name: str) -> 'Topic':
        pass

    def get_available_subresources(self) -> List[str]:
        pass


class PlatformApplication(base.ServiceResource):
    attributes: Dict
    arn: str
    endpoints: 'endpoints'

    def create_platform_endpoint(self, Token: str, CustomUserData: str = None, Attributes: Dict = None) -> 'PlatformEndpoint':
        pass

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def set_attributes(self, Attributes: Dict):
        pass


class PlatformEndpoint(base.ServiceResource):
    attributes: Dict
    arn: str

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def publish(self, Message: str, TopicArn: str = None, PhoneNumber: str = None, Subject: str = None, MessageStructure: str = None, MessageAttributes: Dict = None) -> Dict:
        pass

    def reload(self):
        pass

    def set_attributes(self, Attributes: Dict):
        pass


class Subscription(base.ServiceResource):
    attributes: Dict
    arn: str

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def set_attributes(self, AttributeName: str, AttributeValue: str = None):
        pass


class Topic(base.ServiceResource):
    attributes: Dict
    arn: str
    subscriptions: 'subscriptions'

    def add_permission(self, Label: str, AWSAccountId: List, ActionName: List):
        pass

    def confirm_subscription(self, Token: str, AuthenticateOnUnsubscribe: str = None) -> 'Subscription':
        pass

    def delete(self):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def publish(self, Message: str, TargetArn: str = None, PhoneNumber: str = None, Subject: str = None, MessageStructure: str = None, MessageAttributes: Dict = None) -> Dict:
        pass

    def reload(self):
        pass

    def remove_permission(self, Label: str):
        pass

    def set_attributes(self, AttributeName: str, AttributeValue: str = None):
        pass

    def subscribe(self, Protocol: str, Endpoint: str = None, Attributes: Dict = None, ReturnSubscriptionArn: bool = None) -> 'Subscription':
        pass


class platform_applications(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['PlatformApplication']:
        pass

    
    @classmethod
    def filter(cls, NextToken: str = None) -> List['PlatformApplication']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['PlatformApplication']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['PlatformApplication']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class subscriptions(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Subscription']:
        pass

    
    @classmethod
    def filter(cls, NextToken: str = None) -> List['Subscription']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Subscription']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Subscription']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class topics(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Topic']:
        pass

    
    @classmethod
    def filter(cls, NextToken: str = None) -> List['Topic']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Topic']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Topic']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass
