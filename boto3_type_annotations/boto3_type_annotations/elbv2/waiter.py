from typing import List
from typing import Dict
from botocore.waiter import Waiter


class LoadBalancerAvailable(Waiter):
    def wait(self, LoadBalancerArns: List = None, Names: List = None, Marker: str = None, PageSize: int = None, WaiterConfig: Dict = None):
        pass


class LoadBalancerExists(Waiter):
    def wait(self, LoadBalancerArns: List = None, Names: List = None, Marker: str = None, PageSize: int = None, WaiterConfig: Dict = None):
        pass


class LoadBalancersDeleted(Waiter):
    def wait(self, LoadBalancerArns: List = None, Names: List = None, Marker: str = None, PageSize: int = None, WaiterConfig: Dict = None):
        pass


class TargetDeregistered(Waiter):
    def wait(self, TargetGroupArn: str, Targets: List = None, WaiterConfig: Dict = None):
        pass


class TargetInService(Waiter):
    def wait(self, TargetGroupArn: str, Targets: List = None, WaiterConfig: Dict = None):
        pass
