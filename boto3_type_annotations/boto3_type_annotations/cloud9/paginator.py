from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeEnvironmentMemberships(Paginator):
    def paginate(self, userArn: str = None, environmentId: str = None, permissions: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListEnvironments(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
