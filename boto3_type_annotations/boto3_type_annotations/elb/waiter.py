from typing import List
from typing import Dict
from botocore.waiter import Waiter


class AnyInstanceInService(Waiter):
    def wait(self, LoadBalancerName: str, Instances: List = None, WaiterConfig: Dict = None):
        pass


class InstanceDeregistered(Waiter):
    def wait(self, LoadBalancerName: str, Instances: List = None, WaiterConfig: Dict = None):
        pass


class InstanceInService(Waiter):
    def wait(self, LoadBalancerName: str, Instances: List = None, WaiterConfig: Dict = None):
        pass
