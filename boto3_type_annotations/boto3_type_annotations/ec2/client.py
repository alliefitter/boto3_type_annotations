from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def accept_reserved_instances_exchange_quote(self, ReservedInstanceIds: List, DryRun: bool = None, TargetConfigurations: List = None) -> Dict:
        pass

    def accept_vpc_endpoint_connections(self, ServiceId: str, VpcEndpointIds: List, DryRun: bool = None) -> Dict:
        pass

    def accept_vpc_peering_connection(self, DryRun: bool = None, VpcPeeringConnectionId: str = None) -> Dict:
        pass

    def advertise_byoip_cidr(self, Cidr: str, DryRun: bool = None) -> Dict:
        pass

    def allocate_address(self, Domain: str = None, Address: str = None, PublicIpv4Pool: str = None, DryRun: bool = None) -> Dict:
        pass

    def allocate_hosts(self, AvailabilityZone: str, InstanceType: str, Quantity: int, AutoPlacement: str = None, ClientToken: str = None, TagSpecifications: List = None) -> Dict:
        pass

    def assign_ipv6_addresses(self, NetworkInterfaceId: str, Ipv6AddressCount: int = None, Ipv6Addresses: List = None) -> Dict:
        pass

    def assign_private_ip_addresses(self, NetworkInterfaceId: str, AllowReassignment: bool = None, PrivateIpAddresses: List = None, SecondaryPrivateIpAddressCount: int = None) -> NoReturn:
        pass

    def associate_address(self, AllocationId: str = None, InstanceId: str = None, PublicIp: str = None, AllowReassociation: bool = None, DryRun: bool = None, NetworkInterfaceId: str = None, PrivateIpAddress: str = None) -> Dict:
        pass

    def associate_dhcp_options(self, DhcpOptionsId: str, VpcId: str, DryRun: bool = None) -> NoReturn:
        pass

    def associate_iam_instance_profile(self, IamInstanceProfile: Dict, InstanceId: str) -> Dict:
        pass

    def associate_route_table(self, RouteTableId: str, SubnetId: str, DryRun: bool = None) -> Dict:
        pass

    def associate_subnet_cidr_block(self, Ipv6CidrBlock: str, SubnetId: str) -> Dict:
        pass

    def associate_vpc_cidr_block(self, VpcId: str, AmazonProvidedIpv6CidrBlock: bool = None, CidrBlock: str = None) -> Dict:
        pass

    def attach_classic_link_vpc(self, Groups: List, InstanceId: str, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    def attach_internet_gateway(self, InternetGatewayId: str, VpcId: str, DryRun: bool = None) -> NoReturn:
        pass

    def attach_network_interface(self, DeviceIndex: int, InstanceId: str, NetworkInterfaceId: str, DryRun: bool = None) -> Dict:
        pass

    def attach_volume(self, Device: str, InstanceId: str, VolumeId: str, DryRun: bool = None) -> Dict:
        pass

    def attach_vpn_gateway(self, VpcId: str, VpnGatewayId: str, DryRun: bool = None) -> Dict:
        pass

    def authorize_security_group_egress(self, GroupId: str, DryRun: bool = None, IpPermissions: List = None, CidrIp: str = None, FromPort: int = None, IpProtocol: str = None, ToPort: int = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None) -> NoReturn:
        pass

    def authorize_security_group_ingress(self, CidrIp: str = None, FromPort: int = None, GroupId: str = None, GroupName: str = None, IpPermissions: List = None, IpProtocol: str = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None, ToPort: int = None, DryRun: bool = None) -> NoReturn:
        pass

    def bundle_instance(self, InstanceId: str, Storage: Dict, DryRun: bool = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def cancel_bundle_task(self, BundleId: str, DryRun: bool = None) -> Dict:
        pass

    def cancel_capacity_reservation(self, CapacityReservationId: str, DryRun: bool = None) -> Dict:
        pass

    def cancel_conversion_task(self, ConversionTaskId: str, DryRun: bool = None, ReasonMessage: str = None) -> NoReturn:
        pass

    def cancel_export_task(self, ExportTaskId: str) -> NoReturn:
        pass

    def cancel_import_task(self, CancelReason: str = None, DryRun: bool = None, ImportTaskId: str = None) -> Dict:
        pass

    def cancel_reserved_instances_listing(self, ReservedInstancesListingId: str) -> Dict:
        pass

    def cancel_spot_fleet_requests(self, SpotFleetRequestIds: List, TerminateInstances: bool, DryRun: bool = None) -> Dict:
        pass

    def cancel_spot_instance_requests(self, SpotInstanceRequestIds: List, DryRun: bool = None) -> Dict:
        pass

    def confirm_product_instance(self, InstanceId: str, ProductCode: str, DryRun: bool = None) -> Dict:
        pass

    def copy_fpga_image(self, SourceFpgaImageId: str, SourceRegion: str, DryRun: bool = None, Description: str = None, Name: str = None, ClientToken: str = None) -> Dict:
        pass

    def copy_image(self, Name: str, SourceImageId: str, SourceRegion: str, ClientToken: str = None, Description: str = None, Encrypted: bool = None, KmsKeyId: str = None, DryRun: bool = None) -> Dict:
        pass

    def copy_snapshot(self, SourceRegion: str, SourceSnapshotId: str, Description: str = None, DestinationRegion: str = None, Encrypted: bool = None, KmsKeyId: str = None, PresignedUrl: str = None, DryRun: bool = None) -> Dict:
        pass

    def create_capacity_reservation(self, InstanceType: str, InstancePlatform: str, AvailabilityZone: str, InstanceCount: int, ClientToken: str = None, Tenancy: str = None, EbsOptimized: bool = None, EphemeralStorage: bool = None, EndDate: datetime = None, EndDateType: str = None, InstanceMatchCriteria: str = None, TagSpecifications: List = None, DryRun: bool = None) -> Dict:
        pass

    def create_customer_gateway(self, BgpAsn: int, PublicIp: str, Type: str, DryRun: bool = None) -> Dict:
        pass

    def create_default_subnet(self, AvailabilityZone: str, DryRun: bool = None) -> Dict:
        pass

    def create_default_vpc(self, DryRun: bool = None) -> Dict:
        pass

    def create_dhcp_options(self, DhcpConfigurations: List, DryRun: bool = None) -> Dict:
        pass

    def create_egress_only_internet_gateway(self, VpcId: str, ClientToken: str = None, DryRun: bool = None) -> Dict:
        pass

    def create_fleet(self, LaunchTemplateConfigs: List, TargetCapacitySpecification: Dict, DryRun: bool = None, ClientToken: str = None, SpotOptions: Dict = None, OnDemandOptions: Dict = None, ExcessCapacityTerminationPolicy: str = None, TerminateInstancesWithExpiration: bool = None, Type: str = None, ValidFrom: datetime = None, ValidUntil: datetime = None, ReplaceUnhealthyInstances: bool = None, TagSpecifications: List = None) -> Dict:
        pass

    def create_flow_logs(self, ResourceIds: List, ResourceType: str, TrafficType: str, DryRun: bool = None, ClientToken: str = None, DeliverLogsPermissionArn: str = None, LogGroupName: str = None, LogDestinationType: str = None, LogDestination: str = None) -> Dict:
        pass

    def create_fpga_image(self, InputStorageLocation: Dict, DryRun: bool = None, LogsStorageLocation: Dict = None, Description: str = None, Name: str = None, ClientToken: str = None) -> Dict:
        pass

    def create_image(self, InstanceId: str, Name: str, BlockDeviceMappings: List = None, Description: str = None, DryRun: bool = None, NoReboot: bool = None) -> Dict:
        pass

    def create_instance_export_task(self, InstanceId: str, Description: str = None, ExportToS3Task: Dict = None, TargetEnvironment: str = None) -> Dict:
        pass

    def create_internet_gateway(self, DryRun: bool = None) -> Dict:
        pass

    def create_key_pair(self, KeyName: str, DryRun: bool = None) -> Dict:
        pass

    def create_launch_template(self, LaunchTemplateName: str, LaunchTemplateData: Dict, DryRun: bool = None, ClientToken: str = None, VersionDescription: str = None) -> Dict:
        pass

    def create_launch_template_version(self, LaunchTemplateData: Dict, DryRun: bool = None, ClientToken: str = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None, SourceVersion: str = None, VersionDescription: str = None) -> Dict:
        pass

    def create_nat_gateway(self, AllocationId: str, SubnetId: str, ClientToken: str = None) -> Dict:
        pass

    def create_network_acl(self, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    def create_network_acl_entry(self, Egress: bool, NetworkAclId: str, Protocol: str, RuleAction: str, RuleNumber: int, CidrBlock: str = None, DryRun: bool = None, IcmpTypeCode: Dict = None, Ipv6CidrBlock: str = None, PortRange: Dict = None) -> NoReturn:
        pass

    def create_network_interface(self, SubnetId: str, Description: str = None, DryRun: bool = None, Groups: List = None, Ipv6AddressCount: int = None, Ipv6Addresses: List = None, PrivateIpAddress: str = None, PrivateIpAddresses: List = None, SecondaryPrivateIpAddressCount: int = None) -> Dict:
        pass

    def create_network_interface_permission(self, NetworkInterfaceId: str, Permission: str, AwsAccountId: str = None, AwsService: str = None, DryRun: bool = None) -> Dict:
        pass

    def create_placement_group(self, GroupName: str, Strategy: str, DryRun: bool = None) -> NoReturn:
        pass

    def create_reserved_instances_listing(self, ClientToken: str, InstanceCount: int, PriceSchedules: List, ReservedInstancesId: str) -> Dict:
        pass

    def create_route(self, RouteTableId: str, DestinationCidrBlock: str = None, DestinationIpv6CidrBlock: str = None, DryRun: bool = None, EgressOnlyInternetGatewayId: str = None, GatewayId: str = None, InstanceId: str = None, NatGatewayId: str = None, NetworkInterfaceId: str = None, VpcPeeringConnectionId: str = None) -> Dict:
        pass

    def create_route_table(self, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    def create_security_group(self, Description: str, GroupName: str, VpcId: str = None, DryRun: bool = None) -> Dict:
        pass

    def create_snapshot(self, VolumeId: str, Description: str = None, TagSpecifications: List = None, DryRun: bool = None) -> Dict:
        pass

    def create_spot_datafeed_subscription(self, Bucket: str, DryRun: bool = None, Prefix: str = None) -> Dict:
        pass

    def create_subnet(self, CidrBlock: str, VpcId: str, AvailabilityZone: str = None, Ipv6CidrBlock: str = None, DryRun: bool = None) -> Dict:
        pass

    def create_tags(self, Resources: List, Tags: List, DryRun: bool = None) -> NoReturn:
        pass

    def create_volume(self, AvailabilityZone: str, Encrypted: bool = None, Iops: int = None, KmsKeyId: str = None, Size: int = None, SnapshotId: str = None, VolumeType: str = None, DryRun: bool = None, TagSpecifications: List = None) -> Dict:
        pass

    def create_vpc(self, CidrBlock: str, AmazonProvidedIpv6CidrBlock: bool = None, DryRun: bool = None, InstanceTenancy: str = None) -> Dict:
        pass

    def create_vpc_endpoint(self, VpcId: str, ServiceName: str, DryRun: bool = None, VpcEndpointType: str = None, PolicyDocument: str = None, RouteTableIds: List = None, SubnetIds: List = None, SecurityGroupIds: List = None, ClientToken: str = None, PrivateDnsEnabled: bool = None) -> Dict:
        pass

    def create_vpc_endpoint_connection_notification(self, ConnectionNotificationArn: str, ConnectionEvents: List, DryRun: bool = None, ServiceId: str = None, VpcEndpointId: str = None, ClientToken: str = None) -> Dict:
        pass

    def create_vpc_endpoint_service_configuration(self, NetworkLoadBalancerArns: List, DryRun: bool = None, AcceptanceRequired: bool = None, ClientToken: str = None) -> Dict:
        pass

    def create_vpc_peering_connection(self, DryRun: bool = None, PeerOwnerId: str = None, PeerVpcId: str = None, VpcId: str = None, PeerRegion: str = None) -> Dict:
        pass

    def create_vpn_connection(self, CustomerGatewayId: str, Type: str, VpnGatewayId: str, DryRun: bool = None, Options: Dict = None) -> Dict:
        pass

    def create_vpn_connection_route(self, DestinationCidrBlock: str, VpnConnectionId: str) -> NoReturn:
        pass

    def create_vpn_gateway(self, Type: str, AvailabilityZone: str = None, AmazonSideAsn: int = None, DryRun: bool = None) -> Dict:
        pass

    def delete_customer_gateway(self, CustomerGatewayId: str, DryRun: bool = None) -> NoReturn:
        pass

    def delete_dhcp_options(self, DhcpOptionsId: str, DryRun: bool = None) -> NoReturn:
        pass

    def delete_egress_only_internet_gateway(self, EgressOnlyInternetGatewayId: str, DryRun: bool = None) -> Dict:
        pass

    def delete_fleets(self, FleetIds: List, TerminateInstances: bool, DryRun: bool = None) -> Dict:
        pass

    def delete_flow_logs(self, FlowLogIds: List, DryRun: bool = None) -> Dict:
        pass

    def delete_fpga_image(self, FpgaImageId: str, DryRun: bool = None) -> Dict:
        pass

    def delete_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None) -> NoReturn:
        pass

    def delete_key_pair(self, KeyName: str, DryRun: bool = None) -> NoReturn:
        pass

    def delete_launch_template(self, DryRun: bool = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None) -> Dict:
        pass

    def delete_launch_template_versions(self, Versions: List, DryRun: bool = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None) -> Dict:
        pass

    def delete_nat_gateway(self, NatGatewayId: str) -> Dict:
        pass

    def delete_network_acl(self, NetworkAclId: str, DryRun: bool = None) -> NoReturn:
        pass

    def delete_network_acl_entry(self, Egress: bool, NetworkAclId: str, RuleNumber: int, DryRun: bool = None) -> NoReturn:
        pass

    def delete_network_interface(self, NetworkInterfaceId: str, DryRun: bool = None) -> NoReturn:
        pass

    def delete_network_interface_permission(self, NetworkInterfacePermissionId: str, Force: bool = None, DryRun: bool = None) -> Dict:
        pass

    def delete_placement_group(self, GroupName: str, DryRun: bool = None) -> NoReturn:
        pass

    def delete_route(self, RouteTableId: str, DestinationCidrBlock: str = None, DestinationIpv6CidrBlock: str = None, DryRun: bool = None) -> NoReturn:
        pass

    def delete_route_table(self, RouteTableId: str, DryRun: bool = None) -> NoReturn:
        pass

    def delete_security_group(self, GroupId: str = None, GroupName: str = None, DryRun: bool = None) -> NoReturn:
        pass

    def delete_snapshot(self, SnapshotId: str, DryRun: bool = None) -> NoReturn:
        pass

    def delete_spot_datafeed_subscription(self, DryRun: bool = None) -> NoReturn:
        pass

    def delete_subnet(self, SubnetId: str, DryRun: bool = None) -> NoReturn:
        pass

    def delete_tags(self, Resources: List, DryRun: bool = None, Tags: List = None) -> NoReturn:
        pass

    def delete_volume(self, VolumeId: str, DryRun: bool = None) -> NoReturn:
        pass

    def delete_vpc(self, VpcId: str, DryRun: bool = None) -> NoReturn:
        pass

    def delete_vpc_endpoint_connection_notifications(self, ConnectionNotificationIds: List, DryRun: bool = None) -> Dict:
        pass

    def delete_vpc_endpoint_service_configurations(self, ServiceIds: List, DryRun: bool = None) -> Dict:
        pass

    def delete_vpc_endpoints(self, VpcEndpointIds: List, DryRun: bool = None) -> Dict:
        pass

    def delete_vpc_peering_connection(self, VpcPeeringConnectionId: str, DryRun: bool = None) -> Dict:
        pass

    def delete_vpn_connection(self, VpnConnectionId: str, DryRun: bool = None) -> NoReturn:
        pass

    def delete_vpn_connection_route(self, DestinationCidrBlock: str, VpnConnectionId: str) -> NoReturn:
        pass

    def delete_vpn_gateway(self, VpnGatewayId: str, DryRun: bool = None) -> NoReturn:
        pass

    def deprovision_byoip_cidr(self, Cidr: str, DryRun: bool = None) -> Dict:
        pass

    def deregister_image(self, ImageId: str, DryRun: bool = None) -> NoReturn:
        pass

    def describe_account_attributes(self, AttributeNames: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_addresses(self, Filters: List = None, PublicIps: List = None, AllocationIds: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_aggregate_id_format(self, DryRun: bool = None) -> Dict:
        pass

    def describe_availability_zones(self, Filters: List = None, ZoneNames: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_bundle_tasks(self, BundleIds: List = None, Filters: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_byoip_cidrs(self, MaxResults: int, DryRun: bool = None, NextToken: str = None) -> Dict:
        pass

    def describe_capacity_reservations(self, CapacityReservationIds: List = None, NextToken: str = None, MaxResults: int = None, Filters: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_classic_link_instances(self, Filters: List = None, DryRun: bool = None, InstanceIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_conversion_tasks(self, ConversionTaskIds: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_customer_gateways(self, CustomerGatewayIds: List = None, Filters: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_dhcp_options(self, DhcpOptionsIds: List = None, Filters: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_egress_only_internet_gateways(self, DryRun: bool = None, EgressOnlyInternetGatewayIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_elastic_gpus(self, ElasticGpuIds: List = None, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_export_tasks(self, ExportTaskIds: List = None) -> Dict:
        pass

    def describe_fleet_history(self, FleetId: str, StartTime: datetime, DryRun: bool = None, EventType: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_fleet_instances(self, FleetId: str, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        pass

    def describe_fleets(self, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, FleetIds: List = None, Filters: List = None) -> Dict:
        pass

    def describe_flow_logs(self, DryRun: bool = None, Filters: List = None, FlowLogIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_fpga_image_attribute(self, FpgaImageId: str, Attribute: str, DryRun: bool = None) -> Dict:
        pass

    def describe_fpga_images(self, DryRun: bool = None, FpgaImageIds: List = None, Owners: List = None, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_host_reservation_offerings(self, Filters: List = None, MaxDuration: int = None, MaxResults: int = None, MinDuration: int = None, NextToken: str = None, OfferingId: str = None) -> Dict:
        pass

    def describe_host_reservations(self, Filters: List = None, HostReservationIdSet: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_hosts(self, Filters: List = None, HostIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_iam_instance_profile_associations(self, AssociationIds: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_id_format(self, Resource: str = None) -> Dict:
        pass

    def describe_identity_id_format(self, PrincipalArn: str, Resource: str = None) -> Dict:
        pass

    def describe_image_attribute(self, Attribute: str, ImageId: str, DryRun: bool = None) -> Dict:
        pass

    def describe_images(self, ExecutableUsers: List = None, Filters: List = None, ImageIds: List = None, Owners: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_import_image_tasks(self, DryRun: bool = None, Filters: List = None, ImportTaskIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_import_snapshot_tasks(self, DryRun: bool = None, Filters: List = None, ImportTaskIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_instance_attribute(self, Attribute: str, InstanceId: str, DryRun: bool = None) -> Dict:
        pass

    def describe_instance_credit_specifications(self, DryRun: bool = None, Filters: List = None, InstanceIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_instance_status(self, Filters: List = None, InstanceIds: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None, IncludeAllInstances: bool = None) -> Dict:
        pass

    def describe_instances(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_internet_gateways(self, Filters: List = None, DryRun: bool = None, InternetGatewayIds: List = None) -> Dict:
        pass

    def describe_key_pairs(self, Filters: List = None, KeyNames: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_launch_template_versions(self, DryRun: bool = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None, Versions: List = None, MinVersion: str = None, MaxVersion: str = None, NextToken: str = None, MaxResults: int = None, Filters: List = None) -> Dict:
        pass

    def describe_launch_templates(self, DryRun: bool = None, LaunchTemplateIds: List = None, LaunchTemplateNames: List = None, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_moving_addresses(self, Filters: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, PublicIps: List = None) -> Dict:
        pass

    def describe_nat_gateways(self, Filters: List = None, MaxResults: int = None, NatGatewayIds: List = None, NextToken: str = None) -> Dict:
        pass

    def describe_network_acls(self, Filters: List = None, DryRun: bool = None, NetworkAclIds: List = None) -> Dict:
        pass

    def describe_network_interface_attribute(self, NetworkInterfaceId: str, Attribute: str = None, DryRun: bool = None) -> Dict:
        pass

    def describe_network_interface_permissions(self, NetworkInterfacePermissionIds: List = None, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_network_interfaces(self, Filters: List = None, DryRun: bool = None, NetworkInterfaceIds: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_placement_groups(self, Filters: List = None, DryRun: bool = None, GroupNames: List = None) -> Dict:
        pass

    def describe_prefix_lists(self, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None, PrefixListIds: List = None) -> Dict:
        pass

    def describe_principal_id_format(self, DryRun: bool = None, Resources: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_public_ipv4_pools(self, PoolIds: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_regions(self, Filters: List = None, RegionNames: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_reserved_instances(self, Filters: List = None, OfferingClass: str = None, ReservedInstancesIds: List = None, DryRun: bool = None, OfferingType: str = None) -> Dict:
        pass

    def describe_reserved_instances_listings(self, Filters: List = None, ReservedInstancesId: str = None, ReservedInstancesListingId: str = None) -> Dict:
        pass

    def describe_reserved_instances_modifications(self, Filters: List = None, ReservedInstancesModificationIds: List = None, NextToken: str = None) -> Dict:
        pass

    def describe_reserved_instances_offerings(self, AvailabilityZone: str = None, Filters: List = None, IncludeMarketplace: bool = None, InstanceType: str = None, MaxDuration: int = None, MaxInstanceCount: int = None, MinDuration: int = None, OfferingClass: str = None, ProductDescription: str = None, ReservedInstancesOfferingIds: List = None, DryRun: bool = None, InstanceTenancy: str = None, MaxResults: int = None, NextToken: str = None, OfferingType: str = None) -> Dict:
        pass

    def describe_route_tables(self, Filters: List = None, DryRun: bool = None, RouteTableIds: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_scheduled_instance_availability(self, FirstSlotStartTimeRange: Dict, Recurrence: Dict, DryRun: bool = None, Filters: List = None, MaxResults: int = None, MaxSlotDurationInHours: int = None, MinSlotDurationInHours: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_scheduled_instances(self, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None, ScheduledInstanceIds: List = None, SlotStartTimeRange: Dict = None) -> Dict:
        pass

    def describe_security_group_references(self, GroupId: List, DryRun: bool = None) -> Dict:
        pass

    def describe_security_groups(self, Filters: List = None, GroupIds: List = None, GroupNames: List = None, DryRun: bool = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_snapshot_attribute(self, Attribute: str, SnapshotId: str, DryRun: bool = None) -> Dict:
        pass

    def describe_snapshots(self, Filters: List = None, MaxResults: int = None, NextToken: str = None, OwnerIds: List = None, RestorableByUserIds: List = None, SnapshotIds: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_spot_datafeed_subscription(self, DryRun: bool = None) -> Dict:
        pass

    def describe_spot_fleet_instances(self, SpotFleetRequestId: str, DryRun: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_spot_fleet_request_history(self, SpotFleetRequestId: str, StartTime: datetime, DryRun: bool = None, EventType: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_spot_fleet_requests(self, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, SpotFleetRequestIds: List = None) -> Dict:
        pass

    def describe_spot_instance_requests(self, Filters: List = None, DryRun: bool = None, SpotInstanceRequestIds: List = None) -> Dict:
        pass

    def describe_spot_price_history(self, Filters: List = None, AvailabilityZone: str = None, DryRun: bool = None, EndTime: datetime = None, InstanceTypes: List = None, MaxResults: int = None, NextToken: str = None, ProductDescriptions: List = None, StartTime: datetime = None) -> Dict:
        pass

    def describe_stale_security_groups(self, VpcId: str, DryRun: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_subnets(self, Filters: List = None, SubnetIds: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_tags(self, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_volume_attribute(self, Attribute: str, VolumeId: str, DryRun: bool = None) -> Dict:
        pass

    def describe_volume_status(self, Filters: List = None, MaxResults: int = None, NextToken: str = None, VolumeIds: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_volumes(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_volumes_modifications(self, DryRun: bool = None, VolumeIds: List = None, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def describe_vpc_attribute(self, Attribute: str, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    def describe_vpc_classic_link(self, Filters: List = None, DryRun: bool = None, VpcIds: List = None) -> Dict:
        pass

    def describe_vpc_classic_link_dns_support(self, MaxResults: int = None, NextToken: str = None, VpcIds: List = None) -> Dict:
        pass

    def describe_vpc_endpoint_connection_notifications(self, DryRun: bool = None, ConnectionNotificationId: str = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_vpc_endpoint_connections(self, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_vpc_endpoint_service_configurations(self, DryRun: bool = None, ServiceIds: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_vpc_endpoint_service_permissions(self, ServiceId: str, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_vpc_endpoint_services(self, DryRun: bool = None, ServiceNames: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_vpc_endpoints(self, DryRun: bool = None, VpcEndpointIds: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def describe_vpc_peering_connections(self, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None) -> Dict:
        pass

    def describe_vpcs(self, Filters: List = None, VpcIds: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_vpn_connections(self, Filters: List = None, VpnConnectionIds: List = None, DryRun: bool = None) -> Dict:
        pass

    def describe_vpn_gateways(self, Filters: List = None, VpnGatewayIds: List = None, DryRun: bool = None) -> Dict:
        pass

    def detach_classic_link_vpc(self, InstanceId: str, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    def detach_internet_gateway(self, InternetGatewayId: str, VpcId: str, DryRun: bool = None) -> NoReturn:
        pass

    def detach_network_interface(self, AttachmentId: str, DryRun: bool = None, Force: bool = None) -> NoReturn:
        pass

    def detach_volume(self, VolumeId: str, Device: str = None, Force: bool = None, InstanceId: str = None, DryRun: bool = None) -> Dict:
        pass

    def detach_vpn_gateway(self, VpcId: str, VpnGatewayId: str, DryRun: bool = None) -> NoReturn:
        pass

    def disable_vgw_route_propagation(self, GatewayId: str, RouteTableId: str) -> NoReturn:
        pass

    def disable_vpc_classic_link(self, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    def disable_vpc_classic_link_dns_support(self, VpcId: str = None) -> Dict:
        pass

    def disassociate_address(self, AssociationId: str = None, PublicIp: str = None, DryRun: bool = None) -> NoReturn:
        pass

    def disassociate_iam_instance_profile(self, AssociationId: str) -> Dict:
        pass

    def disassociate_route_table(self, AssociationId: str, DryRun: bool = None) -> NoReturn:
        pass

    def disassociate_subnet_cidr_block(self, AssociationId: str) -> Dict:
        pass

    def disassociate_vpc_cidr_block(self, AssociationId: str) -> Dict:
        pass

    def enable_vgw_route_propagation(self, GatewayId: str, RouteTableId: str) -> NoReturn:
        pass

    def enable_volume_io(self, VolumeId: str, DryRun: bool = None) -> NoReturn:
        pass

    def enable_vpc_classic_link(self, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    def enable_vpc_classic_link_dns_support(self, VpcId: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_console_output(self, InstanceId: str, DryRun: bool = None, Latest: bool = None) -> Dict:
        pass

    def get_console_screenshot(self, InstanceId: str, DryRun: bool = None, WakeUp: bool = None) -> Dict:
        pass

    def get_host_reservation_purchase_preview(self, HostIdSet: List, OfferingId: str) -> Dict:
        pass

    def get_launch_template_data(self, InstanceId: str, DryRun: bool = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_password_data(self, InstanceId: str, DryRun: bool = None) -> Dict:
        pass

    def get_reserved_instances_exchange_quote(self, ReservedInstanceIds: List, DryRun: bool = None, TargetConfigurations: List = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def import_image(self, Architecture: str = None, ClientData: Dict = None, ClientToken: str = None, Description: str = None, DiskContainers: List = None, DryRun: bool = None, Encrypted: bool = None, Hypervisor: str = None, KmsKeyId: str = None, LicenseType: str = None, Platform: str = None, RoleName: str = None) -> Dict:
        pass

    def import_instance(self, Platform: str, Description: str = None, DiskImages: List = None, DryRun: bool = None, LaunchSpecification: Dict = None) -> Dict:
        pass

    def import_key_pair(self, KeyName: str, PublicKeyMaterial: bytes, DryRun: bool = None) -> Dict:
        pass

    def import_snapshot(self, ClientData: Dict = None, ClientToken: str = None, Description: str = None, DiskContainer: Dict = None, DryRun: bool = None, Encrypted: bool = None, KmsKeyId: str = None, RoleName: str = None) -> Dict:
        pass

    def import_volume(self, AvailabilityZone: str, Image: Dict, Volume: Dict, Description: str = None, DryRun: bool = None) -> Dict:
        pass

    def modify_capacity_reservation(self, CapacityReservationId: str, InstanceCount: int = None, EndDate: datetime = None, EndDateType: str = None, DryRun: bool = None) -> Dict:
        pass

    def modify_fleet(self, FleetId: str, TargetCapacitySpecification: Dict, DryRun: bool = None, ExcessCapacityTerminationPolicy: str = None) -> Dict:
        pass

    def modify_fpga_image_attribute(self, FpgaImageId: str, DryRun: bool = None, Attribute: str = None, OperationType: str = None, UserIds: List = None, UserGroups: List = None, ProductCodes: List = None, LoadPermission: Dict = None, Description: str = None, Name: str = None) -> Dict:
        pass

    def modify_hosts(self, AutoPlacement: str, HostIds: List) -> Dict:
        pass

    def modify_id_format(self, Resource: str, UseLongIds: bool) -> NoReturn:
        pass

    def modify_identity_id_format(self, PrincipalArn: str, Resource: str, UseLongIds: bool) -> NoReturn:
        pass

    def modify_image_attribute(self, ImageId: str, Attribute: str = None, Description: Dict = None, LaunchPermission: Dict = None, OperationType: str = None, ProductCodes: List = None, UserGroups: List = None, UserIds: List = None, Value: str = None, DryRun: bool = None) -> NoReturn:
        pass

    def modify_instance_attribute(self, InstanceId: str, SourceDestCheck: Dict = None, Attribute: str = None, BlockDeviceMappings: List = None, DisableApiTermination: Dict = None, DryRun: bool = None, EbsOptimized: Dict = None, EnaSupport: Dict = None, Groups: List = None, InstanceInitiatedShutdownBehavior: Dict = None, InstanceType: Dict = None, Kernel: Dict = None, Ramdisk: Dict = None, SriovNetSupport: Dict = None, UserData: Dict = None, Value: str = None) -> NoReturn:
        pass

    def modify_instance_capacity_reservation_attributes(self, InstanceId: str, CapacityReservationSpecification: Dict, DryRun: bool = None) -> Dict:
        pass

    def modify_instance_credit_specification(self, InstanceCreditSpecifications: List, DryRun: bool = None, ClientToken: str = None) -> Dict:
        pass

    def modify_instance_placement(self, InstanceId: str, Affinity: str = None, GroupName: str = None, HostId: str = None, Tenancy: str = None) -> Dict:
        pass

    def modify_launch_template(self, DryRun: bool = None, ClientToken: str = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None, DefaultVersion: str = None) -> Dict:
        pass

    def modify_network_interface_attribute(self, NetworkInterfaceId: str, Attachment: Dict = None, Description: Dict = None, DryRun: bool = None, Groups: List = None, SourceDestCheck: Dict = None) -> NoReturn:
        pass

    def modify_reserved_instances(self, ReservedInstancesIds: List, TargetConfigurations: List, ClientToken: str = None) -> Dict:
        pass

    def modify_snapshot_attribute(self, SnapshotId: str, Attribute: str = None, CreateVolumePermission: Dict = None, GroupNames: List = None, OperationType: str = None, UserIds: List = None, DryRun: bool = None) -> NoReturn:
        pass

    def modify_spot_fleet_request(self, SpotFleetRequestId: str, ExcessCapacityTerminationPolicy: str = None, TargetCapacity: int = None) -> Dict:
        pass

    def modify_subnet_attribute(self, SubnetId: str, AssignIpv6AddressOnCreation: Dict = None, MapPublicIpOnLaunch: Dict = None) -> NoReturn:
        pass

    def modify_volume(self, VolumeId: str, DryRun: bool = None, Size: int = None, VolumeType: str = None, Iops: int = None) -> Dict:
        pass

    def modify_volume_attribute(self, VolumeId: str, AutoEnableIO: Dict = None, DryRun: bool = None) -> NoReturn:
        pass

    def modify_vpc_attribute(self, VpcId: str, EnableDnsHostnames: Dict = None, EnableDnsSupport: Dict = None) -> NoReturn:
        pass

    def modify_vpc_endpoint(self, VpcEndpointId: str, DryRun: bool = None, ResetPolicy: bool = None, PolicyDocument: str = None, AddRouteTableIds: List = None, RemoveRouteTableIds: List = None, AddSubnetIds: List = None, RemoveSubnetIds: List = None, AddSecurityGroupIds: List = None, RemoveSecurityGroupIds: List = None, PrivateDnsEnabled: bool = None) -> Dict:
        pass

    def modify_vpc_endpoint_connection_notification(self, ConnectionNotificationId: str, DryRun: bool = None, ConnectionNotificationArn: str = None, ConnectionEvents: List = None) -> Dict:
        pass

    def modify_vpc_endpoint_service_configuration(self, ServiceId: str, DryRun: bool = None, AcceptanceRequired: bool = None, AddNetworkLoadBalancerArns: List = None, RemoveNetworkLoadBalancerArns: List = None) -> Dict:
        pass

    def modify_vpc_endpoint_service_permissions(self, ServiceId: str, DryRun: bool = None, AddAllowedPrincipals: List = None, RemoveAllowedPrincipals: List = None) -> Dict:
        pass

    def modify_vpc_peering_connection_options(self, VpcPeeringConnectionId: str, AccepterPeeringConnectionOptions: Dict = None, DryRun: bool = None, RequesterPeeringConnectionOptions: Dict = None) -> Dict:
        pass

    def modify_vpc_tenancy(self, VpcId: str, InstanceTenancy: str, DryRun: bool = None) -> Dict:
        pass

    def monitor_instances(self, InstanceIds: List, DryRun: bool = None) -> Dict:
        pass

    def move_address_to_vpc(self, PublicIp: str, DryRun: bool = None) -> Dict:
        pass

    def provision_byoip_cidr(self, Cidr: str, CidrAuthorizationContext: Dict = None, Description: str = None, DryRun: bool = None) -> Dict:
        pass

    def purchase_host_reservation(self, HostIdSet: List, OfferingId: str, ClientToken: str = None, CurrencyCode: str = None, LimitPrice: str = None) -> Dict:
        pass

    def purchase_reserved_instances_offering(self, InstanceCount: int, ReservedInstancesOfferingId: str, DryRun: bool = None, LimitPrice: Dict = None) -> Dict:
        pass

    def purchase_scheduled_instances(self, PurchaseRequests: List, ClientToken: str = None, DryRun: bool = None) -> Dict:
        pass

    def reboot_instances(self, InstanceIds: List, DryRun: bool = None) -> NoReturn:
        pass

    def register_image(self, Name: str, ImageLocation: str = None, Architecture: str = None, BlockDeviceMappings: List = None, Description: str = None, DryRun: bool = None, EnaSupport: bool = None, KernelId: str = None, BillingProducts: List = None, RamdiskId: str = None, RootDeviceName: str = None, SriovNetSupport: str = None, VirtualizationType: str = None) -> Dict:
        pass

    def reject_vpc_endpoint_connections(self, ServiceId: str, VpcEndpointIds: List, DryRun: bool = None) -> Dict:
        pass

    def reject_vpc_peering_connection(self, VpcPeeringConnectionId: str, DryRun: bool = None) -> Dict:
        pass

    def release_address(self, AllocationId: str = None, PublicIp: str = None, DryRun: bool = None) -> NoReturn:
        pass

    def release_hosts(self, HostIds: List) -> Dict:
        pass

    def replace_iam_instance_profile_association(self, IamInstanceProfile: Dict, AssociationId: str) -> Dict:
        pass

    def replace_network_acl_association(self, AssociationId: str, NetworkAclId: str, DryRun: bool = None) -> Dict:
        pass

    def replace_network_acl_entry(self, Egress: bool, NetworkAclId: str, Protocol: str, RuleAction: str, RuleNumber: int, CidrBlock: str = None, DryRun: bool = None, IcmpTypeCode: Dict = None, Ipv6CidrBlock: str = None, PortRange: Dict = None) -> NoReturn:
        pass

    def replace_route(self, RouteTableId: str, DestinationCidrBlock: str = None, DestinationIpv6CidrBlock: str = None, DryRun: bool = None, EgressOnlyInternetGatewayId: str = None, GatewayId: str = None, InstanceId: str = None, NatGatewayId: str = None, NetworkInterfaceId: str = None, VpcPeeringConnectionId: str = None) -> NoReturn:
        pass

    def replace_route_table_association(self, AssociationId: str, RouteTableId: str, DryRun: bool = None) -> Dict:
        pass

    def report_instance_status(self, Instances: List, ReasonCodes: List, Status: str, Description: str = None, DryRun: bool = None, EndTime: datetime = None, StartTime: datetime = None) -> NoReturn:
        pass

    def request_spot_fleet(self, SpotFleetRequestConfig: Dict, DryRun: bool = None) -> Dict:
        pass

    def request_spot_instances(self, AvailabilityZoneGroup: str = None, BlockDurationMinutes: int = None, ClientToken: str = None, DryRun: bool = None, InstanceCount: int = None, LaunchGroup: str = None, LaunchSpecification: Dict = None, SpotPrice: str = None, Type: str = None, ValidFrom: datetime = None, ValidUntil: datetime = None, InstanceInterruptionBehavior: str = None) -> Dict:
        pass

    def reset_fpga_image_attribute(self, FpgaImageId: str, DryRun: bool = None, Attribute: str = None) -> Dict:
        pass

    def reset_image_attribute(self, Attribute: str, ImageId: str, DryRun: bool = None) -> NoReturn:
        pass

    def reset_instance_attribute(self, Attribute: str, InstanceId: str, DryRun: bool = None) -> NoReturn:
        pass

    def reset_network_interface_attribute(self, NetworkInterfaceId: str, DryRun: bool = None, SourceDestCheck: str = None) -> NoReturn:
        pass

    def reset_snapshot_attribute(self, Attribute: str, SnapshotId: str, DryRun: bool = None) -> NoReturn:
        pass

    def restore_address_to_classic(self, PublicIp: str, DryRun: bool = None) -> Dict:
        pass

    def revoke_security_group_egress(self, GroupId: str, DryRun: bool = None, IpPermissions: List = None, CidrIp: str = None, FromPort: int = None, IpProtocol: str = None, ToPort: int = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None) -> NoReturn:
        pass

    def revoke_security_group_ingress(self, CidrIp: str = None, FromPort: int = None, GroupId: str = None, GroupName: str = None, IpPermissions: List = None, IpProtocol: str = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None, ToPort: int = None, DryRun: bool = None) -> NoReturn:
        pass

    def run_instances(self, MaxCount: int, MinCount: int, BlockDeviceMappings: List = None, ImageId: str = None, InstanceType: str = None, Ipv6AddressCount: int = None, Ipv6Addresses: List = None, KernelId: str = None, KeyName: str = None, Monitoring: Dict = None, Placement: Dict = None, RamdiskId: str = None, SecurityGroupIds: List = None, SecurityGroups: List = None, SubnetId: str = None, UserData: str = None, AdditionalInfo: str = None, ClientToken: str = None, DisableApiTermination: bool = None, DryRun: bool = None, EbsOptimized: bool = None, IamInstanceProfile: Dict = None, InstanceInitiatedShutdownBehavior: str = None, NetworkInterfaces: List = None, PrivateIpAddress: str = None, ElasticGpuSpecification: List = None, TagSpecifications: List = None, LaunchTemplate: Dict = None, InstanceMarketOptions: Dict = None, CreditSpecification: Dict = None, CpuOptions: Dict = None, CapacityReservationSpecification: Dict = None) -> Dict:
        pass

    def run_scheduled_instances(self, LaunchSpecification: Dict, ScheduledInstanceId: str, ClientToken: str = None, DryRun: bool = None, InstanceCount: int = None) -> Dict:
        pass

    def start_instances(self, InstanceIds: List, AdditionalInfo: str = None, DryRun: bool = None) -> Dict:
        pass

    def stop_instances(self, InstanceIds: List, DryRun: bool = None, Force: bool = None) -> Dict:
        pass

    def terminate_instances(self, InstanceIds: List, DryRun: bool = None) -> Dict:
        pass

    def unassign_ipv6_addresses(self, Ipv6Addresses: List, NetworkInterfaceId: str) -> Dict:
        pass

    def unassign_private_ip_addresses(self, NetworkInterfaceId: str, PrivateIpAddresses: List) -> NoReturn:
        pass

    def unmonitor_instances(self, InstanceIds: List, DryRun: bool = None) -> Dict:
        pass

    def update_security_group_rule_descriptions_egress(self, IpPermissions: List, DryRun: bool = None, GroupId: str = None, GroupName: str = None) -> Dict:
        pass

    def update_security_group_rule_descriptions_ingress(self, IpPermissions: List, DryRun: bool = None, GroupId: str = None, GroupName: str = None) -> Dict:
        pass

    def withdraw_byoip_cidr(self, Cidr: str, DryRun: bool = None) -> Dict:
        pass
