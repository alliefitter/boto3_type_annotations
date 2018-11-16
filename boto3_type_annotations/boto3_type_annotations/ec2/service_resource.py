from typing import List
from boto3.resources.collection import ResourceCollection
from typing import Optional
from typing import Union
from datetime import datetime
from typing import Dict
from boto3.resources import base


class ServiceResource(base.ServiceResource):
    classic_addresses: 'classic_addresses'
    dhcp_options_sets: 'dhcp_options_sets'
    images: 'images'
    instances: 'instances'
    internet_gateways: 'internet_gateways'
    key_pairs: 'key_pairs'
    network_acls: 'network_acls'
    network_interfaces: 'network_interfaces'
    placement_groups: 'placement_groups'
    route_tables: 'route_tables'
    security_groups: 'security_groups'
    snapshots: 'snapshots'
    subnets: 'subnets'
    volumes: 'volumes'
    vpc_addresses: 'vpc_addresses'
    vpc_peering_connections: 'vpc_peering_connections'
    vpcs: 'vpcs'

    def ClassicAddress(self, public_ip: str = None) -> 'ClassicAddress':
        pass

    def DhcpOptions(self, id: str = None) -> 'DhcpOptions':
        pass

    def Image(self, id: str = None) -> 'Image':
        pass

    def Instance(self, id: str = None) -> 'Instance':
        pass

    def InternetGateway(self, id: str = None) -> 'InternetGateway':
        pass

    def KeyPair(self, name: str = None) -> 'KeyPairInfo':
        pass

    def NetworkAcl(self, id: str = None) -> 'NetworkAcl':
        pass

    def NetworkInterface(self, id: str = None) -> 'NetworkInterface':
        pass

    def NetworkInterfaceAssociation(self, id: str = None) -> 'NetworkInterfaceAssociation':
        pass

    def PlacementGroup(self, name: str = None) -> 'PlacementGroup':
        pass

    def Route(self, route_table_id: str = None, destination_cidr_block: str = None) -> 'Route':
        pass

    def RouteTable(self, id: str = None) -> 'RouteTable':
        pass

    def RouteTableAssociation(self, id: str = None) -> 'RouteTableAssociation':
        pass

    def SecurityGroup(self, id: str = None) -> 'SecurityGroup':
        pass

    def Snapshot(self, id: str = None) -> 'Snapshot':
        pass

    def Subnet(self, id: str = None) -> 'Subnet':
        pass

    def Tag(self, resource_id: str = None, key: str = None, value: str = None) -> 'Tag':
        pass

    def Volume(self, id: str = None) -> 'Volume':
        pass

    def Vpc(self, id: str = None) -> 'Vpc':
        pass

    def VpcAddress(self, allocation_id: str = None) -> 'VpcAddress':
        pass

    def VpcPeeringConnection(self, id: str = None) -> 'VpcPeeringConnection':
        pass

    def create_dhcp_options(self, DhcpConfigurations: List, DryRun: bool = None) -> 'DhcpOptions':
        pass

    def create_instances(self, MaxCount: int, MinCount: int, BlockDeviceMappings: List = None, ImageId: str = None, InstanceType: str = None, Ipv6AddressCount: int = None, Ipv6Addresses: List = None, KernelId: str = None, KeyName: str = None, Monitoring: Dict = None, Placement: Dict = None, RamdiskId: str = None, SecurityGroupIds: List = None, SecurityGroups: List = None, SubnetId: str = None, UserData: str = None, AdditionalInfo: str = None, ClientToken: str = None, DisableApiTermination: bool = None, DryRun: bool = None, EbsOptimized: bool = None, IamInstanceProfile: Dict = None, InstanceInitiatedShutdownBehavior: str = None, NetworkInterfaces: List = None, PrivateIpAddress: str = None, ElasticGpuSpecification: List = None, TagSpecifications: List = None, LaunchTemplate: Dict = None, InstanceMarketOptions: Dict = None, CreditSpecification: Dict = None, CpuOptions: Dict = None, CapacityReservationSpecification: Dict = None) -> List['Instance']:
        pass

    def create_internet_gateway(self, DryRun: bool = None) -> 'InternetGateway':
        pass

    def create_key_pair(self, KeyName: str, DryRun: bool = None) -> 'KeyPair':
        pass

    def create_network_acl(self, VpcId: str, DryRun: bool = None) -> 'NetworkAcl':
        pass

    def create_network_interface(self, SubnetId: str, Description: str = None, DryRun: bool = None, Groups: List = None, Ipv6AddressCount: int = None, Ipv6Addresses: List = None, PrivateIpAddress: str = None, PrivateIpAddresses: List = None, SecondaryPrivateIpAddressCount: int = None) -> 'NetworkInterface':
        pass

    def create_placement_group(self, GroupName: str, Strategy: str, DryRun: bool = None) -> 'PlacementGroup':
        pass

    def create_route_table(self, VpcId: str, DryRun: bool = None) -> 'RouteTable':
        pass

    def create_security_group(self, Description: str, GroupName: str, VpcId: str = None, DryRun: bool = None) -> 'SecurityGroup':
        pass

    def create_snapshot(self, VolumeId: str, Description: str = None, TagSpecifications: List = None, DryRun: bool = None) -> 'Snapshot':
        pass

    def create_subnet(self, CidrBlock: str, VpcId: str, AvailabilityZone: str = None, Ipv6CidrBlock: str = None, DryRun: bool = None) -> 'Subnet':
        pass

    def create_tags(self, Resources: List[str], Tags: List, DryRun: bool = None):
        pass

    def create_volume(self, AvailabilityZone: str, Encrypted: bool = None, Iops: int = None, KmsKeyId: str = None, Size: int = None, SnapshotId: str = None, VolumeType: str = None, DryRun: bool = None, TagSpecifications: List = None) -> 'Volume':
        pass

    def create_vpc(self, CidrBlock: str, AmazonProvidedIpv6CidrBlock: bool = None, DryRun: bool = None, InstanceTenancy: str = None) -> 'Vpc':
        pass

    def create_vpc_peering_connection(self, DryRun: bool = None, PeerOwnerId: str = None, PeerVpcId: str = None, VpcId: str = None, PeerRegion: str = None) -> 'VpcPeeringConnection':
        pass

    def disassociate_route_table(self, AssociationId: str, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def import_key_pair(self, KeyName: str, PublicKeyMaterial: bytes, DryRun: bool = None) -> 'KeyPairInfo':
        pass

    def register_image(self, Name: str, ImageLocation: str = None, Architecture: str = None, BlockDeviceMappings: List = None, Description: str = None, DryRun: bool = None, EnaSupport: bool = None, KernelId: str = None, BillingProducts: List = None, RamdiskId: str = None, RootDeviceName: str = None, SriovNetSupport: str = None, VirtualizationType: str = None) -> 'Image':
        pass


class ClassicAddress(base.ServiceResource):
    instance_id: str
    allocation_id: str
    association_id: str
    domain: str
    network_interface_id: str
    network_interface_owner_id: str
    private_ip_address: str
    tags: List
    public_ipv4_pool: str
    public_ip: str

    def associate(self, AllocationId: str = None, InstanceId: str = None, AllowReassociation: bool = None, DryRun: bool = None, NetworkInterfaceId: str = None, PrivateIpAddress: str = None) -> Dict:
        pass

    def disassociate(self, AssociationId: str = None, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def release(self, AllocationId: str = None, DryRun: bool = None):
        pass

    def reload(self):
        pass


class DhcpOptions(base.ServiceResource):
    dhcp_configurations: List
    dhcp_options_id: str
    tags: List
    id: str

    def associate_with_vpc(self, VpcId: str, DryRun: bool = None):
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        pass

    def delete(self, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass


class Image(base.ServiceResource):
    architecture: str
    creation_date: str
    image_id: str
    image_location: str
    image_type: str
    public: bool
    kernel_id: str
    owner_id: str
    platform: str
    product_codes: List
    ramdisk_id: str
    state: str
    block_device_mappings: List
    description: str
    ena_support: bool
    hypervisor: str
    image_owner_alias: str
    name: str
    root_device_name: str
    root_device_type: str
    sriov_net_support: str
    state_reason: Dict
    tags: List
    virtualization_type: str
    id: str

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        pass

    def deregister(self, DryRun: bool = None):
        pass

    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict:
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def modify_attribute(self, Attribute: str = None, Description: Dict = None, LaunchPermission: Dict = None, OperationType: str = None, ProductCodes: List = None, UserGroups: List = None, UserIds: List = None, Value: str = None, DryRun: bool = None):
        pass

    def reload(self):
        pass

    def reset_attribute(self, Attribute: str, DryRun: bool = None):
        pass

    def wait_until_exists(self, ExecutableUsers: List = None, Filters: List = None, Owners: List = None, DryRun: bool = None):
        pass


class Instance(base.ServiceResource):
    ami_launch_index: int
    image_id: str
    instance_id: str
    instance_type: str
    kernel_id: str
    key_name: str
    launch_time: datetime
    monitoring: Dict
    placement: Dict
    platform: str
    private_dns_name: str
    private_ip_address: str
    product_codes: List
    public_dns_name: str
    public_ip_address: str
    ramdisk_id: str
    state: Dict
    state_transition_reason: str
    subnet_id: str
    vpc_id: str
    architecture: str
    block_device_mappings: List
    client_token: str
    ebs_optimized: bool
    ena_support: bool
    hypervisor: str
    iam_instance_profile: Dict
    instance_lifecycle: str
    elastic_gpu_associations: List
    network_interfaces_attribute: List
    root_device_name: str
    root_device_type: str
    security_groups: List
    source_dest_check: bool
    spot_instance_request_id: str
    sriov_net_support: str
    state_reason: Dict
    tags: List
    virtualization_type: str
    cpu_options: Dict
    capacity_reservation_id: str
    capacity_reservation_specification: Dict
    id: str
    volumes: 'volumes'
    vpc_addresses: 'vpc_addresses'

    def attach_classic_link_vpc(self, Groups: List, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    def attach_volume(self, Device: str, VolumeId: str, DryRun: bool = None) -> Dict:
        pass

    def console_output(self, DryRun: bool = None, Latest: bool = None) -> Dict:
        pass

    def create_image(self, Name: str, BlockDeviceMappings: List = None, Description: str = None, DryRun: bool = None, NoReboot: bool = None) -> 'Image':
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        pass

    def delete_tags(self, DryRun: bool = None, Tags: List = None):
        pass

    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict:
        pass

    def detach_classic_link_vpc(self, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    def detach_volume(self, VolumeId: str, Device: str = None, Force: bool = None, DryRun: bool = None) -> Dict:
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def modify_attribute(self, SourceDestCheck: Dict = None, Attribute: str = None, BlockDeviceMappings: List = None, DisableApiTermination: Dict = None, DryRun: bool = None, EbsOptimized: Dict = None, EnaSupport: Dict = None, Groups: List = None, InstanceInitiatedShutdownBehavior: Dict = None, InstanceType: Dict = None, Kernel: Dict = None, Ramdisk: Dict = None, SriovNetSupport: Dict = None, UserData: Dict = None, Value: str = None):
        pass

    def monitor(self, DryRun: bool = None) -> Dict:
        pass

    def password_data(self, DryRun: bool = None) -> Dict:
        pass

    def reboot(self, DryRun: bool = None):
        pass

    def reload(self):
        pass

    def report_status(self, ReasonCodes: List, Status: str, Description: str = None, DryRun: bool = None, EndTime: datetime = None, StartTime: datetime = None):
        pass

    def reset_attribute(self, Attribute: str, DryRun: bool = None):
        pass

    def reset_kernel(self, DryRun: bool = None):
        pass

    def reset_ramdisk(self, DryRun: bool = None):
        pass

    def reset_source_dest_check(self, DryRun: bool = None):
        pass

    def start(self, AdditionalInfo: str = None, DryRun: bool = None) -> Dict:
        pass

    def stop(self, DryRun: bool = None, Force: bool = None) -> Dict:
        pass

    def terminate(self, DryRun: bool = None) -> Dict:
        pass

    def unmonitor(self, DryRun: bool = None) -> Dict:
        pass

    def wait_until_exists(self, Filters: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None):
        pass

    def wait_until_running(self, Filters: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None):
        pass

    def wait_until_stopped(self, Filters: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None):
        pass

    def wait_until_terminated(self, Filters: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None):
        pass


class InternetGateway(base.ServiceResource):
    attachments: List
    internet_gateway_id: str
    tags: List
    id: str

    def attach_to_vpc(self, VpcId: str, DryRun: bool = None):
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        pass

    def delete(self, DryRun: bool = None):
        pass

    def detach_from_vpc(self, VpcId: str, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass


class KeyPair(base.ServiceResource):
    key_fingerprint: str
    key_material: str
    key_name: str
    name: str

    def delete(self, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass


class KeyPairInfo(base.ServiceResource):
    key_fingerprint: str
    key_name: str
    name: str

    def delete(self, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass


class NetworkAcl(base.ServiceResource):
    associations: List
    entries: List
    is_default: bool
    network_acl_id: str
    tags: List
    vpc_id: str
    id: str

    def create_entry(self, Egress: bool, Protocol: str, RuleAction: str, RuleNumber: int, CidrBlock: str = None, DryRun: bool = None, IcmpTypeCode: Dict = None, Ipv6CidrBlock: str = None, PortRange: Dict = None):
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        pass

    def delete(self, DryRun: bool = None):
        pass

    def delete_entry(self, Egress: bool, RuleNumber: int, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def replace_association(self, AssociationId: str, DryRun: bool = None) -> Dict:
        pass

    def replace_entry(self, Egress: bool, Protocol: str, RuleAction: str, RuleNumber: int, CidrBlock: str = None, DryRun: bool = None, IcmpTypeCode: Dict = None, Ipv6CidrBlock: str = None, PortRange: Dict = None):
        pass


class NetworkInterface(base.ServiceResource):
    association_attribute: Dict
    attachment: Dict
    availability_zone: str
    description: str
    groups: List
    interface_type: str
    ipv6_addresses: List
    mac_address: str
    network_interface_id: str
    owner_id: str
    private_dns_name: str
    private_ip_address: str
    private_ip_addresses: List
    requester_id: str
    requester_managed: bool
    source_dest_check: bool
    status: str
    subnet_id: str
    tag_set: List
    vpc_id: str
    id: str

    def assign_private_ip_addresses(self, AllowReassignment: bool = None, PrivateIpAddresses: List = None, SecondaryPrivateIpAddressCount: int = None):
        pass

    def attach(self, DeviceIndex: int, InstanceId: str, DryRun: bool = None) -> Dict:
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        pass

    def delete(self, DryRun: bool = None):
        pass

    def describe_attribute(self, Attribute: str = None, DryRun: bool = None) -> Dict:
        pass

    def detach(self, DryRun: bool = None, Force: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def modify_attribute(self, Attachment: Dict = None, Description: Dict = None, DryRun: bool = None, Groups: List = None, SourceDestCheck: Dict = None):
        pass

    def reload(self):
        pass

    def reset_attribute(self, DryRun: bool = None, SourceDestCheck: str = None):
        pass

    def unassign_private_ip_addresses(self, PrivateIpAddresses: List):
        pass


class NetworkInterfaceAssociation(base.ServiceResource):
    ip_owner_id: str
    public_dns_name: str
    public_ip: str
    id: str

    def delete(self, PublicIp: str = None, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass


class PlacementGroup(base.ServiceResource):
    group_name: str
    state: str
    strategy: str
    name: str
    instances: 'instances'

    def delete(self, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass


class Route(base.ServiceResource):
    destination_ipv6_cidr_block: str
    destination_prefix_list_id: str
    egress_only_internet_gateway_id: str
    gateway_id: str
    instance_id: str
    instance_owner_id: str
    nat_gateway_id: str
    network_interface_id: str
    origin: str
    state: str
    vpc_peering_connection_id: str
    route_table_id: str
    destination_cidr_block: str

    def delete(self, DestinationIpv6CidrBlock: str = None, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def replace(self, DestinationIpv6CidrBlock: str = None, DryRun: bool = None, EgressOnlyInternetGatewayId: str = None, GatewayId: str = None, InstanceId: str = None, NatGatewayId: str = None, NetworkInterfaceId: str = None, VpcPeeringConnectionId: str = None):
        pass


class RouteTable(base.ServiceResource):
    associations_attribute: List
    propagating_vgws: List
    route_table_id: str
    routes_attribute: List
    tags: List
    vpc_id: str
    id: str

    def associate_with_subnet(self, SubnetId: str, DryRun: bool = None) -> 'RouteTableAssociation':
        pass

    def create_route(self, DestinationCidrBlock: str = None, DestinationIpv6CidrBlock: str = None, DryRun: bool = None, EgressOnlyInternetGatewayId: str = None, GatewayId: str = None, InstanceId: str = None, NatGatewayId: str = None, NetworkInterfaceId: str = None, VpcPeeringConnectionId: str = None) -> 'Route':
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        pass

    def delete(self, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass


class RouteTableAssociation(base.ServiceResource):
    main: bool
    route_table_association_id: str
    route_table_id: str
    subnet_id: str
    id: str

    def delete(self, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def replace_subnet(self, RouteTableId: str, DryRun: bool = None) -> 'RouteTableAssociation':
        pass


class SecurityGroup(base.ServiceResource):
    description: str
    group_name: str
    ip_permissions: List
    owner_id: str
    group_id: str
    ip_permissions_egress: List
    tags: List
    vpc_id: str
    id: str

    def authorize_egress(self, DryRun: bool = None, IpPermissions: List = None, CidrIp: str = None, FromPort: int = None, IpProtocol: str = None, ToPort: int = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None):
        pass

    def authorize_ingress(self, CidrIp: str = None, FromPort: int = None, GroupName: str = None, IpPermissions: List = None, IpProtocol: str = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None, ToPort: int = None, DryRun: bool = None):
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        pass

    def delete(self, GroupName: str = None, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass

    def revoke_egress(self, DryRun: bool = None, IpPermissions: List = None, CidrIp: str = None, FromPort: int = None, IpProtocol: str = None, ToPort: int = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None):
        pass

    def revoke_ingress(self, CidrIp: str = None, FromPort: int = None, GroupName: str = None, IpPermissions: List = None, IpProtocol: str = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None, ToPort: int = None, DryRun: bool = None):
        pass


class Snapshot(base.ServiceResource):
    data_encryption_key_id: str
    description: str
    encrypted: bool
    kms_key_id: str
    owner_id: str
    progress: str
    snapshot_id: str
    start_time: datetime
    state: str
    state_message: str
    volume_id: str
    volume_size: int
    owner_alias: str
    tags: List
    id: str

    def copy(self, SourceRegion: str, Description: str = None, DestinationRegion: str = None, Encrypted: bool = None, KmsKeyId: str = None, PresignedUrl: str = None, DryRun: bool = None) -> Dict:
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        pass

    def delete(self, DryRun: bool = None):
        pass

    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict:
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def modify_attribute(self, Attribute: str = None, CreateVolumePermission: Dict = None, GroupNames: List = None, OperationType: str = None, UserIds: List = None, DryRun: bool = None):
        pass

    def reload(self):
        pass

    def reset_attribute(self, Attribute: str, DryRun: bool = None):
        pass

    def wait_until_completed(self, Filters: List = None, MaxResults: int = None, NextToken: str = None, OwnerIds: List = None, RestorableByUserIds: List = None, DryRun: bool = None):
        pass


class Subnet(base.ServiceResource):
    availability_zone: str
    available_ip_address_count: int
    cidr_block: str
    default_for_az: bool
    map_public_ip_on_launch: bool
    state: str
    subnet_id: str
    vpc_id: str
    assign_ipv6_address_on_creation: bool
    ipv6_cidr_block_association_set: List
    tags: List
    id: str
    instances: 'instances'
    network_interfaces: 'network_interfaces'

    def create_instances(self, MaxCount: int, MinCount: int, BlockDeviceMappings: List = None, ImageId: str = None, InstanceType: str = None, Ipv6AddressCount: int = None, Ipv6Addresses: List = None, KernelId: str = None, KeyName: str = None, Monitoring: Dict = None, Placement: Dict = None, RamdiskId: str = None, SecurityGroupIds: List = None, SecurityGroups: List = None, UserData: str = None, AdditionalInfo: str = None, ClientToken: str = None, DisableApiTermination: bool = None, DryRun: bool = None, EbsOptimized: bool = None, IamInstanceProfile: Dict = None, InstanceInitiatedShutdownBehavior: str = None, NetworkInterfaces: List = None, PrivateIpAddress: str = None, ElasticGpuSpecification: List = None, TagSpecifications: List = None, LaunchTemplate: Dict = None, InstanceMarketOptions: Dict = None, CreditSpecification: Dict = None, CpuOptions: Dict = None, CapacityReservationSpecification: Dict = None) -> List['Instance']:
        pass

    def create_network_interface(self, Description: str = None, DryRun: bool = None, Groups: List = None, Ipv6AddressCount: int = None, Ipv6Addresses: List = None, PrivateIpAddress: str = None, PrivateIpAddresses: List = None, SecondaryPrivateIpAddressCount: int = None) -> 'NetworkInterface':
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        pass

    def delete(self, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass


class Tag(base.ServiceResource):
    resource_type: str
    resource_id: str
    key: str
    value: str

    def delete(self, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reload(self):
        pass


class Volume(base.ServiceResource):
    attachments: List
    availability_zone: str
    create_time: datetime
    encrypted: bool
    kms_key_id: str
    size: int
    snapshot_id: str
    state: str
    volume_id: str
    iops: int
    tags: List
    volume_type: str
    id: str
    snapshots: 'snapshots'

    def attach_to_instance(self, Device: str, InstanceId: str, DryRun: bool = None) -> Dict:
        pass

    def create_snapshot(self, Description: str = None, TagSpecifications: List = None, DryRun: bool = None) -> 'Snapshot':
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        pass

    def delete(self, DryRun: bool = None):
        pass

    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict:
        pass

    def describe_status(self, Filters: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None) -> Dict:
        pass

    def detach_from_instance(self, Device: str = None, Force: bool = None, InstanceId: str = None, DryRun: bool = None) -> Dict:
        pass

    def enable_io(self, DryRun: bool = None):
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def modify_attribute(self, AutoEnableIO: Dict = None, DryRun: bool = None):
        pass

    def reload(self):
        pass


class Vpc(base.ServiceResource):
    cidr_block: str
    dhcp_options_id: str
    state: str
    vpc_id: str
    instance_tenancy: str
    ipv6_cidr_block_association_set: List
    cidr_block_association_set: List
    is_default: bool
    tags: List
    id: str
    accepted_vpc_peering_connections: 'accepted_vpc_peering_connections'
    instances: 'instances'
    internet_gateways: 'internet_gateways'
    network_acls: 'network_acls'
    network_interfaces: 'network_interfaces'
    requested_vpc_peering_connections: 'requested_vpc_peering_connections'
    route_tables: 'route_tables'
    security_groups: 'security_groups'
    subnets: 'subnets'

    def associate_dhcp_options(self, DhcpOptionsId: str, DryRun: bool = None):
        pass

    def attach_classic_link_instance(self, Groups: List, InstanceId: str, DryRun: bool = None) -> Dict:
        pass

    def attach_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None):
        pass

    def create_network_acl(self, DryRun: bool = None) -> 'NetworkAcl':
        pass

    def create_route_table(self, DryRun: bool = None) -> 'RouteTable':
        pass

    def create_security_group(self, Description: str, GroupName: str, DryRun: bool = None) -> 'SecurityGroup':
        pass

    def create_subnet(self, CidrBlock: str, AvailabilityZone: str = None, Ipv6CidrBlock: str = None, DryRun: bool = None) -> 'Subnet':
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        pass

    def delete(self, DryRun: bool = None):
        pass

    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict:
        pass

    def detach_classic_link_instance(self, InstanceId: str, DryRun: bool = None) -> Dict:
        pass

    def detach_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None):
        pass

    def disable_classic_link(self, DryRun: bool = None) -> Dict:
        pass

    def enable_classic_link(self, DryRun: bool = None) -> Dict:
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def modify_attribute(self, EnableDnsHostnames: Dict = None, EnableDnsSupport: Dict = None):
        pass

    def reload(self):
        pass

    def request_vpc_peering_connection(self, DryRun: bool = None, PeerOwnerId: str = None, PeerVpcId: str = None, PeerRegion: str = None) -> 'VpcPeeringConnection':
        pass

    def wait_until_available(self, Filters: List = None, DryRun: bool = None):
        pass

    def wait_until_exists(self, Filters: List = None, DryRun: bool = None):
        pass


class VpcPeeringConnection(base.ServiceResource):
    accepter_vpc_info: Dict
    expiration_time: datetime
    requester_vpc_info: Dict
    status: Dict
    tags: List
    vpc_peering_connection_id: str
    id: str

    def accept(self, DryRun: bool = None) -> Dict:
        pass

    def delete(self, DryRun: bool = None) -> Dict:
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def reject(self, DryRun: bool = None) -> Dict:
        pass

    def reload(self):
        pass

    def wait_until_exists(self, Filters: List = None, DryRun: bool = None):
        pass


class VpcAddress(base.ServiceResource):
    instance_id: str
    public_ip: str
    association_id: str
    domain: str
    network_interface_id: str
    network_interface_owner_id: str
    private_ip_address: str
    tags: List
    public_ipv4_pool: str
    allocation_id: str

    def associate(self, InstanceId: str = None, PublicIp: str = None, AllowReassociation: bool = None, DryRun: bool = None, NetworkInterfaceId: str = None, PrivateIpAddress: str = None) -> Dict:
        pass

    def get_available_subresources(self) -> List[str]:
        pass

    def load(self):
        pass

    def release(self, PublicIp: str = None, DryRun: bool = None):
        pass

    def reload(self):
        pass


class classic_addresses(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['ClassicAddress']:
        pass

    
    @classmethod
    def filter(cls, PublicIps: List = None, AllocationIds: List = None, DryRun: bool = None) -> List['ClassicAddress']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['ClassicAddress']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['ClassicAddress']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class dhcp_options_sets(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['DhcpOptions']:
        pass

    
    @classmethod
    def filter(cls, DhcpOptionsIds: List = None, Filters: List = None, DryRun: bool = None) -> List['DhcpOptions']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['DhcpOptions']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['DhcpOptions']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class images(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Image']:
        pass

    
    @classmethod
    def filter(cls, ExecutableUsers: List = None, Filters: List = None, ImageIds: List = None, Owners: List = None, DryRun: bool = None) -> List['Image']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Image']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Image']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class instances(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Instance']:
        pass

    
    @classmethod
    def create_tags(cls, Tags: List, DryRun: bool = None):
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None) -> List['Instance']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Instance']:
        pass

    
    @classmethod
    def monitor(cls, DryRun: bool = None) -> Dict:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Instance']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass

    
    @classmethod
    def reboot(cls, DryRun: bool = None):
        pass

    
    @classmethod
    def start(cls, AdditionalInfo: str = None, DryRun: bool = None) -> Dict:
        pass

    
    @classmethod
    def stop(cls, DryRun: bool = None, Force: bool = None) -> Dict:
        pass

    
    @classmethod
    def terminate(cls, DryRun: bool = None) -> Dict:
        pass

    
    @classmethod
    def unmonitor(cls, DryRun: bool = None) -> Dict:
        pass


class internet_gateways(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['InternetGateway']:
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, DryRun: bool = None, InternetGatewayIds: List = None) -> List['InternetGateway']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['InternetGateway']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['InternetGateway']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class key_pairs(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['KeyPairInfo']:
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, KeyNames: List = None, DryRun: bool = None) -> List['KeyPairInfo']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['KeyPairInfo']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['KeyPairInfo']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class network_acls(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['NetworkAcl']:
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, DryRun: bool = None, NetworkAclIds: List = None) -> List['NetworkAcl']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['NetworkAcl']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['NetworkAcl']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class network_interfaces(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['NetworkInterface']:
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, DryRun: bool = None, NetworkInterfaceIds: List = None, NextToken: str = None, MaxResults: int = None) -> List['NetworkInterface']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['NetworkInterface']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['NetworkInterface']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class placement_groups(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['PlacementGroup']:
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, DryRun: bool = None, GroupNames: List = None) -> List['PlacementGroup']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['PlacementGroup']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['PlacementGroup']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class route_tables(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['RouteTable']:
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, DryRun: bool = None, RouteTableIds: List = None, NextToken: str = None, MaxResults: int = None) -> List['RouteTable']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['RouteTable']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['RouteTable']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class security_groups(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['SecurityGroup']:
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, GroupIds: List = None, GroupNames: List = None, DryRun: bool = None, NextToken: str = None, MaxResults: int = None) -> List['SecurityGroup']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['SecurityGroup']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['SecurityGroup']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class snapshots(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Snapshot']:
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, MaxResults: int = None, NextToken: str = None, OwnerIds: List = None, RestorableByUserIds: List = None, SnapshotIds: List = None, DryRun: bool = None) -> List['Snapshot']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Snapshot']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Snapshot']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class subnets(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Subnet']:
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, SubnetIds: List = None, DryRun: bool = None) -> List['Subnet']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Subnet']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Subnet']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class volumes(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Volume']:
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None) -> List['Volume']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Volume']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Volume']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class vpc_addresses(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['VpcAddress']:
        pass

    
    @classmethod
    def filter(cls, PublicIps: List = None, AllocationIds: List = None, DryRun: bool = None) -> List['VpcAddress']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['VpcAddress']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['VpcAddress']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class vpc_peering_connections(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['VpcPeeringConnection']:
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None) -> List['VpcPeeringConnection']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['VpcPeeringConnection']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['VpcPeeringConnection']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass


class vpcs(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Vpc']:
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, VpcIds: List = None, DryRun: bool = None) -> List['Vpc']:
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Vpc']:
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Vpc']:
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        pass
