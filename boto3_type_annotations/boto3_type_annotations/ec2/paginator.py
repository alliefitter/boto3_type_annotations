from typing import Dict
from datetime import datetime
from typing import List
from botocore.paginate import Paginator


class DescribeByoipCidrs(Paginator):
    def paginate(self, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeCapacityReservations(Paginator):
    def paginate(self, CapacityReservationIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClassicLinkInstances(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, InstanceIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClientVpnAuthorizationRules(Paginator):
    def paginate(self, ClientVpnEndpointId: str, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClientVpnConnections(Paginator):
    def paginate(self, ClientVpnEndpointId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClientVpnEndpoints(Paginator):
    def paginate(self, ClientVpnEndpointIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClientVpnRoutes(Paginator):
    def paginate(self, ClientVpnEndpointId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeClientVpnTargetNetworks(Paginator):
    def paginate(self, ClientVpnEndpointId: str, AssociationIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEgressOnlyInternetGateways(Paginator):
    def paginate(self, DryRun: bool = None, EgressOnlyInternetGatewayIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeFleets(Paginator):
    def paginate(self, DryRun: bool = None, FleetIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeFlowLogs(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, FlowLogIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeFpgaImages(Paginator):
    def paginate(self, DryRun: bool = None, FpgaImageIds: List = None, Owners: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeHostReservationOfferings(Paginator):
    def paginate(self, Filters: List = None, MaxDuration: int = None, MinDuration: int = None, OfferingId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeHostReservations(Paginator):
    def paginate(self, Filters: List = None, HostReservationIdSet: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeHosts(Paginator):
    def paginate(self, Filters: List = None, HostIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeIamInstanceProfileAssociations(Paginator):
    def paginate(self, AssociationIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeImportImageTasks(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, ImportTaskIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeImportSnapshotTasks(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, ImportTaskIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeInstanceCreditSpecifications(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, InstanceIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeInstanceStatus(Paginator):
    def paginate(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, IncludeAllInstances: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeInstances(Paginator):
    def paginate(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeInternetGateways(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, InternetGatewayIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeLaunchTemplateVersions(Paginator):
    def paginate(self, DryRun: bool = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None, Versions: List = None, MinVersion: str = None, MaxVersion: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeLaunchTemplates(Paginator):
    def paginate(self, DryRun: bool = None, LaunchTemplateIds: List = None, LaunchTemplateNames: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeMovingAddresses(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, PublicIps: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeNatGateways(Paginator):
    def paginate(self, Filters: List = None, NatGatewayIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeNetworkAcls(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, NetworkAclIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeNetworkInterfacePermissions(Paginator):
    def paginate(self, NetworkInterfacePermissionIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeNetworkInterfaces(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, NetworkInterfaceIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribePrefixLists(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, PrefixListIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribePrincipalIdFormat(Paginator):
    def paginate(self, DryRun: bool = None, Resources: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribePublicIpv4Pools(Paginator):
    def paginate(self, PoolIds: List = None, PaginationConfig: Dict = None) -> Dict:
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


class DescribeScheduledInstanceAvailability(Paginator):
    def paginate(self, FirstSlotStartTimeRange: Dict, Recurrence: Dict, DryRun: bool = None, Filters: List = None, MaxSlotDurationInHours: int = None, MinSlotDurationInHours: int = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeScheduledInstances(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, ScheduledInstanceIds: List = None, SlotStartTimeRange: Dict = None, PaginationConfig: Dict = None) -> Dict:
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


class DescribeSpotInstanceRequests(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, SpotInstanceRequestIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeSpotPriceHistory(Paginator):
    def paginate(self, Filters: List = None, AvailabilityZone: str = None, DryRun: bool = None, EndTime: datetime = None, InstanceTypes: List = None, ProductDescriptions: List = None, StartTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeStaleSecurityGroups(Paginator):
    def paginate(self, VpcId: str, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTags(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTransitGatewayAttachments(Paginator):
    def paginate(self, TransitGatewayAttachmentIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTransitGatewayRouteTables(Paginator):
    def paginate(self, TransitGatewayRouteTableIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTransitGatewayVpcAttachments(Paginator):
    def paginate(self, TransitGatewayAttachmentIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTransitGateways(Paginator):
    def paginate(self, TransitGatewayIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVolumeStatus(Paginator):
    def paginate(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVolumes(Paginator):
    def paginate(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVolumesModifications(Paginator):
    def paginate(self, DryRun: bool = None, VolumeIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVpcClassicLinkDnsSupport(Paginator):
    def paginate(self, VpcIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVpcEndpointConnectionNotifications(Paginator):
    def paginate(self, DryRun: bool = None, ConnectionNotificationId: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVpcEndpointConnections(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVpcEndpointServiceConfigurations(Paginator):
    def paginate(self, DryRun: bool = None, ServiceIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVpcEndpointServicePermissions(Paginator):
    def paginate(self, ServiceId: str, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVpcEndpointServices(Paginator):
    def paginate(self, DryRun: bool = None, ServiceNames: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVpcEndpoints(Paginator):
    def paginate(self, DryRun: bool = None, VpcEndpointIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVpcPeeringConnections(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVpcs(Paginator):
    def paginate(self, Filters: List = None, VpcIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetTransitGatewayAttachmentPropagations(Paginator):
    def paginate(self, TransitGatewayAttachmentId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetTransitGatewayRouteTableAssociations(Paginator):
    def paginate(self, TransitGatewayRouteTableId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetTransitGatewayRouteTablePropagations(Paginator):
    def paginate(self, TransitGatewayRouteTableId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass
