from typing import Dict
from botocore.paginate import Paginator


class ListBulkDeploymentDetailedReports(Paginator):
    def paginate(self, BulkDeploymentId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListBulkDeployments(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListConnectorDefinitionVersions(Paginator):
    def paginate(self, ConnectorDefinitionId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListConnectorDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCoreDefinitionVersions(Paginator):
    def paginate(self, CoreDefinitionId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCoreDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDeployments(Paginator):
    def paginate(self, GroupId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDeviceDefinitionVersions(Paginator):
    def paginate(self, DeviceDefinitionId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDeviceDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListFunctionDefinitionVersions(Paginator):
    def paginate(self, FunctionDefinitionId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListFunctionDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListGroupVersions(Paginator):
    def paginate(self, GroupId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListGroups(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListLoggerDefinitionVersions(Paginator):
    def paginate(self, LoggerDefinitionId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListLoggerDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListResourceDefinitionVersions(Paginator):
    def paginate(self, ResourceDefinitionId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListResourceDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSubscriptionDefinitionVersions(Paginator):
    def paginate(self, SubscriptionDefinitionId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSubscriptionDefinitions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
