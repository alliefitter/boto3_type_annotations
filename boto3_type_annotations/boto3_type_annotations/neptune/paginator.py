from typing import List
from typing import Dict
from datetime import datetime
from botocore.paginate import Paginator


class DescribeDBClusterParameterGroups(Paginator):
    def paginate(self, DBClusterParameterGroupName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBClusterParameters(Paginator):
    def paginate(self, DBClusterParameterGroupName: str, Source: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBClusterSnapshots(Paginator):
    def paginate(self, DBClusterIdentifier: str = None, DBClusterSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, IncludeShared: bool = None, IncludePublic: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBClusters(Paginator):
    def paginate(self, DBClusterIdentifier: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBEngineVersions(Paginator):
    def paginate(self, Engine: str = None, EngineVersion: str = None, DBParameterGroupFamily: str = None, Filters: List = None, DefaultOnly: bool = None, ListSupportedCharacterSets: bool = None, ListSupportedTimezones: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBInstances(Paginator):
    def paginate(self, DBInstanceIdentifier: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBParameterGroups(Paginator):
    def paginate(self, DBParameterGroupName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBParameters(Paginator):
    def paginate(self, DBParameterGroupName: str, Source: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBSubnetGroups(Paginator):
    def paginate(self, DBSubnetGroupName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEngineDefaultParameters(Paginator):
    def paginate(self, DBParameterGroupFamily: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEventSubscriptions(Paginator):
    def paginate(self, SubscriptionName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEvents(Paginator):
    def paginate(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, EventCategories: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeOrderableDBInstanceOptions(Paginator):
    def paginate(self, Engine: str, EngineVersion: str = None, DBInstanceClass: str = None, LicenseModel: str = None, Vpc: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribePendingMaintenanceActions(Paginator):
    def paginate(self, ResourceIdentifier: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
