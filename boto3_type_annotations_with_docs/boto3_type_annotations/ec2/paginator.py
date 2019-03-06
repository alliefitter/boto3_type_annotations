from typing import List
from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class DescribeByoipCidrs(Paginator):
    def paginate(self, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_byoip_cidrs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeByoipCidrs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ByoipCidrs': [
                    {
                        'Cidr': 'string',
                        'Description': 'string',
                        'StatusMessage': 'string',
                        'State': 'advertised'|'deprovisioned'|'failed-deprovision'|'failed-provision'|'pending-deprovision'|'pending-provision'|'provisioned'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ByoipCidrs** *(list) --* 
              Information about your address ranges.
              - *(dict) --* 
                Information about an address range that is provisioned for use with your AWS resources through bring your own IP addresses (BYOIP).
                - **Cidr** *(string) --* 
                  The public IPv4 address range, in CIDR notation.
                - **Description** *(string) --* 
                  The description of the address range.
                - **StatusMessage** *(string) --* 
                  Upon success, contains the ID of the address pool. Otherwise, contains an error message.
                - **State** *(string) --* 
                  The state of the address pool.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeCapacityReservations(Paginator):
    def paginate(self, CapacityReservationIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_capacity_reservations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeCapacityReservations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              CapacityReservationIds=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'CapacityReservations': [
                    {
                        'CapacityReservationId': 'string',
                        'InstanceType': 'string',
                        'InstancePlatform': 'Linux/UNIX'|'Red Hat Enterprise Linux'|'SUSE Linux'|'Windows'|'Windows with SQL Server'|'Windows with SQL Server Enterprise'|'Windows with SQL Server Standard'|'Windows with SQL Server Web'|'Linux with SQL Server Standard'|'Linux with SQL Server Web'|'Linux with SQL Server Enterprise',
                        'AvailabilityZone': 'string',
                        'Tenancy': 'default'|'dedicated',
                        'TotalInstanceCount': 123,
                        'AvailableInstanceCount': 123,
                        'EbsOptimized': True|False,
                        'EphemeralStorage': True|False,
                        'State': 'active'|'expired'|'cancelled'|'pending'|'failed',
                        'EndDate': datetime(2015, 1, 1),
                        'EndDateType': 'unlimited'|'limited',
                        'InstanceMatchCriteria': 'open'|'targeted',
                        'CreateDate': datetime(2015, 1, 1),
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CapacityReservations** *(list) --* 
              Information about the Capacity Reservations.
              - *(dict) --* 
                Describes a Capacity Reservation.
                - **CapacityReservationId** *(string) --* 
                  The ID of the Capacity Reservation.
                - **InstanceType** *(string) --* 
                  The type of instance for which the Capacity Reservation reserves capacity.
                - **InstancePlatform** *(string) --* 
                  The type of operating system for which the Capacity Reservation reserves capacity.
                - **AvailabilityZone** *(string) --* 
                  The Availability Zone in which the capacity is reserved.
                - **Tenancy** *(string) --* 
                  Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings:
                  * ``default`` - The Capacity Reservation is created on hardware that is shared with other AWS accounts. 
                  * ``dedicated`` - The Capacity Reservation is created on single-tenant hardware that is dedicated to a single AWS account. 
                - **TotalInstanceCount** *(integer) --* 
                  The number of instances for which the Capacity Reservation reserves capacity.
                - **AvailableInstanceCount** *(integer) --* 
                  The remaining capacity. Indicates the number of instances that can be launched in the Capacity Reservation.
                - **EbsOptimized** *(boolean) --* 
                  Indicates whether the Capacity Reservation supports EBS-optimized instances. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS- optimized instance.
                - **EphemeralStorage** *(boolean) --* 
                  Indicates whether the Capacity Reservation supports instances with temporary, block-level storage.
                - **State** *(string) --* 
                  The current state of the Capacity Reservation. A Capacity Reservation can be in one of the following states:
                  * ``active`` - The Capacity Reservation is active and the capacity is available for your use. 
                  * ``cancelled`` - The Capacity Reservation expired automatically at the date and time specified in your request. The reserved capacity is no longer available for your use. 
                  * ``expired`` - The Capacity Reservation was manually cancelled. The reserved capacity is no longer available for your use. 
                  * ``pending`` - The Capacity Reservation request was successful but the capacity provisioning is still pending. 
                  * ``failed`` - The Capacity Reservation request has failed. A request might fail due to invalid request parameters, capacity constraints, or instance limit constraints. Failed requests are retained for 60 minutes. 
                - **EndDate** *(datetime) --* 
                  The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to ``expired`` when it reaches its end date and time.
                - **EndDateType** *(string) --* 
                  Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:
                  * ``unlimited`` - The Capacity Reservation remains active until you explicitly cancel it. 
                  * ``limited`` - The Capacity Reservation expires automatically at a specified date and time. 
                - **InstanceMatchCriteria** *(string) --* 
                  Indicates the type of instance launches that the Capacity Reservation accepts. The options include:
                  * ``open`` - The Capacity Reservation accepts all instances that have matching attributes (instance type, platform, and Availability Zone). Instances that have matching attributes launch into the Capacity Reservation automatically without specifying any additional parameters. 
                  * ``targeted`` - The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, and Availability Zone), and explicitly target the Capacity Reservation. This ensures that only permitted instances can use the reserved capacity.  
                - **CreateDate** *(datetime) --* 
                  The date and time at which the Capacity Reservation was created.
                - **Tags** *(list) --* 
                  Any tags assigned to the Capacity Reservation.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        :type CapacityReservationIds: list
        :param CapacityReservationIds:
          The ID of the Capacity Reservation.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeClassicLinkInstances(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, InstanceIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_classic_link_instances`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeClassicLinkInstances>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              InstanceIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Instances': [
                    {
                        'Groups': [
                            {
                                'GroupName': 'string',
                                'GroupId': 'string'
                            },
                        ],
                        'InstanceId': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'VpcId': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Instances** *(list) --* 
              Information about one or more linked EC2-Classic instances.
              - *(dict) --* 
                Describes a linked EC2-Classic instance.
                - **Groups** *(list) --* 
                  A list of security groups.
                  - *(dict) --* 
                    Describes a security group.
                    - **GroupName** *(string) --* 
                      The name of the security group.
                    - **GroupId** *(string) --* 
                      The ID of the security group.
                - **InstanceId** *(string) --* 
                  The ID of the instance.
                - **Tags** *(list) --* 
                  Any tags assigned to the instance.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
                - **VpcId** *(string) --* 
                  The ID of the VPC.
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``group-id`` - The ID of a VPC security group that\'s associated with the instance.
          * ``instance-id`` - The ID of the instance.
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value.
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
          * ``vpc-id`` - The ID of the VPC to which the instance is linked.  ``vpc-id`` - The ID of the VPC that the instance is linked to.
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
        :type InstanceIds: list
        :param InstanceIds:
          One or more instance IDs. Must be instances linked to a VPC through ClassicLink.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeClientVpnAuthorizationRules(Paginator):
    def paginate(self, ClientVpnEndpointId: str, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_client_vpn_authorization_rules`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeClientVpnAuthorizationRules>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClientVpnEndpointId='string',
              DryRun=True|False,
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'AuthorizationRules': [
                    {
                        'ClientVpnEndpointId': 'string',
                        'Description': 'string',
                        'GroupId': 'string',
                        'AccessAll': True|False,
                        'DestinationCidr': 'string',
                        'Status': {
                            'Code': 'authorizing'|'active'|'failed'|'revoking',
                            'Message': 'string'
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AuthorizationRules** *(list) --* 
              Information about the authorization rules.
              - *(dict) --* 
        
        **Information about an authorization rule.**
                - **ClientVpnEndpointId** *(string) --* 
                  The ID of the Client VPN endpoint with which the authorization rule is associated.
                - **Description** *(string) --* 
                  A brief description of the authorization rule.
                - **GroupId** *(string) --* 
                  The ID of the Active Directory group to which the authorization rule grants access.
                - **AccessAll** *(boolean) --* 
                  Indicates whether the authorization rule grants access to all clients.
                - **DestinationCidr** *(string) --* 
                  The IPv4 address range, in CIDR notation, of the network to which the authorization rule applies.
                - **Status** *(dict) --* 
                  The current state of the authorization rule.
                  - **Code** *(string) --* 
                    The state of the authorization rule.
                  - **Message** *(string) --* 
                    A message about the status of the authorization rule, if applicable.
        :type ClientVpnEndpointId: string
        :param ClientVpnEndpointId: **[REQUIRED]**
          The ID of the Client VPN endpoint.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type Filters: list
        :param Filters:
          One or more filters. Filter names and values are case-sensitive.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeClientVpnConnections(Paginator):
    def paginate(self, ClientVpnEndpointId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_client_vpn_connections`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeClientVpnConnections>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClientVpnEndpointId='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Connections': [
                    {
                        'ClientVpnEndpointId': 'string',
                        'Timestamp': 'string',
                        'ConnectionId': 'string',
                        'Username': 'string',
                        'ConnectionEstablishedTime': 'string',
                        'IngressBytes': 'string',
                        'EgressBytes': 'string',
                        'IngressPackets': 'string',
                        'EgressPackets': 'string',
                        'ClientIp': 'string',
                        'CommonName': 'string',
                        'Status': {
                            'Code': 'active'|'failed-to-terminate'|'terminating'|'terminated',
                            'Message': 'string'
                        },
                        'ConnectionEndTime': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Connections** *(list) --* 
              Information about the active and terminated client connections.
              - *(dict) --* 
                Describes a client connection.
                - **ClientVpnEndpointId** *(string) --* 
                  The ID of the Client VPN endpoint to which the client is connected.
                - **Timestamp** *(string) --* 
        
        **The current date and time.**
                - **ConnectionId** *(string) --* 
                  The ID of the client connection.
                - **Username** *(string) --* 
                  The username of the client who established the client connection. This information is only provided if Active Directory client authentication is used.
                - **ConnectionEstablishedTime** *(string) --* 
                  The date and time the client connection was established.
                - **IngressBytes** *(string) --* 
                  The number of bytes sent by the client.
                - **EgressBytes** *(string) --* 
                  The number of bytes received by the client.
                - **IngressPackets** *(string) --* 
                  The number of packets sent by the client.
                - **EgressPackets** *(string) --* 
                  The number of packets received by the client.
                - **ClientIp** *(string) --* 
                  The IP address of the client.
                - **CommonName** *(string) --* 
        
        **The common name associated with the client. This is either the name of the client certificate, or the Active Directory user name.**
                - **Status** *(dict) --* 
                  The current state of the client connection.
                  - **Code** *(string) --* 
                    The state of the client connection.
                  - **Message** *(string) --* 
                    A message about the status of the client connection, if applicable.
                - **ConnectionEndTime** *(string) --* 
                  The date and time the client connection was terminated.
        :type ClientVpnEndpointId: string
        :param ClientVpnEndpointId: **[REQUIRED]**
          The ID of the Client VPN endpoint.
        :type Filters: list
        :param Filters:
          One or more filters. Filter names and values are case-sensitive.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeClientVpnEndpoints(Paginator):
    def paginate(self, ClientVpnEndpointIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_client_vpn_endpoints`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeClientVpnEndpoints>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClientVpnEndpointIds=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ClientVpnEndpoints': [
                    {
                        'ClientVpnEndpointId': 'string',
                        'Description': 'string',
                        'Status': {
                            'Code': 'pending-associate'|'available'|'deleting'|'deleted',
                            'Message': 'string'
                        },
                        'CreationTime': 'string',
                        'DeletionTime': 'string',
                        'DnsName': 'string',
                        'ClientCidrBlock': 'string',
                        'DnsServers': [
                            'string',
                        ],
                        'SplitTunnel': True|False,
                        'VpnProtocol': 'openvpn',
                        'TransportProtocol': 'tcp'|'udp',
                        'AssociatedTargetNetworks': [
                            {
                                'NetworkId': 'string',
                                'NetworkType': 'vpc'
                            },
                        ],
                        'ServerCertificateArn': 'string',
                        'AuthenticationOptions': [
                            {
                                'Type': 'certificate-authentication'|'directory-service-authentication',
                                'ActiveDirectory': {
                                    'DirectoryId': 'string'
                                },
                                'MutualAuthentication': {
                                    'ClientRootCertificateChain': 'string'
                                }
                            },
                        ],
                        'ConnectionLogOptions': {
                            'Enabled': True|False,
                            'CloudwatchLogGroup': 'string',
                            'CloudwatchLogStream': 'string'
                        },
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ClientVpnEndpoints** *(list) --* 
              Information about the Client VPN endpoints.
              - *(dict) --* 
                Describes a Client VPN endpoint.
                - **ClientVpnEndpointId** *(string) --* 
                  The ID of the Client VPN endpoint.
                - **Description** *(string) --* 
                  A brief description of the endpoint.
                - **Status** *(dict) --* 
                  The current state of the Client VPN endpoint.
                  - **Code** *(string) --* 
                    The state of the Client VPN endpoint. Possible states include:
                    * ``pending-associate`` - The Client VPN endpoint has been created but no target networks have been associated. The Client VPN endpoint cannot accept connections. 
                    * ``available`` - The Client VPN endpoint has been created and a target network has been associated. The Client VPN endpoint can accept connections. 
                    * ``deleting`` - The Client VPN endpoint is being deleted. The Client VPN endpoint cannot accept connections. 
                    * ``deleted`` - The Client VPN endpoint has been deleted. The Client VPN endpoint cannot accept connections. 
                  - **Message** *(string) --* 
                    A message about the status of the Client VPN endpoint.
                - **CreationTime** *(string) --* 
                  The date and time the Client VPN endpoint was created.
                - **DeletionTime** *(string) --* 
                  The date and time the Client VPN endpoint was deleted, if applicable.
                - **DnsName** *(string) --* 
                  The DNS name to be used by clients when connecting to the Client VPN endpoint.
                - **ClientCidrBlock** *(string) --* 
                  The IPv4 address range, in CIDR notation, from which client IP addresses are assigned.
                - **DnsServers** *(list) --* 
                  Information about the DNS servers to be used for DNS resolution. 
                  - *(string) --* 
                - **SplitTunnel** *(boolean) --* 
                  Indicates whether VPN split tunneling is supported.
                - **VpnProtocol** *(string) --* 
                  The protocol used by the VPN session.
                - **TransportProtocol** *(string) --* 
        
        **The transport protocol used by the Client VPN endpoint.**
                - **AssociatedTargetNetworks** *(list) --* 
                  Information about the associated target networks. A target network is a subnet in a VPC.
                  - *(dict) --* 
                    Describes a target network that is associated with a Client VPN endpoint. A target network is a subnet in a VPC.
                    - **NetworkId** *(string) --* 
        
        **The ID of the subnet.**
                    - **NetworkType** *(string) --* 
        
        **The target network type.**
                - **ServerCertificateArn** *(string) --* 
                  The ARN of the server certificate.
                - **AuthenticationOptions** *(list) --* 
                  Information about the authentication method used by the Client VPN endpoint.
                  - *(dict) --* 
                    Describes the authentication methods used by a Client VPN endpoint. Client VPN supports Active Directory and mutual authentication. For more information, see `Authentication <vpn/latest/clientvpn-admin/authentication-authrization.html#client-authentication>`__ in the *AWS Client VPN Admin Guide* .
                    - **Type** *(string) --* 
                      The authentication type used.
                    - **ActiveDirectory** *(dict) --* 
                      Information about the Active Directory, if applicable.
                      - **DirectoryId** *(string) --* 
                        The ID of the Active Directory used for authentication.
                    - **MutualAuthentication** *(dict) --* 
                      Information about the authentication certificates, if applicable.
                      - **ClientRootCertificateChain** *(string) --* 
        
        **The ARN of the client certificate.**
                - **ConnectionLogOptions** *(dict) --* 
                  Information about the client connection logging options for the Client VPN endpoint.
                  - **Enabled** *(boolean) --* 
                    Indicates whether client connection logging is enabled for the Client VPN endpoint.
                  - **CloudwatchLogGroup** *(string) --* 
                    The name of the Amazon CloudWatch Logs log group to which connection logging data is published.
                  - **CloudwatchLogStream** *(string) --* 
                    The name of the Amazon CloudWatch Logs log stream to which connection logging data is published.
                - **Tags** *(list) --* 
                  Any tags assigned to the Client VPN endpoint.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        :type ClientVpnEndpointIds: list
        :param ClientVpnEndpointIds:
          The ID of the Client VPN endpoint.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters. Filter names and values are case-sensitive.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeClientVpnRoutes(Paginator):
    def paginate(self, ClientVpnEndpointId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_client_vpn_routes`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeClientVpnRoutes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClientVpnEndpointId='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Routes': [
                    {
                        'ClientVpnEndpointId': 'string',
                        'DestinationCidr': 'string',
                        'TargetSubnet': 'string',
                        'Type': 'string',
                        'Origin': 'string',
                        'Status': {
                            'Code': 'creating'|'active'|'failed'|'deleting',
                            'Message': 'string'
                        },
                        'Description': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Routes** *(list) --* 
              Information about the Client VPN endpoint routes.
              - *(dict) --* 
        
        **Information about a Client VPN endpoint route.**
                - **ClientVpnEndpointId** *(string) --* 
                  The ID of the Client VPN endpoint with which the route is associated.
                - **DestinationCidr** *(string) --* 
                  The IPv4 address range, in CIDR notation, of the route destination.
                - **TargetSubnet** *(string) --* 
                  The ID of the subnet through which traffic is routed.
                - **Type** *(string) --* 
        
        **The route type.**
                - **Origin** *(string) --* 
                  Indicates how the route was associated with the Client VPN endpoint. ``associate`` indicates that the route was automatically added when the target network was associated with the Client VPN endpoint. ``add-route`` indicates that the route was manually added using the **CreateClientVpnRoute** action.
                - **Status** *(dict) --* 
                  The current state of the route.
                  - **Code** *(string) --* 
                    The state of the Client VPN endpoint route.
                  - **Message** *(string) --* 
                    A message about the status of the Client VPN endpoint route, if applicable.
                - **Description** *(string) --* 
                  A brief description of the route.
        :type ClientVpnEndpointId: string
        :param ClientVpnEndpointId: **[REQUIRED]**
          The ID of the Client VPN endpoint.
        :type Filters: list
        :param Filters:
          One or more filters. Filter names and values are case-sensitive.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeClientVpnTargetNetworks(Paginator):
    def paginate(self, ClientVpnEndpointId: str, AssociationIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_client_vpn_target_networks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeClientVpnTargetNetworks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClientVpnEndpointId='string',
              AssociationIds=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ClientVpnTargetNetworks': [
                    {
                        'AssociationId': 'string',
                        'VpcId': 'string',
                        'TargetNetworkId': 'string',
                        'ClientVpnEndpointId': 'string',
                        'Status': {
                            'Code': 'associating'|'associated'|'association-failed'|'disassociating'|'disassociated',
                            'Message': 'string'
                        },
                        'SecurityGroups': [
                            'string',
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ClientVpnTargetNetworks** *(list) --* 
              Information about the associated target networks.
              - *(dict) --* 
                Describes a target network associated with a Client VPN endpoint.
                - **AssociationId** *(string) --* 
                  The ID of the association.
                - **VpcId** *(string) --* 
                  The ID of the VPC in which the target network (subnet) is located.
                - **TargetNetworkId** *(string) --* 
                  The ID of the subnet specified as the target network.
                - **ClientVpnEndpointId** *(string) --* 
                  The ID of the Client VPN endpoint with which the target network is associated.
                - **Status** *(dict) --* 
                  The current state of the target network association.
                  - **Code** *(string) --* 
                    The state of the target network association.
                  - **Message** *(string) --* 
                    A message about the status of the target network association, if applicable.
                - **SecurityGroups** *(list) --* 
                  The IDs of the security groups applied to the target network association.
                  - *(string) --* 
        :type ClientVpnEndpointId: string
        :param ClientVpnEndpointId: **[REQUIRED]**
          The ID of the Client VPN endpoint.
        :type AssociationIds: list
        :param AssociationIds:
          The IDs of the target network associations.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters. Filter names and values are case-sensitive.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeEgressOnlyInternetGateways(Paginator):
    def paginate(self, DryRun: bool = None, EgressOnlyInternetGatewayIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_egress_only_internet_gateways`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeEgressOnlyInternetGateways>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              EgressOnlyInternetGatewayIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'EgressOnlyInternetGateways': [
                    {
                        'Attachments': [
                            {
                                'State': 'attaching'|'attached'|'detaching'|'detached',
                                'VpcId': 'string'
                            },
                        ],
                        'EgressOnlyInternetGatewayId': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EgressOnlyInternetGateways** *(list) --* 
              Information about the egress-only internet gateways.
              - *(dict) --* 
                Describes an egress-only internet gateway.
                - **Attachments** *(list) --* 
                  Information about the attachment of the egress-only internet gateway.
                  - *(dict) --* 
                    Describes the attachment of a VPC to an internet gateway or an egress-only internet gateway.
                    - **State** *(string) --* 
                      The current state of the attachment. For an internet gateway, the state is ``available`` when attached to a VPC; otherwise, this value is not returned.
                    - **VpcId** *(string) --* 
                      The ID of the VPC.
                - **EgressOnlyInternetGatewayId** *(string) --* 
                  The ID of the egress-only internet gateway.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type EgressOnlyInternetGatewayIds: list
        :param EgressOnlyInternetGatewayIds:
          One or more egress-only internet gateway IDs.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeFleets(Paginator):
    def paginate(self, DryRun: bool = None, FleetIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_fleets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeFleets>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              FleetIds=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Fleets': [
                    {
                        'ActivityStatus': 'error'|'pending-fulfillment'|'pending-termination'|'fulfilled',
                        'CreateTime': datetime(2015, 1, 1),
                        'FleetId': 'string',
                        'FleetState': 'submitted'|'active'|'deleted'|'failed'|'deleted-running'|'deleted-terminating'|'modifying',
                        'ClientToken': 'string',
                        'ExcessCapacityTerminationPolicy': 'no-termination'|'termination',
                        'FulfilledCapacity': 123.0,
                        'FulfilledOnDemandCapacity': 123.0,
                        'LaunchTemplateConfigs': [
                            {
                                'LaunchTemplateSpecification': {
                                    'LaunchTemplateId': 'string',
                                    'LaunchTemplateName': 'string',
                                    'Version': 'string'
                                },
                                'Overrides': [
                                    {
                                        'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'t3.nano'|'t3.micro'|'t3.small'|'t3.medium'|'t3.large'|'t3.xlarge'|'t3.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.12xlarge'|'r5.24xlarge'|'r5.metal'|'r5a.large'|'r5a.xlarge'|'r5a.2xlarge'|'r5a.4xlarge'|'r5a.12xlarge'|'r5a.24xlarge'|'r5d.large'|'r5d.xlarge'|'r5d.2xlarge'|'r5d.4xlarge'|'r5d.12xlarge'|'r5d.24xlarge'|'r5d.metal'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'i3.metal'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'c5d.large'|'c5d.xlarge'|'c5d.2xlarge'|'c5d.4xlarge'|'c5d.9xlarge'|'c5d.18xlarge'|'c5n.large'|'c5n.xlarge'|'c5n.2xlarge'|'c5n.4xlarge'|'c5n.9xlarge'|'c5n.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'g3s.xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'p3dn.24xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.4xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'m5.metal'|'m5a.large'|'m5a.xlarge'|'m5a.2xlarge'|'m5a.4xlarge'|'m5a.12xlarge'|'m5a.24xlarge'|'m5d.large'|'m5d.xlarge'|'m5d.2xlarge'|'m5d.4xlarge'|'m5d.12xlarge'|'m5d.24xlarge'|'m5d.metal'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge'|'z1d.large'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'z1d.metal'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal'|'a1.medium'|'a1.large'|'a1.xlarge'|'a1.2xlarge'|'a1.4xlarge',
                                        'MaxPrice': 'string',
                                        'SubnetId': 'string',
                                        'AvailabilityZone': 'string',
                                        'WeightedCapacity': 123.0,
                                        'Priority': 123.0,
                                        'Placement': {
                                            'GroupName': 'string'
                                        }
                                    },
                                ]
                            },
                        ],
                        'TargetCapacitySpecification': {
                            'TotalTargetCapacity': 123,
                            'OnDemandTargetCapacity': 123,
                            'SpotTargetCapacity': 123,
                            'DefaultTargetCapacityType': 'spot'|'on-demand'
                        },
                        'TerminateInstancesWithExpiration': True|False,
                        'Type': 'request'|'maintain'|'instant',
                        'ValidFrom': datetime(2015, 1, 1),
                        'ValidUntil': datetime(2015, 1, 1),
                        'ReplaceUnhealthyInstances': True|False,
                        'SpotOptions': {
                            'AllocationStrategy': 'lowest-price'|'diversified',
                            'InstanceInterruptionBehavior': 'hibernate'|'stop'|'terminate',
                            'InstancePoolsToUseCount': 123,
                            'SingleInstanceType': True|False,
                            'SingleAvailabilityZone': True|False,
                            'MinTargetCapacity': 123
                        },
                        'OnDemandOptions': {
                            'AllocationStrategy': 'lowest-price'|'prioritized',
                            'SingleInstanceType': True|False,
                            'SingleAvailabilityZone': True|False,
                            'MinTargetCapacity': 123
                        },
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'Errors': [
                            {
                                'LaunchTemplateAndOverrides': {
                                    'LaunchTemplateSpecification': {
                                        'LaunchTemplateId': 'string',
                                        'LaunchTemplateName': 'string',
                                        'Version': 'string'
                                    },
                                    'Overrides': {
                                        'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'t3.nano'|'t3.micro'|'t3.small'|'t3.medium'|'t3.large'|'t3.xlarge'|'t3.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.12xlarge'|'r5.24xlarge'|'r5.metal'|'r5a.large'|'r5a.xlarge'|'r5a.2xlarge'|'r5a.4xlarge'|'r5a.12xlarge'|'r5a.24xlarge'|'r5d.large'|'r5d.xlarge'|'r5d.2xlarge'|'r5d.4xlarge'|'r5d.12xlarge'|'r5d.24xlarge'|'r5d.metal'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'i3.metal'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'c5d.large'|'c5d.xlarge'|'c5d.2xlarge'|'c5d.4xlarge'|'c5d.9xlarge'|'c5d.18xlarge'|'c5n.large'|'c5n.xlarge'|'c5n.2xlarge'|'c5n.4xlarge'|'c5n.9xlarge'|'c5n.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'g3s.xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'p3dn.24xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.4xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'m5.metal'|'m5a.large'|'m5a.xlarge'|'m5a.2xlarge'|'m5a.4xlarge'|'m5a.12xlarge'|'m5a.24xlarge'|'m5d.large'|'m5d.xlarge'|'m5d.2xlarge'|'m5d.4xlarge'|'m5d.12xlarge'|'m5d.24xlarge'|'m5d.metal'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge'|'z1d.large'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'z1d.metal'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal'|'a1.medium'|'a1.large'|'a1.xlarge'|'a1.2xlarge'|'a1.4xlarge',
                                        'MaxPrice': 'string',
                                        'SubnetId': 'string',
                                        'AvailabilityZone': 'string',
                                        'WeightedCapacity': 123.0,
                                        'Priority': 123.0,
                                        'Placement': {
                                            'GroupName': 'string'
                                        }
                                    }
                                },
                                'Lifecycle': 'spot'|'on-demand',
                                'ErrorCode': 'string',
                                'ErrorMessage': 'string'
                            },
                        ],
                        'Instances': [
                            {
                                'LaunchTemplateAndOverrides': {
                                    'LaunchTemplateSpecification': {
                                        'LaunchTemplateId': 'string',
                                        'LaunchTemplateName': 'string',
                                        'Version': 'string'
                                    },
                                    'Overrides': {
                                        'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'t3.nano'|'t3.micro'|'t3.small'|'t3.medium'|'t3.large'|'t3.xlarge'|'t3.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.12xlarge'|'r5.24xlarge'|'r5.metal'|'r5a.large'|'r5a.xlarge'|'r5a.2xlarge'|'r5a.4xlarge'|'r5a.12xlarge'|'r5a.24xlarge'|'r5d.large'|'r5d.xlarge'|'r5d.2xlarge'|'r5d.4xlarge'|'r5d.12xlarge'|'r5d.24xlarge'|'r5d.metal'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'i3.metal'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'c5d.large'|'c5d.xlarge'|'c5d.2xlarge'|'c5d.4xlarge'|'c5d.9xlarge'|'c5d.18xlarge'|'c5n.large'|'c5n.xlarge'|'c5n.2xlarge'|'c5n.4xlarge'|'c5n.9xlarge'|'c5n.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'g3s.xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'p3dn.24xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.4xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'m5.metal'|'m5a.large'|'m5a.xlarge'|'m5a.2xlarge'|'m5a.4xlarge'|'m5a.12xlarge'|'m5a.24xlarge'|'m5d.large'|'m5d.xlarge'|'m5d.2xlarge'|'m5d.4xlarge'|'m5d.12xlarge'|'m5d.24xlarge'|'m5d.metal'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge'|'z1d.large'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'z1d.metal'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal'|'a1.medium'|'a1.large'|'a1.xlarge'|'a1.2xlarge'|'a1.4xlarge',
                                        'MaxPrice': 'string',
                                        'SubnetId': 'string',
                                        'AvailabilityZone': 'string',
                                        'WeightedCapacity': 123.0,
                                        'Priority': 123.0,
                                        'Placement': {
                                            'GroupName': 'string'
                                        }
                                    }
                                },
                                'Lifecycle': 'spot'|'on-demand',
                                'InstanceIds': [
                                    'string',
                                ],
                                'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'t3.nano'|'t3.micro'|'t3.small'|'t3.medium'|'t3.large'|'t3.xlarge'|'t3.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.12xlarge'|'r5.24xlarge'|'r5.metal'|'r5a.large'|'r5a.xlarge'|'r5a.2xlarge'|'r5a.4xlarge'|'r5a.12xlarge'|'r5a.24xlarge'|'r5d.large'|'r5d.xlarge'|'r5d.2xlarge'|'r5d.4xlarge'|'r5d.12xlarge'|'r5d.24xlarge'|'r5d.metal'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'i3.metal'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'c5d.large'|'c5d.xlarge'|'c5d.2xlarge'|'c5d.4xlarge'|'c5d.9xlarge'|'c5d.18xlarge'|'c5n.large'|'c5n.xlarge'|'c5n.2xlarge'|'c5n.4xlarge'|'c5n.9xlarge'|'c5n.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'g3s.xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'p3dn.24xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.4xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'m5.metal'|'m5a.large'|'m5a.xlarge'|'m5a.2xlarge'|'m5a.4xlarge'|'m5a.12xlarge'|'m5a.24xlarge'|'m5d.large'|'m5d.xlarge'|'m5d.2xlarge'|'m5d.4xlarge'|'m5d.12xlarge'|'m5d.24xlarge'|'m5d.metal'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge'|'z1d.large'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'z1d.metal'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal'|'a1.medium'|'a1.large'|'a1.xlarge'|'a1.2xlarge'|'a1.4xlarge',
                                'Platform': 'Windows'
                            },
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Fleets** *(list) --* 
              Information about the EC2 Fleets.
              - *(dict) --* 
                Describes an EC2 Fleet.
                - **ActivityStatus** *(string) --* 
                  The progress of the EC2 Fleet. If there is an error, the status is ``error`` . After all requests are placed, the status is ``pending_fulfillment`` . If the size of the EC2 Fleet is equal to or greater than its target capacity, the status is ``fulfilled`` . If the size of the EC2 Fleet is decreased, the status is ``pending_termination`` while instances are terminating.
                - **CreateTime** *(datetime) --* 
                  The creation date and time of the EC2 Fleet.
                - **FleetId** *(string) --* 
                  The ID of the EC2 Fleet.
                - **FleetState** *(string) --* 
                  The state of the EC2 Fleet.
                - **ClientToken** *(string) --* 
                  Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see `Ensuring Idempotency <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html>`__ .
                  Constraints: Maximum 64 ASCII characters
                - **ExcessCapacityTerminationPolicy** *(string) --* 
                  Indicates whether running instances should be terminated if the target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet.
                - **FulfilledCapacity** *(float) --* 
                  The number of units fulfilled by this request compared to the set target capacity.
                - **FulfilledOnDemandCapacity** *(float) --* 
                  The number of units fulfilled by this request compared to the set target On-Demand capacity.
                - **LaunchTemplateConfigs** *(list) --* 
                  The launch template and overrides.
                  - *(dict) --* 
                    Describes a launch template and overrides.
                    - **LaunchTemplateSpecification** *(dict) --* 
                      The launch template.
                      - **LaunchTemplateId** *(string) --* 
                        The ID of the launch template. You must specify either a template ID or a template name.
                      - **LaunchTemplateName** *(string) --* 
                        The name of the launch template. You must specify either a template name or a template ID.
                      - **Version** *(string) --* 
                        The version number of the launch template. You must specify a version number.
                    - **Overrides** *(list) --* 
                      Any parameters that you specify override the same parameters in the launch template.
                      - *(dict) --* 
                        Describes overrides for a launch template.
                        - **InstanceType** *(string) --* 
                          The instance type.
                        - **MaxPrice** *(string) --* 
                          The maximum price per unit hour that you are willing to pay for a Spot Instance.
                        - **SubnetId** *(string) --* 
                          The ID of the subnet in which to launch the instances.
                        - **AvailabilityZone** *(string) --* 
                          The Availability Zone in which to launch the instances.
                        - **WeightedCapacity** *(float) --* 
                          The number of units provided by the specified instance type.
                        - **Priority** *(float) --* 
                          The priority for the launch template override. If **AllocationStrategy** is set to ``prioritized`` , EC2 Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity. The highest priority is launched first. Valid values are whole numbers starting at ``0`` . The lower the number, the higher the priority. If no number is set, the override has the lowest priority.
                        - **Placement** *(dict) --* 
                          The location where the instance launched, if applicable.
                          - **GroupName** *(string) --* 
                            The name of the placement group the instance is in.
                - **TargetCapacitySpecification** *(dict) --* 
                  The number of units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is ``maintain`` , you can specify a target capacity of 0 and add capacity later.
                  - **TotalTargetCapacity** *(integer) --* 
                    The number of units to request, filled using ``DefaultTargetCapacityType`` .
                  - **OnDemandTargetCapacity** *(integer) --* 
                    The number of On-Demand units to request.
                  - **SpotTargetCapacity** *(integer) --* 
                    The maximum number of Spot units to launch.
                  - **DefaultTargetCapacityType** *(string) --* 
                    The default ``TotalTargetCapacity`` , which is either ``Spot`` or ``On-Demand`` .
                - **TerminateInstancesWithExpiration** *(boolean) --* 
                  Indicates whether running instances should be terminated when the EC2 Fleet expires. 
                - **Type** *(string) --* 
                  The type of request. Indicates whether the EC2 Fleet only ``requests`` the target capacity, or also attempts to ``maintain`` it. If you request a certain target capacity, EC2 Fleet only places the required requests; it does not attempt to replenish instances if capacity is diminished, and does not submit requests in alternative capacity pools if capacity is unavailable. To maintain a certain target capacity, EC2 Fleet places the required requests to meet this target capacity. It also automatically replenishes any interrupted Spot Instances. Default: ``maintain`` .
                - **ValidFrom** *(datetime) --* 
                  The start date and time of the request, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z). The default is to start fulfilling the request immediately. 
                - **ValidUntil** *(datetime) --* 
                  The end date and time of the request, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z). At this point, no new instance requests are placed or able to fulfill the request. The default end date is 7 days from the current date. 
                - **ReplaceUnhealthyInstances** *(boolean) --* 
                  Indicates whether EC2 Fleet should replace unhealthy instances.
                - **SpotOptions** *(dict) --* 
                  The configuration of Spot Instances in an EC2 Fleet.
                  - **AllocationStrategy** *(string) --* 
                    Indicates how to allocate the target capacity across the Spot pools specified by the Spot Fleet request. The default is ``lowest-price`` .
                  - **InstanceInterruptionBehavior** *(string) --* 
                    The behavior when a Spot Instance is interrupted. The default is ``terminate`` .
                  - **InstancePoolsToUseCount** *(integer) --* 
                    The number of Spot pools across which to allocate your target Spot capacity. Valid only when **AllocationStrategy** is set to ``lowestPrice`` . EC2 Fleet selects the cheapest Spot pools and evenly allocates your target Spot capacity across the number of Spot pools that you specify.
                  - **SingleInstanceType** *(boolean) --* 
                    Indicates that the fleet uses a single instance type to launch all Spot Instances in the fleet.
                  - **SingleAvailabilityZone** *(boolean) --* 
                    Indicates that the fleet launches all Spot Instances into a single Availability Zone.
                  - **MinTargetCapacity** *(integer) --* 
                    The minimum target capacity for Spot Instances in the fleet. If the minimum target capacity is not reached, the fleet launches no instances.
                - **OnDemandOptions** *(dict) --* 
                  The allocation strategy of On-Demand Instances in an EC2 Fleet.
                  - **AllocationStrategy** *(string) --* 
                    The order of the launch template overrides to use in fulfilling On-Demand capacity. If you specify ``lowest-price`` , EC2 Fleet uses price to determine the order, launching the lowest price first. If you specify ``prioritized`` , EC2 Fleet uses the priority that you assigned to each launch template override, launching the highest priority first. If you do not specify a value, EC2 Fleet defaults to ``lowest-price`` .
                  - **SingleInstanceType** *(boolean) --* 
                    Indicates that the fleet uses a single instance type to launch all On-Demand Instances in the fleet.
                  - **SingleAvailabilityZone** *(boolean) --* 
                    Indicates that the fleet launches all On-Demand Instances into a single Availability Zone.
                  - **MinTargetCapacity** *(integer) --* 
                    The minimum target capacity for On-Demand Instances in the fleet. If the minimum target capacity is not reached, the fleet launches no instances.
                - **Tags** *(list) --* 
                  The tags for an EC2 Fleet resource.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
                - **Errors** *(list) --* 
                  Information about the instances that could not be launched by the fleet. Valid only when **Type** is set to ``instant`` .
                  - *(dict) --* 
                    Describes the instances that could not be launched by the fleet.
                    - **LaunchTemplateAndOverrides** *(dict) --* 
                      The launch templates and overrides that were used for launching the instances. Any parameters that you specify in the Overrides override the same parameters in the launch template.
                      - **LaunchTemplateSpecification** *(dict) --* 
                        The launch template.
                        - **LaunchTemplateId** *(string) --* 
                          The ID of the launch template. You must specify either a template ID or a template name.
                        - **LaunchTemplateName** *(string) --* 
                          The name of the launch template. You must specify either a template name or a template ID.
                        - **Version** *(string) --* 
                          The version number of the launch template. You must specify a version number.
                      - **Overrides** *(dict) --* 
                        Any parameters that you specify override the same parameters in the launch template.
                        - **InstanceType** *(string) --* 
                          The instance type.
                        - **MaxPrice** *(string) --* 
                          The maximum price per unit hour that you are willing to pay for a Spot Instance.
                        - **SubnetId** *(string) --* 
                          The ID of the subnet in which to launch the instances.
                        - **AvailabilityZone** *(string) --* 
                          The Availability Zone in which to launch the instances.
                        - **WeightedCapacity** *(float) --* 
                          The number of units provided by the specified instance type.
                        - **Priority** *(float) --* 
                          The priority for the launch template override. If **AllocationStrategy** is set to ``prioritized`` , EC2 Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity. The highest priority is launched first. Valid values are whole numbers starting at ``0`` . The lower the number, the higher the priority. If no number is set, the override has the lowest priority.
                        - **Placement** *(dict) --* 
                          The location where the instance launched, if applicable.
                          - **GroupName** *(string) --* 
                            The name of the placement group the instance is in.
                    - **Lifecycle** *(string) --* 
                      Indicates if the instance that could not be launched was a Spot Instance or On-Demand Instance.
                    - **ErrorCode** *(string) --* 
                      The error code that indicates why the instance could not be launched. For more information about error codes, see `Error Codes <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html.html>`__ .
                    - **ErrorMessage** *(string) --* 
                      The error message that describes why the instance could not be launched. For more information about error messages, see ee `Error Codes <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html.html>`__ .
                - **Instances** *(list) --* 
                  Information about the instances that were launched by the fleet. Valid only when **Type** is set to ``instant`` .
                  - *(dict) --* 
                    Describes the instances that were launched by the fleet.
                    - **LaunchTemplateAndOverrides** *(dict) --* 
                      The launch templates and overrides that were used for launching the instances. Any parameters that you specify in the Overrides override the same parameters in the launch template.
                      - **LaunchTemplateSpecification** *(dict) --* 
                        The launch template.
                        - **LaunchTemplateId** *(string) --* 
                          The ID of the launch template. You must specify either a template ID or a template name.
                        - **LaunchTemplateName** *(string) --* 
                          The name of the launch template. You must specify either a template name or a template ID.
                        - **Version** *(string) --* 
                          The version number of the launch template. You must specify a version number.
                      - **Overrides** *(dict) --* 
                        Any parameters that you specify override the same parameters in the launch template.
                        - **InstanceType** *(string) --* 
                          The instance type.
                        - **MaxPrice** *(string) --* 
                          The maximum price per unit hour that you are willing to pay for a Spot Instance.
                        - **SubnetId** *(string) --* 
                          The ID of the subnet in which to launch the instances.
                        - **AvailabilityZone** *(string) --* 
                          The Availability Zone in which to launch the instances.
                        - **WeightedCapacity** *(float) --* 
                          The number of units provided by the specified instance type.
                        - **Priority** *(float) --* 
                          The priority for the launch template override. If **AllocationStrategy** is set to ``prioritized`` , EC2 Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity. The highest priority is launched first. Valid values are whole numbers starting at ``0`` . The lower the number, the higher the priority. If no number is set, the override has the lowest priority.
                        - **Placement** *(dict) --* 
                          The location where the instance launched, if applicable.
                          - **GroupName** *(string) --* 
                            The name of the placement group the instance is in.
                    - **Lifecycle** *(string) --* 
                      Indicates if the instance that was launched is a Spot Instance or On-Demand Instance.
                    - **InstanceIds** *(list) --* 
                      The IDs of the instances.
                      - *(string) --* 
                    - **InstanceType** *(string) --* 
                      The instance type.
                    - **Platform** *(string) --* 
                      The value is ``Windows`` for Windows instances; otherwise blank.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type FleetIds: list
        :param FleetIds:
          The ID of the EC2 Fleets.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``activity-status`` - The progress of the EC2 Fleet ( ``error`` | ``pending-fulfillment`` | ``pending-termination`` | ``fulfilled`` ).
          * ``excess-capacity-termination-policy`` - Indicates whether to terminate running instances if the target capacity is decreased below the current EC2 Fleet size (``true`` | ``false`` ).
          * ``fleet-state`` - The state of the EC2 Fleet (``submitted`` | ``active`` | ``deleted`` | ``failed`` | ``deleted-running`` | ``deleted-terminating`` | ``modifying`` ).
          * ``replace-unhealthy-instances`` - Indicates whether EC2 Fleet should replace unhealthy instances (``true`` | ``false`` ).
          * ``type`` - The type of request (``instant`` | ``request`` | ``maintain`` ).
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeFlowLogs(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, FlowLogIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_flow_logs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeFlowLogs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              FlowLogIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'FlowLogs': [
                    {
                        'CreationTime': datetime(2015, 1, 1),
                        'DeliverLogsErrorMessage': 'string',
                        'DeliverLogsPermissionArn': 'string',
                        'DeliverLogsStatus': 'string',
                        'FlowLogId': 'string',
                        'FlowLogStatus': 'string',
                        'LogGroupName': 'string',
                        'ResourceId': 'string',
                        'TrafficType': 'ACCEPT'|'REJECT'|'ALL',
                        'LogDestinationType': 'cloud-watch-logs'|'s3',
                        'LogDestination': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FlowLogs** *(list) --* 
              Information about the flow logs.
              - *(dict) --* 
                Describes a flow log.
                - **CreationTime** *(datetime) --* 
                  The date and time the flow log was created.
                - **DeliverLogsErrorMessage** *(string) --* 
                  Information about the error that occurred. ``Rate limited`` indicates that CloudWatch Logs throttling has been applied for one or more network interfaces, or that you've reached the limit on the number of log groups that you can create. ``Access error`` indicates that the IAM role associated with the flow log does not have sufficient permissions to publish to CloudWatch Logs. ``Unknown error`` indicates an internal error.
                - **DeliverLogsPermissionArn** *(string) --* 
                  The ARN of the IAM role that posts logs to CloudWatch Logs.
                - **DeliverLogsStatus** *(string) --* 
                  The status of the logs delivery (``SUCCESS`` | ``FAILED`` ).
                - **FlowLogId** *(string) --* 
                  The flow log ID.
                - **FlowLogStatus** *(string) --* 
                  The status of the flow log (``ACTIVE`` ).
                - **LogGroupName** *(string) --* 
                  The name of the flow log group.
                - **ResourceId** *(string) --* 
                  The ID of the resource on which the flow log was created.
                - **TrafficType** *(string) --* 
                  The type of traffic captured for the flow log.
                - **LogDestinationType** *(string) --* 
                  Specifies the type of destination to which the flow log data is published. Flow log data can be published to CloudWatch Logs or Amazon S3.
                - **LogDestination** *(string) --* 
                  Specifies the destination to which the flow log data is published. Flow log data can be published to an CloudWatch Logs log group or an Amazon S3 bucket. If the flow log publishes to CloudWatch Logs, this element indicates the Amazon Resource Name (ARN) of the CloudWatch Logs log group to which the data is published. If the flow log publishes to Amazon S3, this element indicates the ARN of the Amazon S3 bucket to which the data is published.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``deliver-log-status`` - The status of the logs delivery (``SUCCESS`` | ``FAILED`` ).
          * ``log-destination-type`` - The type of destination to which the flow log publishes data. Possible destination types include ``cloud-watch-logs`` and ``S3`` .
          * ``flow-log-id`` - The ID of the flow log.
          * ``log-group-name`` - The name of the log group.
          * ``resource-id`` - The ID of the VPC, subnet, or network interface.
          * ``traffic-type`` - The type of traffic (``ACCEPT`` | ``REJECT`` | ``ALL`` ).
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
        :type FlowLogIds: list
        :param FlowLogIds:
          One or more flow log IDs.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeFpgaImages(Paginator):
    def paginate(self, DryRun: bool = None, FpgaImageIds: List = None, Owners: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_fpga_images`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeFpgaImages>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              FpgaImageIds=[
                  'string',
              ],
              Owners=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'FpgaImages': [
                    {
                        'FpgaImageId': 'string',
                        'FpgaImageGlobalId': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'ShellVersion': 'string',
                        'PciId': {
                            'DeviceId': 'string',
                            'VendorId': 'string',
                            'SubsystemId': 'string',
                            'SubsystemVendorId': 'string'
                        },
                        'State': {
                            'Code': 'pending'|'failed'|'available'|'unavailable',
                            'Message': 'string'
                        },
                        'CreateTime': datetime(2015, 1, 1),
                        'UpdateTime': datetime(2015, 1, 1),
                        'OwnerId': 'string',
                        'OwnerAlias': 'string',
                        'ProductCodes': [
                            {
                                'ProductCodeId': 'string',
                                'ProductCodeType': 'devpay'|'marketplace'
                            },
                        ],
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'Public': True|False
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FpgaImages** *(list) --* 
              Information about one or more FPGA images.
              - *(dict) --* 
                Describes an Amazon FPGA image (AFI).
                - **FpgaImageId** *(string) --* 
                  The FPGA image identifier (AFI ID).
                - **FpgaImageGlobalId** *(string) --* 
                  The global FPGA image identifier (AGFI ID).
                - **Name** *(string) --* 
                  The name of the AFI.
                - **Description** *(string) --* 
                  The description of the AFI.
                - **ShellVersion** *(string) --* 
                  The version of the AWS Shell that was used to create the bitstream.
                - **PciId** *(dict) --* 
                  Information about the PCI bus.
                  - **DeviceId** *(string) --* 
                    The ID of the device.
                  - **VendorId** *(string) --* 
                    The ID of the vendor.
                  - **SubsystemId** *(string) --* 
                    The ID of the subsystem.
                  - **SubsystemVendorId** *(string) --* 
                    The ID of the vendor for the subsystem.
                - **State** *(dict) --* 
                  Information about the state of the AFI.
                  - **Code** *(string) --* 
                    The state. The following are the possible values:
                    * ``pending`` - AFI bitstream generation is in progress. 
                    * ``available`` - The AFI is available for use. 
                    * ``failed`` - AFI bitstream generation failed. 
                    * ``unavailable`` - The AFI is no longer available for use. 
                  - **Message** *(string) --* 
                    If the state is ``failed`` , this is the error message.
                - **CreateTime** *(datetime) --* 
                  The date and time the AFI was created.
                - **UpdateTime** *(datetime) --* 
                  The time of the most recent update to the AFI.
                - **OwnerId** *(string) --* 
                  The AWS account ID of the AFI owner.
                - **OwnerAlias** *(string) --* 
                  The alias of the AFI owner. Possible values include ``self`` , ``amazon`` , and ``aws-marketplace`` .
                - **ProductCodes** *(list) --* 
                  The product codes for the AFI.
                  - *(dict) --* 
                    Describes a product code.
                    - **ProductCodeId** *(string) --* 
                      The product code.
                    - **ProductCodeType** *(string) --* 
                      The type of product code.
                - **Tags** *(list) --* 
                  Any tags assigned to the AFI.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
                - **Public** *(boolean) --* 
                  Indicates whether the AFI is public.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type FpgaImageIds: list
        :param FpgaImageIds:
          One or more AFI IDs.
          - *(string) --*
        :type Owners: list
        :param Owners:
          Filters the AFI by owner. Specify an AWS account ID, ``self`` (owner is the sender of the request), or an AWS owner alias (valid values are ``amazon`` | ``aws-marketplace`` ).
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``create-time`` - The creation time of the AFI.
          * ``fpga-image-id`` - The FPGA image identifier (AFI ID).
          * ``fpga-image-global-id`` - The global FPGA image identifier (AGFI ID).
          * ``name`` - The name of the AFI.
          * ``owner-id`` - The AWS account ID of the AFI owner.
          * ``product-code`` - The product code.
          * ``shell-version`` - The version of the AWS Shell that was used to create the bitstream.
          * ``state`` - The state of the AFI (``pending`` | ``failed`` | ``available`` | ``unavailable`` ).
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value.
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
          * ``update-time`` - The time of the most recent update.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeHostReservationOfferings(Paginator):
    def paginate(self, Filters: List = None, MaxDuration: int = None, MinDuration: int = None, OfferingId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_host_reservation_offerings`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeHostReservationOfferings>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxDuration=123,
              MinDuration=123,
              OfferingId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'OfferingSet': [
                    {
                        'CurrencyCode': 'USD',
                        'Duration': 123,
                        'HourlyPrice': 'string',
                        'InstanceFamily': 'string',
                        'OfferingId': 'string',
                        'PaymentOption': 'AllUpfront'|'PartialUpfront'|'NoUpfront',
                        'UpfrontPrice': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **OfferingSet** *(list) --* 
              Information about the offerings.
              - *(dict) --* 
                Details about the Dedicated Host Reservation offering.
                - **CurrencyCode** *(string) --* 
                  The currency of the offering.
                - **Duration** *(integer) --* 
                  The duration of the offering (in seconds).
                - **HourlyPrice** *(string) --* 
                  The hourly price of the offering.
                - **InstanceFamily** *(string) --* 
                  The instance family of the offering.
                - **OfferingId** *(string) --* 
                  The ID of the offering.
                - **PaymentOption** *(string) --* 
                  The available payment option.
                - **UpfrontPrice** *(string) --* 
                  The upfront price of the offering. Does not apply to No Upfront offerings.
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``instance-family`` - The instance family of the offering (for example, ``m4`` ).
          * ``payment-option`` - The payment option (``NoUpfront`` | ``PartialUpfront`` | ``AllUpfront`` ).
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
        :type MaxDuration: integer
        :param MaxDuration:
          This is the maximum duration of the reservation to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 94608000 for three years.
        :type MinDuration: integer
        :param MinDuration:
          This is the minimum duration of the reservation you\'d like to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 31536000 for one year.
        :type OfferingId: string
        :param OfferingId:
          The ID of the reservation offering.
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeHostReservations(Paginator):
    def paginate(self, Filters: List = None, HostReservationIdSet: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_host_reservations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeHostReservations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              HostReservationIdSet=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'HostReservationSet': [
                    {
                        'Count': 123,
                        'CurrencyCode': 'USD',
                        'Duration': 123,
                        'End': datetime(2015, 1, 1),
                        'HostIdSet': [
                            'string',
                        ],
                        'HostReservationId': 'string',
                        'HourlyPrice': 'string',
                        'InstanceFamily': 'string',
                        'OfferingId': 'string',
                        'PaymentOption': 'AllUpfront'|'PartialUpfront'|'NoUpfront',
                        'Start': datetime(2015, 1, 1),
                        'State': 'payment-pending'|'payment-failed'|'active'|'retired',
                        'UpfrontPrice': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **HostReservationSet** *(list) --* 
              Details about the reservation's configuration.
              - *(dict) --* 
                Details about the Dedicated Host Reservation and associated Dedicated Hosts.
                - **Count** *(integer) --* 
                  The number of Dedicated Hosts the reservation is associated with.
                - **CurrencyCode** *(string) --* 
                  The currency in which the ``upfrontPrice`` and ``hourlyPrice`` amounts are specified. At this time, the only supported currency is ``USD`` .
                - **Duration** *(integer) --* 
                  The length of the reservation's term, specified in seconds. Can be ``31536000 (1 year)`` | ``94608000 (3 years)`` .
                - **End** *(datetime) --* 
                  The date and time that the reservation ends.
                - **HostIdSet** *(list) --* 
                  The IDs of the Dedicated Hosts associated with the reservation.
                  - *(string) --* 
                - **HostReservationId** *(string) --* 
                  The ID of the reservation that specifies the associated Dedicated Hosts.
                - **HourlyPrice** *(string) --* 
                  The hourly price of the reservation.
                - **InstanceFamily** *(string) --* 
                  The instance family of the Dedicated Host Reservation. The instance family on the Dedicated Host must be the same in order for it to benefit from the reservation.
                - **OfferingId** *(string) --* 
                  The ID of the reservation. This remains the same regardless of which Dedicated Hosts are associated with it.
                - **PaymentOption** *(string) --* 
                  The payment option selected for this reservation.
                - **Start** *(datetime) --* 
                  The date and time that the reservation started.
                - **State** *(string) --* 
                  The state of the reservation.
                - **UpfrontPrice** *(string) --* 
                  The upfront price of the reservation.
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``instance-family`` - The instance family (for example, ``m4`` ).
          * ``payment-option`` - The payment option (``NoUpfront`` | ``PartialUpfront`` | ``AllUpfront`` ).
          * ``state`` - The state of the reservation (``payment-pending`` | ``payment-failed`` | ``active`` | ``retired`` ).
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
        :type HostReservationIdSet: list
        :param HostReservationIdSet:
          One or more host reservation IDs.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeHosts(Paginator):
    def paginate(self, Filters: List = None, HostIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_hosts`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeHosts>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              HostIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Hosts': [
                    {
                        'AutoPlacement': 'on'|'off',
                        'AvailabilityZone': 'string',
                        'AvailableCapacity': {
                            'AvailableInstanceCapacity': [
                                {
                                    'AvailableCapacity': 123,
                                    'InstanceType': 'string',
                                    'TotalCapacity': 123
                                },
                            ],
                            'AvailableVCpus': 123
                        },
                        'ClientToken': 'string',
                        'HostId': 'string',
                        'HostProperties': {
                            'Cores': 123,
                            'InstanceType': 'string',
                            'Sockets': 123,
                            'TotalVCpus': 123
                        },
                        'HostReservationId': 'string',
                        'Instances': [
                            {
                                'InstanceId': 'string',
                                'InstanceType': 'string'
                            },
                        ],
                        'State': 'available'|'under-assessment'|'permanent-failure'|'released'|'released-permanent-failure',
                        'AllocationTime': datetime(2015, 1, 1),
                        'ReleaseTime': datetime(2015, 1, 1),
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Hosts** *(list) --* 
              Information about the Dedicated Hosts.
              - *(dict) --* 
                Describes the properties of the Dedicated Host.
                - **AutoPlacement** *(string) --* 
                  Whether auto-placement is on or off.
                - **AvailabilityZone** *(string) --* 
                  The Availability Zone of the Dedicated Host.
                - **AvailableCapacity** *(dict) --* 
                  The number of new instances that can be launched onto the Dedicated Host.
                  - **AvailableInstanceCapacity** *(list) --* 
                    The total number of instances supported by the Dedicated Host.
                    - *(dict) --* 
                      Information about the instance type that the Dedicated Host supports.
                      - **AvailableCapacity** *(integer) --* 
                        The number of instances that can still be launched onto the Dedicated Host.
                      - **InstanceType** *(string) --* 
                        The instance type size supported by the Dedicated Host.
                      - **TotalCapacity** *(integer) --* 
                        The total number of instances that can be launched onto the Dedicated Host.
                  - **AvailableVCpus** *(integer) --* 
                    The number of vCPUs available on the Dedicated Host.
                - **ClientToken** *(string) --* 
                  Unique, case-sensitive identifier that you provide to ensure idempotency of the request. For more information, see `How to Ensure Idempotency <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Run_Instance_Idempotency.html>`__ in the *Amazon Elastic Compute Cloud User Guide* . 
                - **HostId** *(string) --* 
                  The ID of the Dedicated Host.
                - **HostProperties** *(dict) --* 
                  The hardware specifications of the Dedicated Host.
                  - **Cores** *(integer) --* 
                    The number of cores on the Dedicated Host.
                  - **InstanceType** *(string) --* 
                    The instance type size that the Dedicated Host supports (for example, ``m3.medium`` ).
                  - **Sockets** *(integer) --* 
                    The number of sockets on the Dedicated Host.
                  - **TotalVCpus** *(integer) --* 
                    The number of vCPUs on the Dedicated Host.
                - **HostReservationId** *(string) --* 
                  The reservation ID of the Dedicated Host. This returns a ``null`` response if the Dedicated Host doesn't have an associated reservation.
                - **Instances** *(list) --* 
                  The IDs and instance type that are currently running on the Dedicated Host.
                  - *(dict) --* 
                    Describes an instance running on a Dedicated Host.
                    - **InstanceId** *(string) --* 
                      the IDs of instances that are running on the Dedicated Host.
                    - **InstanceType** *(string) --* 
                      The instance type size (for example, ``m3.medium`` ) of the running instance.
                - **State** *(string) --* 
                  The Dedicated Host's state.
                - **AllocationTime** *(datetime) --* 
                  The time that the Dedicated Host was allocated.
                - **ReleaseTime** *(datetime) --* 
                  The time that the Dedicated Host was released.
                - **Tags** *(list) --* 
                  Any tags assigned to the Dedicated Host.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``auto-placement`` - Whether auto-placement is enabled or disabled (``on`` | ``off`` ).
          * ``availability-zone`` - The Availability Zone of the host.
          * ``client-token`` - The idempotency token that you provided when you allocated the host.
          * ``host-reservation-id`` - The ID of the reservation assigned to this host.
          * ``instance-type`` - The instance type size that the Dedicated Host is configured to support.
          * ``state`` - The allocation state of the Dedicated Host (``available`` | ``under-assessment`` | ``permanent-failure`` | ``released`` | ``released-permanent-failure`` ).
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
        :type HostIds: list
        :param HostIds:
          The IDs of the Dedicated Hosts. The IDs are used for targeted instance launches.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeIamInstanceProfileAssociations(Paginator):
    def paginate(self, AssociationIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_iam_instance_profile_associations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeIamInstanceProfileAssociations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AssociationIds=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'IamInstanceProfileAssociations': [
                    {
                        'AssociationId': 'string',
                        'InstanceId': 'string',
                        'IamInstanceProfile': {
                            'Arn': 'string',
                            'Id': 'string'
                        },
                        'State': 'associating'|'associated'|'disassociating'|'disassociated',
                        'Timestamp': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **IamInstanceProfileAssociations** *(list) --* 
              Information about one or more IAM instance profile associations.
              - *(dict) --* 
                Describes an association between an IAM instance profile and an instance.
                - **AssociationId** *(string) --* 
                  The ID of the association.
                - **InstanceId** *(string) --* 
                  The ID of the instance.
                - **IamInstanceProfile** *(dict) --* 
                  The IAM instance profile.
                  - **Arn** *(string) --* 
                    The Amazon Resource Name (ARN) of the instance profile.
                  - **Id** *(string) --* 
                    The ID of the instance profile.
                - **State** *(string) --* 
                  The state of the association.
                - **Timestamp** *(datetime) --* 
                  The time the IAM instance profile was associated with the instance.
        :type AssociationIds: list
        :param AssociationIds:
          One or more IAM instance profile associations.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``instance-id`` - The ID of the instance.
          * ``state`` - The state of the association (``associating`` | ``associated`` | ``disassociating`` | ``disassociated`` ).
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeImportImageTasks(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, ImportTaskIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_import_image_tasks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeImportImageTasks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              ImportTaskIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ImportImageTasks': [
                    {
                        'Architecture': 'string',
                        'Description': 'string',
                        'Encrypted': True|False,
                        'Hypervisor': 'string',
                        'ImageId': 'string',
                        'ImportTaskId': 'string',
                        'KmsKeyId': 'string',
                        'LicenseType': 'string',
                        'Platform': 'string',
                        'Progress': 'string',
                        'SnapshotDetails': [
                            {
                                'Description': 'string',
                                'DeviceName': 'string',
                                'DiskImageSize': 123.0,
                                'Format': 'string',
                                'Progress': 'string',
                                'SnapshotId': 'string',
                                'Status': 'string',
                                'StatusMessage': 'string',
                                'Url': 'string',
                                'UserBucket': {
                                    'S3Bucket': 'string',
                                    'S3Key': 'string'
                                }
                            },
                        ],
                        'Status': 'string',
                        'StatusMessage': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output for DescribeImportImageTasks.
            - **ImportImageTasks** *(list) --* 
              A list of zero or more import image tasks that are currently active or were completed or canceled in the previous 7 days.
              - *(dict) --* 
                Describes an import image task.
                - **Architecture** *(string) --* 
                  The architecture of the virtual machine.
                  Valid values: ``i386`` | ``x86_64``  
                - **Description** *(string) --* 
                  A description of the import task.
                - **Encrypted** *(boolean) --* 
                  Indicates whether the image is encrypted.
                - **Hypervisor** *(string) --* 
                  The target hypervisor for the import task.
                  Valid values: ``xen``  
                - **ImageId** *(string) --* 
                  The ID of the Amazon Machine Image (AMI) of the imported virtual machine.
                - **ImportTaskId** *(string) --* 
                  The ID of the import image task.
                - **KmsKeyId** *(string) --* 
                  The identifier for the AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to create the encrypted image.
                - **LicenseType** *(string) --* 
                  The license type of the virtual machine.
                - **Platform** *(string) --* 
                  The description string for the import image task.
                - **Progress** *(string) --* 
                  The percentage of progress of the import image task.
                - **SnapshotDetails** *(list) --* 
                  Information about the snapshots.
                  - *(dict) --* 
                    Describes the snapshot created from the imported disk.
                    - **Description** *(string) --* 
                      A description for the snapshot.
                    - **DeviceName** *(string) --* 
                      The block device mapping for the snapshot.
                    - **DiskImageSize** *(float) --* 
                      The size of the disk in the snapshot, in GiB.
                    - **Format** *(string) --* 
                      The format of the disk image from which the snapshot is created.
                    - **Progress** *(string) --* 
                      The percentage of progress for the task.
                    - **SnapshotId** *(string) --* 
                      The snapshot ID of the disk being imported.
                    - **Status** *(string) --* 
                      A brief status of the snapshot creation.
                    - **StatusMessage** *(string) --* 
                      A detailed status message for the snapshot creation.
                    - **Url** *(string) --* 
                      The URL used to access the disk image.
                    - **UserBucket** *(dict) --* 
                      The S3 bucket for the disk image.
                      - **S3Bucket** *(string) --* 
                        The S3 bucket from which the disk image was created.
                      - **S3Key** *(string) --* 
                        The file name of the disk image.
                - **Status** *(string) --* 
                  A brief status for the import image task.
                - **StatusMessage** *(string) --* 
                  A descriptive status message for the import image task.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type Filters: list
        :param Filters:
          Filter tasks using the ``task-state`` filter and one of the following values: active, completed, deleting, deleted.
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
        :type ImportTaskIds: list
        :param ImportTaskIds:
          A list of import image task IDs.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeImportSnapshotTasks(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, ImportTaskIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_import_snapshot_tasks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeImportSnapshotTasks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              ImportTaskIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ImportSnapshotTasks': [
                    {
                        'Description': 'string',
                        'ImportTaskId': 'string',
                        'SnapshotTaskDetail': {
                            'Description': 'string',
                            'DiskImageSize': 123.0,
                            'Encrypted': True|False,
                            'Format': 'string',
                            'KmsKeyId': 'string',
                            'Progress': 'string',
                            'SnapshotId': 'string',
                            'Status': 'string',
                            'StatusMessage': 'string',
                            'Url': 'string',
                            'UserBucket': {
                                'S3Bucket': 'string',
                                'S3Key': 'string'
                            }
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output for DescribeImportSnapshotTasks.
            - **ImportSnapshotTasks** *(list) --* 
              A list of zero or more import snapshot tasks that are currently active or were completed or canceled in the previous 7 days.
              - *(dict) --* 
                Describes an import snapshot task.
                - **Description** *(string) --* 
                  A description of the import snapshot task.
                - **ImportTaskId** *(string) --* 
                  The ID of the import snapshot task.
                - **SnapshotTaskDetail** *(dict) --* 
                  Describes an import snapshot task.
                  - **Description** *(string) --* 
                    The description of the snapshot.
                  - **DiskImageSize** *(float) --* 
                    The size of the disk in the snapshot, in GiB.
                  - **Encrypted** *(boolean) --* 
                    Indicates whether the snapshot is encrypted.
                  - **Format** *(string) --* 
                    The format of the disk image from which the snapshot is created.
                  - **KmsKeyId** *(string) --* 
                    The identifier for the AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to create the encrypted snapshot.
                  - **Progress** *(string) --* 
                    The percentage of completion for the import snapshot task.
                  - **SnapshotId** *(string) --* 
                    The snapshot ID of the disk being imported.
                  - **Status** *(string) --* 
                    A brief status for the import snapshot task.
                  - **StatusMessage** *(string) --* 
                    A detailed status message for the import snapshot task.
                  - **Url** *(string) --* 
                    The URL of the disk image from which the snapshot is created.
                  - **UserBucket** *(dict) --* 
                    The S3 bucket for the disk image.
                    - **S3Bucket** *(string) --* 
                      The S3 bucket from which the disk image was created.
                    - **S3Key** *(string) --* 
                      The file name of the disk image.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type Filters: list
        :param Filters:
          One or more filters.
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
        :type ImportTaskIds: list
        :param ImportTaskIds:
          A list of import snapshot task IDs.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeInstanceCreditSpecifications(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, InstanceIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_instance_credit_specifications`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstanceCreditSpecifications>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              InstanceIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'InstanceCreditSpecifications': [
                    {
                        'InstanceId': 'string',
                        'CpuCredits': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **InstanceCreditSpecifications** *(list) --* 
              Information about the credit option for CPU usage of an instance.
              - *(dict) --* 
                Describes the credit option for CPU usage of a T2 or T3 instance. 
                - **InstanceId** *(string) --* 
                  The ID of the instance.
                - **CpuCredits** *(string) --* 
                  The credit option for CPU usage of the instance. Valid values are ``standard`` and ``unlimited`` .
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``instance-id`` - The ID of the instance.
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
          Constraints: Maximum 1000 explicitly specified instance IDs.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeInstanceStatus(Paginator):
    def paginate(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, IncludeAllInstances: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_instance_status`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstanceStatus>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              InstanceIds=[
                  'string',
              ],
              DryRun=True|False,
              IncludeAllInstances=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'InstanceStatuses': [
                    {
                        'AvailabilityZone': 'string',
                        'Events': [
                            {
                                'Code': 'instance-reboot'|'system-reboot'|'system-maintenance'|'instance-retirement'|'instance-stop',
                                'Description': 'string',
                                'NotAfter': datetime(2015, 1, 1),
                                'NotBefore': datetime(2015, 1, 1)
                            },
                        ],
                        'InstanceId': 'string',
                        'InstanceState': {
                            'Code': 123,
                            'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
                        },
                        'InstanceStatus': {
                            'Details': [
                                {
                                    'ImpairedSince': datetime(2015, 1, 1),
                                    'Name': 'reachability',
                                    'Status': 'passed'|'failed'|'insufficient-data'|'initializing'
                                },
                            ],
                            'Status': 'ok'|'impaired'|'insufficient-data'|'not-applicable'|'initializing'
                        },
                        'SystemStatus': {
                            'Details': [
                                {
                                    'ImpairedSince': datetime(2015, 1, 1),
                                    'Name': 'reachability',
                                    'Status': 'passed'|'failed'|'insufficient-data'|'initializing'
                                },
                            ],
                            'Status': 'ok'|'impaired'|'insufficient-data'|'not-applicable'|'initializing'
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **InstanceStatuses** *(list) --* 
              One or more instance status descriptions.
              - *(dict) --* 
                Describes the status of an instance.
                - **AvailabilityZone** *(string) --* 
                  The Availability Zone of the instance.
                - **Events** *(list) --* 
                  Any scheduled events associated with the instance.
                  - *(dict) --* 
                    Describes a scheduled event for an instance.
                    - **Code** *(string) --* 
                      The event code.
                    - **Description** *(string) --* 
                      A description of the event.
                      After a scheduled event is completed, it can still be described for up to a week. If the event has been completed, this description starts with the following text: [Completed].
                    - **NotAfter** *(datetime) --* 
                      The latest scheduled end time for the event.
                    - **NotBefore** *(datetime) --* 
                      The earliest scheduled start time for the event.
                - **InstanceId** *(string) --* 
                  The ID of the instance.
                - **InstanceState** *(dict) --* 
                  The intended state of the instance.  DescribeInstanceStatus requires that an instance be in the ``running`` state.
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
                - **InstanceStatus** *(dict) --* 
                  Reports impaired functionality that stems from issues internal to the instance, such as impaired reachability.
                  - **Details** *(list) --* 
                    The system instance health or application instance health.
                    - *(dict) --* 
                      Describes the instance status.
                      - **ImpairedSince** *(datetime) --* 
                        The time when a status check failed. For an instance that was launched and impaired, this is the time when the instance was launched.
                      - **Name** *(string) --* 
                        The type of instance status.
                      - **Status** *(string) --* 
                        The status.
                  - **Status** *(string) --* 
                    The status.
                - **SystemStatus** *(dict) --* 
                  Reports impaired functionality that stems from issues related to the systems that support an instance, such as hardware failures and network connectivity problems.
                  - **Details** *(list) --* 
                    The system instance health or application instance health.
                    - *(dict) --* 
                      Describes the instance status.
                      - **ImpairedSince** *(datetime) --* 
                        The time when a status check failed. For an instance that was launched and impaired, this is the time when the instance was launched.
                      - **Name** *(string) --* 
                        The type of instance status.
                      - **Status** *(string) --* 
                        The status.
                  - **Status** *(string) --* 
                    The status.
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``availability-zone`` - The Availability Zone of the instance.
          * ``event.code`` - The code for the scheduled event (``instance-reboot`` | ``system-reboot`` | ``system-maintenance`` | ``instance-retirement`` | ``instance-stop`` ).
          * ``event.description`` - A description of the event.
          * ``event.not-after`` - The latest end time for the scheduled event (for example, ``2014-09-15T17:15:20.000Z`` ).
          * ``event.not-before`` - The earliest start time for the scheduled event (for example, ``2014-09-15T17:15:20.000Z`` ).
          * ``instance-state-code`` - The code for the instance state, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped).
          * ``instance-state-name`` - The state of the instance (``pending`` | ``running`` | ``shutting-down`` | ``terminated`` | ``stopping`` | ``stopped`` ).
          * ``instance-status.reachability`` - Filters on instance status where the name is ``reachability`` (``passed`` | ``failed`` | ``initializing`` | ``insufficient-data`` ).
          * ``instance-status.status`` - The status of the instance (``ok`` | ``impaired`` | ``initializing`` | ``insufficient-data`` | ``not-applicable`` ).
          * ``system-status.reachability`` - Filters on system status where the name is ``reachability`` (``passed`` | ``failed`` | ``initializing`` | ``insufficient-data`` ).
          * ``system-status.status`` - The system status of the instance (``ok`` | ``impaired`` | ``initializing`` | ``insufficient-data`` | ``not-applicable`` ).
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
          Constraints: Maximum 100 explicitly specified instance IDs.
          - *(string) --*
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type IncludeAllInstances: boolean
        :param IncludeAllInstances:
          When ``true`` , includes the health status for all instances. When ``false`` , includes the health status for running instances only.
          Default: ``false``
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeInstances(Paginator):
    def paginate(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_instances`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              InstanceIds=[
                  'string',
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Reservations': [
                    {
                        'Groups': [
                            {
                                'GroupName': 'string',
                                'GroupId': 'string'
                            },
                        ],
                        'Instances': [
                            {
                                'AmiLaunchIndex': 123,
                                'ImageId': 'string',
                                'InstanceId': 'string',
                                'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'t3.nano'|'t3.micro'|'t3.small'|'t3.medium'|'t3.large'|'t3.xlarge'|'t3.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.12xlarge'|'r5.24xlarge'|'r5.metal'|'r5a.large'|'r5a.xlarge'|'r5a.2xlarge'|'r5a.4xlarge'|'r5a.12xlarge'|'r5a.24xlarge'|'r5d.large'|'r5d.xlarge'|'r5d.2xlarge'|'r5d.4xlarge'|'r5d.12xlarge'|'r5d.24xlarge'|'r5d.metal'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'i3.metal'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'c5d.large'|'c5d.xlarge'|'c5d.2xlarge'|'c5d.4xlarge'|'c5d.9xlarge'|'c5d.18xlarge'|'c5n.large'|'c5n.xlarge'|'c5n.2xlarge'|'c5n.4xlarge'|'c5n.9xlarge'|'c5n.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'g3s.xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'p3dn.24xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.4xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'m5.metal'|'m5a.large'|'m5a.xlarge'|'m5a.2xlarge'|'m5a.4xlarge'|'m5a.12xlarge'|'m5a.24xlarge'|'m5d.large'|'m5d.xlarge'|'m5d.2xlarge'|'m5d.4xlarge'|'m5d.12xlarge'|'m5d.24xlarge'|'m5d.metal'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge'|'z1d.large'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'z1d.metal'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal'|'a1.medium'|'a1.large'|'a1.xlarge'|'a1.2xlarge'|'a1.4xlarge',
                                'KernelId': 'string',
                                'KeyName': 'string',
                                'LaunchTime': datetime(2015, 1, 1),
                                'Monitoring': {
                                    'State': 'disabled'|'disabling'|'enabled'|'pending'
                                },
                                'Placement': {
                                    'AvailabilityZone': 'string',
                                    'Affinity': 'string',
                                    'GroupName': 'string',
                                    'PartitionNumber': 123,
                                    'HostId': 'string',
                                    'Tenancy': 'default'|'dedicated'|'host',
                                    'SpreadDomain': 'string'
                                },
                                'Platform': 'Windows',
                                'PrivateDnsName': 'string',
                                'PrivateIpAddress': 'string',
                                'ProductCodes': [
                                    {
                                        'ProductCodeId': 'string',
                                        'ProductCodeType': 'devpay'|'marketplace'
                                    },
                                ],
                                'PublicDnsName': 'string',
                                'PublicIpAddress': 'string',
                                'RamdiskId': 'string',
                                'State': {
                                    'Code': 123,
                                    'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
                                },
                                'StateTransitionReason': 'string',
                                'SubnetId': 'string',
                                'VpcId': 'string',
                                'Architecture': 'i386'|'x86_64'|'arm64',
                                'BlockDeviceMappings': [
                                    {
                                        'DeviceName': 'string',
                                        'Ebs': {
                                            'AttachTime': datetime(2015, 1, 1),
                                            'DeleteOnTermination': True|False,
                                            'Status': 'attaching'|'attached'|'detaching'|'detached',
                                            'VolumeId': 'string'
                                        }
                                    },
                                ],
                                'ClientToken': 'string',
                                'EbsOptimized': True|False,
                                'EnaSupport': True|False,
                                'Hypervisor': 'ovm'|'xen',
                                'IamInstanceProfile': {
                                    'Arn': 'string',
                                    'Id': 'string'
                                },
                                'InstanceLifecycle': 'spot'|'scheduled',
                                'ElasticGpuAssociations': [
                                    {
                                        'ElasticGpuId': 'string',
                                        'ElasticGpuAssociationId': 'string',
                                        'ElasticGpuAssociationState': 'string',
                                        'ElasticGpuAssociationTime': 'string'
                                    },
                                ],
                                'ElasticInferenceAcceleratorAssociations': [
                                    {
                                        'ElasticInferenceAcceleratorArn': 'string',
                                        'ElasticInferenceAcceleratorAssociationId': 'string',
                                        'ElasticInferenceAcceleratorAssociationState': 'string',
                                        'ElasticInferenceAcceleratorAssociationTime': datetime(2015, 1, 1)
                                    },
                                ],
                                'NetworkInterfaces': [
                                    {
                                        'Association': {
                                            'IpOwnerId': 'string',
                                            'PublicDnsName': 'string',
                                            'PublicIp': 'string'
                                        },
                                        'Attachment': {
                                            'AttachTime': datetime(2015, 1, 1),
                                            'AttachmentId': 'string',
                                            'DeleteOnTermination': True|False,
                                            'DeviceIndex': 123,
                                            'Status': 'attaching'|'attached'|'detaching'|'detached'
                                        },
                                        'Description': 'string',
                                        'Groups': [
                                            {
                                                'GroupName': 'string',
                                                'GroupId': 'string'
                                            },
                                        ],
                                        'Ipv6Addresses': [
                                            {
                                                'Ipv6Address': 'string'
                                            },
                                        ],
                                        'MacAddress': 'string',
                                        'NetworkInterfaceId': 'string',
                                        'OwnerId': 'string',
                                        'PrivateDnsName': 'string',
                                        'PrivateIpAddress': 'string',
                                        'PrivateIpAddresses': [
                                            {
                                                'Association': {
                                                    'IpOwnerId': 'string',
                                                    'PublicDnsName': 'string',
                                                    'PublicIp': 'string'
                                                },
                                                'Primary': True|False,
                                                'PrivateDnsName': 'string',
                                                'PrivateIpAddress': 'string'
                                            },
                                        ],
                                        'SourceDestCheck': True|False,
                                        'Status': 'available'|'associated'|'attaching'|'in-use'|'detaching',
                                        'SubnetId': 'string',
                                        'VpcId': 'string'
                                    },
                                ],
                                'RootDeviceName': 'string',
                                'RootDeviceType': 'ebs'|'instance-store',
                                'SecurityGroups': [
                                    {
                                        'GroupName': 'string',
                                        'GroupId': 'string'
                                    },
                                ],
                                'SourceDestCheck': True|False,
                                'SpotInstanceRequestId': 'string',
                                'SriovNetSupport': 'string',
                                'StateReason': {
                                    'Code': 'string',
                                    'Message': 'string'
                                },
                                'Tags': [
                                    {
                                        'Key': 'string',
                                        'Value': 'string'
                                    },
                                ],
                                'VirtualizationType': 'hvm'|'paravirtual',
                                'CpuOptions': {
                                    'CoreCount': 123,
                                    'ThreadsPerCore': 123
                                },
                                'CapacityReservationId': 'string',
                                'CapacityReservationSpecification': {
                                    'CapacityReservationPreference': 'open'|'none',
                                    'CapacityReservationTarget': {
                                        'CapacityReservationId': 'string'
                                    }
                                },
                                'HibernationOptions': {
                                    'Configured': True|False
                                },
                                'Licenses': [
                                    {
                                        'LicenseConfigurationArn': 'string'
                                    },
                                ]
                            },
                        ],
                        'OwnerId': 'string',
                        'RequesterId': 'string',
                        'ReservationId': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Reservations** *(list) --* 
              Zero or more reservations.
              - *(dict) --* 
                Describes a reservation.
                - **Groups** *(list) --* 
                  [EC2-Classic only] One or more security groups.
                  - *(dict) --* 
                    Describes a security group.
                    - **GroupName** *(string) --* 
                      The name of the security group.
                    - **GroupId** *(string) --* 
                      The ID of the security group.
                - **Instances** *(list) --* 
                  One or more instances.
                  - *(dict) --* 
                    Describes an instance.
                    - **AmiLaunchIndex** *(integer) --* 
                      The AMI launch index, which can be used to find this instance in the launch group.
                    - **ImageId** *(string) --* 
                      The ID of the AMI used to launch the instance.
                    - **InstanceId** *(string) --* 
                      The ID of the instance.
                    - **InstanceType** *(string) --* 
                      The instance type.
                    - **KernelId** *(string) --* 
                      The kernel associated with this instance, if applicable.
                    - **KeyName** *(string) --* 
                      The name of the key pair, if this instance was launched with an associated key pair.
                    - **LaunchTime** *(datetime) --* 
                      The time the instance was launched.
                    - **Monitoring** *(dict) --* 
                      The monitoring for the instance.
                      - **State** *(string) --* 
                        Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
                    - **Placement** *(dict) --* 
                      The location where the instance launched, if applicable.
                      - **AvailabilityZone** *(string) --* 
                        The Availability Zone of the instance.
                      - **Affinity** *(string) --* 
                        The affinity setting for the instance on the Dedicated Host. This parameter is not supported for the  ImportInstance command.
                      - **GroupName** *(string) --* 
                        The name of the placement group the instance is in.
                      - **PartitionNumber** *(integer) --* 
                        The number of the partition the instance is in. Valid only if the placement group strategy is set to ``partition`` .
                      - **HostId** *(string) --* 
                        The ID of the Dedicated Host on which the instance resides. This parameter is not supported for the  ImportInstance command.
                      - **Tenancy** *(string) --* 
                        The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of ``dedicated`` runs on single-tenant hardware. The ``host`` tenancy is not supported for the  ImportInstance command.
                      - **SpreadDomain** *(string) --* 
                        Reserved for future use.
                    - **Platform** *(string) --* 
                      The value is ``Windows`` for Windows instances; otherwise blank.
                    - **PrivateDnsName** *(string) --* 
                      (IPv4 only) The private DNS hostname name assigned to the instance. This DNS hostname can only be used inside the Amazon EC2 network. This name is not available until the instance enters the ``running`` state. 
                      [EC2-VPC] The Amazon-provided DNS server resolves Amazon-provided private DNS hostnames if you've enabled DNS resolution and DNS hostnames in your VPC. If you are not using the Amazon-provided DNS server in your VPC, your custom domain name servers must resolve the hostname as appropriate.
                    - **PrivateIpAddress** *(string) --* 
                      The private IPv4 address assigned to the instance.
                    - **ProductCodes** *(list) --* 
                      The product codes attached to this instance, if applicable.
                      - *(dict) --* 
                        Describes a product code.
                        - **ProductCodeId** *(string) --* 
                          The product code.
                        - **ProductCodeType** *(string) --* 
                          The type of product code.
                    - **PublicDnsName** *(string) --* 
                      (IPv4 only) The public DNS name assigned to the instance. This name is not available until the instance enters the ``running`` state. For EC2-VPC, this name is only available if you've enabled DNS hostnames for your VPC.
                    - **PublicIpAddress** *(string) --* 
                      The public IPv4 address assigned to the instance, if applicable.
                    - **RamdiskId** *(string) --* 
                      The RAM disk associated with this instance, if applicable.
                    - **State** *(dict) --* 
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
                    - **StateTransitionReason** *(string) --* 
                      The reason for the most recent state transition. This might be an empty string.
                    - **SubnetId** *(string) --* 
                      [EC2-VPC] The ID of the subnet in which the instance is running.
                    - **VpcId** *(string) --* 
                      [EC2-VPC] The ID of the VPC in which the instance is running.
                    - **Architecture** *(string) --* 
                      The architecture of the image.
                    - **BlockDeviceMappings** *(list) --* 
                      Any block device mapping entries for the instance.
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
                    - **ClientToken** *(string) --* 
                      The idempotency token you provided when you launched the instance, if applicable.
                    - **EbsOptimized** *(boolean) --* 
                      Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.
                    - **EnaSupport** *(boolean) --* 
                      Specifies whether enhanced networking with ENA is enabled.
                    - **Hypervisor** *(string) --* 
                      The hypervisor type of the instance.
                    - **IamInstanceProfile** *(dict) --* 
                      The IAM instance profile associated with the instance, if applicable.
                      - **Arn** *(string) --* 
                        The Amazon Resource Name (ARN) of the instance profile.
                      - **Id** *(string) --* 
                        The ID of the instance profile.
                    - **InstanceLifecycle** *(string) --* 
                      Indicates whether this is a Spot Instance or a Scheduled Instance.
                    - **ElasticGpuAssociations** *(list) --* 
                      The Elastic GPU associated with the instance.
                      - *(dict) --* 
                        Describes the association between an instance and an Elastic Graphics accelerator.
                        - **ElasticGpuId** *(string) --* 
                          The ID of the Elastic Graphics accelerator.
                        - **ElasticGpuAssociationId** *(string) --* 
                          The ID of the association.
                        - **ElasticGpuAssociationState** *(string) --* 
                          The state of the association between the instance and the Elastic Graphics accelerator.
                        - **ElasticGpuAssociationTime** *(string) --* 
                          The time the Elastic Graphics accelerator was associated with the instance.
                    - **ElasticInferenceAcceleratorAssociations** *(list) --* 
                      The elastic inference accelerator associated with the instance. 
                      - *(dict) --* 
                        Describes the association between an instance and an elastic inference accelerator. 
                        - **ElasticInferenceAcceleratorArn** *(string) --* 
                          The Amazon Resource Name (ARN) of the elastic inference accelerator. 
                        - **ElasticInferenceAcceleratorAssociationId** *(string) --* 
                          The ID of the association. 
                        - **ElasticInferenceAcceleratorAssociationState** *(string) --* 
                          The state of the elastic inference accelerator. 
                        - **ElasticInferenceAcceleratorAssociationTime** *(datetime) --* 
                          The time at which the elastic inference accelerator is associated with an instance. 
                    - **NetworkInterfaces** *(list) --* 
                      [EC2-VPC] One or more network interfaces for the instance.
                      - *(dict) --* 
                        Describes a network interface.
                        - **Association** *(dict) --* 
                          The association information for an Elastic IPv4 associated with the network interface.
                          - **IpOwnerId** *(string) --* 
                            The ID of the owner of the Elastic IP address.
                          - **PublicDnsName** *(string) --* 
                            The public DNS name.
                          - **PublicIp** *(string) --* 
                            The public IP address or Elastic IP address bound to the network interface.
                        - **Attachment** *(dict) --* 
                          The network interface attachment.
                          - **AttachTime** *(datetime) --* 
                            The time stamp when the attachment initiated.
                          - **AttachmentId** *(string) --* 
                            The ID of the network interface attachment.
                          - **DeleteOnTermination** *(boolean) --* 
                            Indicates whether the network interface is deleted when the instance is terminated.
                          - **DeviceIndex** *(integer) --* 
                            The index of the device on the instance for the network interface attachment.
                          - **Status** *(string) --* 
                            The attachment state.
                        - **Description** *(string) --* 
                          The description.
                        - **Groups** *(list) --* 
                          One or more security groups.
                          - *(dict) --* 
                            Describes a security group.
                            - **GroupName** *(string) --* 
                              The name of the security group.
                            - **GroupId** *(string) --* 
                              The ID of the security group.
                        - **Ipv6Addresses** *(list) --* 
                          One or more IPv6 addresses associated with the network interface.
                          - *(dict) --* 
                            Describes an IPv6 address.
                            - **Ipv6Address** *(string) --* 
                              The IPv6 address.
                        - **MacAddress** *(string) --* 
                          The MAC address.
                        - **NetworkInterfaceId** *(string) --* 
                          The ID of the network interface.
                        - **OwnerId** *(string) --* 
                          The ID of the AWS account that created the network interface.
                        - **PrivateDnsName** *(string) --* 
                          The private DNS name.
                        - **PrivateIpAddress** *(string) --* 
                          The IPv4 address of the network interface within the subnet.
                        - **PrivateIpAddresses** *(list) --* 
                          One or more private IPv4 addresses associated with the network interface.
                          - *(dict) --* 
                            Describes a private IPv4 address.
                            - **Association** *(dict) --* 
                              The association information for an Elastic IP address for the network interface.
                              - **IpOwnerId** *(string) --* 
                                The ID of the owner of the Elastic IP address.
                              - **PublicDnsName** *(string) --* 
                                The public DNS name.
                              - **PublicIp** *(string) --* 
                                The public IP address or Elastic IP address bound to the network interface.
                            - **Primary** *(boolean) --* 
                              Indicates whether this IPv4 address is the primary private IP address of the network interface.
                            - **PrivateDnsName** *(string) --* 
                              The private IPv4 DNS name.
                            - **PrivateIpAddress** *(string) --* 
                              The private IPv4 address of the network interface.
                        - **SourceDestCheck** *(boolean) --* 
                          Indicates whether to validate network traffic to or from this network interface.
                        - **Status** *(string) --* 
                          The status of the network interface.
                        - **SubnetId** *(string) --* 
                          The ID of the subnet.
                        - **VpcId** *(string) --* 
                          The ID of the VPC.
                    - **RootDeviceName** *(string) --* 
                      The device name of the root device volume (for example, ``/dev/sda1`` ).
                    - **RootDeviceType** *(string) --* 
                      The root device type used by the AMI. The AMI can use an EBS volume or an instance store volume.
                    - **SecurityGroups** *(list) --* 
                      One or more security groups for the instance.
                      - *(dict) --* 
                        Describes a security group.
                        - **GroupName** *(string) --* 
                          The name of the security group.
                        - **GroupId** *(string) --* 
                          The ID of the security group.
                    - **SourceDestCheck** *(boolean) --* 
                      Specifies whether to enable an instance launched in a VPC to perform NAT. This controls whether source/destination checking is enabled on the instance. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the instance to perform NAT. For more information, see `NAT Instances <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
                    - **SpotInstanceRequestId** *(string) --* 
                      If the request is a Spot Instance request, the ID of the request.
                    - **SriovNetSupport** *(string) --* 
                      Specifies whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.
                    - **StateReason** *(dict) --* 
                      The reason for the most recent state transition.
                      - **Code** *(string) --* 
                        The reason code for the state change.
                      - **Message** *(string) --* 
                        The message for the state change.
                        * ``Server.InsufficientInstanceCapacity`` : There was insufficient capacity available to satisfy the launch request. 
                        * ``Server.InternalError`` : An internal error caused the instance to terminate during launch. 
                        * ``Server.ScheduledStop`` : The instance was stopped due to a scheduled retirement. 
                        * ``Server.SpotInstanceShutdown`` : The instance was stopped because the number of Spot requests with a maximum price equal to or higher than the Spot price exceeded available capacity or because of an increase in the Spot price. 
                        * ``Server.SpotInstanceTermination`` : The instance was terminated because the number of Spot requests with a maximum price equal to or higher than the Spot price exceeded available capacity or because of an increase in the Spot price. 
                        * ``Client.InstanceInitiatedShutdown`` : The instance was shut down using the ``shutdown -h`` command from the instance. 
                        * ``Client.InstanceTerminated`` : The instance was terminated or rebooted during AMI creation. 
                        * ``Client.InternalError`` : A client error caused the instance to terminate during launch. 
                        * ``Client.InvalidSnapshot.NotFound`` : The specified snapshot was not found. 
                        * ``Client.UserInitiatedHibernate`` : Hibernation was initiated on the instance. 
                        * ``Client.UserInitiatedShutdown`` : The instance was shut down using the Amazon EC2 API. 
                        * ``Client.VolumeLimitExceeded`` : The limit on the number of EBS volumes or total storage was exceeded. Decrease usage or request an increase in your account limits. 
                    - **Tags** *(list) --* 
                      Any tags assigned to the instance.
                      - *(dict) --* 
                        Describes a tag.
                        - **Key** *(string) --* 
                          The key of the tag.
                          Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                        - **Value** *(string) --* 
                          The value of the tag.
                          Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
                    - **VirtualizationType** *(string) --* 
                      The virtualization type of the instance.
                    - **CpuOptions** *(dict) --* 
                      The CPU options for the instance.
                      - **CoreCount** *(integer) --* 
                        The number of CPU cores for the instance.
                      - **ThreadsPerCore** *(integer) --* 
                        The number of threads per CPU core.
                    - **CapacityReservationId** *(string) --* 
                      The ID of the Capacity Reservation.
                    - **CapacityReservationSpecification** *(dict) --* 
                      Information about the Capacity Reservation targeting option.
                      - **CapacityReservationPreference** *(string) --* 
                        Describes the instance's Capacity Reservation preferences. Possible preferences include:
                        * ``open`` - The instance can run in any ``open`` Capacity Reservation that has matching attributes (instance type, platform, Availability Zone). 
                        * ``none`` - The instance avoids running in a Capacity Reservation even if one is available. The instance runs in On-Demand capacity. 
                      - **CapacityReservationTarget** *(dict) --* 
                        Information about the targeted Capacity Reservation.
                        - **CapacityReservationId** *(string) --* 
                          The ID of the Capacity Reservation.
                    - **HibernationOptions** *(dict) --* 
                      Indicates whether the instance is enabled for hibernation.
                      - **Configured** *(boolean) --* 
                        If this parameter is set to ``true`` , your instance is enabled for hibernation; otherwise, it is not enabled for hibernation.
                    - **Licenses** *(list) --* 
                      The license configurations.
                      - *(dict) --* 
                        Describes a license configuration.
                        - **LicenseConfigurationArn** *(string) --* 
                          The Amazon Resource Name (ARN) of the license configuration.
                - **OwnerId** *(string) --* 
                  The ID of the AWS account that owns the reservation.
                - **RequesterId** *(string) --* 
                  The ID of the requester that launched the instances on your behalf (for example, AWS Management Console or Auto Scaling).
                - **ReservationId** *(string) --* 
                  The ID of the reservation.
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
          * ``hibernation-options.configured`` - A Boolean that indicates whether the instance is enabled for hibernation. A value of ``true`` means that the instance is enabled for hibernation.
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
          * ``placement-partition-number`` - The partition in which the instance is located.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeLaunchTemplateVersions(Paginator):
    def paginate(self, DryRun: bool = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None, Versions: List = None, MinVersion: str = None, MaxVersion: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_launch_template_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeLaunchTemplateVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              LaunchTemplateId='string',
              LaunchTemplateName='string',
              Versions=[
                  'string',
              ],
              MinVersion='string',
              MaxVersion='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'LaunchTemplateVersions': [
                    {
                        'LaunchTemplateId': 'string',
                        'LaunchTemplateName': 'string',
                        'VersionNumber': 123,
                        'VersionDescription': 'string',
                        'CreateTime': datetime(2015, 1, 1),
                        'CreatedBy': 'string',
                        'DefaultVersion': True|False,
                        'LaunchTemplateData': {
                            'KernelId': 'string',
                            'EbsOptimized': True|False,
                            'IamInstanceProfile': {
                                'Arn': 'string',
                                'Name': 'string'
                            },
                            'BlockDeviceMappings': [
                                {
                                    'DeviceName': 'string',
                                    'VirtualName': 'string',
                                    'Ebs': {
                                        'Encrypted': True|False,
                                        'DeleteOnTermination': True|False,
                                        'Iops': 123,
                                        'KmsKeyId': 'string',
                                        'SnapshotId': 'string',
                                        'VolumeSize': 123,
                                        'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1'
                                    },
                                    'NoDevice': 'string'
                                },
                            ],
                            'NetworkInterfaces': [
                                {
                                    'AssociatePublicIpAddress': True|False,
                                    'DeleteOnTermination': True|False,
                                    'Description': 'string',
                                    'DeviceIndex': 123,
                                    'Groups': [
                                        'string',
                                    ],
                                    'Ipv6AddressCount': 123,
                                    'Ipv6Addresses': [
                                        {
                                            'Ipv6Address': 'string'
                                        },
                                    ],
                                    'NetworkInterfaceId': 'string',
                                    'PrivateIpAddress': 'string',
                                    'PrivateIpAddresses': [
                                        {
                                            'Primary': True|False,
                                            'PrivateIpAddress': 'string'
                                        },
                                    ],
                                    'SecondaryPrivateIpAddressCount': 123,
                                    'SubnetId': 'string'
                                },
                            ],
                            'ImageId': 'string',
                            'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'t3.nano'|'t3.micro'|'t3.small'|'t3.medium'|'t3.large'|'t3.xlarge'|'t3.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.12xlarge'|'r5.24xlarge'|'r5.metal'|'r5a.large'|'r5a.xlarge'|'r5a.2xlarge'|'r5a.4xlarge'|'r5a.12xlarge'|'r5a.24xlarge'|'r5d.large'|'r5d.xlarge'|'r5d.2xlarge'|'r5d.4xlarge'|'r5d.12xlarge'|'r5d.24xlarge'|'r5d.metal'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'i3.metal'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'c5d.large'|'c5d.xlarge'|'c5d.2xlarge'|'c5d.4xlarge'|'c5d.9xlarge'|'c5d.18xlarge'|'c5n.large'|'c5n.xlarge'|'c5n.2xlarge'|'c5n.4xlarge'|'c5n.9xlarge'|'c5n.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'g3s.xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'p3dn.24xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.4xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'m5.metal'|'m5a.large'|'m5a.xlarge'|'m5a.2xlarge'|'m5a.4xlarge'|'m5a.12xlarge'|'m5a.24xlarge'|'m5d.large'|'m5d.xlarge'|'m5d.2xlarge'|'m5d.4xlarge'|'m5d.12xlarge'|'m5d.24xlarge'|'m5d.metal'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge'|'z1d.large'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'z1d.metal'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal'|'a1.medium'|'a1.large'|'a1.xlarge'|'a1.2xlarge'|'a1.4xlarge',
                            'KeyName': 'string',
                            'Monitoring': {
                                'Enabled': True|False
                            },
                            'Placement': {
                                'AvailabilityZone': 'string',
                                'Affinity': 'string',
                                'GroupName': 'string',
                                'HostId': 'string',
                                'Tenancy': 'default'|'dedicated'|'host',
                                'SpreadDomain': 'string'
                            },
                            'RamDiskId': 'string',
                            'DisableApiTermination': True|False,
                            'InstanceInitiatedShutdownBehavior': 'stop'|'terminate',
                            'UserData': 'string',
                            'TagSpecifications': [
                                {
                                    'ResourceType': 'client-vpn-endpoint'|'customer-gateway'|'dedicated-host'|'dhcp-options'|'elastic-ip'|'fleet'|'fpga-image'|'image'|'instance'|'internet-gateway'|'launch-template'|'natgateway'|'network-acl'|'network-interface'|'reserved-instances'|'route-table'|'security-group'|'snapshot'|'spot-instances-request'|'subnet'|'transit-gateway'|'transit-gateway-attachment'|'transit-gateway-route-table'|'volume'|'vpc'|'vpc-peering-connection'|'vpn-connection'|'vpn-gateway',
                                    'Tags': [
                                        {
                                            'Key': 'string',
                                            'Value': 'string'
                                        },
                                    ]
                                },
                            ],
                            'ElasticGpuSpecifications': [
                                {
                                    'Type': 'string'
                                },
                            ],
                            'ElasticInferenceAccelerators': [
                                {
                                    'Type': 'string'
                                },
                            ],
                            'SecurityGroupIds': [
                                'string',
                            ],
                            'SecurityGroups': [
                                'string',
                            ],
                            'InstanceMarketOptions': {
                                'MarketType': 'spot',
                                'SpotOptions': {
                                    'MaxPrice': 'string',
                                    'SpotInstanceType': 'one-time'|'persistent',
                                    'BlockDurationMinutes': 123,
                                    'ValidUntil': datetime(2015, 1, 1),
                                    'InstanceInterruptionBehavior': 'hibernate'|'stop'|'terminate'
                                }
                            },
                            'CreditSpecification': {
                                'CpuCredits': 'string'
                            },
                            'CpuOptions': {
                                'CoreCount': 123,
                                'ThreadsPerCore': 123
                            },
                            'CapacityReservationSpecification': {
                                'CapacityReservationPreference': 'open'|'none',
                                'CapacityReservationTarget': {
                                    'CapacityReservationId': 'string'
                                }
                            },
                            'HibernationOptions': {
                                'Configured': True|False
                            },
                            'LicenseSpecifications': [
                                {
                                    'LicenseConfigurationArn': 'string'
                                },
                            ]
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LaunchTemplateVersions** *(list) --* 
              Information about the launch template versions.
              - *(dict) --* 
                Describes a launch template version.
                - **LaunchTemplateId** *(string) --* 
                  The ID of the launch template.
                - **LaunchTemplateName** *(string) --* 
                  The name of the launch template.
                - **VersionNumber** *(integer) --* 
                  The version number.
                - **VersionDescription** *(string) --* 
                  The description for the version.
                - **CreateTime** *(datetime) --* 
                  The time the version was created.
                - **CreatedBy** *(string) --* 
                  The principal that created the version.
                - **DefaultVersion** *(boolean) --* 
                  Indicates whether the version is the default version.
                - **LaunchTemplateData** *(dict) --* 
                  Information about the launch template.
                  - **KernelId** *(string) --* 
                    The ID of the kernel, if applicable.
                  - **EbsOptimized** *(boolean) --* 
                    Indicates whether the instance is optimized for Amazon EBS I/O. 
                  - **IamInstanceProfile** *(dict) --* 
                    The IAM instance profile.
                    - **Arn** *(string) --* 
                      The Amazon Resource Name (ARN) of the instance profile.
                    - **Name** *(string) --* 
                      The name of the instance profile.
                  - **BlockDeviceMappings** *(list) --* 
                    The block device mappings.
                    - *(dict) --* 
                      Describes a block device mapping.
                      - **DeviceName** *(string) --* 
                        The device name.
                      - **VirtualName** *(string) --* 
                        The virtual device name (ephemeralN).
                      - **Ebs** *(dict) --* 
                        Information about the block device for an EBS volume.
                        - **Encrypted** *(boolean) --* 
                          Indicates whether the EBS volume is encrypted.
                        - **DeleteOnTermination** *(boolean) --* 
                          Indicates whether the EBS volume is deleted on instance termination.
                        - **Iops** *(integer) --* 
                          The number of I/O operations per second (IOPS) that the volume supports. 
                        - **KmsKeyId** *(string) --* 
                          The ARN of the AWS Key Management Service (AWS KMS) CMK used for encryption.
                        - **SnapshotId** *(string) --* 
                          The ID of the snapshot.
                        - **VolumeSize** *(integer) --* 
                          The size of the volume, in GiB.
                        - **VolumeType** *(string) --* 
                          The volume type.
                      - **NoDevice** *(string) --* 
                        Suppresses the specified device included in the block device mapping of the AMI.
                  - **NetworkInterfaces** *(list) --* 
                    The network interfaces.
                    - *(dict) --* 
                      Describes a network interface.
                      - **AssociatePublicIpAddress** *(boolean) --* 
                        Indicates whether to associate a public IPv4 address with eth0 for a new network interface.
                      - **DeleteOnTermination** *(boolean) --* 
                        Indicates whether the network interface is deleted when the instance is terminated.
                      - **Description** *(string) --* 
                        A description for the network interface.
                      - **DeviceIndex** *(integer) --* 
                        The device index for the network interface attachment.
                      - **Groups** *(list) --* 
                        The IDs of one or more security groups.
                        - *(string) --* 
                      - **Ipv6AddressCount** *(integer) --* 
                        The number of IPv6 addresses for the network interface.
                      - **Ipv6Addresses** *(list) --* 
                        The IPv6 addresses for the network interface.
                        - *(dict) --* 
                          Describes an IPv6 address.
                          - **Ipv6Address** *(string) --* 
                            The IPv6 address.
                      - **NetworkInterfaceId** *(string) --* 
                        The ID of the network interface.
                      - **PrivateIpAddress** *(string) --* 
                        The primary private IPv4 address of the network interface.
                      - **PrivateIpAddresses** *(list) --* 
                        One or more private IPv4 addresses.
                        - *(dict) --* 
                          Describes a secondary private IPv4 address for a network interface.
                          - **Primary** *(boolean) --* 
                            Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.
                          - **PrivateIpAddress** *(string) --* 
                            The private IPv4 addresses.
                      - **SecondaryPrivateIpAddressCount** *(integer) --* 
                        The number of secondary private IPv4 addresses for the network interface.
                      - **SubnetId** *(string) --* 
                        The ID of the subnet for the network interface.
                  - **ImageId** *(string) --* 
                    The ID of the AMI that was used to launch the instance.
                  - **InstanceType** *(string) --* 
                    The instance type.
                  - **KeyName** *(string) --* 
                    The name of the key pair.
                  - **Monitoring** *(dict) --* 
                    The monitoring for the instance.
                    - **Enabled** *(boolean) --* 
                      Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
                  - **Placement** *(dict) --* 
                    The placement of the instance.
                    - **AvailabilityZone** *(string) --* 
                      The Availability Zone of the instance.
                    - **Affinity** *(string) --* 
                      The affinity setting for the instance on the Dedicated Host.
                    - **GroupName** *(string) --* 
                      The name of the placement group for the instance.
                    - **HostId** *(string) --* 
                      The ID of the Dedicated Host for the instance.
                    - **Tenancy** *(string) --* 
                      The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of ``dedicated`` runs on single-tenant hardware. 
                    - **SpreadDomain** *(string) --* 
                      Reserved for future use.
                  - **RamDiskId** *(string) --* 
                    The ID of the RAM disk, if applicable.
                  - **DisableApiTermination** *(boolean) --* 
                    If set to ``true`` , indicates that the instance cannot be terminated using the Amazon EC2 console, command line tool, or API.
                  - **InstanceInitiatedShutdownBehavior** *(string) --* 
                    Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
                  - **UserData** *(string) --* 
                    The user data for the instance. 
                  - **TagSpecifications** *(list) --* 
                    The tags.
                    - *(dict) --* 
                      The tag specification for the launch template.
                      - **ResourceType** *(string) --* 
                        The type of resource.
                      - **Tags** *(list) --* 
                        The tags for the resource.
                        - *(dict) --* 
                          Describes a tag.
                          - **Key** *(string) --* 
                            The key of the tag.
                            Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                          - **Value** *(string) --* 
                            The value of the tag.
                            Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
                  - **ElasticGpuSpecifications** *(list) --* 
                    The elastic GPU specification.
                    - *(dict) --* 
                      Describes an elastic GPU.
                      - **Type** *(string) --* 
                        The elastic GPU type.
                  - **ElasticInferenceAccelerators** *(list) --* 
                    The elastic inference accelerator for the instance. 
                    - *(dict) --* 
                      Describes an elastic inference accelerator. 
                      - **Type** *(string) --* 
                        The type of elastic inference accelerator. The possible values are eia1.medium, eia1.large, and eia1.xlarge. 
                  - **SecurityGroupIds** *(list) --* 
                    The security group IDs.
                    - *(string) --* 
                  - **SecurityGroups** *(list) --* 
                    The security group names.
                    - *(string) --* 
                  - **InstanceMarketOptions** *(dict) --* 
                    The market (purchasing) option for the instances.
                    - **MarketType** *(string) --* 
                      The market type.
                    - **SpotOptions** *(dict) --* 
                      The options for Spot Instances.
                      - **MaxPrice** *(string) --* 
                        The maximum hourly price you're willing to pay for the Spot Instances.
                      - **SpotInstanceType** *(string) --* 
                        The Spot Instance request type.
                      - **BlockDurationMinutes** *(integer) --* 
                        The required duration for the Spot Instances (also known as Spot blocks), in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).
                      - **ValidUntil** *(datetime) --* 
                        The end date of the request. For a one-time request, the request remains active until all instances launch, the request is canceled, or this date is reached. If the request is persistent, it remains active until it is canceled or this date and time is reached.
                      - **InstanceInterruptionBehavior** *(string) --* 
                        The behavior when a Spot Instance is interrupted.
                  - **CreditSpecification** *(dict) --* 
                    The credit option for CPU usage of the instance.
                    - **CpuCredits** *(string) --* 
                      The credit option for CPU usage of a T2 or T3 instance. Valid values are ``standard`` and ``unlimited`` .
                  - **CpuOptions** *(dict) --* 
                    The CPU options for the instance. For more information, see `Optimizing CPU Options <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
                    - **CoreCount** *(integer) --* 
                      The number of CPU cores for the instance.
                    - **ThreadsPerCore** *(integer) --* 
                      The number of threads per CPU core.
                  - **CapacityReservationSpecification** *(dict) --* 
                    Information about the Capacity Reservation targeting option.
                    - **CapacityReservationPreference** *(string) --* 
                      Indicates the instance's Capacity Reservation preferences. Possible preferences include:
                      * ``open`` - The instance can run in any ``open`` Capacity Reservation that has matching attributes (instance type, platform, Availability Zone). 
                      * ``none`` - The instance avoids running in a Capacity Reservation even if one is available. The instance runs in On-Demand capacity. 
                    - **CapacityReservationTarget** *(dict) --* 
                      Information about the target Capacity Reservation.
                      - **CapacityReservationId** *(string) --* 
                        The ID of the Capacity Reservation.
                  - **HibernationOptions** *(dict) --* 
                    Indicates whether an instance is configured for hibernation. For more information, see `Hibernate Your Instance <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
                    - **Configured** *(boolean) --* 
                      If this parameter is set to ``true`` , the instance is enabled for hibernation; otherwise, it is not enabled for hibernation.
                  - **LicenseSpecifications** *(list) --* 
                    The license configurations.
                    - *(dict) --* 
                      Describes a license configuration.
                      - **LicenseConfigurationArn** *(string) --* 
                        The Amazon Resource Name (ARN) of the license configuration.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type LaunchTemplateId: string
        :param LaunchTemplateId:
          The ID of the launch template. You must specify either the launch template ID or launch template name in the request.
        :type LaunchTemplateName: string
        :param LaunchTemplateName:
          The name of the launch template. You must specify either the launch template ID or launch template name in the request.
        :type Versions: list
        :param Versions:
          One or more versions of the launch template.
          - *(string) --*
        :type MinVersion: string
        :param MinVersion:
          The version number after which to describe launch template versions.
        :type MaxVersion: string
        :param MaxVersion:
          The version number up to which to describe launch template versions.
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``create-time`` - The time the launch template version was created.
          * ``ebs-optimized`` - A boolean that indicates whether the instance is optimized for Amazon EBS I/O.
          * ``iam-instance-profile`` - The ARN of the IAM instance profile.
          * ``image-id`` - The ID of the AMI.
          * ``instance-type`` - The instance type.
          * ``is-default-version`` - A boolean that indicates whether the launch template version is the default version.
          * ``kernel-id`` - The kernel ID.
          * ``ram-disk-id`` - The RAM disk ID.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeLaunchTemplates(Paginator):
    def paginate(self, DryRun: bool = None, LaunchTemplateIds: List = None, LaunchTemplateNames: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_launch_templates`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeLaunchTemplates>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              LaunchTemplateIds=[
                  'string',
              ],
              LaunchTemplateNames=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'LaunchTemplates': [
                    {
                        'LaunchTemplateId': 'string',
                        'LaunchTemplateName': 'string',
                        'CreateTime': datetime(2015, 1, 1),
                        'CreatedBy': 'string',
                        'DefaultVersionNumber': 123,
                        'LatestVersionNumber': 123,
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LaunchTemplates** *(list) --* 
              Information about the launch templates.
              - *(dict) --* 
                Describes a launch template.
                - **LaunchTemplateId** *(string) --* 
                  The ID of the launch template.
                - **LaunchTemplateName** *(string) --* 
                  The name of the launch template.
                - **CreateTime** *(datetime) --* 
                  The time launch template was created.
                - **CreatedBy** *(string) --* 
                  The principal that created the launch template. 
                - **DefaultVersionNumber** *(integer) --* 
                  The version number of the default version of the launch template.
                - **LatestVersionNumber** *(integer) --* 
                  The version number of the latest version of the launch template.
                - **Tags** *(list) --* 
                  The tags for the launch template.
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
        :type LaunchTemplateIds: list
        :param LaunchTemplateIds:
          One or more launch template IDs.
          - *(string) --*
        :type LaunchTemplateNames: list
        :param LaunchTemplateNames:
          One or more launch template names.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``create-time`` - The time the launch template was created.
          * ``launch-template-name`` - The name of the launch template.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeMovingAddresses(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, PublicIps: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_moving_addresses`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeMovingAddresses>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              PublicIps=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'MovingAddressStatuses': [
                    {
                        'MoveStatus': 'movingToVpc'|'restoringToClassic',
                        'PublicIp': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **MovingAddressStatuses** *(list) --* 
              The status for each Elastic IP address.
              - *(dict) --* 
                Describes the status of a moving Elastic IP address.
                - **MoveStatus** *(string) --* 
                  The status of the Elastic IP address that's being moved to the EC2-VPC platform, or restored to the EC2-Classic platform.
                - **PublicIp** *(string) --* 
                  The Elastic IP address.
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``moving-status`` - The status of the Elastic IP address (``MovingToVpc`` | ``RestoringToClassic`` ).
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
        :type PublicIps: list
        :param PublicIps:
          One or more Elastic IP addresses.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeNatGateways(Paginator):
    def paginate(self, Filters: List = None, NatGatewayIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_nat_gateways`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNatGateways>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              NatGatewayIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'NatGateways': [
                    {
                        'CreateTime': datetime(2015, 1, 1),
                        'DeleteTime': datetime(2015, 1, 1),
                        'FailureCode': 'string',
                        'FailureMessage': 'string',
                        'NatGatewayAddresses': [
                            {
                                'AllocationId': 'string',
                                'NetworkInterfaceId': 'string',
                                'PrivateIp': 'string',
                                'PublicIp': 'string'
                            },
                        ],
                        'NatGatewayId': 'string',
                        'ProvisionedBandwidth': {
                            'ProvisionTime': datetime(2015, 1, 1),
                            'Provisioned': 'string',
                            'RequestTime': datetime(2015, 1, 1),
                            'Requested': 'string',
                            'Status': 'string'
                        },
                        'State': 'pending'|'failed'|'available'|'deleting'|'deleted',
                        'SubnetId': 'string',
                        'VpcId': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NatGateways** *(list) --* 
              Information about the NAT gateways.
              - *(dict) --* 
                Describes a NAT gateway.
                - **CreateTime** *(datetime) --* 
                  The date and time the NAT gateway was created.
                - **DeleteTime** *(datetime) --* 
                  The date and time the NAT gateway was deleted, if applicable.
                - **FailureCode** *(string) --* 
                  If the NAT gateway could not be created, specifies the error code for the failure. (``InsufficientFreeAddressesInSubnet`` | ``Gateway.NotAttached`` | ``InvalidAllocationID.NotFound`` | ``Resource.AlreadyAssociated`` | ``InternalError`` | ``InvalidSubnetID.NotFound`` )
                - **FailureMessage** *(string) --* 
                  If the NAT gateway could not be created, specifies the error message for the failure, that corresponds to the error code.
                  * For InsufficientFreeAddressesInSubnet: "Subnet has insufficient free addresses to create this NAT gateway" 
                  * For Gateway.NotAttached: "Network vpc-xxxxxxxx has no Internet gateway attached" 
                  * For InvalidAllocationID.NotFound: "Elastic IP address eipalloc-xxxxxxxx could not be associated with this NAT gateway" 
                  * For Resource.AlreadyAssociated: "Elastic IP address eipalloc-xxxxxxxx is already associated" 
                  * For InternalError: "Network interface eni-xxxxxxxx, created and used internally by this NAT gateway is in an invalid state. Please try again." 
                  * For InvalidSubnetID.NotFound: "The specified subnet subnet-xxxxxxxx does not exist or could not be found." 
                - **NatGatewayAddresses** *(list) --* 
                  Information about the IP addresses and network interface associated with the NAT gateway.
                  - *(dict) --* 
                    Describes the IP addresses and network interface associated with a NAT gateway.
                    - **AllocationId** *(string) --* 
                      The allocation ID of the Elastic IP address that's associated with the NAT gateway.
                    - **NetworkInterfaceId** *(string) --* 
                      The ID of the network interface associated with the NAT gateway.
                    - **PrivateIp** *(string) --* 
                      The private IP address associated with the Elastic IP address.
                    - **PublicIp** *(string) --* 
                      The Elastic IP address associated with the NAT gateway.
                - **NatGatewayId** *(string) --* 
                  The ID of the NAT gateway.
                - **ProvisionedBandwidth** *(dict) --* 
                  Reserved. If you need to sustain traffic greater than the `documented limits <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html>`__ , contact us through the `Support Center <https://console.aws.amazon.com/support/home?>`__ .
                  - **ProvisionTime** *(datetime) --* 
                    Reserved. If you need to sustain traffic greater than the `documented limits <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html>`__ , contact us through the `Support Center <https://console.aws.amazon.com/support/home?>`__ .
                  - **Provisioned** *(string) --* 
                    Reserved. If you need to sustain traffic greater than the `documented limits <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html>`__ , contact us through the `Support Center <https://console.aws.amazon.com/support/home?>`__ .
                  - **RequestTime** *(datetime) --* 
                    Reserved. If you need to sustain traffic greater than the `documented limits <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html>`__ , contact us through the `Support Center <https://console.aws.amazon.com/support/home?>`__ .
                  - **Requested** *(string) --* 
                    Reserved. If you need to sustain traffic greater than the `documented limits <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html>`__ , contact us through the `Support Center <https://console.aws.amazon.com/support/home?>`__ .
                  - **Status** *(string) --* 
                    Reserved. If you need to sustain traffic greater than the `documented limits <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html>`__ , contact us through the `Support Center <https://console.aws.amazon.com/support/home?>`__ .
                - **State** *(string) --* 
                  The state of the NAT gateway.
                  * ``pending`` : The NAT gateway is being created and is not ready to process traffic. 
                  * ``failed`` : The NAT gateway could not be created. Check the ``failureCode`` and ``failureMessage`` fields for the reason. 
                  * ``available`` : The NAT gateway is able to process traffic. This status remains until you delete the NAT gateway, and does not indicate the health of the NAT gateway. 
                  * ``deleting`` : The NAT gateway is in the process of being terminated and may still be processing traffic. 
                  * ``deleted`` : The NAT gateway has been terminated and is no longer processing traffic. 
                - **SubnetId** *(string) --* 
                  The ID of the subnet in which the NAT gateway is located.
                - **VpcId** *(string) --* 
                  The ID of the VPC in which the NAT gateway is located.
                - **Tags** *(list) --* 
                  The tags for the NAT gateway.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``nat-gateway-id`` - The ID of the NAT gateway.
          * ``state`` - The state of the NAT gateway (``pending`` | ``failed`` | ``available`` | ``deleting`` | ``deleted`` ).
          * ``subnet-id`` - The ID of the subnet in which the NAT gateway resides.
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value.
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
          * ``vpc-id`` - The ID of the VPC in which the NAT gateway resides.
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
        :type NatGatewayIds: list
        :param NatGatewayIds:
          One or more NAT gateway IDs.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeNetworkInterfacePermissions(Paginator):
    def paginate(self, NetworkInterfacePermissionIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_network_interface_permissions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNetworkInterfacePermissions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              NetworkInterfacePermissionIds=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'NetworkInterfacePermissions': [
                    {
                        'NetworkInterfacePermissionId': 'string',
                        'NetworkInterfaceId': 'string',
                        'AwsAccountId': 'string',
                        'AwsService': 'string',
                        'Permission': 'INSTANCE-ATTACH'|'EIP-ASSOCIATE',
                        'PermissionState': {
                            'State': 'pending'|'granted'|'revoking'|'revoked',
                            'StatusMessage': 'string'
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output for DescribeNetworkInterfacePermissions.
            - **NetworkInterfacePermissions** *(list) --* 
              The network interface permissions.
              - *(dict) --* 
                Describes a permission for a network interface.
                - **NetworkInterfacePermissionId** *(string) --* 
                  The ID of the network interface permission.
                - **NetworkInterfaceId** *(string) --* 
                  The ID of the network interface.
                - **AwsAccountId** *(string) --* 
                  The AWS account ID.
                - **AwsService** *(string) --* 
                  The AWS service.
                - **Permission** *(string) --* 
                  The type of permission.
                - **PermissionState** *(dict) --* 
                  Information about the state of the permission.
                  - **State** *(string) --* 
                    The state of the permission.
                  - **StatusMessage** *(string) --* 
                    A status message, if applicable.
        :type NetworkInterfacePermissionIds: list
        :param NetworkInterfacePermissionIds:
          One or more network interface permission IDs.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``network-interface-permission.network-interface-permission-id`` - The ID of the permission.
          * ``network-interface-permission.network-interface-id`` - The ID of the network interface.
          * ``network-interface-permission.aws-account-id`` - The AWS account ID.
          * ``network-interface-permission.aws-service`` - The AWS service.
          * ``network-interface-permission.permission`` - The type of permission (``INSTANCE-ATTACH`` | ``EIP-ASSOCIATE`` ).
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeNetworkInterfaces(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, NetworkInterfaceIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_network_interfaces`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNetworkInterfaces>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              NetworkInterfaceIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'NetworkInterfaces': [
                    {
                        'Association': {
                            'AllocationId': 'string',
                            'AssociationId': 'string',
                            'IpOwnerId': 'string',
                            'PublicDnsName': 'string',
                            'PublicIp': 'string'
                        },
                        'Attachment': {
                            'AttachTime': datetime(2015, 1, 1),
                            'AttachmentId': 'string',
                            'DeleteOnTermination': True|False,
                            'DeviceIndex': 123,
                            'InstanceId': 'string',
                            'InstanceOwnerId': 'string',
                            'Status': 'attaching'|'attached'|'detaching'|'detached'
                        },
                        'AvailabilityZone': 'string',
                        'Description': 'string',
                        'Groups': [
                            {
                                'GroupName': 'string',
                                'GroupId': 'string'
                            },
                        ],
                        'InterfaceType': 'interface'|'natGateway',
                        'Ipv6Addresses': [
                            {
                                'Ipv6Address': 'string'
                            },
                        ],
                        'MacAddress': 'string',
                        'NetworkInterfaceId': 'string',
                        'OwnerId': 'string',
                        'PrivateDnsName': 'string',
                        'PrivateIpAddress': 'string',
                        'PrivateIpAddresses': [
                            {
                                'Association': {
                                    'AllocationId': 'string',
                                    'AssociationId': 'string',
                                    'IpOwnerId': 'string',
                                    'PublicDnsName': 'string',
                                    'PublicIp': 'string'
                                },
                                'Primary': True|False,
                                'PrivateDnsName': 'string',
                                'PrivateIpAddress': 'string'
                            },
                        ],
                        'RequesterId': 'string',
                        'RequesterManaged': True|False,
                        'SourceDestCheck': True|False,
                        'Status': 'available'|'associated'|'attaching'|'in-use'|'detaching',
                        'SubnetId': 'string',
                        'TagSet': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'VpcId': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of DescribeNetworkInterfaces.
            - **NetworkInterfaces** *(list) --* 
              Information about one or more network interfaces.
              - *(dict) --* 
                Describes a network interface.
                - **Association** *(dict) --* 
                  The association information for an Elastic IP address (IPv4) associated with the network interface.
                  - **AllocationId** *(string) --* 
                    The allocation ID.
                  - **AssociationId** *(string) --* 
                    The association ID.
                  - **IpOwnerId** *(string) --* 
                    The ID of the Elastic IP address owner.
                  - **PublicDnsName** *(string) --* 
                    The public DNS name.
                  - **PublicIp** *(string) --* 
                    The address of the Elastic IP address bound to the network interface.
                - **Attachment** *(dict) --* 
                  The network interface attachment.
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
                - **AvailabilityZone** *(string) --* 
                  The Availability Zone.
                - **Description** *(string) --* 
                  A description.
                - **Groups** *(list) --* 
                  Any security groups for the network interface.
                  - *(dict) --* 
                    Describes a security group.
                    - **GroupName** *(string) --* 
                      The name of the security group.
                    - **GroupId** *(string) --* 
                      The ID of the security group.
                - **InterfaceType** *(string) --* 
                  The type of interface.
                - **Ipv6Addresses** *(list) --* 
                  The IPv6 addresses associated with the network interface.
                  - *(dict) --* 
                    Describes an IPv6 address associated with a network interface.
                    - **Ipv6Address** *(string) --* 
                      The IPv6 address.
                - **MacAddress** *(string) --* 
                  The MAC address.
                - **NetworkInterfaceId** *(string) --* 
                  The ID of the network interface.
                - **OwnerId** *(string) --* 
                  The AWS account ID of the owner of the network interface.
                - **PrivateDnsName** *(string) --* 
                  The private DNS name.
                - **PrivateIpAddress** *(string) --* 
                  The IPv4 address of the network interface within the subnet.
                - **PrivateIpAddresses** *(list) --* 
                  The private IPv4 addresses associated with the network interface.
                  - *(dict) --* 
                    Describes the private IPv4 address of a network interface.
                    - **Association** *(dict) --* 
                      The association information for an Elastic IP address (IPv4) associated with the network interface.
                      - **AllocationId** *(string) --* 
                        The allocation ID.
                      - **AssociationId** *(string) --* 
                        The association ID.
                      - **IpOwnerId** *(string) --* 
                        The ID of the Elastic IP address owner.
                      - **PublicDnsName** *(string) --* 
                        The public DNS name.
                      - **PublicIp** *(string) --* 
                        The address of the Elastic IP address bound to the network interface.
                    - **Primary** *(boolean) --* 
                      Indicates whether this IPv4 address is the primary private IPv4 address of the network interface.
                    - **PrivateDnsName** *(string) --* 
                      The private DNS name.
                    - **PrivateIpAddress** *(string) --* 
                      The private IPv4 address.
                - **RequesterId** *(string) --* 
                  The ID of the entity that launched the instance on your behalf (for example, AWS Management Console or Auto Scaling).
                - **RequesterManaged** *(boolean) --* 
                  Indicates whether the network interface is being managed by AWS.
                - **SourceDestCheck** *(boolean) --* 
                  Indicates whether traffic to or from the instance is validated.
                - **Status** *(string) --* 
                  The status of the network interface.
                - **SubnetId** *(string) --* 
                  The ID of the subnet.
                - **TagSet** *(list) --* 
                  Any tags assigned to the network interface.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
                - **VpcId** *(string) --* 
                  The ID of the VPC.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribePrefixLists(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, PrefixListIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_prefix_lists`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribePrefixLists>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PrefixListIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'PrefixLists': [
                    {
                        'Cidrs': [
                            'string',
                        ],
                        'PrefixListId': 'string',
                        'PrefixListName': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PrefixLists** *(list) --* 
              All available prefix lists.
              - *(dict) --* 
                Describes prefixes for AWS services.
                - **Cidrs** *(list) --* 
                  The IP address range of the AWS service.
                  - *(string) --* 
                - **PrefixListId** *(string) --* 
                  The ID of the prefix.
                - **PrefixListName** *(string) --* 
                  The name of the prefix.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``prefix-list-id`` : The ID of a prefix list.
          * ``prefix-list-name`` : The name of a prefix list.
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
        :type PrefixListIds: list
        :param PrefixListIds:
          One or more prefix list IDs.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribePrincipalIdFormat(Paginator):
    def paginate(self, DryRun: bool = None, Resources: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_principal_id_format`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribePrincipalIdFormat>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              Resources=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Principals': [
                    {
                        'Arn': 'string',
                        'Statuses': [
                            {
                                'Deadline': datetime(2015, 1, 1),
                                'Resource': 'string',
                                'UseLongIds': True|False
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Principals** *(list) --* 
              Information about the ID format settings for the ARN.
              - *(dict) --* 
                PrincipalIdFormat description
                - **Arn** *(string) --* 
                  PrincipalIdFormatARN description
                - **Statuses** *(list) --* 
                  PrincipalIdFormatStatuses description
                  - *(dict) --* 
                    Describes the ID format for a resource.
                    - **Deadline** *(datetime) --* 
                      The date in UTC at which you are permanently switched over to using longer IDs. If a deadline is not yet available for this resource type, this field is not returned.
                    - **Resource** *(string) --* 
                      The type of resource.
                    - **UseLongIds** *(boolean) --* 
                      Indicates whether longer IDs (17-character IDs) are enabled for the resource.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type Resources: list
        :param Resources:
          The type of resource: ``bundle`` | ``conversion-task`` | ``customer-gateway`` | ``dhcp-options`` | ``elastic-ip-allocation`` | ``elastic-ip-association`` | ``export-task`` | ``flow-log`` | ``image`` | ``import-task`` | ``instance`` | ``internet-gateway`` | ``network-acl`` | ``network-acl-association`` | ``network-interface`` | ``network-interface-attachment`` | ``prefix-list`` | ``reservation`` | ``route-table`` | ``route-table-association`` | ``security-group`` | ``snapshot`` | ``subnet`` | ``subnet-cidr-block-association`` | ``volume`` | ``vpc`` | ``vpc-cidr-block-association`` | ``vpc-endpoint`` | ``vpc-peering-connection`` | ``vpn-connection`` | ``vpn-gateway``
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribePublicIpv4Pools(Paginator):
    def paginate(self, PoolIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_public_ipv4_pools`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribePublicIpv4Pools>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PoolIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'PublicIpv4Pools': [
                    {
                        'PoolId': 'string',
                        'Description': 'string',
                        'PoolAddressRanges': [
                            {
                                'FirstAddress': 'string',
                                'LastAddress': 'string',
                                'AddressCount': 123,
                                'AvailableAddressCount': 123
                            },
                        ],
                        'TotalAddressCount': 123,
                        'TotalAvailableAddressCount': 123
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PublicIpv4Pools** *(list) --* 
              Information about the address pools.
              - *(dict) --* 
                Describes an address pool.
                - **PoolId** *(string) --* 
                  The ID of the IPv4 address pool.
                - **Description** *(string) --* 
                  A description of the address pool.
                - **PoolAddressRanges** *(list) --* 
                  The address ranges.
                  - *(dict) --* 
                    Describes an address range of an IPv4 address pool.
                    - **FirstAddress** *(string) --* 
                      The first IP address in the range.
                    - **LastAddress** *(string) --* 
                      The last IP address in the range.
                    - **AddressCount** *(integer) --* 
                      The number of addresses in the range.
                    - **AvailableAddressCount** *(integer) --* 
                      The number of available addresses in the range.
                - **TotalAddressCount** *(integer) --* 
                  The total number of addresses.
                - **TotalAvailableAddressCount** *(integer) --* 
                  The total number of available addresses.
        :type PoolIds: list
        :param PoolIds:
          The IDs of the address pools.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeReservedInstancesModifications(Paginator):
    def paginate(self, Filters: List = None, ReservedInstancesModificationIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_reserved_instances_modifications`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeReservedInstancesModifications>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              ReservedInstancesModificationIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ReservedInstancesModifications': [
                    {
                        'ClientToken': 'string',
                        'CreateDate': datetime(2015, 1, 1),
                        'EffectiveDate': datetime(2015, 1, 1),
                        'ModificationResults': [
                            {
                                'ReservedInstancesId': 'string',
                                'TargetConfiguration': {
                                    'AvailabilityZone': 'string',
                                    'InstanceCount': 123,
                                    'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'t3.nano'|'t3.micro'|'t3.small'|'t3.medium'|'t3.large'|'t3.xlarge'|'t3.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.12xlarge'|'r5.24xlarge'|'r5.metal'|'r5a.large'|'r5a.xlarge'|'r5a.2xlarge'|'r5a.4xlarge'|'r5a.12xlarge'|'r5a.24xlarge'|'r5d.large'|'r5d.xlarge'|'r5d.2xlarge'|'r5d.4xlarge'|'r5d.12xlarge'|'r5d.24xlarge'|'r5d.metal'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'i3.metal'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'c5d.large'|'c5d.xlarge'|'c5d.2xlarge'|'c5d.4xlarge'|'c5d.9xlarge'|'c5d.18xlarge'|'c5n.large'|'c5n.xlarge'|'c5n.2xlarge'|'c5n.4xlarge'|'c5n.9xlarge'|'c5n.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'g3s.xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'p3dn.24xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.4xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'m5.metal'|'m5a.large'|'m5a.xlarge'|'m5a.2xlarge'|'m5a.4xlarge'|'m5a.12xlarge'|'m5a.24xlarge'|'m5d.large'|'m5d.xlarge'|'m5d.2xlarge'|'m5d.4xlarge'|'m5d.12xlarge'|'m5d.24xlarge'|'m5d.metal'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge'|'z1d.large'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'z1d.metal'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal'|'a1.medium'|'a1.large'|'a1.xlarge'|'a1.2xlarge'|'a1.4xlarge',
                                    'Platform': 'string',
                                    'Scope': 'Availability Zone'|'Region'
                                }
                            },
                        ],
                        'ReservedInstancesIds': [
                            {
                                'ReservedInstancesId': 'string'
                            },
                        ],
                        'ReservedInstancesModificationId': 'string',
                        'Status': 'string',
                        'StatusMessage': 'string',
                        'UpdateDate': datetime(2015, 1, 1)
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of DescribeReservedInstancesModifications.
            - **ReservedInstancesModifications** *(list) --* 
              The Reserved Instance modification information.
              - *(dict) --* 
                Describes a Reserved Instance modification.
                - **ClientToken** *(string) --* 
                  A unique, case-sensitive key supplied by the client to ensure that the request is idempotent. For more information, see `Ensuring Idempotency <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html>`__ .
                - **CreateDate** *(datetime) --* 
                  The time when the modification request was created.
                - **EffectiveDate** *(datetime) --* 
                  The time for the modification to become effective.
                - **ModificationResults** *(list) --* 
                  Contains target configurations along with their corresponding new Reserved Instance IDs.
                  - *(dict) --* 
                    Describes the modification request/s.
                    - **ReservedInstancesId** *(string) --* 
                      The ID for the Reserved Instances that were created as part of the modification request. This field is only available when the modification is fulfilled.
                    - **TargetConfiguration** *(dict) --* 
                      The target Reserved Instances configurations supplied as part of the modification request.
                      - **AvailabilityZone** *(string) --* 
                        The Availability Zone for the modified Reserved Instances.
                      - **InstanceCount** *(integer) --* 
                        The number of modified Reserved Instances.
                        .. note::
                          This is a required field for a request.
                      - **InstanceType** *(string) --* 
                        The instance type for the modified Reserved Instances.
                      - **Platform** *(string) --* 
                        The network platform of the modified Reserved Instances, which is either EC2-Classic or EC2-VPC.
                      - **Scope** *(string) --* 
                        Whether the Reserved Instance is applied to instances in a region or instances in a specific Availability Zone.
                - **ReservedInstancesIds** *(list) --* 
                  The IDs of one or more Reserved Instances.
                  - *(dict) --* 
                    Describes the ID of a Reserved Instance.
                    - **ReservedInstancesId** *(string) --* 
                      The ID of the Reserved Instance.
                - **ReservedInstancesModificationId** *(string) --* 
                  A unique ID for the Reserved Instance modification.
                - **Status** *(string) --* 
                  The status of the Reserved Instances modification request.
                - **StatusMessage** *(string) --* 
                  The reason for the status.
                - **UpdateDate** *(datetime) --* 
                  The time when the modification request was last updated.
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``client-token`` - The idempotency token for the modification request.
          * ``create-date`` - The time when the modification request was created.
          * ``effective-date`` - The time when the modification becomes effective.
          * ``modification-result.reserved-instances-id`` - The ID for the Reserved Instances created as part of the modification request. This ID is only available when the status of the modification is ``fulfilled`` .
          * ``modification-result.target-configuration.availability-zone`` - The Availability Zone for the new Reserved Instances.
          * ``modification-result.target-configuration.instance-count`` - The number of new Reserved Instances.
          * ``modification-result.target-configuration.instance-type`` - The instance type of the new Reserved Instances.
          * ``modification-result.target-configuration.platform`` - The network platform of the new Reserved Instances (``EC2-Classic`` | ``EC2-VPC`` ).
          * ``reserved-instances-id`` - The ID of the Reserved Instances modified.
          * ``reserved-instances-modification-id`` - The ID of the modification request.
          * ``status`` - The status of the Reserved Instances modification request (``processing`` | ``fulfilled`` | ``failed`` ).
          * ``status-message`` - The reason for the status.
          * ``update-date`` - The time when the modification request was last updated.
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
        :type ReservedInstancesModificationIds: list
        :param ReservedInstancesModificationIds:
          IDs for the submitted modification request.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeReservedInstancesOfferings(Paginator):
    def paginate(self, AvailabilityZone: str = None, Filters: List = None, IncludeMarketplace: bool = None, InstanceType: str = None, MaxDuration: int = None, MaxInstanceCount: int = None, MinDuration: int = None, OfferingClass: str = None, ProductDescription: str = None, ReservedInstancesOfferingIds: List = None, DryRun: bool = None, InstanceTenancy: str = None, OfferingType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_reserved_instances_offerings`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeReservedInstancesOfferings>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AvailabilityZone='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              IncludeMarketplace=True|False,
              InstanceType='t1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'t3.nano'|'t3.micro'|'t3.small'|'t3.medium'|'t3.large'|'t3.xlarge'|'t3.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.12xlarge'|'r5.24xlarge'|'r5.metal'|'r5a.large'|'r5a.xlarge'|'r5a.2xlarge'|'r5a.4xlarge'|'r5a.12xlarge'|'r5a.24xlarge'|'r5d.large'|'r5d.xlarge'|'r5d.2xlarge'|'r5d.4xlarge'|'r5d.12xlarge'|'r5d.24xlarge'|'r5d.metal'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'i3.metal'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'c5d.large'|'c5d.xlarge'|'c5d.2xlarge'|'c5d.4xlarge'|'c5d.9xlarge'|'c5d.18xlarge'|'c5n.large'|'c5n.xlarge'|'c5n.2xlarge'|'c5n.4xlarge'|'c5n.9xlarge'|'c5n.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'g3s.xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'p3dn.24xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.4xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'m5.metal'|'m5a.large'|'m5a.xlarge'|'m5a.2xlarge'|'m5a.4xlarge'|'m5a.12xlarge'|'m5a.24xlarge'|'m5d.large'|'m5d.xlarge'|'m5d.2xlarge'|'m5d.4xlarge'|'m5d.12xlarge'|'m5d.24xlarge'|'m5d.metal'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge'|'z1d.large'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'z1d.metal'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal'|'a1.medium'|'a1.large'|'a1.xlarge'|'a1.2xlarge'|'a1.4xlarge',
              MaxDuration=123,
              MaxInstanceCount=123,
              MinDuration=123,
              OfferingClass='standard'|'convertible',
              ProductDescription='Linux/UNIX'|'Linux/UNIX (Amazon VPC)'|'Windows'|'Windows (Amazon VPC)',
              ReservedInstancesOfferingIds=[
                  'string',
              ],
              DryRun=True|False,
              InstanceTenancy='default'|'dedicated'|'host',
              OfferingType='Heavy Utilization'|'Medium Utilization'|'Light Utilization'|'No Upfront'|'Partial Upfront'|'All Upfront',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ReservedInstancesOfferings': [
                    {
                        'AvailabilityZone': 'string',
                        'Duration': 123,
                        'FixedPrice': ...,
                        'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'t3.nano'|'t3.micro'|'t3.small'|'t3.medium'|'t3.large'|'t3.xlarge'|'t3.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.12xlarge'|'r5.24xlarge'|'r5.metal'|'r5a.large'|'r5a.xlarge'|'r5a.2xlarge'|'r5a.4xlarge'|'r5a.12xlarge'|'r5a.24xlarge'|'r5d.large'|'r5d.xlarge'|'r5d.2xlarge'|'r5d.4xlarge'|'r5d.12xlarge'|'r5d.24xlarge'|'r5d.metal'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'i3.metal'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'c5d.large'|'c5d.xlarge'|'c5d.2xlarge'|'c5d.4xlarge'|'c5d.9xlarge'|'c5d.18xlarge'|'c5n.large'|'c5n.xlarge'|'c5n.2xlarge'|'c5n.4xlarge'|'c5n.9xlarge'|'c5n.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'g3s.xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'p3dn.24xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.4xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'m5.metal'|'m5a.large'|'m5a.xlarge'|'m5a.2xlarge'|'m5a.4xlarge'|'m5a.12xlarge'|'m5a.24xlarge'|'m5d.large'|'m5d.xlarge'|'m5d.2xlarge'|'m5d.4xlarge'|'m5d.12xlarge'|'m5d.24xlarge'|'m5d.metal'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge'|'z1d.large'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'z1d.metal'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal'|'a1.medium'|'a1.large'|'a1.xlarge'|'a1.2xlarge'|'a1.4xlarge',
                        'ProductDescription': 'Linux/UNIX'|'Linux/UNIX (Amazon VPC)'|'Windows'|'Windows (Amazon VPC)',
                        'ReservedInstancesOfferingId': 'string',
                        'UsagePrice': ...,
                        'CurrencyCode': 'USD',
                        'InstanceTenancy': 'default'|'dedicated'|'host',
                        'Marketplace': True|False,
                        'OfferingClass': 'standard'|'convertible',
                        'OfferingType': 'Heavy Utilization'|'Medium Utilization'|'Light Utilization'|'No Upfront'|'Partial Upfront'|'All Upfront',
                        'PricingDetails': [
                            {
                                'Count': 123,
                                'Price': 123.0
                            },
                        ],
                        'RecurringCharges': [
                            {
                                'Amount': 123.0,
                                'Frequency': 'Hourly'
                            },
                        ],
                        'Scope': 'Availability Zone'|'Region'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of DescribeReservedInstancesOfferings.
            - **ReservedInstancesOfferings** *(list) --* 
              A list of Reserved Instances offerings.
              - *(dict) --* 
                Describes a Reserved Instance offering.
                - **AvailabilityZone** *(string) --* 
                  The Availability Zone in which the Reserved Instance can be used.
                - **Duration** *(integer) --* 
                  The duration of the Reserved Instance, in seconds.
                - **FixedPrice** *(float) --* 
                  The purchase price of the Reserved Instance.
                - **InstanceType** *(string) --* 
                  The instance type on which the Reserved Instance can be used.
                - **ProductDescription** *(string) --* 
                  The Reserved Instance product platform description.
                - **ReservedInstancesOfferingId** *(string) --* 
                  The ID of the Reserved Instance offering. This is the offering ID used in  GetReservedInstancesExchangeQuote to confirm that an exchange can be made.
                - **UsagePrice** *(float) --* 
                  The usage price of the Reserved Instance, per hour.
                - **CurrencyCode** *(string) --* 
                  The currency of the Reserved Instance offering you are purchasing. It's specified using ISO 4217 standard currency codes. At this time, the only supported currency is ``USD`` .
                - **InstanceTenancy** *(string) --* 
                  The tenancy of the instance.
                - **Marketplace** *(boolean) --* 
                  Indicates whether the offering is available through the Reserved Instance Marketplace (resale) or AWS. If it's a Reserved Instance Marketplace offering, this is ``true`` .
                - **OfferingClass** *(string) --* 
                  If ``convertible`` it can be exchanged for Reserved Instances of the same or higher monetary value, with different configurations. If ``standard`` , it is not possible to perform an exchange.
                - **OfferingType** *(string) --* 
                  The Reserved Instance offering type.
                - **PricingDetails** *(list) --* 
                  The pricing details of the Reserved Instance offering.
                  - *(dict) --* 
                    Describes a Reserved Instance offering.
                    - **Count** *(integer) --* 
                      The number of reservations available for the price.
                    - **Price** *(float) --* 
                      The price per instance.
                - **RecurringCharges** *(list) --* 
                  The recurring charge tag assigned to the resource.
                  - *(dict) --* 
                    Describes a recurring charge.
                    - **Amount** *(float) --* 
                      The amount of the recurring charge.
                    - **Frequency** *(string) --* 
                      The frequency of the recurring charge.
                - **Scope** *(string) --* 
                  Whether the Reserved Instance is applied to instances in a region or an Availability Zone.
        :type AvailabilityZone: string
        :param AvailabilityZone:
          The Availability Zone in which the Reserved Instance can be used.
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``availability-zone`` - The Availability Zone where the Reserved Instance can be used.
          * ``duration`` - The duration of the Reserved Instance (for example, one year or three years), in seconds (``31536000`` | ``94608000`` ).
          * ``fixed-price`` - The purchase price of the Reserved Instance (for example, 9800.0).
          * ``instance-type`` - The instance type that is covered by the reservation.
          * ``marketplace`` - Set to ``true`` to show only Reserved Instance Marketplace offerings. When this filter is not used, which is the default behavior, all offerings from both AWS and the Reserved Instance Marketplace are listed.
          * ``product-description`` - The Reserved Instance product platform description. Instances that include ``(Amazon VPC)`` in the product platform description will only be displayed to EC2-Classic account holders and are for use with Amazon VPC. (``Linux/UNIX`` | ``Linux/UNIX (Amazon VPC)`` | ``SUSE Linux`` | ``SUSE Linux (Amazon VPC)`` | ``Red Hat Enterprise Linux`` | ``Red Hat Enterprise Linux (Amazon VPC)`` | ``Windows`` | ``Windows (Amazon VPC)`` | ``Windows with SQL Server Standard`` | ``Windows with SQL Server Standard (Amazon VPC)`` | ``Windows with SQL Server Web`` | ``Windows with SQL Server Web (Amazon VPC)`` | ``Windows with SQL Server Enterprise`` | ``Windows with SQL Server Enterprise (Amazon VPC)`` )
          * ``reserved-instances-offering-id`` - The Reserved Instances offering ID.
          * ``scope`` - The scope of the Reserved Instance (``Availability Zone`` or ``Region`` ).
          * ``usage-price`` - The usage price of the Reserved Instance, per hour (for example, 0.84).
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
        :type IncludeMarketplace: boolean
        :param IncludeMarketplace:
          Include Reserved Instance Marketplace offerings in the response.
        :type InstanceType: string
        :param InstanceType:
          The instance type that the reservation will cover (for example, ``m1.small`` ). For more information, see `Instance Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        :type MaxDuration: integer
        :param MaxDuration:
          The maximum duration (in seconds) to filter when searching for offerings.
          Default: 94608000 (3 years)
        :type MaxInstanceCount: integer
        :param MaxInstanceCount:
          The maximum number of instances to filter when searching for offerings.
          Default: 20
        :type MinDuration: integer
        :param MinDuration:
          The minimum duration (in seconds) to filter when searching for offerings.
          Default: 2592000 (1 month)
        :type OfferingClass: string
        :param OfferingClass:
          The offering class of the Reserved Instance. Can be ``standard`` or ``convertible`` .
        :type ProductDescription: string
        :param ProductDescription:
          The Reserved Instance product platform description. Instances that include ``(Amazon VPC)`` in the description are for use with Amazon VPC.
        :type ReservedInstancesOfferingIds: list
        :param ReservedInstancesOfferingIds:
          One or more Reserved Instances offering IDs.
          - *(string) --*
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type InstanceTenancy: string
        :param InstanceTenancy:
          The tenancy of the instances covered by the reservation. A Reserved Instance with a tenancy of ``dedicated`` is applied to instances that run in a VPC on single-tenant hardware (i.e., Dedicated Instances).
           **Important:** The ``host`` value cannot be used with this parameter. Use the ``default`` or ``dedicated`` values only.
          Default: ``default``
        :type OfferingType: string
        :param OfferingType:
          The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have access to the ``Medium Utilization`` Reserved Instance offering type.
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeRouteTables(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, RouteTableIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_route_tables`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeRouteTables>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              RouteTableIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'RouteTables': [
                    {
                        'Associations': [
                            {
                                'Main': True|False,
                                'RouteTableAssociationId': 'string',
                                'RouteTableId': 'string',
                                'SubnetId': 'string'
                            },
                        ],
                        'PropagatingVgws': [
                            {
                                'GatewayId': 'string'
                            },
                        ],
                        'RouteTableId': 'string',
                        'Routes': [
                            {
                                'DestinationCidrBlock': 'string',
                                'DestinationIpv6CidrBlock': 'string',
                                'DestinationPrefixListId': 'string',
                                'EgressOnlyInternetGatewayId': 'string',
                                'GatewayId': 'string',
                                'InstanceId': 'string',
                                'InstanceOwnerId': 'string',
                                'NatGatewayId': 'string',
                                'TransitGatewayId': 'string',
                                'NetworkInterfaceId': 'string',
                                'Origin': 'CreateRouteTable'|'CreateRoute'|'EnableVgwRoutePropagation',
                                'State': 'active'|'blackhole',
                                'VpcPeeringConnectionId': 'string'
                            },
                        ],
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'VpcId': 'string',
                        'OwnerId': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of DescribeRouteTables.
            - **RouteTables** *(list) --* 
              Information about one or more route tables.
              - *(dict) --* 
                Describes a route table.
                - **Associations** *(list) --* 
                  The associations between the route table and one or more subnets.
                  - *(dict) --* 
                    Describes an association between a route table and a subnet.
                    - **Main** *(boolean) --* 
                      Indicates whether this is the main route table.
                    - **RouteTableAssociationId** *(string) --* 
                      The ID of the association between a route table and a subnet.
                    - **RouteTableId** *(string) --* 
                      The ID of the route table.
                    - **SubnetId** *(string) --* 
                      The ID of the subnet. A subnet ID is not returned for an implicit association.
                - **PropagatingVgws** *(list) --* 
                  Any virtual private gateway (VGW) propagating routes.
                  - *(dict) --* 
                    Describes a virtual private gateway propagating route.
                    - **GatewayId** *(string) --* 
                      The ID of the virtual private gateway.
                - **RouteTableId** *(string) --* 
                  The ID of the route table.
                - **Routes** *(list) --* 
                  The routes in the route table.
                  - *(dict) --* 
                    Describes a route in a route table.
                    - **DestinationCidrBlock** *(string) --* 
                      The IPv4 CIDR block used for the destination match.
                    - **DestinationIpv6CidrBlock** *(string) --* 
                      The IPv6 CIDR block used for the destination match.
                    - **DestinationPrefixListId** *(string) --* 
                      The prefix of the AWS service.
                    - **EgressOnlyInternetGatewayId** *(string) --* 
                      The ID of the egress-only internet gateway.
                    - **GatewayId** *(string) --* 
                      The ID of a gateway attached to your VPC.
                    - **InstanceId** *(string) --* 
                      The ID of a NAT instance in your VPC.
                    - **InstanceOwnerId** *(string) --* 
                      The AWS account ID of the owner of the instance.
                    - **NatGatewayId** *(string) --* 
                      The ID of a NAT gateway.
                    - **TransitGatewayId** *(string) --* 
                      The ID of a transit gateway.
                    - **NetworkInterfaceId** *(string) --* 
                      The ID of the network interface.
                    - **Origin** *(string) --* 
                      Describes how the route was created.
                      * ``CreateRouteTable`` - The route was automatically created when the route table was created. 
                      * ``CreateRoute`` - The route was manually added to the route table. 
                      * ``EnableVgwRoutePropagation`` - The route was propagated by route propagation. 
                    - **State** *(string) --* 
                      The state of the route. The ``blackhole`` state indicates that the route's target isn't available (for example, the specified gateway isn't attached to the VPC, or the specified NAT instance has been terminated).
                    - **VpcPeeringConnectionId** *(string) --* 
                      The ID of a VPC peering connection.
                - **Tags** *(list) --* 
                  Any tags assigned to the route table.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
                - **VpcId** *(string) --* 
                  The ID of the VPC.
                - **OwnerId** *(string) --* 
                  The ID of the AWS account that owns the route table.
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``association.route-table-association-id`` - The ID of an association ID for the route table.
          * ``association.route-table-id`` - The ID of the route table involved in the association.
          * ``association.subnet-id`` - The ID of the subnet involved in the association.
          * ``association.main`` - Indicates whether the route table is the main route table for the VPC (``true`` | ``false`` ). Route tables that do not have an association ID are not returned in the response.
          * ``owner-id`` - The ID of the AWS account that owns the route table.
          * ``route-table-id`` - The ID of the route table.
          * ``route.destination-cidr-block`` - The IPv4 CIDR range specified in a route in the table.
          * ``route.destination-ipv6-cidr-block`` - The IPv6 CIDR range specified in a route in the route table.
          * ``route.destination-prefix-list-id`` - The ID (prefix) of the AWS service specified in a route in the table.
          * ``route.egress-only-internet-gateway-id`` - The ID of an egress-only Internet gateway specified in a route in the route table.
          * ``route.gateway-id`` - The ID of a gateway specified in a route in the table.
          * ``route.instance-id`` - The ID of an instance specified in a route in the table.
          * ``route.nat-gateway-id`` - The ID of a NAT gateway.
          * ``route.transit-gateway-id`` - The ID of a transit gateway.
          * ``route.origin`` - Describes how the route was created. ``CreateRouteTable`` indicates that the route was automatically created when the route table was created; ``CreateRoute`` indicates that the route was manually added to the route table; ``EnableVgwRoutePropagation`` indicates that the route was propagated by route propagation.
          * ``route.state`` - The state of a route in the route table (``active`` | ``blackhole`` ). The blackhole state indicates that the route\'s target isn\'t available (for example, the specified gateway isn\'t attached to the VPC, the specified NAT instance has been terminated, and so on).
          * ``route.vpc-peering-connection-id`` - The ID of a VPC peering connection specified in a route in the table.
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value.
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
          * ``transit-gateway-id`` - The ID of a transit gateway.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeScheduledInstanceAvailability(Paginator):
    def paginate(self, FirstSlotStartTimeRange: Dict, Recurrence: Dict, DryRun: bool = None, Filters: List = None, MaxSlotDurationInHours: int = None, MinSlotDurationInHours: int = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_scheduled_instance_availability`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeScheduledInstanceAvailability>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              FirstSlotStartTimeRange={
                  'EarliestTime': datetime(2015, 1, 1),
                  'LatestTime': datetime(2015, 1, 1)
              },
              MaxSlotDurationInHours=123,
              MinSlotDurationInHours=123,
              Recurrence={
                  'Frequency': 'string',
                  'Interval': 123,
                  'OccurrenceDays': [
                      123,
                  ],
                  'OccurrenceRelativeToEnd': True|False,
                  'OccurrenceUnit': 'string'
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ScheduledInstanceAvailabilitySet': [
                    {
                        'AvailabilityZone': 'string',
                        'AvailableInstanceCount': 123,
                        'FirstSlotStartTime': datetime(2015, 1, 1),
                        'HourlyPrice': 'string',
                        'InstanceType': 'string',
                        'MaxTermDurationInDays': 123,
                        'MinTermDurationInDays': 123,
                        'NetworkPlatform': 'string',
                        'Platform': 'string',
                        'PurchaseToken': 'string',
                        'Recurrence': {
                            'Frequency': 'string',
                            'Interval': 123,
                            'OccurrenceDaySet': [
                                123,
                            ],
                            'OccurrenceRelativeToEnd': True|False,
                            'OccurrenceUnit': 'string'
                        },
                        'SlotDurationInHours': 123,
                        'TotalScheduledInstanceHours': 123
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of DescribeScheduledInstanceAvailability.
            - **ScheduledInstanceAvailabilitySet** *(list) --* 
              Information about the available Scheduled Instances.
              - *(dict) --* 
                Describes a schedule that is available for your Scheduled Instances.
                - **AvailabilityZone** *(string) --* 
                  The Availability Zone.
                - **AvailableInstanceCount** *(integer) --* 
                  The number of available instances.
                - **FirstSlotStartTime** *(datetime) --* 
                  The time period for the first schedule to start.
                - **HourlyPrice** *(string) --* 
                  The hourly price for a single instance.
                - **InstanceType** *(string) --* 
                  The instance type. You can specify one of the C3, C4, M4, or R3 instance types.
                - **MaxTermDurationInDays** *(integer) --* 
                  The maximum term. The only possible value is 365 days.
                - **MinTermDurationInDays** *(integer) --* 
                  The minimum term. The only possible value is 365 days.
                - **NetworkPlatform** *(string) --* 
                  The network platform (``EC2-Classic`` or ``EC2-VPC`` ).
                - **Platform** *(string) --* 
                  The platform (``Linux/UNIX`` or ``Windows`` ).
                - **PurchaseToken** *(string) --* 
                  The purchase token. This token expires in two hours.
                - **Recurrence** *(dict) --* 
                  The schedule recurrence.
                  - **Frequency** *(string) --* 
                    The frequency (``Daily`` , ``Weekly`` , or ``Monthly`` ).
                  - **Interval** *(integer) --* 
                    The interval quantity. The interval unit depends on the value of ``frequency`` . For example, every 2 weeks or every 2 months.
                  - **OccurrenceDaySet** *(list) --* 
                    The days. For a monthly schedule, this is one or more days of the month (1-31). For a weekly schedule, this is one or more days of the week (1-7, where 1 is Sunday).
                    - *(integer) --* 
                  - **OccurrenceRelativeToEnd** *(boolean) --* 
                    Indicates whether the occurrence is relative to the end of the specified week or month.
                  - **OccurrenceUnit** *(string) --* 
                    The unit for ``occurrenceDaySet`` (``DayOfWeek`` or ``DayOfMonth`` ).
                - **SlotDurationInHours** *(integer) --* 
                  The number of hours in the schedule.
                - **TotalScheduledInstanceHours** *(integer) --* 
                  The total number of hours for a single instance for the entire term.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``availability-zone`` - The Availability Zone (for example, ``us-west-2a`` ).
          * ``instance-type`` - The instance type (for example, ``c4.large`` ).
          * ``network-platform`` - The network platform (``EC2-Classic`` or ``EC2-VPC`` ).
          * ``platform`` - The platform (``Linux/UNIX`` or ``Windows`` ).
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
        :type FirstSlotStartTimeRange: dict
        :param FirstSlotStartTimeRange: **[REQUIRED]**
          The time period for the first schedule to start.
          - **EarliestTime** *(datetime) --* **[REQUIRED]**
            The earliest date and time, in UTC, for the Scheduled Instance to start.
          - **LatestTime** *(datetime) --* **[REQUIRED]**
            The latest date and time, in UTC, for the Scheduled Instance to start. This value must be later than or equal to the earliest date and at most three months in the future.
        :type MaxSlotDurationInHours: integer
        :param MaxSlotDurationInHours:
          The maximum available duration, in hours. This value must be greater than ``MinSlotDurationInHours`` and less than 1,720.
        :type MinSlotDurationInHours: integer
        :param MinSlotDurationInHours:
          The minimum available duration, in hours. The minimum required duration is 1,200 hours per year. For example, the minimum daily schedule is 4 hours, the minimum weekly schedule is 24 hours, and the minimum monthly schedule is 100 hours.
        :type Recurrence: dict
        :param Recurrence: **[REQUIRED]**
          The schedule recurrence.
          - **Frequency** *(string) --*
            The frequency (``Daily`` , ``Weekly`` , or ``Monthly`` ).
          - **Interval** *(integer) --*
            The interval quantity. The interval unit depends on the value of ``Frequency`` . For example, every 2 weeks or every 2 months.
          - **OccurrenceDays** *(list) --*
            The days. For a monthly schedule, this is one or more days of the month (1-31). For a weekly schedule, this is one or more days of the week (1-7, where 1 is Sunday). You can\'t specify this value with a daily schedule. If the occurrence is relative to the end of the month, you can specify only a single day.
            - *(integer) --*
          - **OccurrenceRelativeToEnd** *(boolean) --*
            Indicates whether the occurrence is relative to the end of the specified week or month. You can\'t specify this value with a daily schedule.
          - **OccurrenceUnit** *(string) --*
            The unit for ``OccurrenceDays`` (``DayOfWeek`` or ``DayOfMonth`` ). This value is required for a monthly schedule. You can\'t specify ``DayOfWeek`` with a weekly schedule. You can\'t specify this value with a daily schedule.
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeScheduledInstances(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, ScheduledInstanceIds: List = None, SlotStartTimeRange: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_scheduled_instances`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeScheduledInstances>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              ScheduledInstanceIds=[
                  'string',
              ],
              SlotStartTimeRange={
                  'EarliestTime': datetime(2015, 1, 1),
                  'LatestTime': datetime(2015, 1, 1)
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ScheduledInstanceSet': [
                    {
                        'AvailabilityZone': 'string',
                        'CreateDate': datetime(2015, 1, 1),
                        'HourlyPrice': 'string',
                        'InstanceCount': 123,
                        'InstanceType': 'string',
                        'NetworkPlatform': 'string',
                        'NextSlotStartTime': datetime(2015, 1, 1),
                        'Platform': 'string',
                        'PreviousSlotEndTime': datetime(2015, 1, 1),
                        'Recurrence': {
                            'Frequency': 'string',
                            'Interval': 123,
                            'OccurrenceDaySet': [
                                123,
                            ],
                            'OccurrenceRelativeToEnd': True|False,
                            'OccurrenceUnit': 'string'
                        },
                        'ScheduledInstanceId': 'string',
                        'SlotDurationInHours': 123,
                        'TermEndDate': datetime(2015, 1, 1),
                        'TermStartDate': datetime(2015, 1, 1),
                        'TotalScheduledInstanceHours': 123
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of DescribeScheduledInstances.
            - **ScheduledInstanceSet** *(list) --* 
              Information about the Scheduled Instances.
              - *(dict) --* 
                Describes a Scheduled Instance.
                - **AvailabilityZone** *(string) --* 
                  The Availability Zone.
                - **CreateDate** *(datetime) --* 
                  The date when the Scheduled Instance was purchased.
                - **HourlyPrice** *(string) --* 
                  The hourly price for a single instance.
                - **InstanceCount** *(integer) --* 
                  The number of instances.
                - **InstanceType** *(string) --* 
                  The instance type.
                - **NetworkPlatform** *(string) --* 
                  The network platform (``EC2-Classic`` or ``EC2-VPC`` ).
                - **NextSlotStartTime** *(datetime) --* 
                  The time for the next schedule to start.
                - **Platform** *(string) --* 
                  The platform (``Linux/UNIX`` or ``Windows`` ).
                - **PreviousSlotEndTime** *(datetime) --* 
                  The time that the previous schedule ended or will end.
                - **Recurrence** *(dict) --* 
                  The schedule recurrence.
                  - **Frequency** *(string) --* 
                    The frequency (``Daily`` , ``Weekly`` , or ``Monthly`` ).
                  - **Interval** *(integer) --* 
                    The interval quantity. The interval unit depends on the value of ``frequency`` . For example, every 2 weeks or every 2 months.
                  - **OccurrenceDaySet** *(list) --* 
                    The days. For a monthly schedule, this is one or more days of the month (1-31). For a weekly schedule, this is one or more days of the week (1-7, where 1 is Sunday).
                    - *(integer) --* 
                  - **OccurrenceRelativeToEnd** *(boolean) --* 
                    Indicates whether the occurrence is relative to the end of the specified week or month.
                  - **OccurrenceUnit** *(string) --* 
                    The unit for ``occurrenceDaySet`` (``DayOfWeek`` or ``DayOfMonth`` ).
                - **ScheduledInstanceId** *(string) --* 
                  The Scheduled Instance ID.
                - **SlotDurationInHours** *(integer) --* 
                  The number of hours in the schedule.
                - **TermEndDate** *(datetime) --* 
                  The end date for the Scheduled Instance.
                - **TermStartDate** *(datetime) --* 
                  The start date for the Scheduled Instance.
                - **TotalScheduledInstanceHours** *(integer) --* 
                  The total number of hours for a single instance for the entire term.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``availability-zone`` - The Availability Zone (for example, ``us-west-2a`` ).
          * ``instance-type`` - The instance type (for example, ``c4.large`` ).
          * ``network-platform`` - The network platform (``EC2-Classic`` or ``EC2-VPC`` ).
          * ``platform`` - The platform (``Linux/UNIX`` or ``Windows`` ).
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
        :type ScheduledInstanceIds: list
        :param ScheduledInstanceIds:
          One or more Scheduled Instance IDs.
          - *(string) --*
        :type SlotStartTimeRange: dict
        :param SlotStartTimeRange:
          The time period for the first schedule to start.
          - **EarliestTime** *(datetime) --*
            The earliest date and time, in UTC, for the Scheduled Instance to start.
          - **LatestTime** *(datetime) --*
            The latest date and time, in UTC, for the Scheduled Instance to start.
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeSecurityGroups(Paginator):
    def paginate(self, Filters: List = None, GroupIds: List = None, GroupNames: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_security_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSecurityGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              GroupIds=[
                  'string',
              ],
              GroupNames=[
                  'string',
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'SecurityGroups': [
                    {
                        'Description': 'string',
                        'GroupName': 'string',
                        'IpPermissions': [
                            {
                                'FromPort': 123,
                                'IpProtocol': 'string',
                                'IpRanges': [
                                    {
                                        'CidrIp': 'string',
                                        'Description': 'string'
                                    },
                                ],
                                'Ipv6Ranges': [
                                    {
                                        'CidrIpv6': 'string',
                                        'Description': 'string'
                                    },
                                ],
                                'PrefixListIds': [
                                    {
                                        'Description': 'string',
                                        'PrefixListId': 'string'
                                    },
                                ],
                                'ToPort': 123,
                                'UserIdGroupPairs': [
                                    {
                                        'Description': 'string',
                                        'GroupId': 'string',
                                        'GroupName': 'string',
                                        'PeeringStatus': 'string',
                                        'UserId': 'string',
                                        'VpcId': 'string',
                                        'VpcPeeringConnectionId': 'string'
                                    },
                                ]
                            },
                        ],
                        'OwnerId': 'string',
                        'GroupId': 'string',
                        'IpPermissionsEgress': [
                            {
                                'FromPort': 123,
                                'IpProtocol': 'string',
                                'IpRanges': [
                                    {
                                        'CidrIp': 'string',
                                        'Description': 'string'
                                    },
                                ],
                                'Ipv6Ranges': [
                                    {
                                        'CidrIpv6': 'string',
                                        'Description': 'string'
                                    },
                                ],
                                'PrefixListIds': [
                                    {
                                        'Description': 'string',
                                        'PrefixListId': 'string'
                                    },
                                ],
                                'ToPort': 123,
                                'UserIdGroupPairs': [
                                    {
                                        'Description': 'string',
                                        'GroupId': 'string',
                                        'GroupName': 'string',
                                        'PeeringStatus': 'string',
                                        'UserId': 'string',
                                        'VpcId': 'string',
                                        'VpcPeeringConnectionId': 'string'
                                    },
                                ]
                            },
                        ],
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'VpcId': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SecurityGroups** *(list) --* 
              Information about one or more security groups.
              - *(dict) --* 
                Describes a security group
                - **Description** *(string) --* 
                  A description of the security group.
                - **GroupName** *(string) --* 
                  The name of the security group.
                - **IpPermissions** *(list) --* 
                  One or more inbound rules associated with the security group.
                  - *(dict) --* 
                    Describes a set of permissions for a security group rule.
                    - **FromPort** *(integer) --* 
                      The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of ``-1`` indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.
                    - **IpProtocol** *(string) --* 
                      The IP protocol name (``tcp`` , ``udp`` , ``icmp`` ) or number (see `Protocol Numbers <http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml>`__ ). 
                      [EC2-VPC only] Use ``-1`` to specify all protocols. When authorizing security group rules, specifying ``-1`` or a protocol number other than ``tcp`` , ``udp`` , ``icmp`` , or ``58`` (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For ``tcp`` , ``udp`` , and ``icmp`` , you must specify a port range. For ``58`` (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed when authorizing rules. 
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
                - **OwnerId** *(string) --* 
                  The AWS account ID of the owner of the security group.
                - **GroupId** *(string) --* 
                  The ID of the security group.
                - **IpPermissionsEgress** *(list) --* 
                  [EC2-VPC] One or more outbound rules associated with the security group.
                  - *(dict) --* 
                    Describes a set of permissions for a security group rule.
                    - **FromPort** *(integer) --* 
                      The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of ``-1`` indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.
                    - **IpProtocol** *(string) --* 
                      The IP protocol name (``tcp`` , ``udp`` , ``icmp`` ) or number (see `Protocol Numbers <http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml>`__ ). 
                      [EC2-VPC only] Use ``-1`` to specify all protocols. When authorizing security group rules, specifying ``-1`` or a protocol number other than ``tcp`` , ``udp`` , ``icmp`` , or ``58`` (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For ``tcp`` , ``udp`` , and ``icmp`` , you must specify a port range. For ``58`` (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed when authorizing rules. 
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
                - **Tags** *(list) --* 
                  Any tags assigned to the security group.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
                - **VpcId** *(string) --* 
                  [EC2-VPC] The ID of the VPC for the security group.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeSnapshots(Paginator):
    def paginate(self, Filters: List = None, OwnerIds: List = None, RestorableByUserIds: List = None, SnapshotIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_snapshots`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSnapshots>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              OwnerIds=[
                  'string',
              ],
              RestorableByUserIds=[
                  'string',
              ],
              SnapshotIds=[
                  'string',
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Snapshots': [
                    {
                        'DataEncryptionKeyId': 'string',
                        'Description': 'string',
                        'Encrypted': True|False,
                        'KmsKeyId': 'string',
                        'OwnerId': 'string',
                        'Progress': 'string',
                        'SnapshotId': 'string',
                        'StartTime': datetime(2015, 1, 1),
                        'State': 'pending'|'completed'|'error',
                        'StateMessage': 'string',
                        'VolumeId': 'string',
                        'VolumeSize': 123,
                        'OwnerAlias': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of DescribeSnapshots.
            - **Snapshots** *(list) --* 
              Information about the snapshots.
              - *(dict) --* 
                Describes a snapshot.
                - **DataEncryptionKeyId** *(string) --* 
                  The data encryption key identifier for the snapshot. This value is a unique identifier that corresponds to the data encryption key that was used to encrypt the original volume or snapshot copy. Because data encryption keys are inherited by volumes created from snapshots, and vice versa, if snapshots share the same data encryption key identifier, then they belong to the same volume/snapshot lineage. This parameter is only returned by the  DescribeSnapshots API operation.
                - **Description** *(string) --* 
                  The description for the snapshot.
                - **Encrypted** *(boolean) --* 
                  Indicates whether the snapshot is encrypted.
                - **KmsKeyId** *(string) --* 
                  The full ARN of the AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the volume encryption key for the parent volume.
                - **OwnerId** *(string) --* 
                  The AWS account ID of the EBS snapshot owner.
                - **Progress** *(string) --* 
                  The progress of the snapshot, as a percentage.
                - **SnapshotId** *(string) --* 
                  The ID of the snapshot. Each snapshot receives a unique identifier when it is created.
                - **StartTime** *(datetime) --* 
                  The time stamp when the snapshot was initiated.
                - **State** *(string) --* 
                  The snapshot state.
                - **StateMessage** *(string) --* 
                  Encrypted Amazon EBS snapshots are copied asynchronously. If a snapshot copy operation fails (for example, if the proper AWS Key Management Service (AWS KMS) permissions are not obtained) this field displays error state details to help you diagnose why the error occurred. This parameter is only returned by the  DescribeSnapshots API operation.
                - **VolumeId** *(string) --* 
                  The ID of the volume that was used to create the snapshot. Snapshots created by the  CopySnapshot action have an arbitrary volume ID that should not be used for any purpose.
                - **VolumeSize** *(integer) --* 
                  The size of the volume, in GiB.
                - **OwnerAlias** *(string) --* 
                  Value from an Amazon-maintained list (``amazon`` | ``aws-marketplace`` | ``microsoft`` ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM console. 
                - **Tags** *(list) --* 
                  Any tags assigned to the snapshot.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeSpotFleetInstances(Paginator):
    def paginate(self, SpotFleetRequestId: str, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_spot_fleet_instances`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSpotFleetInstances>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              SpotFleetRequestId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ActiveInstances': [
                    {
                        'InstanceId': 'string',
                        'InstanceType': 'string',
                        'SpotInstanceRequestId': 'string',
                        'InstanceHealth': 'healthy'|'unhealthy'
                    },
                ],
                'SpotFleetRequestId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of DescribeSpotFleetInstances.
            - **ActiveInstances** *(list) --* 
              The running instances. This list is refreshed periodically and might be out of date.
              - *(dict) --* 
                Describes a running instance in a Spot Fleet.
                - **InstanceId** *(string) --* 
                  The ID of the instance.
                - **InstanceType** *(string) --* 
                  The instance type.
                - **SpotInstanceRequestId** *(string) --* 
                  The ID of the Spot Instance request.
                - **InstanceHealth** *(string) --* 
                  The health status of the instance. If the status of either the instance status check or the system status check is ``impaired`` , the health status of the instance is ``unhealthy`` . Otherwise, the health status is ``healthy`` .
            - **SpotFleetRequestId** *(string) --* 
              The ID of the Spot Fleet request.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type SpotFleetRequestId: string
        :param SpotFleetRequestId: **[REQUIRED]**
          The ID of the Spot Fleet request.
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeSpotFleetRequests(Paginator):
    def paginate(self, DryRun: bool = None, SpotFleetRequestIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_spot_fleet_requests`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSpotFleetRequests>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              SpotFleetRequestIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'SpotFleetRequestConfigs': [
                    {
                        'ActivityStatus': 'error'|'pending_fulfillment'|'pending_termination'|'fulfilled',
                        'CreateTime': datetime(2015, 1, 1),
                        'SpotFleetRequestConfig': {
                            'AllocationStrategy': 'lowestPrice'|'diversified',
                            'OnDemandAllocationStrategy': 'lowestPrice'|'prioritized',
                            'ClientToken': 'string',
                            'ExcessCapacityTerminationPolicy': 'noTermination'|'default',
                            'FulfilledCapacity': 123.0,
                            'OnDemandFulfilledCapacity': 123.0,
                            'IamFleetRole': 'string',
                            'LaunchSpecifications': [
                                {
                                    'SecurityGroups': [
                                        {
                                            'GroupName': 'string',
                                            'GroupId': 'string'
                                        },
                                    ],
                                    'AddressingType': 'string',
                                    'BlockDeviceMappings': [
                                        {
                                            'DeviceName': 'string',
                                            'VirtualName': 'string',
                                            'Ebs': {
                                                'DeleteOnTermination': True|False,
                                                'Iops': 123,
                                                'SnapshotId': 'string',
                                                'VolumeSize': 123,
                                                'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                                                'Encrypted': True|False,
                                                'KmsKeyId': 'string'
                                            },
                                            'NoDevice': 'string'
                                        },
                                    ],
                                    'EbsOptimized': True|False,
                                    'IamInstanceProfile': {
                                        'Arn': 'string',
                                        'Name': 'string'
                                    },
                                    'ImageId': 'string',
                                    'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'t3.nano'|'t3.micro'|'t3.small'|'t3.medium'|'t3.large'|'t3.xlarge'|'t3.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.12xlarge'|'r5.24xlarge'|'r5.metal'|'r5a.large'|'r5a.xlarge'|'r5a.2xlarge'|'r5a.4xlarge'|'r5a.12xlarge'|'r5a.24xlarge'|'r5d.large'|'r5d.xlarge'|'r5d.2xlarge'|'r5d.4xlarge'|'r5d.12xlarge'|'r5d.24xlarge'|'r5d.metal'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'i3.metal'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'c5d.large'|'c5d.xlarge'|'c5d.2xlarge'|'c5d.4xlarge'|'c5d.9xlarge'|'c5d.18xlarge'|'c5n.large'|'c5n.xlarge'|'c5n.2xlarge'|'c5n.4xlarge'|'c5n.9xlarge'|'c5n.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'g3s.xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'p3dn.24xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.4xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'m5.metal'|'m5a.large'|'m5a.xlarge'|'m5a.2xlarge'|'m5a.4xlarge'|'m5a.12xlarge'|'m5a.24xlarge'|'m5d.large'|'m5d.xlarge'|'m5d.2xlarge'|'m5d.4xlarge'|'m5d.12xlarge'|'m5d.24xlarge'|'m5d.metal'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge'|'z1d.large'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'z1d.metal'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal'|'a1.medium'|'a1.large'|'a1.xlarge'|'a1.2xlarge'|'a1.4xlarge',
                                    'KernelId': 'string',
                                    'KeyName': 'string',
                                    'Monitoring': {
                                        'Enabled': True|False
                                    },
                                    'NetworkInterfaces': [
                                        {
                                            'AssociatePublicIpAddress': True|False,
                                            'DeleteOnTermination': True|False,
                                            'Description': 'string',
                                            'DeviceIndex': 123,
                                            'Groups': [
                                                'string',
                                            ],
                                            'Ipv6AddressCount': 123,
                                            'Ipv6Addresses': [
                                                {
                                                    'Ipv6Address': 'string'
                                                },
                                            ],
                                            'NetworkInterfaceId': 'string',
                                            'PrivateIpAddress': 'string',
                                            'PrivateIpAddresses': [
                                                {
                                                    'Primary': True|False,
                                                    'PrivateIpAddress': 'string'
                                                },
                                            ],
                                            'SecondaryPrivateIpAddressCount': 123,
                                            'SubnetId': 'string'
                                        },
                                    ],
                                    'Placement': {
                                        'AvailabilityZone': 'string',
                                        'GroupName': 'string',
                                        'Tenancy': 'default'|'dedicated'|'host'
                                    },
                                    'RamdiskId': 'string',
                                    'SpotPrice': 'string',
                                    'SubnetId': 'string',
                                    'UserData': 'string',
                                    'WeightedCapacity': 123.0,
                                    'TagSpecifications': [
                                        {
                                            'ResourceType': 'client-vpn-endpoint'|'customer-gateway'|'dedicated-host'|'dhcp-options'|'elastic-ip'|'fleet'|'fpga-image'|'image'|'instance'|'internet-gateway'|'launch-template'|'natgateway'|'network-acl'|'network-interface'|'reserved-instances'|'route-table'|'security-group'|'snapshot'|'spot-instances-request'|'subnet'|'transit-gateway'|'transit-gateway-attachment'|'transit-gateway-route-table'|'volume'|'vpc'|'vpc-peering-connection'|'vpn-connection'|'vpn-gateway',
                                            'Tags': [
                                                {
                                                    'Key': 'string',
                                                    'Value': 'string'
                                                },
                                            ]
                                        },
                                    ]
                                },
                            ],
                            'LaunchTemplateConfigs': [
                                {
                                    'LaunchTemplateSpecification': {
                                        'LaunchTemplateId': 'string',
                                        'LaunchTemplateName': 'string',
                                        'Version': 'string'
                                    },
                                    'Overrides': [
                                        {
                                            'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'t3.nano'|'t3.micro'|'t3.small'|'t3.medium'|'t3.large'|'t3.xlarge'|'t3.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.12xlarge'|'r5.24xlarge'|'r5.metal'|'r5a.large'|'r5a.xlarge'|'r5a.2xlarge'|'r5a.4xlarge'|'r5a.12xlarge'|'r5a.24xlarge'|'r5d.large'|'r5d.xlarge'|'r5d.2xlarge'|'r5d.4xlarge'|'r5d.12xlarge'|'r5d.24xlarge'|'r5d.metal'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'i3.metal'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'c5d.large'|'c5d.xlarge'|'c5d.2xlarge'|'c5d.4xlarge'|'c5d.9xlarge'|'c5d.18xlarge'|'c5n.large'|'c5n.xlarge'|'c5n.2xlarge'|'c5n.4xlarge'|'c5n.9xlarge'|'c5n.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'g3s.xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'p3dn.24xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.4xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'m5.metal'|'m5a.large'|'m5a.xlarge'|'m5a.2xlarge'|'m5a.4xlarge'|'m5a.12xlarge'|'m5a.24xlarge'|'m5d.large'|'m5d.xlarge'|'m5d.2xlarge'|'m5d.4xlarge'|'m5d.12xlarge'|'m5d.24xlarge'|'m5d.metal'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge'|'z1d.large'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'z1d.metal'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal'|'a1.medium'|'a1.large'|'a1.xlarge'|'a1.2xlarge'|'a1.4xlarge',
                                            'SpotPrice': 'string',
                                            'SubnetId': 'string',
                                            'AvailabilityZone': 'string',
                                            'WeightedCapacity': 123.0,
                                            'Priority': 123.0
                                        },
                                    ]
                                },
                            ],
                            'SpotPrice': 'string',
                            'TargetCapacity': 123,
                            'OnDemandTargetCapacity': 123,
                            'TerminateInstancesWithExpiration': True|False,
                            'Type': 'request'|'maintain'|'instant',
                            'ValidFrom': datetime(2015, 1, 1),
                            'ValidUntil': datetime(2015, 1, 1),
                            'ReplaceUnhealthyInstances': True|False,
                            'InstanceInterruptionBehavior': 'hibernate'|'stop'|'terminate',
                            'LoadBalancersConfig': {
                                'ClassicLoadBalancersConfig': {
                                    'ClassicLoadBalancers': [
                                        {
                                            'Name': 'string'
                                        },
                                    ]
                                },
                                'TargetGroupsConfig': {
                                    'TargetGroups': [
                                        {
                                            'Arn': 'string'
                                        },
                                    ]
                                }
                            },
                            'InstancePoolsToUseCount': 123
                        },
                        'SpotFleetRequestId': 'string',
                        'SpotFleetRequestState': 'submitted'|'active'|'cancelled'|'failed'|'cancelled_running'|'cancelled_terminating'|'modifying'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of DescribeSpotFleetRequests.
            - **SpotFleetRequestConfigs** *(list) --* 
              Information about the configuration of your Spot Fleet.
              - *(dict) --* 
                Describes a Spot Fleet request.
                - **ActivityStatus** *(string) --* 
                  The progress of the Spot Fleet request. If there is an error, the status is ``error`` . After all requests are placed, the status is ``pending_fulfillment`` . If the size of the fleet is equal to or greater than its target capacity, the status is ``fulfilled`` . If the size of the fleet is decreased, the status is ``pending_termination`` while Spot Instances are terminating.
                - **CreateTime** *(datetime) --* 
                  The creation date and time of the request.
                - **SpotFleetRequestConfig** *(dict) --* 
                  The configuration of the Spot Fleet request.
                  - **AllocationStrategy** *(string) --* 
                    Indicates how to allocate the target capacity across the Spot pools specified by the Spot Fleet request. The default is ``lowestPrice`` .
                  - **OnDemandAllocationStrategy** *(string) --* 
                    The order of the launch template overrides to use in fulfilling On-Demand capacity. If you specify ``lowestPrice`` , Spot Fleet uses price to determine the order, launching the lowest price first. If you specify ``prioritized`` , Spot Fleet uses the priority that you assign to each Spot Fleet launch template override, launching the highest priority first. If you do not specify a value, Spot Fleet defaults to ``lowestPrice`` .
                  - **ClientToken** *(string) --* 
                    A unique, case-sensitive identifier that you provide to ensure the idempotency of your listings. This helps to avoid duplicate listings. For more information, see `Ensuring Idempotency <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html>`__ .
                  - **ExcessCapacityTerminationPolicy** *(string) --* 
                    Indicates whether running Spot Instances should be terminated if the target capacity of the Spot Fleet request is decreased below the current size of the Spot Fleet.
                  - **FulfilledCapacity** *(float) --* 
                    The number of units fulfilled by this request compared to the set target capacity. You cannot set this value.
                  - **OnDemandFulfilledCapacity** *(float) --* 
                    The number of On-Demand units fulfilled by this request compared to the set target On-Demand capacity.
                  - **IamFleetRole** *(string) --* 
                    Grants the Spot Fleet permission to terminate Spot Instances on your behalf when you cancel its Spot Fleet request using  CancelSpotFleetRequests or when the Spot Fleet request expires, if you set ``terminateInstancesWithExpiration`` .
                  - **LaunchSpecifications** *(list) --* 
                    The launch specifications for the Spot Fleet request.
                    - *(dict) --* 
                      Describes the launch specification for one or more Spot Instances.
                      - **SecurityGroups** *(list) --* 
                        One or more security groups. When requesting instances in a VPC, you must specify the IDs of the security groups. When requesting instances in EC2-Classic, you can specify the names or the IDs of the security groups.
                        - *(dict) --* 
                          Describes a security group.
                          - **GroupName** *(string) --* 
                            The name of the security group.
                          - **GroupId** *(string) --* 
                            The ID of the security group.
                      - **AddressingType** *(string) --* 
                        Deprecated.
                      - **BlockDeviceMappings** *(list) --* 
                        One or more block device mapping entries. You can't specify both a snapshot ID and an encryption value. This is because only blank volumes can be encrypted on creation. If a snapshot is the basis for a volume, it is not blank and its encryption status is used for the volume encryption status.
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
                              The number of I/O operations per second (IOPS) that the volume supports. For ``io1`` , this represents the number of IOPS that are provisioned for the volume. For ``gp2`` , this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see `Amazon EBS Volume Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
                              Constraints: Range is 100-16,000 IOPS for ``gp2`` volumes and 100 to 64,000IOPS for ``io1`` volumes in most Regions. Maximum ``io1`` IOPS of 64,000 is guaranteed only on `Nitro-based instances <AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances>`__ . Other instance families guarantee performance up to 32,000 IOPS. For more information, see `Amazon EBS Volume Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
                              Condition: This parameter is required for requests to create ``io1`` volumes; it is not used in requests to create ``gp2`` , ``st1`` , ``sc1`` , or ``standard`` volumes.
                            - **SnapshotId** *(string) --* 
                              The ID of the snapshot.
                            - **VolumeSize** *(integer) --* 
                              The size of the volume, in GiB.
                              Constraints: 1-16384 for General Purpose SSD (``gp2`` ), 4-16384 for Provisioned IOPS SSD (``io1`` ), 500-16384 for Throughput Optimized HDD (``st1`` ), 500-16384 for Cold HDD (``sc1`` ), and 1-1024 for Magnetic (``standard`` ) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
                              Default: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.
                            - **VolumeType** *(string) --* 
                              The volume type: ``gp2`` , ``io1`` , ``st1`` , ``sc1`` , or ``standard`` .
                              Default: ``standard``  
                            - **Encrypted** *(boolean) --* 
                              Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. 
                              If you are creating a volume from a snapshot, you cannot specify an encryption value. This is because only blank volumes can be encrypted on creation. If you are creating a snapshot from an existing EBS volume, you cannot specify an encryption value that differs from that of the EBS volume. We recommend that you omit the encryption value from the block device mappings when creating an image from an instance.
                            - **KmsKeyId** *(string) --* 
                              Identifier (key ID, key alias, ID ARN, or alias ARN) for a user-managed CMK under which the EBS volume is encrypted.
                              This parameter is only supported on ``BlockDeviceMapping`` objects called by `RunInstances <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html>`__ , `RequestSpotFleet <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet.html>`__ , and `RequestSpotInstances <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html>`__ .
                          - **NoDevice** *(string) --* 
                            Suppresses the specified device included in the block device mapping of the AMI.
                      - **EbsOptimized** *(boolean) --* 
                        Indicates whether the instances are optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.
                        Default: ``false``  
                      - **IamInstanceProfile** *(dict) --* 
                        The IAM instance profile.
                        - **Arn** *(string) --* 
                          The Amazon Resource Name (ARN) of the instance profile.
                        - **Name** *(string) --* 
                          The name of the instance profile.
                      - **ImageId** *(string) --* 
                        The ID of the AMI.
                      - **InstanceType** *(string) --* 
                        The instance type.
                      - **KernelId** *(string) --* 
                        The ID of the kernel.
                      - **KeyName** *(string) --* 
                        The name of the key pair.
                      - **Monitoring** *(dict) --* 
                        Enable or disable monitoring for the instances.
                        - **Enabled** *(boolean) --* 
                          Enables monitoring for the instance.
                          Default: ``false``  
                      - **NetworkInterfaces** *(list) --* 
                        One or more network interfaces. If you specify a network interface, you must specify subnet IDs and security group IDs using the network interface.
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
                            A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.
                          - **Ipv6Addresses** *(list) --* 
                            One or more IPv6 addresses to assign to the network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.
                            - *(dict) --* 
                              Describes an IPv6 address.
                              - **Ipv6Address** *(string) --* 
                                The IPv6 address.
                          - **NetworkInterfaceId** *(string) --* 
                            The ID of the network interface.
                          - **PrivateIpAddress** *(string) --* 
                            The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a  RunInstances request.
                          - **PrivateIpAddresses** *(list) --* 
                            One or more private IPv4 addresses to assign to the network interface. Only one private IPv4 address can be designated as primary. You cannot specify this option if you're launching more than one instance in a  RunInstances request.
                            - *(dict) --* 
                              Describes a secondary private IPv4 address for a network interface.
                              - **Primary** *(boolean) --* 
                                Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.
                              - **PrivateIpAddress** *(string) --* 
                                The private IPv4 addresses.
                          - **SecondaryPrivateIpAddressCount** *(integer) --* 
                            The number of secondary private IPv4 addresses. You can't specify this option and specify more than one private IP address using the private IP addresses option. You cannot specify this option if you're launching more than one instance in a  RunInstances request.
                          - **SubnetId** *(string) --* 
                            The ID of the subnet associated with the network string. Applies only if creating a network interface when launching an instance.
                      - **Placement** *(dict) --* 
                        The placement information.
                        - **AvailabilityZone** *(string) --* 
                          The Availability Zone.
                          [Spot Fleet only] To specify multiple Availability Zones, separate them using commas; for example, "us-west-2a, us-west-2b".
                        - **GroupName** *(string) --* 
                          The name of the placement group.
                        - **Tenancy** *(string) --* 
                          The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of ``dedicated`` runs on single-tenant hardware. The ``host`` tenancy is not supported for Spot Instances.
                      - **RamdiskId** *(string) --* 
                        The ID of the RAM disk.
                      - **SpotPrice** *(string) --* 
                        The maximum price per unit hour that you are willing to pay for a Spot Instance. If this value is not specified, the default is the Spot price specified for the fleet. To determine the Spot price per unit hour, divide the Spot price by the value of ``WeightedCapacity`` .
                      - **SubnetId** *(string) --* 
                        The ID of the subnet in which to launch the instances. To specify multiple subnets, separate them using commas; for example, "subnet-a61dafcf, subnet-65ea5f08".
                      - **UserData** *(string) --* 
                        The Base64-encoded user data to make available to the instances.
                      - **WeightedCapacity** *(float) --* 
                        The number of units provided by the specified instance type. These are the same units that you chose to set the target capacity in terms (instances or a performance characteristic such as vCPUs, memory, or I/O).
                        If the target capacity divided by this value is not a whole number, we round the number of instances to the next whole number. If this value is not specified, the default is 1.
                      - **TagSpecifications** *(list) --* 
                        The tags to apply during creation.
                        - *(dict) --* 
                          The tags for a Spot Fleet resource.
                          - **ResourceType** *(string) --* 
                            The type of resource. Currently, the only resource type that is supported is ``instance`` .
                          - **Tags** *(list) --* 
                            The tags.
                            - *(dict) --* 
                              Describes a tag.
                              - **Key** *(string) --* 
                                The key of the tag.
                                Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                              - **Value** *(string) --* 
                                The value of the tag.
                                Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
                  - **LaunchTemplateConfigs** *(list) --* 
                    The launch template and overrides.
                    - *(dict) --* 
                      Describes a launch template and overrides.
                      - **LaunchTemplateSpecification** *(dict) --* 
                        The launch template.
                        - **LaunchTemplateId** *(string) --* 
                          The ID of the launch template. You must specify either a template ID or a template name.
                        - **LaunchTemplateName** *(string) --* 
                          The name of the launch template. You must specify either a template name or a template ID.
                        - **Version** *(string) --* 
                          The version number of the launch template. You must specify a version number.
                      - **Overrides** *(list) --* 
                        Any parameters that you specify override the same parameters in the launch template.
                        - *(dict) --* 
                          Describes overrides for a launch template.
                          - **InstanceType** *(string) --* 
                            The instance type.
                          - **SpotPrice** *(string) --* 
                            The maximum price per unit hour that you are willing to pay for a Spot Instance.
                          - **SubnetId** *(string) --* 
                            The ID of the subnet in which to launch the instances.
                          - **AvailabilityZone** *(string) --* 
                            The Availability Zone in which to launch the instances.
                          - **WeightedCapacity** *(float) --* 
                            The number of units provided by the specified instance type.
                          - **Priority** *(float) --* 
                            The priority for the launch template override. If **OnDemandAllocationStrategy** is set to ``prioritized`` , Spot Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity. The highest priority is launched first. Valid values are whole numbers starting at ``0`` . The lower the number, the higher the priority. If no number is set, the launch template override has the lowest priority.
                  - **SpotPrice** *(string) --* 
                    The maximum price per unit hour that you are willing to pay for a Spot Instance. The default is the On-Demand price.
                  - **TargetCapacity** *(integer) --* 
                    The number of units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is ``maintain`` , you can specify a target capacity of 0 and add capacity later.
                  - **OnDemandTargetCapacity** *(integer) --* 
                    The number of On-Demand units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is ``maintain`` , you can specify a target capacity of 0 and add capacity later.
                  - **TerminateInstancesWithExpiration** *(boolean) --* 
                    Indicates whether running Spot Instances should be terminated when the Spot Fleet request expires.
                  - **Type** *(string) --* 
                    The type of request. Indicates whether the Spot Fleet only requests the target capacity or also attempts to maintain it. When this value is ``request`` , the Spot Fleet only places the required requests. It does not attempt to replenish Spot Instances if capacity is diminished, nor does it submit requests in alternative Spot pools if capacity is not available. When this value is ``maintain`` , the Spot Fleet maintains the target capacity. The Spot Fleet places the required requests to meet capacity and automatically replenishes any interrupted instances. Default: ``maintain`` . ``instant`` is listed but is not used by Spot Fleet.
                  - **ValidFrom** *(datetime) --* 
                    The start date and time of the request, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z). The default is to start fulfilling the request immediately.
                  - **ValidUntil** *(datetime) --* 
                    The end date and time of the request, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z). At this point, no new Spot Instance requests are placed or able to fulfill the request. The default end date is 7 days from the current date.
                  - **ReplaceUnhealthyInstances** *(boolean) --* 
                    Indicates whether Spot Fleet should replace unhealthy instances.
                  - **InstanceInterruptionBehavior** *(string) --* 
                    The behavior when a Spot Instance is interrupted. The default is ``terminate`` .
                  - **LoadBalancersConfig** *(dict) --* 
                    One or more Classic Load Balancers and target groups to attach to the Spot Fleet request. Spot Fleet registers the running Spot Instances with the specified Classic Load Balancers and target groups.
                    With Network Load Balancers, Spot Fleet cannot register instances that have the following instance types: C1, CC1, CC2, CG1, CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, and T1.
                    - **ClassicLoadBalancersConfig** *(dict) --* 
                      The Classic Load Balancers.
                      - **ClassicLoadBalancers** *(list) --* 
                        One or more Classic Load Balancers.
                        - *(dict) --* 
                          Describes a Classic Load Balancer.
                          - **Name** *(string) --* 
                            The name of the load balancer.
                    - **TargetGroupsConfig** *(dict) --* 
                      The target groups.
                      - **TargetGroups** *(list) --* 
                        One or more target groups.
                        - *(dict) --* 
                          Describes a load balancer target group.
                          - **Arn** *(string) --* 
                            The Amazon Resource Name (ARN) of the target group.
                  - **InstancePoolsToUseCount** *(integer) --* 
                    The number of Spot pools across which to allocate your target Spot capacity. Valid only when Spot **AllocationStrategy** is set to ``lowest-price`` . Spot Fleet selects the cheapest Spot pools and evenly allocates your target Spot capacity across the number of Spot pools that you specify.
                - **SpotFleetRequestId** *(string) --* 
                  The ID of the Spot Fleet request.
                - **SpotFleetRequestState** *(string) --* 
                  The state of the Spot Fleet request.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type SpotFleetRequestIds: list
        :param SpotFleetRequestIds:
          The IDs of the Spot Fleet requests.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeSpotPriceHistory(Paginator):
    def paginate(self, Filters: List = None, AvailabilityZone: str = None, DryRun: bool = None, EndTime: datetime = None, InstanceTypes: List = None, ProductDescriptions: List = None, StartTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_spot_price_history`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSpotPriceHistory>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              AvailabilityZone='string',
              DryRun=True|False,
              EndTime=datetime(2015, 1, 1),
              InstanceTypes=[
                  't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'t3.nano'|'t3.micro'|'t3.small'|'t3.medium'|'t3.large'|'t3.xlarge'|'t3.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.12xlarge'|'r5.24xlarge'|'r5.metal'|'r5a.large'|'r5a.xlarge'|'r5a.2xlarge'|'r5a.4xlarge'|'r5a.12xlarge'|'r5a.24xlarge'|'r5d.large'|'r5d.xlarge'|'r5d.2xlarge'|'r5d.4xlarge'|'r5d.12xlarge'|'r5d.24xlarge'|'r5d.metal'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'i3.metal'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'c5d.large'|'c5d.xlarge'|'c5d.2xlarge'|'c5d.4xlarge'|'c5d.9xlarge'|'c5d.18xlarge'|'c5n.large'|'c5n.xlarge'|'c5n.2xlarge'|'c5n.4xlarge'|'c5n.9xlarge'|'c5n.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'g3s.xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'p3dn.24xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.4xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'m5.metal'|'m5a.large'|'m5a.xlarge'|'m5a.2xlarge'|'m5a.4xlarge'|'m5a.12xlarge'|'m5a.24xlarge'|'m5d.large'|'m5d.xlarge'|'m5d.2xlarge'|'m5d.4xlarge'|'m5d.12xlarge'|'m5d.24xlarge'|'m5d.metal'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge'|'z1d.large'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'z1d.metal'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal'|'a1.medium'|'a1.large'|'a1.xlarge'|'a1.2xlarge'|'a1.4xlarge',
              ],
              ProductDescriptions=[
                  'string',
              ],
              StartTime=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'SpotPriceHistory': [
                    {
                        'AvailabilityZone': 'string',
                        'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'t3.nano'|'t3.micro'|'t3.small'|'t3.medium'|'t3.large'|'t3.xlarge'|'t3.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.12xlarge'|'r5.24xlarge'|'r5.metal'|'r5a.large'|'r5a.xlarge'|'r5a.2xlarge'|'r5a.4xlarge'|'r5a.12xlarge'|'r5a.24xlarge'|'r5d.large'|'r5d.xlarge'|'r5d.2xlarge'|'r5d.4xlarge'|'r5d.12xlarge'|'r5d.24xlarge'|'r5d.metal'|'x1.16xlarge'|'x1.32xlarge'|'x1e.xlarge'|'x1e.2xlarge'|'x1e.4xlarge'|'x1e.8xlarge'|'x1e.16xlarge'|'x1e.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'i3.metal'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.18xlarge'|'c5d.large'|'c5d.xlarge'|'c5d.2xlarge'|'c5d.4xlarge'|'c5d.9xlarge'|'c5d.18xlarge'|'c5n.large'|'c5n.xlarge'|'c5n.2xlarge'|'c5n.4xlarge'|'c5n.9xlarge'|'c5n.18xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'g3.4xlarge'|'g3.8xlarge'|'g3.16xlarge'|'g3s.xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'p3.2xlarge'|'p3.8xlarge'|'p3.16xlarge'|'p3dn.24xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.4xlarge'|'f1.16xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.12xlarge'|'m5.24xlarge'|'m5.metal'|'m5a.large'|'m5a.xlarge'|'m5a.2xlarge'|'m5a.4xlarge'|'m5a.12xlarge'|'m5a.24xlarge'|'m5d.large'|'m5d.xlarge'|'m5d.2xlarge'|'m5d.4xlarge'|'m5d.12xlarge'|'m5d.24xlarge'|'m5d.metal'|'h1.2xlarge'|'h1.4xlarge'|'h1.8xlarge'|'h1.16xlarge'|'z1d.large'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'z1d.metal'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal'|'a1.medium'|'a1.large'|'a1.xlarge'|'a1.2xlarge'|'a1.4xlarge',
                        'ProductDescription': 'Linux/UNIX'|'Linux/UNIX (Amazon VPC)'|'Windows'|'Windows (Amazon VPC)',
                        'SpotPrice': 'string',
                        'Timestamp': datetime(2015, 1, 1)
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of DescribeSpotPriceHistory.
            - **SpotPriceHistory** *(list) --* 
              The historical Spot prices.
              - *(dict) --* 
                Describes the maximum price per hour that you are willing to pay for a Spot Instance.
                - **AvailabilityZone** *(string) --* 
                  The Availability Zone.
                - **InstanceType** *(string) --* 
                  The instance type.
                - **ProductDescription** *(string) --* 
                  A general description of the AMI.
                - **SpotPrice** *(string) --* 
                  The maximum price per hour that you are willing to pay for a Spot Instance.
                - **Timestamp** *(datetime) --* 
                  The date and time the request was created, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z).
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``availability-zone`` - The Availability Zone for which prices should be returned.
          * ``instance-type`` - The type of instance (for example, ``m3.medium`` ).
          * ``product-description`` - The product description for the Spot price (``Linux/UNIX`` | ``SUSE Linux`` | ``Windows`` | ``Linux/UNIX (Amazon VPC)`` | ``SUSE Linux (Amazon VPC)`` | ``Windows (Amazon VPC)`` ).
          * ``spot-price`` - The Spot price. The value must match exactly (or use wildcards; greater than or less than comparison is not supported).
          * ``timestamp`` - The time stamp of the Spot price history, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z). You can use wildcards (* and ?). Greater than or less than comparison is not supported.
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
        :type AvailabilityZone: string
        :param AvailabilityZone:
          Filters the results by the specified Availability Zone.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type EndTime: datetime
        :param EndTime:
          The date and time, up to the current date, from which to stop retrieving the price history data, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z).
        :type InstanceTypes: list
        :param InstanceTypes:
          Filters the results by the specified instance types.
          - *(string) --*
        :type ProductDescriptions: list
        :param ProductDescriptions:
          Filters the results by the specified basic product descriptions.
          - *(string) --*
        :type StartTime: datetime
        :param StartTime:
          The date and time, up to the past 90 days, from which to start retrieving the price history data, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z).
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeStaleSecurityGroups(Paginator):
    def paginate(self, VpcId: str, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_stale_security_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeStaleSecurityGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              VpcId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'StaleSecurityGroupSet': [
                    {
                        'Description': 'string',
                        'GroupId': 'string',
                        'GroupName': 'string',
                        'StaleIpPermissions': [
                            {
                                'FromPort': 123,
                                'IpProtocol': 'string',
                                'IpRanges': [
                                    'string',
                                ],
                                'PrefixListIds': [
                                    'string',
                                ],
                                'ToPort': 123,
                                'UserIdGroupPairs': [
                                    {
                                        'Description': 'string',
                                        'GroupId': 'string',
                                        'GroupName': 'string',
                                        'PeeringStatus': 'string',
                                        'UserId': 'string',
                                        'VpcId': 'string',
                                        'VpcPeeringConnectionId': 'string'
                                    },
                                ]
                            },
                        ],
                        'StaleIpPermissionsEgress': [
                            {
                                'FromPort': 123,
                                'IpProtocol': 'string',
                                'IpRanges': [
                                    'string',
                                ],
                                'PrefixListIds': [
                                    'string',
                                ],
                                'ToPort': 123,
                                'UserIdGroupPairs': [
                                    {
                                        'Description': 'string',
                                        'GroupId': 'string',
                                        'GroupName': 'string',
                                        'PeeringStatus': 'string',
                                        'UserId': 'string',
                                        'VpcId': 'string',
                                        'VpcPeeringConnectionId': 'string'
                                    },
                                ]
                            },
                        ],
                        'VpcId': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **StaleSecurityGroupSet** *(list) --* 
              Information about the stale security groups.
              - *(dict) --* 
                Describes a stale security group (a security group that contains stale rules).
                - **Description** *(string) --* 
                  The description of the security group.
                - **GroupId** *(string) --* 
                  The ID of the security group.
                - **GroupName** *(string) --* 
                  The name of the security group.
                - **StaleIpPermissions** *(list) --* 
                  Information about the stale inbound rules in the security group.
                  - *(dict) --* 
                    Describes a stale rule in a security group.
                    - **FromPort** *(integer) --* 
                      The start of the port range for the TCP and UDP protocols, or an ICMP type number. A value of ``-1`` indicates all ICMP types. 
                    - **IpProtocol** *(string) --* 
                      The IP protocol name (for ``tcp`` , ``udp`` , and ``icmp`` ) or number (see `Protocol Numbers) <http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml>`__ .
                    - **IpRanges** *(list) --* 
                      One or more IP ranges. Not applicable for stale security group rules.
                      - *(string) --* 
                    - **PrefixListIds** *(list) --* 
                      One or more prefix list IDs for an AWS service. Not applicable for stale security group rules.
                      - *(string) --* 
                    - **ToPort** *(integer) --* 
                      The end of the port range for the TCP and UDP protocols, or an ICMP type number. A value of ``-1`` indicates all ICMP types. 
                    - **UserIdGroupPairs** *(list) --* 
                      One or more security group pairs. Returns the ID of the referenced security group and VPC, and the ID and status of the VPC peering connection.
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
                - **StaleIpPermissionsEgress** *(list) --* 
                  Information about the stale outbound rules in the security group.
                  - *(dict) --* 
                    Describes a stale rule in a security group.
                    - **FromPort** *(integer) --* 
                      The start of the port range for the TCP and UDP protocols, or an ICMP type number. A value of ``-1`` indicates all ICMP types. 
                    - **IpProtocol** *(string) --* 
                      The IP protocol name (for ``tcp`` , ``udp`` , and ``icmp`` ) or number (see `Protocol Numbers) <http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml>`__ .
                    - **IpRanges** *(list) --* 
                      One or more IP ranges. Not applicable for stale security group rules.
                      - *(string) --* 
                    - **PrefixListIds** *(list) --* 
                      One or more prefix list IDs for an AWS service. Not applicable for stale security group rules.
                      - *(string) --* 
                    - **ToPort** *(integer) --* 
                      The end of the port range for the TCP and UDP protocols, or an ICMP type number. A value of ``-1`` indicates all ICMP types. 
                    - **UserIdGroupPairs** *(list) --* 
                      One or more security group pairs. Returns the ID of the referenced security group and VPC, and the ID and status of the VPC peering connection.
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
                - **VpcId** *(string) --* 
                  The ID of the VPC for the security group.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type VpcId: string
        :param VpcId: **[REQUIRED]**
          The ID of the VPC.
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeTags(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_tags`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeTags>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Tags': [
                    {
                        'Key': 'string',
                        'ResourceId': 'string',
                        'ResourceType': 'client-vpn-endpoint'|'customer-gateway'|'dedicated-host'|'dhcp-options'|'elastic-ip'|'fleet'|'fpga-image'|'image'|'instance'|'internet-gateway'|'launch-template'|'natgateway'|'network-acl'|'network-interface'|'reserved-instances'|'route-table'|'security-group'|'snapshot'|'spot-instances-request'|'subnet'|'transit-gateway'|'transit-gateway-attachment'|'transit-gateway-route-table'|'volume'|'vpc'|'vpc-peering-connection'|'vpn-connection'|'vpn-gateway',
                        'Value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Tags** *(list) --* 
              The tags.
              - *(dict) --* 
                Describes a tag.
                - **Key** *(string) --* 
                  The tag key.
                - **ResourceId** *(string) --* 
                  The ID of the resource.
                - **ResourceType** *(string) --* 
                  The resource type.
                - **Value** *(string) --* 
                  The tag value.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``key`` - The tag key.
          * ``resource-id`` - The ID of the resource.
          * ``resource-type`` - The resource type (``customer-gateway`` | ``dedicated-host`` | ``dhcp-options`` | ``elastic-ip`` | ``fleet`` | ``fpga-image`` | ``image`` | ``instance`` | ``internet-gateway`` | ``launch-template`` | ``natgateway`` | ``network-acl`` | ``network-interface`` | ``reserved-instances`` | ``route-table`` | ``security-group`` | ``snapshot`` | ``spot-instances-request`` | ``subnet`` | ``volume`` | ``vpc`` | ``vpc-peering-connection`` | ``vpn-connection`` | ``vpn-gateway`` ).
          * ``tag`` :<key> - The key/value combination of the tag. For example, specify \"tag:Owner\" for the filter name and \"TeamA\" for the filter value to find resources with the tag \"Owner=TeamA\".
          * ``value`` - The tag value.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeTransitGatewayAttachments(Paginator):
    def paginate(self, TransitGatewayAttachmentIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_transit_gateway_attachments`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeTransitGatewayAttachments>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              TransitGatewayAttachmentIds=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TransitGatewayAttachments': [
                    {
                        'TransitGatewayAttachmentId': 'string',
                        'TransitGatewayId': 'string',
                        'TransitGatewayOwnerId': 'string',
                        'ResourceOwnerId': 'string',
                        'ResourceType': 'vpc'|'vpn',
                        'ResourceId': 'string',
                        'State': 'pendingAcceptance'|'rollingBack'|'pending'|'available'|'modifying'|'deleting'|'deleted'|'failed'|'rejected'|'rejecting'|'failing',
                        'Association': {
                            'TransitGatewayRouteTableId': 'string',
                            'State': 'associating'|'associated'|'disassociating'|'disassociated'
                        },
                        'CreationTime': datetime(2015, 1, 1),
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TransitGatewayAttachments** *(list) --* 
              Information about the attachments.
              - *(dict) --* 
                Describes an attachment between a resource and a transit gateway.
                - **TransitGatewayAttachmentId** *(string) --* 
                  The ID of the attachment.
                - **TransitGatewayId** *(string) --* 
                  The ID of the transit gateway.
                - **TransitGatewayOwnerId** *(string) --* 
                  The ID of the AWS account that owns the transit gateway.
                - **ResourceOwnerId** *(string) --* 
                  The ID of the AWS account that owns the resource.
                - **ResourceType** *(string) --* 
                  The resource type.
                - **ResourceId** *(string) --* 
                  The ID of the resource.
                - **State** *(string) --* 
                  The attachment state.
                - **Association** *(dict) --* 
                  The association.
                  - **TransitGatewayRouteTableId** *(string) --* 
                    The ID of the route table for the transit gateway.
                  - **State** *(string) --* 
                    The state of the association.
                - **CreationTime** *(datetime) --* 
                  The creation time.
                - **Tags** *(list) --* 
                  The tags for the attachment.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        :type TransitGatewayAttachmentIds: list
        :param TransitGatewayAttachmentIds:
          The IDs of the attachments.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters. The possible values are:
          * ``association.state`` - The state of the association (``associating`` | ``associated`` | ``disassociating`` ).
          * ``association.transit-gateway-route-table-id`` - The ID of the route table for the transit gateway.
          * ``resource-id`` - The ID of the resource.
          * ``resource-owner-id`` - The ID of the AWS account that owns the resource.
          * ``resource-type`` - The resource type (``vpc`` | ``vpn`` ).
          * ``state`` - The state of the attachment (``available`` | ``deleted`` | ``deleting`` | ``failed`` | ``modifying`` | ``pendingAcceptance`` | ``pending`` | ``rollingBack`` | ``rejected`` | ``rejecting`` ).
          * ``transit-gateway-attachment-id`` - The ID of the attachment.
          * ``transit-gateway-id`` - The ID of the transit gateway.
          * ``transit-gateway-owner-id`` - The ID of the AWS account that owns the transit gateway.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeTransitGatewayRouteTables(Paginator):
    def paginate(self, TransitGatewayRouteTableIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_transit_gateway_route_tables`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeTransitGatewayRouteTables>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              TransitGatewayRouteTableIds=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TransitGatewayRouteTables': [
                    {
                        'TransitGatewayRouteTableId': 'string',
                        'TransitGatewayId': 'string',
                        'State': 'pending'|'available'|'deleting'|'deleted',
                        'DefaultAssociationRouteTable': True|False,
                        'DefaultPropagationRouteTable': True|False,
                        'CreationTime': datetime(2015, 1, 1),
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TransitGatewayRouteTables** *(list) --* 
              Information about the transit gateway route tables.
              - *(dict) --* 
                Describes a transit gateway route table.
                - **TransitGatewayRouteTableId** *(string) --* 
                  The ID of the transit gateway route table.
                - **TransitGatewayId** *(string) --* 
                  The ID of the transit gateway.
                - **State** *(string) --* 
                  The state of the transit gateway route table.
                - **DefaultAssociationRouteTable** *(boolean) --* 
                  Indicates whether this is the default association route table for the transit gateway.
                - **DefaultPropagationRouteTable** *(boolean) --* 
                  Indicates whether this is the default propagation route table for the transit gateway.
                - **CreationTime** *(datetime) --* 
                  The creation time.
                - **Tags** *(list) --* 
                  Any tags assigned to the route table.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        :type TransitGatewayRouteTableIds: list
        :param TransitGatewayRouteTableIds:
          The IDs of the transit gateway route tables.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters. The possible values are:
          * ``default-association-route-table`` - Indicates whether this is the default association route table for the transit gateway (``true`` | ``false`` ).
          * ``default-propagation-route-table`` - Indicates whether this is the default propagation route table for the transit gateway (``true`` | ``false`` ).
          * ``state`` - The state of the attachment (``available`` | ``deleted`` | ``deleting`` | ``failed`` | ``modifying`` | ``pendingAcceptance`` | ``pending`` | ``rollingBack`` | ``rejected`` | ``rejecting`` ).
          * ``transit-gateway-id`` - The ID of the transit gateway.
          * ``transit-gateway-route-table-id`` - The ID of the transit gateway route table.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeTransitGatewayVpcAttachments(Paginator):
    def paginate(self, TransitGatewayAttachmentIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_transit_gateway_vpc_attachments`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeTransitGatewayVpcAttachments>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              TransitGatewayAttachmentIds=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TransitGatewayVpcAttachments': [
                    {
                        'TransitGatewayAttachmentId': 'string',
                        'TransitGatewayId': 'string',
                        'VpcId': 'string',
                        'VpcOwnerId': 'string',
                        'State': 'pendingAcceptance'|'rollingBack'|'pending'|'available'|'modifying'|'deleting'|'deleted'|'failed'|'rejected'|'rejecting'|'failing',
                        'SubnetIds': [
                            'string',
                        ],
                        'CreationTime': datetime(2015, 1, 1),
                        'Options': {
                            'DnsSupport': 'enable'|'disable',
                            'Ipv6Support': 'enable'|'disable'
                        },
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TransitGatewayVpcAttachments** *(list) --* 
              Information about the VPC attachments.
              - *(dict) --* 
                Describes a VPC attachment.
                - **TransitGatewayAttachmentId** *(string) --* 
                  The ID of the attachment.
                - **TransitGatewayId** *(string) --* 
                  The ID of the transit gateway.
                - **VpcId** *(string) --* 
                  The ID of the VPC.
                - **VpcOwnerId** *(string) --* 
                  The ID of the AWS account that owns the VPC.
                - **State** *(string) --* 
                  The state of the VPC attachment.
                - **SubnetIds** *(list) --* 
                  The IDs of the subnets.
                  - *(string) --* 
                - **CreationTime** *(datetime) --* 
                  The creation time.
                - **Options** *(dict) --* 
                  The VPC attachment options.
                  - **DnsSupport** *(string) --* 
                    Indicates whether DNS support is enabled.
                  - **Ipv6Support** *(string) --* 
                    Indicates whether IPv6 support is enabled.
                - **Tags** *(list) --* 
                  The tags for the VPC attachment.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        :type TransitGatewayAttachmentIds: list
        :param TransitGatewayAttachmentIds:
          The IDs of the attachments.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters. The possible values are:
          * ``state`` - The state of the attachment (``available`` | ``deleted`` | ``deleting`` | ``failed`` | ``modifying`` | ``pendingAcceptance`` | ``pending`` | ``rollingBack`` | ``rejected`` | ``rejecting`` ).
          * ``transit-gateway-attachment-id`` - The ID of the attachment.
          * ``transit-gateway-id`` - The ID of the transit gateway.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeTransitGateways(Paginator):
    def paginate(self, TransitGatewayIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_transit_gateways`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeTransitGateways>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              TransitGatewayIds=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TransitGateways': [
                    {
                        'TransitGatewayId': 'string',
                        'TransitGatewayArn': 'string',
                        'State': 'pending'|'available'|'modifying'|'deleting'|'deleted',
                        'OwnerId': 'string',
                        'Description': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'Options': {
                            'AmazonSideAsn': 123,
                            'AutoAcceptSharedAttachments': 'enable'|'disable',
                            'DefaultRouteTableAssociation': 'enable'|'disable',
                            'AssociationDefaultRouteTableId': 'string',
                            'DefaultRouteTablePropagation': 'enable'|'disable',
                            'PropagationDefaultRouteTableId': 'string',
                            'VpnEcmpSupport': 'enable'|'disable',
                            'DnsSupport': 'enable'|'disable'
                        },
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TransitGateways** *(list) --* 
              Information about the transit gateways.
              - *(dict) --* 
                Describes a transit gateway.
                - **TransitGatewayId** *(string) --* 
                  The ID of the transit gateway.
                - **TransitGatewayArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the transit gateway.
                - **State** *(string) --* 
                  The state of the transit gateway.
                - **OwnerId** *(string) --* 
                  The ID of the AWS account ID that owns the transit gateway.
                - **Description** *(string) --* 
                  The description of the transit gateway.
                - **CreationTime** *(datetime) --* 
                  The creation time.
                - **Options** *(dict) --* 
                  The transit gateway options.
                  - **AmazonSideAsn** *(integer) --* 
                    A private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is 64512 to 65534 for 16-bit ASNs and 4200000000 to 4294967294 for 32-bit ASNs.
                  - **AutoAcceptSharedAttachments** *(string) --* 
                    Indicates whether attachment requests are automatically accepted.
                  - **DefaultRouteTableAssociation** *(string) --* 
                    Indicates whether resource attachments are automatically associated with the default association route table.
                  - **AssociationDefaultRouteTableId** *(string) --* 
                    The ID of the default association route table.
                  - **DefaultRouteTablePropagation** *(string) --* 
                    Indicates whether resource attachments automatically propagate routes to the default propagation route table.
                  - **PropagationDefaultRouteTableId** *(string) --* 
                    The ID of the default propagation route table.
                  - **VpnEcmpSupport** *(string) --* 
                    Indicates whether Equal Cost Multipath Protocol support is enabled.
                  - **DnsSupport** *(string) --* 
                    Indicates whether DNS support is enabled.
                - **Tags** *(list) --* 
                  The tags for the transit gateway.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        :type TransitGatewayIds: list
        :param TransitGatewayIds:
          The IDs of the transit gateways.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters. The possible values are:
          * ``options.propagation-default-route-table-id`` - The ID of the default propagation route table.
          * ``options.amazon-side-asn`` - The private ASN for the Amazon side of a BGP session.
          * ``options.association-default-route-table-id`` - The ID of the default association route table.
          * ``options.auto-accept-shared-attachments`` - Indicates whether there is automatic acceptance of attachment requests (``enable`` | ``disable`` ).
          * ``options.default-route-table-association`` - Indicates whether resource attachments are automatically associated with the default association route table (``enable`` | ``disable`` ).
          * ``options.default-route-table-propagation`` - Indicates whether resource attachments automatically propagate routes to the default propagation route table (``enable`` | ``disable`` ).
          * ``options.dns-support`` - Indicates whether DNS support is enabled (``enable`` | ``disable`` ).
          * ``options.vpn-ecmp-support`` - Indicates whether Equal Cost Multipath Protocol support is enabled (``enable`` | ``disable`` ).
          * ``owner-id`` - The ID of the AWS account that owns the transit gateway.
          * ``state`` - The state of the attachment (``available`` | ``deleted`` | ``deleting`` | ``failed`` | ``modifying`` | ``pendingAcceptance`` | ``pending`` | ``rollingBack`` | ``rejected`` | ``rejecting`` ).
          * ``transit-gateway-id`` - The ID of the transit gateway.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeVolumeStatus(Paginator):
    def paginate(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_volume_status`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumeStatus>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              VolumeIds=[
                  'string',
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'VolumeStatuses': [
                    {
                        'Actions': [
                            {
                                'Code': 'string',
                                'Description': 'string',
                                'EventId': 'string',
                                'EventType': 'string'
                            },
                        ],
                        'AvailabilityZone': 'string',
                        'Events': [
                            {
                                'Description': 'string',
                                'EventId': 'string',
                                'EventType': 'string',
                                'NotAfter': datetime(2015, 1, 1),
                                'NotBefore': datetime(2015, 1, 1)
                            },
                        ],
                        'VolumeId': 'string',
                        'VolumeStatus': {
                            'Details': [
                                {
                                    'Name': 'io-enabled'|'io-performance',
                                    'Status': 'string'
                                },
                            ],
                            'Status': 'ok'|'impaired'|'insufficient-data'
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of DescribeVolumeStatus.
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
        :type VolumeIds: list
        :param VolumeIds:
          One or more volume IDs.
          Default: Describes all your volumes.
          - *(string) --*
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeVolumes(Paginator):
    def paginate(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_volumes`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              VolumeIds=[
                  'string',
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Volumes': [
                    {
                        'Attachments': [
                            {
                                'AttachTime': datetime(2015, 1, 1),
                                'Device': 'string',
                                'InstanceId': 'string',
                                'State': 'attaching'|'attached'|'detaching'|'detached'|'busy',
                                'VolumeId': 'string',
                                'DeleteOnTermination': True|False
                            },
                        ],
                        'AvailabilityZone': 'string',
                        'CreateTime': datetime(2015, 1, 1),
                        'Encrypted': True|False,
                        'KmsKeyId': 'string',
                        'Size': 123,
                        'SnapshotId': 'string',
                        'State': 'creating'|'available'|'in-use'|'deleting'|'deleted'|'error',
                        'VolumeId': 'string',
                        'Iops': 123,
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of DescribeVolumes.
            - **Volumes** *(list) --* 
              Information about the volumes.
              - *(dict) --* 
                Describes a volume.
                - **Attachments** *(list) --* 
                  Information about the volume attachments.
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
                - **AvailabilityZone** *(string) --* 
                  The Availability Zone for the volume.
                - **CreateTime** *(datetime) --* 
                  The time stamp when volume creation was initiated.
                - **Encrypted** *(boolean) --* 
                  Indicates whether the volume will be encrypted.
                - **KmsKeyId** *(string) --* 
                  The full ARN of the AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the volume encryption key for the volume.
                - **Size** *(integer) --* 
                  The size of the volume, in GiBs.
                - **SnapshotId** *(string) --* 
                  The snapshot from which the volume was created, if applicable.
                - **State** *(string) --* 
                  The volume state.
                - **VolumeId** *(string) --* 
                  The ID of the volume.
                - **Iops** *(integer) --* 
                  The number of I/O operations per second (IOPS) that the volume supports. For Provisioned IOPS SSD volumes, this represents the number of IOPS that are provisioned for the volume. For General Purpose SSD volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see `Amazon EBS Volume Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
                  Constraints: Range is 100-16,000 IOPS for ``gp2`` volumes and 100 to 64,000IOPS for ``io1`` volumes in most regions. Maximum ``io1`` IOPS of 64,000 is guaranteed only on `Nitro-based instances <AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances>`__ . Other instance families guarantee performance up to 32,000 IOPS. For more information, see `Amazon EBS Volume Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
                  Condition: This parameter is required for requests to create ``io1`` volumes; it is not used in requests to create ``gp2`` , ``st1`` , ``sc1`` , or ``standard`` volumes.
                - **Tags** *(list) --* 
                  Any tags assigned to the volume.
                  - *(dict) --* 
                    Describes a tag.
                    - **Key** *(string) --* 
                      The key of the tag.
                      Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:`` .
                    - **Value** *(string) --* 
                      The value of the tag.
                      Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
                - **VolumeType** *(string) --* 
                  The volume type. This can be ``gp2`` for General Purpose SSD, ``io1`` for Provisioned IOPS SSD, ``st1`` for Throughput Optimized HDD, ``sc1`` for Cold HDD, or ``standard`` for Magnetic volumes.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeVolumesModifications(Paginator):
    def paginate(self, DryRun: bool = None, VolumeIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_volumes_modifications`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumesModifications>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              VolumeIds=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'VolumesModifications': [
                    {
                        'VolumeId': 'string',
                        'ModificationState': 'modifying'|'optimizing'|'completed'|'failed',
                        'StatusMessage': 'string',
                        'TargetSize': 123,
                        'TargetIops': 123,
                        'TargetVolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                        'OriginalSize': 123,
                        'OriginalIops': 123,
                        'OriginalVolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                        'Progress': 123,
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **VolumesModifications** *(list) --* 
              A list of returned  VolumeModification objects.
              - *(dict) --* 
                Describes the modification status of an EBS volume.
                If the volume has never been modified, some element values will be null.
                - **VolumeId** *(string) --* 
                  The ID of the volume.
                - **ModificationState** *(string) --* 
                  The current modification state. The modification state is null for unmodified volumes.
                - **StatusMessage** *(string) --* 
                  A status message about the modification progress or failure.
                - **TargetSize** *(integer) --* 
                  The target size of the volume, in GiB.
                - **TargetIops** *(integer) --* 
                  The target IOPS rate of the volume.
                - **TargetVolumeType** *(string) --* 
                  The target EBS volume type of the volume.
                - **OriginalSize** *(integer) --* 
                  The original size of the volume.
                - **OriginalIops** *(integer) --* 
                  The original IOPS rate of the volume.
                - **OriginalVolumeType** *(string) --* 
                  The original EBS volume type of the volume.
                - **Progress** *(integer) --* 
                  The modification progress, from 0 to 100 percent complete.
                - **StartTime** *(datetime) --* 
                  The modification start time.
                - **EndTime** *(datetime) --* 
                  The modification completion or failure time.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type VolumeIds: list
        :param VolumeIds:
          One or more volume IDs for which in-progress modifications will be described.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters. Supported filters: ``volume-id`` , ``modification-state`` , ``target-size`` , ``target-iops`` , ``target-volume-type`` , ``original-size`` , ``original-iops`` , ``original-volume-type`` , ``start-time`` .
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeVpcClassicLinkDnsSupport(Paginator):
    def paginate(self, VpcIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_vpc_classic_link_dns_support`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcClassicLinkDnsSupport>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              VpcIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Vpcs': [
                    {
                        'ClassicLinkDnsSupported': True|False,
                        'VpcId': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Vpcs** *(list) --* 
              Information about the ClassicLink DNS support status of the VPCs.
              - *(dict) --* 
                Describes the ClassicLink DNS support status of a VPC.
                - **ClassicLinkDnsSupported** *(boolean) --* 
                  Indicates whether ClassicLink DNS support is enabled for the VPC.
                - **VpcId** *(string) --* 
                  The ID of the VPC.
        :type VpcIds: list
        :param VpcIds:
          One or more VPC IDs.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeVpcEndpointConnectionNotifications(Paginator):
    def paginate(self, DryRun: bool = None, ConnectionNotificationId: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_vpc_endpoint_connection_notifications`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcEndpointConnectionNotifications>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              ConnectionNotificationId='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ConnectionNotificationSet': [
                    {
                        'ConnectionNotificationId': 'string',
                        'ServiceId': 'string',
                        'VpcEndpointId': 'string',
                        'ConnectionNotificationType': 'Topic',
                        'ConnectionNotificationArn': 'string',
                        'ConnectionEvents': [
                            'string',
                        ],
                        'ConnectionNotificationState': 'Enabled'|'Disabled'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ConnectionNotificationSet** *(list) --* 
              One or more notifications.
              - *(dict) --* 
                Describes a connection notification for a VPC endpoint or VPC endpoint service.
                - **ConnectionNotificationId** *(string) --* 
                  The ID of the notification.
                - **ServiceId** *(string) --* 
                  The ID of the endpoint service.
                - **VpcEndpointId** *(string) --* 
                  The ID of the VPC endpoint.
                - **ConnectionNotificationType** *(string) --* 
                  The type of notification.
                - **ConnectionNotificationArn** *(string) --* 
                  The ARN of the SNS topic for the notification.
                - **ConnectionEvents** *(list) --* 
                  The events for the notification. Valid values are ``Accept`` , ``Connect`` , ``Delete`` , and ``Reject`` .
                  - *(string) --* 
                - **ConnectionNotificationState** *(string) --* 
                  The state of the notification.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type ConnectionNotificationId: string
        :param ConnectionNotificationId:
          The ID of the notification.
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``connection-notification-arn`` - The ARN of SNS topic for the notification.
          * ``connection-notification-id`` - The ID of the notification.
          * ``connection-notification-state`` - The state of the notification (``Enabled`` | ``Disabled`` ).
          * ``connection-notification-type`` - The type of notification (``Topic`` ).
          * ``service-id`` - The ID of the endpoint service.
          * ``vpc-endpoint-id`` - The ID of the VPC endpoint.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeVpcEndpointConnections(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_vpc_endpoint_connections`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcEndpointConnections>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'VpcEndpointConnections': [
                    {
                        'ServiceId': 'string',
                        'VpcEndpointId': 'string',
                        'VpcEndpointOwner': 'string',
                        'VpcEndpointState': 'PendingAcceptance'|'Pending'|'Available'|'Deleting'|'Deleted'|'Rejected'|'Failed'|'Expired',
                        'CreationTimestamp': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **VpcEndpointConnections** *(list) --* 
              Information about one or more VPC endpoint connections.
              - *(dict) --* 
                Describes a VPC endpoint connection to a service.
                - **ServiceId** *(string) --* 
                  The ID of the service to which the endpoint is connected.
                - **VpcEndpointId** *(string) --* 
                  The ID of the VPC endpoint.
                - **VpcEndpointOwner** *(string) --* 
                  The AWS account ID of the owner of the VPC endpoint.
                - **VpcEndpointState** *(string) --* 
                  The state of the VPC endpoint.
                - **CreationTimestamp** *(datetime) --* 
                  The date and time the VPC endpoint was created.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``service-id`` - The ID of the service.
          * ``vpc-endpoint-owner`` - The AWS account number of the owner of the endpoint.
          * ``vpc-endpoint-state`` - The state of the endpoint (``pendingAcceptance`` | ``pending`` | ``available`` | ``deleting`` | ``deleted`` | ``rejected`` | ``failed`` ).
          * ``vpc-endpoint-id`` - The ID of the endpoint.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeVpcEndpointServiceConfigurations(Paginator):
    def paginate(self, DryRun: bool = None, ServiceIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_vpc_endpoint_service_configurations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcEndpointServiceConfigurations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              ServiceIds=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ServiceConfigurations': [
                    {
                        'ServiceType': [
                            {
                                'ServiceType': 'Interface'|'Gateway'
                            },
                        ],
                        'ServiceId': 'string',
                        'ServiceName': 'string',
                        'ServiceState': 'Pending'|'Available'|'Deleting'|'Deleted'|'Failed',
                        'AvailabilityZones': [
                            'string',
                        ],
                        'AcceptanceRequired': True|False,
                        'NetworkLoadBalancerArns': [
                            'string',
                        ],
                        'BaseEndpointDnsNames': [
                            'string',
                        ],
                        'PrivateDnsName': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ServiceConfigurations** *(list) --* 
              Information about one or more services.
              - *(dict) --* 
                Describes a service configuration for a VPC endpoint service.
                - **ServiceType** *(list) --* 
                  The type of service.
                  - *(dict) --* 
                    Describes the type of service for a VPC endpoint.
                    - **ServiceType** *(string) --* 
                      The type of service.
                - **ServiceId** *(string) --* 
                  The ID of the service.
                - **ServiceName** *(string) --* 
                  The name of the service.
                - **ServiceState** *(string) --* 
                  The service state.
                - **AvailabilityZones** *(list) --* 
                  In the Availability Zones in which the service is available.
                  - *(string) --* 
                - **AcceptanceRequired** *(boolean) --* 
                  Indicates whether requests from other AWS accounts to create an endpoint to the service must first be accepted.
                - **NetworkLoadBalancerArns** *(list) --* 
                  The Amazon Resource Names (ARNs) of the Network Load Balancers for the service.
                  - *(string) --* 
                - **BaseEndpointDnsNames** *(list) --* 
                  The DNS names for the service.
                  - *(string) --* 
                - **PrivateDnsName** *(string) --* 
                  The private DNS name for the service.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type ServiceIds: list
        :param ServiceIds:
          The IDs of one or more services.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``service-name`` - The name of the service.
          * ``service-id`` - The ID of the service.
          * ``service-state`` - The state of the service (``Pending`` | ``Available`` | ``Deleting`` | ``Deleted`` | ``Failed`` ).
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeVpcEndpointServicePermissions(Paginator):
    def paginate(self, ServiceId: str, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_vpc_endpoint_service_permissions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcEndpointServicePermissions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              ServiceId='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'AllowedPrincipals': [
                    {
                        'PrincipalType': 'All'|'Service'|'OrganizationUnit'|'Account'|'User'|'Role',
                        'Principal': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AllowedPrincipals** *(list) --* 
              Information about one or more allowed principals.
              - *(dict) --* 
                Describes a principal.
                - **PrincipalType** *(string) --* 
                  The type of principal.
                - **Principal** *(string) --* 
                  The Amazon Resource Name (ARN) of the principal.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type ServiceId: string
        :param ServiceId: **[REQUIRED]**
          The ID of the service.
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``principal`` - The ARN of the principal.
          * ``principal-type`` - The principal type (``All`` | ``Service`` | ``OrganizationUnit`` | ``Account`` | ``User`` | ``Role`` ).
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeVpcEndpointServices(Paginator):
    def paginate(self, DryRun: bool = None, ServiceNames: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_vpc_endpoint_services`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcEndpointServices>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              ServiceNames=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ServiceNames': [
                    'string',
                ],
                'ServiceDetails': [
                    {
                        'ServiceName': 'string',
                        'ServiceType': [
                            {
                                'ServiceType': 'Interface'|'Gateway'
                            },
                        ],
                        'AvailabilityZones': [
                            'string',
                        ],
                        'Owner': 'string',
                        'BaseEndpointDnsNames': [
                            'string',
                        ],
                        'PrivateDnsName': 'string',
                        'VpcEndpointPolicySupported': True|False,
                        'AcceptanceRequired': True|False
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of DescribeVpcEndpointServices.
            - **ServiceNames** *(list) --* 
              A list of supported services.
              - *(string) --* 
            - **ServiceDetails** *(list) --* 
              Information about the service.
              - *(dict) --* 
                Describes a VPC endpoint service.
                - **ServiceName** *(string) --* 
                  The Amazon Resource Name (ARN) of the service.
                - **ServiceType** *(list) --* 
                  The type of service.
                  - *(dict) --* 
                    Describes the type of service for a VPC endpoint.
                    - **ServiceType** *(string) --* 
                      The type of service.
                - **AvailabilityZones** *(list) --* 
                  The Availability Zones in which the service is available.
                  - *(string) --* 
                - **Owner** *(string) --* 
                  The AWS account ID of the service owner.
                - **BaseEndpointDnsNames** *(list) --* 
                  The DNS names for the service.
                  - *(string) --* 
                - **PrivateDnsName** *(string) --* 
                  The private DNS name for the service.
                - **VpcEndpointPolicySupported** *(boolean) --* 
                  Indicates whether the service supports endpoint policies.
                - **AcceptanceRequired** *(boolean) --* 
                  Indicates whether VPC endpoint connection requests to the service must be accepted by the service owner.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type ServiceNames: list
        :param ServiceNames:
          One or more service names.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``service-name`` : The name of the service.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeVpcEndpoints(Paginator):
    def paginate(self, DryRun: bool = None, VpcEndpointIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_vpc_endpoints`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcEndpoints>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DryRun=True|False,
              VpcEndpointIds=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'VpcEndpoints': [
                    {
                        'VpcEndpointId': 'string',
                        'VpcEndpointType': 'Interface'|'Gateway',
                        'VpcId': 'string',
                        'ServiceName': 'string',
                        'State': 'PendingAcceptance'|'Pending'|'Available'|'Deleting'|'Deleted'|'Rejected'|'Failed'|'Expired',
                        'PolicyDocument': 'string',
                        'RouteTableIds': [
                            'string',
                        ],
                        'SubnetIds': [
                            'string',
                        ],
                        'Groups': [
                            {
                                'GroupId': 'string',
                                'GroupName': 'string'
                            },
                        ],
                        'PrivateDnsEnabled': True|False,
                        'NetworkInterfaceIds': [
                            'string',
                        ],
                        'DnsEntries': [
                            {
                                'DnsName': 'string',
                                'HostedZoneId': 'string'
                            },
                        ],
                        'CreationTimestamp': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of DescribeVpcEndpoints.
            - **VpcEndpoints** *(list) --* 
              Information about the endpoints.
              - *(dict) --* 
                Describes a VPC endpoint.
                - **VpcEndpointId** *(string) --* 
                  The ID of the VPC endpoint.
                - **VpcEndpointType** *(string) --* 
                  The type of endpoint.
                - **VpcId** *(string) --* 
                  The ID of the VPC to which the endpoint is associated.
                - **ServiceName** *(string) --* 
                  The name of the service to which the endpoint is associated.
                - **State** *(string) --* 
                  The state of the VPC endpoint.
                - **PolicyDocument** *(string) --* 
                  The policy document associated with the endpoint, if applicable.
                - **RouteTableIds** *(list) --* 
                  (Gateway endpoint) One or more route tables associated with the endpoint.
                  - *(string) --* 
                - **SubnetIds** *(list) --* 
                  (Interface endpoint) One or more subnets in which the endpoint is located.
                  - *(string) --* 
                - **Groups** *(list) --* 
                  (Interface endpoint) Information about the security groups associated with the network interface.
                  - *(dict) --* 
                    Describes a security group.
                    - **GroupId** *(string) --* 
                      The ID of the security group.
                    - **GroupName** *(string) --* 
                      The name of the security group.
                - **PrivateDnsEnabled** *(boolean) --* 
                  (Interface endpoint) Indicates whether the VPC is associated with a private hosted zone.
                - **NetworkInterfaceIds** *(list) --* 
                  (Interface endpoint) One or more network interfaces for the endpoint.
                  - *(string) --* 
                - **DnsEntries** *(list) --* 
                  (Interface endpoint) The DNS entries for the endpoint.
                  - *(dict) --* 
                    Describes a DNS entry.
                    - **DnsName** *(string) --* 
                      The DNS name.
                    - **HostedZoneId** *(string) --* 
                      The ID of the private hosted zone.
                - **CreationTimestamp** *(datetime) --* 
                  The date and time the VPC endpoint was created.
        :type DryRun: boolean
        :param DryRun:
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        :type VpcEndpointIds: list
        :param VpcEndpointIds:
          One or more endpoint IDs.
          - *(string) --*
        :type Filters: list
        :param Filters:
          One or more filters.
          * ``service-name`` : The name of the service.
          * ``vpc-id`` : The ID of the VPC in which the endpoint resides.
          * ``vpc-endpoint-id`` : The ID of the endpoint.
          * ``vpc-endpoint-state`` : The state of the endpoint. (``pending`` | ``available`` | ``deleting`` | ``deleted`` )
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeVpcPeeringConnections(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.describe_vpc_peering_connections`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcPeeringConnections>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              VpcPeeringConnectionIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'VpcPeeringConnections': [
                    {
                        'AccepterVpcInfo': {
                            'CidrBlock': 'string',
                            'Ipv6CidrBlockSet': [
                                {
                                    'Ipv6CidrBlock': 'string'
                                },
                            ],
                            'CidrBlockSet': [
                                {
                                    'CidrBlock': 'string'
                                },
                            ],
                            'OwnerId': 'string',
                            'PeeringOptions': {
                                'AllowDnsResolutionFromRemoteVpc': True|False,
                                'AllowEgressFromLocalClassicLinkToRemoteVpc': True|False,
                                'AllowEgressFromLocalVpcToRemoteClassicLink': True|False
                            },
                            'VpcId': 'string',
                            'Region': 'string'
                        },
                        'ExpirationTime': datetime(2015, 1, 1),
                        'RequesterVpcInfo': {
                            'CidrBlock': 'string',
                            'Ipv6CidrBlockSet': [
                                {
                                    'Ipv6CidrBlock': 'string'
                                },
                            ],
                            'CidrBlockSet': [
                                {
                                    'CidrBlock': 'string'
                                },
                            ],
                            'OwnerId': 'string',
                            'PeeringOptions': {
                                'AllowDnsResolutionFromRemoteVpc': True|False,
                                'AllowEgressFromLocalClassicLinkToRemoteVpc': True|False,
                                'AllowEgressFromLocalVpcToRemoteClassicLink': True|False
                            },
                            'VpcId': 'string',
                            'Region': 'string'
                        },
                        'Status': {
                            'Code': 'initiating-request'|'pending-acceptance'|'active'|'deleted'|'rejected'|'failed'|'expired'|'provisioning'|'deleting',
                            'Message': 'string'
                        },
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'VpcPeeringConnectionId': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **VpcPeeringConnections** *(list) --* 
              Information about the VPC peering connections.
              - *(dict) --* 
                Describes a VPC peering connection.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class GetTransitGatewayAttachmentPropagations(Paginator):
    def paginate(self, TransitGatewayAttachmentId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.get_transit_gateway_attachment_propagations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/GetTransitGatewayAttachmentPropagations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              TransitGatewayAttachmentId='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TransitGatewayAttachmentPropagations': [
                    {
                        'TransitGatewayRouteTableId': 'string',
                        'State': 'enabling'|'enabled'|'disabling'|'disabled'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TransitGatewayAttachmentPropagations** *(list) --* 
              Information about the propagation route tables.
              - *(dict) --* 
                Describes a propagation route table.
                - **TransitGatewayRouteTableId** *(string) --* 
                  The ID of the propagation route table.
                - **State** *(string) --* 
                  The state of the propagation route table.
        :type TransitGatewayAttachmentId: string
        :param TransitGatewayAttachmentId: **[REQUIRED]**
          The ID of the attachment.
        :type Filters: list
        :param Filters:
          One or more filters. The possible values are:
          * ``transit-gateway-route-table-id`` - The ID of the transit gateway route table.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class GetTransitGatewayRouteTableAssociations(Paginator):
    def paginate(self, TransitGatewayRouteTableId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.get_transit_gateway_route_table_associations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/GetTransitGatewayRouteTableAssociations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              TransitGatewayRouteTableId='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Associations': [
                    {
                        'TransitGatewayAttachmentId': 'string',
                        'ResourceId': 'string',
                        'ResourceType': 'vpc'|'vpn',
                        'State': 'associating'|'associated'|'disassociating'|'disassociated'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Associations** *(list) --* 
              Information about the associations.
              - *(dict) --* 
                Describes an association between a route table and a resource attachment.
                - **TransitGatewayAttachmentId** *(string) --* 
                  The ID of the attachment.
                - **ResourceId** *(string) --* 
                  The ID of the resource.
                - **ResourceType** *(string) --* 
                  The resource type.
                - **State** *(string) --* 
                  The state of the association.
        :type TransitGatewayRouteTableId: string
        :param TransitGatewayRouteTableId: **[REQUIRED]**
          The ID of the transit gateway route table.
        :type Filters: list
        :param Filters:
          One or more filters. The possible values are:
          * ``resource-id`` - The ID of the resource.
          * ``resource-type`` - The resource type (``vpc`` | ``vpn`` ).
          * ``transit-gateway-attachment-id`` - The ID of the attachment.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class GetTransitGatewayRouteTablePropagations(Paginator):
    def paginate(self, TransitGatewayRouteTableId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`EC2.Client.get_transit_gateway_route_table_propagations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/GetTransitGatewayRouteTablePropagations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              TransitGatewayRouteTableId='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DryRun=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TransitGatewayRouteTablePropagations': [
                    {
                        'TransitGatewayAttachmentId': 'string',
                        'ResourceId': 'string',
                        'ResourceType': 'vpc'|'vpn',
                        'State': 'enabling'|'enabled'|'disabling'|'disabled'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TransitGatewayRouteTablePropagations** *(list) --* 
              Information about the route table propagations.
              - *(dict) --* 
                Describes a route table propagation.
                - **TransitGatewayAttachmentId** *(string) --* 
                  The ID of the attachment.
                - **ResourceId** *(string) --* 
                  The ID of the resource.
                - **ResourceType** *(string) --* 
                  The type of resource.
                - **State** *(string) --* 
                  The state of the resource.
        :type TransitGatewayRouteTableId: string
        :param TransitGatewayRouteTableId: **[REQUIRED]**
          The ID of the transit gateway route table.
        :type Filters: list
        :param Filters:
          One or more filters. The possible values are:
          * ``resource-id`` - The ID of the resource.
          * ``resource-type`` - The resource type (``vpc`` | ``vpn`` ).
          * ``transit-gateway-attachment-id`` - The ID of the attachment.
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
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass
