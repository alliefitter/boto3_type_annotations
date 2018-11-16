from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeAutoScalingGroups(Paginator):
    def paginate(self, AutoScalingGroupNames: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAutoScalingGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AutoScalingGroupNames=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AutoScalingGroupNames: list
        :param AutoScalingGroupNames: 
        
          The names of the Auto Scaling groups. You can specify up to ``MaxRecords`` names. If you omit this parameter, all Auto Scaling groups are described.
        
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
                \'AutoScalingGroups\': [
                    {
                        \'AutoScalingGroupName\': \'string\',
                        \'AutoScalingGroupARN\': \'string\',
                        \'LaunchConfigurationName\': \'string\',
                        \'LaunchTemplate\': {
                            \'LaunchTemplateId\': \'string\',
                            \'LaunchTemplateName\': \'string\',
                            \'Version\': \'string\'
                        },
                        \'MinSize\': 123,
                        \'MaxSize\': 123,
                        \'DesiredCapacity\': 123,
                        \'DefaultCooldown\': 123,
                        \'AvailabilityZones\': [
                            \'string\',
                        ],
                        \'LoadBalancerNames\': [
                            \'string\',
                        ],
                        \'TargetGroupARNs\': [
                            \'string\',
                        ],
                        \'HealthCheckType\': \'string\',
                        \'HealthCheckGracePeriod\': 123,
                        \'Instances\': [
                            {
                                \'InstanceId\': \'string\',
                                \'AvailabilityZone\': \'string\',
                                \'LifecycleState\': \'Pending\'|\'Pending:Wait\'|\'Pending:Proceed\'|\'Quarantined\'|\'InService\'|\'Terminating\'|\'Terminating:Wait\'|\'Terminating:Proceed\'|\'Terminated\'|\'Detaching\'|\'Detached\'|\'EnteringStandby\'|\'Standby\',
                                \'HealthStatus\': \'string\',
                                \'LaunchConfigurationName\': \'string\',
                                \'LaunchTemplate\': {
                                    \'LaunchTemplateId\': \'string\',
                                    \'LaunchTemplateName\': \'string\',
                                    \'Version\': \'string\'
                                },
                                \'ProtectedFromScaleIn\': True|False
                            },
                        ],
                        \'CreatedTime\': datetime(2015, 1, 1),
                        \'SuspendedProcesses\': [
                            {
                                \'ProcessName\': \'string\',
                                \'SuspensionReason\': \'string\'
                            },
                        ],
                        \'PlacementGroup\': \'string\',
                        \'VPCZoneIdentifier\': \'string\',
                        \'EnabledMetrics\': [
                            {
                                \'Metric\': \'string\',
                                \'Granularity\': \'string\'
                            },
                        ],
                        \'Status\': \'string\',
                        \'Tags\': [
                            {
                                \'ResourceId\': \'string\',
                                \'ResourceType\': \'string\',
                                \'Key\': \'string\',
                                \'Value\': \'string\',
                                \'PropagateAtLaunch\': True|False
                            },
                        ],
                        \'TerminationPolicies\': [
                            \'string\',
                        ],
                        \'NewInstancesProtectedFromScaleIn\': True|False,
                        \'ServiceLinkedRoleARN\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AutoScalingGroups** *(list) --* 
        
              The groups.
        
              - *(dict) --* 
        
                Describes an Auto Scaling group.
        
                - **AutoScalingGroupName** *(string) --* 
        
                  The name of the Auto Scaling group.
        
                - **AutoScalingGroupARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the Auto Scaling group.
        
                - **LaunchConfigurationName** *(string) --* 
        
                  The name of the associated launch configuration.
        
                - **LaunchTemplate** *(dict) --* 
        
                  The launch template for the group.
        
                  - **LaunchTemplateId** *(string) --* 
        
                    The ID of the launch template. You must specify either a template ID or a template name.
        
                  - **LaunchTemplateName** *(string) --* 
        
                    The name of the launch template. You must specify either a template name or a template ID.
        
                  - **Version** *(string) --* 
        
                    The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is ``$Default`` .
        
                - **MinSize** *(integer) --* 
        
                  The minimum size of the group.
        
                - **MaxSize** *(integer) --* 
        
                  The maximum size of the group.
        
                - **DesiredCapacity** *(integer) --* 
        
                  The desired size of the group.
        
                - **DefaultCooldown** *(integer) --* 
        
                  The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
        
                - **AvailabilityZones** *(list) --* 
        
                  One or more Availability Zones for the group.
        
                  - *(string) --* 
              
                - **LoadBalancerNames** *(list) --* 
        
                  One or more load balancers associated with the group.
        
                  - *(string) --* 
              
                - **TargetGroupARNs** *(list) --* 
        
                  The Amazon Resource Names (ARN) of the target groups for your load balancer.
        
                  - *(string) --* 
              
                - **HealthCheckType** *(string) --* 
        
                  The service to use for the health checks. The valid values are ``EC2`` and ``ELB`` .
        
                - **HealthCheckGracePeriod** *(integer) --* 
        
                  The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service.
        
                - **Instances** *(list) --* 
        
                  The EC2 instances associated with the group.
        
                  - *(dict) --* 
        
                    Describes an EC2 instance.
        
                    - **InstanceId** *(string) --* 
        
                      The ID of the instance.
        
                    - **AvailabilityZone** *(string) --* 
        
                      The Availability Zone in which the instance is running.
        
                    - **LifecycleState** *(string) --* 
        
                      A description of the current lifecycle state. Note that the ``Quarantined`` state is not used.
        
                    - **HealthStatus** *(string) --* 
        
                      The last reported health status of the instance. \"Healthy\" means that the instance is healthy and should remain in service. \"Unhealthy\" means that the instance is unhealthy and Amazon EC2 Auto Scaling should terminate and replace it.
        
                    - **LaunchConfigurationName** *(string) --* 
        
                      The launch configuration associated with the instance.
        
                    - **LaunchTemplate** *(dict) --* 
        
                      The launch template for the instance.
        
                      - **LaunchTemplateId** *(string) --* 
        
                        The ID of the launch template. You must specify either a template ID or a template name.
        
                      - **LaunchTemplateName** *(string) --* 
        
                        The name of the launch template. You must specify either a template name or a template ID.
        
                      - **Version** *(string) --* 
        
                        The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is ``$Default`` .
        
                    - **ProtectedFromScaleIn** *(boolean) --* 
        
                      Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.
        
                - **CreatedTime** *(datetime) --* 
        
                  The date and time the group was created.
        
                - **SuspendedProcesses** *(list) --* 
        
                  The suspended processes associated with the group.
        
                  - *(dict) --* 
        
                    Describes an automatic scaling process that has been suspended. For more information, see  ProcessType .
        
                    - **ProcessName** *(string) --* 
        
                      The name of the suspended process.
        
                    - **SuspensionReason** *(string) --* 
        
                      The reason that the process was suspended.
        
                - **PlacementGroup** *(string) --* 
        
                  The name of the placement group into which you\'ll launch your instances, if any. For more information, see `Placement Groups <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
                - **VPCZoneIdentifier** *(string) --* 
        
                  One or more subnet IDs, if applicable, separated by commas.
        
                  If you specify ``VPCZoneIdentifier`` and ``AvailabilityZones`` , ensure that the Availability Zones of the subnets match the values for ``AvailabilityZones`` .
        
                - **EnabledMetrics** *(list) --* 
        
                  The metrics enabled for the group.
        
                  - *(dict) --* 
        
                    Describes an enabled metric.
        
                    - **Metric** *(string) --* 
        
                      One of the following metrics:
        
                      * ``GroupMinSize``   
                       
                      * ``GroupMaxSize``   
                       
                      * ``GroupDesiredCapacity``   
                       
                      * ``GroupInServiceInstances``   
                       
                      * ``GroupPendingInstances``   
                       
                      * ``GroupStandbyInstances``   
                       
                      * ``GroupTerminatingInstances``   
                       
                      * ``GroupTotalInstances``   
                       
                    - **Granularity** *(string) --* 
        
                      The granularity of the metric. The only valid value is ``1Minute`` .
        
                - **Status** *(string) --* 
        
                  The current state of the group when  DeleteAutoScalingGroup is in progress.
        
                - **Tags** *(list) --* 
        
                  The tags for the group.
        
                  - *(dict) --* 
        
                    Describes a tag for an Auto Scaling group.
        
                    - **ResourceId** *(string) --* 
        
                      The name of the group.
        
                    - **ResourceType** *(string) --* 
        
                      The type of resource. The only supported value is ``auto-scaling-group`` .
        
                    - **Key** *(string) --* 
        
                      The tag key.
        
                    - **Value** *(string) --* 
        
                      The tag value.
        
                    - **PropagateAtLaunch** *(boolean) --* 
        
                      Determines whether the tag is added to new instances as they are launched in the group.
        
                - **TerminationPolicies** *(list) --* 
        
                  The termination policies for the group.
        
                  - *(string) --* 
              
                - **NewInstancesProtectedFromScaleIn** *(boolean) --* 
        
                  Indicates whether newly launched instances are protected from termination by Auto Scaling when scaling in.
        
                - **ServiceLinkedRoleARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf.
        
        """
        pass


class DescribeAutoScalingInstances(Paginator):
    def paginate(self, InstanceIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAutoScalingInstances>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              InstanceIds=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type InstanceIds: list
        :param InstanceIds: 
        
          The IDs of the instances. You can specify up to ``MaxRecords`` IDs. If you omit this parameter, all Auto Scaling instances are described. If you specify an ID that does not exist, it is ignored with no error.
        
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
                \'AutoScalingInstances\': [
                    {
                        \'InstanceId\': \'string\',
                        \'AutoScalingGroupName\': \'string\',
                        \'AvailabilityZone\': \'string\',
                        \'LifecycleState\': \'string\',
                        \'HealthStatus\': \'string\',
                        \'LaunchConfigurationName\': \'string\',
                        \'LaunchTemplate\': {
                            \'LaunchTemplateId\': \'string\',
                            \'LaunchTemplateName\': \'string\',
                            \'Version\': \'string\'
                        },
                        \'ProtectedFromScaleIn\': True|False
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AutoScalingInstances** *(list) --* 
        
              The instances.
        
              - *(dict) --* 
        
                Describes an EC2 instance associated with an Auto Scaling group.
        
                - **InstanceId** *(string) --* 
        
                  The ID of the instance.
        
                - **AutoScalingGroupName** *(string) --* 
        
                  The name of the Auto Scaling group for the instance.
        
                - **AvailabilityZone** *(string) --* 
        
                  The Availability Zone for the instance.
        
                - **LifecycleState** *(string) --* 
        
                  The lifecycle state for the instance. For more information, see `Auto Scaling Lifecycle <http://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroupLifecycle.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        
                - **HealthStatus** *(string) --* 
        
                  The last reported health status of this instance. \"Healthy\" means that the instance is healthy and should remain in service. \"Unhealthy\" means that the instance is unhealthy and Amazon EC2 Auto Scaling should terminate and replace it.
        
                - **LaunchConfigurationName** *(string) --* 
        
                  The launch configuration used to launch the instance. This value is not available if you attached the instance to the Auto Scaling group.
        
                - **LaunchTemplate** *(dict) --* 
        
                  The launch template for the instance.
        
                  - **LaunchTemplateId** *(string) --* 
        
                    The ID of the launch template. You must specify either a template ID or a template name.
        
                  - **LaunchTemplateName** *(string) --* 
        
                    The name of the launch template. You must specify either a template name or a template ID.
        
                  - **Version** *(string) --* 
        
                    The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is ``$Default`` .
        
                - **ProtectedFromScaleIn** *(boolean) --* 
        
                  Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.
        
        """
        pass


class DescribeLaunchConfigurations(Paginator):
    def paginate(self, LaunchConfigurationNames: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLaunchConfigurations>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              LaunchConfigurationNames=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type LaunchConfigurationNames: list
        :param LaunchConfigurationNames: 
        
          The launch configuration names. If you omit this parameter, all launch configurations are described.
        
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
                \'LaunchConfigurations\': [
                    {
                        \'LaunchConfigurationName\': \'string\',
                        \'LaunchConfigurationARN\': \'string\',
                        \'ImageId\': \'string\',
                        \'KeyName\': \'string\',
                        \'SecurityGroups\': [
                            \'string\',
                        ],
                        \'ClassicLinkVPCId\': \'string\',
                        \'ClassicLinkVPCSecurityGroups\': [
                            \'string\',
                        ],
                        \'UserData\': \'string\',
                        \'InstanceType\': \'string\',
                        \'KernelId\': \'string\',
                        \'RamdiskId\': \'string\',
                        \'BlockDeviceMappings\': [
                            {
                                \'VirtualName\': \'string\',
                                \'DeviceName\': \'string\',
                                \'Ebs\': {
                                    \'SnapshotId\': \'string\',
                                    \'VolumeSize\': 123,
                                    \'VolumeType\': \'string\',
                                    \'DeleteOnTermination\': True|False,
                                    \'Iops\': 123,
                                    \'Encrypted\': True|False
                                },
                                \'NoDevice\': True|False
                            },
                        ],
                        \'InstanceMonitoring\': {
                            \'Enabled\': True|False
                        },
                        \'SpotPrice\': \'string\',
                        \'IamInstanceProfile\': \'string\',
                        \'CreatedTime\': datetime(2015, 1, 1),
                        \'EbsOptimized\': True|False,
                        \'AssociatePublicIpAddress\': True|False,
                        \'PlacementTenancy\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **LaunchConfigurations** *(list) --* 
        
              The launch configurations.
        
              - *(dict) --* 
        
                Describes a launch configuration.
        
                - **LaunchConfigurationName** *(string) --* 
        
                  The name of the launch configuration.
        
                - **LaunchConfigurationARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the launch configuration.
        
                - **ImageId** *(string) --* 
        
                  The ID of the Amazon Machine Image (AMI).
        
                - **KeyName** *(string) --* 
        
                  The name of the key pair.
        
                - **SecurityGroups** *(list) --* 
        
                  The security groups to associate with the instances.
        
                  - *(string) --* 
              
                - **ClassicLinkVPCId** *(string) --* 
        
                  The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to. This parameter can only be used if you are launching EC2-Classic instances. For more information, see `ClassicLink <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
                - **ClassicLinkVPCSecurityGroups** *(list) --* 
        
                  The IDs of one or more security groups for the VPC specified in ``ClassicLinkVPCId`` . This parameter is required if you specify a ClassicLink-enabled VPC, and cannot be used otherwise. For more information, see `ClassicLink <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
                  - *(string) --* 
              
                - **UserData** *(string) --* 
        
                  The user data available to the instances.
        
                - **InstanceType** *(string) --* 
        
                  The instance type for the instances.
        
                - **KernelId** *(string) --* 
        
                  The ID of the kernel associated with the AMI.
        
                - **RamdiskId** *(string) --* 
        
                  The ID of the RAM disk associated with the AMI.
        
                - **BlockDeviceMappings** *(list) --* 
        
                  A block device mapping, which specifies the block devices for the instance.
        
                  - *(dict) --* 
        
                    Describes a block device mapping.
        
                    - **VirtualName** *(string) --* 
        
                      The name of the virtual device (for example, ``ephemeral0`` ).
        
                    - **DeviceName** *(string) --* 
        
                      The device name exposed to the EC2 instance (for example, ``/dev/sdh`` or ``xvdh`` ).
        
                    - **Ebs** *(dict) --* 
        
                      The information about the Amazon EBS volume.
        
                      - **SnapshotId** *(string) --* 
        
                        The ID of the snapshot.
        
                      - **VolumeSize** *(integer) --* 
        
                        The volume size, in GiB. For ``standard`` volumes, specify a value from 1 to 1,024. For ``io1`` volumes, specify a value from 4 to 16,384. For ``gp2`` volumes, specify a value from 1 to 16,384. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
        
                        Default: If you create a volume from a snapshot and you don\'t specify a volume size, the default is the snapshot size.
        
                      - **VolumeType** *(string) --* 
        
                        The volume type. For more information, see `Amazon EBS Volume Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
                        Valid values: ``standard`` | ``io1`` | ``gp2``  
        
                      - **DeleteOnTermination** *(boolean) --* 
        
                        Indicates whether the volume is deleted on instance termination. The default is ``true`` .
        
                      - **Iops** *(integer) --* 
        
                        The number of I/O operations per second (IOPS) to provision for the volume.
        
                        Constraint: Required when the volume type is ``io1`` .
        
                      - **Encrypted** *(boolean) --* 
        
                        Indicates whether the volume should be encrypted. Encrypted EBS volumes must be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are automatically encrypted. There is no way to create an encrypted volume from an unencrypted snapshot or an unencrypted volume from an encrypted snapshot. For more information, see `Amazon EBS Encryption <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ in the *Amazon Elastic Compute Cloud User Guide* .
        
                    - **NoDevice** *(boolean) --* 
        
                      Suppresses a device mapping.
        
                      If this parameter is true for the root device, the instance might fail the EC2 health check. Amazon EC2 Auto Scaling launches a replacement instance if the instance fails the health check.
        
                - **InstanceMonitoring** *(dict) --* 
        
                  Controls whether instances in this group are launched with detailed (``true`` ) or basic (``false`` ) monitoring.
        
                  - **Enabled** *(boolean) --* 
        
                    If ``true`` , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
        
                - **SpotPrice** *(string) --* 
        
                  The price to bid when launching Spot Instances.
        
                - **IamInstanceProfile** *(string) --* 
        
                  The name or Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance.
        
                - **CreatedTime** *(datetime) --* 
        
                  The creation date and time for the launch configuration.
        
                - **EbsOptimized** *(boolean) --* 
        
                  Controls whether the instance is optimized for EBS I/O (``true`` ) or not (``false`` ).
        
                - **AssociatePublicIpAddress** *(boolean) --* 
        
                  [EC2-VPC] Indicates whether to assign a public IP address to each instance.
        
                - **PlacementTenancy** *(string) --* 
        
                  The tenancy of the instance, either ``default`` or ``dedicated`` . An instance with ``dedicated`` tenancy runs in an isolated, single-tenant hardware and can only be launched into a VPC.
        
        """
        pass


class DescribeNotificationConfigurations(Paginator):
    def paginate(self, AutoScalingGroupNames: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeNotificationConfigurations>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AutoScalingGroupNames=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AutoScalingGroupNames: list
        :param AutoScalingGroupNames: 
        
          The name of the Auto Scaling group.
        
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
                \'NotificationConfigurations\': [
                    {
                        \'AutoScalingGroupName\': \'string\',
                        \'TopicARN\': \'string\',
                        \'NotificationType\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NotificationConfigurations** *(list) --* 
        
              The notification configurations.
        
              - *(dict) --* 
        
                Describes a notification.
        
                - **AutoScalingGroupName** *(string) --* 
        
                  The name of the Auto Scaling group.
        
                - **TopicARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic.
        
                - **NotificationType** *(string) --* 
        
                  One of the following event notification types:
        
                  * ``autoscaling:EC2_INSTANCE_LAUNCH``   
                   
                  * ``autoscaling:EC2_INSTANCE_LAUNCH_ERROR``   
                   
                  * ``autoscaling:EC2_INSTANCE_TERMINATE``   
                   
                  * ``autoscaling:EC2_INSTANCE_TERMINATE_ERROR``   
                   
                  * ``autoscaling:TEST_NOTIFICATION``   
                   
        """
        pass


class DescribePolicies(Paginator):
    def paginate(self, AutoScalingGroupName: str = None, PolicyNames: List = None, PolicyTypes: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribePolicies>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AutoScalingGroupName=\'string\',
              PolicyNames=[
                  \'string\',
              ],
              PolicyTypes=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: 
        
          The name of the Auto Scaling group.
        
        :type PolicyNames: list
        :param PolicyNames: 
        
          The names of one or more policies. If you omit this parameter, all policies are described. If an group name is provided, the results are limited to that group. This list is limited to 50 items. If you specify an unknown policy name, it is ignored with no error.
        
          - *(string) --* 
        
        :type PolicyTypes: list
        :param PolicyTypes: 
        
          One or more policy types. Valid values are ``SimpleScaling`` and ``StepScaling`` .
        
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
                \'ScalingPolicies\': [
                    {
                        \'AutoScalingGroupName\': \'string\',
                        \'PolicyName\': \'string\',
                        \'PolicyARN\': \'string\',
                        \'PolicyType\': \'string\',
                        \'AdjustmentType\': \'string\',
                        \'MinAdjustmentStep\': 123,
                        \'MinAdjustmentMagnitude\': 123,
                        \'ScalingAdjustment\': 123,
                        \'Cooldown\': 123,
                        \'StepAdjustments\': [
                            {
                                \'MetricIntervalLowerBound\': 123.0,
                                \'MetricIntervalUpperBound\': 123.0,
                                \'ScalingAdjustment\': 123
                            },
                        ],
                        \'MetricAggregationType\': \'string\',
                        \'EstimatedInstanceWarmup\': 123,
                        \'Alarms\': [
                            {
                                \'AlarmName\': \'string\',
                                \'AlarmARN\': \'string\'
                            },
                        ],
                        \'TargetTrackingConfiguration\': {
                            \'PredefinedMetricSpecification\': {
                                \'PredefinedMetricType\': \'ASGAverageCPUUtilization\'|\'ASGAverageNetworkIn\'|\'ASGAverageNetworkOut\'|\'ALBRequestCountPerTarget\',
                                \'ResourceLabel\': \'string\'
                            },
                            \'CustomizedMetricSpecification\': {
                                \'MetricName\': \'string\',
                                \'Namespace\': \'string\',
                                \'Dimensions\': [
                                    {
                                        \'Name\': \'string\',
                                        \'Value\': \'string\'
                                    },
                                ],
                                \'Statistic\': \'Average\'|\'Minimum\'|\'Maximum\'|\'SampleCount\'|\'Sum\',
                                \'Unit\': \'string\'
                            },
                            \'TargetValue\': 123.0,
                            \'DisableScaleIn\': True|False
                        }
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ScalingPolicies** *(list) --* 
        
              The scaling policies.
        
              - *(dict) --* 
        
                Describes a scaling policy.
        
                - **AutoScalingGroupName** *(string) --* 
        
                  The name of the Auto Scaling group.
        
                - **PolicyName** *(string) --* 
        
                  The name of the scaling policy.
        
                - **PolicyARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the policy.
        
                - **PolicyType** *(string) --* 
        
                  The policy type. Valid values are ``SimpleScaling`` and ``StepScaling`` .
        
                - **AdjustmentType** *(string) --* 
        
                  The adjustment type, which specifies how ``ScalingAdjustment`` is interpreted. Valid values are ``ChangeInCapacity`` , ``ExactCapacity`` , and ``PercentChangeInCapacity`` .
        
                - **MinAdjustmentStep** *(integer) --* 
        
                  Available for backward compatibility. Use ``MinAdjustmentMagnitude`` instead.
        
                - **MinAdjustmentMagnitude** *(integer) --* 
        
                  The minimum number of instances to scale. If the value of ``AdjustmentType`` is ``PercentChangeInCapacity`` , the scaling policy changes the ``DesiredCapacity`` of the Auto Scaling group by at least this many instances. Otherwise, the error is ``ValidationError`` .
        
                - **ScalingAdjustment** *(integer) --* 
        
                  The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.
        
                - **Cooldown** *(integer) --* 
        
                  The amount of time, in seconds, after a scaling activity completes before any further dynamic scaling activities can start.
        
                - **StepAdjustments** *(list) --* 
        
                  A set of adjustments that enable you to scale based on the size of the alarm breach.
        
                  - *(dict) --* 
        
                    Describes an adjustment based on the difference between the value of the aggregated CloudWatch metric and the breach threshold that you\'ve defined for the alarm.
        
                    For the following examples, suppose that you have an alarm with a breach threshold of 50:
        
                    * If you want the adjustment to be triggered when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10. 
                     
                    * If you want the adjustment to be triggered when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0. 
                     
                    There are a few rules for the step adjustments for your step policy:
        
                    * The ranges of your step adjustments can\'t overlap or have a gap. 
                     
                    * At most one step adjustment can have a null lower bound. If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound. 
                     
                    * At most one step adjustment can have a null upper bound. If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound. 
                     
                    * The upper and lower bound can\'t be null in the same step adjustment. 
                     
                    - **MetricIntervalLowerBound** *(float) --* 
        
                      The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.
        
                    - **MetricIntervalUpperBound** *(float) --* 
        
                      The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.
        
                      The upper bound must be greater than the lower bound.
        
                    - **ScalingAdjustment** *(integer) --* 
        
                      The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.
        
                - **MetricAggregationType** *(string) --* 
        
                  The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` , ``Maximum`` , and ``Average`` .
        
                - **EstimatedInstanceWarmup** *(integer) --* 
        
                  The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics.
        
                - **Alarms** *(list) --* 
        
                  The CloudWatch alarms related to the policy.
        
                  - *(dict) --* 
        
                    Describes an alarm.
        
                    - **AlarmName** *(string) --* 
        
                      The name of the alarm.
        
                    - **AlarmARN** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the alarm.
        
                - **TargetTrackingConfiguration** *(dict) --* 
        
                  A target tracking policy.
        
                  - **PredefinedMetricSpecification** *(dict) --* 
        
                    A predefined metric. You can specify either a predefined metric or a customized metric.
        
                    - **PredefinedMetricType** *(string) --* 
        
                      The metric type.
        
                    - **ResourceLabel** *(string) --* 
        
                      Identifies the resource associated with the metric type. The following predefined metrics are available:
        
                      * ``ASGAverageCPUUtilization`` - average CPU utilization of the Auto Scaling group 
                       
                      * ``ASGAverageNetworkIn`` - average number of bytes received on all network interfaces by the Auto Scaling group 
                       
                      * ``ASGAverageNetworkOut`` - average number of bytes sent out on all network interfaces by the Auto Scaling group 
                       
                      * ``ALBRequestCountPerTarget`` - number of requests completed per target in an Application Load Balancer target group 
                       
                      For predefined metric types ``ASGAverageCPUUtilization`` , ``ASGAverageNetworkIn`` , and ``ASGAverageNetworkOut`` , the parameter must not be specified as the resource associated with the metric type is the Auto Scaling group. For predefined metric type ``ALBRequestCountPerTarget`` , the parameter must be specified in the format: ``app/*load-balancer-name* /*load-balancer-id* /targetgroup/*target-group-name* /*target-group-id* `` , where ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load balancer ARN, and ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the target group ARN. The target group must be attached to the Auto Scaling group.
        
                  - **CustomizedMetricSpecification** *(dict) --* 
        
                    A customized metric.
        
                    - **MetricName** *(string) --* 
        
                      The name of the metric.
        
                    - **Namespace** *(string) --* 
        
                      The namespace of the metric.
        
                    - **Dimensions** *(list) --* 
        
                      The dimensions of the metric.
        
                      - *(dict) --* 
        
                        Describes the dimension of a metric.
        
                        - **Name** *(string) --* 
        
                          The name of the dimension.
        
                        - **Value** *(string) --* 
        
                          The value of the dimension.
        
                    - **Statistic** *(string) --* 
        
                      The statistic of the metric.
        
                    - **Unit** *(string) --* 
        
                      The unit of the metric.
        
                  - **TargetValue** *(float) --* 
        
                    The target value for the metric.
        
                  - **DisableScaleIn** *(boolean) --* 
        
                    Indicates whether scale in by the target tracking policy is disabled. If scale in is disabled, the target tracking policy won\'t remove instances from the Auto Scaling group. Otherwise, the target tracking policy can remove instances from the Auto Scaling group. The default is disabled.
        
        """
        pass


class DescribeScalingActivities(Paginator):
    def paginate(self, ActivityIds: List = None, AutoScalingGroupName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeScalingActivities>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ActivityIds=[
                  \'string\',
              ],
              AutoScalingGroupName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ActivityIds: list
        :param ActivityIds: 
        
          The activity IDs of the desired scaling activities. You can specify up to 50 IDs. If you omit this parameter, all activities for the past six weeks are described. If unknown activities are requested, they are ignored with no error. If you specify an Auto Scaling group, the results are limited to that group.
        
          - *(string) --* 
        
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: 
        
          The name of the Auto Scaling group.
        
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
                \'Activities\': [
                    {
                        \'ActivityId\': \'string\',
                        \'AutoScalingGroupName\': \'string\',
                        \'Description\': \'string\',
                        \'Cause\': \'string\',
                        \'StartTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'StatusCode\': \'PendingSpotBidPlacement\'|\'WaitingForSpotInstanceRequestId\'|\'WaitingForSpotInstanceId\'|\'WaitingForInstanceId\'|\'PreInService\'|\'InProgress\'|\'WaitingForELBConnectionDraining\'|\'MidLifecycleAction\'|\'WaitingForInstanceWarmup\'|\'Successful\'|\'Failed\'|\'Cancelled\',
                        \'StatusMessage\': \'string\',
                        \'Progress\': 123,
                        \'Details\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Activities** *(list) --* 
        
              The scaling activities. Activities are sorted by start time. Activities still in progress are described first.
        
              - *(dict) --* 
        
                Describes scaling activity, which is a long-running process that represents a change to your Auto Scaling group, such as changing its size or replacing an instance.
        
                - **ActivityId** *(string) --* 
        
                  The ID of the activity.
        
                - **AutoScalingGroupName** *(string) --* 
        
                  The name of the Auto Scaling group.
        
                - **Description** *(string) --* 
        
                  A friendly, more verbose description of the activity.
        
                - **Cause** *(string) --* 
        
                  The reason the activity began.
        
                - **StartTime** *(datetime) --* 
        
                  The start time of the activity.
        
                - **EndTime** *(datetime) --* 
        
                  The end time of the activity.
        
                - **StatusCode** *(string) --* 
        
                  The current status of the activity.
        
                - **StatusMessage** *(string) --* 
        
                  A friendly, more verbose description of the activity status.
        
                - **Progress** *(integer) --* 
        
                  A value between 0 and 100 that indicates the progress of the activity.
        
                - **Details** *(string) --* 
        
                  The details about the activity.
        
        """
        pass


class DescribeScheduledActions(Paginator):
    def paginate(self, AutoScalingGroupName: str = None, ScheduledActionNames: List = None, StartTime: datetime = None, EndTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeScheduledActions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AutoScalingGroupName=\'string\',
              ScheduledActionNames=[
                  \'string\',
              ],
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: 
        
          The name of the Auto Scaling group.
        
        :type ScheduledActionNames: list
        :param ScheduledActionNames: 
        
          The names of one or more scheduled actions. You can specify up to 50 actions. If you omit this parameter, all scheduled actions are described. If you specify an unknown scheduled action, it is ignored with no error.
        
          - *(string) --* 
        
        :type StartTime: datetime
        :param StartTime: 
        
          The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        
        :type EndTime: datetime
        :param EndTime: 
        
          The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        
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
                \'ScheduledUpdateGroupActions\': [
                    {
                        \'AutoScalingGroupName\': \'string\',
                        \'ScheduledActionName\': \'string\',
                        \'ScheduledActionARN\': \'string\',
                        \'Time\': datetime(2015, 1, 1),
                        \'StartTime\': datetime(2015, 1, 1),
                        \'EndTime\': datetime(2015, 1, 1),
                        \'Recurrence\': \'string\',
                        \'MinSize\': 123,
                        \'MaxSize\': 123,
                        \'DesiredCapacity\': 123
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ScheduledUpdateGroupActions** *(list) --* 
        
              The scheduled actions.
        
              - *(dict) --* 
        
                Describes a scheduled scaling action. Used in response to  DescribeScheduledActions . 
        
                - **AutoScalingGroupName** *(string) --* 
        
                  The name of the Auto Scaling group.
        
                - **ScheduledActionName** *(string) --* 
        
                  The name of the scheduled action.
        
                - **ScheduledActionARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the scheduled action.
        
                - **Time** *(datetime) --* 
        
                  This parameter is deprecated.
        
                - **StartTime** *(datetime) --* 
        
                  The date and time that the action is scheduled to begin. This date and time can be up to one month in the future.
        
                  When ``StartTime`` and ``EndTime`` are specified with ``Recurrence`` , they form the boundaries of when the recurring action will start and stop.
        
                - **EndTime** *(datetime) --* 
        
                  The date and time that the action is scheduled to end. This date and time can be up to one month in the future.
        
                - **Recurrence** *(string) --* 
        
                  The recurring schedule for the action.
        
                - **MinSize** *(integer) --* 
        
                  The minimum size of the group.
        
                - **MaxSize** *(integer) --* 
        
                  The maximum size of the group.
        
                - **DesiredCapacity** *(integer) --* 
        
                  The number of instances you prefer to maintain in the group.
        
        """
        pass


class DescribeTags(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeTags>`_
        
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
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filters: list
        :param Filters: 
        
          A filter used to scope the tags to return.
        
          - *(dict) --* 
        
            Describes a filter.
        
            - **Name** *(string) --* 
        
              The name of the filter. The valid values are: ``\"auto-scaling-group\"`` , ``\"key\"`` , ``\"value\"`` , and ``\"propagate-at-launch\"`` .
        
            - **Values** *(list) --* 
        
              The value of the filter.
        
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
                        \'ResourceId\': \'string\',
                        \'ResourceType\': \'string\',
                        \'Key\': \'string\',
                        \'Value\': \'string\',
                        \'PropagateAtLaunch\': True|False
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Tags** *(list) --* 
        
              One or more tags.
        
              - *(dict) --* 
        
                Describes a tag for an Auto Scaling group.
        
                - **ResourceId** *(string) --* 
        
                  The name of the group.
        
                - **ResourceType** *(string) --* 
        
                  The type of resource. The only supported value is ``auto-scaling-group`` .
        
                - **Key** *(string) --* 
        
                  The tag key.
        
                - **Value** *(string) --* 
        
                  The tag value.
        
                - **PropagateAtLaunch** *(boolean) --* 
        
                  Determines whether the tag is added to new instances as they are launched in the group.
        
        """
        pass
