from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListBootstrapActions(Paginator):
    def paginate(self, ClusterId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListClusters(Paginator):
    def paginate(self, CreatedAfter: datetime = None, CreatedBefore: datetime = None, ClusterStates: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListInstanceFleets(Paginator):
    def paginate(self, ClusterId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListInstanceGroups(Paginator):
    def paginate(self, ClusterId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListInstances(Paginator):
    def paginate(self, ClusterId: str, InstanceGroupId: str = None, InstanceGroupTypes: List = None, InstanceFleetId: str = None, InstanceFleetType: str = None, InstanceStates: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSteps(Paginator):
    def paginate(self, ClusterId: str, StepStates: List = None, StepIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
