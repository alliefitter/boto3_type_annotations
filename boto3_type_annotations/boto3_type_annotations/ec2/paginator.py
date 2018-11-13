from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeIamInstanceProfileAssociations(Paginator):
    def paginate(self, AssociationIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeInstanceStatus(Paginator):
    def paginate(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, IncludeAllInstances: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeInstances(Paginator):
    def paginate(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeNatGateways(Paginator):
    def paginate(self, Filters: List = None, NatGatewayIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeNetworkInterfaces(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, NetworkInterfaceIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeReservedInstancesModifications(Paginator):
    def paginate(self, Filters: List = None, ReservedInstancesModificationIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeReservedInstancesOfferings(Paginator):
    def paginate(self, AvailabilityZone: str = None, Filters: List = None, IncludeMarketplace: bool = None, InstanceType: str = None, MaxDuration: int = None, MaxInstanceCount: int = None, MinDuration: int = None, OfferingClass: str = None, ProductDescription: str = None, ReservedInstancesOfferingIds: List = None, DryRun: bool = None, InstanceTenancy: str = None, OfferingType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeRouteTables(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, RouteTableIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSecurityGroups(Paginator):
    def paginate(self, Filters: List = None, GroupIds: List = None, GroupNames: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSnapshots(Paginator):
    def paginate(self, Filters: List = None, OwnerIds: List = None, RestorableByUserIds: List = None, SnapshotIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSpotFleetInstances(Paginator):
    def paginate(self, SpotFleetRequestId: str, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSpotFleetRequests(Paginator):
    def paginate(self, DryRun: bool = None, SpotFleetRequestIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSpotPriceHistory(Paginator):
    def paginate(self, Filters: List = None, AvailabilityZone: str = None, DryRun: bool = None, EndTime: datetime = None, InstanceTypes: List = None, ProductDescriptions: List = None, StartTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTags(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVolumeStatus(Paginator):
    def paginate(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVolumes(Paginator):
    def paginate(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass
