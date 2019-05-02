from typing import Dict
from datetime import datetime
from typing import List
from botocore.paginate import Paginator


class DescribeDBClusters(Paginator):
    def paginate(self, DBClusterIdentifier: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBEngineVersions(Paginator):
    def paginate(self, Engine: str = None, EngineVersion: str = None, DBParameterGroupFamily: str = None, Filters: List = None, DefaultOnly: bool = None, ListSupportedCharacterSets: bool = None, ListSupportedTimezones: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBInstances(Paginator):
    def paginate(self, DBInstanceIdentifier: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDBSubnetGroups(Paginator):
    def paginate(self, DBSubnetGroupName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEvents(Paginator):
    def paginate(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, EventCategories: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeOrderableDBInstanceOptions(Paginator):
    def paginate(self, Engine: str, EngineVersion: str = None, DBInstanceClass: str = None, LicenseModel: str = None, Vpc: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
