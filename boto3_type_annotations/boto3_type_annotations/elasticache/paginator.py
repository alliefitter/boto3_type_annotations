from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class DescribeCacheClusters(Paginator):
    def paginate(self, CacheClusterId: str = None, ShowCacheNodeInfo: bool = None, ShowCacheClustersNotInReplicationGroups: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeCacheEngineVersions(Paginator):
    def paginate(self, Engine: str = None, EngineVersion: str = None, CacheParameterGroupFamily: str = None, DefaultOnly: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeCacheParameterGroups(Paginator):
    def paginate(self, CacheParameterGroupName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeCacheParameters(Paginator):
    def paginate(self, CacheParameterGroupName: str, Source: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeCacheSecurityGroups(Paginator):
    def paginate(self, CacheSecurityGroupName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeCacheSubnetGroups(Paginator):
    def paginate(self, CacheSubnetGroupName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEngineDefaultParameters(Paginator):
    def paginate(self, CacheParameterGroupFamily: str, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEvents(Paginator):
    def paginate(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeReplicationGroups(Paginator):
    def paginate(self, ReplicationGroupId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeReservedCacheNodes(Paginator):
    def paginate(self, ReservedCacheNodeId: str = None, ReservedCacheNodesOfferingId: str = None, CacheNodeType: str = None, Duration: str = None, ProductDescription: str = None, OfferingType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeReservedCacheNodesOfferings(Paginator):
    def paginate(self, ReservedCacheNodesOfferingId: str = None, CacheNodeType: str = None, Duration: str = None, ProductDescription: str = None, OfferingType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSnapshots(Paginator):
    def paginate(self, ReplicationGroupId: str = None, CacheClusterId: str = None, SnapshotName: str = None, SnapshotSource: str = None, ShowNodeGroupConfig: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass
