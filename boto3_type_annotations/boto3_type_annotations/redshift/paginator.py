from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class DescribeClusterDbRevisions(Paginator):
    def paginate(self, ClusterIdentifier: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClusterParameterGroups(Paginator):
    def paginate(self, ParameterGroupName: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClusterParameters(Paginator):
    def paginate(self, ParameterGroupName: str, Source: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClusterSecurityGroups(Paginator):
    def paginate(self, ClusterSecurityGroupName: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClusterSnapshots(Paginator):
    def paginate(self, ClusterIdentifier: str = None, SnapshotIdentifier: str = None, SnapshotType: str = None, StartTime: datetime = None, EndTime: datetime = None, OwnerAccount: str = None, TagKeys: List = None, TagValues: List = None, ClusterExists: bool = None, SortingEntities: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClusterSubnetGroups(Paginator):
    def paginate(self, ClusterSubnetGroupName: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClusterTracks(Paginator):
    def paginate(self, MaintenanceTrackName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClusterVersions(Paginator):
    def paginate(self, ClusterVersion: str = None, ClusterParameterGroupFamily: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClusters(Paginator):
    def paginate(self, ClusterIdentifier: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDefaultClusterParameters(Paginator):
    def paginate(self, ParameterGroupFamily: str, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEventSubscriptions(Paginator):
    def paginate(self, SubscriptionName: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEvents(Paginator):
    def paginate(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeHsmClientCertificates(Paginator):
    def paginate(self, HsmClientCertificateIdentifier: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeHsmConfigurations(Paginator):
    def paginate(self, HsmConfigurationIdentifier: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeOrderableClusterOptions(Paginator):
    def paginate(self, ClusterVersion: str = None, NodeType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeReservedNodeOfferings(Paginator):
    def paginate(self, ReservedNodeOfferingId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeReservedNodes(Paginator):
    def paginate(self, ReservedNodeId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSnapshotCopyGrants(Paginator):
    def paginate(self, SnapshotCopyGrantName: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSnapshotSchedules(Paginator):
    def paginate(self, ClusterIdentifier: str = None, ScheduleIdentifier: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTableRestoreStatus(Paginator):
    def paginate(self, ClusterIdentifier: str = None, TableRestoreRequestId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTags(Paginator):
    def paginate(self, ResourceName: str = None, ResourceType: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetReservedNodeExchangeOfferings(Paginator):
    def paginate(self, ReservedNodeId: str, PaginationConfig: Dict = None) -> Dict:
        pass
