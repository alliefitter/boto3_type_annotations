from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeAccountLimits(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeListenerCertificates(Paginator):
    def paginate(self, ListenerArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeListeners(Paginator):
    def paginate(self, LoadBalancerArn: str = None, ListenerArns: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeLoadBalancers(Paginator):
    def paginate(self, LoadBalancerArns: List = None, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeRules(Paginator):
    def paginate(self, ListenerArn: str = None, RuleArns: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSSLPolicies(Paginator):
    def paginate(self, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTargetGroups(Paginator):
    def paginate(self, LoadBalancerArn: str = None, TargetGroupArns: List = None, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
