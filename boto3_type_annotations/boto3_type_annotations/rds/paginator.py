from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


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


class DescribeDBLogFiles(Paginator):
    def paginate(self, DBInstanceIdentifier: str, FilenameContains: str = None, FileLastWritten: int = None, FileSize: int = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBParameterGroups(Paginator):
    def paginate(self, DBParameterGroupName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBParameters(Paginator):
    def paginate(self, DBParameterGroupName: str, Source: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBSecurityGroups(Paginator):
    def paginate(self, DBSecurityGroupName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBSnapshots(Paginator):
    def paginate(self, DBInstanceIdentifier: str = None, DBSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, IncludeShared: bool = None, IncludePublic: bool = None, PaginationConfig: Dict = None) -> Dict:
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


class DescribeOptionGroupOptions(Paginator):
    def paginate(self, EngineName: str, MajorEngineVersion: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeOptionGroups(Paginator):
    def paginate(self, OptionGroupName: str = None, Filters: List = None, EngineName: str = None, MajorEngineVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeOrderableDBInstanceOptions(Paginator):
    def paginate(self, Engine: str, EngineVersion: str = None, DBInstanceClass: str = None, LicenseModel: str = None, Vpc: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeReservedDBInstances(Paginator):
    def paginate(self, ReservedDBInstanceId: str = None, ReservedDBInstancesOfferingId: str = None, DBInstanceClass: str = None, Duration: str = None, ProductDescription: str = None, OfferingType: str = None, MultiAZ: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeReservedDBInstancesOfferings(Paginator):
    def paginate(self, ReservedDBInstancesOfferingId: str = None, DBInstanceClass: str = None, Duration: str = None, ProductDescription: str = None, OfferingType: str = None, MultiAZ: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DownloadDBLogFilePortion(Paginator):
    def paginate(self, DBInstanceIdentifier: str, LogFileName: str, PaginationConfig: Dict = None) -> Dict:
        pass
