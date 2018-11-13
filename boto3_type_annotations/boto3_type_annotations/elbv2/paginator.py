from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeListeners(Paginator):
    def paginate(self, LoadBalancerArn: str = None, ListenerArns: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeLoadBalancers(Paginator):
    def paginate(self, LoadBalancerArns: List = None, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTargetGroups(Paginator):
    def paginate(self, LoadBalancerArn: str = None, TargetGroupArns: List = None, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
