from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class DescribeFleetAttributes(Paginator):
    def paginate(self, FleetIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeFleetCapacity(Paginator):
    def paginate(self, FleetIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeFleetEvents(Paginator):
    def paginate(self, FleetId: str, StartTime: datetime = None, EndTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeFleetUtilization(Paginator):
    def paginate(self, FleetIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeGameSessionDetails(Paginator):
    def paginate(self, FleetId: str = None, GameSessionId: str = None, AliasId: str = None, StatusFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeGameSessionQueues(Paginator):
    def paginate(self, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeGameSessions(Paginator):
    def paginate(self, FleetId: str = None, GameSessionId: str = None, AliasId: str = None, StatusFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeInstances(Paginator):
    def paginate(self, FleetId: str, InstanceId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeMatchmakingConfigurations(Paginator):
    def paginate(self, Names: List = None, RuleSetName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeMatchmakingRuleSets(Paginator):
    def paginate(self, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribePlayerSessions(Paginator):
    def paginate(self, GameSessionId: str = None, PlayerId: str = None, PlayerSessionId: str = None, PlayerSessionStatusFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeScalingPolicies(Paginator):
    def paginate(self, FleetId: str, StatusFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListAliases(Paginator):
    def paginate(self, RoutingStrategyType: str = None, Name: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListBuilds(Paginator):
    def paginate(self, Status: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListFleets(Paginator):
    def paginate(self, BuildId: str = None, ScriptId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class SearchGameSessions(Paginator):
    def paginate(self, FleetId: str = None, AliasId: str = None, FilterExpression: str = None, SortExpression: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
