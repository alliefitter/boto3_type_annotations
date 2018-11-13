from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeActivations(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeInstanceInformation(Paginator):
    def paginate(self, InstanceInformationFilterList: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeParameters(Paginator):
    def paginate(self, Filters: List = None, ParameterFilters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetParameterHistory(Paginator):
    def paginate(self, Name: str, WithDecryption: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetParametersByPath(Paginator):
    def paginate(self, Path: str, Recursive: bool = None, ParameterFilters: List = None, WithDecryption: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAssociations(Paginator):
    def paginate(self, AssociationFilterList: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCommandInvocations(Paginator):
    def paginate(self, CommandId: str = None, InstanceId: str = None, Filters: List = None, Details: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCommands(Paginator):
    def paginate(self, CommandId: str = None, InstanceId: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDocuments(Paginator):
    def paginate(self, DocumentFilterList: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
