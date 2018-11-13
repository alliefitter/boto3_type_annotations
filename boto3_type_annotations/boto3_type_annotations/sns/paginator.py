from typing import Dict
from botocore.paginate import Paginator


class ListEndpointsByPlatformApplication(Paginator):
    def paginate(self, PlatformApplicationArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPlatformApplications(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSubscriptions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSubscriptionsByTopic(Paginator):
    def paginate(self, TopicArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTopics(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
