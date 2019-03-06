from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeScalingPlanResources(Paginator):
    def paginate(self, ScalingPlanName: str, ScalingPlanVersion: int, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeScalingPlans(Paginator):
    def paginate(self, ScalingPlanNames: List = None, ScalingPlanVersion: int = None, ApplicationSources: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
