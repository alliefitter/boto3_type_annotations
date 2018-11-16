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
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        """
        
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        
        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """
        pass

    def create_cluster(self, ClusterName: str, NodeType: str, ReplicationFactor: int, IamRoleArn: str, Description: str = None, AvailabilityZones: List = None, SubnetGroupName: str = None, SecurityGroupIds: List = None, PreferredMaintenanceWindow: str = None, NotificationTopicArn: str = None, ParameterGroupName: str = None, Tags: List = None, SSESpecification: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/CreateCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_cluster(
              ClusterName=\'string\',
              NodeType=\'string\',
              Description=\'string\',
              ReplicationFactor=123,
              AvailabilityZones=[
                  \'string\',
              ],
              SubnetGroupName=\'string\',
              SecurityGroupIds=[
                  \'string\',
              ],
              PreferredMaintenanceWindow=\'string\',
              NotificationTopicArn=\'string\',
              IamRoleArn=\'string\',
              ParameterGroupName=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              SSESpecification={
                  \'Enabled\': True|False
              }
          )
        :type ClusterName: string
        :param ClusterName: **[REQUIRED]** 
        
          The cluster identifier. This parameter is stored as a lowercase string.
        
           **Constraints:**  
        
          * A name must contain from 1 to 20 alphanumeric characters or hyphens. 
           
          * The first character must be a letter. 
           
          * A name cannot end with a hyphen or contain two consecutive hyphens. 
           
        :type NodeType: string
        :param NodeType: **[REQUIRED]** 
        
          The compute and memory capacity of the nodes in the cluster.
        
        :type Description: string
        :param Description: 
        
          A description of the cluster.
        
        :type ReplicationFactor: integer
        :param ReplicationFactor: **[REQUIRED]** 
        
          The number of nodes in the DAX cluster. A replication factor of 1 will create a single-node cluster, without any read replicas. For additional fault tolerance, you can create a multiple node cluster with one or more read replicas. To do this, set *ReplicationFactor* to 2 or more.
        
          .. note::
        
            AWS recommends that you have at least two read replicas per cluster.
        
        :type AvailabilityZones: list
        :param AvailabilityZones: 
        
          The Availability Zones (AZs) in which the cluster nodes will be created. All nodes belonging to the cluster are placed in these Availability Zones. Use this parameter if you want to distribute the nodes across multiple AZs.
        
          - *(string) --* 
        
        :type SubnetGroupName: string
        :param SubnetGroupName: 
        
          The name of the subnet group to be used for the replication group.
        
          .. warning::
        
            DAX clusters can only run in an Amazon VPC environment. All of the subnets that you specify in a subnet group must exist in the same VPC.
        
        :type SecurityGroupIds: list
        :param SecurityGroupIds: 
        
          A list of security group IDs to be assigned to each node in the DAX cluster. (Each of the security group ID is system-generated.)
        
          If this parameter is not specified, DAX assigns the default VPC security group to each node.
        
          - *(string) --* 
        
        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow: 
        
          Specifies the weekly time range during which maintenance on the DAX cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ``ddd`` are:
        
          * ``sun``   
           
          * ``mon``   
           
          * ``tue``   
           
          * ``wed``   
           
          * ``thu``   
           
          * ``fri``   
           
          * ``sat``   
           
          Example: ``sun:05:00-sun:09:00``  
        
          .. note::
        
            If you don\'t specify a preferred maintenance window when you create or modify a cache cluster, DAX assigns a 60-minute maintenance window on a randomly selected day of the week.
        
        :type NotificationTopicArn: string
        :param NotificationTopicArn: 
        
          The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications will be sent.
        
          .. note::
        
            The Amazon SNS topic owner must be same as the DAX cluster owner.
        
        :type IamRoleArn: string
        :param IamRoleArn: **[REQUIRED]** 
        
          A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.
        
        :type ParameterGroupName: string
        :param ParameterGroupName: 
        
          The parameter group to be associated with the DAX cluster.
        
        :type Tags: list
        :param Tags: 
        
          A set of tags to associate with the DAX cluster. 
        
          - *(dict) --* 
        
            A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single DAX cluster.
        
            AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix ``user:`` .
        
            You cannot backdate the application of a tag.
        
            - **Key** *(string) --* 
        
              The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.
        
            - **Value** *(string) --* 
        
              The value of the tag. Tag values are case-sensitive and can be null. 
        
        :type SSESpecification: dict
        :param SSESpecification: 
        
          Represents the settings used to enable server-side encryption on the cluster.
        
          - **Enabled** *(boolean) --* **[REQUIRED]** 
        
            Indicates whether server-side encryption is enabled (true) or disabled (false) on the cluster.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterName\': \'string\',
                    \'Description\': \'string\',
                    \'ClusterArn\': \'string\',
                    \'TotalNodes\': 123,
                    \'ActiveNodes\': 123,
                    \'NodeType\': \'string\',
                    \'Status\': \'string\',
                    \'ClusterDiscoveryEndpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'NodeIdsToRemove\': [
                        \'string\',
                    ],
                    \'Nodes\': [
                        {
                            \'NodeId\': \'string\',
                            \'Endpoint\': {
                                \'Address\': \'string\',
                                \'Port\': 123
                            },
                            \'NodeCreateTime\': datetime(2015, 1, 1),
                            \'AvailabilityZone\': \'string\',
                            \'NodeStatus\': \'string\',
                            \'ParameterGroupStatus\': \'string\'
                        },
                    ],
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'NotificationConfiguration\': {
                        \'TopicArn\': \'string\',
                        \'TopicStatus\': \'string\'
                    },
                    \'SubnetGroup\': \'string\',
                    \'SecurityGroups\': [
                        {
                            \'SecurityGroupIdentifier\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'IamRoleArn\': \'string\',
                    \'ParameterGroup\': {
                        \'ParameterGroupName\': \'string\',
                        \'ParameterApplyStatus\': \'string\',
                        \'NodeIdsToReboot\': [
                            \'string\',
                        ]
                    },
                    \'SSEDescription\': {
                        \'Status\': \'ENABLING\'|\'ENABLED\'|\'DISABLING\'|\'DISABLED\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              A description of the DAX cluster that you have created.
        
              - **ClusterName** *(string) --* 
        
                The name of the DAX cluster.
        
              - **Description** *(string) --* 
        
                The description of the cluster.
        
              - **ClusterArn** *(string) --* 
        
                The Amazon Resource Name (ARN) that uniquely identifies the cluster. 
        
              - **TotalNodes** *(integer) --* 
        
                The total number of nodes in the cluster.
        
              - **ActiveNodes** *(integer) --* 
        
                The number of nodes in the cluster that are active (i.e., capable of serving requests).
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)
        
              - **Status** *(string) --* 
        
                The current status of the cluster.
        
              - **ClusterDiscoveryEndpoint** *(dict) --* 
        
                The configuration endpoint for this DAX cluster, consisting of a DNS name and a port number. Client applications can specify this endpoint, rather than an individual node endpoint, and allow the DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
        
                - **Address** *(string) --* 
        
                  The DNS hostname of the endpoint.
        
                - **Port** *(integer) --* 
        
                  The port number that applications should use to connect to the endpoint.
        
              - **NodeIdsToRemove** *(list) --* 
        
                A list of nodes to be removed from the cluster.
        
                - *(string) --* 
            
              - **Nodes** *(list) --* 
        
                A list of nodes that are currently in the cluster.
        
                - *(dict) --* 
        
                  Represents an individual node within a DAX cluster.
        
                  - **NodeId** *(string) --* 
        
                    A system-generated identifier for the node.
        
                  - **Endpoint** *(dict) --* 
        
                    The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
        
                    - **Address** *(string) --* 
        
                      The DNS hostname of the endpoint.
        
                    - **Port** *(integer) --* 
        
                      The port number that applications should use to connect to the endpoint.
        
                  - **NodeCreateTime** *(datetime) --* 
        
                    The date and time (in UNIX epoch format) when the node was launched.
        
                  - **AvailabilityZone** *(string) --* 
        
                    The Availability Zone (AZ) in which the node has been deployed.
        
                  - **NodeStatus** *(string) --* 
        
                    The current status of the node. For example: ``available`` .
        
                  - **ParameterGroupStatus** *(string) --* 
        
                    The status of the parameter group associated with this node. For example, ``in-sync`` .
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                A range of time when maintenance of DAX cluster software will be performed. For example: ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.
        
              - **NotificationConfiguration** *(dict) --* 
        
                Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).
        
                - **TopicArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that identifies the topic. 
        
                - **TopicStatus** *(string) --* 
        
                  The current state of the topic.
        
              - **SubnetGroup** *(string) --* 
        
                The subnet group where the DAX cluster is running.
        
              - **SecurityGroups** *(list) --* 
        
                A list of security groups, and the status of each, for the nodes in the cluster.
        
                - *(dict) --* 
        
                  An individual VPC security group and its status.
        
                  - **SecurityGroupIdentifier** *(string) --* 
        
                    The unique ID for this security group.
        
                  - **Status** *(string) --* 
        
                    The status of this security group.
        
              - **IamRoleArn** *(string) --* 
        
                A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.
        
              - **ParameterGroup** *(dict) --* 
        
                The parameter group being used by nodes in the cluster.
        
                - **ParameterGroupName** *(string) --* 
        
                  The name of the parameter group.
        
                - **ParameterApplyStatus** *(string) --* 
        
                  The status of parameter updates. 
        
                - **NodeIdsToReboot** *(list) --* 
        
                  The node IDs of one or more nodes to be rebooted.
        
                  - *(string) --* 
              
              - **SSEDescription** *(dict) --* 
        
                The description of the server-side encryption status on the specified DAX cluster.
        
                - **Status** *(string) --* 
        
                  The current state of server-side encryption:
        
                  * ``ENABLING`` - Server-side encryption is being enabled. 
                   
                  * ``ENABLED`` - Server-side encryption is enabled. 
                   
                  * ``DISABLING`` - Server-side encryption is being disabled. 
                   
                  * ``DISABLED`` - Server-side encryption is disabled. 
                   
        """
        pass

    def create_parameter_group(self, ParameterGroupName: str, Description: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/CreateParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_parameter_group(
              ParameterGroupName=\'string\',
              Description=\'string\'
          )
        :type ParameterGroupName: string
        :param ParameterGroupName: **[REQUIRED]** 
        
          The name of the parameter group to apply to all of the clusters in this replication group.
        
        :type Description: string
        :param Description: 
        
          A description of the parameter group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ParameterGroup\': {
                    \'ParameterGroupName\': \'string\',
                    \'Description\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ParameterGroup** *(dict) --* 
        
              Represents the output of a *CreateParameterGroup* action.
        
              - **ParameterGroupName** *(string) --* 
        
                The name of the parameter group.
        
              - **Description** *(string) --* 
        
                A description of the parameter group.
        
        """
        pass

    def create_subnet_group(self, SubnetGroupName: str, SubnetIds: List, Description: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/CreateSubnetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_subnet_group(
              SubnetGroupName=\'string\',
              Description=\'string\',
              SubnetIds=[
                  \'string\',
              ]
          )
        :type SubnetGroupName: string
        :param SubnetGroupName: **[REQUIRED]** 
        
          A name for the subnet group. This value is stored as a lowercase string. 
        
        :type Description: string
        :param Description: 
        
          A description for the subnet group
        
        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]** 
        
          A list of VPC subnet IDs for the subnet group.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SubnetGroup\': {
                    \'SubnetGroupName\': \'string\',
                    \'Description\': \'string\',
                    \'VpcId\': \'string\',
                    \'Subnets\': [
                        {
                            \'SubnetIdentifier\': \'string\',
                            \'SubnetAvailabilityZone\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SubnetGroup** *(dict) --* 
        
              Represents the output of a *CreateSubnetGroup* operation.
        
              - **SubnetGroupName** *(string) --* 
        
                The name of the subnet group.
        
              - **Description** *(string) --* 
        
                The description of the subnet group.
        
              - **VpcId** *(string) --* 
        
                The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.
        
              - **Subnets** *(list) --* 
        
                A list of subnets associated with the subnet group. 
        
                - *(dict) --* 
        
                  Represents the subnet associated with a DAX cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.
        
                  - **SubnetIdentifier** *(string) --* 
        
                    The system-assigned identifier for the subnet.
        
                  - **SubnetAvailabilityZone** *(string) --* 
        
                    The Availability Zone (AZ) for subnet subnet.
        
        """
        pass

    def decrease_replication_factor(self, ClusterName: str, NewReplicationFactor: int, AvailabilityZones: List = None, NodeIdsToRemove: List = None) -> Dict:
        """
        
        .. note::
        
          You cannot use ``DecreaseReplicationFactor`` to remove the last node in a DAX cluster. If you need to do this, use ``DeleteCluster`` instead.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DecreaseReplicationFactor>`_
        
        **Request Syntax** 
        ::
        
          response = client.decrease_replication_factor(
              ClusterName=\'string\',
              NewReplicationFactor=123,
              AvailabilityZones=[
                  \'string\',
              ],
              NodeIdsToRemove=[
                  \'string\',
              ]
          )
        :type ClusterName: string
        :param ClusterName: **[REQUIRED]** 
        
          The name of the DAX cluster from which you want to remove nodes.
        
        :type NewReplicationFactor: integer
        :param NewReplicationFactor: **[REQUIRED]** 
        
          The new number of nodes for the DAX cluster.
        
        :type AvailabilityZones: list
        :param AvailabilityZones: 
        
          The Availability Zone(s) from which to remove nodes.
        
          - *(string) --* 
        
        :type NodeIdsToRemove: list
        :param NodeIdsToRemove: 
        
          The unique identifiers of the nodes to be removed from the cluster.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterName\': \'string\',
                    \'Description\': \'string\',
                    \'ClusterArn\': \'string\',
                    \'TotalNodes\': 123,
                    \'ActiveNodes\': 123,
                    \'NodeType\': \'string\',
                    \'Status\': \'string\',
                    \'ClusterDiscoveryEndpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'NodeIdsToRemove\': [
                        \'string\',
                    ],
                    \'Nodes\': [
                        {
                            \'NodeId\': \'string\',
                            \'Endpoint\': {
                                \'Address\': \'string\',
                                \'Port\': 123
                            },
                            \'NodeCreateTime\': datetime(2015, 1, 1),
                            \'AvailabilityZone\': \'string\',
                            \'NodeStatus\': \'string\',
                            \'ParameterGroupStatus\': \'string\'
                        },
                    ],
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'NotificationConfiguration\': {
                        \'TopicArn\': \'string\',
                        \'TopicStatus\': \'string\'
                    },
                    \'SubnetGroup\': \'string\',
                    \'SecurityGroups\': [
                        {
                            \'SecurityGroupIdentifier\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'IamRoleArn\': \'string\',
                    \'ParameterGroup\': {
                        \'ParameterGroupName\': \'string\',
                        \'ParameterApplyStatus\': \'string\',
                        \'NodeIdsToReboot\': [
                            \'string\',
                        ]
                    },
                    \'SSEDescription\': {
                        \'Status\': \'ENABLING\'|\'ENABLED\'|\'DISABLING\'|\'DISABLED\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              A description of the DAX cluster, after you have decreased its replication factor.
        
              - **ClusterName** *(string) --* 
        
                The name of the DAX cluster.
        
              - **Description** *(string) --* 
        
                The description of the cluster.
        
              - **ClusterArn** *(string) --* 
        
                The Amazon Resource Name (ARN) that uniquely identifies the cluster. 
        
              - **TotalNodes** *(integer) --* 
        
                The total number of nodes in the cluster.
        
              - **ActiveNodes** *(integer) --* 
        
                The number of nodes in the cluster that are active (i.e., capable of serving requests).
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)
        
              - **Status** *(string) --* 
        
                The current status of the cluster.
        
              - **ClusterDiscoveryEndpoint** *(dict) --* 
        
                The configuration endpoint for this DAX cluster, consisting of a DNS name and a port number. Client applications can specify this endpoint, rather than an individual node endpoint, and allow the DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
        
                - **Address** *(string) --* 
        
                  The DNS hostname of the endpoint.
        
                - **Port** *(integer) --* 
        
                  The port number that applications should use to connect to the endpoint.
        
              - **NodeIdsToRemove** *(list) --* 
        
                A list of nodes to be removed from the cluster.
        
                - *(string) --* 
            
              - **Nodes** *(list) --* 
        
                A list of nodes that are currently in the cluster.
        
                - *(dict) --* 
        
                  Represents an individual node within a DAX cluster.
        
                  - **NodeId** *(string) --* 
        
                    A system-generated identifier for the node.
        
                  - **Endpoint** *(dict) --* 
        
                    The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
        
                    - **Address** *(string) --* 
        
                      The DNS hostname of the endpoint.
        
                    - **Port** *(integer) --* 
        
                      The port number that applications should use to connect to the endpoint.
        
                  - **NodeCreateTime** *(datetime) --* 
        
                    The date and time (in UNIX epoch format) when the node was launched.
        
                  - **AvailabilityZone** *(string) --* 
        
                    The Availability Zone (AZ) in which the node has been deployed.
        
                  - **NodeStatus** *(string) --* 
        
                    The current status of the node. For example: ``available`` .
        
                  - **ParameterGroupStatus** *(string) --* 
        
                    The status of the parameter group associated with this node. For example, ``in-sync`` .
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                A range of time when maintenance of DAX cluster software will be performed. For example: ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.
        
              - **NotificationConfiguration** *(dict) --* 
        
                Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).
        
                - **TopicArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that identifies the topic. 
        
                - **TopicStatus** *(string) --* 
        
                  The current state of the topic.
        
              - **SubnetGroup** *(string) --* 
        
                The subnet group where the DAX cluster is running.
        
              - **SecurityGroups** *(list) --* 
        
                A list of security groups, and the status of each, for the nodes in the cluster.
        
                - *(dict) --* 
        
                  An individual VPC security group and its status.
        
                  - **SecurityGroupIdentifier** *(string) --* 
        
                    The unique ID for this security group.
        
                  - **Status** *(string) --* 
        
                    The status of this security group.
        
              - **IamRoleArn** *(string) --* 
        
                A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.
        
              - **ParameterGroup** *(dict) --* 
        
                The parameter group being used by nodes in the cluster.
        
                - **ParameterGroupName** *(string) --* 
        
                  The name of the parameter group.
        
                - **ParameterApplyStatus** *(string) --* 
        
                  The status of parameter updates. 
        
                - **NodeIdsToReboot** *(list) --* 
        
                  The node IDs of one or more nodes to be rebooted.
        
                  - *(string) --* 
              
              - **SSEDescription** *(dict) --* 
        
                The description of the server-side encryption status on the specified DAX cluster.
        
                - **Status** *(string) --* 
        
                  The current state of server-side encryption:
        
                  * ``ENABLING`` - Server-side encryption is being enabled. 
                   
                  * ``ENABLED`` - Server-side encryption is enabled. 
                   
                  * ``DISABLING`` - Server-side encryption is being disabled. 
                   
                  * ``DISABLED`` - Server-side encryption is disabled. 
                   
        """
        pass

    def delete_cluster(self, ClusterName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DeleteCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_cluster(
              ClusterName=\'string\'
          )
        :type ClusterName: string
        :param ClusterName: **[REQUIRED]** 
        
          The name of the cluster to be deleted.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterName\': \'string\',
                    \'Description\': \'string\',
                    \'ClusterArn\': \'string\',
                    \'TotalNodes\': 123,
                    \'ActiveNodes\': 123,
                    \'NodeType\': \'string\',
                    \'Status\': \'string\',
                    \'ClusterDiscoveryEndpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'NodeIdsToRemove\': [
                        \'string\',
                    ],
                    \'Nodes\': [
                        {
                            \'NodeId\': \'string\',
                            \'Endpoint\': {
                                \'Address\': \'string\',
                                \'Port\': 123
                            },
                            \'NodeCreateTime\': datetime(2015, 1, 1),
                            \'AvailabilityZone\': \'string\',
                            \'NodeStatus\': \'string\',
                            \'ParameterGroupStatus\': \'string\'
                        },
                    ],
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'NotificationConfiguration\': {
                        \'TopicArn\': \'string\',
                        \'TopicStatus\': \'string\'
                    },
                    \'SubnetGroup\': \'string\',
                    \'SecurityGroups\': [
                        {
                            \'SecurityGroupIdentifier\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'IamRoleArn\': \'string\',
                    \'ParameterGroup\': {
                        \'ParameterGroupName\': \'string\',
                        \'ParameterApplyStatus\': \'string\',
                        \'NodeIdsToReboot\': [
                            \'string\',
                        ]
                    },
                    \'SSEDescription\': {
                        \'Status\': \'ENABLING\'|\'ENABLED\'|\'DISABLING\'|\'DISABLED\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              A description of the DAX cluster that is being deleted.
        
              - **ClusterName** *(string) --* 
        
                The name of the DAX cluster.
        
              - **Description** *(string) --* 
        
                The description of the cluster.
        
              - **ClusterArn** *(string) --* 
        
                The Amazon Resource Name (ARN) that uniquely identifies the cluster. 
        
              - **TotalNodes** *(integer) --* 
        
                The total number of nodes in the cluster.
        
              - **ActiveNodes** *(integer) --* 
        
                The number of nodes in the cluster that are active (i.e., capable of serving requests).
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)
        
              - **Status** *(string) --* 
        
                The current status of the cluster.
        
              - **ClusterDiscoveryEndpoint** *(dict) --* 
        
                The configuration endpoint for this DAX cluster, consisting of a DNS name and a port number. Client applications can specify this endpoint, rather than an individual node endpoint, and allow the DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
        
                - **Address** *(string) --* 
        
                  The DNS hostname of the endpoint.
        
                - **Port** *(integer) --* 
        
                  The port number that applications should use to connect to the endpoint.
        
              - **NodeIdsToRemove** *(list) --* 
        
                A list of nodes to be removed from the cluster.
        
                - *(string) --* 
            
              - **Nodes** *(list) --* 
        
                A list of nodes that are currently in the cluster.
        
                - *(dict) --* 
        
                  Represents an individual node within a DAX cluster.
        
                  - **NodeId** *(string) --* 
        
                    A system-generated identifier for the node.
        
                  - **Endpoint** *(dict) --* 
        
                    The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
        
                    - **Address** *(string) --* 
        
                      The DNS hostname of the endpoint.
        
                    - **Port** *(integer) --* 
        
                      The port number that applications should use to connect to the endpoint.
        
                  - **NodeCreateTime** *(datetime) --* 
        
                    The date and time (in UNIX epoch format) when the node was launched.
        
                  - **AvailabilityZone** *(string) --* 
        
                    The Availability Zone (AZ) in which the node has been deployed.
        
                  - **NodeStatus** *(string) --* 
        
                    The current status of the node. For example: ``available`` .
        
                  - **ParameterGroupStatus** *(string) --* 
        
                    The status of the parameter group associated with this node. For example, ``in-sync`` .
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                A range of time when maintenance of DAX cluster software will be performed. For example: ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.
        
              - **NotificationConfiguration** *(dict) --* 
        
                Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).
        
                - **TopicArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that identifies the topic. 
        
                - **TopicStatus** *(string) --* 
        
                  The current state of the topic.
        
              - **SubnetGroup** *(string) --* 
        
                The subnet group where the DAX cluster is running.
        
              - **SecurityGroups** *(list) --* 
        
                A list of security groups, and the status of each, for the nodes in the cluster.
        
                - *(dict) --* 
        
                  An individual VPC security group and its status.
        
                  - **SecurityGroupIdentifier** *(string) --* 
        
                    The unique ID for this security group.
        
                  - **Status** *(string) --* 
        
                    The status of this security group.
        
              - **IamRoleArn** *(string) --* 
        
                A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.
        
              - **ParameterGroup** *(dict) --* 
        
                The parameter group being used by nodes in the cluster.
        
                - **ParameterGroupName** *(string) --* 
        
                  The name of the parameter group.
        
                - **ParameterApplyStatus** *(string) --* 
        
                  The status of parameter updates. 
        
                - **NodeIdsToReboot** *(list) --* 
        
                  The node IDs of one or more nodes to be rebooted.
        
                  - *(string) --* 
              
              - **SSEDescription** *(dict) --* 
        
                The description of the server-side encryption status on the specified DAX cluster.
        
                - **Status** *(string) --* 
        
                  The current state of server-side encryption:
        
                  * ``ENABLING`` - Server-side encryption is being enabled. 
                   
                  * ``ENABLED`` - Server-side encryption is enabled. 
                   
                  * ``DISABLING`` - Server-side encryption is being disabled. 
                   
                  * ``DISABLED`` - Server-side encryption is disabled. 
                   
        """
        pass

    def delete_parameter_group(self, ParameterGroupName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DeleteParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_parameter_group(
              ParameterGroupName=\'string\'
          )
        :type ParameterGroupName: string
        :param ParameterGroupName: **[REQUIRED]** 
        
          The name of the parameter group to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeletionMessage\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DeletionMessage** *(string) --* 
        
              A user-specified message for this action (i.e., a reason for deleting the parameter group).
        
        """
        pass

    def delete_subnet_group(self, SubnetGroupName: str) -> Dict:
        """
        
        .. note::
        
          You cannot delete a subnet group if it is associated with any DAX clusters.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DeleteSubnetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_subnet_group(
              SubnetGroupName=\'string\'
          )
        :type SubnetGroupName: string
        :param SubnetGroupName: **[REQUIRED]** 
        
          The name of the subnet group to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeletionMessage\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DeletionMessage** *(string) --* 
        
              A user-specified message for this action (i.e., a reason for deleting the subnet group).
        
        """
        pass

    def describe_clusters(self, ClusterNames: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        If the cluster is in the CREATING state, only cluster level information will be displayed until all of the nodes are successfully provisioned.
        
        If the cluster is in the DELETING state, only cluster level information will be displayed.
        
        If nodes are currently being added to the DAX cluster, node endpoint information and creation time for the additional nodes will not be displayed until they are completely provisioned. When the DAX cluster state is *available* , the cluster is ready for use.
        
        If nodes are currently being removed from the DAX cluster, no endpoint information for the removed nodes is displayed.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DescribeClusters>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_clusters(
              ClusterNames=[
                  \'string\',
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
        :type ClusterNames: list
        :param ClusterNames: 
        
          The names of the DAX clusters being described.
        
          - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved.
        
          The value for ``MaxResults`` must be between 20 and 100.
        
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'Clusters\': [
                    {
                        \'ClusterName\': \'string\',
                        \'Description\': \'string\',
                        \'ClusterArn\': \'string\',
                        \'TotalNodes\': 123,
                        \'ActiveNodes\': 123,
                        \'NodeType\': \'string\',
                        \'Status\': \'string\',
                        \'ClusterDiscoveryEndpoint\': {
                            \'Address\': \'string\',
                            \'Port\': 123
                        },
                        \'NodeIdsToRemove\': [
                            \'string\',
                        ],
                        \'Nodes\': [
                            {
                                \'NodeId\': \'string\',
                                \'Endpoint\': {
                                    \'Address\': \'string\',
                                    \'Port\': 123
                                },
                                \'NodeCreateTime\': datetime(2015, 1, 1),
                                \'AvailabilityZone\': \'string\',
                                \'NodeStatus\': \'string\',
                                \'ParameterGroupStatus\': \'string\'
                            },
                        ],
                        \'PreferredMaintenanceWindow\': \'string\',
                        \'NotificationConfiguration\': {
                            \'TopicArn\': \'string\',
                            \'TopicStatus\': \'string\'
                        },
                        \'SubnetGroup\': \'string\',
                        \'SecurityGroups\': [
                            {
                                \'SecurityGroupIdentifier\': \'string\',
                                \'Status\': \'string\'
                            },
                        ],
                        \'IamRoleArn\': \'string\',
                        \'ParameterGroup\': {
                            \'ParameterGroupName\': \'string\',
                            \'ParameterApplyStatus\': \'string\',
                            \'NodeIdsToReboot\': [
                                \'string\',
                            ]
                        },
                        \'SSEDescription\': {
                            \'Status\': \'ENABLING\'|\'ENABLED\'|\'DISABLING\'|\'DISABLED\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* 
        
              Provides an identifier to allow retrieval of paginated results.
        
            - **Clusters** *(list) --* 
        
              The descriptions of your DAX clusters, in response to a *DescribeClusters* request.
        
              - *(dict) --* 
        
                Contains all of the attributes of a specific DAX cluster.
        
                - **ClusterName** *(string) --* 
        
                  The name of the DAX cluster.
        
                - **Description** *(string) --* 
        
                  The description of the cluster.
        
                - **ClusterArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that uniquely identifies the cluster. 
        
                - **TotalNodes** *(integer) --* 
        
                  The total number of nodes in the cluster.
        
                - **ActiveNodes** *(integer) --* 
        
                  The number of nodes in the cluster that are active (i.e., capable of serving requests).
        
                - **NodeType** *(string) --* 
        
                  The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)
        
                - **Status** *(string) --* 
        
                  The current status of the cluster.
        
                - **ClusterDiscoveryEndpoint** *(dict) --* 
        
                  The configuration endpoint for this DAX cluster, consisting of a DNS name and a port number. Client applications can specify this endpoint, rather than an individual node endpoint, and allow the DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
        
                  - **Address** *(string) --* 
        
                    The DNS hostname of the endpoint.
        
                  - **Port** *(integer) --* 
        
                    The port number that applications should use to connect to the endpoint.
        
                - **NodeIdsToRemove** *(list) --* 
        
                  A list of nodes to be removed from the cluster.
        
                  - *(string) --* 
              
                - **Nodes** *(list) --* 
        
                  A list of nodes that are currently in the cluster.
        
                  - *(dict) --* 
        
                    Represents an individual node within a DAX cluster.
        
                    - **NodeId** *(string) --* 
        
                      A system-generated identifier for the node.
        
                    - **Endpoint** *(dict) --* 
        
                      The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
        
                      - **Address** *(string) --* 
        
                        The DNS hostname of the endpoint.
        
                      - **Port** *(integer) --* 
        
                        The port number that applications should use to connect to the endpoint.
        
                    - **NodeCreateTime** *(datetime) --* 
        
                      The date and time (in UNIX epoch format) when the node was launched.
        
                    - **AvailabilityZone** *(string) --* 
        
                      The Availability Zone (AZ) in which the node has been deployed.
        
                    - **NodeStatus** *(string) --* 
        
                      The current status of the node. For example: ``available`` .
        
                    - **ParameterGroupStatus** *(string) --* 
        
                      The status of the parameter group associated with this node. For example, ``in-sync`` .
        
                - **PreferredMaintenanceWindow** *(string) --* 
        
                  A range of time when maintenance of DAX cluster software will be performed. For example: ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.
        
                - **NotificationConfiguration** *(dict) --* 
        
                  Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).
        
                  - **TopicArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) that identifies the topic. 
        
                  - **TopicStatus** *(string) --* 
        
                    The current state of the topic.
        
                - **SubnetGroup** *(string) --* 
        
                  The subnet group where the DAX cluster is running.
        
                - **SecurityGroups** *(list) --* 
        
                  A list of security groups, and the status of each, for the nodes in the cluster.
        
                  - *(dict) --* 
        
                    An individual VPC security group and its status.
        
                    - **SecurityGroupIdentifier** *(string) --* 
        
                      The unique ID for this security group.
        
                    - **Status** *(string) --* 
        
                      The status of this security group.
        
                - **IamRoleArn** *(string) --* 
        
                  A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.
        
                - **ParameterGroup** *(dict) --* 
        
                  The parameter group being used by nodes in the cluster.
        
                  - **ParameterGroupName** *(string) --* 
        
                    The name of the parameter group.
        
                  - **ParameterApplyStatus** *(string) --* 
        
                    The status of parameter updates. 
        
                  - **NodeIdsToReboot** *(list) --* 
        
                    The node IDs of one or more nodes to be rebooted.
        
                    - *(string) --* 
                
                - **SSEDescription** *(dict) --* 
        
                  The description of the server-side encryption status on the specified DAX cluster.
        
                  - **Status** *(string) --* 
        
                    The current state of server-side encryption:
        
                    * ``ENABLING`` - Server-side encryption is being enabled. 
                     
                    * ``ENABLED`` - Server-side encryption is enabled. 
                     
                    * ``DISABLING`` - Server-side encryption is being disabled. 
                     
                    * ``DISABLED`` - Server-side encryption is disabled. 
                     
        """
        pass

    def describe_default_parameters(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DescribeDefaultParameters>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_default_parameters(
              MaxResults=123,
              NextToken=\'string\'
          )
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved.
        
          The value for ``MaxResults`` must be between 20 and 100.
        
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'Parameters\': [
                    {
                        \'ParameterName\': \'string\',
                        \'ParameterType\': \'DEFAULT\'|\'NODE_TYPE_SPECIFIC\',
                        \'ParameterValue\': \'string\',
                        \'NodeTypeSpecificValues\': [
                            {
                                \'NodeType\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'Description\': \'string\',
                        \'Source\': \'string\',
                        \'DataType\': \'string\',
                        \'AllowedValues\': \'string\',
                        \'IsModifiable\': \'TRUE\'|\'FALSE\'|\'CONDITIONAL\',
                        \'ChangeType\': \'IMMEDIATE\'|\'REQUIRES_REBOOT\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* 
        
              Provides an identifier to allow retrieval of paginated results.
        
            - **Parameters** *(list) --* 
        
              A list of parameters. Each element in the list represents one parameter.
        
              - *(dict) --* 
        
                Describes an individual setting that controls some aspect of DAX behavior.
        
                - **ParameterName** *(string) --* 
        
                  The name of the parameter.
        
                - **ParameterType** *(string) --* 
        
                  Determines whether the parameter can be applied to any nodes, or only nodes of a particular type.
        
                - **ParameterValue** *(string) --* 
        
                  The value for the parameter.
        
                - **NodeTypeSpecificValues** *(list) --* 
        
                  A list of node types, and specific parameter values for each node.
        
                  - *(dict) --* 
        
                    Represents a parameter value that is applicable to a particular node type.
        
                    - **NodeType** *(string) --* 
        
                      A node type to which the parameter value applies.
        
                    - **Value** *(string) --* 
        
                      The parameter value for this node type.
        
                - **Description** *(string) --* 
        
                  A description of the parameter
        
                - **Source** *(string) --* 
        
                  How the parameter is defined. For example, ``system`` denotes a system-defined parameter.
        
                - **DataType** *(string) --* 
        
                  The data type of the parameter. For example, ``integer`` :
        
                - **AllowedValues** *(string) --* 
        
                  A range of values within which the parameter can be set.
        
                - **IsModifiable** *(string) --* 
        
                  Whether the customer is allowed to modify the parameter.
        
                - **ChangeType** *(string) --* 
        
                  The conditions under which changes to this parameter can be applied. For example, ``requires-reboot`` indicates that a new value for this parameter will only take effect if a node is rebooted.
        
        """
        pass

    def describe_events(self, SourceName: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        By default, only the events occurring within the last hour are returned; however, you can retrieve up to 14 days\' worth of events if necessary.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DescribeEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_events(
              SourceName=\'string\',
              SourceType=\'CLUSTER\'|\'PARAMETER_GROUP\'|\'SUBNET_GROUP\',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Duration=123,
              MaxResults=123,
              NextToken=\'string\'
          )
        :type SourceName: string
        :param SourceName: 
        
          The identifier of the event source for which events will be returned. If not specified, then all sources are included in the response.
        
        :type SourceType: string
        :param SourceType: 
        
          The event source to retrieve events for. If no value is specified, all events are returned.
        
        :type StartTime: datetime
        :param StartTime: 
        
          The beginning of the time interval to retrieve events for, specified in ISO 8601 format.
        
        :type EndTime: datetime
        :param EndTime: 
        
          The end of the time interval for which to retrieve events, specified in ISO 8601 format.
        
        :type Duration: integer
        :param Duration: 
        
          The number of minutes\' worth of events to retrieve.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved.
        
          The value for ``MaxResults`` must be between 20 and 100.
        
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'Events\': [
                    {
                        \'SourceName\': \'string\',
                        \'SourceType\': \'CLUSTER\'|\'PARAMETER_GROUP\'|\'SUBNET_GROUP\',
                        \'Message\': \'string\',
                        \'Date\': datetime(2015, 1, 1)
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* 
        
              Provides an identifier to allow retrieval of paginated results.
        
            - **Events** *(list) --* 
        
              An array of events. Each element in the array represents one event.
        
              - *(dict) --* 
        
                Represents a single occurrence of something interesting within the system. Some examples of events are creating a DAX cluster, adding or removing a node, or rebooting a node.
        
                - **SourceName** *(string) --* 
        
                  The source of the event. For example, if the event occurred at the node level, the source would be the node ID.
        
                - **SourceType** *(string) --* 
        
                  Specifies the origin of this event - a cluster, a parameter group, a node ID, etc.
        
                - **Message** *(string) --* 
        
                  A user-defined message associated with the event.
        
                - **Date** *(datetime) --* 
        
                  The date and time when the event occurred.
        
        """
        pass

    def describe_parameter_groups(self, ParameterGroupNames: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DescribeParameterGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_parameter_groups(
              ParameterGroupNames=[
                  \'string\',
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
        :type ParameterGroupNames: list
        :param ParameterGroupNames: 
        
          The names of the parameter groups.
        
          - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved.
        
          The value for ``MaxResults`` must be between 20 and 100.
        
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'ParameterGroups\': [
                    {
                        \'ParameterGroupName\': \'string\',
                        \'Description\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* 
        
              Provides an identifier to allow retrieval of paginated results.
        
            - **ParameterGroups** *(list) --* 
        
              An array of parameter groups. Each element in the array represents one parameter group.
        
              - *(dict) --* 
        
                A named set of parameters that are applied to all of the nodes in a DAX cluster.
        
                - **ParameterGroupName** *(string) --* 
        
                  The name of the parameter group.
        
                - **Description** *(string) --* 
        
                  A description of the parameter group.
        
        """
        pass

    def describe_parameters(self, ParameterGroupName: str, Source: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DescribeParameters>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_parameters(
              ParameterGroupName=\'string\',
              Source=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type ParameterGroupName: string
        :param ParameterGroupName: **[REQUIRED]** 
        
          The name of the parameter group.
        
        :type Source: string
        :param Source: 
        
          How the parameter is defined. For example, ``system`` denotes a system-defined parameter.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved.
        
          The value for ``MaxResults`` must be between 20 and 100.
        
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'Parameters\': [
                    {
                        \'ParameterName\': \'string\',
                        \'ParameterType\': \'DEFAULT\'|\'NODE_TYPE_SPECIFIC\',
                        \'ParameterValue\': \'string\',
                        \'NodeTypeSpecificValues\': [
                            {
                                \'NodeType\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'Description\': \'string\',
                        \'Source\': \'string\',
                        \'DataType\': \'string\',
                        \'AllowedValues\': \'string\',
                        \'IsModifiable\': \'TRUE\'|\'FALSE\'|\'CONDITIONAL\',
                        \'ChangeType\': \'IMMEDIATE\'|\'REQUIRES_REBOOT\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* 
        
              Provides an identifier to allow retrieval of paginated results.
        
            - **Parameters** *(list) --* 
        
              A list of parameters within a parameter group. Each element in the list represents one parameter.
        
              - *(dict) --* 
        
                Describes an individual setting that controls some aspect of DAX behavior.
        
                - **ParameterName** *(string) --* 
        
                  The name of the parameter.
        
                - **ParameterType** *(string) --* 
        
                  Determines whether the parameter can be applied to any nodes, or only nodes of a particular type.
        
                - **ParameterValue** *(string) --* 
        
                  The value for the parameter.
        
                - **NodeTypeSpecificValues** *(list) --* 
        
                  A list of node types, and specific parameter values for each node.
        
                  - *(dict) --* 
        
                    Represents a parameter value that is applicable to a particular node type.
        
                    - **NodeType** *(string) --* 
        
                      A node type to which the parameter value applies.
        
                    - **Value** *(string) --* 
        
                      The parameter value for this node type.
        
                - **Description** *(string) --* 
        
                  A description of the parameter
        
                - **Source** *(string) --* 
        
                  How the parameter is defined. For example, ``system`` denotes a system-defined parameter.
        
                - **DataType** *(string) --* 
        
                  The data type of the parameter. For example, ``integer`` :
        
                - **AllowedValues** *(string) --* 
        
                  A range of values within which the parameter can be set.
        
                - **IsModifiable** *(string) --* 
        
                  Whether the customer is allowed to modify the parameter.
        
                - **ChangeType** *(string) --* 
        
                  The conditions under which changes to this parameter can be applied. For example, ``requires-reboot`` indicates that a new value for this parameter will only take effect if a node is rebooted.
        
        """
        pass

    def describe_subnet_groups(self, SubnetGroupNames: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DescribeSubnetGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_subnet_groups(
              SubnetGroupNames=[
                  \'string\',
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
        :type SubnetGroupNames: list
        :param SubnetGroupNames: 
        
          The name of the subnet group.
        
          - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to include in the response. If more results exist than the specified ``MaxResults`` value, a token is included in the response so that the remaining results can be retrieved.
        
          The value for ``MaxResults`` must be between 20 and 100.
        
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by ``MaxResults`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'SubnetGroups\': [
                    {
                        \'SubnetGroupName\': \'string\',
                        \'Description\': \'string\',
                        \'VpcId\': \'string\',
                        \'Subnets\': [
                            {
                                \'SubnetIdentifier\': \'string\',
                                \'SubnetAvailabilityZone\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* 
        
              Provides an identifier to allow retrieval of paginated results.
        
            - **SubnetGroups** *(list) --* 
        
              An array of subnet groups. Each element in the array represents a single subnet group.
        
              - *(dict) --* 
        
                Represents the output of one of the following actions:
        
                * *CreateSubnetGroup*   
                 
                * *ModifySubnetGroup*   
                 
                - **SubnetGroupName** *(string) --* 
        
                  The name of the subnet group.
        
                - **Description** *(string) --* 
        
                  The description of the subnet group.
        
                - **VpcId** *(string) --* 
        
                  The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.
        
                - **Subnets** *(list) --* 
        
                  A list of subnets associated with the subnet group. 
        
                  - *(dict) --* 
        
                    Represents the subnet associated with a DAX cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.
        
                    - **SubnetIdentifier** *(string) --* 
        
                      The system-assigned identifier for the subnet.
        
                    - **SubnetAvailabilityZone** *(string) --* 
        
                      The Availability Zone (AZ) for subnet subnet.
        
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        """
        
        :type ClientMethod: string
        :param ClientMethod: The client method to presign for
        
        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.
        
        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
        
        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method\'s model.
        
        :returns: The presigned url
        """
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        
        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.
        
        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def increase_replication_factor(self, ClusterName: str, NewReplicationFactor: int, AvailabilityZones: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/IncreaseReplicationFactor>`_
        
        **Request Syntax** 
        ::
        
          response = client.increase_replication_factor(
              ClusterName=\'string\',
              NewReplicationFactor=123,
              AvailabilityZones=[
                  \'string\',
              ]
          )
        :type ClusterName: string
        :param ClusterName: **[REQUIRED]** 
        
          The name of the DAX cluster that will receive additional nodes.
        
        :type NewReplicationFactor: integer
        :param NewReplicationFactor: **[REQUIRED]** 
        
          The new number of nodes for the DAX cluster.
        
        :type AvailabilityZones: list
        :param AvailabilityZones: 
        
          The Availability Zones (AZs) in which the cluster nodes will be created. All nodes belonging to the cluster are placed in these Availability Zones. Use this parameter if you want to distribute the nodes across multiple AZs.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterName\': \'string\',
                    \'Description\': \'string\',
                    \'ClusterArn\': \'string\',
                    \'TotalNodes\': 123,
                    \'ActiveNodes\': 123,
                    \'NodeType\': \'string\',
                    \'Status\': \'string\',
                    \'ClusterDiscoveryEndpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'NodeIdsToRemove\': [
                        \'string\',
                    ],
                    \'Nodes\': [
                        {
                            \'NodeId\': \'string\',
                            \'Endpoint\': {
                                \'Address\': \'string\',
                                \'Port\': 123
                            },
                            \'NodeCreateTime\': datetime(2015, 1, 1),
                            \'AvailabilityZone\': \'string\',
                            \'NodeStatus\': \'string\',
                            \'ParameterGroupStatus\': \'string\'
                        },
                    ],
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'NotificationConfiguration\': {
                        \'TopicArn\': \'string\',
                        \'TopicStatus\': \'string\'
                    },
                    \'SubnetGroup\': \'string\',
                    \'SecurityGroups\': [
                        {
                            \'SecurityGroupIdentifier\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'IamRoleArn\': \'string\',
                    \'ParameterGroup\': {
                        \'ParameterGroupName\': \'string\',
                        \'ParameterApplyStatus\': \'string\',
                        \'NodeIdsToReboot\': [
                            \'string\',
                        ]
                    },
                    \'SSEDescription\': {
                        \'Status\': \'ENABLING\'|\'ENABLED\'|\'DISABLING\'|\'DISABLED\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              A description of the DAX cluster. with its new replication factor.
        
              - **ClusterName** *(string) --* 
        
                The name of the DAX cluster.
        
              - **Description** *(string) --* 
        
                The description of the cluster.
        
              - **ClusterArn** *(string) --* 
        
                The Amazon Resource Name (ARN) that uniquely identifies the cluster. 
        
              - **TotalNodes** *(integer) --* 
        
                The total number of nodes in the cluster.
        
              - **ActiveNodes** *(integer) --* 
        
                The number of nodes in the cluster that are active (i.e., capable of serving requests).
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)
        
              - **Status** *(string) --* 
        
                The current status of the cluster.
        
              - **ClusterDiscoveryEndpoint** *(dict) --* 
        
                The configuration endpoint for this DAX cluster, consisting of a DNS name and a port number. Client applications can specify this endpoint, rather than an individual node endpoint, and allow the DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
        
                - **Address** *(string) --* 
        
                  The DNS hostname of the endpoint.
        
                - **Port** *(integer) --* 
        
                  The port number that applications should use to connect to the endpoint.
        
              - **NodeIdsToRemove** *(list) --* 
        
                A list of nodes to be removed from the cluster.
        
                - *(string) --* 
            
              - **Nodes** *(list) --* 
        
                A list of nodes that are currently in the cluster.
        
                - *(dict) --* 
        
                  Represents an individual node within a DAX cluster.
        
                  - **NodeId** *(string) --* 
        
                    A system-generated identifier for the node.
        
                  - **Endpoint** *(dict) --* 
        
                    The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
        
                    - **Address** *(string) --* 
        
                      The DNS hostname of the endpoint.
        
                    - **Port** *(integer) --* 
        
                      The port number that applications should use to connect to the endpoint.
        
                  - **NodeCreateTime** *(datetime) --* 
        
                    The date and time (in UNIX epoch format) when the node was launched.
        
                  - **AvailabilityZone** *(string) --* 
        
                    The Availability Zone (AZ) in which the node has been deployed.
        
                  - **NodeStatus** *(string) --* 
        
                    The current status of the node. For example: ``available`` .
        
                  - **ParameterGroupStatus** *(string) --* 
        
                    The status of the parameter group associated with this node. For example, ``in-sync`` .
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                A range of time when maintenance of DAX cluster software will be performed. For example: ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.
        
              - **NotificationConfiguration** *(dict) --* 
        
                Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).
        
                - **TopicArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that identifies the topic. 
        
                - **TopicStatus** *(string) --* 
        
                  The current state of the topic.
        
              - **SubnetGroup** *(string) --* 
        
                The subnet group where the DAX cluster is running.
        
              - **SecurityGroups** *(list) --* 
        
                A list of security groups, and the status of each, for the nodes in the cluster.
        
                - *(dict) --* 
        
                  An individual VPC security group and its status.
        
                  - **SecurityGroupIdentifier** *(string) --* 
        
                    The unique ID for this security group.
        
                  - **Status** *(string) --* 
        
                    The status of this security group.
        
              - **IamRoleArn** *(string) --* 
        
                A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.
        
              - **ParameterGroup** *(dict) --* 
        
                The parameter group being used by nodes in the cluster.
        
                - **ParameterGroupName** *(string) --* 
        
                  The name of the parameter group.
        
                - **ParameterApplyStatus** *(string) --* 
        
                  The status of parameter updates. 
        
                - **NodeIdsToReboot** *(list) --* 
        
                  The node IDs of one or more nodes to be rebooted.
        
                  - *(string) --* 
              
              - **SSEDescription** *(dict) --* 
        
                The description of the server-side encryption status on the specified DAX cluster.
        
                - **Status** *(string) --* 
        
                  The current state of server-side encryption:
        
                  * ``ENABLING`` - Server-side encryption is being enabled. 
                   
                  * ``ENABLED`` - Server-side encryption is enabled. 
                   
                  * ``DISABLING`` - Server-side encryption is being disabled. 
                   
                  * ``DISABLED`` - Server-side encryption is disabled. 
                   
        """
        pass

    def list_tags(self, ResourceName: str, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/ListTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags(
              ResourceName=\'string\',
              NextToken=\'string\'
          )
        :type ResourceName: string
        :param ResourceName: **[REQUIRED]** 
        
          The name of the DAX resource to which the tags belong.
        
        :type NextToken: string
        :param NextToken: 
        
          An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Tags** *(list) --* 
        
              A list of tags currently associated with the DAX cluster.
        
              - *(dict) --* 
        
                A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single DAX cluster.
        
                AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix ``user:`` .
        
                You cannot backdate the application of a tag.
        
                - **Key** *(string) --* 
        
                  The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.
        
                - **Value** *(string) --* 
        
                  The value of the tag. Tag values are case-sensitive and can be null. 
        
            - **NextToken** *(string) --* 
        
              If this value is present, there are additional results to be displayed. To retrieve them, call ``ListTags`` again, with ``NextToken`` set to this value.
        
        """
        pass

    def reboot_node(self, ClusterName: str, NodeId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/RebootNode>`_
        
        **Request Syntax** 
        ::
        
          response = client.reboot_node(
              ClusterName=\'string\',
              NodeId=\'string\'
          )
        :type ClusterName: string
        :param ClusterName: **[REQUIRED]** 
        
          The name of the DAX cluster containing the node to be rebooted.
        
        :type NodeId: string
        :param NodeId: **[REQUIRED]** 
        
          The system-assigned ID of the node to be rebooted.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterName\': \'string\',
                    \'Description\': \'string\',
                    \'ClusterArn\': \'string\',
                    \'TotalNodes\': 123,
                    \'ActiveNodes\': 123,
                    \'NodeType\': \'string\',
                    \'Status\': \'string\',
                    \'ClusterDiscoveryEndpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'NodeIdsToRemove\': [
                        \'string\',
                    ],
                    \'Nodes\': [
                        {
                            \'NodeId\': \'string\',
                            \'Endpoint\': {
                                \'Address\': \'string\',
                                \'Port\': 123
                            },
                            \'NodeCreateTime\': datetime(2015, 1, 1),
                            \'AvailabilityZone\': \'string\',
                            \'NodeStatus\': \'string\',
                            \'ParameterGroupStatus\': \'string\'
                        },
                    ],
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'NotificationConfiguration\': {
                        \'TopicArn\': \'string\',
                        \'TopicStatus\': \'string\'
                    },
                    \'SubnetGroup\': \'string\',
                    \'SecurityGroups\': [
                        {
                            \'SecurityGroupIdentifier\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'IamRoleArn\': \'string\',
                    \'ParameterGroup\': {
                        \'ParameterGroupName\': \'string\',
                        \'ParameterApplyStatus\': \'string\',
                        \'NodeIdsToReboot\': [
                            \'string\',
                        ]
                    },
                    \'SSEDescription\': {
                        \'Status\': \'ENABLING\'|\'ENABLED\'|\'DISABLING\'|\'DISABLED\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              A description of the DAX cluster after a node has been rebooted.
        
              - **ClusterName** *(string) --* 
        
                The name of the DAX cluster.
        
              - **Description** *(string) --* 
        
                The description of the cluster.
        
              - **ClusterArn** *(string) --* 
        
                The Amazon Resource Name (ARN) that uniquely identifies the cluster. 
        
              - **TotalNodes** *(integer) --* 
        
                The total number of nodes in the cluster.
        
              - **ActiveNodes** *(integer) --* 
        
                The number of nodes in the cluster that are active (i.e., capable of serving requests).
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)
        
              - **Status** *(string) --* 
        
                The current status of the cluster.
        
              - **ClusterDiscoveryEndpoint** *(dict) --* 
        
                The configuration endpoint for this DAX cluster, consisting of a DNS name and a port number. Client applications can specify this endpoint, rather than an individual node endpoint, and allow the DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
        
                - **Address** *(string) --* 
        
                  The DNS hostname of the endpoint.
        
                - **Port** *(integer) --* 
        
                  The port number that applications should use to connect to the endpoint.
        
              - **NodeIdsToRemove** *(list) --* 
        
                A list of nodes to be removed from the cluster.
        
                - *(string) --* 
            
              - **Nodes** *(list) --* 
        
                A list of nodes that are currently in the cluster.
        
                - *(dict) --* 
        
                  Represents an individual node within a DAX cluster.
        
                  - **NodeId** *(string) --* 
        
                    A system-generated identifier for the node.
        
                  - **Endpoint** *(dict) --* 
        
                    The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
        
                    - **Address** *(string) --* 
        
                      The DNS hostname of the endpoint.
        
                    - **Port** *(integer) --* 
        
                      The port number that applications should use to connect to the endpoint.
        
                  - **NodeCreateTime** *(datetime) --* 
        
                    The date and time (in UNIX epoch format) when the node was launched.
        
                  - **AvailabilityZone** *(string) --* 
        
                    The Availability Zone (AZ) in which the node has been deployed.
        
                  - **NodeStatus** *(string) --* 
        
                    The current status of the node. For example: ``available`` .
        
                  - **ParameterGroupStatus** *(string) --* 
        
                    The status of the parameter group associated with this node. For example, ``in-sync`` .
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                A range of time when maintenance of DAX cluster software will be performed. For example: ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.
        
              - **NotificationConfiguration** *(dict) --* 
        
                Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).
        
                - **TopicArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that identifies the topic. 
        
                - **TopicStatus** *(string) --* 
        
                  The current state of the topic.
        
              - **SubnetGroup** *(string) --* 
        
                The subnet group where the DAX cluster is running.
        
              - **SecurityGroups** *(list) --* 
        
                A list of security groups, and the status of each, for the nodes in the cluster.
        
                - *(dict) --* 
        
                  An individual VPC security group and its status.
        
                  - **SecurityGroupIdentifier** *(string) --* 
        
                    The unique ID for this security group.
        
                  - **Status** *(string) --* 
        
                    The status of this security group.
        
              - **IamRoleArn** *(string) --* 
        
                A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.
        
              - **ParameterGroup** *(dict) --* 
        
                The parameter group being used by nodes in the cluster.
        
                - **ParameterGroupName** *(string) --* 
        
                  The name of the parameter group.
        
                - **ParameterApplyStatus** *(string) --* 
        
                  The status of parameter updates. 
        
                - **NodeIdsToReboot** *(list) --* 
        
                  The node IDs of one or more nodes to be rebooted.
        
                  - *(string) --* 
              
              - **SSEDescription** *(dict) --* 
        
                The description of the server-side encryption status on the specified DAX cluster.
        
                - **Status** *(string) --* 
        
                  The current state of server-side encryption:
        
                  * ``ENABLING`` - Server-side encryption is being enabled. 
                   
                  * ``ENABLED`` - Server-side encryption is enabled. 
                   
                  * ``DISABLING`` - Server-side encryption is being disabled. 
                   
                  * ``DISABLED`` - Server-side encryption is disabled. 
                   
        """
        pass

    def tag_resource(self, ResourceName: str, Tags: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/TagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.tag_resource(
              ResourceName=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ResourceName: string
        :param ResourceName: **[REQUIRED]** 
        
          The name of the DAX resource to which tags should be added.
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          The tags to be assigned to the DAX resource. 
        
          - *(dict) --* 
        
            A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single DAX cluster.
        
            AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix ``user:`` .
        
            You cannot backdate the application of a tag.
        
            - **Key** *(string) --* 
        
              The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.
        
            - **Value** *(string) --* 
        
              The value of the tag. Tag values are case-sensitive and can be null. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Tags** *(list) --* 
        
              The list of tags that are associated with the DAX resource.
        
              - *(dict) --* 
        
                A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single DAX cluster.
        
                AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix ``user:`` .
        
                You cannot backdate the application of a tag.
        
                - **Key** *(string) --* 
        
                  The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.
        
                - **Value** *(string) --* 
        
                  The value of the tag. Tag values are case-sensitive and can be null. 
        
        """
        pass

    def untag_resource(self, ResourceName: str, TagKeys: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/UntagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.untag_resource(
              ResourceName=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type ResourceName: string
        :param ResourceName: **[REQUIRED]** 
        
          The name of the DAX resource from which the tags should be removed.
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          A list of tag keys. If the DAX cluster has any tags with these keys, then the tags are removed from the cluster.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Tags** *(list) --* 
        
              The tag keys that have been removed from the cluster.
        
              - *(dict) --* 
        
                A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single DAX cluster.
        
                AWS-assigned tag names and values are automatically assigned the ``aws:`` prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix ``user:`` .
        
                You cannot backdate the application of a tag.
        
                - **Key** *(string) --* 
        
                  The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.
        
                - **Value** *(string) --* 
        
                  The value of the tag. Tag values are case-sensitive and can be null. 
        
        """
        pass

    def update_cluster(self, ClusterName: str, Description: str = None, PreferredMaintenanceWindow: str = None, NotificationTopicArn: str = None, NotificationTopicStatus: str = None, ParameterGroupName: str = None, SecurityGroupIds: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/UpdateCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_cluster(
              ClusterName=\'string\',
              Description=\'string\',
              PreferredMaintenanceWindow=\'string\',
              NotificationTopicArn=\'string\',
              NotificationTopicStatus=\'string\',
              ParameterGroupName=\'string\',
              SecurityGroupIds=[
                  \'string\',
              ]
          )
        :type ClusterName: string
        :param ClusterName: **[REQUIRED]** 
        
          The name of the DAX cluster to be modified.
        
        :type Description: string
        :param Description: 
        
          A description of the changes being made to the cluster.
        
        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow: 
        
          A range of time when maintenance of DAX cluster software will be performed. For example: ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.
        
        :type NotificationTopicArn: string
        :param NotificationTopicArn: 
        
          The Amazon Resource Name (ARN) that identifies the topic.
        
        :type NotificationTopicStatus: string
        :param NotificationTopicStatus: 
        
          The current state of the topic.
        
        :type ParameterGroupName: string
        :param ParameterGroupName: 
        
          The name of a parameter group for this cluster.
        
        :type SecurityGroupIds: list
        :param SecurityGroupIds: 
        
          A list of user-specified security group IDs to be assigned to each node in the DAX cluster. If this parameter is not specified, DAX assigns the default VPC security group to each node.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Cluster\': {
                    \'ClusterName\': \'string\',
                    \'Description\': \'string\',
                    \'ClusterArn\': \'string\',
                    \'TotalNodes\': 123,
                    \'ActiveNodes\': 123,
                    \'NodeType\': \'string\',
                    \'Status\': \'string\',
                    \'ClusterDiscoveryEndpoint\': {
                        \'Address\': \'string\',
                        \'Port\': 123
                    },
                    \'NodeIdsToRemove\': [
                        \'string\',
                    ],
                    \'Nodes\': [
                        {
                            \'NodeId\': \'string\',
                            \'Endpoint\': {
                                \'Address\': \'string\',
                                \'Port\': 123
                            },
                            \'NodeCreateTime\': datetime(2015, 1, 1),
                            \'AvailabilityZone\': \'string\',
                            \'NodeStatus\': \'string\',
                            \'ParameterGroupStatus\': \'string\'
                        },
                    ],
                    \'PreferredMaintenanceWindow\': \'string\',
                    \'NotificationConfiguration\': {
                        \'TopicArn\': \'string\',
                        \'TopicStatus\': \'string\'
                    },
                    \'SubnetGroup\': \'string\',
                    \'SecurityGroups\': [
                        {
                            \'SecurityGroupIdentifier\': \'string\',
                            \'Status\': \'string\'
                        },
                    ],
                    \'IamRoleArn\': \'string\',
                    \'ParameterGroup\': {
                        \'ParameterGroupName\': \'string\',
                        \'ParameterApplyStatus\': \'string\',
                        \'NodeIdsToReboot\': [
                            \'string\',
                        ]
                    },
                    \'SSEDescription\': {
                        \'Status\': \'ENABLING\'|\'ENABLED\'|\'DISABLING\'|\'DISABLED\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Cluster** *(dict) --* 
        
              A description of the DAX cluster, after it has been modified.
        
              - **ClusterName** *(string) --* 
        
                The name of the DAX cluster.
        
              - **Description** *(string) --* 
        
                The description of the cluster.
        
              - **ClusterArn** *(string) --* 
        
                The Amazon Resource Name (ARN) that uniquely identifies the cluster. 
        
              - **TotalNodes** *(integer) --* 
        
                The total number of nodes in the cluster.
        
              - **ActiveNodes** *(integer) --* 
        
                The number of nodes in the cluster that are active (i.e., capable of serving requests).
        
              - **NodeType** *(string) --* 
        
                The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)
        
              - **Status** *(string) --* 
        
                The current status of the cluster.
        
              - **ClusterDiscoveryEndpoint** *(dict) --* 
        
                The configuration endpoint for this DAX cluster, consisting of a DNS name and a port number. Client applications can specify this endpoint, rather than an individual node endpoint, and allow the DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
        
                - **Address** *(string) --* 
        
                  The DNS hostname of the endpoint.
        
                - **Port** *(integer) --* 
        
                  The port number that applications should use to connect to the endpoint.
        
              - **NodeIdsToRemove** *(list) --* 
        
                A list of nodes to be removed from the cluster.
        
                - *(string) --* 
            
              - **Nodes** *(list) --* 
        
                A list of nodes that are currently in the cluster.
        
                - *(dict) --* 
        
                  Represents an individual node within a DAX cluster.
        
                  - **NodeId** *(string) --* 
        
                    A system-generated identifier for the node.
        
                  - **Endpoint** *(dict) --* 
        
                    The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.
        
                    - **Address** *(string) --* 
        
                      The DNS hostname of the endpoint.
        
                    - **Port** *(integer) --* 
        
                      The port number that applications should use to connect to the endpoint.
        
                  - **NodeCreateTime** *(datetime) --* 
        
                    The date and time (in UNIX epoch format) when the node was launched.
        
                  - **AvailabilityZone** *(string) --* 
        
                    The Availability Zone (AZ) in which the node has been deployed.
        
                  - **NodeStatus** *(string) --* 
        
                    The current status of the node. For example: ``available`` .
        
                  - **ParameterGroupStatus** *(string) --* 
        
                    The status of the parameter group associated with this node. For example, ``in-sync`` .
        
              - **PreferredMaintenanceWindow** *(string) --* 
        
                A range of time when maintenance of DAX cluster software will be performed. For example: ``sun:01:00-sun:09:00`` . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.
        
              - **NotificationConfiguration** *(dict) --* 
        
                Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).
        
                - **TopicArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that identifies the topic. 
        
                - **TopicStatus** *(string) --* 
        
                  The current state of the topic.
        
              - **SubnetGroup** *(string) --* 
        
                The subnet group where the DAX cluster is running.
        
              - **SecurityGroups** *(list) --* 
        
                A list of security groups, and the status of each, for the nodes in the cluster.
        
                - *(dict) --* 
        
                  An individual VPC security group and its status.
        
                  - **SecurityGroupIdentifier** *(string) --* 
        
                    The unique ID for this security group.
        
                  - **Status** *(string) --* 
        
                    The status of this security group.
        
              - **IamRoleArn** *(string) --* 
        
                A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.
        
              - **ParameterGroup** *(dict) --* 
        
                The parameter group being used by nodes in the cluster.
        
                - **ParameterGroupName** *(string) --* 
        
                  The name of the parameter group.
        
                - **ParameterApplyStatus** *(string) --* 
        
                  The status of parameter updates. 
        
                - **NodeIdsToReboot** *(list) --* 
        
                  The node IDs of one or more nodes to be rebooted.
        
                  - *(string) --* 
              
              - **SSEDescription** *(dict) --* 
        
                The description of the server-side encryption status on the specified DAX cluster.
        
                - **Status** *(string) --* 
        
                  The current state of server-side encryption:
        
                  * ``ENABLING`` - Server-side encryption is being enabled. 
                   
                  * ``ENABLED`` - Server-side encryption is enabled. 
                   
                  * ``DISABLING`` - Server-side encryption is being disabled. 
                   
                  * ``DISABLED`` - Server-side encryption is disabled. 
                   
        """
        pass

    def update_parameter_group(self, ParameterGroupName: str, ParameterNameValues: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/UpdateParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_parameter_group(
              ParameterGroupName=\'string\',
              ParameterNameValues=[
                  {
                      \'ParameterName\': \'string\',
                      \'ParameterValue\': \'string\'
                  },
              ]
          )
        :type ParameterGroupName: string
        :param ParameterGroupName: **[REQUIRED]** 
        
          The name of the parameter group.
        
        :type ParameterNameValues: list
        :param ParameterNameValues: **[REQUIRED]** 
        
          An array of name-value pairs for the parameters in the group. Each element in the array represents a single parameter.
        
          - *(dict) --* 
        
            An individual DAX parameter.
        
            - **ParameterName** *(string) --* 
        
              The name of the parameter.
        
            - **ParameterValue** *(string) --* 
        
              The value of the parameter.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ParameterGroup\': {
                    \'ParameterGroupName\': \'string\',
                    \'Description\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ParameterGroup** *(dict) --* 
        
              The parameter group that has been modified.
        
              - **ParameterGroupName** *(string) --* 
        
                The name of the parameter group.
        
              - **Description** *(string) --* 
        
                A description of the parameter group.
        
        """
        pass

    def update_subnet_group(self, SubnetGroupName: str, Description: str = None, SubnetIds: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/UpdateSubnetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_subnet_group(
              SubnetGroupName=\'string\',
              Description=\'string\',
              SubnetIds=[
                  \'string\',
              ]
          )
        :type SubnetGroupName: string
        :param SubnetGroupName: **[REQUIRED]** 
        
          The name of the subnet group.
        
        :type Description: string
        :param Description: 
        
          A description of the subnet group.
        
        :type SubnetIds: list
        :param SubnetIds: 
        
          A list of subnet IDs in the subnet group.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SubnetGroup\': {
                    \'SubnetGroupName\': \'string\',
                    \'Description\': \'string\',
                    \'VpcId\': \'string\',
                    \'Subnets\': [
                        {
                            \'SubnetIdentifier\': \'string\',
                            \'SubnetAvailabilityZone\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SubnetGroup** *(dict) --* 
        
              The subnet group that has been modified.
        
              - **SubnetGroupName** *(string) --* 
        
                The name of the subnet group.
        
              - **Description** *(string) --* 
        
                The description of the subnet group.
        
              - **VpcId** *(string) --* 
        
                The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.
        
              - **Subnets** *(list) --* 
        
                A list of subnets associated with the subnet group. 
        
                - *(dict) --* 
        
                  Represents the subnet associated with a DAX cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.
        
                  - **SubnetIdentifier** *(string) --* 
        
                    The system-assigned identifier for the subnet.
        
                  - **SubnetAvailabilityZone** *(string) --* 
        
                    The Availability Zone (AZ) for subnet subnet.
        
        """
        pass
