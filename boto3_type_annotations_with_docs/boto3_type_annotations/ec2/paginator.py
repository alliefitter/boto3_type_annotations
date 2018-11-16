from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeIamInstanceProfileAssociations(Paginator):
    def paginate(self, AssociationIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeIamInstanceProfileAssociations>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AssociationIds=[
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
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'IamInstanceProfileAssociations\': [
                    {
                        \'AssociationId\': \'string\',
                        \'InstanceId\': \'string\',
                        \'IamInstanceProfile\': {
                            \'Arn\': \'string\',
                            \'Id\': \'string\'
                        },
                        \'State\': \'associating\'|\'associated\'|\'disassociating\'|\'disassociated\',
                        \'Timestamp\': datetime(2015, 1, 1)
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
        
        """
        pass


class DescribeInstanceStatus(Paginator):
    def paginate(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, IncludeAllInstances: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstanceStatus>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
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
              IncludeAllInstances=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstanceStatuses\': [
                    {
                        \'AvailabilityZone\': \'string\',
                        \'Events\': [
                            {
                                \'Code\': \'instance-reboot\'|\'system-reboot\'|\'system-maintenance\'|\'instance-retirement\'|\'instance-stop\',
                                \'Description\': \'string\',
                                \'NotAfter\': datetime(2015, 1, 1),
                                \'NotBefore\': datetime(2015, 1, 1)
                            },
                        ],
                        \'InstanceId\': \'string\',
                        \'InstanceState\': {
                            \'Code\': 123,
                            \'Name\': \'pending\'|\'running\'|\'shutting-down\'|\'terminated\'|\'stopping\'|\'stopped\'
                        },
                        \'InstanceStatus\': {
                            \'Details\': [
                                {
                                    \'ImpairedSince\': datetime(2015, 1, 1),
                                    \'Name\': \'reachability\',
                                    \'Status\': \'passed\'|\'failed\'|\'insufficient-data\'|\'initializing\'
                                },
                            ],
                            \'Status\': \'ok\'|\'impaired\'|\'insufficient-data\'|\'not-applicable\'|\'initializing\'
                        },
                        \'SystemStatus\': {
                            \'Details\': [
                                {
                                    \'ImpairedSince\': datetime(2015, 1, 1),
                                    \'Name\': \'reachability\',
                                    \'Status\': \'passed\'|\'failed\'|\'insufficient-data\'|\'initializing\'
                                },
                            ],
                            \'Status\': \'ok\'|\'impaired\'|\'insufficient-data\'|\'not-applicable\'|\'initializing\'
                        }
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DescribeInstanceStatus.
        
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
        
        """
        pass


class DescribeInstances(Paginator):
    def paginate(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
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
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Reservations\': [
                    {
                        \'Groups\': [
                            {
                                \'GroupName\': \'string\',
                                \'GroupId\': \'string\'
                            },
                        ],
                        \'Instances\': [
                            {
                                \'AmiLaunchIndex\': 123,
                                \'ImageId\': \'string\',
                                \'InstanceId\': \'string\',
                                \'InstanceType\': \'t1.micro\'|\'t2.nano\'|\'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'t2.xlarge\'|\'t2.2xlarge\'|\'t3.nano\'|\'t3.micro\'|\'t3.small\'|\'t3.medium\'|\'t3.large\'|\'t3.xlarge\'|\'t3.2xlarge\'|\'m1.small\'|\'m1.medium\'|\'m1.large\'|\'m1.xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\'|\'m4.16xlarge\'|\'m2.xlarge\'|\'m2.2xlarge\'|\'m2.4xlarge\'|\'cr1.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'r5.large\'|\'r5.xlarge\'|\'r5.2xlarge\'|\'r5.4xlarge\'|\'r5.8xlarge\'|\'r5.12xlarge\'|\'r5.16xlarge\'|\'r5.24xlarge\'|\'r5.metal\'|\'r5a.large\'|\'r5a.xlarge\'|\'r5a.2xlarge\'|\'r5a.4xlarge\'|\'r5a.12xlarge\'|\'r5a.24xlarge\'|\'r5d.large\'|\'r5d.xlarge\'|\'r5d.2xlarge\'|\'r5d.4xlarge\'|\'r5d.8xlarge\'|\'r5d.12xlarge\'|\'r5d.16xlarge\'|\'r5d.24xlarge\'|\'r5d.metal\'|\'x1.16xlarge\'|\'x1.32xlarge\'|\'x1e.xlarge\'|\'x1e.2xlarge\'|\'x1e.4xlarge\'|\'x1e.8xlarge\'|\'x1e.16xlarge\'|\'x1e.32xlarge\'|\'i2.xlarge\'|\'i2.2xlarge\'|\'i2.4xlarge\'|\'i2.8xlarge\'|\'i3.large\'|\'i3.xlarge\'|\'i3.2xlarge\'|\'i3.4xlarge\'|\'i3.8xlarge\'|\'i3.16xlarge\'|\'i3.metal\'|\'hi1.4xlarge\'|\'hs1.8xlarge\'|\'c1.medium\'|\'c1.xlarge\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'c5.large\'|\'c5.xlarge\'|\'c5.2xlarge\'|\'c5.4xlarge\'|\'c5.9xlarge\'|\'c5.18xlarge\'|\'c5d.large\'|\'c5d.xlarge\'|\'c5d.2xlarge\'|\'c5d.4xlarge\'|\'c5d.9xlarge\'|\'c5d.18xlarge\'|\'cc1.4xlarge\'|\'cc2.8xlarge\'|\'g2.2xlarge\'|\'g2.8xlarge\'|\'g3.4xlarge\'|\'g3.8xlarge\'|\'g3.16xlarge\'|\'g3s.xlarge\'|\'cg1.4xlarge\'|\'p2.xlarge\'|\'p2.8xlarge\'|\'p2.16xlarge\'|\'p3.2xlarge\'|\'p3.8xlarge\'|\'p3.16xlarge\'|\'d2.xlarge\'|\'d2.2xlarge\'|\'d2.4xlarge\'|\'d2.8xlarge\'|\'f1.2xlarge\'|\'f1.4xlarge\'|\'f1.16xlarge\'|\'m5.large\'|\'m5.xlarge\'|\'m5.2xlarge\'|\'m5.4xlarge\'|\'m5.12xlarge\'|\'m5.24xlarge\'|\'m5a.large\'|\'m5a.xlarge\'|\'m5a.2xlarge\'|\'m5a.4xlarge\'|\'m5a.12xlarge\'|\'m5a.24xlarge\'|\'m5d.large\'|\'m5d.xlarge\'|\'m5d.2xlarge\'|\'m5d.4xlarge\'|\'m5d.12xlarge\'|\'m5d.24xlarge\'|\'h1.2xlarge\'|\'h1.4xlarge\'|\'h1.8xlarge\'|\'h1.16xlarge\'|\'z1d.large\'|\'z1d.xlarge\'|\'z1d.2xlarge\'|\'z1d.3xlarge\'|\'z1d.6xlarge\'|\'z1d.12xlarge\'|\'u-6tb1.metal\'|\'u-9tb1.metal\'|\'u-12tb1.metal\',
                                \'KernelId\': \'string\',
                                \'KeyName\': \'string\',
                                \'LaunchTime\': datetime(2015, 1, 1),
                                \'Monitoring\': {
                                    \'State\': \'disabled\'|\'disabling\'|\'enabled\'|\'pending\'
                                },
                                \'Placement\': {
                                    \'AvailabilityZone\': \'string\',
                                    \'Affinity\': \'string\',
                                    \'GroupName\': \'string\',
                                    \'HostId\': \'string\',
                                    \'Tenancy\': \'default\'|\'dedicated\'|\'host\',
                                    \'SpreadDomain\': \'string\'
                                },
                                \'Platform\': \'Windows\',
                                \'PrivateDnsName\': \'string\',
                                \'PrivateIpAddress\': \'string\',
                                \'ProductCodes\': [
                                    {
                                        \'ProductCodeId\': \'string\',
                                        \'ProductCodeType\': \'devpay\'|\'marketplace\'
                                    },
                                ],
                                \'PublicDnsName\': \'string\',
                                \'PublicIpAddress\': \'string\',
                                \'RamdiskId\': \'string\',
                                \'State\': {
                                    \'Code\': 123,
                                    \'Name\': \'pending\'|\'running\'|\'shutting-down\'|\'terminated\'|\'stopping\'|\'stopped\'
                                },
                                \'StateTransitionReason\': \'string\',
                                \'SubnetId\': \'string\',
                                \'VpcId\': \'string\',
                                \'Architecture\': \'i386\'|\'x86_64\',
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
                                \'ClientToken\': \'string\',
                                \'EbsOptimized\': True|False,
                                \'EnaSupport\': True|False,
                                \'Hypervisor\': \'ovm\'|\'xen\',
                                \'IamInstanceProfile\': {
                                    \'Arn\': \'string\',
                                    \'Id\': \'string\'
                                },
                                \'InstanceLifecycle\': \'spot\'|\'scheduled\',
                                \'ElasticGpuAssociations\': [
                                    {
                                        \'ElasticGpuId\': \'string\',
                                        \'ElasticGpuAssociationId\': \'string\',
                                        \'ElasticGpuAssociationState\': \'string\',
                                        \'ElasticGpuAssociationTime\': \'string\'
                                    },
                                ],
                                \'NetworkInterfaces\': [
                                    {
                                        \'Association\': {
                                            \'IpOwnerId\': \'string\',
                                            \'PublicDnsName\': \'string\',
                                            \'PublicIp\': \'string\'
                                        },
                                        \'Attachment\': {
                                            \'AttachTime\': datetime(2015, 1, 1),
                                            \'AttachmentId\': \'string\',
                                            \'DeleteOnTermination\': True|False,
                                            \'DeviceIndex\': 123,
                                            \'Status\': \'attaching\'|\'attached\'|\'detaching\'|\'detached\'
                                        },
                                        \'Description\': \'string\',
                                        \'Groups\': [
                                            {
                                                \'GroupName\': \'string\',
                                                \'GroupId\': \'string\'
                                            },
                                        ],
                                        \'Ipv6Addresses\': [
                                            {
                                                \'Ipv6Address\': \'string\'
                                            },
                                        ],
                                        \'MacAddress\': \'string\',
                                        \'NetworkInterfaceId\': \'string\',
                                        \'OwnerId\': \'string\',
                                        \'PrivateDnsName\': \'string\',
                                        \'PrivateIpAddress\': \'string\',
                                        \'PrivateIpAddresses\': [
                                            {
                                                \'Association\': {
                                                    \'IpOwnerId\': \'string\',
                                                    \'PublicDnsName\': \'string\',
                                                    \'PublicIp\': \'string\'
                                                },
                                                \'Primary\': True|False,
                                                \'PrivateDnsName\': \'string\',
                                                \'PrivateIpAddress\': \'string\'
                                            },
                                        ],
                                        \'SourceDestCheck\': True|False,
                                        \'Status\': \'available\'|\'associated\'|\'attaching\'|\'in-use\'|\'detaching\',
                                        \'SubnetId\': \'string\',
                                        \'VpcId\': \'string\'
                                    },
                                ],
                                \'RootDeviceName\': \'string\',
                                \'RootDeviceType\': \'ebs\'|\'instance-store\',
                                \'SecurityGroups\': [
                                    {
                                        \'GroupName\': \'string\',
                                        \'GroupId\': \'string\'
                                    },
                                ],
                                \'SourceDestCheck\': True|False,
                                \'SpotInstanceRequestId\': \'string\',
                                \'SriovNetSupport\': \'string\',
                                \'StateReason\': {
                                    \'Code\': \'string\',
                                    \'Message\': \'string\'
                                },
                                \'Tags\': [
                                    {
                                        \'Key\': \'string\',
                                        \'Value\': \'string\'
                                    },
                                ],
                                \'VirtualizationType\': \'hvm\'|\'paravirtual\',
                                \'CpuOptions\': {
                                    \'CoreCount\': 123,
                                    \'ThreadsPerCore\': 123
                                },
                                \'CapacityReservationId\': \'string\',
                                \'CapacityReservationSpecification\': {
                                    \'CapacityReservationPreference\': \'open\'|\'none\',
                                    \'CapacityReservationTarget\': {
                                        \'CapacityReservationId\': \'string\'
                                    }
                                }
                            },
                        ],
                        \'OwnerId\': \'string\',
                        \'RequesterId\': \'string\',
                        \'ReservationId\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DescribeInstances.
        
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
        
                      [EC2-VPC] The Amazon-provided DNS server resolves Amazon-provided private DNS hostnames if you\'ve enabled DNS resolution and DNS hostnames in your VPC. If you are not using the Amazon-provided DNS server in your VPC, your custom domain name servers must resolve the hostname as appropriate.
        
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
        
                      (IPv4 only) The public DNS name assigned to the instance. This name is not available until the instance enters the ``running`` state. For EC2-VPC, this name is only available if you\'ve enabled DNS hostnames for your VPC.
        
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
        
                      Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn\'t available with all instance types. Additional usage charges apply when using an EBS Optimized instance.
        
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
        
                        Describes the association between an instance and an Elastic GPU.
        
                        - **ElasticGpuId** *(string) --* 
        
                          The ID of the Elastic GPU.
        
                        - **ElasticGpuAssociationId** *(string) --* 
        
                          The ID of the association.
        
                        - **ElasticGpuAssociationState** *(string) --* 
        
                          The state of the association between the instance and the Elastic GPU.
        
                        - **ElasticGpuAssociationTime** *(string) --* 
        
                          The time the Elastic GPU was associated with the instance.
        
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
        
                      Specifies whether to enable an instance launched in a VPC to perform NAT. This controls whether source/destination checking is enabled on the instance. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the instance to perform NAT. For more information, see `NAT Instances <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
        
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
        
                        Describes the instance\'s Capacity Reservation preferences. Possible preferences include:
        
                        * ``open`` - The instance can run in any ``open`` Capacity Reservation that has matching attributes (instance type, platform, Availability Zone). 
                         
                        * ``none`` - The instance avoids running in a Capacity Reservation even if one is available. The instance runs in On-Demand capacity. 
                         
                      - **CapacityReservationTarget** *(dict) --* 
        
                        Information about the targeted Capacity Reservation.
        
                        - **CapacityReservationId** *(string) --* 
        
                          The ID of the Capacity Reservation.
        
                - **OwnerId** *(string) --* 
        
                  The ID of the AWS account that owns the reservation.
        
                - **RequesterId** *(string) --* 
        
                  The ID of the requester that launched the instances on your behalf (for example, AWS Management Console or Auto Scaling).
        
                - **ReservationId** *(string) --* 
        
                  The ID of the reservation.
        
        """
        pass


class DescribeNatGateways(Paginator):
    def paginate(self, Filters: List = None, NatGatewayIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNatGateways>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              NatGatewayIds=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'NatGateways\': [
                    {
                        \'CreateTime\': datetime(2015, 1, 1),
                        \'DeleteTime\': datetime(2015, 1, 1),
                        \'FailureCode\': \'string\',
                        \'FailureMessage\': \'string\',
                        \'NatGatewayAddresses\': [
                            {
                                \'AllocationId\': \'string\',
                                \'NetworkInterfaceId\': \'string\',
                                \'PrivateIp\': \'string\',
                                \'PublicIp\': \'string\'
                            },
                        ],
                        \'NatGatewayId\': \'string\',
                        \'ProvisionedBandwidth\': {
                            \'ProvisionTime\': datetime(2015, 1, 1),
                            \'Provisioned\': \'string\',
                            \'RequestTime\': datetime(2015, 1, 1),
                            \'Requested\': \'string\',
                            \'Status\': \'string\'
                        },
                        \'State\': \'pending\'|\'failed\'|\'available\'|\'deleting\'|\'deleted\',
                        \'SubnetId\': \'string\',
                        \'VpcId\': \'string\',
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
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
        
                  * For InsufficientFreeAddressesInSubnet: \"Subnet has insufficient free addresses to create this NAT gateway\" 
                   
                  * For Gateway.NotAttached: \"Network vpc-xxxxxxxx has no Internet gateway attached\" 
                   
                  * For InvalidAllocationID.NotFound: \"Elastic IP address eipalloc-xxxxxxxx could not be associated with this NAT gateway\" 
                   
                  * For Resource.AlreadyAssociated: \"Elastic IP address eipalloc-xxxxxxxx is already associated\" 
                   
                  * For InternalError: \"Network interface eni-xxxxxxxx, created and used internally by this NAT gateway is in an invalid state. Please try again.\" 
                   
                  * For InvalidSubnetID.NotFound: \"The specified subnet subnet-xxxxxxxx does not exist or could not be found.\" 
                   
                - **NatGatewayAddresses** *(list) --* 
        
                  Information about the IP addresses and network interface associated with the NAT gateway.
        
                  - *(dict) --* 
        
                    Describes the IP addresses and network interface associated with a NAT gateway.
        
                    - **AllocationId** *(string) --* 
        
                      The allocation ID of the Elastic IP address that\'s associated with the NAT gateway.
        
                    - **NetworkInterfaceId** *(string) --* 
        
                      The ID of the network interface associated with the NAT gateway.
        
                    - **PrivateIp** *(string) --* 
        
                      The private IP address associated with the Elastic IP address.
        
                    - **PublicIp** *(string) --* 
        
                      The Elastic IP address associated with the NAT gateway.
        
                - **NatGatewayId** *(string) --* 
        
                  The ID of the NAT gateway.
        
                - **ProvisionedBandwidth** *(dict) --* 
        
                  Reserved. If you need to sustain traffic greater than the `documented limits <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html>`__ , contact us through the `Support Center <https://console.aws.amazon.com/support/home?>`__ .
        
                  - **ProvisionTime** *(datetime) --* 
        
                    Reserved. If you need to sustain traffic greater than the `documented limits <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html>`__ , contact us through the `Support Center <https://console.aws.amazon.com/support/home?>`__ .
        
                  - **Provisioned** *(string) --* 
        
                    Reserved. If you need to sustain traffic greater than the `documented limits <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html>`__ , contact us through the `Support Center <https://console.aws.amazon.com/support/home?>`__ .
        
                  - **RequestTime** *(datetime) --* 
        
                    Reserved. If you need to sustain traffic greater than the `documented limits <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html>`__ , contact us through the `Support Center <https://console.aws.amazon.com/support/home?>`__ .
        
                  - **Requested** *(string) --* 
        
                    Reserved. If you need to sustain traffic greater than the `documented limits <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html>`__ , contact us through the `Support Center <https://console.aws.amazon.com/support/home?>`__ .
        
                  - **Status** *(string) --* 
        
                    Reserved. If you need to sustain traffic greater than the `documented limits <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html>`__ , contact us through the `Support Center <https://console.aws.amazon.com/support/home?>`__ .
        
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
        
        """
        pass


class DescribeNetworkInterfaces(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, NetworkInterfaceIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNetworkInterfaces>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
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
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'NetworkInterfaces\': [
                    {
                        \'Association\': {
                            \'AllocationId\': \'string\',
                            \'AssociationId\': \'string\',
                            \'IpOwnerId\': \'string\',
                            \'PublicDnsName\': \'string\',
                            \'PublicIp\': \'string\'
                        },
                        \'Attachment\': {
                            \'AttachTime\': datetime(2015, 1, 1),
                            \'AttachmentId\': \'string\',
                            \'DeleteOnTermination\': True|False,
                            \'DeviceIndex\': 123,
                            \'InstanceId\': \'string\',
                            \'InstanceOwnerId\': \'string\',
                            \'Status\': \'attaching\'|\'attached\'|\'detaching\'|\'detached\'
                        },
                        \'AvailabilityZone\': \'string\',
                        \'Description\': \'string\',
                        \'Groups\': [
                            {
                                \'GroupName\': \'string\',
                                \'GroupId\': \'string\'
                            },
                        ],
                        \'InterfaceType\': \'interface\'|\'natGateway\',
                        \'Ipv6Addresses\': [
                            {
                                \'Ipv6Address\': \'string\'
                            },
                        ],
                        \'MacAddress\': \'string\',
                        \'NetworkInterfaceId\': \'string\',
                        \'OwnerId\': \'string\',
                        \'PrivateDnsName\': \'string\',
                        \'PrivateIpAddress\': \'string\',
                        \'PrivateIpAddresses\': [
                            {
                                \'Association\': {
                                    \'AllocationId\': \'string\',
                                    \'AssociationId\': \'string\',
                                    \'IpOwnerId\': \'string\',
                                    \'PublicDnsName\': \'string\',
                                    \'PublicIp\': \'string\'
                                },
                                \'Primary\': True|False,
                                \'PrivateDnsName\': \'string\',
                                \'PrivateIpAddress\': \'string\'
                            },
                        ],
                        \'RequesterId\': \'string\',
                        \'RequesterManaged\': True|False,
                        \'SourceDestCheck\': True|False,
                        \'Status\': \'available\'|\'associated\'|\'attaching\'|\'in-use\'|\'detaching\',
                        \'SubnetId\': \'string\',
                        \'TagSet\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'VpcId\': \'string\'
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
        
        """
        pass


class DescribeReservedInstancesModifications(Paginator):
    def paginate(self, Filters: List = None, ReservedInstancesModificationIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeReservedInstancesModifications>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              ReservedInstancesModificationIds=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReservedInstancesModifications\': [
                    {
                        \'ClientToken\': \'string\',
                        \'CreateDate\': datetime(2015, 1, 1),
                        \'EffectiveDate\': datetime(2015, 1, 1),
                        \'ModificationResults\': [
                            {
                                \'ReservedInstancesId\': \'string\',
                                \'TargetConfiguration\': {
                                    \'AvailabilityZone\': \'string\',
                                    \'InstanceCount\': 123,
                                    \'InstanceType\': \'t1.micro\'|\'t2.nano\'|\'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'t2.xlarge\'|\'t2.2xlarge\'|\'t3.nano\'|\'t3.micro\'|\'t3.small\'|\'t3.medium\'|\'t3.large\'|\'t3.xlarge\'|\'t3.2xlarge\'|\'m1.small\'|\'m1.medium\'|\'m1.large\'|\'m1.xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\'|\'m4.16xlarge\'|\'m2.xlarge\'|\'m2.2xlarge\'|\'m2.4xlarge\'|\'cr1.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'r5.large\'|\'r5.xlarge\'|\'r5.2xlarge\'|\'r5.4xlarge\'|\'r5.8xlarge\'|\'r5.12xlarge\'|\'r5.16xlarge\'|\'r5.24xlarge\'|\'r5.metal\'|\'r5a.large\'|\'r5a.xlarge\'|\'r5a.2xlarge\'|\'r5a.4xlarge\'|\'r5a.12xlarge\'|\'r5a.24xlarge\'|\'r5d.large\'|\'r5d.xlarge\'|\'r5d.2xlarge\'|\'r5d.4xlarge\'|\'r5d.8xlarge\'|\'r5d.12xlarge\'|\'r5d.16xlarge\'|\'r5d.24xlarge\'|\'r5d.metal\'|\'x1.16xlarge\'|\'x1.32xlarge\'|\'x1e.xlarge\'|\'x1e.2xlarge\'|\'x1e.4xlarge\'|\'x1e.8xlarge\'|\'x1e.16xlarge\'|\'x1e.32xlarge\'|\'i2.xlarge\'|\'i2.2xlarge\'|\'i2.4xlarge\'|\'i2.8xlarge\'|\'i3.large\'|\'i3.xlarge\'|\'i3.2xlarge\'|\'i3.4xlarge\'|\'i3.8xlarge\'|\'i3.16xlarge\'|\'i3.metal\'|\'hi1.4xlarge\'|\'hs1.8xlarge\'|\'c1.medium\'|\'c1.xlarge\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'c5.large\'|\'c5.xlarge\'|\'c5.2xlarge\'|\'c5.4xlarge\'|\'c5.9xlarge\'|\'c5.18xlarge\'|\'c5d.large\'|\'c5d.xlarge\'|\'c5d.2xlarge\'|\'c5d.4xlarge\'|\'c5d.9xlarge\'|\'c5d.18xlarge\'|\'cc1.4xlarge\'|\'cc2.8xlarge\'|\'g2.2xlarge\'|\'g2.8xlarge\'|\'g3.4xlarge\'|\'g3.8xlarge\'|\'g3.16xlarge\'|\'g3s.xlarge\'|\'cg1.4xlarge\'|\'p2.xlarge\'|\'p2.8xlarge\'|\'p2.16xlarge\'|\'p3.2xlarge\'|\'p3.8xlarge\'|\'p3.16xlarge\'|\'d2.xlarge\'|\'d2.2xlarge\'|\'d2.4xlarge\'|\'d2.8xlarge\'|\'f1.2xlarge\'|\'f1.4xlarge\'|\'f1.16xlarge\'|\'m5.large\'|\'m5.xlarge\'|\'m5.2xlarge\'|\'m5.4xlarge\'|\'m5.12xlarge\'|\'m5.24xlarge\'|\'m5a.large\'|\'m5a.xlarge\'|\'m5a.2xlarge\'|\'m5a.4xlarge\'|\'m5a.12xlarge\'|\'m5a.24xlarge\'|\'m5d.large\'|\'m5d.xlarge\'|\'m5d.2xlarge\'|\'m5d.4xlarge\'|\'m5d.12xlarge\'|\'m5d.24xlarge\'|\'h1.2xlarge\'|\'h1.4xlarge\'|\'h1.8xlarge\'|\'h1.16xlarge\'|\'z1d.large\'|\'z1d.xlarge\'|\'z1d.2xlarge\'|\'z1d.3xlarge\'|\'z1d.6xlarge\'|\'z1d.12xlarge\'|\'u-6tb1.metal\'|\'u-9tb1.metal\'|\'u-12tb1.metal\',
                                    \'Platform\': \'string\',
                                    \'Scope\': \'Availability Zone\'|\'Region\'
                                }
                            },
                        ],
                        \'ReservedInstancesIds\': [
                            {
                                \'ReservedInstancesId\': \'string\'
                            },
                        ],
                        \'ReservedInstancesModificationId\': \'string\',
                        \'Status\': \'string\',
                        \'StatusMessage\': \'string\',
                        \'UpdateDate\': datetime(2015, 1, 1)
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
        
                  A unique, case-sensitive key supplied by the client to ensure that the request is idempotent. For more information, see `Ensuring Idempotency <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html>`__ .
        
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
        
        """
        pass


class DescribeReservedInstancesOfferings(Paginator):
    def paginate(self, AvailabilityZone: str = None, Filters: List = None, IncludeMarketplace: bool = None, InstanceType: str = None, MaxDuration: int = None, MaxInstanceCount: int = None, MinDuration: int = None, OfferingClass: str = None, ProductDescription: str = None, ReservedInstancesOfferingIds: List = None, DryRun: bool = None, InstanceTenancy: str = None, OfferingType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeReservedInstancesOfferings>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AvailabilityZone=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              IncludeMarketplace=True|False,
              InstanceType=\'t1.micro\'|\'t2.nano\'|\'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'t2.xlarge\'|\'t2.2xlarge\'|\'t3.nano\'|\'t3.micro\'|\'t3.small\'|\'t3.medium\'|\'t3.large\'|\'t3.xlarge\'|\'t3.2xlarge\'|\'m1.small\'|\'m1.medium\'|\'m1.large\'|\'m1.xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\'|\'m4.16xlarge\'|\'m2.xlarge\'|\'m2.2xlarge\'|\'m2.4xlarge\'|\'cr1.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'r5.large\'|\'r5.xlarge\'|\'r5.2xlarge\'|\'r5.4xlarge\'|\'r5.8xlarge\'|\'r5.12xlarge\'|\'r5.16xlarge\'|\'r5.24xlarge\'|\'r5.metal\'|\'r5a.large\'|\'r5a.xlarge\'|\'r5a.2xlarge\'|\'r5a.4xlarge\'|\'r5a.12xlarge\'|\'r5a.24xlarge\'|\'r5d.large\'|\'r5d.xlarge\'|\'r5d.2xlarge\'|\'r5d.4xlarge\'|\'r5d.8xlarge\'|\'r5d.12xlarge\'|\'r5d.16xlarge\'|\'r5d.24xlarge\'|\'r5d.metal\'|\'x1.16xlarge\'|\'x1.32xlarge\'|\'x1e.xlarge\'|\'x1e.2xlarge\'|\'x1e.4xlarge\'|\'x1e.8xlarge\'|\'x1e.16xlarge\'|\'x1e.32xlarge\'|\'i2.xlarge\'|\'i2.2xlarge\'|\'i2.4xlarge\'|\'i2.8xlarge\'|\'i3.large\'|\'i3.xlarge\'|\'i3.2xlarge\'|\'i3.4xlarge\'|\'i3.8xlarge\'|\'i3.16xlarge\'|\'i3.metal\'|\'hi1.4xlarge\'|\'hs1.8xlarge\'|\'c1.medium\'|\'c1.xlarge\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'c5.large\'|\'c5.xlarge\'|\'c5.2xlarge\'|\'c5.4xlarge\'|\'c5.9xlarge\'|\'c5.18xlarge\'|\'c5d.large\'|\'c5d.xlarge\'|\'c5d.2xlarge\'|\'c5d.4xlarge\'|\'c5d.9xlarge\'|\'c5d.18xlarge\'|\'cc1.4xlarge\'|\'cc2.8xlarge\'|\'g2.2xlarge\'|\'g2.8xlarge\'|\'g3.4xlarge\'|\'g3.8xlarge\'|\'g3.16xlarge\'|\'g3s.xlarge\'|\'cg1.4xlarge\'|\'p2.xlarge\'|\'p2.8xlarge\'|\'p2.16xlarge\'|\'p3.2xlarge\'|\'p3.8xlarge\'|\'p3.16xlarge\'|\'d2.xlarge\'|\'d2.2xlarge\'|\'d2.4xlarge\'|\'d2.8xlarge\'|\'f1.2xlarge\'|\'f1.4xlarge\'|\'f1.16xlarge\'|\'m5.large\'|\'m5.xlarge\'|\'m5.2xlarge\'|\'m5.4xlarge\'|\'m5.12xlarge\'|\'m5.24xlarge\'|\'m5a.large\'|\'m5a.xlarge\'|\'m5a.2xlarge\'|\'m5a.4xlarge\'|\'m5a.12xlarge\'|\'m5a.24xlarge\'|\'m5d.large\'|\'m5d.xlarge\'|\'m5d.2xlarge\'|\'m5d.4xlarge\'|\'m5d.12xlarge\'|\'m5d.24xlarge\'|\'h1.2xlarge\'|\'h1.4xlarge\'|\'h1.8xlarge\'|\'h1.16xlarge\'|\'z1d.large\'|\'z1d.xlarge\'|\'z1d.2xlarge\'|\'z1d.3xlarge\'|\'z1d.6xlarge\'|\'z1d.12xlarge\'|\'u-6tb1.metal\'|\'u-9tb1.metal\'|\'u-12tb1.metal\',
              MaxDuration=123,
              MaxInstanceCount=123,
              MinDuration=123,
              OfferingClass=\'standard\'|\'convertible\',
              ProductDescription=\'Linux/UNIX\'|\'Linux/UNIX (Amazon VPC)\'|\'Windows\'|\'Windows (Amazon VPC)\',
              ReservedInstancesOfferingIds=[
                  \'string\',
              ],
              DryRun=True|False,
              InstanceTenancy=\'default\'|\'dedicated\'|\'host\',
              OfferingType=\'Heavy Utilization\'|\'Medium Utilization\'|\'Light Utilization\'|\'No Upfront\'|\'Partial Upfront\'|\'All Upfront\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
        
          The instance type that the reservation will cover (for example, ``m1.small`` ). For more information, see `Instance Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'ReservedInstancesOfferings\': [
                    {
                        \'AvailabilityZone\': \'string\',
                        \'Duration\': 123,
                        \'FixedPrice\': ...,
                        \'InstanceType\': \'t1.micro\'|\'t2.nano\'|\'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'t2.xlarge\'|\'t2.2xlarge\'|\'t3.nano\'|\'t3.micro\'|\'t3.small\'|\'t3.medium\'|\'t3.large\'|\'t3.xlarge\'|\'t3.2xlarge\'|\'m1.small\'|\'m1.medium\'|\'m1.large\'|\'m1.xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\'|\'m4.16xlarge\'|\'m2.xlarge\'|\'m2.2xlarge\'|\'m2.4xlarge\'|\'cr1.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'r5.large\'|\'r5.xlarge\'|\'r5.2xlarge\'|\'r5.4xlarge\'|\'r5.8xlarge\'|\'r5.12xlarge\'|\'r5.16xlarge\'|\'r5.24xlarge\'|\'r5.metal\'|\'r5a.large\'|\'r5a.xlarge\'|\'r5a.2xlarge\'|\'r5a.4xlarge\'|\'r5a.12xlarge\'|\'r5a.24xlarge\'|\'r5d.large\'|\'r5d.xlarge\'|\'r5d.2xlarge\'|\'r5d.4xlarge\'|\'r5d.8xlarge\'|\'r5d.12xlarge\'|\'r5d.16xlarge\'|\'r5d.24xlarge\'|\'r5d.metal\'|\'x1.16xlarge\'|\'x1.32xlarge\'|\'x1e.xlarge\'|\'x1e.2xlarge\'|\'x1e.4xlarge\'|\'x1e.8xlarge\'|\'x1e.16xlarge\'|\'x1e.32xlarge\'|\'i2.xlarge\'|\'i2.2xlarge\'|\'i2.4xlarge\'|\'i2.8xlarge\'|\'i3.large\'|\'i3.xlarge\'|\'i3.2xlarge\'|\'i3.4xlarge\'|\'i3.8xlarge\'|\'i3.16xlarge\'|\'i3.metal\'|\'hi1.4xlarge\'|\'hs1.8xlarge\'|\'c1.medium\'|\'c1.xlarge\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'c5.large\'|\'c5.xlarge\'|\'c5.2xlarge\'|\'c5.4xlarge\'|\'c5.9xlarge\'|\'c5.18xlarge\'|\'c5d.large\'|\'c5d.xlarge\'|\'c5d.2xlarge\'|\'c5d.4xlarge\'|\'c5d.9xlarge\'|\'c5d.18xlarge\'|\'cc1.4xlarge\'|\'cc2.8xlarge\'|\'g2.2xlarge\'|\'g2.8xlarge\'|\'g3.4xlarge\'|\'g3.8xlarge\'|\'g3.16xlarge\'|\'g3s.xlarge\'|\'cg1.4xlarge\'|\'p2.xlarge\'|\'p2.8xlarge\'|\'p2.16xlarge\'|\'p3.2xlarge\'|\'p3.8xlarge\'|\'p3.16xlarge\'|\'d2.xlarge\'|\'d2.2xlarge\'|\'d2.4xlarge\'|\'d2.8xlarge\'|\'f1.2xlarge\'|\'f1.4xlarge\'|\'f1.16xlarge\'|\'m5.large\'|\'m5.xlarge\'|\'m5.2xlarge\'|\'m5.4xlarge\'|\'m5.12xlarge\'|\'m5.24xlarge\'|\'m5a.large\'|\'m5a.xlarge\'|\'m5a.2xlarge\'|\'m5a.4xlarge\'|\'m5a.12xlarge\'|\'m5a.24xlarge\'|\'m5d.large\'|\'m5d.xlarge\'|\'m5d.2xlarge\'|\'m5d.4xlarge\'|\'m5d.12xlarge\'|\'m5d.24xlarge\'|\'h1.2xlarge\'|\'h1.4xlarge\'|\'h1.8xlarge\'|\'h1.16xlarge\'|\'z1d.large\'|\'z1d.xlarge\'|\'z1d.2xlarge\'|\'z1d.3xlarge\'|\'z1d.6xlarge\'|\'z1d.12xlarge\'|\'u-6tb1.metal\'|\'u-9tb1.metal\'|\'u-12tb1.metal\',
                        \'ProductDescription\': \'Linux/UNIX\'|\'Linux/UNIX (Amazon VPC)\'|\'Windows\'|\'Windows (Amazon VPC)\',
                        \'ReservedInstancesOfferingId\': \'string\',
                        \'UsagePrice\': ...,
                        \'CurrencyCode\': \'USD\',
                        \'InstanceTenancy\': \'default\'|\'dedicated\'|\'host\',
                        \'Marketplace\': True|False,
                        \'OfferingClass\': \'standard\'|\'convertible\',
                        \'OfferingType\': \'Heavy Utilization\'|\'Medium Utilization\'|\'Light Utilization\'|\'No Upfront\'|\'Partial Upfront\'|\'All Upfront\',
                        \'PricingDetails\': [
                            {
                                \'Count\': 123,
                                \'Price\': 123.0
                            },
                        ],
                        \'RecurringCharges\': [
                            {
                                \'Amount\': 123.0,
                                \'Frequency\': \'Hourly\'
                            },
                        ],
                        \'Scope\': \'Availability Zone\'|\'Region\'
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
        
                  The currency of the Reserved Instance offering you are purchasing. It\'s specified using ISO 4217 standard currency codes. At this time, the only supported currency is ``USD`` .
        
                - **InstanceTenancy** *(string) --* 
        
                  The tenancy of the instance.
        
                - **Marketplace** *(boolean) --* 
        
                  Indicates whether the offering is available through the Reserved Instance Marketplace (resale) or AWS. If it\'s a Reserved Instance Marketplace offering, this is ``true`` .
        
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
        
        """
        pass


class DescribeRouteTables(Paginator):
    def paginate(self, Filters: List = None, DryRun: bool = None, RouteTableIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeRouteTables>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
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
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'RouteTables\': [
                    {
                        \'Associations\': [
                            {
                                \'Main\': True|False,
                                \'RouteTableAssociationId\': \'string\',
                                \'RouteTableId\': \'string\',
                                \'SubnetId\': \'string\'
                            },
                        ],
                        \'PropagatingVgws\': [
                            {
                                \'GatewayId\': \'string\'
                            },
                        ],
                        \'RouteTableId\': \'string\',
                        \'Routes\': [
                            {
                                \'DestinationCidrBlock\': \'string\',
                                \'DestinationIpv6CidrBlock\': \'string\',
                                \'DestinationPrefixListId\': \'string\',
                                \'EgressOnlyInternetGatewayId\': \'string\',
                                \'GatewayId\': \'string\',
                                \'InstanceId\': \'string\',
                                \'InstanceOwnerId\': \'string\',
                                \'NatGatewayId\': \'string\',
                                \'NetworkInterfaceId\': \'string\',
                                \'Origin\': \'CreateRouteTable\'|\'CreateRoute\'|\'EnableVgwRoutePropagation\',
                                \'State\': \'active\'|\'blackhole\',
                                \'VpcPeeringConnectionId\': \'string\'
                            },
                        ],
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'VpcId\': \'string\'
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
        
                    - **NetworkInterfaceId** *(string) --* 
        
                      The ID of the network interface.
        
                    - **Origin** *(string) --* 
        
                      Describes how the route was created.
        
                      * ``CreateRouteTable`` - The route was automatically created when the route table was created. 
                       
                      * ``CreateRoute`` - The route was manually added to the route table. 
                       
                      * ``EnableVgwRoutePropagation`` - The route was propagated by route propagation. 
                       
                    - **State** *(string) --* 
        
                      The state of the route. The ``blackhole`` state indicates that the route\'s target isn\'t available (for example, the specified gateway isn\'t attached to the VPC, or the specified NAT instance has been terminated).
        
                    - **VpcPeeringConnectionId** *(string) --* 
        
                      The ID of the VPC peering connection.
        
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
        
        """
        pass


class DescribeSecurityGroups(Paginator):
    def paginate(self, Filters: List = None, GroupIds: List = None, GroupNames: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSecurityGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
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
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'SecurityGroups\': [
                    {
                        \'Description\': \'string\',
                        \'GroupName\': \'string\',
                        \'IpPermissions\': [
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
                        \'OwnerId\': \'string\',
                        \'GroupId\': \'string\',
                        \'IpPermissionsEgress\': [
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
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'VpcId\': \'string\'
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
        
        """
        pass


class DescribeSnapshots(Paginator):
    def paginate(self, Filters: List = None, OwnerIds: List = None, RestorableByUserIds: List = None, SnapshotIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSnapshots>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              OwnerIds=[
                  \'string\',
              ],
              RestorableByUserIds=[
                  \'string\',
              ],
              SnapshotIds=[
                  \'string\',
              ],
              DryRun=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Snapshots\': [
                    {
                        \'DataEncryptionKeyId\': \'string\',
                        \'Description\': \'string\',
                        \'Encrypted\': True|False,
                        \'KmsKeyId\': \'string\',
                        \'OwnerId\': \'string\',
                        \'Progress\': \'string\',
                        \'SnapshotId\': \'string\',
                        \'StartTime\': datetime(2015, 1, 1),
                        \'State\': \'pending\'|\'completed\'|\'error\',
                        \'StateMessage\': \'string\',
                        \'VolumeId\': \'string\',
                        \'VolumeSize\': 123,
                        \'OwnerAlias\': \'string\',
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
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
        
        """
        pass


class DescribeSpotFleetInstances(Paginator):
    def paginate(self, SpotFleetRequestId: str, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSpotFleetInstances>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DryRun=True|False,
              SpotFleetRequestId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'ActiveInstances\': [
                    {
                        \'InstanceId\': \'string\',
                        \'InstanceType\': \'string\',
                        \'SpotInstanceRequestId\': \'string\',
                        \'InstanceHealth\': \'healthy\'|\'unhealthy\'
                    },
                ],
                \'SpotFleetRequestId\': \'string\'
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
        
        """
        pass


class DescribeSpotFleetRequests(Paginator):
    def paginate(self, DryRun: bool = None, SpotFleetRequestIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSpotFleetRequests>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DryRun=True|False,
              SpotFleetRequestIds=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'SpotFleetRequestConfigs\': [
                    {
                        \'ActivityStatus\': \'error\'|\'pending_fulfillment\'|\'pending_termination\'|\'fulfilled\',
                        \'CreateTime\': datetime(2015, 1, 1),
                        \'SpotFleetRequestConfig\': {
                            \'AllocationStrategy\': \'lowestPrice\'|\'diversified\',
                            \'OnDemandAllocationStrategy\': \'lowestPrice\'|\'prioritized\',
                            \'ClientToken\': \'string\',
                            \'ExcessCapacityTerminationPolicy\': \'noTermination\'|\'default\',
                            \'FulfilledCapacity\': 123.0,
                            \'OnDemandFulfilledCapacity\': 123.0,
                            \'IamFleetRole\': \'string\',
                            \'LaunchSpecifications\': [
                                {
                                    \'SecurityGroups\': [
                                        {
                                            \'GroupName\': \'string\',
                                            \'GroupId\': \'string\'
                                        },
                                    ],
                                    \'AddressingType\': \'string\',
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
                                    \'EbsOptimized\': True|False,
                                    \'IamInstanceProfile\': {
                                        \'Arn\': \'string\',
                                        \'Name\': \'string\'
                                    },
                                    \'ImageId\': \'string\',
                                    \'InstanceType\': \'t1.micro\'|\'t2.nano\'|\'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'t2.xlarge\'|\'t2.2xlarge\'|\'t3.nano\'|\'t3.micro\'|\'t3.small\'|\'t3.medium\'|\'t3.large\'|\'t3.xlarge\'|\'t3.2xlarge\'|\'m1.small\'|\'m1.medium\'|\'m1.large\'|\'m1.xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\'|\'m4.16xlarge\'|\'m2.xlarge\'|\'m2.2xlarge\'|\'m2.4xlarge\'|\'cr1.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'r5.large\'|\'r5.xlarge\'|\'r5.2xlarge\'|\'r5.4xlarge\'|\'r5.8xlarge\'|\'r5.12xlarge\'|\'r5.16xlarge\'|\'r5.24xlarge\'|\'r5.metal\'|\'r5a.large\'|\'r5a.xlarge\'|\'r5a.2xlarge\'|\'r5a.4xlarge\'|\'r5a.12xlarge\'|\'r5a.24xlarge\'|\'r5d.large\'|\'r5d.xlarge\'|\'r5d.2xlarge\'|\'r5d.4xlarge\'|\'r5d.8xlarge\'|\'r5d.12xlarge\'|\'r5d.16xlarge\'|\'r5d.24xlarge\'|\'r5d.metal\'|\'x1.16xlarge\'|\'x1.32xlarge\'|\'x1e.xlarge\'|\'x1e.2xlarge\'|\'x1e.4xlarge\'|\'x1e.8xlarge\'|\'x1e.16xlarge\'|\'x1e.32xlarge\'|\'i2.xlarge\'|\'i2.2xlarge\'|\'i2.4xlarge\'|\'i2.8xlarge\'|\'i3.large\'|\'i3.xlarge\'|\'i3.2xlarge\'|\'i3.4xlarge\'|\'i3.8xlarge\'|\'i3.16xlarge\'|\'i3.metal\'|\'hi1.4xlarge\'|\'hs1.8xlarge\'|\'c1.medium\'|\'c1.xlarge\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'c5.large\'|\'c5.xlarge\'|\'c5.2xlarge\'|\'c5.4xlarge\'|\'c5.9xlarge\'|\'c5.18xlarge\'|\'c5d.large\'|\'c5d.xlarge\'|\'c5d.2xlarge\'|\'c5d.4xlarge\'|\'c5d.9xlarge\'|\'c5d.18xlarge\'|\'cc1.4xlarge\'|\'cc2.8xlarge\'|\'g2.2xlarge\'|\'g2.8xlarge\'|\'g3.4xlarge\'|\'g3.8xlarge\'|\'g3.16xlarge\'|\'g3s.xlarge\'|\'cg1.4xlarge\'|\'p2.xlarge\'|\'p2.8xlarge\'|\'p2.16xlarge\'|\'p3.2xlarge\'|\'p3.8xlarge\'|\'p3.16xlarge\'|\'d2.xlarge\'|\'d2.2xlarge\'|\'d2.4xlarge\'|\'d2.8xlarge\'|\'f1.2xlarge\'|\'f1.4xlarge\'|\'f1.16xlarge\'|\'m5.large\'|\'m5.xlarge\'|\'m5.2xlarge\'|\'m5.4xlarge\'|\'m5.12xlarge\'|\'m5.24xlarge\'|\'m5a.large\'|\'m5a.xlarge\'|\'m5a.2xlarge\'|\'m5a.4xlarge\'|\'m5a.12xlarge\'|\'m5a.24xlarge\'|\'m5d.large\'|\'m5d.xlarge\'|\'m5d.2xlarge\'|\'m5d.4xlarge\'|\'m5d.12xlarge\'|\'m5d.24xlarge\'|\'h1.2xlarge\'|\'h1.4xlarge\'|\'h1.8xlarge\'|\'h1.16xlarge\'|\'z1d.large\'|\'z1d.xlarge\'|\'z1d.2xlarge\'|\'z1d.3xlarge\'|\'z1d.6xlarge\'|\'z1d.12xlarge\'|\'u-6tb1.metal\'|\'u-9tb1.metal\'|\'u-12tb1.metal\',
                                    \'KernelId\': \'string\',
                                    \'KeyName\': \'string\',
                                    \'Monitoring\': {
                                        \'Enabled\': True|False
                                    },
                                    \'NetworkInterfaces\': [
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
                                    \'Placement\': {
                                        \'AvailabilityZone\': \'string\',
                                        \'GroupName\': \'string\',
                                        \'Tenancy\': \'default\'|\'dedicated\'|\'host\'
                                    },
                                    \'RamdiskId\': \'string\',
                                    \'SpotPrice\': \'string\',
                                    \'SubnetId\': \'string\',
                                    \'UserData\': \'string\',
                                    \'WeightedCapacity\': 123.0,
                                    \'TagSpecifications\': [
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
                                },
                            ],
                            \'LaunchTemplateConfigs\': [
                                {
                                    \'LaunchTemplateSpecification\': {
                                        \'LaunchTemplateId\': \'string\',
                                        \'LaunchTemplateName\': \'string\',
                                        \'Version\': \'string\'
                                    },
                                    \'Overrides\': [
                                        {
                                            \'InstanceType\': \'t1.micro\'|\'t2.nano\'|\'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'t2.xlarge\'|\'t2.2xlarge\'|\'t3.nano\'|\'t3.micro\'|\'t3.small\'|\'t3.medium\'|\'t3.large\'|\'t3.xlarge\'|\'t3.2xlarge\'|\'m1.small\'|\'m1.medium\'|\'m1.large\'|\'m1.xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\'|\'m4.16xlarge\'|\'m2.xlarge\'|\'m2.2xlarge\'|\'m2.4xlarge\'|\'cr1.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'r5.large\'|\'r5.xlarge\'|\'r5.2xlarge\'|\'r5.4xlarge\'|\'r5.8xlarge\'|\'r5.12xlarge\'|\'r5.16xlarge\'|\'r5.24xlarge\'|\'r5.metal\'|\'r5a.large\'|\'r5a.xlarge\'|\'r5a.2xlarge\'|\'r5a.4xlarge\'|\'r5a.12xlarge\'|\'r5a.24xlarge\'|\'r5d.large\'|\'r5d.xlarge\'|\'r5d.2xlarge\'|\'r5d.4xlarge\'|\'r5d.8xlarge\'|\'r5d.12xlarge\'|\'r5d.16xlarge\'|\'r5d.24xlarge\'|\'r5d.metal\'|\'x1.16xlarge\'|\'x1.32xlarge\'|\'x1e.xlarge\'|\'x1e.2xlarge\'|\'x1e.4xlarge\'|\'x1e.8xlarge\'|\'x1e.16xlarge\'|\'x1e.32xlarge\'|\'i2.xlarge\'|\'i2.2xlarge\'|\'i2.4xlarge\'|\'i2.8xlarge\'|\'i3.large\'|\'i3.xlarge\'|\'i3.2xlarge\'|\'i3.4xlarge\'|\'i3.8xlarge\'|\'i3.16xlarge\'|\'i3.metal\'|\'hi1.4xlarge\'|\'hs1.8xlarge\'|\'c1.medium\'|\'c1.xlarge\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'c5.large\'|\'c5.xlarge\'|\'c5.2xlarge\'|\'c5.4xlarge\'|\'c5.9xlarge\'|\'c5.18xlarge\'|\'c5d.large\'|\'c5d.xlarge\'|\'c5d.2xlarge\'|\'c5d.4xlarge\'|\'c5d.9xlarge\'|\'c5d.18xlarge\'|\'cc1.4xlarge\'|\'cc2.8xlarge\'|\'g2.2xlarge\'|\'g2.8xlarge\'|\'g3.4xlarge\'|\'g3.8xlarge\'|\'g3.16xlarge\'|\'g3s.xlarge\'|\'cg1.4xlarge\'|\'p2.xlarge\'|\'p2.8xlarge\'|\'p2.16xlarge\'|\'p3.2xlarge\'|\'p3.8xlarge\'|\'p3.16xlarge\'|\'d2.xlarge\'|\'d2.2xlarge\'|\'d2.4xlarge\'|\'d2.8xlarge\'|\'f1.2xlarge\'|\'f1.4xlarge\'|\'f1.16xlarge\'|\'m5.large\'|\'m5.xlarge\'|\'m5.2xlarge\'|\'m5.4xlarge\'|\'m5.12xlarge\'|\'m5.24xlarge\'|\'m5a.large\'|\'m5a.xlarge\'|\'m5a.2xlarge\'|\'m5a.4xlarge\'|\'m5a.12xlarge\'|\'m5a.24xlarge\'|\'m5d.large\'|\'m5d.xlarge\'|\'m5d.2xlarge\'|\'m5d.4xlarge\'|\'m5d.12xlarge\'|\'m5d.24xlarge\'|\'h1.2xlarge\'|\'h1.4xlarge\'|\'h1.8xlarge\'|\'h1.16xlarge\'|\'z1d.large\'|\'z1d.xlarge\'|\'z1d.2xlarge\'|\'z1d.3xlarge\'|\'z1d.6xlarge\'|\'z1d.12xlarge\'|\'u-6tb1.metal\'|\'u-9tb1.metal\'|\'u-12tb1.metal\',
                                            \'SpotPrice\': \'string\',
                                            \'SubnetId\': \'string\',
                                            \'AvailabilityZone\': \'string\',
                                            \'WeightedCapacity\': 123.0,
                                            \'Priority\': 123.0
                                        },
                                    ]
                                },
                            ],
                            \'SpotPrice\': \'string\',
                            \'TargetCapacity\': 123,
                            \'OnDemandTargetCapacity\': 123,
                            \'TerminateInstancesWithExpiration\': True|False,
                            \'Type\': \'request\'|\'maintain\',
                            \'ValidFrom\': datetime(2015, 1, 1),
                            \'ValidUntil\': datetime(2015, 1, 1),
                            \'ReplaceUnhealthyInstances\': True|False,
                            \'InstanceInterruptionBehavior\': \'hibernate\'|\'stop\'|\'terminate\',
                            \'LoadBalancersConfig\': {
                                \'ClassicLoadBalancersConfig\': {
                                    \'ClassicLoadBalancers\': [
                                        {
                                            \'Name\': \'string\'
                                        },
                                    ]
                                },
                                \'TargetGroupsConfig\': {
                                    \'TargetGroups\': [
                                        {
                                            \'Arn\': \'string\'
                                        },
                                    ]
                                }
                            },
                            \'InstancePoolsToUseCount\': 123
                        },
                        \'SpotFleetRequestId\': \'string\',
                        \'SpotFleetRequestState\': \'submitted\'|\'active\'|\'cancelled\'|\'failed\'|\'cancelled_running\'|\'cancelled_terminating\'|\'modifying\'
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
        
                    A unique, case-sensitive identifier that you provide to ensure the idempotency of your listings. This helps to avoid duplicate listings. For more information, see `Ensuring Idempotency <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html>`__ .
        
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
        
                      - **EbsOptimized** *(boolean) --* 
        
                        Indicates whether the instances are optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn\'t available with all instance types. Additional usage charges apply when using an EBS Optimized instance.
        
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
        
                      - **Placement** *(dict) --* 
        
                        The placement information.
        
                        - **AvailabilityZone** *(string) --* 
        
                          The Availability Zone.
        
                          [Spot Fleet only] To specify multiple Availability Zones, separate them using commas; for example, \"us-west-2a, us-west-2b\".
        
                        - **GroupName** *(string) --* 
        
                          The name of the placement group.
        
                        - **Tenancy** *(string) --* 
        
                          The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of ``dedicated`` runs on single-tenant hardware. The ``host`` tenancy is not supported for Spot Instances.
        
                      - **RamdiskId** *(string) --* 
        
                        The ID of the RAM disk.
        
                      - **SpotPrice** *(string) --* 
        
                        The maximum price per unit hour that you are willing to pay for a Spot Instance. If this value is not specified, the default is the Spot price specified for the fleet. To determine the Spot price per unit hour, divide the Spot price by the value of ``WeightedCapacity`` .
        
                      - **SubnetId** *(string) --* 
        
                        The ID of the subnet in which to launch the instances. To specify multiple subnets, separate them using commas; for example, \"subnet-a61dafcf, subnet-65ea5f08\".
        
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
        
                    The type of request. Indicates whether the Spot Fleet only requests the target capacity or also attempts to maintain it. When this value is ``request`` , the Spot Fleet only places the required requests. It does not attempt to replenish Spot Instances if capacity is diminished, nor does it submit requests in alternative Spot pools if capacity is not available. To maintain a certain target capacity, the Spot Fleet places the required requests to meet capacity and automatically replenishes any interrupted instances. Default: ``maintain`` .
        
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
        
        """
        pass


class DescribeSpotPriceHistory(Paginator):
    def paginate(self, Filters: List = None, AvailabilityZone: str = None, DryRun: bool = None, EndTime: datetime = None, InstanceTypes: List = None, ProductDescriptions: List = None, StartTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSpotPriceHistory>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              AvailabilityZone=\'string\',
              DryRun=True|False,
              EndTime=datetime(2015, 1, 1),
              InstanceTypes=[
                  \'t1.micro\'|\'t2.nano\'|\'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'t2.xlarge\'|\'t2.2xlarge\'|\'t3.nano\'|\'t3.micro\'|\'t3.small\'|\'t3.medium\'|\'t3.large\'|\'t3.xlarge\'|\'t3.2xlarge\'|\'m1.small\'|\'m1.medium\'|\'m1.large\'|\'m1.xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\'|\'m4.16xlarge\'|\'m2.xlarge\'|\'m2.2xlarge\'|\'m2.4xlarge\'|\'cr1.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'r5.large\'|\'r5.xlarge\'|\'r5.2xlarge\'|\'r5.4xlarge\'|\'r5.8xlarge\'|\'r5.12xlarge\'|\'r5.16xlarge\'|\'r5.24xlarge\'|\'r5.metal\'|\'r5a.large\'|\'r5a.xlarge\'|\'r5a.2xlarge\'|\'r5a.4xlarge\'|\'r5a.12xlarge\'|\'r5a.24xlarge\'|\'r5d.large\'|\'r5d.xlarge\'|\'r5d.2xlarge\'|\'r5d.4xlarge\'|\'r5d.8xlarge\'|\'r5d.12xlarge\'|\'r5d.16xlarge\'|\'r5d.24xlarge\'|\'r5d.metal\'|\'x1.16xlarge\'|\'x1.32xlarge\'|\'x1e.xlarge\'|\'x1e.2xlarge\'|\'x1e.4xlarge\'|\'x1e.8xlarge\'|\'x1e.16xlarge\'|\'x1e.32xlarge\'|\'i2.xlarge\'|\'i2.2xlarge\'|\'i2.4xlarge\'|\'i2.8xlarge\'|\'i3.large\'|\'i3.xlarge\'|\'i3.2xlarge\'|\'i3.4xlarge\'|\'i3.8xlarge\'|\'i3.16xlarge\'|\'i3.metal\'|\'hi1.4xlarge\'|\'hs1.8xlarge\'|\'c1.medium\'|\'c1.xlarge\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'c5.large\'|\'c5.xlarge\'|\'c5.2xlarge\'|\'c5.4xlarge\'|\'c5.9xlarge\'|\'c5.18xlarge\'|\'c5d.large\'|\'c5d.xlarge\'|\'c5d.2xlarge\'|\'c5d.4xlarge\'|\'c5d.9xlarge\'|\'c5d.18xlarge\'|\'cc1.4xlarge\'|\'cc2.8xlarge\'|\'g2.2xlarge\'|\'g2.8xlarge\'|\'g3.4xlarge\'|\'g3.8xlarge\'|\'g3.16xlarge\'|\'g3s.xlarge\'|\'cg1.4xlarge\'|\'p2.xlarge\'|\'p2.8xlarge\'|\'p2.16xlarge\'|\'p3.2xlarge\'|\'p3.8xlarge\'|\'p3.16xlarge\'|\'d2.xlarge\'|\'d2.2xlarge\'|\'d2.4xlarge\'|\'d2.8xlarge\'|\'f1.2xlarge\'|\'f1.4xlarge\'|\'f1.16xlarge\'|\'m5.large\'|\'m5.xlarge\'|\'m5.2xlarge\'|\'m5.4xlarge\'|\'m5.12xlarge\'|\'m5.24xlarge\'|\'m5a.large\'|\'m5a.xlarge\'|\'m5a.2xlarge\'|\'m5a.4xlarge\'|\'m5a.12xlarge\'|\'m5a.24xlarge\'|\'m5d.large\'|\'m5d.xlarge\'|\'m5d.2xlarge\'|\'m5d.4xlarge\'|\'m5d.12xlarge\'|\'m5d.24xlarge\'|\'h1.2xlarge\'|\'h1.4xlarge\'|\'h1.8xlarge\'|\'h1.16xlarge\'|\'z1d.large\'|\'z1d.xlarge\'|\'z1d.2xlarge\'|\'z1d.3xlarge\'|\'z1d.6xlarge\'|\'z1d.12xlarge\'|\'u-6tb1.metal\'|\'u-9tb1.metal\'|\'u-12tb1.metal\',
              ],
              ProductDescriptions=[
                  \'string\',
              ],
              StartTime=datetime(2015, 1, 1),
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'SpotPriceHistory\': [
                    {
                        \'AvailabilityZone\': \'string\',
                        \'InstanceType\': \'t1.micro\'|\'t2.nano\'|\'t2.micro\'|\'t2.small\'|\'t2.medium\'|\'t2.large\'|\'t2.xlarge\'|\'t2.2xlarge\'|\'t3.nano\'|\'t3.micro\'|\'t3.small\'|\'t3.medium\'|\'t3.large\'|\'t3.xlarge\'|\'t3.2xlarge\'|\'m1.small\'|\'m1.medium\'|\'m1.large\'|\'m1.xlarge\'|\'m3.medium\'|\'m3.large\'|\'m3.xlarge\'|\'m3.2xlarge\'|\'m4.large\'|\'m4.xlarge\'|\'m4.2xlarge\'|\'m4.4xlarge\'|\'m4.10xlarge\'|\'m4.16xlarge\'|\'m2.xlarge\'|\'m2.2xlarge\'|\'m2.4xlarge\'|\'cr1.8xlarge\'|\'r3.large\'|\'r3.xlarge\'|\'r3.2xlarge\'|\'r3.4xlarge\'|\'r3.8xlarge\'|\'r4.large\'|\'r4.xlarge\'|\'r4.2xlarge\'|\'r4.4xlarge\'|\'r4.8xlarge\'|\'r4.16xlarge\'|\'r5.large\'|\'r5.xlarge\'|\'r5.2xlarge\'|\'r5.4xlarge\'|\'r5.8xlarge\'|\'r5.12xlarge\'|\'r5.16xlarge\'|\'r5.24xlarge\'|\'r5.metal\'|\'r5a.large\'|\'r5a.xlarge\'|\'r5a.2xlarge\'|\'r5a.4xlarge\'|\'r5a.12xlarge\'|\'r5a.24xlarge\'|\'r5d.large\'|\'r5d.xlarge\'|\'r5d.2xlarge\'|\'r5d.4xlarge\'|\'r5d.8xlarge\'|\'r5d.12xlarge\'|\'r5d.16xlarge\'|\'r5d.24xlarge\'|\'r5d.metal\'|\'x1.16xlarge\'|\'x1.32xlarge\'|\'x1e.xlarge\'|\'x1e.2xlarge\'|\'x1e.4xlarge\'|\'x1e.8xlarge\'|\'x1e.16xlarge\'|\'x1e.32xlarge\'|\'i2.xlarge\'|\'i2.2xlarge\'|\'i2.4xlarge\'|\'i2.8xlarge\'|\'i3.large\'|\'i3.xlarge\'|\'i3.2xlarge\'|\'i3.4xlarge\'|\'i3.8xlarge\'|\'i3.16xlarge\'|\'i3.metal\'|\'hi1.4xlarge\'|\'hs1.8xlarge\'|\'c1.medium\'|\'c1.xlarge\'|\'c3.large\'|\'c3.xlarge\'|\'c3.2xlarge\'|\'c3.4xlarge\'|\'c3.8xlarge\'|\'c4.large\'|\'c4.xlarge\'|\'c4.2xlarge\'|\'c4.4xlarge\'|\'c4.8xlarge\'|\'c5.large\'|\'c5.xlarge\'|\'c5.2xlarge\'|\'c5.4xlarge\'|\'c5.9xlarge\'|\'c5.18xlarge\'|\'c5d.large\'|\'c5d.xlarge\'|\'c5d.2xlarge\'|\'c5d.4xlarge\'|\'c5d.9xlarge\'|\'c5d.18xlarge\'|\'cc1.4xlarge\'|\'cc2.8xlarge\'|\'g2.2xlarge\'|\'g2.8xlarge\'|\'g3.4xlarge\'|\'g3.8xlarge\'|\'g3.16xlarge\'|\'g3s.xlarge\'|\'cg1.4xlarge\'|\'p2.xlarge\'|\'p2.8xlarge\'|\'p2.16xlarge\'|\'p3.2xlarge\'|\'p3.8xlarge\'|\'p3.16xlarge\'|\'d2.xlarge\'|\'d2.2xlarge\'|\'d2.4xlarge\'|\'d2.8xlarge\'|\'f1.2xlarge\'|\'f1.4xlarge\'|\'f1.16xlarge\'|\'m5.large\'|\'m5.xlarge\'|\'m5.2xlarge\'|\'m5.4xlarge\'|\'m5.12xlarge\'|\'m5.24xlarge\'|\'m5a.large\'|\'m5a.xlarge\'|\'m5a.2xlarge\'|\'m5a.4xlarge\'|\'m5a.12xlarge\'|\'m5a.24xlarge\'|\'m5d.large\'|\'m5d.xlarge\'|\'m5d.2xlarge\'|\'m5d.4xlarge\'|\'m5d.12xlarge\'|\'m5d.24xlarge\'|\'h1.2xlarge\'|\'h1.4xlarge\'|\'h1.8xlarge\'|\'h1.16xlarge\'|\'z1d.large\'|\'z1d.xlarge\'|\'z1d.2xlarge\'|\'z1d.3xlarge\'|\'z1d.6xlarge\'|\'z1d.12xlarge\'|\'u-6tb1.metal\'|\'u-9tb1.metal\'|\'u-12tb1.metal\',
                        \'ProductDescription\': \'Linux/UNIX\'|\'Linux/UNIX (Amazon VPC)\'|\'Windows\'|\'Windows (Amazon VPC)\',
                        \'SpotPrice\': \'string\',
                        \'Timestamp\': datetime(2015, 1, 1)
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
        
        """
        pass


class DescribeTags(Paginator):
    def paginate(self, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeTags>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DryRun=True|False,
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'ResourceId\': \'string\',
                        \'ResourceType\': \'customer-gateway\'|\'dedicated-host\'|\'dhcp-options\'|\'image\'|\'instance\'|\'internet-gateway\'|\'network-acl\'|\'network-interface\'|\'reserved-instances\'|\'route-table\'|\'snapshot\'|\'spot-instances-request\'|\'subnet\'|\'security-group\'|\'volume\'|\'vpc\'|\'vpn-connection\'|\'vpn-gateway\',
                        \'Value\': \'string\'
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
        
        """
        pass


class DescribeVolumeStatus(Paginator):
    def paginate(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumeStatus>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
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
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
          
          **Response Syntax** 
        
          ::
        
            {
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


class DescribeVolumes(Paginator):
    def paginate(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
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
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Volumes\': [
                    {
                        \'Attachments\': [
                            {
                                \'AttachTime\': datetime(2015, 1, 1),
                                \'Device\': \'string\',
                                \'InstanceId\': \'string\',
                                \'State\': \'attaching\'|\'attached\'|\'detaching\'|\'detached\'|\'busy\',
                                \'VolumeId\': \'string\',
                                \'DeleteOnTermination\': True|False
                            },
                        ],
                        \'AvailabilityZone\': \'string\',
                        \'CreateTime\': datetime(2015, 1, 1),
                        \'Encrypted\': True|False,
                        \'KmsKeyId\': \'string\',
                        \'Size\': 123,
                        \'SnapshotId\': \'string\',
                        \'State\': \'creating\'|\'available\'|\'in-use\'|\'deleting\'|\'deleted\'|\'error\',
                        \'VolumeId\': \'string\',
                        \'Iops\': 123,
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'VolumeType\': \'standard\'|\'io1\'|\'gp2\'|\'sc1\'|\'st1\'
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
        
                  The number of I/O operations per second (IOPS) that the volume supports. For Provisioned IOPS SSD volumes, this represents the number of IOPS that are provisioned for the volume. For General Purpose SSD volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see `Amazon EBS Volume Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
                  Constraint: Range is 100-32000 IOPS for io1 volumes and 100-10000 IOPS for ``gp2`` volumes.
        
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
        
        """
        pass
