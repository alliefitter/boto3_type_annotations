from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListBootstrapActions(Paginator):
    def paginate(self, ClusterId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/ListBootstrapActions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ClusterId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The cluster identifier for the bootstrap actions to list.
        
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
                \'BootstrapActions\': [
                    {
                        \'Name\': \'string\',
                        \'ScriptPath\': \'string\',
                        \'Args\': [
                            \'string\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            This output contains the bootstrap actions detail.
        
            - **BootstrapActions** *(list) --* 
        
              The bootstrap actions associated with the cluster.
        
              - *(dict) --* 
        
                An entity describing an executable that runs on a cluster.
        
                - **Name** *(string) --* 
        
                  The name of the command.
        
                - **ScriptPath** *(string) --* 
        
                  The Amazon S3 location of the command script.
        
                - **Args** *(list) --* 
        
                  Arguments for Amazon EMR to pass to the command for execution.
        
                  - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListClusters(Paginator):
    def paginate(self, CreatedAfter: datetime = None, CreatedBefore: datetime = None, ClusterStates: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/ListClusters>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CreatedAfter=datetime(2015, 1, 1),
              CreatedBefore=datetime(2015, 1, 1),
              ClusterStates=[
                  \'STARTING\'|\'BOOTSTRAPPING\'|\'RUNNING\'|\'WAITING\'|\'TERMINATING\'|\'TERMINATED\'|\'TERMINATED_WITH_ERRORS\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CreatedAfter: datetime
        :param CreatedAfter: 
        
          The creation date and time beginning value filter for listing clusters.
        
        :type CreatedBefore: datetime
        :param CreatedBefore: 
        
          The creation date and time end value filter for listing clusters.
        
        :type ClusterStates: list
        :param ClusterStates: 
        
          The cluster state filters to apply when listing clusters.
        
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
                \'Clusters\': [
                    {
                        \'Id\': \'string\',
                        \'Name\': \'string\',
                        \'Status\': {
                            \'State\': \'STARTING\'|\'BOOTSTRAPPING\'|\'RUNNING\'|\'WAITING\'|\'TERMINATING\'|\'TERMINATED\'|\'TERMINATED_WITH_ERRORS\',
                            \'StateChangeReason\': {
                                \'Code\': \'INTERNAL_ERROR\'|\'VALIDATION_ERROR\'|\'INSTANCE_FAILURE\'|\'INSTANCE_FLEET_TIMEOUT\'|\'BOOTSTRAP_FAILURE\'|\'USER_REQUEST\'|\'STEP_FAILURE\'|\'ALL_STEPS_COMPLETED\',
                                \'Message\': \'string\'
                            },
                            \'Timeline\': {
                                \'CreationDateTime\': datetime(2015, 1, 1),
                                \'ReadyDateTime\': datetime(2015, 1, 1),
                                \'EndDateTime\': datetime(2015, 1, 1)
                            }
                        },
                        \'NormalizedInstanceHours\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            This contains a ClusterSummaryList with the cluster details; for example, the cluster IDs, names, and status.
        
            - **Clusters** *(list) --* 
        
              The list of clusters for the account based on the given filters.
        
              - *(dict) --* 
        
                The summary description of the cluster.
        
                - **Id** *(string) --* 
        
                  The unique identifier for the cluster.
        
                - **Name** *(string) --* 
        
                  The name of the cluster.
        
                - **Status** *(dict) --* 
        
                  The details about the current status of the cluster.
        
                  - **State** *(string) --* 
        
                    The current state of the cluster.
        
                  - **StateChangeReason** *(dict) --* 
        
                    The reason for the cluster status change.
        
                    - **Code** *(string) --* 
        
                      The programmatic code for the state change reason.
        
                    - **Message** *(string) --* 
        
                      The descriptive message for the state change reason.
        
                  - **Timeline** *(dict) --* 
        
                    A timeline that represents the status of a cluster over the lifetime of the cluster.
        
                    - **CreationDateTime** *(datetime) --* 
        
                      The creation date and time of the cluster.
        
                    - **ReadyDateTime** *(datetime) --* 
        
                      The date and time when the cluster was ready to execute steps.
        
                    - **EndDateTime** *(datetime) --* 
        
                      The date and time when the cluster was terminated.
        
                - **NormalizedInstanceHours** *(integer) --* 
        
                  An approximation of the cost of the cluster, represented in m1.small/hours. This value is incremented one time for every hour an m1.small instance runs. Larger instances are weighted more, so an EC2 instance that is roughly four times more expensive would result in the normalized instance hours being incremented by four. This result is only an approximation and does not reflect the actual billing rate.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListInstanceFleets(Paginator):
    def paginate(self, ClusterId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/ListInstanceFleets>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ClusterId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The unique identifier of the cluster.
        
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
                \'InstanceFleets\': [
                    {
                        \'Id\': \'string\',
                        \'Name\': \'string\',
                        \'Status\': {
                            \'State\': \'PROVISIONING\'|\'BOOTSTRAPPING\'|\'RUNNING\'|\'RESIZING\'|\'SUSPENDED\'|\'TERMINATING\'|\'TERMINATED\',
                            \'StateChangeReason\': {
                                \'Code\': \'INTERNAL_ERROR\'|\'VALIDATION_ERROR\'|\'INSTANCE_FAILURE\'|\'CLUSTER_TERMINATED\',
                                \'Message\': \'string\'
                            },
                            \'Timeline\': {
                                \'CreationDateTime\': datetime(2015, 1, 1),
                                \'ReadyDateTime\': datetime(2015, 1, 1),
                                \'EndDateTime\': datetime(2015, 1, 1)
                            }
                        },
                        \'InstanceFleetType\': \'MASTER\'|\'CORE\'|\'TASK\',
                        \'TargetOnDemandCapacity\': 123,
                        \'TargetSpotCapacity\': 123,
                        \'ProvisionedOnDemandCapacity\': 123,
                        \'ProvisionedSpotCapacity\': 123,
                        \'InstanceTypeSpecifications\': [
                            {
                                \'InstanceType\': \'string\',
                                \'WeightedCapacity\': 123,
                                \'BidPrice\': \'string\',
                                \'BidPriceAsPercentageOfOnDemandPrice\': 123.0,
                                \'Configurations\': [
                                    {
                                        \'Classification\': \'string\',
                                        \'Configurations\': {\'... recursive ...\'},
                                        \'Properties\': {
                                            \'string\': \'string\'
                                        }
                                    },
                                ],
                                \'EbsBlockDevices\': [
                                    {
                                        \'VolumeSpecification\': {
                                            \'VolumeType\': \'string\',
                                            \'Iops\': 123,
                                            \'SizeInGB\': 123
                                        },
                                        \'Device\': \'string\'
                                    },
                                ],
                                \'EbsOptimized\': True|False
                            },
                        ],
                        \'LaunchSpecifications\': {
                            \'SpotSpecification\': {
                                \'TimeoutDurationMinutes\': 123,
                                \'TimeoutAction\': \'SWITCH_TO_ON_DEMAND\'|\'TERMINATE_CLUSTER\',
                                \'BlockDurationMinutes\': 123
                            }
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **InstanceFleets** *(list) --* 
        
              The list of instance fleets for the cluster and given filters.
        
              - *(dict) --* 
        
                Describes an instance fleet, which is a group of EC2 instances that host a particular node type (master, core, or task) in an Amazon EMR cluster. Instance fleets can consist of a mix of instance types and On-Demand and Spot instances, which are provisioned to meet a defined target capacity. 
        
                .. note::
        
                  The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.
        
                - **Id** *(string) --* 
        
                  The unique identifier of the instance fleet.
        
                - **Name** *(string) --* 
        
                  A friendly name for the instance fleet.
        
                - **Status** *(dict) --* 
        
                  The current status of the instance fleet. 
        
                  - **State** *(string) --* 
        
                    A code representing the instance fleet status.
        
                    * ``PROVISIONING`` —The instance fleet is provisioning EC2 resources and is not yet ready to run jobs. 
                     
                    * ``BOOTSTRAPPING`` —EC2 instances and other resources have been provisioned and the bootstrap actions specified for the instances are underway. 
                     
                    * ``RUNNING`` —EC2 instances and other resources are running. They are either executing jobs or waiting to execute jobs. 
                     
                    * ``RESIZING`` —A resize operation is underway. EC2 instances are either being added or removed. 
                     
                    * ``SUSPENDED`` —A resize operation could not complete. Existing EC2 instances are running, but instances can\'t be added or removed. 
                     
                    * ``TERMINATING`` —The instance fleet is terminating EC2 instances. 
                     
                    * ``TERMINATED`` —The instance fleet is no longer active, and all EC2 instances have been terminated. 
                     
                  - **StateChangeReason** *(dict) --* 
        
                    Provides status change reason details for the instance fleet.
        
                    - **Code** *(string) --* 
        
                      A code corresponding to the reason the state change occurred.
        
                    - **Message** *(string) --* 
        
                      An explanatory message.
        
                  - **Timeline** *(dict) --* 
        
                    Provides historical timestamps for the instance fleet, including the time of creation, the time it became ready to run jobs, and the time of termination.
        
                    - **CreationDateTime** *(datetime) --* 
        
                      The time and date the instance fleet was created.
        
                    - **ReadyDateTime** *(datetime) --* 
        
                      The time and date the instance fleet was ready to run jobs.
        
                    - **EndDateTime** *(datetime) --* 
        
                      The time and date the instance fleet terminated.
        
                - **InstanceFleetType** *(string) --* 
        
                  The node type that the instance fleet hosts. Valid values are MASTER, CORE, or TASK. 
        
                - **TargetOnDemandCapacity** *(integer) --* 
        
                  The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand instances as specified by  InstanceTypeConfig . Each instance configuration has a specified ``WeightedCapacity`` . When an On-Demand instance is provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. You can use  InstanceFleet$ProvisionedOnDemandCapacity to determine the Spot capacity units that have been provisioned for the instance fleet.
        
                  .. note::
        
                    If not specified or set to 0, only Spot instances are provisioned for the instance fleet using ``TargetSpotCapacity`` . At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its value must be 1.
        
                - **TargetSpotCapacity** *(integer) --* 
        
                  The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot instances as specified by  InstanceTypeConfig . Each instance configuration has a specified ``WeightedCapacity`` . When a Spot instance is provisioned, the ``WeightedCapacity`` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a ``WeightedCapacity`` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. You can use  InstanceFleet$ProvisionedSpotCapacity to determine the Spot capacity units that have been provisioned for the instance fleet.
        
                  .. note::
        
                    If not specified or set to 0, only On-Demand instances are provisioned for the instance fleet. At least one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` should be greater than 0. For a master instance fleet, only one of ``TargetSpotCapacity`` and ``TargetOnDemandCapacity`` can be specified, and its value must be 1.
        
                - **ProvisionedOnDemandCapacity** *(integer) --* 
        
                  The number of On-Demand units that have been provisioned for the instance fleet to fulfill ``TargetOnDemandCapacity`` . This provisioned capacity might be less than or greater than ``TargetOnDemandCapacity`` .
        
                - **ProvisionedSpotCapacity** *(integer) --* 
        
                  The number of Spot units that have been provisioned for this instance fleet to fulfill ``TargetSpotCapacity`` . This provisioned capacity might be less than or greater than ``TargetSpotCapacity`` .
        
                - **InstanceTypeSpecifications** *(list) --* 
        
                  The specification for the instance types that comprise an instance fleet. Up to five unique instance specifications may be defined for each instance fleet. 
        
                  - *(dict) --* 
        
                    The configuration specification for each instance type in an instance fleet.
        
                    .. note::
        
                      The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.
        
                    - **InstanceType** *(string) --* 
        
                      The EC2 instance type, for example ``m3.xlarge`` .
        
                    - **WeightedCapacity** *(integer) --* 
        
                      The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in  InstanceFleetConfig . Capacity values represent performance characteristics such as vCPUs, memory, or I/O. If not specified, the default value is 1.
        
                    - **BidPrice** *(string) --* 
        
                      The bid price for each EC2 Spot instance type as defined by ``InstanceType`` . Expressed in USD.
        
                    - **BidPriceAsPercentageOfOnDemandPrice** *(float) --* 
        
                      The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as defined by ``InstanceType`` . Expressed as a number (for example, 20 specifies 20%).
        
                    - **Configurations** *(list) --* 
        
                      A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR.
        
                      - *(dict) --* 
        
                        .. note::
        
                          Amazon EMR releases 4.x or later.
        
                        An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see `Configuring Applications <http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .
        
                        - **Classification** *(string) --* 
        
                          The classification within a configuration.
        
                        - **Configurations** *(list) --* 
        
                          A list of additional configurations to apply within a configuration object.
        
                        - **Properties** *(dict) --* 
        
                          A set of properties specified within a configuration classification.
        
                          - *(string) --* 
                            
                            - *(string) --* 
                      
                    - **EbsBlockDevices** *(list) --* 
        
                      The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as defined by ``InstanceType`` .
        
                      - *(dict) --* 
        
                        Configuration of requested EBS block device associated with the instance group.
        
                        - **VolumeSpecification** *(dict) --* 
        
                          EBS volume specifications such as volume type, IOPS, and size (GiB) that will be requested for the EBS volume attached to an EC2 instance in the cluster.
        
                          - **VolumeType** *(string) --* 
        
                            The volume type. Volume types supported are gp2, io1, standard.
        
                          - **Iops** *(integer) --* 
        
                            The number of I/O operations per second (IOPS) that the volume supports.
        
                          - **SizeInGB** *(integer) --* 
        
                            The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
        
                        - **Device** *(string) --* 
        
                          The device name that is exposed to the instance, such as /dev/sdh.
        
                    - **EbsOptimized** *(boolean) --* 
        
                      Evaluates to ``TRUE`` when the specified ``InstanceType`` is EBS-optimized.
        
                - **LaunchSpecifications** *(dict) --* 
        
                  Describes the launch specification for an instance fleet. 
        
                  - **SpotSpecification** *(dict) --* 
        
                    The launch specification for Spot instances in the fleet, which determines the defined duration and provisioning timeout behavior.
        
                    - **TimeoutDurationMinutes** *(integer) --* 
        
                      The spot provisioning timeout period in minutes. If Spot instances are not provisioned within this time period, the ``TimeOutAction`` is taken. Minimum value is 5 and maximum value is 1440. The timeout applies only during initial provisioning, when the cluster is first created.
        
                    - **TimeoutAction** *(string) --* 
        
                      The action to take when ``TargetSpotCapacity`` has not been fulfilled when the ``TimeoutDurationMinutes`` has expired. Spot instances are not uprovisioned within the Spot provisioining timeout. Valid values are ``TERMINATE_CLUSTER`` and ``SWITCH_TO_ON_DEMAND`` . SWITCH_TO_ON_DEMAND specifies that if no Spot instances are available, On-Demand Instances should be provisioned to fulfill any remaining Spot capacity.
        
                    - **BlockDurationMinutes** *(integer) --* 
        
                      The defined duration for Spot instances (also known as Spot blocks) in minutes. When specified, the Spot instance does not terminate before the defined duration expires, and defined duration pricing for Spot instances applies. Valid values are 60, 120, 180, 240, 300, or 360. The duration period starts as soon as a Spot instance receives its instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for termination and provides a Spot instance termination notice, which gives the instance a two-minute warning before it terminates. 
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListInstanceGroups(Paginator):
    def paginate(self, ClusterId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/ListInstanceGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ClusterId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The identifier of the cluster for which to list the instance groups.
        
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
                \'InstanceGroups\': [
                    {
                        \'Id\': \'string\',
                        \'Name\': \'string\',
                        \'Market\': \'ON_DEMAND\'|\'SPOT\',
                        \'InstanceGroupType\': \'MASTER\'|\'CORE\'|\'TASK\',
                        \'BidPrice\': \'string\',
                        \'InstanceType\': \'string\',
                        \'RequestedInstanceCount\': 123,
                        \'RunningInstanceCount\': 123,
                        \'Status\': {
                            \'State\': \'PROVISIONING\'|\'BOOTSTRAPPING\'|\'RUNNING\'|\'RESIZING\'|\'SUSPENDED\'|\'TERMINATING\'|\'TERMINATED\'|\'ARRESTED\'|\'SHUTTING_DOWN\'|\'ENDED\',
                            \'StateChangeReason\': {
                                \'Code\': \'INTERNAL_ERROR\'|\'VALIDATION_ERROR\'|\'INSTANCE_FAILURE\'|\'CLUSTER_TERMINATED\',
                                \'Message\': \'string\'
                            },
                            \'Timeline\': {
                                \'CreationDateTime\': datetime(2015, 1, 1),
                                \'ReadyDateTime\': datetime(2015, 1, 1),
                                \'EndDateTime\': datetime(2015, 1, 1)
                            }
                        },
                        \'Configurations\': [
                            {
                                \'Classification\': \'string\',
                                \'Configurations\': {\'... recursive ...\'},
                                \'Properties\': {
                                    \'string\': \'string\'
                                }
                            },
                        ],
                        \'EbsBlockDevices\': [
                            {
                                \'VolumeSpecification\': {
                                    \'VolumeType\': \'string\',
                                    \'Iops\': 123,
                                    \'SizeInGB\': 123
                                },
                                \'Device\': \'string\'
                            },
                        ],
                        \'EbsOptimized\': True|False,
                        \'ShrinkPolicy\': {
                            \'DecommissionTimeout\': 123,
                            \'InstanceResizePolicy\': {
                                \'InstancesToTerminate\': [
                                    \'string\',
                                ],
                                \'InstancesToProtect\': [
                                    \'string\',
                                ],
                                \'InstanceTerminationTimeout\': 123
                            }
                        },
                        \'AutoScalingPolicy\': {
                            \'Status\': {
                                \'State\': \'PENDING\'|\'ATTACHING\'|\'ATTACHED\'|\'DETACHING\'|\'DETACHED\'|\'FAILED\',
                                \'StateChangeReason\': {
                                    \'Code\': \'USER_REQUEST\'|\'PROVISION_FAILURE\'|\'CLEANUP_FAILURE\',
                                    \'Message\': \'string\'
                                }
                            },
                            \'Constraints\': {
                                \'MinCapacity\': 123,
                                \'MaxCapacity\': 123
                            },
                            \'Rules\': [
                                {
                                    \'Name\': \'string\',
                                    \'Description\': \'string\',
                                    \'Action\': {
                                        \'Market\': \'ON_DEMAND\'|\'SPOT\',
                                        \'SimpleScalingPolicyConfiguration\': {
                                            \'AdjustmentType\': \'CHANGE_IN_CAPACITY\'|\'PERCENT_CHANGE_IN_CAPACITY\'|\'EXACT_CAPACITY\',
                                            \'ScalingAdjustment\': 123,
                                            \'CoolDown\': 123
                                        }
                                    },
                                    \'Trigger\': {
                                        \'CloudWatchAlarmDefinition\': {
                                            \'ComparisonOperator\': \'GREATER_THAN_OR_EQUAL\'|\'GREATER_THAN\'|\'LESS_THAN\'|\'LESS_THAN_OR_EQUAL\',
                                            \'EvaluationPeriods\': 123,
                                            \'MetricName\': \'string\',
                                            \'Namespace\': \'string\',
                                            \'Period\': 123,
                                            \'Statistic\': \'SAMPLE_COUNT\'|\'AVERAGE\'|\'SUM\'|\'MINIMUM\'|\'MAXIMUM\',
                                            \'Threshold\': 123.0,
                                            \'Unit\': \'NONE\'|\'SECONDS\'|\'MICRO_SECONDS\'|\'MILLI_SECONDS\'|\'BYTES\'|\'KILO_BYTES\'|\'MEGA_BYTES\'|\'GIGA_BYTES\'|\'TERA_BYTES\'|\'BITS\'|\'KILO_BITS\'|\'MEGA_BITS\'|\'GIGA_BITS\'|\'TERA_BITS\'|\'PERCENT\'|\'COUNT\'|\'BYTES_PER_SECOND\'|\'KILO_BYTES_PER_SECOND\'|\'MEGA_BYTES_PER_SECOND\'|\'GIGA_BYTES_PER_SECOND\'|\'TERA_BYTES_PER_SECOND\'|\'BITS_PER_SECOND\'|\'KILO_BITS_PER_SECOND\'|\'MEGA_BITS_PER_SECOND\'|\'GIGA_BITS_PER_SECOND\'|\'TERA_BITS_PER_SECOND\'|\'COUNT_PER_SECOND\',
                                            \'Dimensions\': [
                                                {
                                                    \'Key\': \'string\',
                                                    \'Value\': \'string\'
                                                },
                                            ]
                                        }
                                    }
                                },
                            ]
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            This input determines which instance groups to retrieve.
        
            - **InstanceGroups** *(list) --* 
        
              The list of instance groups for the cluster and given filters.
        
              - *(dict) --* 
        
                This entity represents an instance group, which is a group of instances that have common purpose. For example, CORE instance group is used for HDFS.
        
                - **Id** *(string) --* 
        
                  The identifier of the instance group.
        
                - **Name** *(string) --* 
        
                  The name of the instance group.
        
                - **Market** *(string) --* 
        
                  The marketplace to provision instances for this group. Valid values are ON_DEMAND or SPOT.
        
                - **InstanceGroupType** *(string) --* 
        
                  The type of the instance group. Valid values are MASTER, CORE or TASK.
        
                - **BidPrice** *(string) --* 
        
                  The maximum Spot price your are willing to pay for EC2 instances.
        
                  An optional, nullable field that applies if the ``MarketType`` for the instance group is specified as ``SPOT`` . Specify the maximum spot price in USD. If the value is NULL and ``SPOT`` is specified, the maximum Spot price is set equal to the On-Demand price.
        
                - **InstanceType** *(string) --* 
        
                  The EC2 instance type for all instances in the instance group.
        
                - **RequestedInstanceCount** *(integer) --* 
        
                  The target number of instances for the instance group.
        
                - **RunningInstanceCount** *(integer) --* 
        
                  The number of instances currently running in this instance group.
        
                - **Status** *(dict) --* 
        
                  The current status of the instance group.
        
                  - **State** *(string) --* 
        
                    The current state of the instance group.
        
                  - **StateChangeReason** *(dict) --* 
        
                    The status change reason details for the instance group.
        
                    - **Code** *(string) --* 
        
                      The programmable code for the state change reason.
        
                    - **Message** *(string) --* 
        
                      The status change reason description.
        
                  - **Timeline** *(dict) --* 
        
                    The timeline of the instance group status over time.
        
                    - **CreationDateTime** *(datetime) --* 
        
                      The creation date and time of the instance group.
        
                    - **ReadyDateTime** *(datetime) --* 
        
                      The date and time when the instance group became ready to perform tasks.
        
                    - **EndDateTime** *(datetime) --* 
        
                      The date and time when the instance group terminated.
        
                - **Configurations** *(list) --* 
        
                  .. note::
        
                    Amazon EMR releases 4.x or later.
        
                  The list of configurations supplied for an EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).
        
                  - *(dict) --* 
        
                    .. note::
        
                      Amazon EMR releases 4.x or later.
        
                    An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see `Configuring Applications <http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html>`__ .
        
                    - **Classification** *(string) --* 
        
                      The classification within a configuration.
        
                    - **Configurations** *(list) --* 
        
                      A list of additional configurations to apply within a configuration object.
        
                    - **Properties** *(dict) --* 
        
                      A set of properties specified within a configuration classification.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
                - **EbsBlockDevices** *(list) --* 
        
                  The EBS block devices that are mapped to this instance group.
        
                  - *(dict) --* 
        
                    Configuration of requested EBS block device associated with the instance group.
        
                    - **VolumeSpecification** *(dict) --* 
        
                      EBS volume specifications such as volume type, IOPS, and size (GiB) that will be requested for the EBS volume attached to an EC2 instance in the cluster.
        
                      - **VolumeType** *(string) --* 
        
                        The volume type. Volume types supported are gp2, io1, standard.
        
                      - **Iops** *(integer) --* 
        
                        The number of I/O operations per second (IOPS) that the volume supports.
        
                      - **SizeInGB** *(integer) --* 
        
                        The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
        
                    - **Device** *(string) --* 
        
                      The device name that is exposed to the instance, such as /dev/sdh.
        
                - **EbsOptimized** *(boolean) --* 
        
                  If the instance group is EBS-optimized. An Amazon EBS-optimized instance uses an optimized configuration stack and provides additional, dedicated capacity for Amazon EBS I/O.
        
                - **ShrinkPolicy** *(dict) --* 
        
                  Policy for customizing shrink operations.
        
                  - **DecommissionTimeout** *(integer) --* 
        
                    The desired timeout for decommissioning an instance. Overrides the default YARN decommissioning timeout.
        
                  - **InstanceResizePolicy** *(dict) --* 
        
                    Custom policy for requesting termination protection or termination of specific instances when shrinking an instance group.
        
                    - **InstancesToTerminate** *(list) --* 
        
                      Specific list of instances to be terminated when shrinking an instance group.
        
                      - *(string) --* 
                  
                    - **InstancesToProtect** *(list) --* 
        
                      Specific list of instances to be protected when shrinking an instance group.
        
                      - *(string) --* 
                  
                    - **InstanceTerminationTimeout** *(integer) --* 
        
                      Decommissioning timeout override for the specific list of instances to be terminated.
        
                - **AutoScalingPolicy** *(dict) --* 
        
                  An automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric. See PutAutoScalingPolicy.
        
                  - **Status** *(dict) --* 
        
                    The status of an automatic scaling policy. 
        
                    - **State** *(string) --* 
        
                      Indicates the status of the automatic scaling policy.
        
                    - **StateChangeReason** *(dict) --* 
        
                      The reason for a change in status.
        
                      - **Code** *(string) --* 
        
                        The code indicating the reason for the change in status.``USER_REQUEST`` indicates that the scaling policy status was changed by a user. ``PROVISION_FAILURE`` indicates that the status change was because the policy failed to provision. ``CLEANUP_FAILURE`` indicates an error.
        
                      - **Message** *(string) --* 
        
                        A friendly, more verbose message that accompanies an automatic scaling policy state change.
        
                  - **Constraints** *(dict) --* 
        
                    The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.
        
                    - **MinCapacity** *(integer) --* 
        
                      The lower boundary of EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.
        
                    - **MaxCapacity** *(integer) --* 
        
                      The upper boundary of EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.
        
                  - **Rules** *(list) --* 
        
                    The scale-in and scale-out rules that comprise the automatic scaling policy.
        
                    - *(dict) --* 
        
                      A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.
        
                      - **Name** *(string) --* 
        
                        The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.
        
                      - **Description** *(string) --* 
        
                        A friendly, more verbose description of the automatic scaling rule.
        
                      - **Action** *(dict) --* 
        
                        The conditions that trigger an automatic scaling activity.
        
                        - **Market** *(string) --* 
        
                          Not available for instance groups. Instance groups use the market type specified for the group.
        
                        - **SimpleScalingPolicyConfiguration** *(dict) --* 
        
                          The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.
        
                          - **AdjustmentType** *(string) --* 
        
                            The way in which EC2 instances are added (if ``ScalingAdjustment`` is a positive number) or terminated (if ``ScalingAdjustment`` is a negative number) each time the scaling activity is triggered. ``CHANGE_IN_CAPACITY`` is the default. ``CHANGE_IN_CAPACITY`` indicates that the EC2 instance count increments or decrements by ``ScalingAdjustment`` , which should be expressed as an integer. ``PERCENT_CHANGE_IN_CAPACITY`` indicates the instance count increments or decrements by the percentage specified by ``ScalingAdjustment`` , which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. ``EXACT_CAPACITY`` indicates the scaling activity results in an instance group with the number of EC2 instances specified by ``ScalingAdjustment`` , which should be expressed as a positive integer.
        
                          - **ScalingAdjustment** *(integer) --* 
        
                            The amount by which to scale in or scale out, based on the specified ``AdjustmentType`` . A positive value adds to the instance group\'s EC2 instance count while a negative number removes instances. If ``AdjustmentType`` is set to ``EXACT_CAPACITY`` , the number should only be a positive integer. If ``AdjustmentType`` is set to ``PERCENT_CHANGE_IN_CAPACITY`` , the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.
        
                          - **CoolDown** *(integer) --* 
        
                            The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.
        
                      - **Trigger** *(dict) --* 
        
                        The CloudWatch alarm definition that determines when automatic scaling activity is triggered.
        
                        - **CloudWatchAlarmDefinition** *(dict) --* 
        
                          The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.
        
                          - **ComparisonOperator** *(string) --* 
        
                            Determines how the metric specified by ``MetricName`` is compared to the value specified by ``Threshold`` .
        
                          - **EvaluationPeriods** *(integer) --* 
        
                            The number of periods, expressed in seconds using ``Period`` , during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is ``1`` .
        
                          - **MetricName** *(string) --* 
        
                            The name of the CloudWatch metric that is watched to determine an alarm condition.
        
                          - **Namespace** *(string) --* 
        
                            The namespace for the CloudWatch metric. The default is ``AWS/ElasticMapReduce`` .
        
                          - **Period** *(integer) --* 
        
                            The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is specified, specify ``300`` .
        
                          - **Statistic** *(string) --* 
        
                            The statistic to apply to the metric associated with the alarm. The default is ``AVERAGE`` .
        
                          - **Threshold** *(float) --* 
        
                            The value against which the specified statistic is compared.
        
                          - **Unit** *(string) --* 
        
                            The unit of measure associated with the CloudWatch metric being watched. The value specified for ``Unit`` must correspond to the units specified in the CloudWatch metric.
        
                          - **Dimensions** *(list) --* 
        
                            A CloudWatch metric dimension.
        
                            - *(dict) --* 
        
                              A CloudWatch dimension, which is specified using a ``Key`` (known as a ``Name`` in CloudWatch), ``Value`` pair. By default, Amazon EMR uses one dimension whose ``Key`` is ``JobFlowID`` and ``Value`` is a variable representing the cluster ID, which is ``${emr.clusterId}`` . This enables the rule to bootstrap when the cluster ID becomes available.
        
                              - **Key** *(string) --* 
        
                                The dimension name.
        
                              - **Value** *(string) --* 
        
                                The dimension value.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListInstances(Paginator):
    def paginate(self, ClusterId: str, InstanceGroupId: str = None, InstanceGroupTypes: List = None, InstanceFleetId: str = None, InstanceFleetType: str = None, InstanceStates: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/ListInstances>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ClusterId=\'string\',
              InstanceGroupId=\'string\',
              InstanceGroupTypes=[
                  \'MASTER\'|\'CORE\'|\'TASK\',
              ],
              InstanceFleetId=\'string\',
              InstanceFleetType=\'MASTER\'|\'CORE\'|\'TASK\',
              InstanceStates=[
                  \'AWAITING_FULFILLMENT\'|\'PROVISIONING\'|\'BOOTSTRAPPING\'|\'RUNNING\'|\'TERMINATED\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The identifier of the cluster for which to list the instances.
        
        :type InstanceGroupId: string
        :param InstanceGroupId: 
        
          The identifier of the instance group for which to list the instances.
        
        :type InstanceGroupTypes: list
        :param InstanceGroupTypes: 
        
          The type of instance group for which to list the instances.
        
          - *(string) --* 
        
        :type InstanceFleetId: string
        :param InstanceFleetId: 
        
          The unique identifier of the instance fleet.
        
        :type InstanceFleetType: string
        :param InstanceFleetType: 
        
          The node type of the instance fleet. For example MASTER, CORE, or TASK.
        
        :type InstanceStates: list
        :param InstanceStates: 
        
          A list of instance states that will filter the instances returned with this request.
        
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
                \'Instances\': [
                    {
                        \'Id\': \'string\',
                        \'Ec2InstanceId\': \'string\',
                        \'PublicDnsName\': \'string\',
                        \'PublicIpAddress\': \'string\',
                        \'PrivateDnsName\': \'string\',
                        \'PrivateIpAddress\': \'string\',
                        \'Status\': {
                            \'State\': \'AWAITING_FULFILLMENT\'|\'PROVISIONING\'|\'BOOTSTRAPPING\'|\'RUNNING\'|\'TERMINATED\',
                            \'StateChangeReason\': {
                                \'Code\': \'INTERNAL_ERROR\'|\'VALIDATION_ERROR\'|\'INSTANCE_FAILURE\'|\'BOOTSTRAP_FAILURE\'|\'CLUSTER_TERMINATED\',
                                \'Message\': \'string\'
                            },
                            \'Timeline\': {
                                \'CreationDateTime\': datetime(2015, 1, 1),
                                \'ReadyDateTime\': datetime(2015, 1, 1),
                                \'EndDateTime\': datetime(2015, 1, 1)
                            }
                        },
                        \'InstanceGroupId\': \'string\',
                        \'InstanceFleetId\': \'string\',
                        \'Market\': \'ON_DEMAND\'|\'SPOT\',
                        \'InstanceType\': \'string\',
                        \'EbsVolumes\': [
                            {
                                \'Device\': \'string\',
                                \'VolumeId\': \'string\'
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            This output contains the list of instances.
        
            - **Instances** *(list) --* 
        
              The list of instances for the cluster and given filters.
        
              - *(dict) --* 
        
                Represents an EC2 instance provisioned as part of cluster.
        
                - **Id** *(string) --* 
        
                  The unique identifier for the instance in Amazon EMR.
        
                - **Ec2InstanceId** *(string) --* 
        
                  The unique identifier of the instance in Amazon EC2.
        
                - **PublicDnsName** *(string) --* 
        
                  The public DNS name of the instance.
        
                - **PublicIpAddress** *(string) --* 
        
                  The public IP address of the instance.
        
                - **PrivateDnsName** *(string) --* 
        
                  The private DNS name of the instance.
        
                - **PrivateIpAddress** *(string) --* 
        
                  The private IP address of the instance.
        
                - **Status** *(dict) --* 
        
                  The current status of the instance.
        
                  - **State** *(string) --* 
        
                    The current state of the instance.
        
                  - **StateChangeReason** *(dict) --* 
        
                    The details of the status change reason for the instance.
        
                    - **Code** *(string) --* 
        
                      The programmable code for the state change reason.
        
                    - **Message** *(string) --* 
        
                      The status change reason description.
        
                  - **Timeline** *(dict) --* 
        
                    The timeline of the instance status over time.
        
                    - **CreationDateTime** *(datetime) --* 
        
                      The creation date and time of the instance.
        
                    - **ReadyDateTime** *(datetime) --* 
        
                      The date and time when the instance was ready to perform tasks.
        
                    - **EndDateTime** *(datetime) --* 
        
                      The date and time when the instance was terminated.
        
                - **InstanceGroupId** *(string) --* 
        
                  The identifier of the instance group to which this instance belongs.
        
                - **InstanceFleetId** *(string) --* 
        
                  The unique identifier of the instance fleet to which an EC2 instance belongs.
        
                - **Market** *(string) --* 
        
                  The instance purchasing option. Valid values are ``ON_DEMAND`` or ``SPOT`` . 
        
                - **InstanceType** *(string) --* 
        
                  The EC2 instance type, for example ``m3.xlarge`` .
        
                - **EbsVolumes** *(list) --* 
        
                  The list of EBS volumes that are attached to this instance.
        
                  - *(dict) --* 
        
                    EBS block device that\'s attached to an EC2 instance.
        
                    - **Device** *(string) --* 
        
                      The device name that is exposed to the instance, such as /dev/sdh.
        
                    - **VolumeId** *(string) --* 
        
                      The volume identifier of the EBS volume.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListSteps(Paginator):
    def paginate(self, ClusterId: str, StepStates: List = None, StepIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/ListSteps>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ClusterId=\'string\',
              StepStates=[
                  \'PENDING\'|\'CANCEL_PENDING\'|\'RUNNING\'|\'COMPLETED\'|\'CANCELLED\'|\'FAILED\'|\'INTERRUPTED\',
              ],
              StepIds=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]** 
        
          The identifier of the cluster for which to list the steps.
        
        :type StepStates: list
        :param StepStates: 
        
          The filter to limit the step list based on certain states.
        
          - *(string) --* 
        
        :type StepIds: list
        :param StepIds: 
        
          The filter to limit the step list based on the identifier of the steps.
        
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
                \'Steps\': [
                    {
                        \'Id\': \'string\',
                        \'Name\': \'string\',
                        \'Config\': {
                            \'Jar\': \'string\',
                            \'Properties\': {
                                \'string\': \'string\'
                            },
                            \'MainClass\': \'string\',
                            \'Args\': [
                                \'string\',
                            ]
                        },
                        \'ActionOnFailure\': \'TERMINATE_JOB_FLOW\'|\'TERMINATE_CLUSTER\'|\'CANCEL_AND_WAIT\'|\'CONTINUE\',
                        \'Status\': {
                            \'State\': \'PENDING\'|\'CANCEL_PENDING\'|\'RUNNING\'|\'COMPLETED\'|\'CANCELLED\'|\'FAILED\'|\'INTERRUPTED\',
                            \'StateChangeReason\': {
                                \'Code\': \'NONE\',
                                \'Message\': \'string\'
                            },
                            \'FailureDetails\': {
                                \'Reason\': \'string\',
                                \'Message\': \'string\',
                                \'LogFile\': \'string\'
                            },
                            \'Timeline\': {
                                \'CreationDateTime\': datetime(2015, 1, 1),
                                \'StartDateTime\': datetime(2015, 1, 1),
                                \'EndDateTime\': datetime(2015, 1, 1)
                            }
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            This output contains the list of steps returned in reverse order. This means that the last step is the first element in the list.
        
            - **Steps** *(list) --* 
        
              The filtered list of steps for the cluster.
        
              - *(dict) --* 
        
                The summary of the cluster step.
        
                - **Id** *(string) --* 
        
                  The identifier of the cluster step.
        
                - **Name** *(string) --* 
        
                  The name of the cluster step.
        
                - **Config** *(dict) --* 
        
                  The Hadoop job configuration of the cluster step.
        
                  - **Jar** *(string) --* 
        
                    The path to the JAR file that runs during the step.
        
                  - **Properties** *(dict) --* 
        
                    The list of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                  - **MainClass** *(string) --* 
        
                    The name of the main class in the specified Java file. If not specified, the JAR file should specify a main class in its manifest file.
        
                  - **Args** *(list) --* 
        
                    The list of command line arguments to pass to the JAR file\'s main function for execution.
        
                    - *(string) --* 
                
                - **ActionOnFailure** *(string) --* 
        
                  This specifies what action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER, CANCEL_AND_WAIT, and CONTINUE.
        
                - **Status** *(dict) --* 
        
                  The current execution status details of the cluster step.
        
                  - **State** *(string) --* 
        
                    The execution state of the cluster step.
        
                  - **StateChangeReason** *(dict) --* 
        
                    The reason for the step execution status change.
        
                    - **Code** *(string) --* 
        
                      The programmable code for the state change reason. Note: Currently, the service provides no code for the state change.
        
                    - **Message** *(string) --* 
        
                      The descriptive message for the state change reason.
        
                  - **FailureDetails** *(dict) --* 
        
                    The details for the step failure including reason, message, and log file path where the root cause was identified.
        
                    - **Reason** *(string) --* 
        
                      The reason for the step failure. In the case where the service cannot successfully determine the root cause of the failure, it returns \"Unknown Error\" as a reason.
        
                    - **Message** *(string) --* 
        
                      The descriptive message including the error the EMR service has identified as the cause of step failure. This is text from an error log that describes the root cause of the failure.
        
                    - **LogFile** *(string) --* 
        
                      The path to the log file where the step failure root cause was originally recorded.
        
                  - **Timeline** *(dict) --* 
        
                    The timeline of the cluster step status over time.
        
                    - **CreationDateTime** *(datetime) --* 
        
                      The date and time when the cluster step was created.
        
                    - **StartDateTime** *(datetime) --* 
        
                      The date and time when the cluster step execution started.
        
                    - **EndDateTime** *(datetime) --* 
        
                      The date and time when the cluster step execution completed or failed.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
