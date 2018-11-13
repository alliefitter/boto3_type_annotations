from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeAutoScalingGroups(Paginator):
    def paginate(self, AutoScalingGroupNames: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeAutoScalingInstances(Paginator):
    def paginate(self, InstanceIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeLaunchConfigurations(Paginator):
    def paginate(self, LaunchConfigurationNames: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeNotificationConfigurations(Paginator):
    def paginate(self, AutoScalingGroupNames: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribePolicies(Paginator):
    def paginate(self, AutoScalingGroupName: str = None, PolicyNames: List = None, PolicyTypes: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeScalingActivities(Paginator):
    def paginate(self, ActivityIds: List = None, AutoScalingGroupName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeScheduledActions(Paginator):
    def paginate(self, AutoScalingGroupName: str = None, ScheduledActionNames: List = None, StartTime: datetime = None, EndTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTags(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
