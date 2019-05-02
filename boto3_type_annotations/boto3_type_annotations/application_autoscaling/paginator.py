from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeScalableTargets(Paginator):
    def paginate(self, ServiceNamespace: str, ResourceIds: List = None, ScalableDimension: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeScalingActivities(Paginator):
    def paginate(self, ServiceNamespace: str, ResourceId: str = None, ScalableDimension: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeScalingPolicies(Paginator):
    def paginate(self, ServiceNamespace: str, PolicyNames: List = None, ResourceId: str = None, ScalableDimension: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeScheduledActions(Paginator):
    def paginate(self, ServiceNamespace: str, ScheduledActionNames: List = None, ResourceId: str = None, ScalableDimension: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
