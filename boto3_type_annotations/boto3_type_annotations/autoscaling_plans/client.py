from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_scaling_plan(self, ScalingPlanName: str, ApplicationSource: Dict, ScalingInstructions: List) -> Dict:
        pass

    def delete_scaling_plan(self, ScalingPlanName: str, ScalingPlanVersion: int) -> Dict:
        pass

    def describe_scaling_plan_resources(self, ScalingPlanName: str, ScalingPlanVersion: int, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_scaling_plans(self, ScalingPlanNames: List = None, ScalingPlanVersion: int = None, ApplicationSources: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def update_scaling_plan(self, ScalingPlanName: str, ScalingPlanVersion: int, ApplicationSource: Dict = None, ScalingInstructions: List = None) -> Dict:
        pass
