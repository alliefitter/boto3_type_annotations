from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeEcsClusters(Paginator):
    def paginate(self, EcsClusterArns: List = None, StackId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
