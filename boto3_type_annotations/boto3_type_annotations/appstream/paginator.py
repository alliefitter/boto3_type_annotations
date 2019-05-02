from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeDirectoryConfigs(Paginator):
    def paginate(self, DirectoryNames: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeFleets(Paginator):
    def paginate(self, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeImageBuilders(Paginator):
    def paginate(self, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeImages(Paginator):
    def paginate(self, Names: List = None, Arns: List = None, Type: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSessions(Paginator):
    def paginate(self, StackName: str, FleetName: str, UserId: str = None, AuthenticationType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeStacks(Paginator):
    def paginate(self, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeUserStackAssociations(Paginator):
    def paginate(self, StackName: str = None, UserName: str = None, AuthenticationType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeUsers(Paginator):
    def paginate(self, AuthenticationType: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAssociatedFleets(Paginator):
    def paginate(self, StackName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAssociatedStacks(Paginator):
    def paginate(self, FleetName: str, PaginationConfig: Dict = None) -> Dict:
        pass
