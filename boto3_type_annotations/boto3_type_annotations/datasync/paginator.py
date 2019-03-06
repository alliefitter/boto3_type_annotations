from typing import Dict
from botocore.paginate import Paginator


class ListAgents(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListLocations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTagsForResource(Paginator):
    def paginate(self, ResourceArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTaskExecutions(Paginator):
    def paginate(self, TaskArn: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTasks(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
