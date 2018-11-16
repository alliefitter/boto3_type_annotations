from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def add_permission(self, TopicArn: str, Label: str, AWSAccountId: List, ActionName: List) -> NoReturn:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def check_if_phone_number_is_opted_out(self, phoneNumber: str) -> Dict:
        pass

    def confirm_subscription(self, TopicArn: str, Token: str, AuthenticateOnUnsubscribe: str = None) -> Dict:
        pass

    def create_platform_application(self, Name: str, Platform: str, Attributes: Dict) -> Dict:
        pass

    def create_platform_endpoint(self, PlatformApplicationArn: str, Token: str, CustomUserData: str = None, Attributes: Dict = None) -> Dict:
        pass

    def create_topic(self, Name: str) -> Dict:
        pass

    def delete_endpoint(self, EndpointArn: str) -> NoReturn:
        pass

    def delete_platform_application(self, PlatformApplicationArn: str) -> NoReturn:
        pass

    def delete_topic(self, TopicArn: str) -> NoReturn:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_endpoint_attributes(self, EndpointArn: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_platform_application_attributes(self, PlatformApplicationArn: str) -> Dict:
        pass

    def get_sms_attributes(self, attributes: List = None) -> Dict:
        pass

    def get_subscription_attributes(self, SubscriptionArn: str) -> Dict:
        pass

    def get_topic_attributes(self, TopicArn: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_endpoints_by_platform_application(self, PlatformApplicationArn: str, NextToken: str = None) -> Dict:
        pass

    def list_phone_numbers_opted_out(self, nextToken: str = None) -> Dict:
        pass

    def list_platform_applications(self, NextToken: str = None) -> Dict:
        pass

    def list_subscriptions(self, NextToken: str = None) -> Dict:
        pass

    def list_subscriptions_by_topic(self, TopicArn: str, NextToken: str = None) -> Dict:
        pass

    def list_topics(self, NextToken: str = None) -> Dict:
        pass

    def opt_in_phone_number(self, phoneNumber: str) -> Dict:
        pass

    def publish(self, Message: str, TopicArn: str = None, TargetArn: str = None, PhoneNumber: str = None, Subject: str = None, MessageStructure: str = None, MessageAttributes: Dict = None) -> Dict:
        pass

    def remove_permission(self, TopicArn: str, Label: str) -> NoReturn:
        pass

    def set_endpoint_attributes(self, EndpointArn: str, Attributes: Dict) -> NoReturn:
        pass

    def set_platform_application_attributes(self, PlatformApplicationArn: str, Attributes: Dict) -> NoReturn:
        pass

    def set_sms_attributes(self, attributes: Dict) -> Dict:
        pass

    def set_subscription_attributes(self, SubscriptionArn: str, AttributeName: str, AttributeValue: str = None) -> NoReturn:
        pass

    def set_topic_attributes(self, TopicArn: str, AttributeName: str, AttributeValue: str = None) -> NoReturn:
        pass

    def subscribe(self, TopicArn: str, Protocol: str, Endpoint: str = None, Attributes: Dict = None, ReturnSubscriptionArn: bool = None) -> Dict:
        pass

    def unsubscribe(self, SubscriptionArn: str) -> NoReturn:
        pass
