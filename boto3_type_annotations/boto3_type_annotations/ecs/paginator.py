from typing import Dict
from botocore.paginate import Paginator


class ListAccountSettings(Paginator):
    def paginate(self, name: str = None, value: str = None, principalArn: str = None, effectiveSettings: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAttributes(Paginator):
    def paginate(self, targetType: str, cluster: str = None, attributeName: str = None, attributeValue: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListClusters(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListContainerInstances(Paginator):
    def paginate(self, cluster: str = None, filter: str = None, status: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListServices(Paginator):
    def paginate(self, cluster: str = None, launchType: str = None, schedulingStrategy: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTaskDefinitionFamilies(Paginator):
    def paginate(self, familyPrefix: str = None, status: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTaskDefinitions(Paginator):
    def paginate(self, familyPrefix: str = None, status: str = None, sort: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTasks(Paginator):
    def paginate(self, cluster: str = None, containerInstance: str = None, family: str = None, startedBy: str = None, serviceName: str = None, desiredStatus: str = None, launchType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
