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
        """
        Creates a ClassicAddress resource.::
        
          classic_address = ec2.ClassicAddress(\'public_ip\')
        
        :type public_ip: string
        :param public_ip: The ClassicAddress\'s public_ip identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.ClassicAddress`
        :returns: A ClassicAddress resource
        """
        pass

    def DhcpOptions(self, id: str = None) -> 'DhcpOptions':
        """
        Creates a DhcpOptions resource.::
        
          dhcp_options = ec2.DhcpOptions(\'id\')
        
        :type id: string
        :param id: The DhcpOptions\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.DhcpOptions`
        :returns: A DhcpOptions resource
        """
        pass

    def Image(self, id: str = None) -> 'Image':
        """
        Creates a Image resource.::
        
          image = ec2.Image(\'id\')
        
        :type id: string
        :param id: The Image\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.Image`
        :returns: A Image resource
        """
        pass

    def Instance(self, id: str = None) -> 'Instance':
        """
        Creates a Instance resource.::
        
          instance = ec2.Instance(\'id\')
        
        :type id: string
        :param id: The Instance\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.Instance`
        :returns: A Instance resource
        """
        pass

    def InternetGateway(self, id: str = None) -> 'InternetGateway':
        """
        Creates a InternetGateway resource.::
        
          internet_gateway = ec2.InternetGateway(\'id\')
        
        :type id: string
        :param id: The InternetGateway\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.InternetGateway`
        :returns: A InternetGateway resource
        """
        pass

    def KeyPair(self, name: str = None) -> 'KeyPairInfo':
        """
        Creates a KeyPairInfo resource.::
        
          key_pair_info = ec2.KeyPair(\'name\')
        
        :type name: string
        :param name: The KeyPair\'s name identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.KeyPairInfo`
        :returns: A KeyPairInfo resource
        """
        pass

    def NetworkAcl(self, id: str = None) -> 'NetworkAcl':
        """
        Creates a NetworkAcl resource.::
        
          network_acl = ec2.NetworkAcl(\'id\')
        
        :type id: string
        :param id: The NetworkAcl\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.NetworkAcl`
        :returns: A NetworkAcl resource
        """
        pass

    def NetworkInterface(self, id: str = None) -> 'NetworkInterface':
        """
        Creates a NetworkInterface resource.::
        
          network_interface = ec2.NetworkInterface(\'id\')
        
        :type id: string
        :param id: The NetworkInterface\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.NetworkInterface`
        :returns: A NetworkInterface resource
        """
        pass

    def NetworkInterfaceAssociation(self, id: str = None) -> 'NetworkInterfaceAssociation':
        """
        Creates a NetworkInterfaceAssociation resource.::
        
          network_interface_association = ec2.NetworkInterfaceAssociation(\'id\')
        
        :type id: string
        :param id: The NetworkInterfaceAssociation\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.NetworkInterfaceAssociation`
        :returns: A NetworkInterfaceAssociation resource
        """
        pass

    def PlacementGroup(self, name: str = None) -> 'PlacementGroup':
        """
        Creates a PlacementGroup resource.::
        
          placement_group = ec2.PlacementGroup(\'name\')
        
        :type name: string
        :param name: The PlacementGroup\'s name identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.PlacementGroup`
        :returns: A PlacementGroup resource
        """
        pass

    def Route(self, route_table_id: str = None, destination_cidr_block: str = None) -> 'Route':
        """
        Creates a Route resource.::
        
          route = ec2.Route(\'route_table_id\',\'destination_cidr_block\')
        
        :type route_table_id: string
        :param route_table_id: The Route\'s route_table_id identifier. This **must** be set.
        :type destination_cidr_block: string
        :param destination_cidr_block: The Route\'s destination_cidr_block identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.Route`
        :returns: A Route resource
        """
        pass

    def RouteTable(self, id: str = None) -> 'RouteTable':
        """
        Creates a RouteTable resource.::
        
          route_table = ec2.RouteTable(\'id\')
        
        :type id: string
        :param id: The RouteTable\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.RouteTable`
        :returns: A RouteTable resource
        """
        pass

    def RouteTableAssociation(self, id: str = None) -> 'RouteTableAssociation':
        """
        Creates a RouteTableAssociation resource.::
        
          route_table_association = ec2.RouteTableAssociation(\'id\')
        
        :type id: string
        :param id: The RouteTableAssociation\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.RouteTableAssociation`
        :returns: A RouteTableAssociation resource
        """
        pass

    def SecurityGroup(self, id: str = None) -> 'SecurityGroup':
        """
        Creates a SecurityGroup resource.::
        
          security_group = ec2.SecurityGroup(\'id\')
        
        :type id: string
        :param id: The SecurityGroup\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.SecurityGroup`
        :returns: A SecurityGroup resource
        """
        pass

    def Snapshot(self, id: str = None) -> 'Snapshot':
        """
        Creates a Snapshot resource.::
        
          snapshot = ec2.Snapshot(\'id\')
        
        :type id: string
        :param id: The Snapshot\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.Snapshot`
        :returns: A Snapshot resource
        """
        pass

    def Subnet(self, id: str = None) -> 'Subnet':
        """
        Creates a Subnet resource.::
        
          subnet = ec2.Subnet(\'id\')
        
        :type id: string
        :param id: The Subnet\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.Subnet`
        :returns: A Subnet resource
        """
        pass

    def Tag(self, resource_id: str = None, key: str = None, value: str = None) -> 'Tag':
        """
        Creates a Tag resource.::
        
          tag = ec2.Tag(\'resource_id\',\'key\',\'value\')
        
        :type resource_id: string
        :param resource_id: The Tag\'s resource_id identifier. This **must** be set.
        :type key: string
        :param key: The Tag\'s key identifier. This **must** be set.
        :type value: string
        :param value: The Tag\'s value identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.Tag`
        :returns: A Tag resource
        """
        pass

    def Volume(self, id: str = None) -> 'Volume':
        """
        Creates a Volume resource.::
        
          volume = ec2.Volume(\'id\')
        
        :type id: string
        :param id: The Volume\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.Volume`
        :returns: A Volume resource
        """
        pass

    def Vpc(self, id: str = None) -> 'Vpc':
        """
        Creates a Vpc resource.::
        
          vpc = ec2.Vpc(\'id\')
        
        :type id: string
        :param id: The Vpc\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.Vpc`
        :returns: A Vpc resource
        """
        pass

    def VpcAddress(self, allocation_id: str = None) -> 'VpcAddress':
        """
        Creates a VpcAddress resource.::
        
          vpc_address = ec2.VpcAddress(\'allocation_id\')
        
        :type allocation_id: string
        :param allocation_id: The VpcAddress\'s allocation_id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.VpcAddress`
        :returns: A VpcAddress resource
        """
        pass

    def VpcPeeringConnection(self, id: str = None) -> 'VpcPeeringConnection':
        """
        Creates a VpcPeeringConnection resource.::
        
          vpc_peering_connection = ec2.VpcPeeringConnection(\'id\')
        
        :type id: string
        :param id: The VpcPeeringConnection\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`EC2.VpcPeeringConnection`
        :returns: A VpcPeeringConnection resource
        """
        pass

    def create_dhcp_options(self, DhcpConfigurations: List, DryRun: bool = None) -> 'DhcpOptions':
        """
        
        * ``domain-name-servers`` - The IP addresses of up to four domain name servers, or AmazonProvidedDNS. The default DHCP option set specifies AmazonProvidedDNS. If specifying more than one domain name server, specify the IP addresses in a single parameter, separated by commas. ITo have your instance to receive a custom DNS hostname as specified in ``domain-name`` , you must set ``domain-name-servers`` to a custom DNS server. 
         
        * ``domain-name`` - If you\'re using AmazonProvidedDNS in ``us-east-1`` , specify ``ec2.internal`` . If you\'re using AmazonProvidedDNS in another region, specify ``region.compute.internal`` (for example, ``ap-northeast-1.compute.internal`` ). Otherwise, specify a domain name (for example, ``MyCompany.com`` ). This value is used to complete unqualified DNS hostnames. **Important** : Some Linux operating systems accept multiple domain names separated by spaces. However, Windows and other Linux operating systems treat the value as a single domain, which results in unexpected behavior. If your DHCP options set is associated with a VPC that has instances with multiple operating systems, specify only one domain name. 
         
        * ``ntp-servers`` - The IP addresses of up to four Network Time Protocol (NTP) servers. 
         
        * ``netbios-name-servers`` - The IP addresses of up to four NetBIOS name servers. 
         
        * ``netbios-node-type`` - The NetBIOS node type (1, 2, 4, or 8). We recommend that you specify 2 (broadcast and multicast are not currently supported). For more information about these node types, see `RFC 2132 <http://www.ietf.org/rfc/rfc2132.txt>`__ . 
         
        Your VPC automatically starts out with a set of DHCP options that includes only a DNS server that we provide (AmazonProvidedDNS). If you create a set of options, and if your VPC has an internet gateway, make sure to set the ``domain-name-servers`` option either to ``AmazonProvidedDNS`` or to a domain name server of your choice. For more information, see `DHCP Options Sets <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateDhcpOptions>`_
        
        **Request Syntax** 
        ::
        
          dhcp_options = ec2.create_dhcp_options(
              DhcpConfigurations=[
                  {
                      \'Key\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False
          )
        :type DhcpConfigurations: list
        :param DhcpConfigurations: **[REQUIRED]** 
        
          A DHCP configuration option.
        
          - *(dict) --* 
        
            - **Key** *(string) --* 
        
            - **Values** *(list) --* 
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: :py:class:`ec2.DhcpOptions`
        :returns: DhcpOptions resource
        """
        pass

    def create_instances(self, MaxCount: int, MinCount: int, BlockDeviceMappings: List = None, ImageId: str = None, InstanceType: str = None, Ipv6AddressCount: int = None, Ipv6Addresses: List = None, KernelId: str = None, KeyName: str = None, Monitoring: Dict = None, Placement: Dict = None, RamdiskId: str = None, SecurityGroupIds: List = None, SecurityGroups: List = None, SubnetId: str = None, UserData: str = None, AdditionalInfo: str = None, ClientToken: str = None, DisableApiTermination: bool = None, DryRun: bool = None, EbsOptimized: bool = None, IamInstanceProfile: Dict = None, InstanceInitiatedShutdownBehavior: str = None, NetworkInterfaces: List = None, PrivateIpAddress: str = None, ElasticGpuSpecification: List = None, TagSpecifications: List = None, LaunchTemplate: Dict = None, InstanceMarketOptions: Dict = None, CreditSpecification: Dict = None, CpuOptions: Dict = None, CapacityReservationSpecification: Dict = None) -> List['Instance']:
        """
        
        You can specify a number of options, or leave the default options. The following rules apply:
        
        * [EC2-VPC] If you don\'t specify a subnet ID, we choose a default subnet from your default VPC for you. If you don\'t have a default VPC, you must specify a subnet ID in the request. 
         
        * [EC2-Classic] If don\'t specify an Availability Zone, we choose one for you. 
         
        * Some instance types must be launched into a VPC. If you do not have a default VPC, or if you do not specify a subnet ID, the request fails. For more information, see `Instance Types Available Only in a VPC <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-vpc.html#vpc-only-instance-types>`__ . 
         
        * [EC2-VPC] All instances have a network interface with a primary private IPv4 address. If you don\'t specify this address, we choose one from the IPv4 range of your subnet. 
         
        * Not all instance types support IPv6 addresses. For more information, see `Instance Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`__ . 
         
        * If you don\'t specify a security group ID, we use the default security group. For more information, see `Security Groups <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html>`__ . 
         
        * If any of the AMIs have a product code attached for which the user has not subscribed, the request fails. 
         
        You can create a `launch template <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html>`__ , which is a resource that contains the parameters to launch an instance. When you launch an instance using  RunInstances , you can specify the launch template instead of specifying the launch parameters.
        
        To ensure faster instance launches, break up large requests into smaller batches. For example, create five separate launch requests for 100 instances each instead of one launch request for 500 instances.
        
        An instance is ready for you to use when it\'s in the ``running`` state. You can check the state of your instance using  DescribeInstances . You can tag instances and EBS volumes during launch, after launch, or both. For more information, see  CreateTags and `Tagging Your Amazon EC2 Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ .
        
        Linux instances have access to the public key of the key pair at boot. You can use this key to provide secure access to the instance. Amazon EC2 public images use this feature to provide secure access without passwords. For more information, see `Key Pairs <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        For troubleshooting, see `What To Do If An Instance Immediately Terminates <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_InstanceStraightToTerminated.html>`__ , and `Troubleshooting Connecting to Your Instance <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/RunInstances>`_
        
        **Request Syntax** 
        ::
        
          instance = ec2.create_instances(
              BlockDeviceMappings=[
                  {
                      \'DeviceName\': \'string\',
                      \'VirtualName\': \'string\',
                      \'Ebs\': {
                          \'DeleteOnTermination\': True|False,
                          \'Iops\': 123,
                          \'SnapshotId\': \'string\',
                          \'VolumeSize\': 123,
                          \'VolumeType\': \'standard\'|\'io1\'|\'gp2\'|\'sc1\'|\'st1\',
                          \'Encrypted\': True|False,
                          \'KmsKeyId\': \'string\'
                      },
                      \'NoDevice\': \'string\'
                  },
              ],
              ImageId=\'string\',
              InstanceType=\'t1.micro\'|\'t2.nano\'|\'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'t2.xlarge\'|\'t2.2xlarge\'|\'t3.nano\'|\'t3.micro\'|\'t3.small\'|\'t3.medium\'|\'t3.large\'|\'t3.xlarge\'|\'t3.2xlarge\'|\'m1.small\'|\'m1.medium\'|\'m1.large\'|\'m1.xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\'|\'m4.16xlarge\'|\'m2.xlarge\'|\'m2.2xlarge\'|\'m2.4xlarge\'|\'cr1.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'r5.large\'|\'r5.xlarge\'|\'r5.2xlarge\'|\'r5.4xlarge\'|\'r5.8xlarge\'|\'r5.12xlarge\'|\'r5.16xlarge\'|\'r5.24xlarge\'|\'r5.metal\'|\'r5a.large\'|\'r5a.xlarge\'|\'r5a.2xlarge\'|\'r5a.4xlarge\'|\'r5a.12xlarge\'|\'r5a.24xlarge\'|\'r5d.large\'|\'r5d.xlarge\'|\'r5d.2xlarge\'|\'r5d.4xlarge\'|\'r5d.8xlarge\'|\'r5d.12xlarge\'|\'r5d.16xlarge\'|\'r5d.24xlarge\'|\'r5d.metal\'|\'x1.16xlarge\'|\'x1.32xlarge\'|\'x1e.xlarge\'|\'x1e.2xlarge\'|\'x1e.4xlarge\'|\'x1e.8xlarge\'|\'x1e.16xlarge\'|\'x1e.32xlarge\'|\'i2.xlarge\'|\'i2.2xlarge\'|\'i2.4xlarge\'|\'i2.8xlarge\'|\'i3.large\'|\'i3.xlarge\'|\'i3.2xlarge\'|\'i3.4xlarge\'|\'i3.8xlarge\'|\'i3.16xlarge\'|\'i3.metal\'|\'hi1.4xlarge\'|\'hs1.8xlarge\'|\'c1.medium\'|\'c1.xlarge\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'c5.large\'|\'c5.xlarge\'|\'c5.2xlarge\'|\'c5.4xlarge\'|\'c5.9xlarge\'|\'c5.18xlarge\'|\'c5d.large\'|\'c5d.xlarge\'|\'c5d.2xlarge\'|\'c5d.4xlarge\'|\'c5d.9xlarge\'|\'c5d.18xlarge\'|\'cc1.4xlarge\'|\'cc2.8xlarge\'|\'g2.2xlarge\'|\'g2.8xlarge\'|\'g3.4xlarge\'|\'g3.8xlarge\'|\'g3.16xlarge\'|\'g3s.xlarge\'|\'cg1.4xlarge\'|\'p2.xlarge\'|\'p2.8xlarge\'|\'p2.16xlarge\'|\'p3.2xlarge\'|\'p3.8xlarge\'|\'p3.16xlarge\'|\'d2.xlarge\'|\'d2.2xlarge\'|\'d2.4xlarge\'|\'d2.8xlarge\'|\'f1.2xlarge\'|\'f1.4xlarge\'|\'f1.16xlarge\'|\'m5.large\'|\'m5.xlarge\'|\'m5.2xlarge\'|\'m5.4xlarge\'|\'m5.12xlarge\'|\'m5.24xlarge\'|\'m5a.large\'|\'m5a.xlarge\'|\'m5a.2xlarge\'|\'m5a.4xlarge\'|\'m5a.12xlarge\'|\'m5a.24xlarge\'|\'m5d.large\'|\'m5d.xlarge\'|\'m5d.2xlarge\'|\'m5d.4xlarge\'|\'m5d.12xlarge\'|\'m5d.24xlarge\'|\'h1.2xlarge\'|\'h1.4xlarge\'|\'h1.8xlarge\'|\'h1.16xlarge\'|\'z1d.large\'|\'z1d.xlarge\'|\'z1d.2xlarge\'|\'z1d.3xlarge\'|\'z1d.6xlarge\'|\'z1d.12xlarge\'|\'u-6tb1.metal\'|\'u-9tb1.metal\'|\'u-12tb1.metal\',
              Ipv6AddressCount=123,
              Ipv6Addresses=[
                  {
                      \'Ipv6Address\': \'string\'
                  },
              ],
              KernelId=\'string\',
              KeyName=\'string\',
              MaxCount=123,
              MinCount=123,
              Monitoring={
                  \'Enabled\': True|False
              },
              Placement={
                  \'AvailabilityZone\': \'string\',
                  \'Affinity\': \'string\',
                  \'GroupName\': \'string\',
                  \'HostId\': \'string\',
                  \'Tenancy\': \'default\'|\'dedicated\'|\'host\',
                  \'SpreadDomain\': \'string\'
              },
              RamdiskId=\'string\',
              SecurityGroupIds=[
                  \'string\',
              ],
              SecurityGroups=[
                  \'string\',
              ],
              SubnetId=\'string\',
              UserData=\'string\',
              AdditionalInfo=\'string\',
              ClientToken=\'string\',
              DisableApiTermination=True|False,
              DryRun=True|False,
              EbsOptimized=True|False,
              IamInstanceProfile={
                  \'Arn\': \'string\',
                  \'Name\': \'string\'
              },
              InstanceInitiatedShutdownBehavior=\'stop\'|\'terminate\',
              NetworkInterfaces=[
                  {
                      \'AssociatePublicIpAddress\': True|False,
                      \'DeleteOnTermination\': True|False,
                      \'Description\': \'string\',
                      \'DeviceIndex\': 123,
                      \'Groups\': [
                          \'string\',
                      ],
                      \'Ipv6AddressCount\': 123,
                      \'Ipv6Addresses\': [
                          {
                              \'Ipv6Address\': \'string\'
                          },
                      ],
                      \'NetworkInterfaceId\': \'string\',
                      \'PrivateIpAddress\': \'string\',
                      \'PrivateIpAddresses\': [
                          {
                              \'Primary\': True|False,
                              \'PrivateIpAddress\': \'string\'
                          },
                      ],
                      \'SecondaryPrivateIpAddressCount\': 123,
                      \'SubnetId\': \'string\'
                  },
              ],
              PrivateIpAddress=\'string\',
              ElasticGpuSpecification=[
                  {
                      \'Type\': \'string\'
                  },
              ],
              TagSpecifications=[
                  {
                      \'ResourceType\': \'customer-gateway\'|\'dedicated-host\'|\'dhcp-options\'|\'image\'|\'instance\'|\'internet-gateway\'|\'network-acl\'|\'network-interface\'|\'reserved-instances\'|\'route-table\'|\'snapshot\'|\'spot-instances-request\'|\'subnet\'|\'security-group\'|\'volume\'|\'vpc\'|\'vpn-connection\'|\'vpn-gateway\',
                      \'Tags\': [
                          {
                              \'Key\': \'string\',
                              \'Value\': \'string\'
                          },
                      ]
                  },
              ],
              LaunchTemplate={
                  \'LaunchTemplateId\': \'string\',
                  \'LaunchTemplateName\': \'string\',
                  \'Version\': \'string\'
              },
              InstanceMarketOptions={
                  \'MarketType\': \'spot\',
                  \'SpotOptions\': {
                      \'MaxPrice\': \'string\',
                      \'SpotInstanceType\': \'one-time\'|\'persistent\',
                      \'BlockDurationMinutes\': 123,
                      \'ValidUntil\': datetime(2015, 1, 1),
                      \'InstanceInterruptionBehavior\': \'hibernate\'|\'stop\'|\'terminate\'
                  }
              },
              CreditSpecification={
                  \'CpuCredits\': \'string\'
              },
              CpuOptions={
                  \'CoreCount\': 123,
                  \'ThreadsPerCore\': 123
              },
              CapacityReservationSpecification={
                  \'CapacityReservationPreference\': \'open\'|\'none\',
                  \'CapacityReservationTarget\': {
                      \'CapacityReservationId\': \'string\'
                  }
              }
          )
        :type BlockDeviceMappings: list
        :param BlockDeviceMappings: 
        
          One or more block device mapping entries. You can\'t specify both a snapshot ID and an encryption value. This is because only blank volumes can be encrypted on creation. If a snapshot is the basis for a volume, it is not blank and its encryption status is used for the volume encryption status.
        
          - *(dict) --* 
        
            Describes a block device mapping.
        
            - **DeviceName** *(string) --* 
        
              The device name (for example, ``/dev/sdh`` or ``xvdh`` ).
        
            - **VirtualName** *(string) --* 
        
              The virtual device name (``ephemeral`` N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ``ephemeral0`` and ``ephemeral1`` . The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
        
              NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect.
        
              Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
        
            - **Ebs** *(dict) --* 
        
              Parameters used to automatically set up EBS volumes when the instance is launched.
        
              - **DeleteOnTermination** *(boolean) --* 
        
                Indicates whether the EBS volume is deleted on instance termination.
        
              - **Iops** *(integer) --* 
        
                The number of I/O operations per second (IOPS) that the volume supports. For ``io1`` , this represents the number of IOPS that are provisioned for the volume. For ``gp2`` , this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see `Amazon EBS Volume Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
                Constraint: Range is 100-20000 IOPS for ``io1`` volumes and 100-10000 IOPS for ``gp2`` volumes.
        
                Condition: This parameter is required for requests to create ``io1`` volumes; it is not used in requests to create ``gp2`` , ``st1`` , ``sc1`` , or ``standard`` volumes.
        
              - **SnapshotId** *(string) --* 
        
                The ID of the snapshot.
        
              - **VolumeSize** *(integer) --* 
        
                The size of the volume, in GiB.
        
                Constraints: 1-16384 for General Purpose SSD (``gp2`` ), 4-16384 for Provisioned IOPS SSD (``io1`` ), 500-16384 for Throughput Optimized HDD (``st1`` ), 500-16384 for Cold HDD (``sc1`` ), and 1-1024 for Magnetic (``standard`` ) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
        
                Default: If you\'re creating the volume from a snapshot and don\'t specify a volume size, the default is the snapshot size.
        
              - **VolumeType** *(string) --* 
        
                The volume type: ``gp2`` , ``io1`` , ``st1`` , ``sc1`` , or ``standard`` .
        
                Default: ``standard``  
        
              - **Encrypted** *(boolean) --* 
        
                Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. 
        
                If you are creating a volume from a snapshot, you cannot specify an encryption value. This is because only blank volumes can be encrypted on creation. If you are creating a snapshot from an existing EBS volume, you cannot specify an encryption value that differs from that of the EBS volume. We recommend that you omit the encryption value from the block device mappings when creating an image from an instance.
        
              - **KmsKeyId** *(string) --* 
        
                Identifier (key ID, key alias, ID ARN, or alias ARN) for a user-managed CMK under which the EBS volume is encrypted.
        
                This parameter is only supported on ``BlockDeviceMapping`` objects called by `RunInstances <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html>`__ , `RequestSpotFleet <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet.html>`__ , and `RequestSpotInstances <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html>`__ .
        
            - **NoDevice** *(string) --* 
        
              Suppresses the specified device included in the block device mapping of the AMI.
        
        :type ImageId: string
        :param ImageId: 
        
          The ID of the AMI, which you can get by calling  DescribeImages . An AMI is required to launch an instance and must be specified here or in a launch template.
        
        :type InstanceType: string
        :param InstanceType: 
        
          The instance type. For more information, see `Instance Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
          Default: ``m1.small``  
        
        :type Ipv6AddressCount: integer
        :param Ipv6AddressCount: 
        
          [EC2-VPC] A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you\'ve specified a minimum number of instances to launch.
        
        :type Ipv6Addresses: list
        :param Ipv6Addresses: 
        
          [EC2-VPC] Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you\'ve specified a minimum number of instances to launch.
        
          - *(dict) --* 
        
            Describes an IPv6 address.
        
            - **Ipv6Address** *(string) --* 
        
              The IPv6 address.
        
        :type KernelId: string
        :param KernelId: 
        
          The ID of the kernel.
        
          .. warning::
        
            We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see `PV-GRUB <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        :type KeyName: string
        :param KeyName: 
        
          The name of the key pair. You can create a key pair using  CreateKeyPair or  ImportKeyPair .
        
          .. warning::
        
            If you do not specify a key pair, you can\'t connect to the instance unless you choose an AMI that is configured to allow users another way to log in.
        
        :type MaxCount: integer
        :param MaxCount: **[REQUIRED]** 
        
          The maximum number of instances to launch. If you specify more instances than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches the largest possible number of instances above ``MinCount`` .
        
          Constraints: Between 1 and the maximum number you\'re allowed for the specified instance type. For more information about the default limits, and how to request an increase, see `How many instances can I run in Amazon EC2 <http://aws.amazon.com/ec2/faqs/#How_many_instances_can_I_run_in_Amazon_EC2>`__ in the Amazon EC2 FAQ.
        
        :type MinCount: integer
        :param MinCount: **[REQUIRED]** 
        
          The minimum number of instances to launch. If you specify a minimum that is more instances than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches no instances.
        
          Constraints: Between 1 and the maximum number you\'re allowed for the specified instance type. For more information about the default limits, and how to request an increase, see `How many instances can I run in Amazon EC2 <http://aws.amazon.com/ec2/faqs/#How_many_instances_can_I_run_in_Amazon_EC2>`__ in the Amazon EC2 General FAQ.
        
        :type Monitoring: dict
        :param Monitoring: 
        
          The monitoring for the instance.
        
          - **Enabled** *(boolean) --* **[REQUIRED]** 
        
            Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
        
        :type Placement: dict
        :param Placement: 
        
          The placement for the instance.
        
          - **AvailabilityZone** *(string) --* 
        
            The Availability Zone of the instance.
        
          - **Affinity** *(string) --* 
        
            The affinity setting for the instance on the Dedicated Host. This parameter is not supported for the  ImportInstance command.
        
          - **GroupName** *(string) --* 
        
            The name of the placement group the instance is in.
        
          - **HostId** *(string) --* 
        
            The ID of the Dedicated Host on which the instance resides. This parameter is not supported for the  ImportInstance command.
        
          - **Tenancy** *(string) --* 
        
            The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of ``dedicated`` runs on single-tenant hardware. The ``host`` tenancy is not supported for the  ImportInstance command.
        
          - **SpreadDomain** *(string) --* 
        
            Reserved for future use.
        
        :type RamdiskId: string
        :param RamdiskId: 
        
          The ID of the RAM disk.
        
          .. warning::
        
            We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see `PV-GRUB <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        :type SecurityGroupIds: list
        :param SecurityGroupIds: 
        
          One or more security group IDs. You can create a security group using  CreateSecurityGroup .
        
          Default: Amazon EC2 uses the default security group.
        
          - *(string) --* 
        
        :type SecurityGroups: list
        :param SecurityGroups: 
        
          [EC2-Classic, default VPC] One or more security group names. For a nondefault VPC, you must use security group IDs instead.
        
          Default: Amazon EC2 uses the default security group.
        
          - *(string) --* 
        
        :type SubnetId: string
        :param SubnetId: 
        
          [EC2-VPC] The ID of the subnet to launch the instance into.
        
        :type UserData: string
        :param UserData: 
        
          The user data to make available to the instance. For more information, see `Running Commands on Your Linux Instance at Launch <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html>`__ (Linux) and `Adding User Data <http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-instance-metadata.html#instancedata-add-user-data>`__ (Windows). If you are using a command line tool, base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide base64-encoded text.
        
            **This value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.**
        
        :type AdditionalInfo: string
        :param AdditionalInfo: 
        
          Reserved.
        
        :type ClientToken: string
        :param ClientToken: 
        
          Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see `Ensuring Idempotency <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html>`__ .
        
          Constraints: Maximum 64 ASCII characters
        
        :type DisableApiTermination: boolean
        :param DisableApiTermination: 
        
          If you set this parameter to ``true`` , you can\'t terminate the instance using the Amazon EC2 console, CLI, or API; otherwise, you can. To change this attribute to ``false`` after launch, use  ModifyInstanceAttribute . Alternatively, if you set ``InstanceInitiatedShutdownBehavior`` to ``terminate`` , you can terminate the instance by running the shutdown command from the instance.
        
          Default: ``false``  
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type EbsOptimized: boolean
        :param EbsOptimized: 
        
          Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isn\'t available with all instance types. Additional usage charges apply when using an EBS-optimized instance.
        
          Default: ``false``  
        
        :type IamInstanceProfile: dict
        :param IamInstanceProfile: 
        
          The IAM instance profile.
        
          - **Arn** *(string) --* 
        
            The Amazon Resource Name (ARN) of the instance profile.
        
          - **Name** *(string) --* 
        
            The name of the instance profile.
        
        :type InstanceInitiatedShutdownBehavior: string
        :param InstanceInitiatedShutdownBehavior: 
        
          Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
        
          Default: ``stop``  
        
        :type NetworkInterfaces: list
        :param NetworkInterfaces: 
        
          One or more network interfaces.
        
          - *(dict) --* 
        
            Describes a network interface.
        
            - **AssociatePublicIpAddress** *(boolean) --* 
        
              Indicates whether to assign a public IPv4 address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is ``true`` .
        
            - **DeleteOnTermination** *(boolean) --* 
        
              If set to ``true`` , the interface is deleted when the instance is terminated. You can specify ``true`` only if creating a new network interface when launching an instance.
        
            - **Description** *(string) --* 
        
              The description of the network interface. Applies only if creating a network interface when launching an instance.
        
            - **DeviceIndex** *(integer) --* 
        
              The index of the device on the instance for the network interface attachment. If you are specifying a network interface in a  RunInstances request, you must provide the device index.
        
            - **Groups** *(list) --* 
        
              The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.
        
              - *(string) --* 
        
            - **Ipv6AddressCount** *(integer) --* 
        
              A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you\'ve specified a minimum number of instances to launch.
        
            - **Ipv6Addresses** *(list) --* 
        
              One or more IPv6 addresses to assign to the network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you\'ve specified a minimum number of instances to launch.
        
              - *(dict) --* 
        
                Describes an IPv6 address.
        
                - **Ipv6Address** *(string) --* 
        
                  The IPv6 address.
        
            - **NetworkInterfaceId** *(string) --* 
        
              The ID of the network interface.
        
            - **PrivateIpAddress** *(string) --* 
        
              The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you\'re launching more than one instance in a  RunInstances request.
        
            - **PrivateIpAddresses** *(list) --* 
        
              One or more private IPv4 addresses to assign to the network interface. Only one private IPv4 address can be designated as primary. You cannot specify this option if you\'re launching more than one instance in a  RunInstances request.
        
              - *(dict) --* 
        
                Describes a secondary private IPv4 address for a network interface.
        
                - **Primary** *(boolean) --* 
        
                  Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.
        
                - **PrivateIpAddress** *(string) --* 
        
                  The private IPv4 addresses.
        
            - **SecondaryPrivateIpAddressCount** *(integer) --* 
        
              The number of secondary private IPv4 addresses. You can\'t specify this option and specify more than one private IP address using the private IP addresses option. You cannot specify this option if you\'re launching more than one instance in a  RunInstances request.
        
            - **SubnetId** *(string) --* 
        
              The ID of the subnet associated with the network string. Applies only if creating a network interface when launching an instance.
        
        :type PrivateIpAddress: string
        :param PrivateIpAddress: 
        
          [EC2-VPC] The primary IPv4 address. You must specify a value from the IPv4 address range of the subnet.
        
          Only one private IP address can be designated as primary. You can\'t specify this option if you\'ve specified the option to designate a private IP address as the primary IP address in a network interface specification. You cannot specify this option if you\'re launching more than one instance in the request.
        
        :type ElasticGpuSpecification: list
        :param ElasticGpuSpecification: 
        
          An elastic GPU to associate with the instance.
        
          - *(dict) --* 
        
            A specification for an Elastic GPU.
        
            - **Type** *(string) --* **[REQUIRED]** 
        
              The type of Elastic GPU.
        
        :type TagSpecifications: list
        :param TagSpecifications: 
        
          The tags to apply to the resources during launch. You can only tag instances and volumes on launch. The specified tags are applied to all instances or volumes that are created during launch. To tag a resource after it has been created, see  CreateTags .
        
          - *(dict) --* 
        
            The tags to apply to a resource when the resource is being created.
        
            - **ResourceType** *(string) --* 
        
              The type of resource to tag. Currently, the resource types that support tagging on creation are ``fleet`` , ``dedicated-host`` , ``instance`` , ``snapshot`` , and ``volume`` . To tag a resource after it has been created, see  CreateTags .
        
            - **Tags** *(list) --* 
        
              The tags to apply to the resource.
        
              - *(dict) --* 
        
                Describes a tag.
        
                - **Key** *(string) --* 
        
                  The key of the tag.
        
                  Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
                - **Value** *(string) --* 
        
                  The value of the tag.
        
                  Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :type LaunchTemplate: dict
        :param LaunchTemplate: 
        
          The launch template to use to launch the instances. Any parameters that you specify in  RunInstances override the same parameters in the launch template. You can specify either the name or ID of a launch template, but not both.
        
          - **LaunchTemplateId** *(string) --* 
        
            The ID of the launch template.
        
          - **LaunchTemplateName** *(string) --* 
        
            The name of the launch template.
        
          - **Version** *(string) --* 
        
            The version number of the launch template.
        
            Default: The default version for the launch template.
        
        :type InstanceMarketOptions: dict
        :param InstanceMarketOptions: 
        
          The market (purchasing) option for the instances.
        
          For  RunInstances , persistent Spot Instance requests are only supported when **InstanceInterruptionBehavior** is set to either ``hibernate`` or ``stop`` .
        
          - **MarketType** *(string) --* 
        
            The market type.
        
          - **SpotOptions** *(dict) --* 
        
            The options for Spot Instances.
        
            - **MaxPrice** *(string) --* 
        
              The maximum hourly price you\'re willing to pay for the Spot Instances. The default is the On-Demand price.
        
            - **SpotInstanceType** *(string) --* 
        
              The Spot Instance request type. For  RunInstances , persistent Spot Instance requests are only supported when **InstanceInterruptionBehavior** is set to either ``hibernate`` or ``stop`` .
        
            - **BlockDurationMinutes** *(integer) --* 
        
              The required duration for the Spot Instances (also known as Spot blocks), in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).
        
            - **ValidUntil** *(datetime) --* 
        
              The end date of the request. For a one-time request, the request remains active until all instances launch, the request is canceled, or this date is reached. If the request is persistent, it remains active until it is canceled or this date and time is reached. The default end date is 7 days from the current date.
        
            - **InstanceInterruptionBehavior** *(string) --* 
        
              The behavior when a Spot Instance is interrupted. The default is ``terminate`` .
        
        :type CreditSpecification: dict
        :param CreditSpecification: 
        
          The credit option for CPU usage of the instance. Valid values are ``standard`` and ``unlimited`` . To change this attribute after launch, use  ModifyInstanceCreditSpecification . For more information, see `Burstable Performance Instances <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
          Default: ``standard`` (T2 instances) or ``unlimited`` (T3 instances)
        
          - **CpuCredits** *(string) --* **[REQUIRED]** 
        
            The credit option for CPU usage of a T2 or T3 instance. Valid values are ``standard`` and ``unlimited`` .
        
        :type CpuOptions: dict
        :param CpuOptions: 
        
          The CPU options for the instance. For more information, see `Optimizing CPU Options <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
          - **CoreCount** *(integer) --* 
        
            The number of CPU cores for the instance.
        
          - **ThreadsPerCore** *(integer) --* 
        
            The number of threads per CPU core. To disable Intel Hyper-Threading Technology for the instance, specify a value of ``1`` . Otherwise, specify the default value of ``2`` .
        
        :type CapacityReservationSpecification: dict
        :param CapacityReservationSpecification: 
        
          Information about the Capacity Reservation targeting option.
        
          - **CapacityReservationPreference** *(string) --* 
        
            Indicates the instance\'s Capacity Reservation preferences. Possible preferences include:
        
            * ``open`` - The instance can run in any ``open`` Capacity Reservation that has matching attributes (instance type, platform, Availability Zone). 
             
            * ``none`` - The instance avoids running in a Capacity Reservation even if one is available. The instance runs as an On-Demand Instance. 
             
          - **CapacityReservationTarget** *(dict) --* 
        
            Information about the target Capacity Reservation.
        
            - **CapacityReservationId** *(string) --* 
        
              The ID of the Capacity Reservation.
        
        :rtype: list(:py:class:`ec2.Instance`)
        :returns: A list of Instance resources
        """
        pass

    def create_internet_gateway(self, DryRun: bool = None) -> 'InternetGateway':
        """
        
        For more information about your VPC and internet gateway, see the `Amazon Virtual Private Cloud User Guide <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateInternetGateway>`_
        
        **Request Syntax** 
        ::
        
          internet_gateway = ec2.create_internet_gateway(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: :py:class:`ec2.InternetGateway`
        :returns: InternetGateway resource
        """
        pass

    def create_key_pair(self, KeyName: str, DryRun: bool = None) -> 'KeyPair':
        """
        
        You can have up to five thousand key pairs per region.
        
        The key pair returned to you is available only in the region in which you create it. If you prefer, you can create your own key pair using a third-party tool and upload it to any region using  ImportKeyPair .
        
        For more information, see `Key Pairs <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateKeyPair>`_
        
        **Request Syntax** 
        ::
        
          key_pair = ec2.create_key_pair(
              KeyName=\'string\',
              DryRun=True|False
          )
        :type KeyName: string
        :param KeyName: **[REQUIRED]** 
        
          A unique name for the key pair.
        
          Constraints: Up to 255 ASCII characters
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: :py:class:`ec2.KeyPair`
        :returns: KeyPair resource
        """
        pass

    def create_network_acl(self, VpcId: str, DryRun: bool = None) -> 'NetworkAcl':
        """
        
        For more information, see `Network ACLs <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateNetworkAcl>`_
        
        **Request Syntax** 
        ::
        
          network_acl = ec2.create_network_acl(
              DryRun=True|False,
              VpcId=\'string\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type VpcId: string
        :param VpcId: **[REQUIRED]** 
        
          The ID of the VPC.
        
        :rtype: :py:class:`ec2.NetworkAcl`
        :returns: NetworkAcl resource
        """
        pass

    def create_network_interface(self, SubnetId: str, Description: str = None, DryRun: bool = None, Groups: List = None, Ipv6AddressCount: int = None, Ipv6Addresses: List = None, PrivateIpAddress: str = None, PrivateIpAddresses: List = None, SecondaryPrivateIpAddressCount: int = None) -> 'NetworkInterface':
        """
        
        For more information about network interfaces, see `Elastic Network Interfaces <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateNetworkInterface>`_
        
        **Request Syntax** 
        ::
        
          network_interface = ec2.create_network_interface(
              Description=\'string\',
              DryRun=True|False,
              Groups=[
                  \'string\',
              ],
              Ipv6AddressCount=123,
              Ipv6Addresses=[
                  {
                      \'Ipv6Address\': \'string\'
                  },
              ],
              PrivateIpAddress=\'string\',
              PrivateIpAddresses=[
                  {
                      \'Primary\': True|False,
                      \'PrivateIpAddress\': \'string\'
                  },
              ],
              SecondaryPrivateIpAddressCount=123,
              SubnetId=\'string\'
          )
        :type Description: string
        :param Description: 
        
          A description for the network interface.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Groups: list
        :param Groups: 
        
          The IDs of one or more security groups.
        
          - *(string) --* 
        
        :type Ipv6AddressCount: integer
        :param Ipv6AddressCount: 
        
          The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can\'t use this option if specifying specific IPv6 addresses. If your subnet has the ``AssignIpv6AddressOnCreation`` attribute set to ``true`` , you can specify ``0`` to override this setting.
        
        :type Ipv6Addresses: list
        :param Ipv6Addresses: 
        
          One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. You can\'t use this option if you\'re specifying a number of IPv6 addresses.
        
          - *(dict) --* 
        
            Describes an IPv6 address.
        
            - **Ipv6Address** *(string) --* 
        
              The IPv6 address.
        
        :type PrivateIpAddress: string
        :param PrivateIpAddress: 
        
          The primary private IPv4 address of the network interface. If you don\'t specify an IPv4 address, Amazon EC2 selects one for you from the subnet\'s IPv4 CIDR range. If you specify an IP address, you cannot indicate any IP addresses specified in ``privateIpAddresses`` as primary (only one IP address can be designated as primary).
        
        :type PrivateIpAddresses: list
        :param PrivateIpAddresses: 
        
          One or more private IPv4 addresses.
        
          - *(dict) --* 
        
            Describes a secondary private IPv4 address for a network interface.
        
            - **Primary** *(boolean) --* 
        
              Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.
        
            - **PrivateIpAddress** *(string) --* 
        
              The private IPv4 addresses.
        
        :type SecondaryPrivateIpAddressCount: integer
        :param SecondaryPrivateIpAddressCount: 
        
          The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary IPv4 addresses, Amazon EC2 selects these IP addresses within the subnet\'s IPv4 CIDR range. You can\'t specify this option and specify more than one private IP address using ``privateIpAddresses`` .
        
          The number of IP addresses you can assign to a network interface varies by instance type. For more information, see `IP Addresses Per ENI Per Instance Type <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        :type SubnetId: string
        :param SubnetId: **[REQUIRED]** 
        
          The ID of the subnet to associate with the network interface.
        
        :rtype: :py:class:`ec2.NetworkInterface`
        :returns: NetworkInterface resource
        """
        pass

    def create_placement_group(self, GroupName: str, Strategy: str, DryRun: bool = None) -> 'PlacementGroup':
        """
        
        A ``cluster`` placement group is a logical grouping of instances within a single Availability Zone that benefit from low network latency, high network throughput. A ``spread`` placement group places instances on distinct hardware.
        
        For more information, see `Placement Groups <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreatePlacementGroup>`_
        
        **Request Syntax** 
        ::
        
          placement_group = ec2.create_placement_group(
              DryRun=True|False,
              GroupName=\'string\',
              Strategy=\'cluster\'|\'spread\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type GroupName: string
        :param GroupName: **[REQUIRED]** 
        
          A name for the placement group. Must be unique within the scope of your account for the region.
        
          Constraints: Up to 255 ASCII characters
        
        :type Strategy: string
        :param Strategy: **[REQUIRED]** 
        
          The placement strategy.
        
        :rtype: :py:class:`ec2.PlacementGroup`
        :returns: PlacementGroup resource
        """
        pass

    def create_route_table(self, VpcId: str, DryRun: bool = None) -> 'RouteTable':
        """
        
        For more information, see `Route Tables <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateRouteTable>`_
        
        **Request Syntax** 
        ::
        
          route_table = ec2.create_route_table(
              DryRun=True|False,
              VpcId=\'string\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type VpcId: string
        :param VpcId: **[REQUIRED]** 
        
          The ID of the VPC.
        
        :rtype: :py:class:`ec2.RouteTable`
        :returns: RouteTable resource
        """
        pass

    def create_security_group(self, Description: str, GroupName: str, VpcId: str = None, DryRun: bool = None) -> 'SecurityGroup':
        """
        
        A security group is for use with instances either in the EC2-Classic platform or in a specific VPC. For more information, see `Amazon EC2 Security Groups <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html>`__ in the *Amazon Elastic Compute Cloud User Guide* and `Security Groups for Your VPC <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        .. warning::
        
          EC2-Classic: You can have up to 500 security groups.
        
          EC2-VPC: You can create up to 500 security groups per VPC.
        
        When you create a security group, you specify a friendly name of your choice. You can have a security group for use in EC2-Classic with the same name as a security group for use in a VPC. However, you can\'t have two security groups for use in EC2-Classic with the same name or two security groups for use in a VPC with the same name.
        
        You have a default security group for use in EC2-Classic and a default security group for use in your VPC. If you don\'t specify a security group when you launch an instance, the instance is launched into the appropriate default security group. A default security group includes a default rule that grants instances unrestricted network access to each other.
        
        You can add or remove rules from your security groups using  AuthorizeSecurityGroupIngress ,  AuthorizeSecurityGroupEgress ,  RevokeSecurityGroupIngress , and  RevokeSecurityGroupEgress .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateSecurityGroup>`_
        
        **Request Syntax** 
        ::
        
          security_group = ec2.create_security_group(
              Description=\'string\',
              GroupName=\'string\',
              VpcId=\'string\',
              DryRun=True|False
          )
        :type Description: string
        :param Description: **[REQUIRED]** 
        
          A description for the security group. This is informational only.
        
          Constraints: Up to 255 characters in length
        
          Constraints for EC2-Classic: ASCII characters
        
          Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*
        
        :type GroupName: string
        :param GroupName: **[REQUIRED]** 
        
          The name of the security group.
        
          Constraints: Up to 255 characters in length. Cannot start with ``sg-`` .
        
          Constraints for EC2-Classic: ASCII characters
        
          Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*
        
        :type VpcId: string
        :param VpcId: 
        
          [EC2-VPC] The ID of the VPC. Required for EC2-VPC.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: :py:class:`ec2.SecurityGroup`
        :returns: SecurityGroup resource
        """
        pass

    def create_snapshot(self, VolumeId: str, Description: str = None, TagSpecifications: List = None, DryRun: bool = None) -> 'Snapshot':
        """
        
        When a snapshot is created, any AWS Marketplace product codes that are associated with the source volume are propagated to the snapshot.
        
        You can take a snapshot of an attached volume that is in use. However, snapshots only capture data that has been written to your EBS volume at the time the snapshot command is issued; this may exclude any data that has been cached by any applications or the operating system. If you can pause any file systems on the volume long enough to take a snapshot, your snapshot should be complete. However, if you cannot pause all file writes to the volume, you should unmount the volume from within the instance, issue the snapshot command, and then remount the volume to ensure a consistent and complete snapshot. You may remount and use your volume while the snapshot status is ``pending`` .
        
        To create a snapshot for EBS volumes that serve as root devices, you should stop the instance before taking the snapshot.
        
        Snapshots that are taken from encrypted volumes are automatically encrypted. Volumes that are created from encrypted snapshots are also automatically encrypted. Your encrypted volumes and any associated snapshots always remain protected.
        
        You can tag your snapshots during creation. For more information, see `Tagging Your Amazon EC2 Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        For more information, see `Amazon Elastic Block Store <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html>`__ and `Amazon EBS Encryption <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateSnapshot>`_
        
        **Request Syntax** 
        ::
        
          snapshot = ec2.create_snapshot(
              Description=\'string\',
              VolumeId=\'string\',
              TagSpecifications=[
                  {
                      \'ResourceType\': \'customer-gateway\'|\'dedicated-host\'|\'dhcp-options\'|\'image\'|\'instance\'|\'internet-gateway\'|\'network-acl\'|\'network-interface\'|\'reserved-instances\'|\'route-table\'|\'snapshot\'|\'spot-instances-request\'|\'subnet\'|\'security-group\'|\'volume\'|\'vpc\'|\'vpn-connection\'|\'vpn-gateway\',
                      \'Tags\': [
                          {
                              \'Key\': \'string\',
                              \'Value\': \'string\'
                          },
                      ]
                  },
              ],
              DryRun=True|False
          )
        :type Description: string
        :param Description: 
        
          A description for the snapshot.
        
        :type VolumeId: string
        :param VolumeId: **[REQUIRED]** 
        
          The ID of the EBS volume.
        
        :type TagSpecifications: list
        :param TagSpecifications: 
        
          The tags to apply to the snapshot during creation.
        
          - *(dict) --* 
        
            The tags to apply to a resource when the resource is being created.
        
            - **ResourceType** *(string) --* 
        
              The type of resource to tag. Currently, the resource types that support tagging on creation are ``fleet`` , ``dedicated-host`` , ``instance`` , ``snapshot`` , and ``volume`` . To tag a resource after it has been created, see  CreateTags .
        
            - **Tags** *(list) --* 
        
              The tags to apply to the resource.
        
              - *(dict) --* 
        
                Describes a tag.
        
                - **Key** *(string) --* 
        
                  The key of the tag.
        
                  Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
                - **Value** *(string) --* 
        
                  The value of the tag.
        
                  Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: :py:class:`ec2.Snapshot`
        :returns: Snapshot resource
        """
        pass

    def create_subnet(self, CidrBlock: str, VpcId: str, AvailabilityZone: str = None, Ipv6CidrBlock: str = None, DryRun: bool = None) -> 'Subnet':
        """
        
        When you create each subnet, you provide the VPC ID and IPv4 CIDR block for the subnet. After you create a subnet, you can\'t change its CIDR block. The size of the subnet\'s IPv4 CIDR block can be the same as a VPC\'s IPv4 CIDR block, or a subset of a VPC\'s IPv4 CIDR block. If you create more than one subnet in a VPC, the subnets\' CIDR blocks must not overlap. The smallest IPv4 subnet (and VPC) you can create uses a /28 netmask (16 IPv4 addresses), and the largest uses a /16 netmask (65,536 IPv4 addresses).
        
        If you\'ve associated an IPv6 CIDR block with your VPC, you can create a subnet with an IPv6 CIDR block that uses a /64 prefix length. 
        
        .. warning::
        
          AWS reserves both the first four and the last IPv4 address in each subnet\'s CIDR block. They\'re not available for use.
        
        If you add more than one subnet to a VPC, they\'re set up in a star topology with a logical router in the middle.
        
        If you launch an instance in a VPC using an Amazon EBS-backed AMI, the IP address doesn\'t change if you stop and restart the instance (unlike a similar instance launched outside a VPC, which gets a new IP address when restarted). It\'s therefore possible to have a subnet with no running instances (they\'re all stopped), but no remaining IP addresses available.
        
        For more information about subnets, see `Your VPC and Subnets <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateSubnet>`_
        
        **Request Syntax** 
        ::
        
          subnet = ec2.create_subnet(
              AvailabilityZone=\'string\',
              CidrBlock=\'string\',
              Ipv6CidrBlock=\'string\',
              VpcId=\'string\',
              DryRun=True|False
          )
        :type AvailabilityZone: string
        :param AvailabilityZone: 
        
          The Availability Zone for the subnet.
        
          Default: AWS selects one for you. If you create more than one subnet in your VPC, we may not necessarily select a different zone for each subnet.
        
        :type CidrBlock: string
        :param CidrBlock: **[REQUIRED]** 
        
          The IPv4 network range for the subnet, in CIDR notation. For example, ``10.0.0.0/24`` .
        
        :type Ipv6CidrBlock: string
        :param Ipv6CidrBlock: 
        
          The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length.
        
        :type VpcId: string
        :param VpcId: **[REQUIRED]** 
        
          The ID of the VPC.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: :py:class:`ec2.Subnet`
        :returns: Subnet resource
        """
        pass

    def create_tags(self, Resources: List[str], Tags: List, DryRun: bool = None):
        """
        
        """
        pass

    def create_volume(self, AvailabilityZone: str, Encrypted: bool = None, Iops: int = None, KmsKeyId: str = None, Size: int = None, SnapshotId: str = None, VolumeType: str = None, DryRun: bool = None, TagSpecifications: List = None) -> 'Volume':
        """
        
        You can create a new empty volume or restore a volume from an EBS snapshot. Any AWS Marketplace product codes from the snapshot are propagated to the volume.
        
        You can create encrypted volumes with the ``Encrypted`` parameter. Encrypted volumes may only be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are also automatically encrypted. For more information, see `Amazon EBS Encryption <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        You can tag your volumes during creation. For more information, see `Tagging Your Amazon EC2 Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        For more information, see `Creating an Amazon EBS Volume <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-volume.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateVolume>`_
        
        **Request Syntax** 
        ::
        
          volume = ec2.create_volume(
              AvailabilityZone=\'string\',
              Encrypted=True|False,
              Iops=123,
              KmsKeyId=\'string\',
              Size=123,
              SnapshotId=\'string\',
              VolumeType=\'standard\'|\'io1\'|\'gp2\'|\'sc1\'|\'st1\',
              DryRun=True|False,
              TagSpecifications=[
                  {
                      \'ResourceType\': \'customer-gateway\'|\'dedicated-host\'|\'dhcp-options\'|\'image\'|\'instance\'|\'internet-gateway\'|\'network-acl\'|\'network-interface\'|\'reserved-instances\'|\'route-table\'|\'snapshot\'|\'spot-instances-request\'|\'subnet\'|\'security-group\'|\'volume\'|\'vpc\'|\'vpn-connection\'|\'vpn-gateway\',
                      \'Tags\': [
                          {
                              \'Key\': \'string\',
                              \'Value\': \'string\'
                          },
                      ]
                  },
              ]
          )
        :type AvailabilityZone: string
        :param AvailabilityZone: **[REQUIRED]** 
        
          The Availability Zone in which to create the volume. Use  DescribeAvailabilityZones to list the Availability Zones that are currently available to you.
        
        :type Encrypted: boolean
        :param Encrypted: 
        
          Specifies whether the volume should be encrypted. Encrypted Amazon EBS volumes may only be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are automatically encrypted. There is no way to create an encrypted volume from an unencrypted snapshot or vice versa. If your AMI uses encrypted volumes, you can only launch it on supported instance types. For more information, see `Amazon EBS Encryption <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        :type Iops: integer
        :param Iops: 
        
          The number of I/O operations per second (IOPS) to provision for the volume, with a maximum ratio of 50 IOPS/GiB. Range is 100 to 32000 IOPS for volumes in most regions. For exceptions, see `Amazon EBS Volume Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
          This parameter is valid only for Provisioned IOPS SSD (io1) volumes.
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          An identifier for the AWS Key Management Service (AWS KMS) customer master key (CMK) to use when creating the encrypted volume. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. If a ``KmsKeyId`` is specified, the ``Encrypted`` flag must also be set. 
        
          The CMK identifier may be provided in any of the following formats: 
        
          * Key ID 
           
          * Key alias 
           
          * ARN using key ID. The ID ARN contains the ``arn:aws:kms`` namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the ``key`` namespace, and then the CMK ID. For example, arn:aws:kms:*us-east-1* :*012345678910* :key/*abcd1234-a123-456a-a12b-a123b4cd56ef* .  
           
          * ARN using key alias. The alias ARN contains the ``arn:aws:kms`` namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the ``alias`` namespace, and then the CMK alias. For example, arn:aws:kms:*us-east-1* :*012345678910* :alias/*ExampleAlias* .  
           
          AWS parses ``KmsKeyId`` asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. The action will eventually fail. 
        
        :type Size: integer
        :param Size: 
        
          The size of the volume, in GiBs.
        
          Constraints: 1-16384 for ``gp2`` , 4-16384 for ``io1`` , 500-16384 for ``st1`` , 500-16384 for ``sc1`` , and 1-1024 for ``standard`` . If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
        
          Default: If you\'re creating the volume from a snapshot and don\'t specify a volume size, the default is the snapshot size.
        
        :type SnapshotId: string
        :param SnapshotId: 
        
          The snapshot from which to create the volume.
        
        :type VolumeType: string
        :param VolumeType: 
        
          The volume type. This can be ``gp2`` for General Purpose SSD, ``io1`` for Provisioned IOPS SSD, ``st1`` for Throughput Optimized HDD, ``sc1`` for Cold HDD, or ``standard`` for Magnetic volumes.
        
          Defaults: If no volume type is specified, the default is ``standard`` in us-east-1, eu-west-1, eu-central-1, us-west-2, us-west-1, sa-east-1, ap-northeast-1, ap-northeast-2, ap-southeast-1, ap-southeast-2, ap-south-1, us-gov-west-1, and cn-north-1. In all other regions, EBS defaults to ``gp2`` .
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type TagSpecifications: list
        :param TagSpecifications: 
        
          The tags to apply to the volume during creation.
        
          - *(dict) --* 
        
            The tags to apply to a resource when the resource is being created.
        
            - **ResourceType** *(string) --* 
        
              The type of resource to tag. Currently, the resource types that support tagging on creation are ``fleet`` , ``dedicated-host`` , ``instance`` , ``snapshot`` , and ``volume`` . To tag a resource after it has been created, see  CreateTags .
        
            - **Tags** *(list) --* 
        
              The tags to apply to the resource.
        
              - *(dict) --* 
        
                Describes a tag.
        
                - **Key** *(string) --* 
        
                  The key of the tag.
        
                  Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
                - **Value** *(string) --* 
        
                  The value of the tag.
        
                  Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :rtype: :py:class:`ec2.Volume`
        :returns: Volume resource
        """
        pass

    def create_vpc(self, CidrBlock: str, AmazonProvidedIpv6CidrBlock: bool = None, DryRun: bool = None, InstanceTenancy: str = None) -> 'Vpc':
        """
        
        You can optionally request an Amazon-provided IPv6 CIDR block for the VPC. The IPv6 CIDR block uses a /56 prefix length, and is allocated from Amazon\'s pool of IPv6 addresses. You cannot choose the IPv6 range for your VPC.
        
        By default, each instance you launch in the VPC has the default DHCP options, which include only a default DNS server that we provide (AmazonProvidedDNS). For more information, see `DHCP Options Sets <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        You can specify the instance tenancy value for the VPC when you create it. You can\'t change this value for the VPC after you create it. For more information, see `Dedicated Instances <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateVpc>`_
        
        **Request Syntax** 
        ::
        
          vpc = ec2.create_vpc(
              CidrBlock=\'string\',
              AmazonProvidedIpv6CidrBlock=True|False,
              DryRun=True|False,
              InstanceTenancy=\'default\'|\'dedicated\'|\'host\'
          )
        :type CidrBlock: string
        :param CidrBlock: **[REQUIRED]** 
        
          The IPv4 network range for the VPC, in CIDR notation. For example, ``10.0.0.0/16`` .
        
        :type AmazonProvidedIpv6CidrBlock: boolean
        :param AmazonProvidedIpv6CidrBlock: 
        
          Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or the size of the CIDR block.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type InstanceTenancy: string
        :param InstanceTenancy: 
        
          The tenancy options for instances launched into the VPC. For ``default`` , instances are launched with shared tenancy by default. You can launch instances with any tenancy into a shared tenancy VPC. For ``dedicated`` , instances are launched as dedicated tenancy instances by default. You can only launch instances with a tenancy of ``dedicated`` or ``host`` into a dedicated tenancy VPC. 
        
           **Important:** The ``host`` value cannot be used with this parameter. Use the ``default`` or ``dedicated`` values only.
        
          Default: ``default``  
        
        :rtype: :py:class:`ec2.Vpc`
        :returns: Vpc resource
        """
        pass

    def create_vpc_peering_connection(self, DryRun: bool = None, PeerOwnerId: str = None, PeerVpcId: str = None, VpcId: str = None, PeerRegion: str = None) -> 'VpcPeeringConnection':
        """
        
        .. note::
        
          Limitations and rules apply to a VPC peering connection. For more information, see the `limitations <http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/vpc-peering-basics.html#vpc-peering-limitations>`__ section in the *VPC Peering Guide* .
        
        The owner of the accepter VPC must accept the peering request to activate the peering connection. The VPC peering connection request expires after 7 days, after which it cannot be accepted or rejected.
        
        If you create a VPC peering connection request between VPCs with overlapping CIDR blocks, the VPC peering connection has a status of ``failed`` .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateVpcPeeringConnection>`_
        
        **Request Syntax** 
        ::
        
          vpc_peering_connection = ec2.create_vpc_peering_connection(
              DryRun=True|False,
              PeerOwnerId=\'string\',
              PeerVpcId=\'string\',
              VpcId=\'string\',
              PeerRegion=\'string\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type PeerOwnerId: string
        :param PeerOwnerId: 
        
          The AWS account ID of the owner of the accepter VPC.
        
          Default: Your AWS account ID
        
        :type PeerVpcId: string
        :param PeerVpcId: 
        
          The ID of the VPC with which you are creating the VPC peering connection. You must specify this parameter in the request.
        
        :type VpcId: string
        :param VpcId: 
        
          The ID of the requester VPC. You must specify this parameter in the request.
        
        :type PeerRegion: string
        :param PeerRegion: 
        
          The region code for the accepter VPC, if the accepter VPC is located in a region other than the region in which you make the request.
        
          Default: The region in which you make the request.
        
        :rtype: :py:class:`ec2.VpcPeeringConnection`
        :returns: VpcPeeringConnection resource
        """
        pass

    def disassociate_route_table(self, AssociationId: str, DryRun: bool = None):
        """
        
        After you perform this action, the subnet no longer uses the routes in the route table. Instead, it uses the routes in the VPC\'s main route table. For more information about route tables, see `Route Tables <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DisassociateRouteTable>`_
        
        **Request Syntax** 
        ::
        
          response = ec2.disassociate_route_table(
              AssociationId=\'string\',
              DryRun=True|False
          )
        :type AssociationId: string
        :param AssociationId: **[REQUIRED]** 
        
          The association ID representing the current association between the route table and subnet.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def import_key_pair(self, KeyName: str, PublicKeyMaterial: bytes, DryRun: bool = None) -> 'KeyPairInfo':
        """
        
        For more information about key pairs, see `Key Pairs <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ImportKeyPair>`_
        
        **Request Syntax** 
        ::
        
          key_pair_info = ec2.import_key_pair(
              DryRun=True|False,
              KeyName=\'string\',
              PublicKeyMaterial=b\'bytes\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type KeyName: string
        :param KeyName: **[REQUIRED]** 
        
          A unique name for the key pair.
        
        :type PublicKeyMaterial: bytes
        :param PublicKeyMaterial: **[REQUIRED]** 
        
          The public key. For API calls, the text must be base64-encoded. For command line tools, base64 encoding is performed for you.
        
        :rtype: :py:class:`ec2.KeyPairInfo`
        :returns: KeyPairInfo resource
        """
        pass

    def register_image(self, Name: str, ImageLocation: str = None, Architecture: str = None, BlockDeviceMappings: List = None, Description: str = None, DryRun: bool = None, EnaSupport: bool = None, KernelId: str = None, BillingProducts: List = None, RamdiskId: str = None, RootDeviceName: str = None, SriovNetSupport: str = None, VirtualizationType: str = None) -> 'Image':
        """
        
        .. note::
        
          For Amazon EBS-backed instances,  CreateImage creates and registers the AMI in a single request, so you don\'t have to register the AMI yourself.
        
        You can also use ``RegisterImage`` to create an Amazon EBS-backed Linux AMI from a snapshot of a root device volume. You specify the snapshot using the block device mapping. For more information, see `Launching a Linux Instance from a Backup <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-launch-snapshot.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        You can\'t register an image where a secondary (non-root) snapshot has AWS Marketplace product codes.
        
        Some Linux distributions, such as Red Hat Enterprise Linux (RHEL) and SUSE Linux Enterprise Server (SLES), use the EC2 billing product code associated with an AMI to verify the subscription status for package updates. Creating an AMI from an EBS snapshot does not maintain this billing code, and instances launched from such an AMI are not able to connect to package update infrastructure. If you purchase a Reserved Instance offering for one of these Linux distributions and launch instances using an AMI that does not contain the required billing code, your Reserved Instance is not applied to these instances.
        
        To create an AMI for operating systems that require a billing code, see  CreateImage .
        
        If needed, you can deregister an AMI at any time. Any modifications you make to an AMI backed by an instance store volume invalidates its registration. If you make changes to an image, deregister the previous image and register the new image.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/RegisterImage>`_
        
        **Request Syntax** 
        ::
        
          image = ec2.register_image(
              ImageLocation=\'string\',
              Architecture=\'i386\'|\'x86_64\',
              BlockDeviceMappings=[
                  {
                      \'DeviceName\': \'string\',
                      \'VirtualName\': \'string\',
                      \'Ebs\': {
                          \'DeleteOnTermination\': True|False,
                          \'Iops\': 123,
                          \'SnapshotId\': \'string\',
                          \'VolumeSize\': 123,
                          \'VolumeType\': \'standard\'|\'io1\'|\'gp2\'|\'sc1\'|\'st1\',
                          \'Encrypted\': True|False,
                          \'KmsKeyId\': \'string\'
                      },
                      \'NoDevice\': \'string\'
                  },
              ],
              Description=\'string\',
              DryRun=True|False,
              EnaSupport=True|False,
              KernelId=\'string\',
              Name=\'string\',
              BillingProducts=[
                  \'string\',
              ],
              RamdiskId=\'string\',
              RootDeviceName=\'string\',
              SriovNetSupport=\'string\',
              VirtualizationType=\'string\'
          )
        :type ImageLocation: string
        :param ImageLocation: 
        
          The full path to your AMI manifest in Amazon S3 storage.
        
        :type Architecture: string
        :param Architecture: 
        
          The architecture of the AMI.
        
          Default: For Amazon EBS-backed AMIs, ``i386`` . For instance store-backed AMIs, the architecture specified in the manifest file.
        
        :type BlockDeviceMappings: list
        :param BlockDeviceMappings: 
        
          One or more block device mapping entries.
        
          - *(dict) --* 
        
            Describes a block device mapping.
        
            - **DeviceName** *(string) --* 
        
              The device name (for example, ``/dev/sdh`` or ``xvdh`` ).
        
            - **VirtualName** *(string) --* 
        
              The virtual device name (``ephemeral`` N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ``ephemeral0`` and ``ephemeral1`` . The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
        
              NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect.
        
              Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
        
            - **Ebs** *(dict) --* 
        
              Parameters used to automatically set up EBS volumes when the instance is launched.
        
              - **DeleteOnTermination** *(boolean) --* 
        
                Indicates whether the EBS volume is deleted on instance termination.
        
              - **Iops** *(integer) --* 
        
                The number of I/O operations per second (IOPS) that the volume supports. For ``io1`` , this represents the number of IOPS that are provisioned for the volume. For ``gp2`` , this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see `Amazon EBS Volume Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
                Constraint: Range is 100-20000 IOPS for ``io1`` volumes and 100-10000 IOPS for ``gp2`` volumes.
        
                Condition: This parameter is required for requests to create ``io1`` volumes; it is not used in requests to create ``gp2`` , ``st1`` , ``sc1`` , or ``standard`` volumes.
        
              - **SnapshotId** *(string) --* 
        
                The ID of the snapshot.
        
              - **VolumeSize** *(integer) --* 
        
                The size of the volume, in GiB.
        
                Constraints: 1-16384 for General Purpose SSD (``gp2`` ), 4-16384 for Provisioned IOPS SSD (``io1`` ), 500-16384 for Throughput Optimized HDD (``st1`` ), 500-16384 for Cold HDD (``sc1`` ), and 1-1024 for Magnetic (``standard`` ) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
        
                Default: If you\'re creating the volume from a snapshot and don\'t specify a volume size, the default is the snapshot size.
        
              - **VolumeType** *(string) --* 
        
                The volume type: ``gp2`` , ``io1`` , ``st1`` , ``sc1`` , or ``standard`` .
        
                Default: ``standard``  
        
              - **Encrypted** *(boolean) --* 
        
                Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. 
        
                If you are creating a volume from a snapshot, you cannot specify an encryption value. This is because only blank volumes can be encrypted on creation. If you are creating a snapshot from an existing EBS volume, you cannot specify an encryption value that differs from that of the EBS volume. We recommend that you omit the encryption value from the block device mappings when creating an image from an instance.
        
              - **KmsKeyId** *(string) --* 
        
                Identifier (key ID, key alias, ID ARN, or alias ARN) for a user-managed CMK under which the EBS volume is encrypted.
        
                This parameter is only supported on ``BlockDeviceMapping`` objects called by `RunInstances <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html>`__ , `RequestSpotFleet <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet.html>`__ , and `RequestSpotInstances <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html>`__ .
        
            - **NoDevice** *(string) --* 
        
              Suppresses the specified device included in the block device mapping of the AMI.
        
        :type Description: string
        :param Description: 
        
          A description for your AMI.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type EnaSupport: boolean
        :param EnaSupport: 
        
          Set to ``true`` to enable enhanced networking with ENA for the AMI and any instances that you launch from the AMI.
        
          This option is supported only for HVM AMIs. Specifying this option with a PV AMI can make instances launched from the AMI unreachable.
        
        :type KernelId: string
        :param KernelId: 
        
          The ID of the kernel.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          A name for your AMI.
        
          Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes (\'), at-signs (@), or underscores(_)
        
        :type BillingProducts: list
        :param BillingProducts: 
        
          The billing product codes. Your account must be authorized to specify billing product codes. Otherwise, you can use the AWS Marketplace to bill for the use of an AMI.
        
          - *(string) --* 
        
        :type RamdiskId: string
        :param RamdiskId: 
        
          The ID of the RAM disk.
        
        :type RootDeviceName: string
        :param RootDeviceName: 
        
          The device name of the root device volume (for example, ``/dev/sda1`` ).
        
        :type SriovNetSupport: string
        :param SriovNetSupport: 
        
          Set to ``simple`` to enable enhanced networking with the Intel 82599 Virtual Function interface for the AMI and any instances that you launch from the AMI.
        
          There is no way to disable ``sriovNetSupport`` at this time.
        
          This option is supported only for HVM AMIs. Specifying this option with a PV AMI can make instances launched from the AMI unreachable.
        
        :type VirtualizationType: string
        :param VirtualizationType: 
        
          The type of virtualization (``hvm`` | ``paravirtual`` ).
        
          Default: ``paravirtual``  
        
        :rtype: :py:class:`ec2.Image`
        :returns: Image resource
        """
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
        """
        
        An Elastic IP address is for use in either the EC2-Classic platform or in a VPC. For more information, see `Elastic IP Addresses <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        [EC2-Classic, VPC in an EC2-VPC-only account] If the Elastic IP address is already associated with a different instance, it is disassociated from that instance and associated with the specified instance. If you associate an Elastic IP address with an instance that has an existing Elastic IP address, the existing address is disassociated from the instance, but remains allocated to your account.
        
        [VPC in an EC2-Classic account] If you don\'t specify a private IP address, the Elastic IP address is associated with the primary IP address. If the Elastic IP address is already associated with a different instance or a network interface, you get an error unless you allow reassociation. You cannot associate an Elastic IP address with an instance or network interface that has an existing Elastic IP address.
        
        .. warning::
        
          This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn\'t return an error, and you may be charged for each time the Elastic IP address is remapped to the same instance. For more information, see the *Elastic IP Addresses* section of `Amazon EC2 Pricing <http://aws.amazon.com/ec2/pricing/>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AssociateAddress>`_
        
        **Request Syntax** 
        ::
        
          response = classic_address.associate(
              AllocationId=\'string\',
              InstanceId=\'string\',
              AllowReassociation=True|False,
              DryRun=True|False,
              NetworkInterfaceId=\'string\',
              PrivateIpAddress=\'string\'
          )
        :type AllocationId: string
        :param AllocationId: 
        
          [EC2-VPC] The allocation ID. This is required for EC2-VPC.
        
        :type InstanceId: string
        :param InstanceId: 
        
          The ID of the instance. This is required for EC2-Classic. For EC2-VPC, you can specify either the instance ID or the network interface ID, but not both. The operation fails if you specify an instance ID unless exactly one network interface is attached.
        
        :type AllowReassociation: boolean
        :param AllowReassociation: 
        
          [EC2-VPC] For a VPC in an EC2-Classic account, specify true to allow an Elastic IP address that is already associated with an instance or network interface to be reassociated with the specified instance or network interface. Otherwise, the operation fails. In a VPC in an EC2-VPC-only account, reassociation is automatic, therefore you can specify false to ensure the operation fails if the Elastic IP address is already associated with another resource.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type NetworkInterfaceId: string
        :param NetworkInterfaceId: 
        
          [EC2-VPC] The ID of the network interface. If the instance has more than one network interface, you must specify a network interface ID.
        
        :type PrivateIpAddress: string
        :param PrivateIpAddress: 
        
          [EC2-VPC] The primary or secondary private IP address to associate with the Elastic IP address. If no private IP address is specified, the Elastic IP address is associated with the primary private IP address.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AssociationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AssociationId** *(string) --* 
        
              [EC2-VPC] The ID that represents the association of the Elastic IP address with an instance.
        
        """
        pass

    def disassociate(self, AssociationId: str = None, DryRun: bool = None):
        """
        
        An Elastic IP address is for use in either the EC2-Classic platform or in a VPC. For more information, see `Elastic IP Addresses <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn\'t return an error.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DisassociateAddress>`_
        
        **Request Syntax** 
        ::
        
          response = classic_address.disassociate(
              AssociationId=\'string\',
              DryRun=True|False
          )
        :type AssociationId: string
        :param AssociationId: 
        
          [EC2-VPC] The association ID. Required for EC2-VPC.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          classic_address.load()
        :returns: None
        """
        pass

    def release(self, AllocationId: str = None, DryRun: bool = None):
        """
        
        [EC2-Classic, default VPC] Releasing an Elastic IP address automatically disassociates it from any instance that it\'s associated with. To disassociate an Elastic IP address without releasing it, use  DisassociateAddress .
        
        [Nondefault VPC] You must use  DisassociateAddress to disassociate the Elastic IP address before you can release it. Otherwise, Amazon EC2 returns an error (``InvalidIPAddress.InUse`` ).
        
        After releasing an Elastic IP address, it is released to the IP address pool. Be sure to update your DNS records and any servers or devices that communicate with the address. If you attempt to release an Elastic IP address that you already released, you\'ll get an ``AuthFailure`` error if the address is already allocated to another AWS account.
        
        [EC2-VPC] After you release an Elastic IP address for use in a VPC, you might be able to recover it. For more information, see  AllocateAddress .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ReleaseAddress>`_
        
        **Request Syntax** 
        ::
        
          response = classic_address.release(
              AllocationId=\'string\',
              DryRun=True|False
          )
        :type AllocationId: string
        :param AllocationId: 
        
          [EC2-VPC] The allocation ID. Required for EC2-VPC.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          classic_address.load()
        :returns: None
        """
        pass


class DhcpOptions(base.ServiceResource):
    dhcp_configurations: List
    dhcp_options_id: str
    tags: List
    id: str

    def associate_with_vpc(self, VpcId: str, DryRun: bool = None):
        """
        
        After you associate the options with the VPC, any existing instances and all new instances that you launch in that VPC use the options. You don\'t need to restart or relaunch the instances. They automatically pick up the changes within a few hours, depending on how frequently the instance renews its DHCP lease. You can explicitly renew the lease using the operating system on the instance.
        
        For more information, see `DHCP Options Sets <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AssociateDhcpOptions>`_
        
        **Request Syntax** 
        ::
        
          response = dhcp_options.associate_with_vpc(
              VpcId=\'string\',
              DryRun=True|False
          )
        :type VpcId: string
        :param VpcId: **[REQUIRED]** 
        
          The ID of the VPC.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        """
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . For more information about creating IAM policies that control users\' access to resources based on tags, see `Supported Resource-Level Permissions for Amazon EC2 API Actions <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          tag = dhcp_options.create_tags(
              DryRun=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. The ``value`` parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 
        
          - *(dict) --* 
        
            Describes a tag.
        
            - **Key** *(string) --* 
        
              The key of the tag.
        
              Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
              Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :rtype: list(:py:class:`ec2.Tag`)
        :returns: A list of Tag resources
        """
        pass

    def delete(self, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteDhcpOptions>`_
        
        **Request Syntax** 
        ::
        
          response = dhcp_options.delete(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          dhcp_options.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          dhcp_options.load()
        :returns: None
        """
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
        """
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . For more information about creating IAM policies that control users\' access to resources based on tags, see `Supported Resource-Level Permissions for Amazon EC2 API Actions <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          tag = image.create_tags(
              DryRun=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. The ``value`` parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 
        
          - *(dict) --* 
        
            Describes a tag.
        
            - **Key** *(string) --* 
        
              The key of the tag.
        
              Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
              Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :rtype: list(:py:class:`ec2.Tag`)
        :returns: A list of Tag resources
        """
        pass

    def deregister(self, DryRun: bool = None):
        """
        
        When you deregister an Amazon EBS-backed AMI, it doesn\'t affect the snapshot that was created for the root volume of the instance during the AMI creation process. When you deregister an instance store-backed AMI, it doesn\'t affect the files that you uploaded to Amazon S3 when you created the AMI.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeregisterImage>`_
        
        **Request Syntax** 
        ::
        
          response = image.deregister(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeImageAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = image.describe_attribute(
              Attribute=\'description\'|\'kernel\'|\'ramdisk\'|\'launchPermission\'|\'productCodes\'|\'blockDeviceMapping\'|\'sriovNetSupport\',
              DryRun=True|False
          )
        :type Attribute: string
        :param Attribute: **[REQUIRED]** 
        
          The AMI attribute.
        
           **Note** : Depending on your account privileges, the ``blockDeviceMapping`` attribute may return a ``Client.AuthFailure`` error. If this happens, use  DescribeImages to get information about the block device mapping for the AMI.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'BlockDeviceMappings\': [
                    {
                        \'DeviceName\': \'string\',
                        \'VirtualName\': \'string\',
                        \'Ebs\': {
                            \'DeleteOnTermination\': True|False,
                            \'Iops\': 123,
                            \'SnapshotId\': \'string\',
                            \'VolumeSize\': 123,
                            \'VolumeType\': \'standard\'|\'io1\'|\'gp2\'|\'sc1\'|\'st1\',
                            \'Encrypted\': True|False,
                            \'KmsKeyId\': \'string\'
                        },
                        \'NoDevice\': \'string\'
                    },
                ],
                \'ImageId\': \'string\',
                \'LaunchPermissions\': [
                    {
                        \'Group\': \'all\',
                        \'UserId\': \'string\'
                    },
                ],
                \'ProductCodes\': [
                    {
                        \'ProductCodeId\': \'string\',
                        \'ProductCodeType\': \'devpay\'|\'marketplace\'
                    },
                ],
                \'Description\': {
                    \'Value\': \'string\'
                },
                \'KernelId\': {
                    \'Value\': \'string\'
                },
                \'RamdiskId\': {
                    \'Value\': \'string\'
                },
                \'SriovNetSupport\': {
                    \'Value\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Describes an image attribute.
        
            - **BlockDeviceMappings** *(list) --* 
        
              One or more block device mapping entries.
        
              - *(dict) --* 
        
                Describes a block device mapping.
        
                - **DeviceName** *(string) --* 
        
                  The device name (for example, ``/dev/sdh`` or ``xvdh`` ).
        
                - **VirtualName** *(string) --* 
        
                  The virtual device name (``ephemeral`` N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ``ephemeral0`` and ``ephemeral1`` . The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
        
                  NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect.
        
                  Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
        
                - **Ebs** *(dict) --* 
        
                  Parameters used to automatically set up EBS volumes when the instance is launched.
        
                  - **DeleteOnTermination** *(boolean) --* 
        
                    Indicates whether the EBS volume is deleted on instance termination.
        
                  - **Iops** *(integer) --* 
        
                    The number of I/O operations per second (IOPS) that the volume supports. For ``io1`` , this represents the number of IOPS that are provisioned for the volume. For ``gp2`` , this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see `Amazon EBS Volume Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
                    Constraint: Range is 100-20000 IOPS for ``io1`` volumes and 100-10000 IOPS for ``gp2`` volumes.
        
                    Condition: This parameter is required for requests to create ``io1`` volumes; it is not used in requests to create ``gp2`` , ``st1`` , ``sc1`` , or ``standard`` volumes.
        
                  - **SnapshotId** *(string) --* 
        
                    The ID of the snapshot.
        
                  - **VolumeSize** *(integer) --* 
        
                    The size of the volume, in GiB.
        
                    Constraints: 1-16384 for General Purpose SSD (``gp2`` ), 4-16384 for Provisioned IOPS SSD (``io1`` ), 500-16384 for Throughput Optimized HDD (``st1`` ), 500-16384 for Cold HDD (``sc1`` ), and 1-1024 for Magnetic (``standard`` ) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
        
                    Default: If you\'re creating the volume from a snapshot and don\'t specify a volume size, the default is the snapshot size.
        
                  - **VolumeType** *(string) --* 
        
                    The volume type: ``gp2`` , ``io1`` , ``st1`` , ``sc1`` , or ``standard`` .
        
                    Default: ``standard``  
        
                  - **Encrypted** *(boolean) --* 
        
                    Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. 
        
                    If you are creating a volume from a snapshot, you cannot specify an encryption value. This is because only blank volumes can be encrypted on creation. If you are creating a snapshot from an existing EBS volume, you cannot specify an encryption value that differs from that of the EBS volume. We recommend that you omit the encryption value from the block device mappings when creating an image from an instance.
        
                  - **KmsKeyId** *(string) --* 
        
                    Identifier (key ID, key alias, ID ARN, or alias ARN) for a user-managed CMK under which the EBS volume is encrypted.
        
                    This parameter is only supported on ``BlockDeviceMapping`` objects called by `RunInstances <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html>`__ , `RequestSpotFleet <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet.html>`__ , and `RequestSpotInstances <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html>`__ .
        
                - **NoDevice** *(string) --* 
        
                  Suppresses the specified device included in the block device mapping of the AMI.
        
            - **ImageId** *(string) --* 
        
              The ID of the AMI.
        
            - **LaunchPermissions** *(list) --* 
        
              One or more launch permissions.
        
              - *(dict) --* 
        
                Describes a launch permission.
        
                - **Group** *(string) --* 
        
                  The name of the group.
        
                - **UserId** *(string) --* 
        
                  The AWS account ID.
        
            - **ProductCodes** *(list) --* 
        
              One or more product codes.
        
              - *(dict) --* 
        
                Describes a product code.
        
                - **ProductCodeId** *(string) --* 
        
                  The product code.
        
                - **ProductCodeType** *(string) --* 
        
                  The type of product code.
        
            - **Description** *(dict) --* 
        
              A description for the AMI.
        
              - **Value** *(string) --* 
        
                The attribute value. The value is case-sensitive.
        
            - **KernelId** *(dict) --* 
        
              The kernel ID.
        
              - **Value** *(string) --* 
        
                The attribute value. The value is case-sensitive.
        
            - **RamdiskId** *(dict) --* 
        
              The RAM disk ID.
        
              - **Value** *(string) --* 
        
                The attribute value. The value is case-sensitive.
        
            - **SriovNetSupport** *(dict) --* 
        
              Indicates whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.
        
              - **Value** *(string) --* 
        
                The attribute value. The value is case-sensitive.
        
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          image.load()
        :returns: None
        """
        pass

    def modify_attribute(self, Attribute: str = None, Description: Dict = None, LaunchPermission: Dict = None, OperationType: str = None, ProductCodes: List = None, UserGroups: List = None, UserIds: List = None, Value: str = None, DryRun: bool = None):
        """
        
        AWS Marketplace product codes cannot be modified. Images with an AWS Marketplace product code cannot be made public.
        
        To enable the SriovNetSupport enhanced networking attribute of an image, enable SriovNetSupport on an instance and create an AMI from the instance.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyImageAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = image.modify_attribute(
              Attribute=\'string\',
              Description={
                  \'Value\': \'string\'
              },
              LaunchPermission={
                  \'Add\': [
                      {
                          \'Group\': \'all\',
                          \'UserId\': \'string\'
                      },
                  ],
                  \'Remove\': [
                      {
                          \'Group\': \'all\',
                          \'UserId\': \'string\'
                      },
                  ]
              },
              OperationType=\'add\'|\'remove\',
              ProductCodes=[
                  \'string\',
              ],
              UserGroups=[
                  \'string\',
              ],
              UserIds=[
                  \'string\',
              ],
              Value=\'string\',
              DryRun=True|False
          )
        :type Attribute: string
        :param Attribute: 
        
          The name of the attribute to modify. The valid values are ``description`` , ``launchPermission`` , and ``productCodes`` .
        
        :type Description: dict
        :param Description: 
        
          A new description for the AMI.
        
          - **Value** *(string) --* 
        
            The attribute value. The value is case-sensitive.
        
        :type LaunchPermission: dict
        :param LaunchPermission: 
        
          A new launch permission for the AMI.
        
          - **Add** *(list) --* 
        
            The AWS account ID to add to the list of launch permissions for the AMI.
        
            - *(dict) --* 
        
              Describes a launch permission.
        
              - **Group** *(string) --* 
        
                The name of the group.
        
              - **UserId** *(string) --* 
        
                The AWS account ID.
        
          - **Remove** *(list) --* 
        
            The AWS account ID to remove from the list of launch permissions for the AMI.
        
            - *(dict) --* 
        
              Describes a launch permission.
        
              - **Group** *(string) --* 
        
                The name of the group.
        
              - **UserId** *(string) --* 
        
                The AWS account ID.
        
        :type OperationType: string
        :param OperationType: 
        
          The operation type. This parameter can be used only when the ``Attribute`` parameter is ``launchPermission`` .
        
        :type ProductCodes: list
        :param ProductCodes: 
        
          One or more DevPay product codes. After you add a product code to an AMI, it can\'t be removed.
        
          - *(string) --* 
        
        :type UserGroups: list
        :param UserGroups: 
        
          One or more user groups. This parameter can be used only when the ``Attribute`` parameter is ``launchPermission`` .
        
          - *(string) --* 
        
        :type UserIds: list
        :param UserIds: 
        
          One or more AWS account IDs. This parameter can be used only when the ``Attribute`` parameter is ``launchPermission`` .
        
          - *(string) --* 
        
        :type Value: string
        :param Value: 
        
          The value of the attribute being modified. This parameter can be used only when the ``Attribute`` parameter is ``description`` or ``productCodes`` .
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          image.load()
        :returns: None
        """
        pass

    def reset_attribute(self, Attribute: str, DryRun: bool = None):
        """
        
        .. note::
        
          The productCodes attribute can\'t be reset.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ResetImageAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = image.reset_attribute(
              Attribute=\'launchPermission\',
              DryRun=True|False
          )
        :type Attribute: string
        :param Attribute: **[REQUIRED]** 
        
          The attribute to reset (currently you can only reset the launch permission attribute).
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def wait_until_exists(self, ExecutableUsers: List = None, Filters: List = None, Owners: List = None, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeImages>`_
        
        **Request Syntax** 
        ::
        
          image.wait_until_exists(
              ExecutableUsers=[
                  \'string\',
              ],
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              Owners=[
                  \'string\',
              ],
              DryRun=True|False
          )
        :type ExecutableUsers: list
        :param ExecutableUsers: 
        
          Scopes the images by users with explicit launch permissions. Specify an AWS account ID, ``self`` (the sender of the request), or ``all`` (public AMIs).
        
          - *(string) --* 
        
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``architecture`` - The image architecture (``i386`` | ``x86_64`` ). 
           
          * ``block-device-mapping.delete-on-termination`` - A Boolean value that indicates whether the Amazon EBS volume is deleted on instance termination. 
           
          * ``block-device-mapping.device-name`` - The device name specified in the block device mapping (for example, ``/dev/sdh`` or ``xvdh`` ). 
           
          * ``block-device-mapping.snapshot-id`` - The ID of the snapshot used for the EBS volume. 
           
          * ``block-device-mapping.volume-size`` - The volume size of the EBS volume, in GiB. 
           
          * ``block-device-mapping.volume-type`` - The volume type of the EBS volume (``gp2`` | ``io1`` | ``st1`` | ``sc1`` | ``standard`` ). 
           
          * ``description`` - The description of the image (provided during image creation). 
           
          * ``ena-support`` - A Boolean that indicates whether enhanced networking with ENA is enabled. 
           
          * ``hypervisor`` - The hypervisor type (``ovm`` | ``xen`` ). 
           
          * ``image-id`` - The ID of the image. 
           
          * ``image-type`` - The image type (``machine`` | ``kernel`` | ``ramdisk`` ). 
           
          * ``is-public`` - A Boolean that indicates whether the image is public. 
           
          * ``kernel-id`` - The kernel ID. 
           
          * ``manifest-location`` - The location of the image manifest. 
           
          * ``name`` - The name of the AMI (provided during image creation). 
           
          * ``owner-alias`` - String value from an Amazon-maintained list (``amazon`` | ``aws-marketplace`` | ``microsoft`` ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM console. 
           
          * ``owner-id`` - The AWS account ID of the image owner. 
           
          * ``platform`` - The platform. To only list Windows-based AMIs, use ``windows`` . 
           
          * ``product-code`` - The product code. 
           
          * ``product-code.type`` - The type of the product code (``devpay`` | ``marketplace`` ). 
           
          * ``ramdisk-id`` - The RAM disk ID. 
           
          * ``root-device-name`` - The device name of the root device volume (for example, ``/dev/sda1`` ). 
           
          * ``root-device-type`` - The type of the root device volume (``ebs`` | ``instance-store`` ). 
           
          * ``state`` - The state of the image (``available`` | ``pending`` | ``failed`` ). 
           
          * ``state-reason-code`` - The reason code for the state change. 
           
          * ``state-reason-message`` - The message for the state change. 
           
          * ``sriov-net-support`` - A value of ``simple`` indicates that enhanced networking with the Intel 82599 VF interface is enabled. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``virtualization-type`` - The virtualization type (``paravirtual`` | ``hvm`` ). 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type Owners: list
        :param Owners: 
        
          Filters the images by the owner. Specify an AWS account ID, ``self`` (owner is the sender of the request), or an AWS owner alias (valid values are ``amazon`` | ``aws-marketplace`` | ``microsoft`` ). Omitting this option returns all images for which you have launch permissions, regardless of ownership.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
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
        """
        
        After you\'ve linked an instance, you cannot change the VPC security groups that are associated with it. To change the security groups, you must first unlink the instance, and then link it again.
        
        Linking your instance to a VPC is sometimes referred to as *attaching* your instance.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AttachClassicLinkVpc>`_
        
        **Request Syntax** 
        ::
        
          response = instance.attach_classic_link_vpc(
              DryRun=True|False,
              Groups=[
                  \'string\',
              ],
              VpcId=\'string\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Groups: list
        :param Groups: **[REQUIRED]** 
        
          The ID of one or more of the VPC\'s security groups. You cannot specify security groups from a different VPC.
        
          - *(string) --* 
        
        :type VpcId: string
        :param VpcId: **[REQUIRED]** 
        
          The ID of a ClassicLink-enabled VPC.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Return\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Return** *(boolean) --* 
        
              Returns ``true`` if the request succeeds; otherwise, it returns an error.
        
        """
        pass

    def attach_volume(self, Device: str, VolumeId: str, DryRun: bool = None) -> Dict:
        """
        
        Encrypted EBS volumes may only be attached to instances that support Amazon EBS encryption. For more information, see `Amazon EBS Encryption <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        For a list of supported device names, see `Attaching an EBS Volume to an Instance <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html>`__ . Any device names that aren\'t reserved for instance store volumes can be used for EBS volumes. For more information, see `Amazon EC2 Instance Store <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        If a volume has an AWS Marketplace product code:
        
        * The volume can be attached only to a stopped instance. 
         
        * AWS Marketplace product codes are copied from the volume to the instance. 
         
        * You must be subscribed to the product. 
         
        * The instance type and operating system of the instance must support the product. For example, you can\'t detach a volume from a Windows instance and attach it to a Linux instance. 
         
        For more information about EBS volumes, see `Attaching Amazon EBS Volumes <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AttachVolume>`_
        
        **Request Syntax** 
        ::
        
          response = instance.attach_volume(
              Device=\'string\',
              VolumeId=\'string\',
              DryRun=True|False
          )
        :type Device: string
        :param Device: **[REQUIRED]** 
        
          The device name (for example, ``/dev/sdh`` or ``xvdh`` ).
        
        :type VolumeId: string
        :param VolumeId: **[REQUIRED]** 
        
          The ID of the EBS volume. The volume and instance must be within the same Availability Zone.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AttachTime\': datetime(2015, 1, 1),
                \'Device\': \'string\',
                \'InstanceId\': \'string\',
                \'State\': \'attaching\'|\'attached\'|\'detaching\'|\'detached\'|\'busy\',
                \'VolumeId\': \'string\',
                \'DeleteOnTermination\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Describes volume attachment details.
        
            - **AttachTime** *(datetime) --* 
        
              The time stamp when the attachment initiated.
        
            - **Device** *(string) --* 
        
              The device name.
        
            - **InstanceId** *(string) --* 
        
              The ID of the instance.
        
            - **State** *(string) --* 
        
              The attachment state of the volume.
        
            - **VolumeId** *(string) --* 
        
              The ID of the volume.
        
            - **DeleteOnTermination** *(boolean) --* 
        
              Indicates whether the EBS volume is deleted on instance termination.
        
        """
        pass

    def console_output(self, DryRun: bool = None, Latest: bool = None) -> Dict:
        """
        
        By default, the console output returns buffered information that was posted shortly after an instance transition state (start, stop, reboot, or terminate). This information is available for at least one hour after the most recent post. Only the most recent 64 KB of console output is available.
        
        You can optionally retrieve the latest serial console output at any time during the instance lifecycle. This option is supported on instance types that use the Nitro hypervisor.
        
        For more information, see `Instance Console Output <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-console.html#instance-console-console-output>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/GetConsoleOutput>`_
        
        **Request Syntax** 
        ::
        
          response = instance.console_output(
              DryRun=True|False,
              Latest=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Latest: boolean
        :param Latest: 
        
          When enabled, retrieves the latest console output for the instance.
        
          Default: disabled (``false`` )
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstanceId\': \'string\',
                \'Output\': \'string\',
                \'Timestamp\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of GetConsoleOutput.
        
            - **InstanceId** *(string) --* 
        
              The ID of the instance.
        
            - **Output** *(string) --* 
        
              The console output, base64-encoded. If you are using a command line tool, the tool decodes the output for you.
        
            - **Timestamp** *(datetime) --* 
        
              The time at which the output was last updated.
        
        """
        pass

    def create_image(self, Name: str, BlockDeviceMappings: List = None, Description: str = None, DryRun: bool = None, NoReboot: bool = None) -> 'Image':
        """
        
        If you customized your instance with instance store volumes or EBS volumes in addition to the root device volume, the new AMI contains block device mapping information for those volumes. When you launch an instance from this new AMI, the instance automatically launches with those additional volumes.
        
        For more information, see `Creating Amazon EBS-Backed Linux AMIs <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateImage>`_
        
        **Request Syntax** 
        ::
        
          image = instance.create_image(
              BlockDeviceMappings=[
                  {
                      \'DeviceName\': \'string\',
                      \'VirtualName\': \'string\',
                      \'Ebs\': {
                          \'DeleteOnTermination\': True|False,
                          \'Iops\': 123,
                          \'SnapshotId\': \'string\',
                          \'VolumeSize\': 123,
                          \'VolumeType\': \'standard\'|\'io1\'|\'gp2\'|\'sc1\'|\'st1\',
                          \'Encrypted\': True|False,
                          \'KmsKeyId\': \'string\'
                      },
                      \'NoDevice\': \'string\'
                  },
              ],
              Description=\'string\',
              DryRun=True|False,
              Name=\'string\',
              NoReboot=True|False
          )
        :type BlockDeviceMappings: list
        :param BlockDeviceMappings: 
        
          Information about one or more block device mappings. This parameter cannot be used to modify the encryption status of existing volumes or snapshots. To create an AMI with encrypted snapshots, use the  CopyImage action.
        
          - *(dict) --* 
        
            Describes a block device mapping.
        
            - **DeviceName** *(string) --* 
        
              The device name (for example, ``/dev/sdh`` or ``xvdh`` ).
        
            - **VirtualName** *(string) --* 
        
              The virtual device name (``ephemeral`` N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ``ephemeral0`` and ``ephemeral1`` . The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
        
              NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect.
        
              Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
        
            - **Ebs** *(dict) --* 
        
              Parameters used to automatically set up EBS volumes when the instance is launched.
        
              - **DeleteOnTermination** *(boolean) --* 
        
                Indicates whether the EBS volume is deleted on instance termination.
        
              - **Iops** *(integer) --* 
        
                The number of I/O operations per second (IOPS) that the volume supports. For ``io1`` , this represents the number of IOPS that are provisioned for the volume. For ``gp2`` , this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see `Amazon EBS Volume Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
                Constraint: Range is 100-20000 IOPS for ``io1`` volumes and 100-10000 IOPS for ``gp2`` volumes.
        
                Condition: This parameter is required for requests to create ``io1`` volumes; it is not used in requests to create ``gp2`` , ``st1`` , ``sc1`` , or ``standard`` volumes.
        
              - **SnapshotId** *(string) --* 
        
                The ID of the snapshot.
        
              - **VolumeSize** *(integer) --* 
        
                The size of the volume, in GiB.
        
                Constraints: 1-16384 for General Purpose SSD (``gp2`` ), 4-16384 for Provisioned IOPS SSD (``io1`` ), 500-16384 for Throughput Optimized HDD (``st1`` ), 500-16384 for Cold HDD (``sc1`` ), and 1-1024 for Magnetic (``standard`` ) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
        
                Default: If you\'re creating the volume from a snapshot and don\'t specify a volume size, the default is the snapshot size.
        
              - **VolumeType** *(string) --* 
        
                The volume type: ``gp2`` , ``io1`` , ``st1`` , ``sc1`` , or ``standard`` .
        
                Default: ``standard``  
        
              - **Encrypted** *(boolean) --* 
        
                Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. 
        
                If you are creating a volume from a snapshot, you cannot specify an encryption value. This is because only blank volumes can be encrypted on creation. If you are creating a snapshot from an existing EBS volume, you cannot specify an encryption value that differs from that of the EBS volume. We recommend that you omit the encryption value from the block device mappings when creating an image from an instance.
        
              - **KmsKeyId** *(string) --* 
        
                Identifier (key ID, key alias, ID ARN, or alias ARN) for a user-managed CMK under which the EBS volume is encrypted.
        
                This parameter is only supported on ``BlockDeviceMapping`` objects called by `RunInstances <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html>`__ , `RequestSpotFleet <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet.html>`__ , and `RequestSpotInstances <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html>`__ .
        
            - **NoDevice** *(string) --* 
        
              Suppresses the specified device included in the block device mapping of the AMI.
        
        :type Description: string
        :param Description: 
        
          A description for the new image.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          A name for the new image.
        
          Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes (\'), at-signs (@), or underscores(_)
        
        :type NoReboot: boolean
        :param NoReboot: 
        
          By default, Amazon EC2 attempts to shut down and reboot the instance before creating the image. If the \'No Reboot\' option is set, Amazon EC2 doesn\'t shut down the instance before creating the image. When this option is used, file system integrity on the created image can\'t be guaranteed.
        
        :rtype: :py:class:`ec2.Image`
        :returns: Image resource
        """
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        """
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . For more information about creating IAM policies that control users\' access to resources based on tags, see `Supported Resource-Level Permissions for Amazon EC2 API Actions <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          tag = instance.create_tags(
              DryRun=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. The ``value`` parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 
        
          - *(dict) --* 
        
            Describes a tag.
        
            - **Key** *(string) --* 
        
              The key of the tag.
        
              Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
              Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :rtype: list(:py:class:`ec2.Tag`)
        :returns: A list of Tag resources
        """
        pass

    def delete_tags(self, DryRun: bool = None, Tags: List = None):
        """
        
        To list the current tags, use  DescribeTags . For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteTags>`_
        
        **Request Syntax** 
        ::
        
          response = instance.delete_tags(
              DryRun=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Tags: list
        :param Tags: 
        
          One or more tags to delete. Specify a tag key and an optional tag value to delete specific tags. If you specify a tag key without a tag value, we delete any tag with this key regardless of its value. If you specify a tag key with an empty string as the tag value, we delete the tag only if its value is an empty string.
        
          If you omit this parameter, we delete all user-defined tags for the specified resources. We do not delete AWS-generated tags (tags that have the ``aws:`` prefix).
        
          - *(dict) --* 
        
            Describes a tag.
        
            - **Key** *(string) --* 
        
              The key of the tag.
        
              Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
              Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :returns: None
        """
        pass

    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstanceAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = instance.describe_attribute(
              Attribute=\'instanceType\'|\'kernel\'|\'ramdisk\'|\'userData\'|\'disableApiTermination\'|\'instanceInitiatedShutdownBehavior\'|\'rootDeviceName\'|\'blockDeviceMapping\'|\'productCodes\'|\'sourceDestCheck\'|\'groupSet\'|\'ebsOptimized\'|\'sriovNetSupport\'|\'enaSupport\',
              DryRun=True|False,
              
          )
        :type Attribute: string
        :param Attribute: **[REQUIRED]** 
        
          The instance attribute.
        
          Note: The ``enaSupport`` attribute is not supported at this time.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Groups\': [
                    {
                        \'GroupName\': \'string\',
                        \'GroupId\': \'string\'
                    },
                ],
                \'BlockDeviceMappings\': [
                    {
                        \'DeviceName\': \'string\',
                        \'Ebs\': {
                            \'AttachTime\': datetime(2015, 1, 1),
                            \'DeleteOnTermination\': True|False,
                            \'Status\': \'attaching\'|\'attached\'|\'detaching\'|\'detached\',
                            \'VolumeId\': \'string\'
                        }
                    },
                ],
                \'DisableApiTermination\': {
                    \'Value\': True|False
                },
                \'EnaSupport\': {
                    \'Value\': True|False
                },
                \'EbsOptimized\': {
                    \'Value\': True|False
                },
                \'InstanceId\': \'string\',
                \'InstanceInitiatedShutdownBehavior\': {
                    \'Value\': \'string\'
                },
                \'InstanceType\': {
                    \'Value\': \'string\'
                },
                \'KernelId\': {
                    \'Value\': \'string\'
                },
                \'ProductCodes\': [
                    {
                        \'ProductCodeId\': \'string\',
                        \'ProductCodeType\': \'devpay\'|\'marketplace\'
                    },
                ],
                \'RamdiskId\': {
                    \'Value\': \'string\'
                },
                \'RootDeviceName\': {
                    \'Value\': \'string\'
                },
                \'SourceDestCheck\': {
                    \'Value\': True|False
                },
                \'SriovNetSupport\': {
                    \'Value\': \'string\'
                },
                \'UserData\': {
                    \'Value\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Describes an instance attribute.
        
            - **Groups** *(list) --* 
        
              The security groups associated with the instance.
        
              - *(dict) --* 
        
                Describes a security group.
        
                - **GroupName** *(string) --* 
        
                  The name of the security group.
        
                - **GroupId** *(string) --* 
        
                  The ID of the security group.
        
            - **BlockDeviceMappings** *(list) --* 
        
              The block device mapping of the instance.
        
              - *(dict) --* 
        
                Describes a block device mapping.
        
                - **DeviceName** *(string) --* 
        
                  The device name (for example, ``/dev/sdh`` or ``xvdh`` ).
        
                - **Ebs** *(dict) --* 
        
                  Parameters used to automatically set up EBS volumes when the instance is launched.
        
                  - **AttachTime** *(datetime) --* 
        
                    The time stamp when the attachment initiated.
        
                  - **DeleteOnTermination** *(boolean) --* 
        
                    Indicates whether the volume is deleted on instance termination.
        
                  - **Status** *(string) --* 
        
                    The attachment state.
        
                  - **VolumeId** *(string) --* 
        
                    The ID of the EBS volume.
        
            - **DisableApiTermination** *(dict) --* 
        
              If the value is ``true`` , you can\'t terminate the instance through the Amazon EC2 console, CLI, or API; otherwise, you can.
        
              - **Value** *(boolean) --* 
        
                The attribute value. The valid values are ``true`` or ``false`` .
        
            - **EnaSupport** *(dict) --* 
        
              Indicates whether enhanced networking with ENA is enabled.
        
              - **Value** *(boolean) --* 
        
                The attribute value. The valid values are ``true`` or ``false`` .
        
            - **EbsOptimized** *(dict) --* 
        
              Indicates whether the instance is optimized for Amazon EBS I/O.
        
              - **Value** *(boolean) --* 
        
                The attribute value. The valid values are ``true`` or ``false`` .
        
            - **InstanceId** *(string) --* 
        
              The ID of the instance.
        
            - **InstanceInitiatedShutdownBehavior** *(dict) --* 
        
              Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
        
              - **Value** *(string) --* 
        
                The attribute value. The value is case-sensitive.
        
            - **InstanceType** *(dict) --* 
        
              The instance type.
        
              - **Value** *(string) --* 
        
                The attribute value. The value is case-sensitive.
        
            - **KernelId** *(dict) --* 
        
              The kernel ID.
        
              - **Value** *(string) --* 
        
                The attribute value. The value is case-sensitive.
        
            - **ProductCodes** *(list) --* 
        
              A list of product codes.
        
              - *(dict) --* 
        
                Describes a product code.
        
                - **ProductCodeId** *(string) --* 
        
                  The product code.
        
                - **ProductCodeType** *(string) --* 
        
                  The type of product code.
        
            - **RamdiskId** *(dict) --* 
        
              The RAM disk ID.
        
              - **Value** *(string) --* 
        
                The attribute value. The value is case-sensitive.
        
            - **RootDeviceName** *(dict) --* 
        
              The device name of the root device volume (for example, ``/dev/sda1`` ).
        
              - **Value** *(string) --* 
        
                The attribute value. The value is case-sensitive.
        
            - **SourceDestCheck** *(dict) --* 
        
              Indicates whether source/destination checking is enabled. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. This value must be ``false`` for a NAT instance to perform NAT.
        
              - **Value** *(boolean) --* 
        
                The attribute value. The valid values are ``true`` or ``false`` .
        
            - **SriovNetSupport** *(dict) --* 
        
              Indicates whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.
        
              - **Value** *(string) --* 
        
                The attribute value. The value is case-sensitive.
        
            - **UserData** *(dict) --* 
        
              The user data.
        
              - **Value** *(string) --* 
        
                The attribute value. The value is case-sensitive.
        
        """
        pass

    def detach_classic_link_vpc(self, VpcId: str, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DetachClassicLinkVpc>`_
        
        **Request Syntax** 
        ::
        
          response = instance.detach_classic_link_vpc(
              DryRun=True|False,
              VpcId=\'string\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type VpcId: string
        :param VpcId: **[REQUIRED]** 
        
          The ID of the VPC to which the instance is linked.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Return\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Return** *(boolean) --* 
        
              Returns ``true`` if the request succeeds; otherwise, it returns an error.
        
        """
        pass

    def detach_volume(self, VolumeId: str, Device: str = None, Force: bool = None, DryRun: bool = None) -> Dict:
        """
        
        When a volume with an AWS Marketplace product code is detached from an instance, the product code is no longer associated with the instance.
        
        For more information, see `Detaching an Amazon EBS Volume <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-detaching-volume.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DetachVolume>`_
        
        **Request Syntax** 
        ::
        
          response = instance.detach_volume(
              Device=\'string\',
              Force=True|False,
              VolumeId=\'string\',
              DryRun=True|False
          )
        :type Device: string
        :param Device: 
        
          The device name.
        
        :type Force: boolean
        :param Force: 
        
          Forces detachment if the previous detachment attempt did not occur cleanly (for example, logging into an instance, unmounting the volume, and detaching normally). This option can lead to data loss or a corrupted file system. Use this option only as a last resort to detach a volume from a failed instance. The instance won\'t have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures.
        
        :type VolumeId: string
        :param VolumeId: **[REQUIRED]** 
        
          The ID of the volume.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AttachTime\': datetime(2015, 1, 1),
                \'Device\': \'string\',
                \'InstanceId\': \'string\',
                \'State\': \'attaching\'|\'attached\'|\'detaching\'|\'detached\'|\'busy\',
                \'VolumeId\': \'string\',
                \'DeleteOnTermination\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Describes volume attachment details.
        
            - **AttachTime** *(datetime) --* 
        
              The time stamp when the attachment initiated.
        
            - **Device** *(string) --* 
        
              The device name.
        
            - **InstanceId** *(string) --* 
        
              The ID of the instance.
        
            - **State** *(string) --* 
        
              The attachment state of the volume.
        
            - **VolumeId** *(string) --* 
        
              The ID of the volume.
        
            - **DeleteOnTermination** *(boolean) --* 
        
              Indicates whether the EBS volume is deleted on instance termination.
        
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          instance.load()
        :returns: None
        """
        pass

    def modify_attribute(self, SourceDestCheck: Dict = None, Attribute: str = None, BlockDeviceMappings: List = None, DisableApiTermination: Dict = None, DryRun: bool = None, EbsOptimized: Dict = None, EnaSupport: Dict = None, Groups: List = None, InstanceInitiatedShutdownBehavior: Dict = None, InstanceType: Dict = None, Kernel: Dict = None, Ramdisk: Dict = None, SriovNetSupport: Dict = None, UserData: Dict = None, Value: str = None):
        """
        
         **Note:** Using this action to change the security groups associated with an elastic network interface (ENI) attached to an instance in a VPC can result in an error if the instance has more than one ENI. To change the security groups associated with an ENI attached to an instance that has multiple ENIs, we recommend that you use the  ModifyNetworkInterfaceAttribute action.
        
        To modify some attributes, the instance must be stopped. For more information, see `Modifying Attributes of a Stopped Instance <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_ChangingAttributesWhileInstanceStopped.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyInstanceAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = instance.modify_attribute(
              SourceDestCheck={
                  \'Value\': True|False
              },
              Attribute=\'instanceType\'|\'kernel\'|\'ramdisk\'|\'userData\'|\'disableApiTermination\'|\'instanceInitiatedShutdownBehavior\'|\'rootDeviceName\'|\'blockDeviceMapping\'|\'productCodes\'|\'sourceDestCheck\'|\'groupSet\'|\'ebsOptimized\'|\'sriovNetSupport\'|\'enaSupport\',
              BlockDeviceMappings=[
                  {
                      \'DeviceName\': \'string\',
                      \'Ebs\': {
                          \'DeleteOnTermination\': True|False,
                          \'VolumeId\': \'string\'
                      },
                      \'NoDevice\': \'string\',
                      \'VirtualName\': \'string\'
                  },
              ],
              DisableApiTermination={
                  \'Value\': True|False
              },
              DryRun=True|False,
              EbsOptimized={
                  \'Value\': True|False
              },
              EnaSupport={
                  \'Value\': True|False
              },
              Groups=[
                  \'string\',
              ],
              InstanceInitiatedShutdownBehavior={
                  \'Value\': \'string\'
              },
              InstanceType={
                  \'Value\': \'string\'
              },
              Kernel={
                  \'Value\': \'string\'
              },
              Ramdisk={
                  \'Value\': \'string\'
              },
              SriovNetSupport={
                  \'Value\': \'string\'
              },
              UserData={
                  \'Value\': b\'bytes\'
              },
              Value=\'string\'
          )
        :type SourceDestCheck: dict
        :param SourceDestCheck: 
        
          Specifies whether source/destination checking is enabled. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. This value must be ``false`` for a NAT instance to perform NAT.
        
          - **Value** *(boolean) --* 
        
            The attribute value. The valid values are ``true`` or ``false`` .
        
        :type Attribute: string
        :param Attribute: 
        
          The name of the attribute.
        
        :type BlockDeviceMappings: list
        :param BlockDeviceMappings: 
        
          Modifies the ``DeleteOnTermination`` attribute for volumes that are currently attached. The volume must be owned by the caller. If no value is specified for ``DeleteOnTermination`` , the default is ``true`` and the volume is deleted when the instance is terminated.
        
          To add instance store volumes to an Amazon EBS-backed instance, you must add them when you launch the instance. For more information, see `Updating the Block Device Mapping when Launching an Instance <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html#Using_OverridingAMIBDM>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
          - *(dict) --* 
        
            Describes a block device mapping entry.
        
            - **DeviceName** *(string) --* 
        
              The device name (for example, ``/dev/sdh`` or ``xvdh`` ).
        
            - **Ebs** *(dict) --* 
        
              Parameters used to automatically set up EBS volumes when the instance is launched.
        
              - **DeleteOnTermination** *(boolean) --* 
        
                Indicates whether the volume is deleted on instance termination.
        
              - **VolumeId** *(string) --* 
        
                The ID of the EBS volume.
        
            - **NoDevice** *(string) --* 
        
              suppress the specified device included in the block device mapping.
        
            - **VirtualName** *(string) --* 
        
              The virtual device name.
        
        :type DisableApiTermination: dict
        :param DisableApiTermination: 
        
          If the value is ``true`` , you can\'t terminate the instance using the Amazon EC2 console, CLI, or API; otherwise, you can. You cannot use this parameter for Spot Instances.
        
          - **Value** *(boolean) --* 
        
            The attribute value. The valid values are ``true`` or ``false`` .
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type EbsOptimized: dict
        :param EbsOptimized: 
        
          Specifies whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn\'t available with all instance types. Additional usage charges apply when using an EBS Optimized instance.
        
          - **Value** *(boolean) --* 
        
            The attribute value. The valid values are ``true`` or ``false`` .
        
        :type EnaSupport: dict
        :param EnaSupport: 
        
          Set to ``true`` to enable enhanced networking with ENA for the instance.
        
          This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.
        
          - **Value** *(boolean) --* 
        
            The attribute value. The valid values are ``true`` or ``false`` .
        
        :type Groups: list
        :param Groups: 
        
          [EC2-VPC] Changes the security groups of the instance. You must specify at least one security group, even if it\'s just the default security group for the VPC. You must specify the security group ID, not the security group name.
        
          - *(string) --* 
        
        :type InstanceInitiatedShutdownBehavior: dict
        :param InstanceInitiatedShutdownBehavior: 
        
          Specifies whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
        
          - **Value** *(string) --* 
        
            The attribute value. The value is case-sensitive.
        
        :type InstanceType: dict
        :param InstanceType: 
        
          Changes the instance type to the specified value. For more information, see `Instance Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`__ . If the instance type is not valid, the error returned is ``InvalidInstanceAttributeValue`` .
        
          - **Value** *(string) --* 
        
            The attribute value. The value is case-sensitive.
        
        :type Kernel: dict
        :param Kernel: 
        
          Changes the instance\'s kernel to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see `PV-GRUB <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedKernels.html>`__ .
        
          - **Value** *(string) --* 
        
            The attribute value. The value is case-sensitive.
        
        :type Ramdisk: dict
        :param Ramdisk: 
        
          Changes the instance\'s RAM disk to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see `PV-GRUB <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedKernels.html>`__ .
        
          - **Value** *(string) --* 
        
            The attribute value. The value is case-sensitive.
        
        :type SriovNetSupport: dict
        :param SriovNetSupport: 
        
          Set to ``simple`` to enable enhanced networking with the Intel 82599 Virtual Function interface for the instance.
        
          There is no way to disable enhanced networking with the Intel 82599 Virtual Function interface at this time.
        
          This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.
        
          - **Value** *(string) --* 
        
            The attribute value. The value is case-sensitive.
        
        :type UserData: dict
        :param UserData: 
        
          Changes the instance\'s user data to the specified value. If you are using an AWS SDK or command line tool, base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide base64-encoded text.
        
          - **Value** *(bytes) --* 
        
        :type Value: string
        :param Value: 
        
          A new value for the attribute. Use only with the ``kernel`` , ``ramdisk`` , ``userData`` , ``disableApiTermination`` , or ``instanceInitiatedShutdownBehavior`` attribute.
        
        :returns: None
        """
        pass

    def monitor(self, DryRun: bool = None) -> Dict:
        """
        
        To disable detailed monitoring, see .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/MonitorInstances>`_
        
        **Request Syntax** 
        ::
        
          response = instance.monitor(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstanceMonitorings\': [
                    {
                        \'InstanceId\': \'string\',
                        \'Monitoring\': {
                            \'State\': \'disabled\'|\'disabling\'|\'enabled\'|\'pending\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of MonitorInstances.
        
            - **InstanceMonitorings** *(list) --* 
        
              The monitoring information.
        
              - *(dict) --* 
        
                Describes the monitoring of an instance.
        
                - **InstanceId** *(string) --* 
        
                  The ID of the instance.
        
                - **Monitoring** *(dict) --* 
        
                  The monitoring for the instance.
        
                  - **State** *(string) --* 
        
                    Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
        
        """
        pass

    def password_data(self, DryRun: bool = None) -> Dict:
        """
        
        The Windows password is generated at boot by the ``EC2Config`` service or ``EC2Launch`` scripts (Windows Server 2016 and later). This usually only happens the first time an instance is launched. For more information, see `EC2Config <http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/UsingConfig_WinAMI.html>`__ and `EC2Launch <http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2launch.html>`__ in the Amazon Elastic Compute Cloud User Guide.
        
        For the ``EC2Config`` service, the password is not generated for rebundled AMIs unless ``Ec2SetPassword`` is enabled before bundling.
        
        The password is encrypted using the key pair that you specified when you launched the instance. You must provide the corresponding key pair file.
        
        When you launch an instance, password generation and encryption may take a few minutes. If you try to retrieve the password before it\'s available, the output returns an empty string. We recommend that you wait up to 15 minutes after launching an instance before trying to retrieve the generated password.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/GetPasswordData>`_
        
        **Request Syntax** 
        ::
        
          response = instance.password_data(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstanceId\': \'string\',
                \'PasswordData\': \'string\',
                \'Timestamp\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of GetPasswordData.
        
            - **InstanceId** *(string) --* 
        
              The ID of the Windows instance.
        
            - **PasswordData** *(string) --* 
        
              The password of the instance. Returns an empty string if the password is not available.
        
            - **Timestamp** *(datetime) --* 
        
              The time the data was last updated.
        
        """
        pass

    def reboot(self, DryRun: bool = None):
        """
        
        If an instance does not cleanly shut down within four minutes, Amazon EC2 performs a hard reboot.
        
        For more information about troubleshooting, see `Getting Console Output and Rebooting Instances <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-console.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/RebootInstances>`_
        
        **Request Syntax** 
        ::
        
          response = instance.reboot(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          instance.load()
        :returns: None
        """
        pass

    def report_status(self, ReasonCodes: List, Status: str, Description: str = None, DryRun: bool = None, EndTime: datetime = None, StartTime: datetime = None):
        """
        
        Use of this action does not change the value returned by  DescribeInstanceStatus .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ReportInstanceStatus>`_
        
        **Request Syntax** 
        ::
        
          response = instance.report_status(
              Description=\'string\',
              DryRun=True|False,
              EndTime=datetime(2015, 1, 1),
              ReasonCodes=[
                  \'instance-stuck-in-state\'|\'unresponsive\'|\'not-accepting-credentials\'|\'password-not-available\'|\'performance-network\'|\'performance-instance-store\'|\'performance-ebs-volume\'|\'performance-other\'|\'other\',
              ],
              StartTime=datetime(2015, 1, 1),
              Status=\'ok\'|\'impaired\'
          )
        :type Description: string
        :param Description: 
        
          Descriptive text about the health state of your instance.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type EndTime: datetime
        :param EndTime: 
        
          The time at which the reported instance health state ended.
        
        :type ReasonCodes: list
        :param ReasonCodes: **[REQUIRED]** 
        
          One or more reason codes that describe the health state of your instance.
        
          * ``instance-stuck-in-state`` : My instance is stuck in a state. 
           
          * ``unresponsive`` : My instance is unresponsive. 
           
          * ``not-accepting-credentials`` : My instance is not accepting my credentials. 
           
          * ``password-not-available`` : A password is not available for my instance. 
           
          * ``performance-network`` : My instance is experiencing performance problems that I believe are network related. 
           
          * ``performance-instance-store`` : My instance is experiencing performance problems that I believe are related to the instance stores. 
           
          * ``performance-ebs-volume`` : My instance is experiencing performance problems that I believe are related to an EBS volume. 
           
          * ``performance-other`` : My instance is experiencing performance problems. 
           
          * ``other`` : [explain using the description parameter] 
           
          - *(string) --* 
        
        :type StartTime: datetime
        :param StartTime: 
        
          The time at which the reported instance health state began.
        
        :type Status: string
        :param Status: **[REQUIRED]** 
        
          The status of all instances listed.
        
        :returns: None
        """
        pass

    def reset_attribute(self, Attribute: str, DryRun: bool = None):
        """
        
        The ``sourceDestCheck`` attribute controls whether source/destination checking is enabled. The default value is ``true`` , which means checking is enabled. This value must be ``false`` for a NAT instance to perform NAT. For more information, see `NAT Instances <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ResetInstanceAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = instance.reset_attribute(
              Attribute=\'instanceType\'|\'kernel\'|\'ramdisk\'|\'userData\'|\'disableApiTermination\'|\'instanceInitiatedShutdownBehavior\'|\'rootDeviceName\'|\'blockDeviceMapping\'|\'productCodes\'|\'sourceDestCheck\'|\'groupSet\'|\'ebsOptimized\'|\'sriovNetSupport\'|\'enaSupport\',
              DryRun=True|False,
              
          )
        :type Attribute: string
        :param Attribute: **[REQUIRED]** 
        
          The attribute to reset.
        
          .. warning::
        
            You can only reset the following attributes: ``kernel`` | ``ramdisk`` | ``sourceDestCheck`` . To change an instance attribute, use  ModifyInstanceAttribute .
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def reset_kernel(self, DryRun: bool = None):
        """
        
        The ``sourceDestCheck`` attribute controls whether source/destination checking is enabled. The default value is ``true`` , which means checking is enabled. This value must be ``false`` for a NAT instance to perform NAT. For more information, see `NAT Instances <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ResetInstanceAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = instance.reset_kernel(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def reset_ramdisk(self, DryRun: bool = None):
        """
        
        The ``sourceDestCheck`` attribute controls whether source/destination checking is enabled. The default value is ``true`` , which means checking is enabled. This value must be ``false`` for a NAT instance to perform NAT. For more information, see `NAT Instances <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ResetInstanceAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = instance.reset_ramdisk(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def reset_source_dest_check(self, DryRun: bool = None):
        """
        
        The ``sourceDestCheck`` attribute controls whether source/destination checking is enabled. The default value is ``true`` , which means checking is enabled. This value must be ``false`` for a NAT instance to perform NAT. For more information, see `NAT Instances <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ResetInstanceAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = instance.reset_source_dest_check(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def start(self, AdditionalInfo: str = None, DryRun: bool = None) -> Dict:
        """
        
        Instances that use Amazon EBS volumes as their root devices can be quickly stopped and started. When an instance is stopped, the compute resources are released and you are not billed for instance usage. However, your root partition Amazon EBS volume remains and continues to persist your data, and you are charged for Amazon EBS volume usage. You can restart your instance at any time. Every time you start your Windows instance, Amazon EC2 charges you for a full instance hour. If you stop and restart your Windows instance, a new instance hour begins and Amazon EC2 charges you for another full instance hour even if you are still within the same 60-minute period when it was stopped. Every time you start your Linux instance, Amazon EC2 charges a one-minute minimum for instance usage, and thereafter charges per second for instance usage.
        
        Before stopping an instance, make sure it is in a state from which it can be restarted. Stopping an instance does not preserve data stored in RAM.
        
        Performing this operation on an instance that uses an instance store as its root device returns an error.
        
        For more information, see `Stopping Instances <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/StartInstances>`_
        
        **Request Syntax** 
        ::
        
          response = instance.start(
              AdditionalInfo=\'string\',
              DryRun=True|False
          )
        :type AdditionalInfo: string
        :param AdditionalInfo: 
        
          Reserved.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StartingInstances\': [
                    {
                        \'CurrentState\': {
                            \'Code\': 123,
                            \'Name\': \'pending\'|\'running\'|\'shutting-down\'|\'terminated\'|\'stopping\'|\'stopped\'
                        },
                        \'InstanceId\': \'string\',
                        \'PreviousState\': {
                            \'Code\': 123,
                            \'Name\': \'pending\'|\'running\'|\'shutting-down\'|\'terminated\'|\'stopping\'|\'stopped\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of StartInstances.
        
            - **StartingInstances** *(list) --* 
        
              Information about one or more started instances.
        
              - *(dict) --* 
        
                Describes an instance state change.
        
                - **CurrentState** *(dict) --* 
        
                  The current state of the instance.
        
                  - **Code** *(integer) --* 
        
                    The low byte represents the state. The high byte is used for internal purposes and should be ignored.
        
                    * ``0`` : ``pending``   
                     
                    * ``16`` : ``running``   
                     
                    * ``32`` : ``shutting-down``   
                     
                    * ``48`` : ``terminated``   
                     
                    * ``64`` : ``stopping``   
                     
                    * ``80`` : ``stopped``   
                     
                  - **Name** *(string) --* 
        
                    The current state of the instance.
        
                - **InstanceId** *(string) --* 
        
                  The ID of the instance.
        
                - **PreviousState** *(dict) --* 
        
                  The previous state of the instance.
        
                  - **Code** *(integer) --* 
        
                    The low byte represents the state. The high byte is used for internal purposes and should be ignored.
        
                    * ``0`` : ``pending``   
                     
                    * ``16`` : ``running``   
                     
                    * ``32`` : ``shutting-down``   
                     
                    * ``48`` : ``terminated``   
                     
                    * ``64`` : ``stopping``   
                     
                    * ``80`` : ``stopped``   
                     
                  - **Name** *(string) --* 
        
                    The current state of the instance.
        
        """
        pass

    def stop(self, DryRun: bool = None, Force: bool = None) -> Dict:
        """
        
        We don\'t charge usage for a stopped instance, or data transfer fees; however, your root partition Amazon EBS volume remains and continues to persist your data, and you are charged for Amazon EBS volume usage. Every time you start your Windows instance, Amazon EC2 charges you for a full instance hour. If you stop and restart your Windows instance, a new instance hour begins and Amazon EC2 charges you for another full instance hour even if you are still within the same 60-minute period when it was stopped. Every time you start your Linux instance, Amazon EC2 charges a one-minute minimum for instance usage, and thereafter charges per second for instance usage.
        
        You can\'t start or stop Spot Instances, and you can\'t stop instance store-backed instances.
        
        When you stop an instance, we shut it down. You can restart your instance at any time. Before stopping an instance, make sure it is in a state from which it can be restarted. Stopping an instance does not preserve data stored in RAM.
        
        Stopping an instance is different to rebooting or terminating it. For example, when you stop an instance, the root device and any other devices attached to the instance persist. When you terminate an instance, the root device and any other devices attached during the instance launch are automatically deleted. For more information about the differences between rebooting, stopping, and terminating instances, see `Instance Lifecycle <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        When you stop an instance, we attempt to shut it down forcibly after a short while. If your instance appears stuck in the stopping state after a period of time, there may be an issue with the underlying host computer. For more information, see `Troubleshooting Stopping Your Instance <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesStopping.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/StopInstances>`_
        
        **Request Syntax** 
        ::
        
          response = instance.stop(
              DryRun=True|False,
              Force=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Force: boolean
        :param Force: 
        
          Forces the instances to stop. The instances do not have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures. This option is not recommended for Windows instances.
        
          Default: ``false``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StoppingInstances\': [
                    {
                        \'CurrentState\': {
                            \'Code\': 123,
                            \'Name\': \'pending\'|\'running\'|\'shutting-down\'|\'terminated\'|\'stopping\'|\'stopped\'
                        },
                        \'InstanceId\': \'string\',
                        \'PreviousState\': {
                            \'Code\': 123,
                            \'Name\': \'pending\'|\'running\'|\'shutting-down\'|\'terminated\'|\'stopping\'|\'stopped\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of StopInstances.
        
            - **StoppingInstances** *(list) --* 
        
              Information about one or more stopped instances.
        
              - *(dict) --* 
        
                Describes an instance state change.
        
                - **CurrentState** *(dict) --* 
        
                  The current state of the instance.
        
                  - **Code** *(integer) --* 
        
                    The low byte represents the state. The high byte is used for internal purposes and should be ignored.
        
                    * ``0`` : ``pending``   
                     
                    * ``16`` : ``running``   
                     
                    * ``32`` : ``shutting-down``   
                     
                    * ``48`` : ``terminated``   
                     
                    * ``64`` : ``stopping``   
                     
                    * ``80`` : ``stopped``   
                     
                  - **Name** *(string) --* 
        
                    The current state of the instance.
        
                - **InstanceId** *(string) --* 
        
                  The ID of the instance.
        
                - **PreviousState** *(dict) --* 
        
                  The previous state of the instance.
        
                  - **Code** *(integer) --* 
        
                    The low byte represents the state. The high byte is used for internal purposes and should be ignored.
        
                    * ``0`` : ``pending``   
                     
                    * ``16`` : ``running``   
                     
                    * ``32`` : ``shutting-down``   
                     
                    * ``48`` : ``terminated``   
                     
                    * ``64`` : ``stopping``   
                     
                    * ``80`` : ``stopped``   
                     
                  - **Name** *(string) --* 
        
                    The current state of the instance.
        
        """
        pass

    def terminate(self, DryRun: bool = None) -> Dict:
        """
        
        If you specify multiple instances and the request fails (for example, because of a single incorrect instance ID), none of the instances are terminated.
        
        Terminated instances remain visible after termination (for approximately one hour).
        
        By default, Amazon EC2 deletes all EBS volumes that were attached when the instance launched. Volumes attached after instance launch continue running.
        
        You can stop, start, and terminate EBS-backed instances. You can only terminate instance store-backed instances. What happens to an instance differs if you stop it or terminate it. For example, when you stop an instance, the root device and any other devices attached to the instance persist. When you terminate an instance, any attached EBS volumes with the ``DeleteOnTermination`` block device mapping parameter set to ``true`` are automatically deleted. For more information about the differences between stopping and terminating instances, see `Instance Lifecycle <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        For more information about troubleshooting, see `Troubleshooting Terminating Your Instance <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesShuttingDown.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/TerminateInstances>`_
        
        **Request Syntax** 
        ::
        
          response = instance.terminate(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TerminatingInstances\': [
                    {
                        \'CurrentState\': {
                            \'Code\': 123,
                            \'Name\': \'pending\'|\'running\'|\'shutting-down\'|\'terminated\'|\'stopping\'|\'stopped\'
                        },
                        \'InstanceId\': \'string\',
                        \'PreviousState\': {
                            \'Code\': 123,
                            \'Name\': \'pending\'|\'running\'|\'shutting-down\'|\'terminated\'|\'stopping\'|\'stopped\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of TerminateInstances.
        
            - **TerminatingInstances** *(list) --* 
        
              Information about one or more terminated instances.
        
              - *(dict) --* 
        
                Describes an instance state change.
        
                - **CurrentState** *(dict) --* 
        
                  The current state of the instance.
        
                  - **Code** *(integer) --* 
        
                    The low byte represents the state. The high byte is used for internal purposes and should be ignored.
        
                    * ``0`` : ``pending``   
                     
                    * ``16`` : ``running``   
                     
                    * ``32`` : ``shutting-down``   
                     
                    * ``48`` : ``terminated``   
                     
                    * ``64`` : ``stopping``   
                     
                    * ``80`` : ``stopped``   
                     
                  - **Name** *(string) --* 
        
                    The current state of the instance.
        
                - **InstanceId** *(string) --* 
        
                  The ID of the instance.
        
                - **PreviousState** *(dict) --* 
        
                  The previous state of the instance.
        
                  - **Code** *(integer) --* 
        
                    The low byte represents the state. The high byte is used for internal purposes and should be ignored.
        
                    * ``0`` : ``pending``   
                     
                    * ``16`` : ``running``   
                     
                    * ``32`` : ``shutting-down``   
                     
                    * ``48`` : ``terminated``   
                     
                    * ``64`` : ``stopping``   
                     
                    * ``80`` : ``stopped``   
                     
                  - **Name** *(string) --* 
        
                    The current state of the instance.
        
        """
        pass

    def unmonitor(self, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/UnmonitorInstances>`_
        
        **Request Syntax** 
        ::
        
          response = instance.unmonitor(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstanceMonitorings\': [
                    {
                        \'InstanceId\': \'string\',
                        \'Monitoring\': {
                            \'State\': \'disabled\'|\'disabling\'|\'enabled\'|\'pending\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of UnmonitorInstances.
        
            - **InstanceMonitorings** *(list) --* 
        
              The monitoring information.
        
              - *(dict) --* 
        
                Describes the monitoring of an instance.
        
                - **InstanceId** *(string) --* 
        
                  The ID of the instance.
        
                - **Monitoring** *(dict) --* 
        
                  The monitoring for the instance.
        
                  - **State** *(string) --* 
        
                    Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
        
        """
        pass

    def wait_until_exists(self, Filters: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances>`_
        
        **Request Syntax** 
        ::
        
          instance.wait_until_exists(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              MaxResults=123,
              NextToken=\'string\'
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``affinity`` - The affinity setting for an instance running on a Dedicated Host (``default`` | ``host`` ). 
           
          * ``architecture`` - The instance architecture (``i386`` | ``x86_64`` ). 
           
          * ``availability-zone`` - The Availability Zone of the instance. 
           
          * ``block-device-mapping.attach-time`` - The attach time for an EBS volume mapped to the instance, for example, ``2010-09-15T17:15:20.000Z`` . 
           
          * ``block-device-mapping.delete-on-termination`` - A Boolean that indicates whether the EBS volume is deleted on instance termination. 
           
          * ``block-device-mapping.device-name`` - The device name specified in the block device mapping (for example, ``/dev/sdh`` or ``xvdh`` ). 
           
          * ``block-device-mapping.status`` - The status for the EBS volume (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``block-device-mapping.volume-id`` - The volume ID of the EBS volume. 
           
          * ``client-token`` - The idempotency token you provided when you launched the instance. 
           
          * ``dns-name`` - The public DNS name of the instance. 
           
          * ``group-id`` - The ID of the security group for the instance. EC2-Classic only. 
           
          * ``group-name`` - The name of the security group for the instance. EC2-Classic only. 
           
          * ``host-id`` - The ID of the Dedicated Host on which the instance is running, if applicable. 
           
          * ``hypervisor`` - The hypervisor type of the instance (``ovm`` | ``xen`` ). 
           
          * ``iam-instance-profile.arn`` - The instance profile associated with the instance. Specified as an ARN. 
           
          * ``image-id`` - The ID of the image used to launch the instance. 
           
          * ``instance-id`` - The ID of the instance. 
           
          * ``instance-lifecycle`` - Indicates whether this is a Spot Instance or a Scheduled Instance (``spot`` | ``scheduled`` ). 
           
          * ``instance-state-code`` - The state of the instance, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are: 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped). 
           
          * ``instance-state-name`` - The state of the instance (``pending`` | ``running`` | ``shutting-down`` | ``terminated`` | ``stopping`` | ``stopped`` ). 
           
          * ``instance-type`` - The type of instance (for example, ``t2.micro`` ). 
           
          * ``instance.group-id`` - The ID of the security group for the instance.  
           
          * ``instance.group-name`` - The name of the security group for the instance.  
           
          * ``ip-address`` - The public IPv4 address of the instance. 
           
          * ``kernel-id`` - The kernel ID. 
           
          * ``key-name`` - The name of the key pair used when the instance was launched. 
           
          * ``launch-index`` - When launching multiple instances, this is the index for the instance in the launch group (for example, 0, 1, 2, and so on).  
           
          * ``launch-time`` - The time when the instance was launched. 
           
          * ``monitoring-state`` - Indicates whether detailed monitoring is enabled (``disabled`` | ``enabled`` ). 
           
          * ``network-interface.addresses.private-ip-address`` - The private IPv4 address associated with the network interface. 
           
          * ``network-interface.addresses.primary`` - Specifies whether the IPv4 address of the network interface is the primary private IPv4 address. 
           
          * ``network-interface.addresses.association.public-ip`` - The ID of the association of an Elastic IP address (IPv4) with a network interface. 
           
          * ``network-interface.addresses.association.ip-owner-id`` - The owner ID of the private IPv4 address associated with the network interface. 
           
          * ``network-interface.association.public-ip`` - The address of the Elastic IP address (IPv4) bound to the network interface. 
           
          * ``network-interface.association.ip-owner-id`` - The owner of the Elastic IP address (IPv4) associated with the network interface. 
           
          * ``network-interface.association.allocation-id`` - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface. 
           
          * ``network-interface.association.association-id`` - The association ID returned when the network interface was associated with an IPv4 address. 
           
          * ``network-interface.attachment.attachment-id`` - The ID of the interface attachment. 
           
          * ``network-interface.attachment.instance-id`` - The ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.instance-owner-id`` - The owner ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.device-index`` - The device index to which the network interface is attached. 
           
          * ``network-interface.attachment.status`` - The status of the attachment (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``network-interface.attachment.attach-time`` - The time that the network interface was attached to an instance. 
           
          * ``network-interface.attachment.delete-on-termination`` - Specifies whether the attachment is deleted when an instance is terminated. 
           
          * ``network-interface.availability-zone`` - The Availability Zone for the network interface. 
           
          * ``network-interface.description`` - The description of the network interface. 
           
          * ``network-interface.group-id`` - The ID of a security group associated with the network interface. 
           
          * ``network-interface.group-name`` - The name of a security group associated with the network interface. 
           
          * ``network-interface.ipv6-addresses.ipv6-address`` - The IPv6 address associated with the network interface. 
           
          * ``network-interface.mac-address`` - The MAC address of the network interface. 
           
          * ``network-interface.network-interface-id`` - The ID of the network interface. 
           
          * ``network-interface.owner-id`` - The ID of the owner of the network interface. 
           
          * ``network-interface.private-dns-name`` - The private DNS name of the network interface. 
           
          * ``network-interface.requester-id`` - The requester ID for the network interface. 
           
          * ``network-interface.requester-managed`` - Indicates whether the network interface is being managed by AWS. 
           
          * ``network-interface.status`` - The status of the network interface (``available`` ) | ``in-use`` ). 
           
          * ``network-interface.source-dest-check`` - Whether the network interface performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the network interface to perform network address translation (NAT) in your VPC. 
           
          * ``network-interface.subnet-id`` - The ID of the subnet for the network interface. 
           
          * ``network-interface.vpc-id`` - The ID of the VPC for the network interface. 
           
          * ``owner-id`` - The AWS account ID of the instance owner. 
           
          * ``placement-group-name`` - The name of the placement group for the instance. 
           
          * ``platform`` - The platform. Use ``windows`` if you have Windows instances; otherwise, leave blank. 
           
          * ``private-dns-name`` - The private IPv4 DNS name of the instance. 
           
          * ``private-ip-address`` - The private IPv4 address of the instance. 
           
          * ``product-code`` - The product code associated with the AMI used to launch the instance. 
           
          * ``product-code.type`` - The type of product code (``devpay`` | ``marketplace`` ). 
           
          * ``ramdisk-id`` - The RAM disk ID. 
           
          * ``reason`` - The reason for the current state of the instance (for example, shows \"User Initiated [date]\" when you stop or terminate the instance). Similar to the state-reason-code filter. 
           
          * ``requester-id`` - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on). 
           
          * ``reservation-id`` - The ID of the instance\'s reservation. A reservation ID is created any time you launch an instance. A reservation ID has a one-to-one relationship with an instance launch request, but can be associated with more than one instance if you launch multiple instances using the same launch request. For example, if you launch one instance, you get one reservation ID. If you launch ten instances using the same launch request, you also get one reservation ID. 
           
          * ``root-device-name`` - The device name of the root device volume (for example, ``/dev/sda1`` ). 
           
          * ``root-device-type`` - The type of the root device volume (``ebs`` | ``instance-store`` ). 
           
          * ``source-dest-check`` - Indicates whether the instance performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the instance to perform network address translation (NAT) in your VPC.  
           
          * ``spot-instance-request-id`` - The ID of the Spot Instance request. 
           
          * ``state-reason-code`` - The reason code for the state change. 
           
          * ``state-reason-message`` - A message that describes the state change. 
           
          * ``subnet-id`` - The ID of the subnet for the instance. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific key, regardless of the tag value. 
           
          * ``tenancy`` - The tenancy of an instance (``dedicated`` | ``default`` | ``host`` ). 
           
          * ``virtualization-type`` - The virtualization type of the instance (``paravirtual`` | ``hvm`` ). 
           
          * ``vpc-id`` - The ID of the VPC that the instance is running in. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to request the next page of results.
        
        :returns: None
        """
        pass

    def wait_until_running(self, Filters: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances>`_
        
        **Request Syntax** 
        ::
        
          instance.wait_until_running(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              MaxResults=123,
              NextToken=\'string\'
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``affinity`` - The affinity setting for an instance running on a Dedicated Host (``default`` | ``host`` ). 
           
          * ``architecture`` - The instance architecture (``i386`` | ``x86_64`` ). 
           
          * ``availability-zone`` - The Availability Zone of the instance. 
           
          * ``block-device-mapping.attach-time`` - The attach time for an EBS volume mapped to the instance, for example, ``2010-09-15T17:15:20.000Z`` . 
           
          * ``block-device-mapping.delete-on-termination`` - A Boolean that indicates whether the EBS volume is deleted on instance termination. 
           
          * ``block-device-mapping.device-name`` - The device name specified in the block device mapping (for example, ``/dev/sdh`` or ``xvdh`` ). 
           
          * ``block-device-mapping.status`` - The status for the EBS volume (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``block-device-mapping.volume-id`` - The volume ID of the EBS volume. 
           
          * ``client-token`` - The idempotency token you provided when you launched the instance. 
           
          * ``dns-name`` - The public DNS name of the instance. 
           
          * ``group-id`` - The ID of the security group for the instance. EC2-Classic only. 
           
          * ``group-name`` - The name of the security group for the instance. EC2-Classic only. 
           
          * ``host-id`` - The ID of the Dedicated Host on which the instance is running, if applicable. 
           
          * ``hypervisor`` - The hypervisor type of the instance (``ovm`` | ``xen`` ). 
           
          * ``iam-instance-profile.arn`` - The instance profile associated with the instance. Specified as an ARN. 
           
          * ``image-id`` - The ID of the image used to launch the instance. 
           
          * ``instance-id`` - The ID of the instance. 
           
          * ``instance-lifecycle`` - Indicates whether this is a Spot Instance or a Scheduled Instance (``spot`` | ``scheduled`` ). 
           
          * ``instance-state-code`` - The state of the instance, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are: 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped). 
           
          * ``instance-state-name`` - The state of the instance (``pending`` | ``running`` | ``shutting-down`` | ``terminated`` | ``stopping`` | ``stopped`` ). 
           
          * ``instance-type`` - The type of instance (for example, ``t2.micro`` ). 
           
          * ``instance.group-id`` - The ID of the security group for the instance.  
           
          * ``instance.group-name`` - The name of the security group for the instance.  
           
          * ``ip-address`` - The public IPv4 address of the instance. 
           
          * ``kernel-id`` - The kernel ID. 
           
          * ``key-name`` - The name of the key pair used when the instance was launched. 
           
          * ``launch-index`` - When launching multiple instances, this is the index for the instance in the launch group (for example, 0, 1, 2, and so on).  
           
          * ``launch-time`` - The time when the instance was launched. 
           
          * ``monitoring-state`` - Indicates whether detailed monitoring is enabled (``disabled`` | ``enabled`` ). 
           
          * ``network-interface.addresses.private-ip-address`` - The private IPv4 address associated with the network interface. 
           
          * ``network-interface.addresses.primary`` - Specifies whether the IPv4 address of the network interface is the primary private IPv4 address. 
           
          * ``network-interface.addresses.association.public-ip`` - The ID of the association of an Elastic IP address (IPv4) with a network interface. 
           
          * ``network-interface.addresses.association.ip-owner-id`` - The owner ID of the private IPv4 address associated with the network interface. 
           
          * ``network-interface.association.public-ip`` - The address of the Elastic IP address (IPv4) bound to the network interface. 
           
          * ``network-interface.association.ip-owner-id`` - The owner of the Elastic IP address (IPv4) associated with the network interface. 
           
          * ``network-interface.association.allocation-id`` - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface. 
           
          * ``network-interface.association.association-id`` - The association ID returned when the network interface was associated with an IPv4 address. 
           
          * ``network-interface.attachment.attachment-id`` - The ID of the interface attachment. 
           
          * ``network-interface.attachment.instance-id`` - The ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.instance-owner-id`` - The owner ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.device-index`` - The device index to which the network interface is attached. 
           
          * ``network-interface.attachment.status`` - The status of the attachment (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``network-interface.attachment.attach-time`` - The time that the network interface was attached to an instance. 
           
          * ``network-interface.attachment.delete-on-termination`` - Specifies whether the attachment is deleted when an instance is terminated. 
           
          * ``network-interface.availability-zone`` - The Availability Zone for the network interface. 
           
          * ``network-interface.description`` - The description of the network interface. 
           
          * ``network-interface.group-id`` - The ID of a security group associated with the network interface. 
           
          * ``network-interface.group-name`` - The name of a security group associated with the network interface. 
           
          * ``network-interface.ipv6-addresses.ipv6-address`` - The IPv6 address associated with the network interface. 
           
          * ``network-interface.mac-address`` - The MAC address of the network interface. 
           
          * ``network-interface.network-interface-id`` - The ID of the network interface. 
           
          * ``network-interface.owner-id`` - The ID of the owner of the network interface. 
           
          * ``network-interface.private-dns-name`` - The private DNS name of the network interface. 
           
          * ``network-interface.requester-id`` - The requester ID for the network interface. 
           
          * ``network-interface.requester-managed`` - Indicates whether the network interface is being managed by AWS. 
           
          * ``network-interface.status`` - The status of the network interface (``available`` ) | ``in-use`` ). 
           
          * ``network-interface.source-dest-check`` - Whether the network interface performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the network interface to perform network address translation (NAT) in your VPC. 
           
          * ``network-interface.subnet-id`` - The ID of the subnet for the network interface. 
           
          * ``network-interface.vpc-id`` - The ID of the VPC for the network interface. 
           
          * ``owner-id`` - The AWS account ID of the instance owner. 
           
          * ``placement-group-name`` - The name of the placement group for the instance. 
           
          * ``platform`` - The platform. Use ``windows`` if you have Windows instances; otherwise, leave blank. 
           
          * ``private-dns-name`` - The private IPv4 DNS name of the instance. 
           
          * ``private-ip-address`` - The private IPv4 address of the instance. 
           
          * ``product-code`` - The product code associated with the AMI used to launch the instance. 
           
          * ``product-code.type`` - The type of product code (``devpay`` | ``marketplace`` ). 
           
          * ``ramdisk-id`` - The RAM disk ID. 
           
          * ``reason`` - The reason for the current state of the instance (for example, shows \"User Initiated [date]\" when you stop or terminate the instance). Similar to the state-reason-code filter. 
           
          * ``requester-id`` - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on). 
           
          * ``reservation-id`` - The ID of the instance\'s reservation. A reservation ID is created any time you launch an instance. A reservation ID has a one-to-one relationship with an instance launch request, but can be associated with more than one instance if you launch multiple instances using the same launch request. For example, if you launch one instance, you get one reservation ID. If you launch ten instances using the same launch request, you also get one reservation ID. 
           
          * ``root-device-name`` - The device name of the root device volume (for example, ``/dev/sda1`` ). 
           
          * ``root-device-type`` - The type of the root device volume (``ebs`` | ``instance-store`` ). 
           
          * ``source-dest-check`` - Indicates whether the instance performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the instance to perform network address translation (NAT) in your VPC.  
           
          * ``spot-instance-request-id`` - The ID of the Spot Instance request. 
           
          * ``state-reason-code`` - The reason code for the state change. 
           
          * ``state-reason-message`` - A message that describes the state change. 
           
          * ``subnet-id`` - The ID of the subnet for the instance. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific key, regardless of the tag value. 
           
          * ``tenancy`` - The tenancy of an instance (``dedicated`` | ``default`` | ``host`` ). 
           
          * ``virtualization-type`` - The virtualization type of the instance (``paravirtual`` | ``hvm`` ). 
           
          * ``vpc-id`` - The ID of the VPC that the instance is running in. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to request the next page of results.
        
        :returns: None
        """
        pass

    def wait_until_stopped(self, Filters: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances>`_
        
        **Request Syntax** 
        ::
        
          instance.wait_until_stopped(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              MaxResults=123,
              NextToken=\'string\'
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``affinity`` - The affinity setting for an instance running on a Dedicated Host (``default`` | ``host`` ). 
           
          * ``architecture`` - The instance architecture (``i386`` | ``x86_64`` ). 
           
          * ``availability-zone`` - The Availability Zone of the instance. 
           
          * ``block-device-mapping.attach-time`` - The attach time for an EBS volume mapped to the instance, for example, ``2010-09-15T17:15:20.000Z`` . 
           
          * ``block-device-mapping.delete-on-termination`` - A Boolean that indicates whether the EBS volume is deleted on instance termination. 
           
          * ``block-device-mapping.device-name`` - The device name specified in the block device mapping (for example, ``/dev/sdh`` or ``xvdh`` ). 
           
          * ``block-device-mapping.status`` - The status for the EBS volume (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``block-device-mapping.volume-id`` - The volume ID of the EBS volume. 
           
          * ``client-token`` - The idempotency token you provided when you launched the instance. 
           
          * ``dns-name`` - The public DNS name of the instance. 
           
          * ``group-id`` - The ID of the security group for the instance. EC2-Classic only. 
           
          * ``group-name`` - The name of the security group for the instance. EC2-Classic only. 
           
          * ``host-id`` - The ID of the Dedicated Host on which the instance is running, if applicable. 
           
          * ``hypervisor`` - The hypervisor type of the instance (``ovm`` | ``xen`` ). 
           
          * ``iam-instance-profile.arn`` - The instance profile associated with the instance. Specified as an ARN. 
           
          * ``image-id`` - The ID of the image used to launch the instance. 
           
          * ``instance-id`` - The ID of the instance. 
           
          * ``instance-lifecycle`` - Indicates whether this is a Spot Instance or a Scheduled Instance (``spot`` | ``scheduled`` ). 
           
          * ``instance-state-code`` - The state of the instance, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are: 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped). 
           
          * ``instance-state-name`` - The state of the instance (``pending`` | ``running`` | ``shutting-down`` | ``terminated`` | ``stopping`` | ``stopped`` ). 
           
          * ``instance-type`` - The type of instance (for example, ``t2.micro`` ). 
           
          * ``instance.group-id`` - The ID of the security group for the instance.  
           
          * ``instance.group-name`` - The name of the security group for the instance.  
           
          * ``ip-address`` - The public IPv4 address of the instance. 
           
          * ``kernel-id`` - The kernel ID. 
           
          * ``key-name`` - The name of the key pair used when the instance was launched. 
           
          * ``launch-index`` - When launching multiple instances, this is the index for the instance in the launch group (for example, 0, 1, 2, and so on).  
           
          * ``launch-time`` - The time when the instance was launched. 
           
          * ``monitoring-state`` - Indicates whether detailed monitoring is enabled (``disabled`` | ``enabled`` ). 
           
          * ``network-interface.addresses.private-ip-address`` - The private IPv4 address associated with the network interface. 
           
          * ``network-interface.addresses.primary`` - Specifies whether the IPv4 address of the network interface is the primary private IPv4 address. 
           
          * ``network-interface.addresses.association.public-ip`` - The ID of the association of an Elastic IP address (IPv4) with a network interface. 
           
          * ``network-interface.addresses.association.ip-owner-id`` - The owner ID of the private IPv4 address associated with the network interface. 
           
          * ``network-interface.association.public-ip`` - The address of the Elastic IP address (IPv4) bound to the network interface. 
           
          * ``network-interface.association.ip-owner-id`` - The owner of the Elastic IP address (IPv4) associated with the network interface. 
           
          * ``network-interface.association.allocation-id`` - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface. 
           
          * ``network-interface.association.association-id`` - The association ID returned when the network interface was associated with an IPv4 address. 
           
          * ``network-interface.attachment.attachment-id`` - The ID of the interface attachment. 
           
          * ``network-interface.attachment.instance-id`` - The ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.instance-owner-id`` - The owner ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.device-index`` - The device index to which the network interface is attached. 
           
          * ``network-interface.attachment.status`` - The status of the attachment (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``network-interface.attachment.attach-time`` - The time that the network interface was attached to an instance. 
           
          * ``network-interface.attachment.delete-on-termination`` - Specifies whether the attachment is deleted when an instance is terminated. 
           
          * ``network-interface.availability-zone`` - The Availability Zone for the network interface. 
           
          * ``network-interface.description`` - The description of the network interface. 
           
          * ``network-interface.group-id`` - The ID of a security group associated with the network interface. 
           
          * ``network-interface.group-name`` - The name of a security group associated with the network interface. 
           
          * ``network-interface.ipv6-addresses.ipv6-address`` - The IPv6 address associated with the network interface. 
           
          * ``network-interface.mac-address`` - The MAC address of the network interface. 
           
          * ``network-interface.network-interface-id`` - The ID of the network interface. 
           
          * ``network-interface.owner-id`` - The ID of the owner of the network interface. 
           
          * ``network-interface.private-dns-name`` - The private DNS name of the network interface. 
           
          * ``network-interface.requester-id`` - The requester ID for the network interface. 
           
          * ``network-interface.requester-managed`` - Indicates whether the network interface is being managed by AWS. 
           
          * ``network-interface.status`` - The status of the network interface (``available`` ) | ``in-use`` ). 
           
          * ``network-interface.source-dest-check`` - Whether the network interface performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the network interface to perform network address translation (NAT) in your VPC. 
           
          * ``network-interface.subnet-id`` - The ID of the subnet for the network interface. 
           
          * ``network-interface.vpc-id`` - The ID of the VPC for the network interface. 
           
          * ``owner-id`` - The AWS account ID of the instance owner. 
           
          * ``placement-group-name`` - The name of the placement group for the instance. 
           
          * ``platform`` - The platform. Use ``windows`` if you have Windows instances; otherwise, leave blank. 
           
          * ``private-dns-name`` - The private IPv4 DNS name of the instance. 
           
          * ``private-ip-address`` - The private IPv4 address of the instance. 
           
          * ``product-code`` - The product code associated with the AMI used to launch the instance. 
           
          * ``product-code.type`` - The type of product code (``devpay`` | ``marketplace`` ). 
           
          * ``ramdisk-id`` - The RAM disk ID. 
           
          * ``reason`` - The reason for the current state of the instance (for example, shows \"User Initiated [date]\" when you stop or terminate the instance). Similar to the state-reason-code filter. 
           
          * ``requester-id`` - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on). 
           
          * ``reservation-id`` - The ID of the instance\'s reservation. A reservation ID is created any time you launch an instance. A reservation ID has a one-to-one relationship with an instance launch request, but can be associated with more than one instance if you launch multiple instances using the same launch request. For example, if you launch one instance, you get one reservation ID. If you launch ten instances using the same launch request, you also get one reservation ID. 
           
          * ``root-device-name`` - The device name of the root device volume (for example, ``/dev/sda1`` ). 
           
          * ``root-device-type`` - The type of the root device volume (``ebs`` | ``instance-store`` ). 
           
          * ``source-dest-check`` - Indicates whether the instance performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the instance to perform network address translation (NAT) in your VPC.  
           
          * ``spot-instance-request-id`` - The ID of the Spot Instance request. 
           
          * ``state-reason-code`` - The reason code for the state change. 
           
          * ``state-reason-message`` - A message that describes the state change. 
           
          * ``subnet-id`` - The ID of the subnet for the instance. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific key, regardless of the tag value. 
           
          * ``tenancy`` - The tenancy of an instance (``dedicated`` | ``default`` | ``host`` ). 
           
          * ``virtualization-type`` - The virtualization type of the instance (``paravirtual`` | ``hvm`` ). 
           
          * ``vpc-id`` - The ID of the VPC that the instance is running in. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to request the next page of results.
        
        :returns: None
        """
        pass

    def wait_until_terminated(self, Filters: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances>`_
        
        **Request Syntax** 
        ::
        
          instance.wait_until_terminated(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              MaxResults=123,
              NextToken=\'string\'
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``affinity`` - The affinity setting for an instance running on a Dedicated Host (``default`` | ``host`` ). 
           
          * ``architecture`` - The instance architecture (``i386`` | ``x86_64`` ). 
           
          * ``availability-zone`` - The Availability Zone of the instance. 
           
          * ``block-device-mapping.attach-time`` - The attach time for an EBS volume mapped to the instance, for example, ``2010-09-15T17:15:20.000Z`` . 
           
          * ``block-device-mapping.delete-on-termination`` - A Boolean that indicates whether the EBS volume is deleted on instance termination. 
           
          * ``block-device-mapping.device-name`` - The device name specified in the block device mapping (for example, ``/dev/sdh`` or ``xvdh`` ). 
           
          * ``block-device-mapping.status`` - The status for the EBS volume (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``block-device-mapping.volume-id`` - The volume ID of the EBS volume. 
           
          * ``client-token`` - The idempotency token you provided when you launched the instance. 
           
          * ``dns-name`` - The public DNS name of the instance. 
           
          * ``group-id`` - The ID of the security group for the instance. EC2-Classic only. 
           
          * ``group-name`` - The name of the security group for the instance. EC2-Classic only. 
           
          * ``host-id`` - The ID of the Dedicated Host on which the instance is running, if applicable. 
           
          * ``hypervisor`` - The hypervisor type of the instance (``ovm`` | ``xen`` ). 
           
          * ``iam-instance-profile.arn`` - The instance profile associated with the instance. Specified as an ARN. 
           
          * ``image-id`` - The ID of the image used to launch the instance. 
           
          * ``instance-id`` - The ID of the instance. 
           
          * ``instance-lifecycle`` - Indicates whether this is a Spot Instance or a Scheduled Instance (``spot`` | ``scheduled`` ). 
           
          * ``instance-state-code`` - The state of the instance, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are: 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped). 
           
          * ``instance-state-name`` - The state of the instance (``pending`` | ``running`` | ``shutting-down`` | ``terminated`` | ``stopping`` | ``stopped`` ). 
           
          * ``instance-type`` - The type of instance (for example, ``t2.micro`` ). 
           
          * ``instance.group-id`` - The ID of the security group for the instance.  
           
          * ``instance.group-name`` - The name of the security group for the instance.  
           
          * ``ip-address`` - The public IPv4 address of the instance. 
           
          * ``kernel-id`` - The kernel ID. 
           
          * ``key-name`` - The name of the key pair used when the instance was launched. 
           
          * ``launch-index`` - When launching multiple instances, this is the index for the instance in the launch group (for example, 0, 1, 2, and so on).  
           
          * ``launch-time`` - The time when the instance was launched. 
           
          * ``monitoring-state`` - Indicates whether detailed monitoring is enabled (``disabled`` | ``enabled`` ). 
           
          * ``network-interface.addresses.private-ip-address`` - The private IPv4 address associated with the network interface. 
           
          * ``network-interface.addresses.primary`` - Specifies whether the IPv4 address of the network interface is the primary private IPv4 address. 
           
          * ``network-interface.addresses.association.public-ip`` - The ID of the association of an Elastic IP address (IPv4) with a network interface. 
           
          * ``network-interface.addresses.association.ip-owner-id`` - The owner ID of the private IPv4 address associated with the network interface. 
           
          * ``network-interface.association.public-ip`` - The address of the Elastic IP address (IPv4) bound to the network interface. 
           
          * ``network-interface.association.ip-owner-id`` - The owner of the Elastic IP address (IPv4) associated with the network interface. 
           
          * ``network-interface.association.allocation-id`` - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface. 
           
          * ``network-interface.association.association-id`` - The association ID returned when the network interface was associated with an IPv4 address. 
           
          * ``network-interface.attachment.attachment-id`` - The ID of the interface attachment. 
           
          * ``network-interface.attachment.instance-id`` - The ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.instance-owner-id`` - The owner ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.device-index`` - The device index to which the network interface is attached. 
           
          * ``network-interface.attachment.status`` - The status of the attachment (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``network-interface.attachment.attach-time`` - The time that the network interface was attached to an instance. 
           
          * ``network-interface.attachment.delete-on-termination`` - Specifies whether the attachment is deleted when an instance is terminated. 
           
          * ``network-interface.availability-zone`` - The Availability Zone for the network interface. 
           
          * ``network-interface.description`` - The description of the network interface. 
           
          * ``network-interface.group-id`` - The ID of a security group associated with the network interface. 
           
          * ``network-interface.group-name`` - The name of a security group associated with the network interface. 
           
          * ``network-interface.ipv6-addresses.ipv6-address`` - The IPv6 address associated with the network interface. 
           
          * ``network-interface.mac-address`` - The MAC address of the network interface. 
           
          * ``network-interface.network-interface-id`` - The ID of the network interface. 
           
          * ``network-interface.owner-id`` - The ID of the owner of the network interface. 
           
          * ``network-interface.private-dns-name`` - The private DNS name of the network interface. 
           
          * ``network-interface.requester-id`` - The requester ID for the network interface. 
           
          * ``network-interface.requester-managed`` - Indicates whether the network interface is being managed by AWS. 
           
          * ``network-interface.status`` - The status of the network interface (``available`` ) | ``in-use`` ). 
           
          * ``network-interface.source-dest-check`` - Whether the network interface performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the network interface to perform network address translation (NAT) in your VPC. 
           
          * ``network-interface.subnet-id`` - The ID of the subnet for the network interface. 
           
          * ``network-interface.vpc-id`` - The ID of the VPC for the network interface. 
           
          * ``owner-id`` - The AWS account ID of the instance owner. 
           
          * ``placement-group-name`` - The name of the placement group for the instance. 
           
          * ``platform`` - The platform. Use ``windows`` if you have Windows instances; otherwise, leave blank. 
           
          * ``private-dns-name`` - The private IPv4 DNS name of the instance. 
           
          * ``private-ip-address`` - The private IPv4 address of the instance. 
           
          * ``product-code`` - The product code associated with the AMI used to launch the instance. 
           
          * ``product-code.type`` - The type of product code (``devpay`` | ``marketplace`` ). 
           
          * ``ramdisk-id`` - The RAM disk ID. 
           
          * ``reason`` - The reason for the current state of the instance (for example, shows \"User Initiated [date]\" when you stop or terminate the instance). Similar to the state-reason-code filter. 
           
          * ``requester-id`` - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on). 
           
          * ``reservation-id`` - The ID of the instance\'s reservation. A reservation ID is created any time you launch an instance. A reservation ID has a one-to-one relationship with an instance launch request, but can be associated with more than one instance if you launch multiple instances using the same launch request. For example, if you launch one instance, you get one reservation ID. If you launch ten instances using the same launch request, you also get one reservation ID. 
           
          * ``root-device-name`` - The device name of the root device volume (for example, ``/dev/sda1`` ). 
           
          * ``root-device-type`` - The type of the root device volume (``ebs`` | ``instance-store`` ). 
           
          * ``source-dest-check`` - Indicates whether the instance performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the instance to perform network address translation (NAT) in your VPC.  
           
          * ``spot-instance-request-id`` - The ID of the Spot Instance request. 
           
          * ``state-reason-code`` - The reason code for the state change. 
           
          * ``state-reason-message`` - A message that describes the state change. 
           
          * ``subnet-id`` - The ID of the subnet for the instance. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific key, regardless of the tag value. 
           
          * ``tenancy`` - The tenancy of an instance (``dedicated`` | ``default`` | ``host`` ). 
           
          * ``virtualization-type`` - The virtualization type of the instance (``paravirtual`` | ``hvm`` ). 
           
          * ``vpc-id`` - The ID of the VPC that the instance is running in. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to request the next page of results.
        
        :returns: None
        """
        pass


class InternetGateway(base.ServiceResource):
    attachments: List
    internet_gateway_id: str
    tags: List
    id: str

    def attach_to_vpc(self, VpcId: str, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AttachInternetGateway>`_
        
        **Request Syntax** 
        ::
        
          response = internet_gateway.attach_to_vpc(
              DryRun=True|False,
              VpcId=\'string\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type VpcId: string
        :param VpcId: **[REQUIRED]** 
        
          The ID of the VPC.
        
        :returns: None
        """
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        """
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . For more information about creating IAM policies that control users\' access to resources based on tags, see `Supported Resource-Level Permissions for Amazon EC2 API Actions <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          tag = internet_gateway.create_tags(
              DryRun=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. The ``value`` parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 
        
          - *(dict) --* 
        
            Describes a tag.
        
            - **Key** *(string) --* 
        
              The key of the tag.
        
              Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
              Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :rtype: list(:py:class:`ec2.Tag`)
        :returns: A list of Tag resources
        """
        pass

    def delete(self, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteInternetGateway>`_
        
        **Request Syntax** 
        ::
        
          response = internet_gateway.delete(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def detach_from_vpc(self, VpcId: str, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DetachInternetGateway>`_
        
        **Request Syntax** 
        ::
        
          response = internet_gateway.detach_from_vpc(
              DryRun=True|False,
              VpcId=\'string\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type VpcId: string
        :param VpcId: **[REQUIRED]** 
        
          The ID of the VPC.
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          internet_gateway.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          internet_gateway.load()
        :returns: None
        """
        pass


class KeyPair(base.ServiceResource):
    key_fingerprint: str
    key_material: str
    key_name: str
    name: str

    def delete(self, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteKeyPair>`_
        
        **Request Syntax** 
        ::
        
          response = key_pair.delete(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass


class KeyPairInfo(base.ServiceResource):
    key_fingerprint: str
    key_name: str
    name: str

    def delete(self, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteKeyPair>`_
        
        **Request Syntax** 
        ::
        
          response = key_pair_info.delete(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          key_pair_info.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          key_pair_info.load()
        :returns: None
        """
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
        """
        
        We recommend that you leave room between the rule numbers (for example, 100, 110, 120, ...), and not number them one right after the other (for example, 101, 102, 103, ...). This makes it easier to add a rule between existing ones without having to renumber the rules.
        
        After you add an entry, you can\'t modify it; you must either replace it, or create an entry and delete the old one.
        
        For more information about network ACLs, see `Network ACLs <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateNetworkAclEntry>`_
        
        **Request Syntax** 
        ::
        
          response = network_acl.create_entry(
              CidrBlock=\'string\',
              DryRun=True|False,
              Egress=True|False,
              IcmpTypeCode={
                  \'Code\': 123,
                  \'Type\': 123
              },
              Ipv6CidrBlock=\'string\',
              PortRange={
                  \'From\': 123,
                  \'To\': 123
              },
              Protocol=\'string\',
              RuleAction=\'allow\'|\'deny\',
              RuleNumber=123
          )
        :type CidrBlock: string
        :param CidrBlock: 
        
          The IPv4 network range to allow or deny, in CIDR notation (for example ``172.16.0.0/24`` ).
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Egress: boolean
        :param Egress: **[REQUIRED]** 
        
          Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet).
        
        :type IcmpTypeCode: dict
        :param IcmpTypeCode: 
        
          ICMP protocol: The ICMP or ICMPv6 type and code. Required if specifying protocol 1 (ICMP) or protocol 58 (ICMPv6) with an IPv6 CIDR block.
        
          - **Code** *(integer) --* 
        
            The ICMP code. A value of -1 means all codes for the specified ICMP type.
        
          - **Type** *(integer) --* 
        
            The ICMP type. A value of -1 means all types.
        
        :type Ipv6CidrBlock: string
        :param Ipv6CidrBlock: 
        
          The IPv6 network range to allow or deny, in CIDR notation (for example ``2001:db8:1234:1a00::/64`` ).
        
        :type PortRange: dict
        :param PortRange: 
        
          TCP or UDP protocols: The range of ports the rule applies to. Required if specifying protocol 6 (TCP) or 17 (UDP).
        
          - **From** *(integer) --* 
        
            The first port in the range.
        
          - **To** *(integer) --* 
        
            The last port in the range.
        
        :type Protocol: string
        :param Protocol: **[REQUIRED]** 
        
          The protocol number. A value of \"-1\" means all protocols. If you specify \"-1\" or a protocol number other than \"6\" (TCP), \"17\" (UDP), or \"1\" (ICMP), traffic on all ports is allowed, regardless of any ports or ICMP types or codes that you specify. If you specify protocol \"58\" (ICMPv6) and specify an IPv4 CIDR block, traffic for all ICMP types and codes allowed, regardless of any that you specify. If you specify protocol \"58\" (ICMPv6) and specify an IPv6 CIDR block, you must specify an ICMP type and code.
        
        :type RuleAction: string
        :param RuleAction: **[REQUIRED]** 
        
          Indicates whether to allow or deny the traffic that matches the rule.
        
        :type RuleNumber: integer
        :param RuleNumber: **[REQUIRED]** 
        
          The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
        
          Constraints: Positive integer from 1 to 32766. The range 32767 to 65535 is reserved for internal use.
        
        :returns: None
        """
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        """
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . For more information about creating IAM policies that control users\' access to resources based on tags, see `Supported Resource-Level Permissions for Amazon EC2 API Actions <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          tag = network_acl.create_tags(
              DryRun=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. The ``value`` parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 
        
          - *(dict) --* 
        
            Describes a tag.
        
            - **Key** *(string) --* 
        
              The key of the tag.
        
              Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
              Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :rtype: list(:py:class:`ec2.Tag`)
        :returns: A list of Tag resources
        """
        pass

    def delete(self, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteNetworkAcl>`_
        
        **Request Syntax** 
        ::
        
          response = network_acl.delete(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def delete_entry(self, Egress: bool, RuleNumber: int, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteNetworkAclEntry>`_
        
        **Request Syntax** 
        ::
        
          response = network_acl.delete_entry(
              DryRun=True|False,
              Egress=True|False,
              RuleNumber=123
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Egress: boolean
        :param Egress: **[REQUIRED]** 
        
          Indicates whether the rule is an egress rule.
        
        :type RuleNumber: integer
        :param RuleNumber: **[REQUIRED]** 
        
          The rule number of the entry to delete.
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          network_acl.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          network_acl.load()
        :returns: None
        """
        pass

    def replace_association(self, AssociationId: str, DryRun: bool = None) -> Dict:
        """
        
        This is an idempotent operation.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ReplaceNetworkAclAssociation>`_
        
        **Request Syntax** 
        ::
        
          response = network_acl.replace_association(
              AssociationId=\'string\',
              DryRun=True|False,
              
          )
        :type AssociationId: string
        :param AssociationId: **[REQUIRED]** 
        
          The ID of the current association between the original network ACL and the subnet.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NewAssociationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NewAssociationId** *(string) --* 
        
              The ID of the new association.
        
        """
        pass

    def replace_entry(self, Egress: bool, Protocol: str, RuleAction: str, RuleNumber: int, CidrBlock: str = None, DryRun: bool = None, IcmpTypeCode: Dict = None, Ipv6CidrBlock: str = None, PortRange: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ReplaceNetworkAclEntry>`_
        
        **Request Syntax** 
        ::
        
          response = network_acl.replace_entry(
              CidrBlock=\'string\',
              DryRun=True|False,
              Egress=True|False,
              IcmpTypeCode={
                  \'Code\': 123,
                  \'Type\': 123
              },
              Ipv6CidrBlock=\'string\',
              PortRange={
                  \'From\': 123,
                  \'To\': 123
              },
              Protocol=\'string\',
              RuleAction=\'allow\'|\'deny\',
              RuleNumber=123
          )
        :type CidrBlock: string
        :param CidrBlock: 
        
          The IPv4 network range to allow or deny, in CIDR notation (for example ``172.16.0.0/24`` ).
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Egress: boolean
        :param Egress: **[REQUIRED]** 
        
          Indicates whether to replace the egress rule.
        
          Default: If no value is specified, we replace the ingress rule.
        
        :type IcmpTypeCode: dict
        :param IcmpTypeCode: 
        
          ICMP protocol: The ICMP or ICMPv6 type and code. Required if specifying protocol 1 (ICMP) or protocol 58 (ICMPv6) with an IPv6 CIDR block.
        
          - **Code** *(integer) --* 
        
            The ICMP code. A value of -1 means all codes for the specified ICMP type.
        
          - **Type** *(integer) --* 
        
            The ICMP type. A value of -1 means all types.
        
        :type Ipv6CidrBlock: string
        :param Ipv6CidrBlock: 
        
          The IPv6 network range to allow or deny, in CIDR notation (for example ``2001:bd8:1234:1a00::/64`` ).
        
        :type PortRange: dict
        :param PortRange: 
        
          TCP or UDP protocols: The range of ports the rule applies to. Required if specifying protocol 6 (TCP) or 17 (UDP).
        
          - **From** *(integer) --* 
        
            The first port in the range.
        
          - **To** *(integer) --* 
        
            The last port in the range.
        
        :type Protocol: string
        :param Protocol: **[REQUIRED]** 
        
          The protocol number. A value of \"-1\" means all protocols. If you specify \"-1\" or a protocol number other than \"6\" (TCP), \"17\" (UDP), or \"1\" (ICMP), traffic on all ports is allowed, regardless of any ports or ICMP types or codes that you specify. If you specify protocol \"58\" (ICMPv6) and specify an IPv4 CIDR block, traffic for all ICMP types and codes allowed, regardless of any that you specify. If you specify protocol \"58\" (ICMPv6) and specify an IPv6 CIDR block, you must specify an ICMP type and code.
        
        :type RuleAction: string
        :param RuleAction: **[REQUIRED]** 
        
          Indicates whether to allow or deny the traffic that matches the rule.
        
        :type RuleNumber: integer
        :param RuleNumber: **[REQUIRED]** 
        
          The rule number of the entry to replace.
        
        :returns: None
        """
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
        """
        
        You can specify one or more specific secondary IP addresses, or you can specify the number of secondary IP addresses to be automatically assigned within the subnet\'s CIDR block range. The number of secondary IP addresses that you can assign to an instance varies by instance type. For information about instance types, see `Instance Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . For more information about Elastic IP addresses, see `Elastic IP Addresses <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        When you move a secondary private IP address to another network interface, any Elastic IP address that is associated with the IP address is also moved.
        
        Remapping an IP address is an asynchronous operation. When you move an IP address from one network interface to another, check ``network/interfaces/macs/mac/local-ipv4s`` in the instance metadata to confirm that the remapping is complete.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AssignPrivateIpAddresses>`_
        
        **Request Syntax** 
        ::
        
          response = network_interface.assign_private_ip_addresses(
              AllowReassignment=True|False,
              PrivateIpAddresses=[
                  \'string\',
              ],
              SecondaryPrivateIpAddressCount=123
          )
        :type AllowReassignment: boolean
        :param AllowReassignment: 
        
          Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassigned to the specified network interface.
        
        :type PrivateIpAddresses: list
        :param PrivateIpAddresses: 
        
          One or more IP addresses to be assigned as a secondary private IP address to the network interface. You can\'t specify this parameter when also specifying a number of secondary IP addresses.
        
          If you don\'t specify an IP address, Amazon EC2 automatically selects an IP address within the subnet range.
        
          - *(string) --* 
        
        :type SecondaryPrivateIpAddressCount: integer
        :param SecondaryPrivateIpAddressCount: 
        
          The number of secondary IP addresses to assign to the network interface. You can\'t specify this parameter when also specifying private IP addresses.
        
        :returns: None
        """
        pass

    def attach(self, DeviceIndex: int, InstanceId: str, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AttachNetworkInterface>`_
        
        **Request Syntax** 
        ::
        
          response = network_interface.attach(
              DeviceIndex=123,
              DryRun=True|False,
              InstanceId=\'string\',
              
          )
        :type DeviceIndex: integer
        :param DeviceIndex: **[REQUIRED]** 
        
          The index of the device for the network interface attachment.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The ID of the instance.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AttachmentId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of AttachNetworkInterface.
        
            - **AttachmentId** *(string) --* 
        
              The ID of the network interface attachment.
        
        """
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        """
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . For more information about creating IAM policies that control users\' access to resources based on tags, see `Supported Resource-Level Permissions for Amazon EC2 API Actions <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          tag = network_interface.create_tags(
              DryRun=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. The ``value`` parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 
        
          - *(dict) --* 
        
            Describes a tag.
        
            - **Key** *(string) --* 
        
              The key of the tag.
        
              Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
              Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :rtype: list(:py:class:`ec2.Tag`)
        :returns: A list of Tag resources
        """
        pass

    def delete(self, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteNetworkInterface>`_
        
        **Request Syntax** 
        ::
        
          response = network_interface.delete(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def describe_attribute(self, Attribute: str = None, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNetworkInterfaceAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = network_interface.describe_attribute(
              Attribute=\'description\'|\'groupSet\'|\'sourceDestCheck\'|\'attachment\',
              DryRun=True|False,
              
          )
        :type Attribute: string
        :param Attribute: 
        
          The attribute of the network interface. This parameter is required.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Attachment\': {
                    \'AttachTime\': datetime(2015, 1, 1),
                    \'AttachmentId\': \'string\',
                    \'DeleteOnTermination\': True|False,
                    \'DeviceIndex\': 123,
                    \'InstanceId\': \'string\',
                    \'InstanceOwnerId\': \'string\',
                    \'Status\': \'attaching\'|\'attached\'|\'detaching\'|\'detached\'
                },
                \'Description\': {
                    \'Value\': \'string\'
                },
                \'Groups\': [
                    {
                        \'GroupName\': \'string\',
                        \'GroupId\': \'string\'
                    },
                ],
                \'NetworkInterfaceId\': \'string\',
                \'SourceDestCheck\': {
                    \'Value\': True|False
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DescribeNetworkInterfaceAttribute.
        
            - **Attachment** *(dict) --* 
        
              The attachment (if any) of the network interface.
        
              - **AttachTime** *(datetime) --* 
        
                The timestamp indicating when the attachment initiated.
        
              - **AttachmentId** *(string) --* 
        
                The ID of the network interface attachment.
        
              - **DeleteOnTermination** *(boolean) --* 
        
                Indicates whether the network interface is deleted when the instance is terminated.
        
              - **DeviceIndex** *(integer) --* 
        
                The device index of the network interface attachment on the instance.
        
              - **InstanceId** *(string) --* 
        
                The ID of the instance.
        
              - **InstanceOwnerId** *(string) --* 
        
                The AWS account ID of the owner of the instance.
        
              - **Status** *(string) --* 
        
                The attachment state.
        
            - **Description** *(dict) --* 
        
              The description of the network interface.
        
              - **Value** *(string) --* 
        
                The attribute value. The value is case-sensitive.
        
            - **Groups** *(list) --* 
        
              The security groups associated with the network interface.
        
              - *(dict) --* 
        
                Describes a security group.
        
                - **GroupName** *(string) --* 
        
                  The name of the security group.
        
                - **GroupId** *(string) --* 
        
                  The ID of the security group.
        
            - **NetworkInterfaceId** *(string) --* 
        
              The ID of the network interface.
        
            - **SourceDestCheck** *(dict) --* 
        
              Indicates whether source/destination checking is enabled.
        
              - **Value** *(boolean) --* 
        
                The attribute value. The valid values are ``true`` or ``false`` .
        
        """
        pass

    def detach(self, DryRun: bool = None, Force: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DetachNetworkInterface>`_
        
        **Request Syntax** 
        ::
        
          response = network_interface.detach(
              DryRun=True|False,
              Force=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Force: boolean
        :param Force: 
        
          Specifies whether to force a detachment.
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          network_interface.load()
        :returns: None
        """
        pass

    def modify_attribute(self, Attachment: Dict = None, Description: Dict = None, DryRun: bool = None, Groups: List = None, SourceDestCheck: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyNetworkInterfaceAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = network_interface.modify_attribute(
              Attachment={
                  \'AttachmentId\': \'string\',
                  \'DeleteOnTermination\': True|False
              },
              Description={
                  \'Value\': \'string\'
              },
              DryRun=True|False,
              Groups=[
                  \'string\',
              ],
              SourceDestCheck={
                  \'Value\': True|False
              }
          )
        :type Attachment: dict
        :param Attachment: 
        
          Information about the interface attachment. If modifying the \'delete on termination\' attribute, you must specify the ID of the interface attachment.
        
          - **AttachmentId** *(string) --* 
        
            The ID of the network interface attachment.
        
          - **DeleteOnTermination** *(boolean) --* 
        
            Indicates whether the network interface is deleted when the instance is terminated.
        
        :type Description: dict
        :param Description: 
        
          A description for the network interface.
        
          - **Value** *(string) --* 
        
            The attribute value. The value is case-sensitive.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Groups: list
        :param Groups: 
        
          Changes the security groups for the network interface. The new set of groups you specify replaces the current set. You must specify at least one group, even if it\'s just the default security group in the VPC. You must specify the ID of the security group, not the name.
        
          - *(string) --* 
        
        :type SourceDestCheck: dict
        :param SourceDestCheck: 
        
          Indicates whether source/destination checking is enabled. A value of ``true`` means checking is enabled, and ``false`` means checking is disabled. This value must be ``false`` for a NAT instance to perform NAT. For more information, see `NAT Instances <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
          - **Value** *(boolean) --* 
        
            The attribute value. The valid values are ``true`` or ``false`` .
        
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          network_interface.load()
        :returns: None
        """
        pass

    def reset_attribute(self, DryRun: bool = None, SourceDestCheck: str = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ResetNetworkInterfaceAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = network_interface.reset_attribute(
              DryRun=True|False,
              SourceDestCheck=\'string\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type SourceDestCheck: string
        :param SourceDestCheck: 
        
          The source/destination checking attribute. Resets the value to ``true`` .
        
        :returns: None
        """
        pass

    def unassign_private_ip_addresses(self, PrivateIpAddresses: List):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/UnassignPrivateIpAddresses>`_
        
        **Request Syntax** 
        ::
        
          response = network_interface.unassign_private_ip_addresses(
              PrivateIpAddresses=[
                  \'string\',
              ]
          )
        :type PrivateIpAddresses: list
        :param PrivateIpAddresses: **[REQUIRED]** 
        
          The secondary private IP addresses to unassign from the network interface. You can specify this option multiple times to unassign more than one IP address.
        
          - *(string) --* 
        
        :returns: None
        """
        pass


class NetworkInterfaceAssociation(base.ServiceResource):
    ip_owner_id: str
    public_dns_name: str
    public_ip: str
    id: str

    def delete(self, PublicIp: str = None, DryRun: bool = None):
        """
        
        An Elastic IP address is for use in either the EC2-Classic platform or in a VPC. For more information, see `Elastic IP Addresses <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn\'t return an error.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DisassociateAddress>`_
        
        **Request Syntax** 
        ::
        
          response = network_interface_association.delete(
              PublicIp=\'string\',
              DryRun=True|False
          )
        :type PublicIp: string
        :param PublicIp: 
        
          [EC2-Classic] The Elastic IP address. Required for EC2-Classic.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          network_interface_association.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          network_interface_association.load()
        :returns: None
        """
        pass


class PlacementGroup(base.ServiceResource):
    group_name: str
    state: str
    strategy: str
    name: str
    instances: 'instances'

    def delete(self, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeletePlacementGroup>`_
        
        **Request Syntax** 
        ::
        
          response = placement_group.delete(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          placement_group.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          placement_group.load()
        :returns: None
        """
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
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteRoute>`_
        
        **Request Syntax** 
        ::
        
          response = route.delete(
              DestinationIpv6CidrBlock=\'string\',
              DryRun=True|False,
              
          )
        :type DestinationIpv6CidrBlock: string
        :param DestinationIpv6CidrBlock: 
        
          The IPv6 CIDR range for the route. The value you specify must match the CIDR for the route exactly.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def replace(self, DestinationIpv6CidrBlock: str = None, DryRun: bool = None, EgressOnlyInternetGatewayId: str = None, GatewayId: str = None, InstanceId: str = None, NatGatewayId: str = None, NetworkInterfaceId: str = None, VpcPeeringConnectionId: str = None):
        """
        
        For more information, see `Route Tables <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ReplaceRoute>`_
        
        **Request Syntax** 
        ::
        
          response = route.replace(
              DestinationIpv6CidrBlock=\'string\',
              DryRun=True|False,
              EgressOnlyInternetGatewayId=\'string\',
              GatewayId=\'string\',
              InstanceId=\'string\',
              NatGatewayId=\'string\',
              NetworkInterfaceId=\'string\',
              VpcPeeringConnectionId=\'string\'
          )
        :type DestinationIpv6CidrBlock: string
        :param DestinationIpv6CidrBlock: 
        
          The IPv6 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existing route in the table.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type EgressOnlyInternetGatewayId: string
        :param EgressOnlyInternetGatewayId: 
        
          [IPv6 traffic only] The ID of an egress-only internet gateway.
        
        :type GatewayId: string
        :param GatewayId: 
        
          The ID of an internet gateway or virtual private gateway.
        
        :type InstanceId: string
        :param InstanceId: 
        
          The ID of a NAT instance in your VPC.
        
        :type NatGatewayId: string
        :param NatGatewayId: 
        
          [IPv4 traffic only] The ID of a NAT gateway.
        
        :type NetworkInterfaceId: string
        :param NetworkInterfaceId: 
        
          The ID of a network interface.
        
        :type VpcPeeringConnectionId: string
        :param VpcPeeringConnectionId: 
        
          The ID of a VPC peering connection.
        
        :returns: None
        """
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
        """
        
        For more information, see `Route Tables <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AssociateRouteTable>`_
        
        **Request Syntax** 
        ::
        
          route_table_association = route_table.associate_with_subnet(
              DryRun=True|False,
              SubnetId=\'string\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type SubnetId: string
        :param SubnetId: **[REQUIRED]** 
        
          The ID of the subnet.
        
        :rtype: :py:class:`ec2.RouteTableAssociation`
        :returns: RouteTableAssociation resource
        """
        pass

    def create_route(self, DestinationCidrBlock: str = None, DestinationIpv6CidrBlock: str = None, DryRun: bool = None, EgressOnlyInternetGatewayId: str = None, GatewayId: str = None, InstanceId: str = None, NatGatewayId: str = None, NetworkInterfaceId: str = None, VpcPeeringConnectionId: str = None) -> 'Route':
        """
        
        You must specify one of the following targets: internet gateway or virtual private gateway, NAT instance, NAT gateway, VPC peering connection, network interface, or egress-only internet gateway.
        
        When determining how to route traffic, we use the route with the most specific match. For example, traffic is destined for the IPv4 address ``192.0.2.3`` , and the route table includes the following two IPv4 routes:
        
        * ``192.0.2.0/24`` (goes to some target A) 
         
        * ``192.0.2.0/28`` (goes to some target B) 
         
        Both routes apply to the traffic destined for ``192.0.2.3`` . However, the second route in the list covers a smaller number of IP addresses and is therefore more specific, so we use that route to determine where to target the traffic.
        
        For more information about route tables, see `Route Tables <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateRoute>`_
        
        **Request Syntax** 
        ::
        
          route = route_table.create_route(
              DestinationCidrBlock=\'string\',
              DestinationIpv6CidrBlock=\'string\',
              DryRun=True|False,
              EgressOnlyInternetGatewayId=\'string\',
              GatewayId=\'string\',
              InstanceId=\'string\',
              NatGatewayId=\'string\',
              NetworkInterfaceId=\'string\',
              VpcPeeringConnectionId=\'string\'
          )
        :type DestinationCidrBlock: string
        :param DestinationCidrBlock: 
        
          The IPv4 CIDR address block used for the destination match. Routing decisions are based on the most specific match.
        
        :type DestinationIpv6CidrBlock: string
        :param DestinationIpv6CidrBlock: 
        
          The IPv6 CIDR block used for the destination match. Routing decisions are based on the most specific match.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type EgressOnlyInternetGatewayId: string
        :param EgressOnlyInternetGatewayId: 
        
          [IPv6 traffic only] The ID of an egress-only internet gateway.
        
        :type GatewayId: string
        :param GatewayId: 
        
          The ID of an internet gateway or virtual private gateway attached to your VPC.
        
        :type InstanceId: string
        :param InstanceId: 
        
          The ID of a NAT instance in your VPC. The operation fails if you specify an instance ID unless exactly one network interface is attached.
        
        :type NatGatewayId: string
        :param NatGatewayId: 
        
          [IPv4 traffic only] The ID of a NAT gateway.
        
        :type NetworkInterfaceId: string
        :param NetworkInterfaceId: 
        
          The ID of a network interface.
        
        :type VpcPeeringConnectionId: string
        :param VpcPeeringConnectionId: 
        
          The ID of a VPC peering connection.
        
        :rtype: :py:class:`ec2.Route`
        :returns: Route resource
        """
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        """
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . For more information about creating IAM policies that control users\' access to resources based on tags, see `Supported Resource-Level Permissions for Amazon EC2 API Actions <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          tag = route_table.create_tags(
              DryRun=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. The ``value`` parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 
        
          - *(dict) --* 
        
            Describes a tag.
        
            - **Key** *(string) --* 
        
              The key of the tag.
        
              Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
              Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :rtype: list(:py:class:`ec2.Tag`)
        :returns: A list of Tag resources
        """
        pass

    def delete(self, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteRouteTable>`_
        
        **Request Syntax** 
        ::
        
          response = route_table.delete(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          route_table.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          route_table.load()
        :returns: None
        """
        pass


class RouteTableAssociation(base.ServiceResource):
    main: bool
    route_table_association_id: str
    route_table_id: str
    subnet_id: str
    id: str

    def delete(self, DryRun: bool = None):
        """
        
        After you perform this action, the subnet no longer uses the routes in the route table. Instead, it uses the routes in the VPC\'s main route table. For more information about route tables, see `Route Tables <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DisassociateRouteTable>`_
        
        **Request Syntax** 
        ::
        
          response = route_table_association.delete(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def replace_subnet(self, RouteTableId: str, DryRun: bool = None) -> 'RouteTableAssociation':
        """
        
        You can also use ReplaceRouteTableAssociation to change which table is the main route table in the VPC. You just specify the main route table\'s association ID and the route table to be the new main route table.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ReplaceRouteTableAssociation>`_
        
        **Request Syntax** 
        ::
        
          route_table_association = route_table_association.replace_subnet(
              DryRun=True|False,
              RouteTableId=\'string\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type RouteTableId: string
        :param RouteTableId: **[REQUIRED]** 
        
          The ID of the new route table to associate with the subnet.
        
        :rtype: :py:class:`ec2.RouteTableAssociation`
        :returns: RouteTableAssociation resource
        """
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
        """
        
        Each rule consists of the protocol (for example, TCP), plus either a CIDR range or a source group. For the TCP and UDP protocols, you must also specify the destination port or port range. For the ICMP protocol, you must also specify the ICMP type and code. You can use -1 for the type or code to mean all types or all codes. You can optionally specify a description for the rule.
        
        Rule changes are propagated to affected instances as quickly as possible. However, a small delay might occur.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AuthorizeSecurityGroupEgress>`_
        
        **Request Syntax** 
        ::
        
          response = security_group.authorize_egress(
              DryRun=True|False,
              IpPermissions=[
                  {
                      \'FromPort\': 123,
                      \'IpProtocol\': \'string\',
                      \'IpRanges\': [
                          {
                              \'CidrIp\': \'string\',
                              \'Description\': \'string\'
                          },
                      ],
                      \'Ipv6Ranges\': [
                          {
                              \'CidrIpv6\': \'string\',
                              \'Description\': \'string\'
                          },
                      ],
                      \'PrefixListIds\': [
                          {
                              \'Description\': \'string\',
                              \'PrefixListId\': \'string\'
                          },
                      ],
                      \'ToPort\': 123,
                      \'UserIdGroupPairs\': [
                          {
                              \'Description\': \'string\',
                              \'GroupId\': \'string\',
                              \'GroupName\': \'string\',
                              \'PeeringStatus\': \'string\',
                              \'UserId\': \'string\',
                              \'VpcId\': \'string\',
                              \'VpcPeeringConnectionId\': \'string\'
                          },
                      ]
                  },
              ],
              CidrIp=\'string\',
              FromPort=123,
              IpProtocol=\'string\',
              ToPort=123,
              SourceSecurityGroupName=\'string\',
              SourceSecurityGroupOwnerId=\'string\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type IpPermissions: list
        :param IpPermissions: 
        
          One or more sets of IP permissions. You can\'t specify a destination security group and a CIDR IP address range in the same set of permissions.
        
          - *(dict) --* 
        
            Describes a set of permissions for a security group rule.
        
            - **FromPort** *(integer) --* 
        
              The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of ``-1`` indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.
        
            - **IpProtocol** *(string) --* 
        
              The IP protocol name (``tcp`` , ``udp`` , ``icmp`` ) or number (see `Protocol Numbers <http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml>`__ ). 
        
              [EC2-VPC only] Use ``-1`` to specify all protocols. When authorizing security group rules, specifying ``-1`` or a protocol number other than ``tcp`` , ``udp`` , ``icmp`` , or ``58`` (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For ``tcp`` , ``udp`` , and ``icmp`` , you must specify a port range. For ``58`` (ICMPv6), you can optionally specify a port range; if you don\'t, traffic for all types and codes is allowed when authorizing rules. 
        
            - **IpRanges** *(list) --* 
        
              One or more IPv4 ranges.
        
              - *(dict) --* 
        
                Describes an IPv4 range.
        
                - **CidrIp** *(string) --* 
        
                  The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this IPv4 address range.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
            - **Ipv6Ranges** *(list) --* 
        
              [EC2-VPC only] One or more IPv6 ranges.
        
              - *(dict) --* 
        
                [EC2-VPC only] Describes an IPv6 range.
        
                - **CidrIpv6** *(string) --* 
        
                  The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this IPv6 address range.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
            - **PrefixListIds** *(list) --* 
        
              [EC2-VPC only] One or more prefix list IDs for an AWS service. With  AuthorizeSecurityGroupEgress , this is the AWS service that you want to access through a VPC endpoint from instances associated with the security group.
        
              - *(dict) --* 
        
                Describes a prefix list ID.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this prefix list ID.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
                - **PrefixListId** *(string) --* 
        
                  The ID of the prefix.
        
            - **ToPort** *(integer) --* 
        
              The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of ``-1`` indicates all ICMP/ICMPv6 codes for the specified ICMP type. If you specify all ICMP/ICMPv6 types, you must specify all codes.
        
            - **UserIdGroupPairs** *(list) --* 
        
              One or more security group and AWS account ID pairs.
        
              - *(dict) --* 
        
                Describes a security group and AWS account ID pair.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this user ID group pair.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
                - **GroupId** *(string) --* 
        
                  The ID of the security group.
        
                - **GroupName** *(string) --* 
        
                  The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID. 
        
                  For a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.
        
                - **PeeringStatus** *(string) --* 
        
                  The status of a VPC peering connection, if applicable.
        
                - **UserId** *(string) --* 
        
                  The ID of an AWS account.
        
                  For a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.
        
                  [EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account.
        
                - **VpcId** *(string) --* 
        
                  The ID of the VPC for the referenced security group, if applicable.
        
                - **VpcPeeringConnectionId** *(string) --* 
        
                  The ID of the VPC peering connection, if applicable.
        
        :type CidrIp: string
        :param CidrIp: 
        
          Not supported. Use a set of IP permissions to specify the CIDR.
        
        :type FromPort: integer
        :param FromPort: 
        
          Not supported. Use a set of IP permissions to specify the port.
        
        :type IpProtocol: string
        :param IpProtocol: 
        
          Not supported. Use a set of IP permissions to specify the protocol name or number.
        
        :type ToPort: integer
        :param ToPort: 
        
          Not supported. Use a set of IP permissions to specify the port.
        
        :type SourceSecurityGroupName: string
        :param SourceSecurityGroupName: 
        
          Not supported. Use a set of IP permissions to specify a destination security group.
        
        :type SourceSecurityGroupOwnerId: string
        :param SourceSecurityGroupOwnerId: 
        
          Not supported. Use a set of IP permissions to specify a destination security group.
        
        :returns: None
        """
        pass

    def authorize_ingress(self, CidrIp: str = None, FromPort: int = None, GroupName: str = None, IpPermissions: List = None, IpProtocol: str = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None, ToPort: int = None, DryRun: bool = None):
        """
        
        Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.
        
        [EC2-Classic] This action gives one or more IPv4 CIDR address ranges permission to access a security group in your account, or gives one or more security groups (called the *source groups* ) permission to access a security group for your account. A source group can be for your own AWS account, or another. You can have up to 100 rules per group.
        
        [EC2-VPC] This action gives one or more IPv4 or IPv6 CIDR address ranges permission to access a security group in your VPC, or gives one or more other security groups (called the *source groups* ) permission to access a security group for your VPC. The security groups must all be for the same VPC or a peer VPC in a VPC peering connection. For more information about VPC security group limits, see `Amazon VPC Limits <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.html>`__ .
        
        You can optionally specify a description for the security group rule.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AuthorizeSecurityGroupIngress>`_
        
        **Request Syntax** 
        ::
        
          response = security_group.authorize_ingress(
              CidrIp=\'string\',
              FromPort=123,
              GroupName=\'string\',
              IpPermissions=[
                  {
                      \'FromPort\': 123,
                      \'IpProtocol\': \'string\',
                      \'IpRanges\': [
                          {
                              \'CidrIp\': \'string\',
                              \'Description\': \'string\'
                          },
                      ],
                      \'Ipv6Ranges\': [
                          {
                              \'CidrIpv6\': \'string\',
                              \'Description\': \'string\'
                          },
                      ],
                      \'PrefixListIds\': [
                          {
                              \'Description\': \'string\',
                              \'PrefixListId\': \'string\'
                          },
                      ],
                      \'ToPort\': 123,
                      \'UserIdGroupPairs\': [
                          {
                              \'Description\': \'string\',
                              \'GroupId\': \'string\',
                              \'GroupName\': \'string\',
                              \'PeeringStatus\': \'string\',
                              \'UserId\': \'string\',
                              \'VpcId\': \'string\',
                              \'VpcPeeringConnectionId\': \'string\'
                          },
                      ]
                  },
              ],
              IpProtocol=\'string\',
              SourceSecurityGroupName=\'string\',
              SourceSecurityGroupOwnerId=\'string\',
              ToPort=123,
              DryRun=True|False
          )
        :type CidrIp: string
        :param CidrIp: 
        
          The CIDR IPv4 address range. You can\'t specify this parameter when specifying a source security group.
        
        :type FromPort: integer
        :param FromPort: 
        
          The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. For the ICMP/ICMPv6 type number, use ``-1`` to specify all types. If you specify all ICMP/ICMPv6 types, you must specify all codes.
        
        :type GroupName: string
        :param GroupName: 
        
          [EC2-Classic, default VPC] The name of the security group. You must specify either the security group ID or the security group name in the request.
        
        :type IpPermissions: list
        :param IpPermissions: 
        
          One or more sets of IP permissions. Can be used to specify multiple rules in a single command.
        
          - *(dict) --* 
        
            Describes a set of permissions for a security group rule.
        
            - **FromPort** *(integer) --* 
        
              The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of ``-1`` indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.
        
            - **IpProtocol** *(string) --* 
        
              The IP protocol name (``tcp`` , ``udp`` , ``icmp`` ) or number (see `Protocol Numbers <http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml>`__ ). 
        
              [EC2-VPC only] Use ``-1`` to specify all protocols. When authorizing security group rules, specifying ``-1`` or a protocol number other than ``tcp`` , ``udp`` , ``icmp`` , or ``58`` (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For ``tcp`` , ``udp`` , and ``icmp`` , you must specify a port range. For ``58`` (ICMPv6), you can optionally specify a port range; if you don\'t, traffic for all types and codes is allowed when authorizing rules. 
        
            - **IpRanges** *(list) --* 
        
              One or more IPv4 ranges.
        
              - *(dict) --* 
        
                Describes an IPv4 range.
        
                - **CidrIp** *(string) --* 
        
                  The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this IPv4 address range.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
            - **Ipv6Ranges** *(list) --* 
        
              [EC2-VPC only] One or more IPv6 ranges.
        
              - *(dict) --* 
        
                [EC2-VPC only] Describes an IPv6 range.
        
                - **CidrIpv6** *(string) --* 
        
                  The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this IPv6 address range.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
            - **PrefixListIds** *(list) --* 
        
              [EC2-VPC only] One or more prefix list IDs for an AWS service. With  AuthorizeSecurityGroupEgress , this is the AWS service that you want to access through a VPC endpoint from instances associated with the security group.
        
              - *(dict) --* 
        
                Describes a prefix list ID.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this prefix list ID.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
                - **PrefixListId** *(string) --* 
        
                  The ID of the prefix.
        
            - **ToPort** *(integer) --* 
        
              The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of ``-1`` indicates all ICMP/ICMPv6 codes for the specified ICMP type. If you specify all ICMP/ICMPv6 types, you must specify all codes.
        
            - **UserIdGroupPairs** *(list) --* 
        
              One or more security group and AWS account ID pairs.
        
              - *(dict) --* 
        
                Describes a security group and AWS account ID pair.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this user ID group pair.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
                - **GroupId** *(string) --* 
        
                  The ID of the security group.
        
                - **GroupName** *(string) --* 
        
                  The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID. 
        
                  For a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.
        
                - **PeeringStatus** *(string) --* 
        
                  The status of a VPC peering connection, if applicable.
        
                - **UserId** *(string) --* 
        
                  The ID of an AWS account.
        
                  For a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.
        
                  [EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account.
        
                - **VpcId** *(string) --* 
        
                  The ID of the VPC for the referenced security group, if applicable.
        
                - **VpcPeeringConnectionId** *(string) --* 
        
                  The ID of the VPC peering connection, if applicable.
        
        :type IpProtocol: string
        :param IpProtocol: 
        
          The IP protocol name (``tcp`` , ``udp`` , ``icmp`` ) or number (see `Protocol Numbers <http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml>`__ ). (VPC only) Use ``-1`` to specify all protocols. If you specify ``-1`` , or a protocol number other than ``tcp`` , ``udp`` , ``icmp`` , or ``58`` (ICMPv6), traffic on all ports is allowed, regardless of any ports you specify. For ``tcp`` , ``udp`` , and ``icmp`` , you must specify a port range. For protocol ``58`` (ICMPv6), you can optionally specify a port range; if you don\'t, traffic for all types and codes is allowed.
        
        :type SourceSecurityGroupName: string
        :param SourceSecurityGroupName: 
        
          [EC2-Classic, default VPC] The name of the source security group. You can\'t specify this parameter in combination with the following parameters: the CIDR IP address range, the start of the port range, the IP protocol, and the end of the port range. Creates rules that grant full ICMP, UDP, and TCP access. To create a rule with a specific IP protocol and port range, use a set of IP permissions instead. For EC2-VPC, the source security group must be in the same VPC.
        
        :type SourceSecurityGroupOwnerId: string
        :param SourceSecurityGroupOwnerId: 
        
          [EC2-Classic] The AWS account ID for the source security group, if the source security group is in a different account. You can\'t specify this parameter in combination with the following parameters: the CIDR IP address range, the IP protocol, the start of the port range, and the end of the port range. Creates rules that grant full ICMP, UDP, and TCP access. To create a rule with a specific IP protocol and port range, use a set of IP permissions instead.
        
        :type ToPort: integer
        :param ToPort: 
        
          The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code number. For the ICMP/ICMPv6 code number, use ``-1`` to specify all codes. If you specify all ICMP/ICMPv6 types, you must specify all codes.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        """
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . For more information about creating IAM policies that control users\' access to resources based on tags, see `Supported Resource-Level Permissions for Amazon EC2 API Actions <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          tag = security_group.create_tags(
              DryRun=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. The ``value`` parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 
        
          - *(dict) --* 
        
            Describes a tag.
        
            - **Key** *(string) --* 
        
              The key of the tag.
        
              Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
              Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :rtype: list(:py:class:`ec2.Tag`)
        :returns: A list of Tag resources
        """
        pass

    def delete(self, GroupName: str = None, DryRun: bool = None):
        """
        
        If you attempt to delete a security group that is associated with an instance, or is referenced by another security group, the operation fails with ``InvalidGroup.InUse`` in EC2-Classic or ``DependencyViolation`` in EC2-VPC.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteSecurityGroup>`_
        
        **Request Syntax** 
        ::
        
          response = security_group.delete(
              GroupName=\'string\',
              DryRun=True|False
          )
        :type GroupName: string
        :param GroupName: 
        
          [EC2-Classic, default VPC] The name of the security group. You can specify either the security group name or the security group ID.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          security_group.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          security_group.load()
        :returns: None
        """
        pass

    def revoke_egress(self, DryRun: bool = None, IpPermissions: List = None, CidrIp: str = None, FromPort: int = None, IpProtocol: str = None, ToPort: int = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None):
        """
        
        Each rule consists of the protocol and the IPv4 or IPv6 CIDR range or source security group. For the TCP and UDP protocols, you must also specify the destination port or range of ports. For the ICMP protocol, you must also specify the ICMP type and code. If the security group rule has a description, you do not have to specify the description to revoke the rule.
        
        Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/RevokeSecurityGroupEgress>`_
        
        **Request Syntax** 
        ::
        
          response = security_group.revoke_egress(
              DryRun=True|False,
              IpPermissions=[
                  {
                      \'FromPort\': 123,
                      \'IpProtocol\': \'string\',
                      \'IpRanges\': [
                          {
                              \'CidrIp\': \'string\',
                              \'Description\': \'string\'
                          },
                      ],
                      \'Ipv6Ranges\': [
                          {
                              \'CidrIpv6\': \'string\',
                              \'Description\': \'string\'
                          },
                      ],
                      \'PrefixListIds\': [
                          {
                              \'Description\': \'string\',
                              \'PrefixListId\': \'string\'
                          },
                      ],
                      \'ToPort\': 123,
                      \'UserIdGroupPairs\': [
                          {
                              \'Description\': \'string\',
                              \'GroupId\': \'string\',
                              \'GroupName\': \'string\',
                              \'PeeringStatus\': \'string\',
                              \'UserId\': \'string\',
                              \'VpcId\': \'string\',
                              \'VpcPeeringConnectionId\': \'string\'
                          },
                      ]
                  },
              ],
              CidrIp=\'string\',
              FromPort=123,
              IpProtocol=\'string\',
              ToPort=123,
              SourceSecurityGroupName=\'string\',
              SourceSecurityGroupOwnerId=\'string\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type IpPermissions: list
        :param IpPermissions: 
        
          One or more sets of IP permissions. You can\'t specify a destination security group and a CIDR IP address range in the same set of permissions.
        
          - *(dict) --* 
        
            Describes a set of permissions for a security group rule.
        
            - **FromPort** *(integer) --* 
        
              The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of ``-1`` indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.
        
            - **IpProtocol** *(string) --* 
        
              The IP protocol name (``tcp`` , ``udp`` , ``icmp`` ) or number (see `Protocol Numbers <http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml>`__ ). 
        
              [EC2-VPC only] Use ``-1`` to specify all protocols. When authorizing security group rules, specifying ``-1`` or a protocol number other than ``tcp`` , ``udp`` , ``icmp`` , or ``58`` (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For ``tcp`` , ``udp`` , and ``icmp`` , you must specify a port range. For ``58`` (ICMPv6), you can optionally specify a port range; if you don\'t, traffic for all types and codes is allowed when authorizing rules. 
        
            - **IpRanges** *(list) --* 
        
              One or more IPv4 ranges.
        
              - *(dict) --* 
        
                Describes an IPv4 range.
        
                - **CidrIp** *(string) --* 
        
                  The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this IPv4 address range.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
            - **Ipv6Ranges** *(list) --* 
        
              [EC2-VPC only] One or more IPv6 ranges.
        
              - *(dict) --* 
        
                [EC2-VPC only] Describes an IPv6 range.
        
                - **CidrIpv6** *(string) --* 
        
                  The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this IPv6 address range.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
            - **PrefixListIds** *(list) --* 
        
              [EC2-VPC only] One or more prefix list IDs for an AWS service. With  AuthorizeSecurityGroupEgress , this is the AWS service that you want to access through a VPC endpoint from instances associated with the security group.
        
              - *(dict) --* 
        
                Describes a prefix list ID.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this prefix list ID.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
                - **PrefixListId** *(string) --* 
        
                  The ID of the prefix.
        
            - **ToPort** *(integer) --* 
        
              The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of ``-1`` indicates all ICMP/ICMPv6 codes for the specified ICMP type. If you specify all ICMP/ICMPv6 types, you must specify all codes.
        
            - **UserIdGroupPairs** *(list) --* 
        
              One or more security group and AWS account ID pairs.
        
              - *(dict) --* 
        
                Describes a security group and AWS account ID pair.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this user ID group pair.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
                - **GroupId** *(string) --* 
        
                  The ID of the security group.
        
                - **GroupName** *(string) --* 
        
                  The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID. 
        
                  For a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.
        
                - **PeeringStatus** *(string) --* 
        
                  The status of a VPC peering connection, if applicable.
        
                - **UserId** *(string) --* 
        
                  The ID of an AWS account.
        
                  For a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.
        
                  [EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account.
        
                - **VpcId** *(string) --* 
        
                  The ID of the VPC for the referenced security group, if applicable.
        
                - **VpcPeeringConnectionId** *(string) --* 
        
                  The ID of the VPC peering connection, if applicable.
        
        :type CidrIp: string
        :param CidrIp: 
        
          Not supported. Use a set of IP permissions to specify the CIDR.
        
        :type FromPort: integer
        :param FromPort: 
        
          Not supported. Use a set of IP permissions to specify the port.
        
        :type IpProtocol: string
        :param IpProtocol: 
        
          Not supported. Use a set of IP permissions to specify the protocol name or number.
        
        :type ToPort: integer
        :param ToPort: 
        
          Not supported. Use a set of IP permissions to specify the port.
        
        :type SourceSecurityGroupName: string
        :param SourceSecurityGroupName: 
        
          Not supported. Use a set of IP permissions to specify a destination security group.
        
        :type SourceSecurityGroupOwnerId: string
        :param SourceSecurityGroupOwnerId: 
        
          Not supported. Use a set of IP permissions to specify a destination security group.
        
        :returns: None
        """
        pass

    def revoke_ingress(self, CidrIp: str = None, FromPort: int = None, GroupName: str = None, IpPermissions: List = None, IpProtocol: str = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None, ToPort: int = None, DryRun: bool = None):
        """
        
        .. note::
        
          [EC2-Classic security groups only] If the values you specify do not match the existing rule\'s values, no error is returned. Use  DescribeSecurityGroups to verify that the rule has been removed.
        
        Each rule consists of the protocol and the CIDR range or source security group. For the TCP and UDP protocols, you must also specify the destination port or range of ports. For the ICMP protocol, you must also specify the ICMP type and code. If the security group rule has a description, you do not have to specify the description to revoke the rule.
        
        Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/RevokeSecurityGroupIngress>`_
        
        **Request Syntax** 
        ::
        
          response = security_group.revoke_ingress(
              CidrIp=\'string\',
              FromPort=123,
              GroupName=\'string\',
              IpPermissions=[
                  {
                      \'FromPort\': 123,
                      \'IpProtocol\': \'string\',
                      \'IpRanges\': [
                          {
                              \'CidrIp\': \'string\',
                              \'Description\': \'string\'
                          },
                      ],
                      \'Ipv6Ranges\': [
                          {
                              \'CidrIpv6\': \'string\',
                              \'Description\': \'string\'
                          },
                      ],
                      \'PrefixListIds\': [
                          {
                              \'Description\': \'string\',
                              \'PrefixListId\': \'string\'
                          },
                      ],
                      \'ToPort\': 123,
                      \'UserIdGroupPairs\': [
                          {
                              \'Description\': \'string\',
                              \'GroupId\': \'string\',
                              \'GroupName\': \'string\',
                              \'PeeringStatus\': \'string\',
                              \'UserId\': \'string\',
                              \'VpcId\': \'string\',
                              \'VpcPeeringConnectionId\': \'string\'
                          },
                      ]
                  },
              ],
              IpProtocol=\'string\',
              SourceSecurityGroupName=\'string\',
              SourceSecurityGroupOwnerId=\'string\',
              ToPort=123,
              DryRun=True|False
          )
        :type CidrIp: string
        :param CidrIp: 
        
          The CIDR IP address range. You can\'t specify this parameter when specifying a source security group.
        
        :type FromPort: integer
        :param FromPort: 
        
          The start of port range for the TCP and UDP protocols, or an ICMP type number. For the ICMP type number, use ``-1`` to specify all ICMP types.
        
        :type GroupName: string
        :param GroupName: 
        
          [EC2-Classic, default VPC] The name of the security group. You must specify either the security group ID or the security group name in the request.
        
        :type IpPermissions: list
        :param IpPermissions: 
        
          One or more sets of IP permissions. You can\'t specify a source security group and a CIDR IP address range in the same set of permissions.
        
          - *(dict) --* 
        
            Describes a set of permissions for a security group rule.
        
            - **FromPort** *(integer) --* 
        
              The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of ``-1`` indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.
        
            - **IpProtocol** *(string) --* 
        
              The IP protocol name (``tcp`` , ``udp`` , ``icmp`` ) or number (see `Protocol Numbers <http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml>`__ ). 
        
              [EC2-VPC only] Use ``-1`` to specify all protocols. When authorizing security group rules, specifying ``-1`` or a protocol number other than ``tcp`` , ``udp`` , ``icmp`` , or ``58`` (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For ``tcp`` , ``udp`` , and ``icmp`` , you must specify a port range. For ``58`` (ICMPv6), you can optionally specify a port range; if you don\'t, traffic for all types and codes is allowed when authorizing rules. 
        
            - **IpRanges** *(list) --* 
        
              One or more IPv4 ranges.
        
              - *(dict) --* 
        
                Describes an IPv4 range.
        
                - **CidrIp** *(string) --* 
        
                  The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this IPv4 address range.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
            - **Ipv6Ranges** *(list) --* 
        
              [EC2-VPC only] One or more IPv6 ranges.
        
              - *(dict) --* 
        
                [EC2-VPC only] Describes an IPv6 range.
        
                - **CidrIpv6** *(string) --* 
        
                  The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this IPv6 address range.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
            - **PrefixListIds** *(list) --* 
        
              [EC2-VPC only] One or more prefix list IDs for an AWS service. With  AuthorizeSecurityGroupEgress , this is the AWS service that you want to access through a VPC endpoint from instances associated with the security group.
        
              - *(dict) --* 
        
                Describes a prefix list ID.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this prefix list ID.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
                - **PrefixListId** *(string) --* 
        
                  The ID of the prefix.
        
            - **ToPort** *(integer) --* 
        
              The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of ``-1`` indicates all ICMP/ICMPv6 codes for the specified ICMP type. If you specify all ICMP/ICMPv6 types, you must specify all codes.
        
            - **UserIdGroupPairs** *(list) --* 
        
              One or more security group and AWS account ID pairs.
        
              - *(dict) --* 
        
                Describes a security group and AWS account ID pair.
        
                - **Description** *(string) --* 
        
                  A description for the security group rule that references this user ID group pair.
        
                  Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
        
                - **GroupId** *(string) --* 
        
                  The ID of the security group.
        
                - **GroupName** *(string) --* 
        
                  The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID. 
        
                  For a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.
        
                - **PeeringStatus** *(string) --* 
        
                  The status of a VPC peering connection, if applicable.
        
                - **UserId** *(string) --* 
        
                  The ID of an AWS account.
        
                  For a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.
        
                  [EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account.
        
                - **VpcId** *(string) --* 
        
                  The ID of the VPC for the referenced security group, if applicable.
        
                - **VpcPeeringConnectionId** *(string) --* 
        
                  The ID of the VPC peering connection, if applicable.
        
        :type IpProtocol: string
        :param IpProtocol: 
        
          The IP protocol name (``tcp`` , ``udp`` , ``icmp`` ) or number (see `Protocol Numbers <http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml>`__ ). Use ``-1`` to specify all.
        
        :type SourceSecurityGroupName: string
        :param SourceSecurityGroupName: 
        
          [EC2-Classic, default VPC] The name of the source security group. You can\'t specify this parameter in combination with the following parameters: the CIDR IP address range, the start of the port range, the IP protocol, and the end of the port range. For EC2-VPC, the source security group must be in the same VPC. To revoke a specific rule for an IP protocol and port range, use a set of IP permissions instead.
        
        :type SourceSecurityGroupOwnerId: string
        :param SourceSecurityGroupOwnerId: 
        
          [EC2-Classic] The AWS account ID of the source security group, if the source security group is in a different account. You can\'t specify this parameter in combination with the following parameters: the CIDR IP address range, the IP protocol, the start of the port range, and the end of the port range. To revoke a specific rule for an IP protocol and port range, use a set of IP permissions instead.
        
        :type ToPort: integer
        :param ToPort: 
        
          The end of port range for the TCP and UDP protocols, or an ICMP code number. For the ICMP code number, use ``-1`` to specify all ICMP codes for the ICMP type.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
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
        """
        
        Copies of encrypted EBS snapshots remain encrypted. Copies of unencrypted snapshots remain unencrypted, unless the ``Encrypted`` flag is specified during the snapshot copy operation. By default, encrypted snapshot copies use the default AWS Key Management Service (AWS KMS) customer master key (CMK); however, you can specify a non-default CMK with the ``KmsKeyId`` parameter.
        
        To copy an encrypted snapshot that has been shared from another account, you must have permissions for the CMK used to encrypt the snapshot.
        
        Snapshots created by copying another snapshot have an arbitrary volume ID that should not be used for any purpose.
        
        For more information, see `Copying an Amazon EBS Snapshot <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-copy-snapshot.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CopySnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = snapshot.copy(
              Description=\'string\',
              Encrypted=True|False,
              KmsKeyId=\'string\',
              SourceRegion=\'string\',
              DryRun=True|False
          )
        :type Description: string
        :param Description: 
        
          A description for the EBS snapshot.
        
        :type DestinationRegion: string
        :param DestinationRegion: 
        
          The destination region to use in the ``PresignedUrl`` parameter of a snapshot copy operation. This parameter is only valid for specifying the destination region in a ``PresignedUrl`` parameter, where it is required.
        
          The snapshot copy is sent to the regional endpoint that you sent the HTTP request to (for example, ``ec2.us-east-1.amazonaws.com`` ). With the AWS CLI, this is specified using the ``--region`` parameter or the default region in your AWS configuration file.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type Encrypted: boolean
        :param Encrypted: 
        
          Specifies whether the destination snapshot should be encrypted. You can encrypt a copy of an unencrypted snapshot, but you cannot use it to create an unencrypted copy of an encrypted snapshot. Your default CMK for EBS is used unless you specify a non-default AWS Key Management Service (AWS KMS) CMK using ``KmsKeyId`` . For more information, see `Amazon EBS Encryption <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          An identifier for the AWS Key Management Service (AWS KMS) customer master key (CMK) to use when creating the encrypted volume. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. If a ``KmsKeyId`` is specified, the ``Encrypted`` flag must also be set. 
        
          The CMK identifier may be provided in any of the following formats: 
        
          * Key ID 
           
          * Key alias 
           
          * ARN using key ID. The ID ARN contains the ``arn:aws:kms`` namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the ``key`` namespace, and then the CMK ID. For example, arn:aws:kms:*us-east-1* :*012345678910* :key/*abcd1234-a123-456a-a12b-a123b4cd56ef* .  
           
          * ARN using key alias. The alias ARN contains the ``arn:aws:kms`` namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the ``alias`` namespace, and then the CMK alias. For example, arn:aws:kms:*us-east-1* :*012345678910* :alias/*ExampleAlias* .  
           
          AWS parses ``KmsKeyId`` asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. The action will eventually fail. 
        
        :type PresignedUrl: string
        :param PresignedUrl: 
        
          When you copy an encrypted source snapshot using the Amazon EC2 Query API, you must supply a pre-signed URL. This parameter is optional for unencrypted snapshots. For more information, see `Query Requests <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html>`__ .
        
          The ``PresignedUrl`` should use the snapshot source endpoint, the ``CopySnapshot`` action, and include the ``SourceRegion`` , ``SourceSnapshotId`` , and ``DestinationRegion`` parameters. The ``PresignedUrl`` must be signed using AWS Signature Version 4. Because EBS snapshots are stored in Amazon S3, the signing algorithm for this parameter uses the same logic that is described in `Authenticating Requests by Using Query Parameters (AWS Signature Version 4) <http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html>`__ in the *Amazon Simple Storage Service API Reference* . An invalid or improperly signed ``PresignedUrl`` will cause the copy operation to fail asynchronously, and the snapshot will move to an ``error`` state.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type SourceRegion: string
        :param SourceRegion: **[REQUIRED]** 
        
          The ID of the region that contains the snapshot to be copied.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SnapshotId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of CopySnapshot.
        
            - **SnapshotId** *(string) --* 
        
              The ID of the new snapshot.
        
        """
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        """
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . For more information about creating IAM policies that control users\' access to resources based on tags, see `Supported Resource-Level Permissions for Amazon EC2 API Actions <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          tag = snapshot.create_tags(
              DryRun=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. The ``value`` parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 
        
          - *(dict) --* 
        
            Describes a tag.
        
            - **Key** *(string) --* 
        
              The key of the tag.
        
              Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
              Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :rtype: list(:py:class:`ec2.Tag`)
        :returns: A list of Tag resources
        """
        pass

    def delete(self, DryRun: bool = None):
        """
        
        When you make periodic snapshots of a volume, the snapshots are incremental, and only the blocks on the device that have changed since your last snapshot are saved in the new snapshot. When you delete a snapshot, only the data not needed for any other snapshot is removed. So regardless of which prior snapshots have been deleted, all active snapshots will have access to all the information needed to restore the volume.
        
        You cannot delete a snapshot of the root device of an EBS volume used by a registered AMI. You must first de-register the AMI before you can delete the snapshot.
        
        For more information, see `Deleting an Amazon EBS Snapshot <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-deleting-snapshot.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = snapshot.delete(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict:
        """
        
        For more information about EBS snapshots, see `Amazon EBS Snapshots <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSnapshotAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = snapshot.describe_attribute(
              Attribute=\'productCodes\'|\'createVolumePermission\',
              DryRun=True|False
          )
        :type Attribute: string
        :param Attribute: **[REQUIRED]** 
        
          The snapshot attribute you would like to view.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CreateVolumePermissions\': [
                    {
                        \'Group\': \'all\',
                        \'UserId\': \'string\'
                    },
                ],
                \'ProductCodes\': [
                    {
                        \'ProductCodeId\': \'string\',
                        \'ProductCodeType\': \'devpay\'|\'marketplace\'
                    },
                ],
                \'SnapshotId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DescribeSnapshotAttribute.
        
            - **CreateVolumePermissions** *(list) --* 
        
              A list of permissions for creating volumes from the snapshot.
        
              - *(dict) --* 
        
                Describes the user or group to be added or removed from the permissions for a volume.
        
                - **Group** *(string) --* 
        
                  The specific group that is to be added or removed from a volume\'s list of create volume permissions.
        
                - **UserId** *(string) --* 
        
                  The specific AWS account ID that is to be added or removed from a volume\'s list of create volume permissions.
        
            - **ProductCodes** *(list) --* 
        
              A list of product codes.
        
              - *(dict) --* 
        
                Describes a product code.
        
                - **ProductCodeId** *(string) --* 
        
                  The product code.
        
                - **ProductCodeType** *(string) --* 
        
                  The type of product code.
        
            - **SnapshotId** *(string) --* 
        
              The ID of the EBS snapshot.
        
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          snapshot.load()
        :returns: None
        """
        pass

    def modify_attribute(self, Attribute: str = None, CreateVolumePermission: Dict = None, GroupNames: List = None, OperationType: str = None, UserIds: List = None, DryRun: bool = None):
        """
        
        Encrypted snapshots and snapshots with AWS Marketplace product codes cannot be made public. Snapshots encrypted with your default CMK cannot be shared with other accounts.
        
        For more information about modifying snapshot permissions, see `Sharing Snapshots <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifySnapshotAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = snapshot.modify_attribute(
              Attribute=\'productCodes\'|\'createVolumePermission\',
              CreateVolumePermission={
                  \'Add\': [
                      {
                          \'Group\': \'all\',
                          \'UserId\': \'string\'
                      },
                  ],
                  \'Remove\': [
                      {
                          \'Group\': \'all\',
                          \'UserId\': \'string\'
                      },
                  ]
              },
              GroupNames=[
                  \'string\',
              ],
              OperationType=\'add\'|\'remove\',
              UserIds=[
                  \'string\',
              ],
              DryRun=True|False
          )
        :type Attribute: string
        :param Attribute: 
        
          The snapshot attribute to modify. Only volume creation permissions can be modified.
        
        :type CreateVolumePermission: dict
        :param CreateVolumePermission: 
        
          A JSON representation of the snapshot attribute modification.
        
          - **Add** *(list) --* 
        
            Adds a specific AWS account ID or group to a volume\'s list of create volume permissions.
        
            - *(dict) --* 
        
              Describes the user or group to be added or removed from the permissions for a volume.
        
              - **Group** *(string) --* 
        
                The specific group that is to be added or removed from a volume\'s list of create volume permissions.
        
              - **UserId** *(string) --* 
        
                The specific AWS account ID that is to be added or removed from a volume\'s list of create volume permissions.
        
          - **Remove** *(list) --* 
        
            Removes a specific AWS account ID or group from a volume\'s list of create volume permissions.
        
            - *(dict) --* 
        
              Describes the user or group to be added or removed from the permissions for a volume.
        
              - **Group** *(string) --* 
        
                The specific group that is to be added or removed from a volume\'s list of create volume permissions.
        
              - **UserId** *(string) --* 
        
                The specific AWS account ID that is to be added or removed from a volume\'s list of create volume permissions.
        
        :type GroupNames: list
        :param GroupNames: 
        
          The group to modify for the snapshot.
        
          - *(string) --* 
        
        :type OperationType: string
        :param OperationType: 
        
          The type of operation to perform to the attribute.
        
        :type UserIds: list
        :param UserIds: 
        
          The account ID to modify for the snapshot.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          snapshot.load()
        :returns: None
        """
        pass

    def reset_attribute(self, Attribute: str, DryRun: bool = None):
        """
        
        For more information about modifying snapshot permissions, see `Sharing Snapshots <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ResetSnapshotAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = snapshot.reset_attribute(
              Attribute=\'productCodes\'|\'createVolumePermission\',
              DryRun=True|False
          )
        :type Attribute: string
        :param Attribute: **[REQUIRED]** 
        
          The attribute to reset. Currently, only the attribute for permission to create volumes can be reset.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def wait_until_completed(self, Filters: List = None, MaxResults: int = None, NextToken: str = None, OwnerIds: List = None, RestorableByUserIds: List = None, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSnapshots>`_
        
        **Request Syntax** 
        ::
        
          snapshot.wait_until_completed(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\',
              OwnerIds=[
                  \'string\',
              ],
              RestorableByUserIds=[
                  \'string\',
              ],
              DryRun=True|False
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``description`` - A description of the snapshot. 
           
          * ``owner-alias`` - Value from an Amazon-maintained list (``amazon`` | ``aws-marketplace`` | ``microsoft`` ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM console. 
           
          * ``owner-id`` - The ID of the AWS account that owns the snapshot. 
           
          * ``progress`` - The progress of the snapshot, as a percentage (for example, 80%). 
           
          * ``snapshot-id`` - The snapshot ID. 
           
          * ``start-time`` - The time stamp when the snapshot was initiated. 
           
          * ``status`` - The status of the snapshot (``pending`` | ``completed`` | ``error`` ). 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``volume-id`` - The ID of the volume the snapshot is for. 
           
          * ``volume-size`` - The size of the volume, in GiB. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of snapshot results returned by ``DescribeSnapshots`` in paginated output. When this parameter is used, ``DescribeSnapshots`` only returns ``MaxResults`` results in a single page along with a ``NextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeSnapshots`` request with the returned ``NextToken`` value. This value can be between 5 and 1000; if ``MaxResults`` is given a value larger than 1000, only 1000 results are returned. If this parameter is not used, then ``DescribeSnapshots`` returns all results. You cannot specify this parameter and the snapshot IDs parameter in the same request.
        
        :type NextToken: string
        :param NextToken: 
        
          The ``NextToken`` value returned from a previous paginated ``DescribeSnapshots`` request where ``MaxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``NextToken`` value. This value is ``null`` when there are no more results to return.
        
        :type OwnerIds: list
        :param OwnerIds: 
        
          Returns the snapshots owned by the specified owner. Multiple owners can be specified.
        
          - *(string) --* 
        
        :type RestorableByUserIds: list
        :param RestorableByUserIds: 
        
          One or more AWS accounts IDs that can create volumes from the snapshot.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
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
        """
        
        You can specify a number of options, or leave the default options. The following rules apply:
        
        * [EC2-VPC] If you don\'t specify a subnet ID, we choose a default subnet from your default VPC for you. If you don\'t have a default VPC, you must specify a subnet ID in the request. 
         
        * [EC2-Classic] If don\'t specify an Availability Zone, we choose one for you. 
         
        * Some instance types must be launched into a VPC. If you do not have a default VPC, or if you do not specify a subnet ID, the request fails. For more information, see `Instance Types Available Only in a VPC <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-vpc.html#vpc-only-instance-types>`__ . 
         
        * [EC2-VPC] All instances have a network interface with a primary private IPv4 address. If you don\'t specify this address, we choose one from the IPv4 range of your subnet. 
         
        * Not all instance types support IPv6 addresses. For more information, see `Instance Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`__ . 
         
        * If you don\'t specify a security group ID, we use the default security group. For more information, see `Security Groups <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html>`__ . 
         
        * If any of the AMIs have a product code attached for which the user has not subscribed, the request fails. 
         
        You can create a `launch template <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html>`__ , which is a resource that contains the parameters to launch an instance. When you launch an instance using  RunInstances , you can specify the launch template instead of specifying the launch parameters.
        
        To ensure faster instance launches, break up large requests into smaller batches. For example, create five separate launch requests for 100 instances each instead of one launch request for 500 instances.
        
        An instance is ready for you to use when it\'s in the ``running`` state. You can check the state of your instance using  DescribeInstances . You can tag instances and EBS volumes during launch, after launch, or both. For more information, see  CreateTags and `Tagging Your Amazon EC2 Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ .
        
        Linux instances have access to the public key of the key pair at boot. You can use this key to provide secure access to the instance. Amazon EC2 public images use this feature to provide secure access without passwords. For more information, see `Key Pairs <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        For troubleshooting, see `What To Do If An Instance Immediately Terminates <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_InstanceStraightToTerminated.html>`__ , and `Troubleshooting Connecting to Your Instance <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/RunInstances>`_
        
        **Request Syntax** 
        ::
        
          instance = subnet.create_instances(
              BlockDeviceMappings=[
                  {
                      \'DeviceName\': \'string\',
                      \'VirtualName\': \'string\',
                      \'Ebs\': {
                          \'DeleteOnTermination\': True|False,
                          \'Iops\': 123,
                          \'SnapshotId\': \'string\',
                          \'VolumeSize\': 123,
                          \'VolumeType\': \'standard\'|\'io1\'|\'gp2\'|\'sc1\'|\'st1\',
                          \'Encrypted\': True|False,
                          \'KmsKeyId\': \'string\'
                      },
                      \'NoDevice\': \'string\'
                  },
              ],
              ImageId=\'string\',
              InstanceType=\'t1.micro\'|\'t2.nano\'|\'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'t2.xlarge\'|\'t2.2xlarge\'|\'t3.nano\'|\'t3.micro\'|\'t3.small\'|\'t3.medium\'|\'t3.large\'|\'t3.xlarge\'|\'t3.2xlarge\'|\'m1.small\'|\'m1.medium\'|\'m1.large\'|\'m1.xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\'|\'m4.16xlarge\'|\'m2.xlarge\'|\'m2.2xlarge\'|\'m2.4xlarge\'|\'cr1.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'r5.large\'|\'r5.xlarge\'|\'r5.2xlarge\'|\'r5.4xlarge\'|\'r5.8xlarge\'|\'r5.12xlarge\'|\'r5.16xlarge\'|\'r5.24xlarge\'|\'r5.metal\'|\'r5a.large\'|\'r5a.xlarge\'|\'r5a.2xlarge\'|\'r5a.4xlarge\'|\'r5a.12xlarge\'|\'r5a.24xlarge\'|\'r5d.large\'|\'r5d.xlarge\'|\'r5d.2xlarge\'|\'r5d.4xlarge\'|\'r5d.8xlarge\'|\'r5d.12xlarge\'|\'r5d.16xlarge\'|\'r5d.24xlarge\'|\'r5d.metal\'|\'x1.16xlarge\'|\'x1.32xlarge\'|\'x1e.xlarge\'|\'x1e.2xlarge\'|\'x1e.4xlarge\'|\'x1e.8xlarge\'|\'x1e.16xlarge\'|\'x1e.32xlarge\'|\'i2.xlarge\'|\'i2.2xlarge\'|\'i2.4xlarge\'|\'i2.8xlarge\'|\'i3.large\'|\'i3.xlarge\'|\'i3.2xlarge\'|\'i3.4xlarge\'|\'i3.8xlarge\'|\'i3.16xlarge\'|\'i3.metal\'|\'hi1.4xlarge\'|\'hs1.8xlarge\'|\'c1.medium\'|\'c1.xlarge\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'c5.large\'|\'c5.xlarge\'|\'c5.2xlarge\'|\'c5.4xlarge\'|\'c5.9xlarge\'|\'c5.18xlarge\'|\'c5d.large\'|\'c5d.xlarge\'|\'c5d.2xlarge\'|\'c5d.4xlarge\'|\'c5d.9xlarge\'|\'c5d.18xlarge\'|\'cc1.4xlarge\'|\'cc2.8xlarge\'|\'g2.2xlarge\'|\'g2.8xlarge\'|\'g3.4xlarge\'|\'g3.8xlarge\'|\'g3.16xlarge\'|\'g3s.xlarge\'|\'cg1.4xlarge\'|\'p2.xlarge\'|\'p2.8xlarge\'|\'p2.16xlarge\'|\'p3.2xlarge\'|\'p3.8xlarge\'|\'p3.16xlarge\'|\'d2.xlarge\'|\'d2.2xlarge\'|\'d2.4xlarge\'|\'d2.8xlarge\'|\'f1.2xlarge\'|\'f1.4xlarge\'|\'f1.16xlarge\'|\'m5.large\'|\'m5.xlarge\'|\'m5.2xlarge\'|\'m5.4xlarge\'|\'m5.12xlarge\'|\'m5.24xlarge\'|\'m5a.large\'|\'m5a.xlarge\'|\'m5a.2xlarge\'|\'m5a.4xlarge\'|\'m5a.12xlarge\'|\'m5a.24xlarge\'|\'m5d.large\'|\'m5d.xlarge\'|\'m5d.2xlarge\'|\'m5d.4xlarge\'|\'m5d.12xlarge\'|\'m5d.24xlarge\'|\'h1.2xlarge\'|\'h1.4xlarge\'|\'h1.8xlarge\'|\'h1.16xlarge\'|\'z1d.large\'|\'z1d.xlarge\'|\'z1d.2xlarge\'|\'z1d.3xlarge\'|\'z1d.6xlarge\'|\'z1d.12xlarge\'|\'u-6tb1.metal\'|\'u-9tb1.metal\'|\'u-12tb1.metal\',
              Ipv6AddressCount=123,
              Ipv6Addresses=[
                  {
                      \'Ipv6Address\': \'string\'
                  },
              ],
              KernelId=\'string\',
              KeyName=\'string\',
              MaxCount=123,
              MinCount=123,
              Monitoring={
                  \'Enabled\': True|False
              },
              Placement={
                  \'AvailabilityZone\': \'string\',
                  \'Affinity\': \'string\',
                  \'GroupName\': \'string\',
                  \'HostId\': \'string\',
                  \'Tenancy\': \'default\'|\'dedicated\'|\'host\',
                  \'SpreadDomain\': \'string\'
              },
              RamdiskId=\'string\',
              SecurityGroupIds=[
                  \'string\',
              ],
              SecurityGroups=[
                  \'string\',
              ],
              UserData=\'string\',
              AdditionalInfo=\'string\',
              ClientToken=\'string\',
              DisableApiTermination=True|False,
              DryRun=True|False,
              EbsOptimized=True|False,
              IamInstanceProfile={
                  \'Arn\': \'string\',
                  \'Name\': \'string\'
              },
              InstanceInitiatedShutdownBehavior=\'stop\'|\'terminate\',
              NetworkInterfaces=[
                  {
                      \'AssociatePublicIpAddress\': True|False,
                      \'DeleteOnTermination\': True|False,
                      \'Description\': \'string\',
                      \'DeviceIndex\': 123,
                      \'Groups\': [
                          \'string\',
                      ],
                      \'Ipv6AddressCount\': 123,
                      \'Ipv6Addresses\': [
                          {
                              \'Ipv6Address\': \'string\'
                          },
                      ],
                      \'NetworkInterfaceId\': \'string\',
                      \'PrivateIpAddress\': \'string\',
                      \'PrivateIpAddresses\': [
                          {
                              \'Primary\': True|False,
                              \'PrivateIpAddress\': \'string\'
                          },
                      ],
                      \'SecondaryPrivateIpAddressCount\': 123,
                      \'SubnetId\': \'string\'
                  },
              ],
              PrivateIpAddress=\'string\',
              ElasticGpuSpecification=[
                  {
                      \'Type\': \'string\'
                  },
              ],
              TagSpecifications=[
                  {
                      \'ResourceType\': \'customer-gateway\'|\'dedicated-host\'|\'dhcp-options\'|\'image\'|\'instance\'|\'internet-gateway\'|\'network-acl\'|\'network-interface\'|\'reserved-instances\'|\'route-table\'|\'snapshot\'|\'spot-instances-request\'|\'subnet\'|\'security-group\'|\'volume\'|\'vpc\'|\'vpn-connection\'|\'vpn-gateway\',
                      \'Tags\': [
                          {
                              \'Key\': \'string\',
                              \'Value\': \'string\'
                          },
                      ]
                  },
              ],
              LaunchTemplate={
                  \'LaunchTemplateId\': \'string\',
                  \'LaunchTemplateName\': \'string\',
                  \'Version\': \'string\'
              },
              InstanceMarketOptions={
                  \'MarketType\': \'spot\',
                  \'SpotOptions\': {
                      \'MaxPrice\': \'string\',
                      \'SpotInstanceType\': \'one-time\'|\'persistent\',
                      \'BlockDurationMinutes\': 123,
                      \'ValidUntil\': datetime(2015, 1, 1),
                      \'InstanceInterruptionBehavior\': \'hibernate\'|\'stop\'|\'terminate\'
                  }
              },
              CreditSpecification={
                  \'CpuCredits\': \'string\'
              },
              CpuOptions={
                  \'CoreCount\': 123,
                  \'ThreadsPerCore\': 123
              },
              CapacityReservationSpecification={
                  \'CapacityReservationPreference\': \'open\'|\'none\',
                  \'CapacityReservationTarget\': {
                      \'CapacityReservationId\': \'string\'
                  }
              }
          )
        :type BlockDeviceMappings: list
        :param BlockDeviceMappings: 
        
          One or more block device mapping entries. You can\'t specify both a snapshot ID and an encryption value. This is because only blank volumes can be encrypted on creation. If a snapshot is the basis for a volume, it is not blank and its encryption status is used for the volume encryption status.
        
          - *(dict) --* 
        
            Describes a block device mapping.
        
            - **DeviceName** *(string) --* 
        
              The device name (for example, ``/dev/sdh`` or ``xvdh`` ).
        
            - **VirtualName** *(string) --* 
        
              The virtual device name (``ephemeral`` N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ``ephemeral0`` and ``ephemeral1`` . The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
        
              NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect.
        
              Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
        
            - **Ebs** *(dict) --* 
        
              Parameters used to automatically set up EBS volumes when the instance is launched.
        
              - **DeleteOnTermination** *(boolean) --* 
        
                Indicates whether the EBS volume is deleted on instance termination.
        
              - **Iops** *(integer) --* 
        
                The number of I/O operations per second (IOPS) that the volume supports. For ``io1`` , this represents the number of IOPS that are provisioned for the volume. For ``gp2`` , this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see `Amazon EBS Volume Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
                Constraint: Range is 100-20000 IOPS for ``io1`` volumes and 100-10000 IOPS for ``gp2`` volumes.
        
                Condition: This parameter is required for requests to create ``io1`` volumes; it is not used in requests to create ``gp2`` , ``st1`` , ``sc1`` , or ``standard`` volumes.
        
              - **SnapshotId** *(string) --* 
        
                The ID of the snapshot.
        
              - **VolumeSize** *(integer) --* 
        
                The size of the volume, in GiB.
        
                Constraints: 1-16384 for General Purpose SSD (``gp2`` ), 4-16384 for Provisioned IOPS SSD (``io1`` ), 500-16384 for Throughput Optimized HDD (``st1`` ), 500-16384 for Cold HDD (``sc1`` ), and 1-1024 for Magnetic (``standard`` ) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
        
                Default: If you\'re creating the volume from a snapshot and don\'t specify a volume size, the default is the snapshot size.
        
              - **VolumeType** *(string) --* 
        
                The volume type: ``gp2`` , ``io1`` , ``st1`` , ``sc1`` , or ``standard`` .
        
                Default: ``standard``  
        
              - **Encrypted** *(boolean) --* 
        
                Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. 
        
                If you are creating a volume from a snapshot, you cannot specify an encryption value. This is because only blank volumes can be encrypted on creation. If you are creating a snapshot from an existing EBS volume, you cannot specify an encryption value that differs from that of the EBS volume. We recommend that you omit the encryption value from the block device mappings when creating an image from an instance.
        
              - **KmsKeyId** *(string) --* 
        
                Identifier (key ID, key alias, ID ARN, or alias ARN) for a user-managed CMK under which the EBS volume is encrypted.
        
                This parameter is only supported on ``BlockDeviceMapping`` objects called by `RunInstances <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html>`__ , `RequestSpotFleet <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet.html>`__ , and `RequestSpotInstances <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html>`__ .
        
            - **NoDevice** *(string) --* 
        
              Suppresses the specified device included in the block device mapping of the AMI.
        
        :type ImageId: string
        :param ImageId: 
        
          The ID of the AMI, which you can get by calling  DescribeImages . An AMI is required to launch an instance and must be specified here or in a launch template.
        
        :type InstanceType: string
        :param InstanceType: 
        
          The instance type. For more information, see `Instance Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
          Default: ``m1.small``  
        
        :type Ipv6AddressCount: integer
        :param Ipv6AddressCount: 
        
          [EC2-VPC] A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you\'ve specified a minimum number of instances to launch.
        
        :type Ipv6Addresses: list
        :param Ipv6Addresses: 
        
          [EC2-VPC] Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you\'ve specified a minimum number of instances to launch.
        
          - *(dict) --* 
        
            Describes an IPv6 address.
        
            - **Ipv6Address** *(string) --* 
        
              The IPv6 address.
        
        :type KernelId: string
        :param KernelId: 
        
          The ID of the kernel.
        
          .. warning::
        
            We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see `PV-GRUB <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        :type KeyName: string
        :param KeyName: 
        
          The name of the key pair. You can create a key pair using  CreateKeyPair or  ImportKeyPair .
        
          .. warning::
        
            If you do not specify a key pair, you can\'t connect to the instance unless you choose an AMI that is configured to allow users another way to log in.
        
        :type MaxCount: integer
        :param MaxCount: **[REQUIRED]** 
        
          The maximum number of instances to launch. If you specify more instances than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches the largest possible number of instances above ``MinCount`` .
        
          Constraints: Between 1 and the maximum number you\'re allowed for the specified instance type. For more information about the default limits, and how to request an increase, see `How many instances can I run in Amazon EC2 <http://aws.amazon.com/ec2/faqs/#How_many_instances_can_I_run_in_Amazon_EC2>`__ in the Amazon EC2 FAQ.
        
        :type MinCount: integer
        :param MinCount: **[REQUIRED]** 
        
          The minimum number of instances to launch. If you specify a minimum that is more instances than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches no instances.
        
          Constraints: Between 1 and the maximum number you\'re allowed for the specified instance type. For more information about the default limits, and how to request an increase, see `How many instances can I run in Amazon EC2 <http://aws.amazon.com/ec2/faqs/#How_many_instances_can_I_run_in_Amazon_EC2>`__ in the Amazon EC2 General FAQ.
        
        :type Monitoring: dict
        :param Monitoring: 
        
          The monitoring for the instance.
        
          - **Enabled** *(boolean) --* **[REQUIRED]** 
        
            Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
        
        :type Placement: dict
        :param Placement: 
        
          The placement for the instance.
        
          - **AvailabilityZone** *(string) --* 
        
            The Availability Zone of the instance.
        
          - **Affinity** *(string) --* 
        
            The affinity setting for the instance on the Dedicated Host. This parameter is not supported for the  ImportInstance command.
        
          - **GroupName** *(string) --* 
        
            The name of the placement group the instance is in.
        
          - **HostId** *(string) --* 
        
            The ID of the Dedicated Host on which the instance resides. This parameter is not supported for the  ImportInstance command.
        
          - **Tenancy** *(string) --* 
        
            The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of ``dedicated`` runs on single-tenant hardware. The ``host`` tenancy is not supported for the  ImportInstance command.
        
          - **SpreadDomain** *(string) --* 
        
            Reserved for future use.
        
        :type RamdiskId: string
        :param RamdiskId: 
        
          The ID of the RAM disk.
        
          .. warning::
        
            We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see `PV-GRUB <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        :type SecurityGroupIds: list
        :param SecurityGroupIds: 
        
          One or more security group IDs. You can create a security group using  CreateSecurityGroup .
        
          Default: Amazon EC2 uses the default security group.
        
          - *(string) --* 
        
        :type SecurityGroups: list
        :param SecurityGroups: 
        
          [EC2-Classic, default VPC] One or more security group names. For a nondefault VPC, you must use security group IDs instead.
        
          Default: Amazon EC2 uses the default security group.
        
          - *(string) --* 
        
        :type UserData: string
        :param UserData: 
        
          The user data to make available to the instance. For more information, see `Running Commands on Your Linux Instance at Launch <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html>`__ (Linux) and `Adding User Data <http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-instance-metadata.html#instancedata-add-user-data>`__ (Windows). If you are using a command line tool, base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide base64-encoded text.
        
            **This value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.**
        
        :type AdditionalInfo: string
        :param AdditionalInfo: 
        
          Reserved.
        
        :type ClientToken: string
        :param ClientToken: 
        
          Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see `Ensuring Idempotency <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html>`__ .
        
          Constraints: Maximum 64 ASCII characters
        
        :type DisableApiTermination: boolean
        :param DisableApiTermination: 
        
          If you set this parameter to ``true`` , you can\'t terminate the instance using the Amazon EC2 console, CLI, or API; otherwise, you can. To change this attribute to ``false`` after launch, use  ModifyInstanceAttribute . Alternatively, if you set ``InstanceInitiatedShutdownBehavior`` to ``terminate`` , you can terminate the instance by running the shutdown command from the instance.
        
          Default: ``false``  
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type EbsOptimized: boolean
        :param EbsOptimized: 
        
          Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isn\'t available with all instance types. Additional usage charges apply when using an EBS-optimized instance.
        
          Default: ``false``  
        
        :type IamInstanceProfile: dict
        :param IamInstanceProfile: 
        
          The IAM instance profile.
        
          - **Arn** *(string) --* 
        
            The Amazon Resource Name (ARN) of the instance profile.
        
          - **Name** *(string) --* 
        
            The name of the instance profile.
        
        :type InstanceInitiatedShutdownBehavior: string
        :param InstanceInitiatedShutdownBehavior: 
        
          Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
        
          Default: ``stop``  
        
        :type NetworkInterfaces: list
        :param NetworkInterfaces: 
        
          One or more network interfaces.
        
          - *(dict) --* 
        
            Describes a network interface.
        
            - **AssociatePublicIpAddress** *(boolean) --* 
        
              Indicates whether to assign a public IPv4 address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is ``true`` .
        
            - **DeleteOnTermination** *(boolean) --* 
        
              If set to ``true`` , the interface is deleted when the instance is terminated. You can specify ``true`` only if creating a new network interface when launching an instance.
        
            - **Description** *(string) --* 
        
              The description of the network interface. Applies only if creating a network interface when launching an instance.
        
            - **DeviceIndex** *(integer) --* 
        
              The index of the device on the instance for the network interface attachment. If you are specifying a network interface in a  RunInstances request, you must provide the device index.
        
            - **Groups** *(list) --* 
        
              The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.
        
              - *(string) --* 
        
            - **Ipv6AddressCount** *(integer) --* 
        
              A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you\'ve specified a minimum number of instances to launch.
        
            - **Ipv6Addresses** *(list) --* 
        
              One or more IPv6 addresses to assign to the network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you\'ve specified a minimum number of instances to launch.
        
              - *(dict) --* 
        
                Describes an IPv6 address.
        
                - **Ipv6Address** *(string) --* 
        
                  The IPv6 address.
        
            - **NetworkInterfaceId** *(string) --* 
        
              The ID of the network interface.
        
            - **PrivateIpAddress** *(string) --* 
        
              The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you\'re launching more than one instance in a  RunInstances request.
        
            - **PrivateIpAddresses** *(list) --* 
        
              One or more private IPv4 addresses to assign to the network interface. Only one private IPv4 address can be designated as primary. You cannot specify this option if you\'re launching more than one instance in a  RunInstances request.
        
              - *(dict) --* 
        
                Describes a secondary private IPv4 address for a network interface.
        
                - **Primary** *(boolean) --* 
        
                  Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.
        
                - **PrivateIpAddress** *(string) --* 
        
                  The private IPv4 addresses.
        
            - **SecondaryPrivateIpAddressCount** *(integer) --* 
        
              The number of secondary private IPv4 addresses. You can\'t specify this option and specify more than one private IP address using the private IP addresses option. You cannot specify this option if you\'re launching more than one instance in a  RunInstances request.
        
            - **SubnetId** *(string) --* 
        
              The ID of the subnet associated with the network string. Applies only if creating a network interface when launching an instance.
        
        :type PrivateIpAddress: string
        :param PrivateIpAddress: 
        
          [EC2-VPC] The primary IPv4 address. You must specify a value from the IPv4 address range of the subnet.
        
          Only one private IP address can be designated as primary. You can\'t specify this option if you\'ve specified the option to designate a private IP address as the primary IP address in a network interface specification. You cannot specify this option if you\'re launching more than one instance in the request.
        
        :type ElasticGpuSpecification: list
        :param ElasticGpuSpecification: 
        
          An elastic GPU to associate with the instance.
        
          - *(dict) --* 
        
            A specification for an Elastic GPU.
        
            - **Type** *(string) --* **[REQUIRED]** 
        
              The type of Elastic GPU.
        
        :type TagSpecifications: list
        :param TagSpecifications: 
        
          The tags to apply to the resources during launch. You can only tag instances and volumes on launch. The specified tags are applied to all instances or volumes that are created during launch. To tag a resource after it has been created, see  CreateTags .
        
          - *(dict) --* 
        
            The tags to apply to a resource when the resource is being created.
        
            - **ResourceType** *(string) --* 
        
              The type of resource to tag. Currently, the resource types that support tagging on creation are ``fleet`` , ``dedicated-host`` , ``instance`` , ``snapshot`` , and ``volume`` . To tag a resource after it has been created, see  CreateTags .
        
            - **Tags** *(list) --* 
        
              The tags to apply to the resource.
        
              - *(dict) --* 
        
                Describes a tag.
        
                - **Key** *(string) --* 
        
                  The key of the tag.
        
                  Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
                - **Value** *(string) --* 
        
                  The value of the tag.
        
                  Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :type LaunchTemplate: dict
        :param LaunchTemplate: 
        
          The launch template to use to launch the instances. Any parameters that you specify in  RunInstances override the same parameters in the launch template. You can specify either the name or ID of a launch template, but not both.
        
          - **LaunchTemplateId** *(string) --* 
        
            The ID of the launch template.
        
          - **LaunchTemplateName** *(string) --* 
        
            The name of the launch template.
        
          - **Version** *(string) --* 
        
            The version number of the launch template.
        
            Default: The default version for the launch template.
        
        :type InstanceMarketOptions: dict
        :param InstanceMarketOptions: 
        
          The market (purchasing) option for the instances.
        
          For  RunInstances , persistent Spot Instance requests are only supported when **InstanceInterruptionBehavior** is set to either ``hibernate`` or ``stop`` .
        
          - **MarketType** *(string) --* 
        
            The market type.
        
          - **SpotOptions** *(dict) --* 
        
            The options for Spot Instances.
        
            - **MaxPrice** *(string) --* 
        
              The maximum hourly price you\'re willing to pay for the Spot Instances. The default is the On-Demand price.
        
            - **SpotInstanceType** *(string) --* 
        
              The Spot Instance request type. For  RunInstances , persistent Spot Instance requests are only supported when **InstanceInterruptionBehavior** is set to either ``hibernate`` or ``stop`` .
        
            - **BlockDurationMinutes** *(integer) --* 
        
              The required duration for the Spot Instances (also known as Spot blocks), in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).
        
            - **ValidUntil** *(datetime) --* 
        
              The end date of the request. For a one-time request, the request remains active until all instances launch, the request is canceled, or this date is reached. If the request is persistent, it remains active until it is canceled or this date and time is reached. The default end date is 7 days from the current date.
        
            - **InstanceInterruptionBehavior** *(string) --* 
        
              The behavior when a Spot Instance is interrupted. The default is ``terminate`` .
        
        :type CreditSpecification: dict
        :param CreditSpecification: 
        
          The credit option for CPU usage of the instance. Valid values are ``standard`` and ``unlimited`` . To change this attribute after launch, use  ModifyInstanceCreditSpecification . For more information, see `Burstable Performance Instances <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
          Default: ``standard`` (T2 instances) or ``unlimited`` (T3 instances)
        
          - **CpuCredits** *(string) --* **[REQUIRED]** 
        
            The credit option for CPU usage of a T2 or T3 instance. Valid values are ``standard`` and ``unlimited`` .
        
        :type CpuOptions: dict
        :param CpuOptions: 
        
          The CPU options for the instance. For more information, see `Optimizing CPU Options <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
          - **CoreCount** *(integer) --* 
        
            The number of CPU cores for the instance.
        
          - **ThreadsPerCore** *(integer) --* 
        
            The number of threads per CPU core. To disable Intel Hyper-Threading Technology for the instance, specify a value of ``1`` . Otherwise, specify the default value of ``2`` .
        
        :type CapacityReservationSpecification: dict
        :param CapacityReservationSpecification: 
        
          Information about the Capacity Reservation targeting option.
        
          - **CapacityReservationPreference** *(string) --* 
        
            Indicates the instance\'s Capacity Reservation preferences. Possible preferences include:
        
            * ``open`` - The instance can run in any ``open`` Capacity Reservation that has matching attributes (instance type, platform, Availability Zone). 
             
            * ``none`` - The instance avoids running in a Capacity Reservation even if one is available. The instance runs as an On-Demand Instance. 
             
          - **CapacityReservationTarget** *(dict) --* 
        
            Information about the target Capacity Reservation.
        
            - **CapacityReservationId** *(string) --* 
        
              The ID of the Capacity Reservation.
        
        :rtype: list(:py:class:`ec2.Instance`)
        :returns: A list of Instance resources
        """
        pass

    def create_network_interface(self, Description: str = None, DryRun: bool = None, Groups: List = None, Ipv6AddressCount: int = None, Ipv6Addresses: List = None, PrivateIpAddress: str = None, PrivateIpAddresses: List = None, SecondaryPrivateIpAddressCount: int = None) -> 'NetworkInterface':
        """
        
        For more information about network interfaces, see `Elastic Network Interfaces <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateNetworkInterface>`_
        
        **Request Syntax** 
        ::
        
          network_interface = subnet.create_network_interface(
              Description=\'string\',
              DryRun=True|False,
              Groups=[
                  \'string\',
              ],
              Ipv6AddressCount=123,
              Ipv6Addresses=[
                  {
                      \'Ipv6Address\': \'string\'
                  },
              ],
              PrivateIpAddress=\'string\',
              PrivateIpAddresses=[
                  {
                      \'Primary\': True|False,
                      \'PrivateIpAddress\': \'string\'
                  },
              ],
              SecondaryPrivateIpAddressCount=123,
              
          )
        :type Description: string
        :param Description: 
        
          A description for the network interface.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Groups: list
        :param Groups: 
        
          The IDs of one or more security groups.
        
          - *(string) --* 
        
        :type Ipv6AddressCount: integer
        :param Ipv6AddressCount: 
        
          The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can\'t use this option if specifying specific IPv6 addresses. If your subnet has the ``AssignIpv6AddressOnCreation`` attribute set to ``true`` , you can specify ``0`` to override this setting.
        
        :type Ipv6Addresses: list
        :param Ipv6Addresses: 
        
          One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. You can\'t use this option if you\'re specifying a number of IPv6 addresses.
        
          - *(dict) --* 
        
            Describes an IPv6 address.
        
            - **Ipv6Address** *(string) --* 
        
              The IPv6 address.
        
        :type PrivateIpAddress: string
        :param PrivateIpAddress: 
        
          The primary private IPv4 address of the network interface. If you don\'t specify an IPv4 address, Amazon EC2 selects one for you from the subnet\'s IPv4 CIDR range. If you specify an IP address, you cannot indicate any IP addresses specified in ``privateIpAddresses`` as primary (only one IP address can be designated as primary).
        
        :type PrivateIpAddresses: list
        :param PrivateIpAddresses: 
        
          One or more private IPv4 addresses.
        
          - *(dict) --* 
        
            Describes a secondary private IPv4 address for a network interface.
        
            - **Primary** *(boolean) --* 
        
              Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.
        
            - **PrivateIpAddress** *(string) --* 
        
              The private IPv4 addresses.
        
        :type SecondaryPrivateIpAddressCount: integer
        :param SecondaryPrivateIpAddressCount: 
        
          The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary IPv4 addresses, Amazon EC2 selects these IP addresses within the subnet\'s IPv4 CIDR range. You can\'t specify this option and specify more than one private IP address using ``privateIpAddresses`` .
        
          The number of IP addresses you can assign to a network interface varies by instance type. For more information, see `IP Addresses Per ENI Per Instance Type <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        :rtype: :py:class:`ec2.NetworkInterface`
        :returns: NetworkInterface resource
        """
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        """
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . For more information about creating IAM policies that control users\' access to resources based on tags, see `Supported Resource-Level Permissions for Amazon EC2 API Actions <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          tag = subnet.create_tags(
              DryRun=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. The ``value`` parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 
        
          - *(dict) --* 
        
            Describes a tag.
        
            - **Key** *(string) --* 
        
              The key of the tag.
        
              Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
              Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :rtype: list(:py:class:`ec2.Tag`)
        :returns: A list of Tag resources
        """
        pass

    def delete(self, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteSubnet>`_
        
        **Request Syntax** 
        ::
        
          response = subnet.delete(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          subnet.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          subnet.load()
        :returns: None
        """
        pass


class Tag(base.ServiceResource):
    resource_type: str
    resource_id: str
    key: str
    value: str

    def delete(self, DryRun: bool = None):
        """
        
        To list the current tags, use  DescribeTags . For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteTags>`_
        
        **Request Syntax** 
        ::
        
          response = tag.delete(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          tag.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          tag.load()
        :returns: None
        """
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
        """
        
        Encrypted EBS volumes may only be attached to instances that support Amazon EBS encryption. For more information, see `Amazon EBS Encryption <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        For a list of supported device names, see `Attaching an EBS Volume to an Instance <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html>`__ . Any device names that aren\'t reserved for instance store volumes can be used for EBS volumes. For more information, see `Amazon EC2 Instance Store <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        If a volume has an AWS Marketplace product code:
        
        * The volume can be attached only to a stopped instance. 
         
        * AWS Marketplace product codes are copied from the volume to the instance. 
         
        * You must be subscribed to the product. 
         
        * The instance type and operating system of the instance must support the product. For example, you can\'t detach a volume from a Windows instance and attach it to a Linux instance. 
         
        For more information about EBS volumes, see `Attaching Amazon EBS Volumes <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AttachVolume>`_
        
        **Request Syntax** 
        ::
        
          response = volume.attach_to_instance(
              Device=\'string\',
              InstanceId=\'string\',
              DryRun=True|False
          )
        :type Device: string
        :param Device: **[REQUIRED]** 
        
          The device name (for example, ``/dev/sdh`` or ``xvdh`` ).
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The ID of the instance.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AttachTime\': datetime(2015, 1, 1),
                \'Device\': \'string\',
                \'InstanceId\': \'string\',
                \'State\': \'attaching\'|\'attached\'|\'detaching\'|\'detached\'|\'busy\',
                \'VolumeId\': \'string\',
                \'DeleteOnTermination\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Describes volume attachment details.
        
            - **AttachTime** *(datetime) --* 
        
              The time stamp when the attachment initiated.
        
            - **Device** *(string) --* 
        
              The device name.
        
            - **InstanceId** *(string) --* 
        
              The ID of the instance.
        
            - **State** *(string) --* 
        
              The attachment state of the volume.
        
            - **VolumeId** *(string) --* 
        
              The ID of the volume.
        
            - **DeleteOnTermination** *(boolean) --* 
        
              Indicates whether the EBS volume is deleted on instance termination.
        
        """
        pass

    def create_snapshot(self, Description: str = None, TagSpecifications: List = None, DryRun: bool = None) -> 'Snapshot':
        """
        
        When a snapshot is created, any AWS Marketplace product codes that are associated with the source volume are propagated to the snapshot.
        
        You can take a snapshot of an attached volume that is in use. However, snapshots only capture data that has been written to your EBS volume at the time the snapshot command is issued; this may exclude any data that has been cached by any applications or the operating system. If you can pause any file systems on the volume long enough to take a snapshot, your snapshot should be complete. However, if you cannot pause all file writes to the volume, you should unmount the volume from within the instance, issue the snapshot command, and then remount the volume to ensure a consistent and complete snapshot. You may remount and use your volume while the snapshot status is ``pending`` .
        
        To create a snapshot for EBS volumes that serve as root devices, you should stop the instance before taking the snapshot.
        
        Snapshots that are taken from encrypted volumes are automatically encrypted. Volumes that are created from encrypted snapshots are also automatically encrypted. Your encrypted volumes and any associated snapshots always remain protected.
        
        You can tag your snapshots during creation. For more information, see `Tagging Your Amazon EC2 Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        For more information, see `Amazon Elastic Block Store <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html>`__ and `Amazon EBS Encryption <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateSnapshot>`_
        
        **Request Syntax** 
        ::
        
          snapshot = volume.create_snapshot(
              Description=\'string\',
              TagSpecifications=[
                  {
                      \'ResourceType\': \'customer-gateway\'|\'dedicated-host\'|\'dhcp-options\'|\'image\'|\'instance\'|\'internet-gateway\'|\'network-acl\'|\'network-interface\'|\'reserved-instances\'|\'route-table\'|\'snapshot\'|\'spot-instances-request\'|\'subnet\'|\'security-group\'|\'volume\'|\'vpc\'|\'vpn-connection\'|\'vpn-gateway\',
                      \'Tags\': [
                          {
                              \'Key\': \'string\',
                              \'Value\': \'string\'
                          },
                      ]
                  },
              ],
              DryRun=True|False
          )
        :type Description: string
        :param Description: 
        
          A description for the snapshot.
        
        :type TagSpecifications: list
        :param TagSpecifications: 
        
          The tags to apply to the snapshot during creation.
        
          - *(dict) --* 
        
            The tags to apply to a resource when the resource is being created.
        
            - **ResourceType** *(string) --* 
        
              The type of resource to tag. Currently, the resource types that support tagging on creation are ``fleet`` , ``dedicated-host`` , ``instance`` , ``snapshot`` , and ``volume`` . To tag a resource after it has been created, see  CreateTags .
        
            - **Tags** *(list) --* 
        
              The tags to apply to the resource.
        
              - *(dict) --* 
        
                Describes a tag.
        
                - **Key** *(string) --* 
        
                  The key of the tag.
        
                  Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
                - **Value** *(string) --* 
        
                  The value of the tag.
        
                  Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: :py:class:`ec2.Snapshot`
        :returns: Snapshot resource
        """
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        """
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . For more information about creating IAM policies that control users\' access to resources based on tags, see `Supported Resource-Level Permissions for Amazon EC2 API Actions <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          tag = volume.create_tags(
              DryRun=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. The ``value`` parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 
        
          - *(dict) --* 
        
            Describes a tag.
        
            - **Key** *(string) --* 
        
              The key of the tag.
        
              Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
              Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :rtype: list(:py:class:`ec2.Tag`)
        :returns: A list of Tag resources
        """
        pass

    def delete(self, DryRun: bool = None):
        """
        
        The volume can remain in the ``deleting`` state for several minutes.
        
        For more information, see `Deleting an Amazon EBS Volume <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-deleting-volume.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteVolume>`_
        
        **Request Syntax** 
        ::
        
          response = volume.delete(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict:
        """
        
        For more information about EBS volumes, see `Amazon EBS Volumes <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumeAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = volume.describe_attribute(
              Attribute=\'autoEnableIO\'|\'productCodes\',
              DryRun=True|False
          )
        :type Attribute: string
        :param Attribute: **[REQUIRED]** 
        
          The attribute of the volume. This parameter is required.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AutoEnableIO\': {
                    \'Value\': True|False
                },
                \'ProductCodes\': [
                    {
                        \'ProductCodeId\': \'string\',
                        \'ProductCodeType\': \'devpay\'|\'marketplace\'
                    },
                ],
                \'VolumeId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DescribeVolumeAttribute.
        
            - **AutoEnableIO** *(dict) --* 
        
              The state of ``autoEnableIO`` attribute.
        
              - **Value** *(boolean) --* 
        
                The attribute value. The valid values are ``true`` or ``false`` .
        
            - **ProductCodes** *(list) --* 
        
              A list of product codes.
        
              - *(dict) --* 
        
                Describes a product code.
        
                - **ProductCodeId** *(string) --* 
        
                  The product code.
        
                - **ProductCodeType** *(string) --* 
        
                  The type of product code.
        
            - **VolumeId** *(string) --* 
        
              The ID of the volume.
        
        """
        pass

    def describe_status(self, Filters: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None) -> Dict:
        """
        
        The ``DescribeVolumeStatus`` operation provides the following information about the specified volumes:
        
         *Status* : Reflects the current status of the volume. The possible values are ``ok`` , ``impaired`` , ``warning`` , or ``insufficient-data`` . If all checks pass, the overall status of the volume is ``ok`` . If the check fails, the overall status is ``impaired`` . If the status is ``insufficient-data`` , then the checks may still be taking place on your volume at the time. We recommend that you retry the request. For more information about volume status, see `Monitoring the Status of Your Volumes <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-volume-status.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
         *Events* : Reflect the cause of a volume status and may require you to take action. For example, if your volume returns an ``impaired`` status, then the volume event might be ``potential-data-inconsistency`` . This means that your volume has been affected by an issue with the underlying host, has all I/O operations disabled, and may have inconsistent data.
        
         *Actions* : Reflect the actions you may have to take in response to an event. For example, if the status of the volume is ``impaired`` and the volume event shows ``potential-data-inconsistency`` , then the action shows ``enable-volume-io`` . This means that you may want to enable the I/O operations for the volume by calling the  EnableVolumeIO action and then check the volume for data consistency.
        
        Volume status is based on the volume status checks, and does not reflect the volume state. Therefore, volume status does not indicate volumes in the ``error`` state (for example, when a volume is incapable of accepting I/O.)
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumeStatus>`_
        
        **Request Syntax** 
        ::
        
          response = volume.describe_status(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\',
              DryRun=True|False
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``action.code`` - The action code for the event (for example, ``enable-volume-io`` ). 
           
          * ``action.description`` - A description of the action. 
           
          * ``action.event-id`` - The event ID associated with the action. 
           
          * ``availability-zone`` - The Availability Zone of the instance. 
           
          * ``event.description`` - A description of the event. 
           
          * ``event.event-id`` - The event ID. 
           
          * ``event.event-type`` - The event type (for ``io-enabled`` : ``passed`` | ``failed`` ; for ``io-performance`` : ``io-performance:degraded`` | ``io-performance:severely-degraded`` | ``io-performance:stalled`` ). 
           
          * ``event.not-after`` - The latest end time for the event. 
           
          * ``event.not-before`` - The earliest start time for the event. 
           
          * ``volume-status.details-name`` - The cause for ``volume-status.status`` (``io-enabled`` | ``io-performance`` ). 
           
          * ``volume-status.details-status`` - The status of ``volume-status.details-name`` (for ``io-enabled`` : ``passed`` | ``failed`` ; for ``io-performance`` : ``normal`` | ``degraded`` | ``severely-degraded`` | ``stalled`` ). 
           
          * ``volume-status.status`` - The status of the volume (``ok`` | ``impaired`` | ``warning`` | ``insufficient-data`` ). 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of volume results returned by ``DescribeVolumeStatus`` in paginated output. When this parameter is used, the request only returns ``MaxResults`` results in a single page along with a ``NextToken`` response element. The remaining results of the initial request can be seen by sending another request with the returned ``NextToken`` value. This value can be between 5 and 1000; if ``MaxResults`` is given a value larger than 1000, only 1000 results are returned. If this parameter is not used, then ``DescribeVolumeStatus`` returns all results. You cannot specify this parameter and the volume IDs parameter in the same request.
        
        :type NextToken: string
        :param NextToken: 
        
          The ``NextToken`` value to include in a future ``DescribeVolumeStatus`` request. When the results of the request exceed ``MaxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'VolumeStatuses\': [
                    {
                        \'Actions\': [
                            {
                                \'Code\': \'string\',
                                \'Description\': \'string\',
                                \'EventId\': \'string\',
                                \'EventType\': \'string\'
                            },
                        ],
                        \'AvailabilityZone\': \'string\',
                        \'Events\': [
                            {
                                \'Description\': \'string\',
                                \'EventId\': \'string\',
                                \'EventType\': \'string\',
                                \'NotAfter\': datetime(2015, 1, 1),
                                \'NotBefore\': datetime(2015, 1, 1)
                            },
                        ],
                        \'VolumeId\': \'string\',
                        \'VolumeStatus\': {
                            \'Details\': [
                                {
                                    \'Name\': \'io-enabled\'|\'io-performance\',
                                    \'Status\': \'string\'
                                },
                            ],
                            \'Status\': \'ok\'|\'impaired\'|\'insufficient-data\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DescribeVolumeStatus.
        
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        
            - **VolumeStatuses** *(list) --* 
        
              A list of volumes.
        
              - *(dict) --* 
        
                Describes the volume status.
        
                - **Actions** *(list) --* 
        
                  The details of the operation.
        
                  - *(dict) --* 
        
                    Describes a volume status operation code.
        
                    - **Code** *(string) --* 
        
                      The code identifying the operation, for example, ``enable-volume-io`` .
        
                    - **Description** *(string) --* 
        
                      A description of the operation.
        
                    - **EventId** *(string) --* 
        
                      The ID of the event associated with this operation.
        
                    - **EventType** *(string) --* 
        
                      The event type associated with this operation.
        
                - **AvailabilityZone** *(string) --* 
        
                  The Availability Zone of the volume.
        
                - **Events** *(list) --* 
        
                  A list of events associated with the volume.
        
                  - *(dict) --* 
        
                    Describes a volume status event.
        
                    - **Description** *(string) --* 
        
                      A description of the event.
        
                    - **EventId** *(string) --* 
        
                      The ID of this event.
        
                    - **EventType** *(string) --* 
        
                      The type of this event.
        
                    - **NotAfter** *(datetime) --* 
        
                      The latest end time of the event.
        
                    - **NotBefore** *(datetime) --* 
        
                      The earliest start time of the event.
        
                - **VolumeId** *(string) --* 
        
                  The volume ID.
        
                - **VolumeStatus** *(dict) --* 
        
                  The volume status.
        
                  - **Details** *(list) --* 
        
                    The details of the volume status.
        
                    - *(dict) --* 
        
                      Describes a volume status.
        
                      - **Name** *(string) --* 
        
                        The name of the volume status.
        
                      - **Status** *(string) --* 
        
                        The intended status of the volume status.
        
                  - **Status** *(string) --* 
        
                    The status of the volume.
        
        """
        pass

    def detach_from_instance(self, Device: str = None, Force: bool = None, InstanceId: str = None, DryRun: bool = None) -> Dict:
        """
        
        When a volume with an AWS Marketplace product code is detached from an instance, the product code is no longer associated with the instance.
        
        For more information, see `Detaching an Amazon EBS Volume <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-detaching-volume.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DetachVolume>`_
        
        **Request Syntax** 
        ::
        
          response = volume.detach_from_instance(
              Device=\'string\',
              Force=True|False,
              InstanceId=\'string\',
              DryRun=True|False
          )
        :type Device: string
        :param Device: 
        
          The device name.
        
        :type Force: boolean
        :param Force: 
        
          Forces detachment if the previous detachment attempt did not occur cleanly (for example, logging into an instance, unmounting the volume, and detaching normally). This option can lead to data loss or a corrupted file system. Use this option only as a last resort to detach a volume from a failed instance. The instance won\'t have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures.
        
        :type InstanceId: string
        :param InstanceId: 
        
          The ID of the instance.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AttachTime\': datetime(2015, 1, 1),
                \'Device\': \'string\',
                \'InstanceId\': \'string\',
                \'State\': \'attaching\'|\'attached\'|\'detaching\'|\'detached\'|\'busy\',
                \'VolumeId\': \'string\',
                \'DeleteOnTermination\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Describes volume attachment details.
        
            - **AttachTime** *(datetime) --* 
        
              The time stamp when the attachment initiated.
        
            - **Device** *(string) --* 
        
              The device name.
        
            - **InstanceId** *(string) --* 
        
              The ID of the instance.
        
            - **State** *(string) --* 
        
              The attachment state of the volume.
        
            - **VolumeId** *(string) --* 
        
              The ID of the volume.
        
            - **DeleteOnTermination** *(boolean) --* 
        
              Indicates whether the EBS volume is deleted on instance termination.
        
        """
        pass

    def enable_io(self, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/EnableVolumeIO>`_
        
        **Request Syntax** 
        ::
        
          response = volume.enable_io(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          volume.load()
        :returns: None
        """
        pass

    def modify_attribute(self, AutoEnableIO: Dict = None, DryRun: bool = None):
        """
        
        By default, all I/O operations for the volume are suspended when the data on the volume is determined to be potentially inconsistent, to prevent undetectable, latent data corruption. The I/O access to the volume can be resumed by first enabling I/O access and then checking the data consistency on your volume.
        
        You can change the default behavior to resume I/O operations. We recommend that you change this only for boot volumes or for volumes that are stateless or disposable.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyVolumeAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = volume.modify_attribute(
              AutoEnableIO={
                  \'Value\': True|False
              },
              DryRun=True|False
          )
        :type AutoEnableIO: dict
        :param AutoEnableIO: 
        
          Indicates whether the volume should be auto-enabled for I/O operations.
        
          - **Value** *(boolean) --* 
        
            The attribute value. The valid values are ``true`` or ``false`` .
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          volume.load()
        :returns: None
        """
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
        """
        
        After you associate the options with the VPC, any existing instances and all new instances that you launch in that VPC use the options. You don\'t need to restart or relaunch the instances. They automatically pick up the changes within a few hours, depending on how frequently the instance renews its DHCP lease. You can explicitly renew the lease using the operating system on the instance.
        
        For more information, see `DHCP Options Sets <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AssociateDhcpOptions>`_
        
        **Request Syntax** 
        ::
        
          response = vpc.associate_dhcp_options(
              DhcpOptionsId=\'string\',
              DryRun=True|False
          )
        :type DhcpOptionsId: string
        :param DhcpOptionsId: **[REQUIRED]** 
        
          The ID of the DHCP options set, or ``default`` to associate no DHCP options with the VPC.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def attach_classic_link_instance(self, Groups: List, InstanceId: str, DryRun: bool = None) -> Dict:
        """
        
        After you\'ve linked an instance, you cannot change the VPC security groups that are associated with it. To change the security groups, you must first unlink the instance, and then link it again.
        
        Linking your instance to a VPC is sometimes referred to as *attaching* your instance.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AttachClassicLinkVpc>`_
        
        **Request Syntax** 
        ::
        
          response = vpc.attach_classic_link_instance(
              DryRun=True|False,
              Groups=[
                  \'string\',
              ],
              InstanceId=\'string\',
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Groups: list
        :param Groups: **[REQUIRED]** 
        
          The ID of one or more of the VPC\'s security groups. You cannot specify security groups from a different VPC.
        
          - *(string) --* 
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The ID of an EC2-Classic instance to link to the ClassicLink-enabled VPC.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Return\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Return** *(boolean) --* 
        
              Returns ``true`` if the request succeeds; otherwise, it returns an error.
        
        """
        pass

    def attach_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AttachInternetGateway>`_
        
        **Request Syntax** 
        ::
        
          response = vpc.attach_internet_gateway(
              DryRun=True|False,
              InternetGatewayId=\'string\',
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type InternetGatewayId: string
        :param InternetGatewayId: **[REQUIRED]** 
        
          The ID of the internet gateway.
        
        :returns: None
        """
        pass

    def create_network_acl(self, DryRun: bool = None) -> 'NetworkAcl':
        """
        
        For more information, see `Network ACLs <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateNetworkAcl>`_
        
        **Request Syntax** 
        ::
        
          network_acl = vpc.create_network_acl(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: :py:class:`ec2.NetworkAcl`
        :returns: NetworkAcl resource
        """
        pass

    def create_route_table(self, DryRun: bool = None) -> 'RouteTable':
        """
        
        For more information, see `Route Tables <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateRouteTable>`_
        
        **Request Syntax** 
        ::
        
          route_table = vpc.create_route_table(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: :py:class:`ec2.RouteTable`
        :returns: RouteTable resource
        """
        pass

    def create_security_group(self, Description: str, GroupName: str, DryRun: bool = None) -> 'SecurityGroup':
        """
        
        A security group is for use with instances either in the EC2-Classic platform or in a specific VPC. For more information, see `Amazon EC2 Security Groups <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html>`__ in the *Amazon Elastic Compute Cloud User Guide* and `Security Groups for Your VPC <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        .. warning::
        
          EC2-Classic: You can have up to 500 security groups.
        
          EC2-VPC: You can create up to 500 security groups per VPC.
        
        When you create a security group, you specify a friendly name of your choice. You can have a security group for use in EC2-Classic with the same name as a security group for use in a VPC. However, you can\'t have two security groups for use in EC2-Classic with the same name or two security groups for use in a VPC with the same name.
        
        You have a default security group for use in EC2-Classic and a default security group for use in your VPC. If you don\'t specify a security group when you launch an instance, the instance is launched into the appropriate default security group. A default security group includes a default rule that grants instances unrestricted network access to each other.
        
        You can add or remove rules from your security groups using  AuthorizeSecurityGroupIngress ,  AuthorizeSecurityGroupEgress ,  RevokeSecurityGroupIngress , and  RevokeSecurityGroupEgress .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateSecurityGroup>`_
        
        **Request Syntax** 
        ::
        
          security_group = vpc.create_security_group(
              Description=\'string\',
              GroupName=\'string\',
              DryRun=True|False
          )
        :type Description: string
        :param Description: **[REQUIRED]** 
        
          A description for the security group. This is informational only.
        
          Constraints: Up to 255 characters in length
        
          Constraints for EC2-Classic: ASCII characters
        
          Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*
        
        :type GroupName: string
        :param GroupName: **[REQUIRED]** 
        
          The name of the security group.
        
          Constraints: Up to 255 characters in length. Cannot start with ``sg-`` .
        
          Constraints for EC2-Classic: ASCII characters
        
          Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: :py:class:`ec2.SecurityGroup`
        :returns: SecurityGroup resource
        """
        pass

    def create_subnet(self, CidrBlock: str, AvailabilityZone: str = None, Ipv6CidrBlock: str = None, DryRun: bool = None) -> 'Subnet':
        """
        
        When you create each subnet, you provide the VPC ID and IPv4 CIDR block for the subnet. After you create a subnet, you can\'t change its CIDR block. The size of the subnet\'s IPv4 CIDR block can be the same as a VPC\'s IPv4 CIDR block, or a subset of a VPC\'s IPv4 CIDR block. If you create more than one subnet in a VPC, the subnets\' CIDR blocks must not overlap. The smallest IPv4 subnet (and VPC) you can create uses a /28 netmask (16 IPv4 addresses), and the largest uses a /16 netmask (65,536 IPv4 addresses).
        
        If you\'ve associated an IPv6 CIDR block with your VPC, you can create a subnet with an IPv6 CIDR block that uses a /64 prefix length. 
        
        .. warning::
        
          AWS reserves both the first four and the last IPv4 address in each subnet\'s CIDR block. They\'re not available for use.
        
        If you add more than one subnet to a VPC, they\'re set up in a star topology with a logical router in the middle.
        
        If you launch an instance in a VPC using an Amazon EBS-backed AMI, the IP address doesn\'t change if you stop and restart the instance (unlike a similar instance launched outside a VPC, which gets a new IP address when restarted). It\'s therefore possible to have a subnet with no running instances (they\'re all stopped), but no remaining IP addresses available.
        
        For more information about subnets, see `Your VPC and Subnets <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateSubnet>`_
        
        **Request Syntax** 
        ::
        
          subnet = vpc.create_subnet(
              AvailabilityZone=\'string\',
              CidrBlock=\'string\',
              Ipv6CidrBlock=\'string\',
              DryRun=True|False
          )
        :type AvailabilityZone: string
        :param AvailabilityZone: 
        
          The Availability Zone for the subnet.
        
          Default: AWS selects one for you. If you create more than one subnet in your VPC, we may not necessarily select a different zone for each subnet.
        
        :type CidrBlock: string
        :param CidrBlock: **[REQUIRED]** 
        
          The IPv4 network range for the subnet, in CIDR notation. For example, ``10.0.0.0/24`` .
        
        :type Ipv6CidrBlock: string
        :param Ipv6CidrBlock: 
        
          The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: :py:class:`ec2.Subnet`
        :returns: Subnet resource
        """
        pass

    def create_tags(self, Tags: List, DryRun: bool = None) -> List['Tag']:
        """
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . For more information about creating IAM policies that control users\' access to resources based on tags, see `Supported Resource-Level Permissions for Amazon EC2 API Actions <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          tag = vpc.create_tags(
              DryRun=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. The ``value`` parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 
        
          - *(dict) --* 
        
            Describes a tag.
        
            - **Key** *(string) --* 
        
              The key of the tag.
        
              Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
              Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :rtype: list(:py:class:`ec2.Tag`)
        :returns: A list of Tag resources
        """
        pass

    def delete(self, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteVpc>`_
        
        **Request Syntax** 
        ::
        
          response = vpc.delete(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = vpc.describe_attribute(
              Attribute=\'enableDnsSupport\'|\'enableDnsHostnames\',
              DryRun=True|False
          )
        :type Attribute: string
        :param Attribute: **[REQUIRED]** 
        
          The VPC attribute.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'VpcId\': \'string\',
                \'EnableDnsHostnames\': {
                    \'Value\': True|False
                },
                \'EnableDnsSupport\': {
                    \'Value\': True|False
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **VpcId** *(string) --* 
        
              The ID of the VPC.
        
            - **EnableDnsHostnames** *(dict) --* 
        
              Indicates whether the instances launched in the VPC get DNS hostnames. If this attribute is ``true`` , instances in the VPC get DNS hostnames; otherwise, they do not.
        
              - **Value** *(boolean) --* 
        
                The attribute value. The valid values are ``true`` or ``false`` .
        
            - **EnableDnsSupport** *(dict) --* 
        
              Indicates whether DNS resolution is enabled for the VPC. If this attribute is ``true`` , the Amazon DNS server resolves DNS hostnames for your instances to their corresponding IP addresses; otherwise, it does not.
        
              - **Value** *(boolean) --* 
        
                The attribute value. The valid values are ``true`` or ``false`` .
        
        """
        pass

    def detach_classic_link_instance(self, InstanceId: str, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DetachClassicLinkVpc>`_
        
        **Request Syntax** 
        ::
        
          response = vpc.detach_classic_link_instance(
              DryRun=True|False,
              InstanceId=\'string\',
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The ID of the instance to unlink from the VPC.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Return\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Return** *(boolean) --* 
        
              Returns ``true`` if the request succeeds; otherwise, it returns an error.
        
        """
        pass

    def detach_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DetachInternetGateway>`_
        
        **Request Syntax** 
        ::
        
          response = vpc.detach_internet_gateway(
              DryRun=True|False,
              InternetGatewayId=\'string\',
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type InternetGatewayId: string
        :param InternetGatewayId: **[REQUIRED]** 
        
          The ID of the internet gateway.
        
        :returns: None
        """
        pass

    def disable_classic_link(self, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DisableVpcClassicLink>`_
        
        **Request Syntax** 
        ::
        
          response = vpc.disable_classic_link(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Return\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Return** *(boolean) --* 
        
              Returns ``true`` if the request succeeds; otherwise, it returns an error.
        
        """
        pass

    def enable_classic_link(self, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/EnableVpcClassicLink>`_
        
        **Request Syntax** 
        ::
        
          response = vpc.enable_classic_link(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Return\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Return** *(boolean) --* 
        
              Returns ``true`` if the request succeeds; otherwise, it returns an error.
        
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          vpc.load()
        :returns: None
        """
        pass

    def modify_attribute(self, EnableDnsHostnames: Dict = None, EnableDnsSupport: Dict = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyVpcAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = vpc.modify_attribute(
              EnableDnsHostnames={
                  \'Value\': True|False
              },
              EnableDnsSupport={
                  \'Value\': True|False
              },
              
          )
        :type EnableDnsHostnames: dict
        :param EnableDnsHostnames: 
        
          Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not.
        
          You cannot modify the DNS resolution and DNS hostnames attributes in the same request. Use separate requests for each attribute. You can only enable DNS hostnames if you\'ve enabled DNS support.
        
          - **Value** *(boolean) --* 
        
            The attribute value. The valid values are ``true`` or ``false`` .
        
        :type EnableDnsSupport: dict
        :param EnableDnsSupport: 
        
          Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range \"plus two\" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled.
        
          You cannot modify the DNS resolution and DNS hostnames attributes in the same request. Use separate requests for each attribute.
        
          - **Value** *(boolean) --* 
        
            The attribute value. The valid values are ``true`` or ``false`` .
        
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          vpc.load()
        :returns: None
        """
        pass

    def request_vpc_peering_connection(self, DryRun: bool = None, PeerOwnerId: str = None, PeerVpcId: str = None, PeerRegion: str = None) -> 'VpcPeeringConnection':
        """
        
        .. note::
        
          Limitations and rules apply to a VPC peering connection. For more information, see the `limitations <http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/vpc-peering-basics.html#vpc-peering-limitations>`__ section in the *VPC Peering Guide* .
        
        The owner of the accepter VPC must accept the peering request to activate the peering connection. The VPC peering connection request expires after 7 days, after which it cannot be accepted or rejected.
        
        If you create a VPC peering connection request between VPCs with overlapping CIDR blocks, the VPC peering connection has a status of ``failed`` .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateVpcPeeringConnection>`_
        
        **Request Syntax** 
        ::
        
          vpc_peering_connection = vpc.request_vpc_peering_connection(
              DryRun=True|False,
              PeerOwnerId=\'string\',
              PeerVpcId=\'string\',
              PeerRegion=\'string\'
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type PeerOwnerId: string
        :param PeerOwnerId: 
        
          The AWS account ID of the owner of the accepter VPC.
        
          Default: Your AWS account ID
        
        :type PeerVpcId: string
        :param PeerVpcId: 
        
          The ID of the VPC with which you are creating the VPC peering connection. You must specify this parameter in the request.
        
        :type PeerRegion: string
        :param PeerRegion: 
        
          The region code for the accepter VPC, if the accepter VPC is located in a region other than the region in which you make the request.
        
          Default: The region in which you make the request.
        
        :rtype: :py:class:`ec2.VpcPeeringConnection`
        :returns: VpcPeeringConnection resource
        """
        pass

    def wait_until_available(self, Filters: List = None, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcs>`_
        
        **Request Syntax** 
        ::
        
          vpc.wait_until_available(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``cidr`` - The primary IPv4 CIDR block of the VPC. The CIDR block you specify must exactly match the VPC\'s CIDR block for information to be returned for the VPC. Must contain the slash followed by one or two digits (for example, ``/28`` ). 
           
          * ``cidr-block-association.cidr-block`` - An IPv4 CIDR block associated with the VPC. 
           
          * ``cidr-block-association.association-id`` - The association ID for an IPv4 CIDR block associated with the VPC. 
           
          * ``cidr-block-association.state`` - The state of an IPv4 CIDR block associated with the VPC. 
           
          * ``dhcp-options-id`` - The ID of a set of DHCP options. 
           
          * ``ipv6-cidr-block-association.ipv6-cidr-block`` - An IPv6 CIDR block associated with the VPC. 
           
          * ``ipv6-cidr-block-association.association-id`` - The association ID for an IPv6 CIDR block associated with the VPC. 
           
          * ``ipv6-cidr-block-association.state`` - The state of an IPv6 CIDR block associated with the VPC. 
           
          * ``isDefault`` - Indicates whether the VPC is the default VPC. 
           
          * ``state`` - The state of the VPC (``pending`` | ``available`` ). 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-id`` - The ID of the VPC. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def wait_until_exists(self, Filters: List = None, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcs>`_
        
        **Request Syntax** 
        ::
        
          vpc.wait_until_exists(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``cidr`` - The primary IPv4 CIDR block of the VPC. The CIDR block you specify must exactly match the VPC\'s CIDR block for information to be returned for the VPC. Must contain the slash followed by one or two digits (for example, ``/28`` ). 
           
          * ``cidr-block-association.cidr-block`` - An IPv4 CIDR block associated with the VPC. 
           
          * ``cidr-block-association.association-id`` - The association ID for an IPv4 CIDR block associated with the VPC. 
           
          * ``cidr-block-association.state`` - The state of an IPv4 CIDR block associated with the VPC. 
           
          * ``dhcp-options-id`` - The ID of a set of DHCP options. 
           
          * ``ipv6-cidr-block-association.ipv6-cidr-block`` - An IPv6 CIDR block associated with the VPC. 
           
          * ``ipv6-cidr-block-association.association-id`` - The association ID for an IPv6 CIDR block associated with the VPC. 
           
          * ``ipv6-cidr-block-association.state`` - The state of an IPv6 CIDR block associated with the VPC. 
           
          * ``isDefault`` - Indicates whether the VPC is the default VPC. 
           
          * ``state`` - The state of the VPC (``pending`` | ``available`` ). 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-id`` - The ID of the VPC. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
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
        """
        
        For an inter-region VPC peering connection request, you must accept the VPC peering connection in the region of the accepter VPC.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AcceptVpcPeeringConnection>`_
        
        **Request Syntax** 
        ::
        
          response = vpc_peering_connection.accept(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'VpcPeeringConnection\': {
                    \'AccepterVpcInfo\': {
                        \'CidrBlock\': \'string\',
                        \'Ipv6CidrBlockSet\': [
                            {
                                \'Ipv6CidrBlock\': \'string\'
                            },
                        ],
                        \'CidrBlockSet\': [
                            {
                                \'CidrBlock\': \'string\'
                            },
                        ],
                        \'OwnerId\': \'string\',
                        \'PeeringOptions\': {
                            \'AllowDnsResolutionFromRemoteVpc\': True|False,
                            \'AllowEgressFromLocalClassicLinkToRemoteVpc\': True|False,
                            \'AllowEgressFromLocalVpcToRemoteClassicLink\': True|False
                        },
                        \'VpcId\': \'string\',
                        \'Region\': \'string\'
                    },
                    \'ExpirationTime\': datetime(2015, 1, 1),
                    \'RequesterVpcInfo\': {
                        \'CidrBlock\': \'string\',
                        \'Ipv6CidrBlockSet\': [
                            {
                                \'Ipv6CidrBlock\': \'string\'
                            },
                        ],
                        \'CidrBlockSet\': [
                            {
                                \'CidrBlock\': \'string\'
                            },
                        ],
                        \'OwnerId\': \'string\',
                        \'PeeringOptions\': {
                            \'AllowDnsResolutionFromRemoteVpc\': True|False,
                            \'AllowEgressFromLocalClassicLinkToRemoteVpc\': True|False,
                            \'AllowEgressFromLocalVpcToRemoteClassicLink\': True|False
                        },
                        \'VpcId\': \'string\',
                        \'Region\': \'string\'
                    },
                    \'Status\': {
                        \'Code\': \'initiating-request\'|\'pending-acceptance\'|\'active\'|\'deleted\'|\'rejected\'|\'failed\'|\'expired\'|\'provisioning\'|\'deleting\',
                        \'Message\': \'string\'
                    },
                    \'Tags\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ],
                    \'VpcPeeringConnectionId\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **VpcPeeringConnection** *(dict) --* 
        
              Information about the VPC peering connection.
        
              - **AccepterVpcInfo** *(dict) --* 
        
                Information about the accepter VPC. CIDR block information is only returned when describing an active VPC peering connection.
        
                - **CidrBlock** *(string) --* 
        
                  The IPv4 CIDR block for the VPC.
        
                - **Ipv6CidrBlockSet** *(list) --* 
        
                  The IPv6 CIDR block for the VPC.
        
                  - *(dict) --* 
        
                    Describes an IPv6 CIDR block.
        
                    - **Ipv6CidrBlock** *(string) --* 
        
                      The IPv6 CIDR block.
        
                - **CidrBlockSet** *(list) --* 
        
                  Information about the IPv4 CIDR blocks for the VPC.
        
                  - *(dict) --* 
        
                    Describes an IPv4 CIDR block.
        
                    - **CidrBlock** *(string) --* 
        
                      The IPv4 CIDR block.
        
                - **OwnerId** *(string) --* 
        
                  The AWS account ID of the VPC owner.
        
                - **PeeringOptions** *(dict) --* 
        
                  Information about the VPC peering connection options for the accepter or requester VPC.
        
                  - **AllowDnsResolutionFromRemoteVpc** *(boolean) --* 
        
                    Indicates whether a local VPC can resolve public DNS hostnames to private IP addresses when queried from instances in a peer VPC.
        
                  - **AllowEgressFromLocalClassicLinkToRemoteVpc** *(boolean) --* 
        
                    Indicates whether a local ClassicLink connection can communicate with the peer VPC over the VPC peering connection.
        
                  - **AllowEgressFromLocalVpcToRemoteClassicLink** *(boolean) --* 
        
                    Indicates whether a local VPC can communicate with a ClassicLink connection in the peer VPC over the VPC peering connection.
        
                - **VpcId** *(string) --* 
        
                  The ID of the VPC.
        
                - **Region** *(string) --* 
        
                  The region in which the VPC is located.
        
              - **ExpirationTime** *(datetime) --* 
        
                The time that an unaccepted VPC peering connection will expire.
        
              - **RequesterVpcInfo** *(dict) --* 
        
                Information about the requester VPC. CIDR block information is only returned when describing an active VPC peering connection.
        
                - **CidrBlock** *(string) --* 
        
                  The IPv4 CIDR block for the VPC.
        
                - **Ipv6CidrBlockSet** *(list) --* 
        
                  The IPv6 CIDR block for the VPC.
        
                  - *(dict) --* 
        
                    Describes an IPv6 CIDR block.
        
                    - **Ipv6CidrBlock** *(string) --* 
        
                      The IPv6 CIDR block.
        
                - **CidrBlockSet** *(list) --* 
        
                  Information about the IPv4 CIDR blocks for the VPC.
        
                  - *(dict) --* 
        
                    Describes an IPv4 CIDR block.
        
                    - **CidrBlock** *(string) --* 
        
                      The IPv4 CIDR block.
        
                - **OwnerId** *(string) --* 
        
                  The AWS account ID of the VPC owner.
        
                - **PeeringOptions** *(dict) --* 
        
                  Information about the VPC peering connection options for the accepter or requester VPC.
        
                  - **AllowDnsResolutionFromRemoteVpc** *(boolean) --* 
        
                    Indicates whether a local VPC can resolve public DNS hostnames to private IP addresses when queried from instances in a peer VPC.
        
                  - **AllowEgressFromLocalClassicLinkToRemoteVpc** *(boolean) --* 
        
                    Indicates whether a local ClassicLink connection can communicate with the peer VPC over the VPC peering connection.
        
                  - **AllowEgressFromLocalVpcToRemoteClassicLink** *(boolean) --* 
        
                    Indicates whether a local VPC can communicate with a ClassicLink connection in the peer VPC over the VPC peering connection.
        
                - **VpcId** *(string) --* 
        
                  The ID of the VPC.
        
                - **Region** *(string) --* 
        
                  The region in which the VPC is located.
        
              - **Status** *(dict) --* 
        
                The status of the VPC peering connection.
        
                - **Code** *(string) --* 
        
                  The status of the VPC peering connection.
        
                - **Message** *(string) --* 
        
                  A message that provides more information about the status, if applicable.
        
              - **Tags** *(list) --* 
        
                Any tags assigned to the resource.
        
                - *(dict) --* 
        
                  Describes a tag.
        
                  - **Key** *(string) --* 
        
                    The key of the tag.
        
                    Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
                  - **Value** *(string) --* 
        
                    The value of the tag.
        
                    Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
              - **VpcPeeringConnectionId** *(string) --* 
        
                The ID of the VPC peering connection.
        
        """
        pass

    def delete(self, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DeleteVpcPeeringConnection>`_
        
        **Request Syntax** 
        ::
        
          response = vpc_peering_connection.delete(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Return\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Return** *(boolean) --* 
        
              Returns ``true`` if the request succeeds; otherwise, it returns an error.
        
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          vpc_peering_connection.load()
        :returns: None
        """
        pass

    def reject(self, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/RejectVpcPeeringConnection>`_
        
        **Request Syntax** 
        ::
        
          response = vpc_peering_connection.reject(
              DryRun=True|False,
              
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Return\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Return** *(boolean) --* 
        
              Returns ``true`` if the request succeeds; otherwise, it returns an error.
        
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          vpc_peering_connection.load()
        :returns: None
        """
        pass

    def wait_until_exists(self, Filters: List = None, DryRun: bool = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcPeeringConnections>`_
        
        **Request Syntax** 
        ::
        
          vpc_peering_connection.wait_until_exists(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``accepter-vpc-info.cidr-block`` - The IPv4 CIDR block of the accepter VPC. 
           
          * ``accepter-vpc-info.owner-id`` - The AWS account ID of the owner of the accepter VPC. 
           
          * ``accepter-vpc-info.vpc-id`` - The ID of the accepter VPC. 
           
          * ``expiration-time`` - The expiration date and time for the VPC peering connection. 
           
          * ``requester-vpc-info.cidr-block`` - The IPv4 CIDR block of the requester\'s VPC. 
           
          * ``requester-vpc-info.owner-id`` - The AWS account ID of the owner of the requester VPC. 
           
          * ``requester-vpc-info.vpc-id`` - The ID of the requester VPC. 
           
          * ``status-code`` - The status of the VPC peering connection (``pending-acceptance`` | ``failed`` | ``expired`` | ``provisioning`` | ``active`` | ``deleting`` | ``deleted`` | ``rejected`` ). 
           
          * ``status-message`` - A message that provides more information about the status of the VPC peering connection, if applicable. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-peering-connection-id`` - The ID of the VPC peering connection. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
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
        """
        
        An Elastic IP address is for use in either the EC2-Classic platform or in a VPC. For more information, see `Elastic IP Addresses <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        [EC2-Classic, VPC in an EC2-VPC-only account] If the Elastic IP address is already associated with a different instance, it is disassociated from that instance and associated with the specified instance. If you associate an Elastic IP address with an instance that has an existing Elastic IP address, the existing address is disassociated from the instance, but remains allocated to your account.
        
        [VPC in an EC2-Classic account] If you don\'t specify a private IP address, the Elastic IP address is associated with the primary IP address. If the Elastic IP address is already associated with a different instance or a network interface, you get an error unless you allow reassociation. You cannot associate an Elastic IP address with an instance or network interface that has an existing Elastic IP address.
        
        .. warning::
        
          This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn\'t return an error, and you may be charged for each time the Elastic IP address is remapped to the same instance. For more information, see the *Elastic IP Addresses* section of `Amazon EC2 Pricing <http://aws.amazon.com/ec2/pricing/>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AssociateAddress>`_
        
        **Request Syntax** 
        ::
        
          response = vpc_address.associate(
              InstanceId=\'string\',
              PublicIp=\'string\',
              AllowReassociation=True|False,
              DryRun=True|False,
              NetworkInterfaceId=\'string\',
              PrivateIpAddress=\'string\'
          )
        :type InstanceId: string
        :param InstanceId: 
        
          The ID of the instance. This is required for EC2-Classic. For EC2-VPC, you can specify either the instance ID or the network interface ID, but not both. The operation fails if you specify an instance ID unless exactly one network interface is attached.
        
        :type PublicIp: string
        :param PublicIp: 
        
          The Elastic IP address. This is required for EC2-Classic.
        
        :type AllowReassociation: boolean
        :param AllowReassociation: 
        
          [EC2-VPC] For a VPC in an EC2-Classic account, specify true to allow an Elastic IP address that is already associated with an instance or network interface to be reassociated with the specified instance or network interface. Otherwise, the operation fails. In a VPC in an EC2-VPC-only account, reassociation is automatic, therefore you can specify false to ensure the operation fails if the Elastic IP address is already associated with another resource.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type NetworkInterfaceId: string
        :param NetworkInterfaceId: 
        
          [EC2-VPC] The ID of the network interface. If the instance has more than one network interface, you must specify a network interface ID.
        
        :type PrivateIpAddress: string
        :param PrivateIpAddress: 
        
          [EC2-VPC] The primary or secondary private IP address to associate with the Elastic IP address. If no private IP address is specified, the Elastic IP address is associated with the primary private IP address.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AssociationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AssociationId** *(string) --* 
        
              [EC2-VPC] The ID that represents the association of the Elastic IP address with an instance.
        
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          vpc_address.load()
        :returns: None
        """
        pass

    def release(self, PublicIp: str = None, DryRun: bool = None):
        """
        
        [EC2-Classic, default VPC] Releasing an Elastic IP address automatically disassociates it from any instance that it\'s associated with. To disassociate an Elastic IP address without releasing it, use  DisassociateAddress .
        
        [Nondefault VPC] You must use  DisassociateAddress to disassociate the Elastic IP address before you can release it. Otherwise, Amazon EC2 returns an error (``InvalidIPAddress.InUse`` ).
        
        After releasing an Elastic IP address, it is released to the IP address pool. Be sure to update your DNS records and any servers or devices that communicate with the address. If you attempt to release an Elastic IP address that you already released, you\'ll get an ``AuthFailure`` error if the address is already allocated to another AWS account.
        
        [EC2-VPC] After you release an Elastic IP address for use in a VPC, you might be able to recover it. For more information, see  AllocateAddress .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ReleaseAddress>`_
        
        **Request Syntax** 
        ::
        
          response = vpc_address.release(
              PublicIp=\'string\',
              DryRun=True|False
          )
        :type PublicIp: string
        :param PublicIp: 
        
          [EC2-Classic] The Elastic IP address. Required for EC2-Classic.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/None>`_
        
        **Request Syntax** 
        
        ::
        
          vpc_address.load()
        :returns: None
        """
        pass


class classic_addresses(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['ClassicAddress']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeAddresses>`_
        
        **Request Syntax** 
        ::
        
          classic_address_iterator = ec2.classic_addresses.all()
          
        :rtype: list(:py:class:`ec2.ClassicAddress`)
        :returns: A list of ClassicAddress resources
        """
        pass

    
    @classmethod
    def filter(cls, PublicIps: List = None, AllocationIds: List = None, DryRun: bool = None) -> List['ClassicAddress']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeAddresses>`_
        
        **Request Syntax** 
        ::
        
          classic_address_iterator = ec2.classic_addresses.filter(
              PublicIps=[
                  \'string\',
              ],
              AllocationIds=[
                  \'string\',
              ],
              DryRun=True|False
          )
        :type PublicIps: list
        :param PublicIps: 
        
          [EC2-Classic] One or more Elastic IP addresses.
        
          Default: Describes all your Elastic IP addresses.
        
          - *(string) --* 
        
        :type AllocationIds: list
        :param AllocationIds: 
        
          [EC2-VPC] One or more allocation IDs.
        
          Default: Describes all your Elastic IP addresses.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: list(:py:class:`ec2.ClassicAddress`)
        :returns: A list of ClassicAddress resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['ClassicAddress']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeAddresses>`_
        
        **Request Syntax** 
        ::
        
          classic_address_iterator = ec2.classic_addresses.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.ClassicAddress`)
        :returns: A list of ClassicAddress resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['ClassicAddress']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeAddresses>`_
        
        **Request Syntax** 
        ::
        
          classic_address_iterator = ec2.classic_addresses.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.ClassicAddress`)
        :returns: A list of ClassicAddress resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class dhcp_options_sets(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['DhcpOptions']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeDhcpOptions>`_
        
        **Request Syntax** 
        ::
        
          dhcp_options_iterator = ec2.dhcp_options_sets.all()
          
        :rtype: list(:py:class:`ec2.DhcpOptions`)
        :returns: A list of DhcpOptions resources
        """
        pass

    
    @classmethod
    def filter(cls, DhcpOptionsIds: List = None, Filters: List = None, DryRun: bool = None) -> List['DhcpOptions']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeDhcpOptions>`_
        
        **Request Syntax** 
        ::
        
          dhcp_options_iterator = ec2.dhcp_options_sets.filter(
              DhcpOptionsIds=[
                  \'string\',
              ],
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False
          )
        :type DhcpOptionsIds: list
        :param DhcpOptionsIds: 
        
          The IDs of one or more DHCP options sets.
        
          Default: Describes all your DHCP options sets.
        
          - *(string) --* 
        
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``dhcp-options-id`` - The ID of a set of DHCP options. 
           
          * ``key`` - The key for one of the options (for example, ``domain-name`` ). 
           
          * ``value`` - The value for one of the options. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: list(:py:class:`ec2.DhcpOptions`)
        :returns: A list of DhcpOptions resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['DhcpOptions']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeDhcpOptions>`_
        
        **Request Syntax** 
        ::
        
          dhcp_options_iterator = ec2.dhcp_options_sets.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.DhcpOptions`)
        :returns: A list of DhcpOptions resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['DhcpOptions']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeDhcpOptions>`_
        
        **Request Syntax** 
        ::
        
          dhcp_options_iterator = ec2.dhcp_options_sets.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.DhcpOptions`)
        :returns: A list of DhcpOptions resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class images(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Image']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeImages>`_
        
        **Request Syntax** 
        ::
        
          image_iterator = ec2.images.all()
          
        :rtype: list(:py:class:`ec2.Image`)
        :returns: A list of Image resources
        """
        pass

    
    @classmethod
    def filter(cls, ExecutableUsers: List = None, Filters: List = None, ImageIds: List = None, Owners: List = None, DryRun: bool = None) -> List['Image']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeImages>`_
        
        **Request Syntax** 
        ::
        
          image_iterator = ec2.images.filter(
              ExecutableUsers=[
                  \'string\',
              ],
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              ImageIds=[
                  \'string\',
              ],
              Owners=[
                  \'string\',
              ],
              DryRun=True|False
          )
        :type ExecutableUsers: list
        :param ExecutableUsers: 
        
          Scopes the images by users with explicit launch permissions. Specify an AWS account ID, ``self`` (the sender of the request), or ``all`` (public AMIs).
        
          - *(string) --* 
        
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``architecture`` - The image architecture (``i386`` | ``x86_64`` ). 
           
          * ``block-device-mapping.delete-on-termination`` - A Boolean value that indicates whether the Amazon EBS volume is deleted on instance termination. 
           
          * ``block-device-mapping.device-name`` - The device name specified in the block device mapping (for example, ``/dev/sdh`` or ``xvdh`` ). 
           
          * ``block-device-mapping.snapshot-id`` - The ID of the snapshot used for the EBS volume. 
           
          * ``block-device-mapping.volume-size`` - The volume size of the EBS volume, in GiB. 
           
          * ``block-device-mapping.volume-type`` - The volume type of the EBS volume (``gp2`` | ``io1`` | ``st1`` | ``sc1`` | ``standard`` ). 
           
          * ``description`` - The description of the image (provided during image creation). 
           
          * ``ena-support`` - A Boolean that indicates whether enhanced networking with ENA is enabled. 
           
          * ``hypervisor`` - The hypervisor type (``ovm`` | ``xen`` ). 
           
          * ``image-id`` - The ID of the image. 
           
          * ``image-type`` - The image type (``machine`` | ``kernel`` | ``ramdisk`` ). 
           
          * ``is-public`` - A Boolean that indicates whether the image is public. 
           
          * ``kernel-id`` - The kernel ID. 
           
          * ``manifest-location`` - The location of the image manifest. 
           
          * ``name`` - The name of the AMI (provided during image creation). 
           
          * ``owner-alias`` - String value from an Amazon-maintained list (``amazon`` | ``aws-marketplace`` | ``microsoft`` ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM console. 
           
          * ``owner-id`` - The AWS account ID of the image owner. 
           
          * ``platform`` - The platform. To only list Windows-based AMIs, use ``windows`` . 
           
          * ``product-code`` - The product code. 
           
          * ``product-code.type`` - The type of the product code (``devpay`` | ``marketplace`` ). 
           
          * ``ramdisk-id`` - The RAM disk ID. 
           
          * ``root-device-name`` - The device name of the root device volume (for example, ``/dev/sda1`` ). 
           
          * ``root-device-type`` - The type of the root device volume (``ebs`` | ``instance-store`` ). 
           
          * ``state`` - The state of the image (``available`` | ``pending`` | ``failed`` ). 
           
          * ``state-reason-code`` - The reason code for the state change. 
           
          * ``state-reason-message`` - The message for the state change. 
           
          * ``sriov-net-support`` - A value of ``simple`` indicates that enhanced networking with the Intel 82599 VF interface is enabled. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``virtualization-type`` - The virtualization type (``paravirtual`` | ``hvm`` ). 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type ImageIds: list
        :param ImageIds: 
        
          One or more image IDs.
        
          Default: Describes all images available to you.
        
          - *(string) --* 
        
        :type Owners: list
        :param Owners: 
        
          Filters the images by the owner. Specify an AWS account ID, ``self`` (owner is the sender of the request), or an AWS owner alias (valid values are ``amazon`` | ``aws-marketplace`` | ``microsoft`` ). Omitting this option returns all images for which you have launch permissions, regardless of ownership.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: list(:py:class:`ec2.Image`)
        :returns: A list of Image resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Image']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeImages>`_
        
        **Request Syntax** 
        ::
        
          image_iterator = ec2.images.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.Image`)
        :returns: A list of Image resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Image']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeImages>`_
        
        **Request Syntax** 
        ::
        
          image_iterator = ec2.images.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.Image`)
        :returns: A list of Image resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class instances(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Instance']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances>`_
        
        **Request Syntax** 
        ::
        
          instance_iterator = ec2.instances.all()
          
        :rtype: list(:py:class:`ec2.Instance`)
        :returns: A list of Instance resources
        """
        pass

    
    @classmethod
    def create_tags(cls, Tags: List, DryRun: bool = None):
        """
        
        For more information about tags, see `Tagging Your Resources <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . For more information about creating IAM policies that control users\' access to resources based on tags, see `Supported Resource-Level Permissions for Amazon EC2 API Actions <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateTags>`_
        
        **Request Syntax** 
        ::
        
          response = ec2.instances.create_tags(
              DryRun=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. The ``value`` parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. 
        
          - *(dict) --* 
        
            Describes a tag.
        
            - **Key** *(string) --* 
        
              The key of the tag.
        
              Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
              Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        
        :returns: None
        """
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None) -> List['Instance']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances>`_
        
        **Request Syntax** 
        ::
        
          instance_iterator = ec2.instances.filter(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              InstanceIds=[
                  \'string\',
              ],
              DryRun=True|False,
              MaxResults=123,
              NextToken=\'string\'
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``affinity`` - The affinity setting for an instance running on a Dedicated Host (``default`` | ``host`` ). 
           
          * ``architecture`` - The instance architecture (``i386`` | ``x86_64`` ). 
           
          * ``availability-zone`` - The Availability Zone of the instance. 
           
          * ``block-device-mapping.attach-time`` - The attach time for an EBS volume mapped to the instance, for example, ``2010-09-15T17:15:20.000Z`` . 
           
          * ``block-device-mapping.delete-on-termination`` - A Boolean that indicates whether the EBS volume is deleted on instance termination. 
           
          * ``block-device-mapping.device-name`` - The device name specified in the block device mapping (for example, ``/dev/sdh`` or ``xvdh`` ). 
           
          * ``block-device-mapping.status`` - The status for the EBS volume (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``block-device-mapping.volume-id`` - The volume ID of the EBS volume. 
           
          * ``client-token`` - The idempotency token you provided when you launched the instance. 
           
          * ``dns-name`` - The public DNS name of the instance. 
           
          * ``group-id`` - The ID of the security group for the instance. EC2-Classic only. 
           
          * ``group-name`` - The name of the security group for the instance. EC2-Classic only. 
           
          * ``host-id`` - The ID of the Dedicated Host on which the instance is running, if applicable. 
           
          * ``hypervisor`` - The hypervisor type of the instance (``ovm`` | ``xen`` ). 
           
          * ``iam-instance-profile.arn`` - The instance profile associated with the instance. Specified as an ARN. 
           
          * ``image-id`` - The ID of the image used to launch the instance. 
           
          * ``instance-id`` - The ID of the instance. 
           
          * ``instance-lifecycle`` - Indicates whether this is a Spot Instance or a Scheduled Instance (``spot`` | ``scheduled`` ). 
           
          * ``instance-state-code`` - The state of the instance, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are: 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped). 
           
          * ``instance-state-name`` - The state of the instance (``pending`` | ``running`` | ``shutting-down`` | ``terminated`` | ``stopping`` | ``stopped`` ). 
           
          * ``instance-type`` - The type of instance (for example, ``t2.micro`` ). 
           
          * ``instance.group-id`` - The ID of the security group for the instance.  
           
          * ``instance.group-name`` - The name of the security group for the instance.  
           
          * ``ip-address`` - The public IPv4 address of the instance. 
           
          * ``kernel-id`` - The kernel ID. 
           
          * ``key-name`` - The name of the key pair used when the instance was launched. 
           
          * ``launch-index`` - When launching multiple instances, this is the index for the instance in the launch group (for example, 0, 1, 2, and so on).  
           
          * ``launch-time`` - The time when the instance was launched. 
           
          * ``monitoring-state`` - Indicates whether detailed monitoring is enabled (``disabled`` | ``enabled`` ). 
           
          * ``network-interface.addresses.private-ip-address`` - The private IPv4 address associated with the network interface. 
           
          * ``network-interface.addresses.primary`` - Specifies whether the IPv4 address of the network interface is the primary private IPv4 address. 
           
          * ``network-interface.addresses.association.public-ip`` - The ID of the association of an Elastic IP address (IPv4) with a network interface. 
           
          * ``network-interface.addresses.association.ip-owner-id`` - The owner ID of the private IPv4 address associated with the network interface. 
           
          * ``network-interface.association.public-ip`` - The address of the Elastic IP address (IPv4) bound to the network interface. 
           
          * ``network-interface.association.ip-owner-id`` - The owner of the Elastic IP address (IPv4) associated with the network interface. 
           
          * ``network-interface.association.allocation-id`` - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface. 
           
          * ``network-interface.association.association-id`` - The association ID returned when the network interface was associated with an IPv4 address. 
           
          * ``network-interface.attachment.attachment-id`` - The ID of the interface attachment. 
           
          * ``network-interface.attachment.instance-id`` - The ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.instance-owner-id`` - The owner ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.device-index`` - The device index to which the network interface is attached. 
           
          * ``network-interface.attachment.status`` - The status of the attachment (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``network-interface.attachment.attach-time`` - The time that the network interface was attached to an instance. 
           
          * ``network-interface.attachment.delete-on-termination`` - Specifies whether the attachment is deleted when an instance is terminated. 
           
          * ``network-interface.availability-zone`` - The Availability Zone for the network interface. 
           
          * ``network-interface.description`` - The description of the network interface. 
           
          * ``network-interface.group-id`` - The ID of a security group associated with the network interface. 
           
          * ``network-interface.group-name`` - The name of a security group associated with the network interface. 
           
          * ``network-interface.ipv6-addresses.ipv6-address`` - The IPv6 address associated with the network interface. 
           
          * ``network-interface.mac-address`` - The MAC address of the network interface. 
           
          * ``network-interface.network-interface-id`` - The ID of the network interface. 
           
          * ``network-interface.owner-id`` - The ID of the owner of the network interface. 
           
          * ``network-interface.private-dns-name`` - The private DNS name of the network interface. 
           
          * ``network-interface.requester-id`` - The requester ID for the network interface. 
           
          * ``network-interface.requester-managed`` - Indicates whether the network interface is being managed by AWS. 
           
          * ``network-interface.status`` - The status of the network interface (``available`` ) | ``in-use`` ). 
           
          * ``network-interface.source-dest-check`` - Whether the network interface performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the network interface to perform network address translation (NAT) in your VPC. 
           
          * ``network-interface.subnet-id`` - The ID of the subnet for the network interface. 
           
          * ``network-interface.vpc-id`` - The ID of the VPC for the network interface. 
           
          * ``owner-id`` - The AWS account ID of the instance owner. 
           
          * ``placement-group-name`` - The name of the placement group for the instance. 
           
          * ``platform`` - The platform. Use ``windows`` if you have Windows instances; otherwise, leave blank. 
           
          * ``private-dns-name`` - The private IPv4 DNS name of the instance. 
           
          * ``private-ip-address`` - The private IPv4 address of the instance. 
           
          * ``product-code`` - The product code associated with the AMI used to launch the instance. 
           
          * ``product-code.type`` - The type of product code (``devpay`` | ``marketplace`` ). 
           
          * ``ramdisk-id`` - The RAM disk ID. 
           
          * ``reason`` - The reason for the current state of the instance (for example, shows \"User Initiated [date]\" when you stop or terminate the instance). Similar to the state-reason-code filter. 
           
          * ``requester-id`` - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on). 
           
          * ``reservation-id`` - The ID of the instance\'s reservation. A reservation ID is created any time you launch an instance. A reservation ID has a one-to-one relationship with an instance launch request, but can be associated with more than one instance if you launch multiple instances using the same launch request. For example, if you launch one instance, you get one reservation ID. If you launch ten instances using the same launch request, you also get one reservation ID. 
           
          * ``root-device-name`` - The device name of the root device volume (for example, ``/dev/sda1`` ). 
           
          * ``root-device-type`` - The type of the root device volume (``ebs`` | ``instance-store`` ). 
           
          * ``source-dest-check`` - Indicates whether the instance performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the instance to perform network address translation (NAT) in your VPC.  
           
          * ``spot-instance-request-id`` - The ID of the Spot Instance request. 
           
          * ``state-reason-code`` - The reason code for the state change. 
           
          * ``state-reason-message`` - A message that describes the state change. 
           
          * ``subnet-id`` - The ID of the subnet for the instance. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific key, regardless of the tag value. 
           
          * ``tenancy`` - The tenancy of an instance (``dedicated`` | ``default`` | ``host`` ). 
           
          * ``virtualization-type`` - The virtualization type of the instance (``paravirtual`` | ``hvm`` ). 
           
          * ``vpc-id`` - The ID of the VPC that the instance is running in. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type InstanceIds: list
        :param InstanceIds: 
        
          One or more instance IDs.
        
          Default: Describes all your instances.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to request the next page of results.
        
        :rtype: list(:py:class:`ec2.Instance`)
        :returns: A list of Instance resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Instance']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances>`_
        
        **Request Syntax** 
        ::
        
          instance_iterator = ec2.instances.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.Instance`)
        :returns: A list of Instance resources
        """
        pass

    
    @classmethod
    def monitor(cls, DryRun: bool = None) -> Dict:
        """
        
        To disable detailed monitoring, see .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/MonitorInstances>`_
        
        **Request Syntax** 
        ::
        
          response = ec2.instances.monitor(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstanceMonitorings\': [
                    {
                        \'InstanceId\': \'string\',
                        \'Monitoring\': {
                            \'State\': \'disabled\'|\'disabling\'|\'enabled\'|\'pending\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of MonitorInstances.
        
            - **InstanceMonitorings** *(list) --* 
        
              The monitoring information.
        
              - *(dict) --* 
        
                Describes the monitoring of an instance.
        
                - **InstanceId** *(string) --* 
        
                  The ID of the instance.
        
                - **Monitoring** *(dict) --* 
        
                  The monitoring for the instance.
        
                  - **State** *(string) --* 
        
                    Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
        
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Instance']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances>`_
        
        **Request Syntax** 
        ::
        
          instance_iterator = ec2.instances.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.Instance`)
        :returns: A list of Instance resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass

    
    @classmethod
    def reboot(cls, DryRun: bool = None):
        """
        
        If an instance does not cleanly shut down within four minutes, Amazon EC2 performs a hard reboot.
        
        For more information about troubleshooting, see `Getting Console Output and Rebooting Instances <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-console.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/RebootInstances>`_
        
        **Request Syntax** 
        ::
        
          response = ec2.instances.reboot(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :returns: None
        """
        pass

    
    @classmethod
    def start(cls, AdditionalInfo: str = None, DryRun: bool = None) -> Dict:
        """
        
        Instances that use Amazon EBS volumes as their root devices can be quickly stopped and started. When an instance is stopped, the compute resources are released and you are not billed for instance usage. However, your root partition Amazon EBS volume remains and continues to persist your data, and you are charged for Amazon EBS volume usage. You can restart your instance at any time. Every time you start your Windows instance, Amazon EC2 charges you for a full instance hour. If you stop and restart your Windows instance, a new instance hour begins and Amazon EC2 charges you for another full instance hour even if you are still within the same 60-minute period when it was stopped. Every time you start your Linux instance, Amazon EC2 charges a one-minute minimum for instance usage, and thereafter charges per second for instance usage.
        
        Before stopping an instance, make sure it is in a state from which it can be restarted. Stopping an instance does not preserve data stored in RAM.
        
        Performing this operation on an instance that uses an instance store as its root device returns an error.
        
        For more information, see `Stopping Instances <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/StartInstances>`_
        
        **Request Syntax** 
        ::
        
          response = ec2.instances.start(
              AdditionalInfo=\'string\',
              DryRun=True|False
          )
        :type AdditionalInfo: string
        :param AdditionalInfo: 
        
          Reserved.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StartingInstances\': [
                    {
                        \'CurrentState\': {
                            \'Code\': 123,
                            \'Name\': \'pending\'|\'running\'|\'shutting-down\'|\'terminated\'|\'stopping\'|\'stopped\'
                        },
                        \'InstanceId\': \'string\',
                        \'PreviousState\': {
                            \'Code\': 123,
                            \'Name\': \'pending\'|\'running\'|\'shutting-down\'|\'terminated\'|\'stopping\'|\'stopped\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of StartInstances.
        
            - **StartingInstances** *(list) --* 
        
              Information about one or more started instances.
        
              - *(dict) --* 
        
                Describes an instance state change.
        
                - **CurrentState** *(dict) --* 
        
                  The current state of the instance.
        
                  - **Code** *(integer) --* 
        
                    The low byte represents the state. The high byte is used for internal purposes and should be ignored.
        
                    * ``0`` : ``pending``   
                     
                    * ``16`` : ``running``   
                     
                    * ``32`` : ``shutting-down``   
                     
                    * ``48`` : ``terminated``   
                     
                    * ``64`` : ``stopping``   
                     
                    * ``80`` : ``stopped``   
                     
                  - **Name** *(string) --* 
        
                    The current state of the instance.
        
                - **InstanceId** *(string) --* 
        
                  The ID of the instance.
        
                - **PreviousState** *(dict) --* 
        
                  The previous state of the instance.
        
                  - **Code** *(integer) --* 
        
                    The low byte represents the state. The high byte is used for internal purposes and should be ignored.
        
                    * ``0`` : ``pending``   
                     
                    * ``16`` : ``running``   
                     
                    * ``32`` : ``shutting-down``   
                     
                    * ``48`` : ``terminated``   
                     
                    * ``64`` : ``stopping``   
                     
                    * ``80`` : ``stopped``   
                     
                  - **Name** *(string) --* 
        
                    The current state of the instance.
        
        """
        pass

    
    @classmethod
    def stop(cls, DryRun: bool = None, Force: bool = None) -> Dict:
        """
        
        We don\'t charge usage for a stopped instance, or data transfer fees; however, your root partition Amazon EBS volume remains and continues to persist your data, and you are charged for Amazon EBS volume usage. Every time you start your Windows instance, Amazon EC2 charges you for a full instance hour. If you stop and restart your Windows instance, a new instance hour begins and Amazon EC2 charges you for another full instance hour even if you are still within the same 60-minute period when it was stopped. Every time you start your Linux instance, Amazon EC2 charges a one-minute minimum for instance usage, and thereafter charges per second for instance usage.
        
        You can\'t start or stop Spot Instances, and you can\'t stop instance store-backed instances.
        
        When you stop an instance, we shut it down. You can restart your instance at any time. Before stopping an instance, make sure it is in a state from which it can be restarted. Stopping an instance does not preserve data stored in RAM.
        
        Stopping an instance is different to rebooting or terminating it. For example, when you stop an instance, the root device and any other devices attached to the instance persist. When you terminate an instance, the root device and any other devices attached during the instance launch are automatically deleted. For more information about the differences between rebooting, stopping, and terminating instances, see `Instance Lifecycle <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        When you stop an instance, we attempt to shut it down forcibly after a short while. If your instance appears stuck in the stopping state after a period of time, there may be an issue with the underlying host computer. For more information, see `Troubleshooting Stopping Your Instance <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesStopping.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/StopInstances>`_
        
        **Request Syntax** 
        ::
        
          response = ec2.instances.stop(
              DryRun=True|False,
              Force=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type Force: boolean
        :param Force: 
        
          Forces the instances to stop. The instances do not have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures. This option is not recommended for Windows instances.
        
          Default: ``false``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'StoppingInstances\': [
                    {
                        \'CurrentState\': {
                            \'Code\': 123,
                            \'Name\': \'pending\'|\'running\'|\'shutting-down\'|\'terminated\'|\'stopping\'|\'stopped\'
                        },
                        \'InstanceId\': \'string\',
                        \'PreviousState\': {
                            \'Code\': 123,
                            \'Name\': \'pending\'|\'running\'|\'shutting-down\'|\'terminated\'|\'stopping\'|\'stopped\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of StopInstances.
        
            - **StoppingInstances** *(list) --* 
        
              Information about one or more stopped instances.
        
              - *(dict) --* 
        
                Describes an instance state change.
        
                - **CurrentState** *(dict) --* 
        
                  The current state of the instance.
        
                  - **Code** *(integer) --* 
        
                    The low byte represents the state. The high byte is used for internal purposes and should be ignored.
        
                    * ``0`` : ``pending``   
                     
                    * ``16`` : ``running``   
                     
                    * ``32`` : ``shutting-down``   
                     
                    * ``48`` : ``terminated``   
                     
                    * ``64`` : ``stopping``   
                     
                    * ``80`` : ``stopped``   
                     
                  - **Name** *(string) --* 
        
                    The current state of the instance.
        
                - **InstanceId** *(string) --* 
        
                  The ID of the instance.
        
                - **PreviousState** *(dict) --* 
        
                  The previous state of the instance.
        
                  - **Code** *(integer) --* 
        
                    The low byte represents the state. The high byte is used for internal purposes and should be ignored.
        
                    * ``0`` : ``pending``   
                     
                    * ``16`` : ``running``   
                     
                    * ``32`` : ``shutting-down``   
                     
                    * ``48`` : ``terminated``   
                     
                    * ``64`` : ``stopping``   
                     
                    * ``80`` : ``stopped``   
                     
                  - **Name** *(string) --* 
        
                    The current state of the instance.
        
        """
        pass

    
    @classmethod
    def terminate(cls, DryRun: bool = None) -> Dict:
        """
        
        If you specify multiple instances and the request fails (for example, because of a single incorrect instance ID), none of the instances are terminated.
        
        Terminated instances remain visible after termination (for approximately one hour).
        
        By default, Amazon EC2 deletes all EBS volumes that were attached when the instance launched. Volumes attached after instance launch continue running.
        
        You can stop, start, and terminate EBS-backed instances. You can only terminate instance store-backed instances. What happens to an instance differs if you stop it or terminate it. For example, when you stop an instance, the root device and any other devices attached to the instance persist. When you terminate an instance, any attached EBS volumes with the ``DeleteOnTermination`` block device mapping parameter set to ``true`` are automatically deleted. For more information about the differences between stopping and terminating instances, see `Instance Lifecycle <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        For more information about troubleshooting, see `Troubleshooting Terminating Your Instance <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesShuttingDown.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/TerminateInstances>`_
        
        **Request Syntax** 
        ::
        
          response = ec2.instances.terminate(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TerminatingInstances\': [
                    {
                        \'CurrentState\': {
                            \'Code\': 123,
                            \'Name\': \'pending\'|\'running\'|\'shutting-down\'|\'terminated\'|\'stopping\'|\'stopped\'
                        },
                        \'InstanceId\': \'string\',
                        \'PreviousState\': {
                            \'Code\': 123,
                            \'Name\': \'pending\'|\'running\'|\'shutting-down\'|\'terminated\'|\'stopping\'|\'stopped\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of TerminateInstances.
        
            - **TerminatingInstances** *(list) --* 
        
              Information about one or more terminated instances.
        
              - *(dict) --* 
        
                Describes an instance state change.
        
                - **CurrentState** *(dict) --* 
        
                  The current state of the instance.
        
                  - **Code** *(integer) --* 
        
                    The low byte represents the state. The high byte is used for internal purposes and should be ignored.
        
                    * ``0`` : ``pending``   
                     
                    * ``16`` : ``running``   
                     
                    * ``32`` : ``shutting-down``   
                     
                    * ``48`` : ``terminated``   
                     
                    * ``64`` : ``stopping``   
                     
                    * ``80`` : ``stopped``   
                     
                  - **Name** *(string) --* 
        
                    The current state of the instance.
        
                - **InstanceId** *(string) --* 
        
                  The ID of the instance.
        
                - **PreviousState** *(dict) --* 
        
                  The previous state of the instance.
        
                  - **Code** *(integer) --* 
        
                    The low byte represents the state. The high byte is used for internal purposes and should be ignored.
        
                    * ``0`` : ``pending``   
                     
                    * ``16`` : ``running``   
                     
                    * ``32`` : ``shutting-down``   
                     
                    * ``48`` : ``terminated``   
                     
                    * ``64`` : ``stopping``   
                     
                    * ``80`` : ``stopped``   
                     
                  - **Name** *(string) --* 
        
                    The current state of the instance.
        
        """
        pass

    
    @classmethod
    def unmonitor(cls, DryRun: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/UnmonitorInstances>`_
        
        **Request Syntax** 
        ::
        
          response = ec2.instances.unmonitor(
              DryRun=True|False
          )
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstanceMonitorings\': [
                    {
                        \'InstanceId\': \'string\',
                        \'Monitoring\': {
                            \'State\': \'disabled\'|\'disabling\'|\'enabled\'|\'pending\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of UnmonitorInstances.
        
            - **InstanceMonitorings** *(list) --* 
        
              The monitoring information.
        
              - *(dict) --* 
        
                Describes the monitoring of an instance.
        
                - **InstanceId** *(string) --* 
        
                  The ID of the instance.
        
                - **Monitoring** *(dict) --* 
        
                  The monitoring for the instance.
        
                  - **State** *(string) --* 
        
                    Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
        
        """
        pass


class internet_gateways(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['InternetGateway']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInternetGateways>`_
        
        **Request Syntax** 
        ::
        
          internet_gateway_iterator = ec2.internet_gateways.all()
          
        :rtype: list(:py:class:`ec2.InternetGateway`)
        :returns: A list of InternetGateway resources
        """
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, DryRun: bool = None, InternetGatewayIds: List = None) -> List['InternetGateway']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInternetGateways>`_
        
        **Request Syntax** 
        ::
        
          internet_gateway_iterator = ec2.internet_gateways.filter(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              InternetGatewayIds=[
                  \'string\',
              ]
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``attachment.state`` - The current state of the attachment between the gateway and the VPC (``available`` ). Present only if a VPC is attached. 
           
          * ``attachment.vpc-id`` - The ID of an attached VPC. 
           
          * ``internet-gateway-id`` - The ID of the Internet gateway. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type InternetGatewayIds: list
        :param InternetGatewayIds: 
        
          One or more internet gateway IDs.
        
          Default: Describes all your internet gateways.
        
          - *(string) --* 
        
        :rtype: list(:py:class:`ec2.InternetGateway`)
        :returns: A list of InternetGateway resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['InternetGateway']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInternetGateways>`_
        
        **Request Syntax** 
        ::
        
          internet_gateway_iterator = ec2.internet_gateways.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.InternetGateway`)
        :returns: A list of InternetGateway resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['InternetGateway']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInternetGateways>`_
        
        **Request Syntax** 
        ::
        
          internet_gateway_iterator = ec2.internet_gateways.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.InternetGateway`)
        :returns: A list of InternetGateway resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class key_pairs(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['KeyPairInfo']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeKeyPairs>`_
        
        **Request Syntax** 
        ::
        
          key_pair_info_iterator = ec2.key_pairs.all()
          
        :rtype: list(:py:class:`ec2.KeyPairInfo`)
        :returns: A list of KeyPairInfo resources
        """
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, KeyNames: List = None, DryRun: bool = None) -> List['KeyPairInfo']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeKeyPairs>`_
        
        **Request Syntax** 
        ::
        
          key_pair_info_iterator = ec2.key_pairs.filter(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              KeyNames=[
                  \'string\',
              ],
              DryRun=True|False
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``fingerprint`` - The fingerprint of the key pair. 
           
          * ``key-name`` - The name of the key pair. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type KeyNames: list
        :param KeyNames: 
        
          One or more key pair names.
        
          Default: Describes all your key pairs.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: list(:py:class:`ec2.KeyPairInfo`)
        :returns: A list of KeyPairInfo resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['KeyPairInfo']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeKeyPairs>`_
        
        **Request Syntax** 
        ::
        
          key_pair_info_iterator = ec2.key_pairs.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.KeyPairInfo`)
        :returns: A list of KeyPairInfo resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['KeyPairInfo']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeKeyPairs>`_
        
        **Request Syntax** 
        ::
        
          key_pair_info_iterator = ec2.key_pairs.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.KeyPairInfo`)
        :returns: A list of KeyPairInfo resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class network_acls(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['NetworkAcl']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNetworkAcls>`_
        
        **Request Syntax** 
        ::
        
          network_acl_iterator = ec2.network_acls.all()
          
        :rtype: list(:py:class:`ec2.NetworkAcl`)
        :returns: A list of NetworkAcl resources
        """
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, DryRun: bool = None, NetworkAclIds: List = None) -> List['NetworkAcl']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNetworkAcls>`_
        
        **Request Syntax** 
        ::
        
          network_acl_iterator = ec2.network_acls.filter(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              NetworkAclIds=[
                  \'string\',
              ]
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``association.association-id`` - The ID of an association ID for the ACL. 
           
          * ``association.network-acl-id`` - The ID of the network ACL involved in the association. 
           
          * ``association.subnet-id`` - The ID of the subnet involved in the association. 
           
          * ``default`` - Indicates whether the ACL is the default network ACL for the VPC. 
           
          * ``entry.cidr`` - The IPv4 CIDR range specified in the entry. 
           
          * ``entry.icmp.code`` - The ICMP code specified in the entry, if any. 
           
          * ``entry.icmp.type`` - The ICMP type specified in the entry, if any. 
           
          * ``entry.ipv6-cidr`` - The IPv6 CIDR range specified in the entry. 
           
          * ``entry.port-range.from`` - The start of the port range specified in the entry.  
           
          * ``entry.port-range.to`` - The end of the port range specified in the entry.  
           
          * ``entry.protocol`` - The protocol specified in the entry (``tcp`` | ``udp`` | ``icmp`` or a protocol number). 
           
          * ``entry.rule-action`` - Allows or denies the matching traffic (``allow`` | ``deny`` ). 
           
          * ``entry.rule-number`` - The number of an entry (in other words, rule) in the set of ACL entries. 
           
          * ``network-acl-id`` - The ID of the network ACL. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-id`` - The ID of the VPC for the network ACL. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type NetworkAclIds: list
        :param NetworkAclIds: 
        
          One or more network ACL IDs.
        
          Default: Describes all your network ACLs.
        
          - *(string) --* 
        
        :rtype: list(:py:class:`ec2.NetworkAcl`)
        :returns: A list of NetworkAcl resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['NetworkAcl']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNetworkAcls>`_
        
        **Request Syntax** 
        ::
        
          network_acl_iterator = ec2.network_acls.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.NetworkAcl`)
        :returns: A list of NetworkAcl resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['NetworkAcl']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNetworkAcls>`_
        
        **Request Syntax** 
        ::
        
          network_acl_iterator = ec2.network_acls.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.NetworkAcl`)
        :returns: A list of NetworkAcl resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class network_interfaces(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['NetworkInterface']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNetworkInterfaces>`_
        
        **Request Syntax** 
        ::
        
          network_interface_iterator = ec2.network_interfaces.all()
          
        :rtype: list(:py:class:`ec2.NetworkInterface`)
        :returns: A list of NetworkInterface resources
        """
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, DryRun: bool = None, NetworkInterfaceIds: List = None, NextToken: str = None, MaxResults: int = None) -> List['NetworkInterface']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNetworkInterfaces>`_
        
        **Request Syntax** 
        ::
        
          network_interface_iterator = ec2.network_interfaces.filter(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              NetworkInterfaceIds=[
                  \'string\',
              ],
              NextToken=\'string\',
              MaxResults=123
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``addresses.private-ip-address`` - The private IPv4 addresses associated with the network interface. 
           
          * ``addresses.primary`` - Whether the private IPv4 address is the primary IP address associated with the network interface.  
           
          * ``addresses.association.public-ip`` - The association ID returned when the network interface was associated with the Elastic IP address (IPv4). 
           
          * ``addresses.association.owner-id`` - The owner ID of the addresses associated with the network interface. 
           
          * ``association.association-id`` - The association ID returned when the network interface was associated with an IPv4 address. 
           
          * ``association.allocation-id`` - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface. 
           
          * ``association.ip-owner-id`` - The owner of the Elastic IP address (IPv4) associated with the network interface. 
           
          * ``association.public-ip`` - The address of the Elastic IP address (IPv4) bound to the network interface. 
           
          * ``association.public-dns-name`` - The public DNS name for the network interface (IPv4). 
           
          * ``attachment.attachment-id`` - The ID of the interface attachment. 
           
          * ``attachment.attach.time`` - The time that the network interface was attached to an instance. 
           
          * ``attachment.delete-on-termination`` - Indicates whether the attachment is deleted when an instance is terminated. 
           
          * ``attachment.device-index`` - The device index to which the network interface is attached. 
           
          * ``attachment.instance-id`` - The ID of the instance to which the network interface is attached. 
           
          * ``attachment.instance-owner-id`` - The owner ID of the instance to which the network interface is attached. 
           
          * ``attachment.nat-gateway-id`` - The ID of the NAT gateway to which the network interface is attached. 
           
          * ``attachment.status`` - The status of the attachment (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``availability-zone`` - The Availability Zone of the network interface. 
           
          * ``description`` - The description of the network interface. 
           
          * ``group-id`` - The ID of a security group associated with the network interface. 
           
          * ``group-name`` - The name of a security group associated with the network interface. 
           
          * ``ipv6-addresses.ipv6-address`` - An IPv6 address associated with the network interface. 
           
          * ``mac-address`` - The MAC address of the network interface. 
           
          * ``network-interface-id`` - The ID of the network interface. 
           
          * ``owner-id`` - The AWS account ID of the network interface owner. 
           
          * ``private-ip-address`` - The private IPv4 address or addresses of the network interface. 
           
          * ``private-dns-name`` - The private DNS name of the network interface (IPv4). 
           
          * ``requester-id`` - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on). 
           
          * ``requester-managed`` - Indicates whether the network interface is being managed by an AWS service (for example, AWS Management Console, Auto Scaling, and so on). 
           
          * ``source-desk-check`` - Indicates whether the network interface performs source/destination checking. A value of ``true`` means checking is enabled, and ``false`` means checking is disabled. The value must be ``false`` for the network interface to perform network address translation (NAT) in your VPC.  
           
          * ``status`` - The status of the network interface. If the network interface is not attached to an instance, the status is ``available`` ; if a network interface is attached to an instance the status is ``in-use`` . 
           
          * ``subnet-id`` - The ID of the subnet for the network interface. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-id`` - The ID of the VPC for the network interface. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type NetworkInterfaceIds: list
        :param NetworkInterfaceIds: 
        
          One or more network interface IDs.
        
          Default: Describes all your network interfaces.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The token to retrieve the next page of results.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
        
        :rtype: list(:py:class:`ec2.NetworkInterface`)
        :returns: A list of NetworkInterface resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['NetworkInterface']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNetworkInterfaces>`_
        
        **Request Syntax** 
        ::
        
          network_interface_iterator = ec2.network_interfaces.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.NetworkInterface`)
        :returns: A list of NetworkInterface resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['NetworkInterface']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNetworkInterfaces>`_
        
        **Request Syntax** 
        ::
        
          network_interface_iterator = ec2.network_interfaces.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.NetworkInterface`)
        :returns: A list of NetworkInterface resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class placement_groups(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['PlacementGroup']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribePlacementGroups>`_
        
        **Request Syntax** 
        ::
        
          placement_group_iterator = ec2.placement_groups.all()
          
        :rtype: list(:py:class:`ec2.PlacementGroup`)
        :returns: A list of PlacementGroup resources
        """
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, DryRun: bool = None, GroupNames: List = None) -> List['PlacementGroup']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribePlacementGroups>`_
        
        **Request Syntax** 
        ::
        
          placement_group_iterator = ec2.placement_groups.filter(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              GroupNames=[
                  \'string\',
              ]
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``group-name`` - The name of the placement group. 
           
          * ``state`` - The state of the placement group (``pending`` | ``available`` | ``deleting`` | ``deleted`` ). 
           
          * ``strategy`` - The strategy of the placement group (``cluster`` | ``spread`` ). 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type GroupNames: list
        :param GroupNames: 
        
          One or more placement group names.
        
          Default: Describes all your placement groups, or only those otherwise specified.
        
          - *(string) --* 
        
        :rtype: list(:py:class:`ec2.PlacementGroup`)
        :returns: A list of PlacementGroup resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['PlacementGroup']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribePlacementGroups>`_
        
        **Request Syntax** 
        ::
        
          placement_group_iterator = ec2.placement_groups.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.PlacementGroup`)
        :returns: A list of PlacementGroup resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['PlacementGroup']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribePlacementGroups>`_
        
        **Request Syntax** 
        ::
        
          placement_group_iterator = ec2.placement_groups.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.PlacementGroup`)
        :returns: A list of PlacementGroup resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class route_tables(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['RouteTable']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeRouteTables>`_
        
        **Request Syntax** 
        ::
        
          route_table_iterator = ec2.route_tables.all()
          
        :rtype: list(:py:class:`ec2.RouteTable`)
        :returns: A list of RouteTable resources
        """
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, DryRun: bool = None, RouteTableIds: List = None, NextToken: str = None, MaxResults: int = None) -> List['RouteTable']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeRouteTables>`_
        
        **Request Syntax** 
        ::
        
          route_table_iterator = ec2.route_tables.filter(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              RouteTableIds=[
                  \'string\',
              ],
              NextToken=\'string\',
              MaxResults=123
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``association.route-table-association-id`` - The ID of an association ID for the route table. 
           
          * ``association.route-table-id`` - The ID of the route table involved in the association. 
           
          * ``association.subnet-id`` - The ID of the subnet involved in the association. 
           
          * ``association.main`` - Indicates whether the route table is the main route table for the VPC (``true`` | ``false`` ). Route tables that do not have an association ID are not returned in the response. 
           
          * ``route-table-id`` - The ID of the route table. 
           
          * ``route.destination-cidr-block`` - The IPv4 CIDR range specified in a route in the table. 
           
          * ``route.destination-ipv6-cidr-block`` - The IPv6 CIDR range specified in a route in the route table. 
           
          * ``route.destination-prefix-list-id`` - The ID (prefix) of the AWS service specified in a route in the table. 
           
          * ``route.egress-only-internet-gateway-id`` - The ID of an egress-only Internet gateway specified in a route in the route table. 
           
          * ``route.gateway-id`` - The ID of a gateway specified in a route in the table. 
           
          * ``route.instance-id`` - The ID of an instance specified in a route in the table. 
           
          * ``route.nat-gateway-id`` - The ID of a NAT gateway. 
           
          * ``route.origin`` - Describes how the route was created. ``CreateRouteTable`` indicates that the route was automatically created when the route table was created; ``CreateRoute`` indicates that the route was manually added to the route table; ``EnableVgwRoutePropagation`` indicates that the route was propagated by route propagation. 
           
          * ``route.state`` - The state of a route in the route table (``active`` | ``blackhole`` ). The blackhole state indicates that the route\'s target isn\'t available (for example, the specified gateway isn\'t attached to the VPC, the specified NAT instance has been terminated, and so on). 
           
          * ``route.vpc-peering-connection-id`` - The ID of a VPC peering connection specified in a route in the table. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-id`` - The ID of the VPC for the route table. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type RouteTableIds: list
        :param RouteTableIds: 
        
          One or more route table IDs.
        
          Default: Describes all your route tables.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The token to retrieve the next page of results.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned **NextToken** value. This value can be between 5 and 100.
        
        :rtype: list(:py:class:`ec2.RouteTable`)
        :returns: A list of RouteTable resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['RouteTable']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeRouteTables>`_
        
        **Request Syntax** 
        ::
        
          route_table_iterator = ec2.route_tables.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.RouteTable`)
        :returns: A list of RouteTable resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['RouteTable']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeRouteTables>`_
        
        **Request Syntax** 
        ::
        
          route_table_iterator = ec2.route_tables.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.RouteTable`)
        :returns: A list of RouteTable resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class security_groups(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['SecurityGroup']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSecurityGroups>`_
        
        **Request Syntax** 
        ::
        
          security_group_iterator = ec2.security_groups.all()
          
        :rtype: list(:py:class:`ec2.SecurityGroup`)
        :returns: A list of SecurityGroup resources
        """
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, GroupIds: List = None, GroupNames: List = None, DryRun: bool = None, NextToken: str = None, MaxResults: int = None) -> List['SecurityGroup']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSecurityGroups>`_
        
        **Request Syntax** 
        ::
        
          security_group_iterator = ec2.security_groups.filter(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              GroupIds=[
                  \'string\',
              ],
              GroupNames=[
                  \'string\',
              ],
              DryRun=True|False,
              NextToken=\'string\',
              MaxResults=123
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters. If using multiple filters for rules, the results include security groups for which any combination of rules - not necessarily a single rule - match all filters.
        
          * ``description`` - The description of the security group. 
           
          * ``egress.ip-permission.cidr`` - An IPv4 CIDR block for an outbound security group rule. 
           
          * ``egress.ip-permission.from-port`` - For an outbound rule, the start of port range for the TCP and UDP protocols, or an ICMP type number. 
           
          * ``egress.ip-permission.group-id`` - The ID of a security group that has been referenced in an outbound security group rule. 
           
          * ``egress.ip-permission.group-name`` - The name of a security group that has been referenced in an outbound security group rule. 
           
          * ``egress.ip-permission.ipv6-cidr`` - An IPv6 CIDR block for an outbound security group rule. 
           
          * ``egress.ip-permission.prefix-list-id`` - The ID (prefix) of the AWS service to which a security group rule allows outbound access. 
           
          * ``egress.ip-permission.protocol`` - The IP protocol for an outbound security group rule (``tcp`` | ``udp`` | ``icmp`` or a protocol number). 
           
          * ``egress.ip-permission.to-port`` - For an outbound rule, the end of port range for the TCP and UDP protocols, or an ICMP code. 
           
          * ``egress.ip-permission.user-id`` - The ID of an AWS account that has been referenced in an outbound security group rule. 
           
          * ``group-id`` - The ID of the security group.  
           
          * ``group-name`` - The name of the security group. 
           
          * ``ip-permission.cidr`` - An IPv4 CIDR block for an inbound security group rule. 
           
          * ``ip-permission.from-port`` - For an inbound rule, the start of port range for the TCP and UDP protocols, or an ICMP type number. 
           
          * ``ip-permission.group-id`` - The ID of a security group that has been referenced in an inbound security group rule. 
           
          * ``ip-permission.group-name`` - The name of a security group that has been referenced in an inbound security group rule. 
           
          * ``ip-permission.ipv6-cidr`` - An IPv6 CIDR block for an inbound security group rule. 
           
          * ``ip-permission.prefix-list-id`` - The ID (prefix) of the AWS service from which a security group rule allows inbound access. 
           
          * ``ip-permission.protocol`` - The IP protocol for an inbound security group rule (``tcp`` | ``udp`` | ``icmp`` or a protocol number). 
           
          * ``ip-permission.to-port`` - For an inbound rule, the end of port range for the TCP and UDP protocols, or an ICMP code. 
           
          * ``ip-permission.user-id`` - The ID of an AWS account that has been referenced in an inbound security group rule. 
           
          * ``owner-id`` - The AWS account ID of the owner of the security group. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-id`` - The ID of the VPC specified when the security group was created. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type GroupIds: list
        :param GroupIds: 
        
          One or more security group IDs. Required for security groups in a nondefault VPC.
        
          Default: Describes all your security groups.
        
          - *(string) --* 
        
        :type GroupNames: list
        :param GroupNames: 
        
          [EC2-Classic and default VPC only] One or more security group names. You can specify either the security group name or the security group ID. For security groups in a nondefault VPC, use the ``group-name`` filter to describe security groups by name.
        
          Default: Describes all your security groups.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type NextToken: string
        :param NextToken: 
        
          The token to request the next page of results.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another request with the returned ``NextToken`` value. This value can be between 5 and 1000. If this parameter is not specified, then all results are returned.
        
        :rtype: list(:py:class:`ec2.SecurityGroup`)
        :returns: A list of SecurityGroup resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['SecurityGroup']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSecurityGroups>`_
        
        **Request Syntax** 
        ::
        
          security_group_iterator = ec2.security_groups.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.SecurityGroup`)
        :returns: A list of SecurityGroup resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['SecurityGroup']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSecurityGroups>`_
        
        **Request Syntax** 
        ::
        
          security_group_iterator = ec2.security_groups.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.SecurityGroup`)
        :returns: A list of SecurityGroup resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class snapshots(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Snapshot']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSnapshots>`_
        
        **Request Syntax** 
        ::
        
          snapshot_iterator = ec2.snapshots.all()
          
        :rtype: list(:py:class:`ec2.Snapshot`)
        :returns: A list of Snapshot resources
        """
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, MaxResults: int = None, NextToken: str = None, OwnerIds: List = None, RestorableByUserIds: List = None, SnapshotIds: List = None, DryRun: bool = None) -> List['Snapshot']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSnapshots>`_
        
        **Request Syntax** 
        ::
        
          snapshot_iterator = ec2.snapshots.filter(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\',
              OwnerIds=[
                  \'string\',
              ],
              RestorableByUserIds=[
                  \'string\',
              ],
              SnapshotIds=[
                  \'string\',
              ],
              DryRun=True|False
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``description`` - A description of the snapshot. 
           
          * ``owner-alias`` - Value from an Amazon-maintained list (``amazon`` | ``aws-marketplace`` | ``microsoft`` ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM console. 
           
          * ``owner-id`` - The ID of the AWS account that owns the snapshot. 
           
          * ``progress`` - The progress of the snapshot, as a percentage (for example, 80%). 
           
          * ``snapshot-id`` - The snapshot ID. 
           
          * ``start-time`` - The time stamp when the snapshot was initiated. 
           
          * ``status`` - The status of the snapshot (``pending`` | ``completed`` | ``error`` ). 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``volume-id`` - The ID of the volume the snapshot is for. 
           
          * ``volume-size`` - The size of the volume, in GiB. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of snapshot results returned by ``DescribeSnapshots`` in paginated output. When this parameter is used, ``DescribeSnapshots`` only returns ``MaxResults`` results in a single page along with a ``NextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeSnapshots`` request with the returned ``NextToken`` value. This value can be between 5 and 1000; if ``MaxResults`` is given a value larger than 1000, only 1000 results are returned. If this parameter is not used, then ``DescribeSnapshots`` returns all results. You cannot specify this parameter and the snapshot IDs parameter in the same request.
        
        :type NextToken: string
        :param NextToken: 
        
          The ``NextToken`` value returned from a previous paginated ``DescribeSnapshots`` request where ``MaxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``NextToken`` value. This value is ``null`` when there are no more results to return.
        
        :type OwnerIds: list
        :param OwnerIds: 
        
          Returns the snapshots owned by the specified owner. Multiple owners can be specified.
        
          - *(string) --* 
        
        :type RestorableByUserIds: list
        :param RestorableByUserIds: 
        
          One or more AWS accounts IDs that can create volumes from the snapshot.
        
          - *(string) --* 
        
        :type SnapshotIds: list
        :param SnapshotIds: 
        
          One or more snapshot IDs.
        
          Default: Describes snapshots for which you have launch permissions.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: list(:py:class:`ec2.Snapshot`)
        :returns: A list of Snapshot resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Snapshot']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSnapshots>`_
        
        **Request Syntax** 
        ::
        
          snapshot_iterator = ec2.snapshots.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.Snapshot`)
        :returns: A list of Snapshot resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Snapshot']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSnapshots>`_
        
        **Request Syntax** 
        ::
        
          snapshot_iterator = ec2.snapshots.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.Snapshot`)
        :returns: A list of Snapshot resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class subnets(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Subnet']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSubnets>`_
        
        **Request Syntax** 
        ::
        
          subnet_iterator = ec2.subnets.all()
          
        :rtype: list(:py:class:`ec2.Subnet`)
        :returns: A list of Subnet resources
        """
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, SubnetIds: List = None, DryRun: bool = None) -> List['Subnet']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSubnets>`_
        
        **Request Syntax** 
        ::
        
          subnet_iterator = ec2.subnets.filter(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              SubnetIds=[
                  \'string\',
              ],
              DryRun=True|False
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``availabilityZone`` - The Availability Zone for the subnet. You can also use ``availability-zone`` as the filter name. 
           
          * ``available-ip-address-count`` - The number of IPv4 addresses in the subnet that are available. 
           
          * ``cidrBlock`` - The IPv4 CIDR block of the subnet. The CIDR block you specify must exactly match the subnet\'s CIDR block for information to be returned for the subnet. You can also use ``cidr`` or ``cidr-block`` as the filter names. 
           
          * ``defaultForAz`` - Indicates whether this is the default subnet for the Availability Zone. You can also use ``default-for-az`` as the filter name. 
           
          * ``ipv6-cidr-block-association.ipv6-cidr-block`` - An IPv6 CIDR block associated with the subnet. 
           
          * ``ipv6-cidr-block-association.association-id`` - An association ID for an IPv6 CIDR block associated with the subnet. 
           
          * ``ipv6-cidr-block-association.state`` - The state of an IPv6 CIDR block associated with the subnet. 
           
          * ``state`` - The state of the subnet (``pending`` | ``available`` ). 
           
          * ``subnet-id`` - The ID of the subnet. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-id`` - The ID of the VPC for the subnet. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type SubnetIds: list
        :param SubnetIds: 
        
          One or more subnet IDs.
        
          Default: Describes all your subnets.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: list(:py:class:`ec2.Subnet`)
        :returns: A list of Subnet resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Subnet']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSubnets>`_
        
        **Request Syntax** 
        ::
        
          subnet_iterator = ec2.subnets.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.Subnet`)
        :returns: A list of Subnet resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Subnet']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSubnets>`_
        
        **Request Syntax** 
        ::
        
          subnet_iterator = ec2.subnets.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.Subnet`)
        :returns: A list of Subnet resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class volumes(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Volume']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumes>`_
        
        **Request Syntax** 
        ::
        
          volume_iterator = ec2.volumes.all()
          
        :rtype: list(:py:class:`ec2.Volume`)
        :returns: A list of Volume resources
        """
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None) -> List['Volume']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumes>`_
        
        **Request Syntax** 
        ::
        
          volume_iterator = ec2.volumes.filter(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              VolumeIds=[
                  \'string\',
              ],
              DryRun=True|False,
              MaxResults=123,
              NextToken=\'string\'
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``attachment.attach-time`` - The time stamp when the attachment initiated. 
           
          * ``attachment.delete-on-termination`` - Whether the volume is deleted on instance termination. 
           
          * ``attachment.device`` - The device name specified in the block device mapping (for example, ``/dev/sda1`` ). 
           
          * ``attachment.instance-id`` - The ID of the instance the volume is attached to. 
           
          * ``attachment.status`` - The attachment state (``attaching`` | ``attached`` | ``detaching`` ). 
           
          * ``availability-zone`` - The Availability Zone in which the volume was created. 
           
          * ``create-time`` - The time stamp when the volume was created. 
           
          * ``encrypted`` - The encryption status of the volume. 
           
          * ``size`` - The size of the volume, in GiB. 
           
          * ``snapshot-id`` - The snapshot from which the volume was created. 
           
          * ``status`` - The status of the volume (``creating`` | ``available`` | ``in-use`` | ``deleting`` | ``deleted`` | ``error`` ). 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``volume-id`` - The volume ID. 
           
          * ``volume-type`` - The Amazon EBS volume type. This can be ``gp2`` for General Purpose SSD, ``io1`` for Provisioned IOPS SSD, ``st1`` for Throughput Optimized HDD, ``sc1`` for Cold HDD, or ``standard`` for Magnetic volumes. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type VolumeIds: list
        :param VolumeIds: 
        
          One or more volume IDs.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of volume results returned by ``DescribeVolumes`` in paginated output. When this parameter is used, ``DescribeVolumes`` only returns ``MaxResults`` results in a single page along with a ``NextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeVolumes`` request with the returned ``NextToken`` value. This value can be between 5 and 500; if ``MaxResults`` is given a value larger than 500, only 500 results are returned. If this parameter is not used, then ``DescribeVolumes`` returns all results. You cannot specify this parameter and the volume IDs parameter in the same request.
        
        :type NextToken: string
        :param NextToken: 
        
          The ``NextToken`` value returned from a previous paginated ``DescribeVolumes`` request where ``MaxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``NextToken`` value. This value is ``null`` when there are no more results to return.
        
        :rtype: list(:py:class:`ec2.Volume`)
        :returns: A list of Volume resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Volume']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumes>`_
        
        **Request Syntax** 
        ::
        
          volume_iterator = ec2.volumes.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.Volume`)
        :returns: A list of Volume resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Volume']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumes>`_
        
        **Request Syntax** 
        ::
        
          volume_iterator = ec2.volumes.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.Volume`)
        :returns: A list of Volume resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class vpc_addresses(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['VpcAddress']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeAddresses>`_
        
        **Request Syntax** 
        ::
        
          vpc_address_iterator = ec2.vpc_addresses.all()
          
        :rtype: list(:py:class:`ec2.VpcAddress`)
        :returns: A list of VpcAddress resources
        """
        pass

    
    @classmethod
    def filter(cls, PublicIps: List = None, AllocationIds: List = None, DryRun: bool = None) -> List['VpcAddress']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeAddresses>`_
        
        **Request Syntax** 
        ::
        
          vpc_address_iterator = ec2.vpc_addresses.filter(
              PublicIps=[
                  \'string\',
              ],
              AllocationIds=[
                  \'string\',
              ],
              DryRun=True|False
          )
        :type PublicIps: list
        :param PublicIps: 
        
          [EC2-Classic] One or more Elastic IP addresses.
        
          Default: Describes all your Elastic IP addresses.
        
          - *(string) --* 
        
        :type AllocationIds: list
        :param AllocationIds: 
        
          [EC2-VPC] One or more allocation IDs.
        
          Default: Describes all your Elastic IP addresses.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: list(:py:class:`ec2.VpcAddress`)
        :returns: A list of VpcAddress resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['VpcAddress']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeAddresses>`_
        
        **Request Syntax** 
        ::
        
          vpc_address_iterator = ec2.vpc_addresses.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.VpcAddress`)
        :returns: A list of VpcAddress resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['VpcAddress']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeAddresses>`_
        
        **Request Syntax** 
        ::
        
          vpc_address_iterator = ec2.vpc_addresses.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.VpcAddress`)
        :returns: A list of VpcAddress resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class vpc_peering_connections(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['VpcPeeringConnection']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcPeeringConnections>`_
        
        **Request Syntax** 
        ::
        
          vpc_peering_connection_iterator = ec2.vpc_peering_connections.all()
          
        :rtype: list(:py:class:`ec2.VpcPeeringConnection`)
        :returns: A list of VpcPeeringConnection resources
        """
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None) -> List['VpcPeeringConnection']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcPeeringConnections>`_
        
        **Request Syntax** 
        ::
        
          vpc_peering_connection_iterator = ec2.vpc_peering_connections.filter(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              VpcPeeringConnectionIds=[
                  \'string\',
              ]
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``accepter-vpc-info.cidr-block`` - The IPv4 CIDR block of the accepter VPC. 
           
          * ``accepter-vpc-info.owner-id`` - The AWS account ID of the owner of the accepter VPC. 
           
          * ``accepter-vpc-info.vpc-id`` - The ID of the accepter VPC. 
           
          * ``expiration-time`` - The expiration date and time for the VPC peering connection. 
           
          * ``requester-vpc-info.cidr-block`` - The IPv4 CIDR block of the requester\'s VPC. 
           
          * ``requester-vpc-info.owner-id`` - The AWS account ID of the owner of the requester VPC. 
           
          * ``requester-vpc-info.vpc-id`` - The ID of the requester VPC. 
           
          * ``status-code`` - The status of the VPC peering connection (``pending-acceptance`` | ``failed`` | ``expired`` | ``provisioning`` | ``active`` | ``deleting`` | ``deleted`` | ``rejected`` ). 
           
          * ``status-message`` - A message that provides more information about the status of the VPC peering connection, if applicable. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-peering-connection-id`` - The ID of the VPC peering connection. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type VpcPeeringConnectionIds: list
        :param VpcPeeringConnectionIds: 
        
          One or more VPC peering connection IDs.
        
          Default: Describes all your VPC peering connections.
        
          - *(string) --* 
        
        :rtype: list(:py:class:`ec2.VpcPeeringConnection`)
        :returns: A list of VpcPeeringConnection resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['VpcPeeringConnection']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcPeeringConnections>`_
        
        **Request Syntax** 
        ::
        
          vpc_peering_connection_iterator = ec2.vpc_peering_connections.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.VpcPeeringConnection`)
        :returns: A list of VpcPeeringConnection resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['VpcPeeringConnection']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcPeeringConnections>`_
        
        **Request Syntax** 
        ::
        
          vpc_peering_connection_iterator = ec2.vpc_peering_connections.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.VpcPeeringConnection`)
        :returns: A list of VpcPeeringConnection resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass


class vpcs(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Vpc']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcs>`_
        
        **Request Syntax** 
        ::
        
          vpc_iterator = ec2.vpcs.all()
          
        :rtype: list(:py:class:`ec2.Vpc`)
        :returns: A list of Vpc resources
        """
        pass

    
    @classmethod
    def filter(cls, Filters: List = None, VpcIds: List = None, DryRun: bool = None) -> List['Vpc']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcs>`_
        
        **Request Syntax** 
        ::
        
          vpc_iterator = ec2.vpcs.filter(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              VpcIds=[
                  \'string\',
              ],
              DryRun=True|False
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``cidr`` - The primary IPv4 CIDR block of the VPC. The CIDR block you specify must exactly match the VPC\'s CIDR block for information to be returned for the VPC. Must contain the slash followed by one or two digits (for example, ``/28`` ). 
           
          * ``cidr-block-association.cidr-block`` - An IPv4 CIDR block associated with the VPC. 
           
          * ``cidr-block-association.association-id`` - The association ID for an IPv4 CIDR block associated with the VPC. 
           
          * ``cidr-block-association.state`` - The state of an IPv4 CIDR block associated with the VPC. 
           
          * ``dhcp-options-id`` - The ID of a set of DHCP options. 
           
          * ``ipv6-cidr-block-association.ipv6-cidr-block`` - An IPv6 CIDR block associated with the VPC. 
           
          * ``ipv6-cidr-block-association.association-id`` - The association ID for an IPv6 CIDR block associated with the VPC. 
           
          * ``ipv6-cidr-block-association.state`` - The state of an IPv6 CIDR block associated with the VPC. 
           
          * ``isDefault`` - Indicates whether the VPC is the default VPC. 
           
          * ``state`` - The state of the VPC (``pending`` | ``available`` ). 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-id`` - The ID of the VPC. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type VpcIds: list
        :param VpcIds: 
        
          One or more VPC IDs.
        
          Default: Describes all your VPCs.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :rtype: list(:py:class:`ec2.Vpc`)
        :returns: A list of Vpc resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls, count: int = None) -> List['Vpc']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcs>`_
        
        **Request Syntax** 
        ::
        
          vpc_iterator = ec2.vpcs.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`ec2.Vpc`)
        :returns: A list of Vpc resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Vpc']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcs>`_
        
        **Request Syntax** 
        ::
        
          vpc_iterator = ec2.vpcs.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`ec2.Vpc`)
        :returns: A list of Vpc resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass
