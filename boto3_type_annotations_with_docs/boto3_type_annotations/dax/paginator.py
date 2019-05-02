from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class DescribeClusters(Paginator):
    def paginate(self, ClusterNames: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DAX.Client.describe_clusters`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DescribeClusters>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClusterNames=[
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
                'Clusters': [
                    {
                        'ClusterName': 'string',
                        'Description': 'string',
                        'ClusterArn': 'string',
                        'TotalNodes': 123,
                        'ActiveNodes': 123,
                        'NodeType': 'string',
                        'Status': 'string',
                        'ClusterDiscoveryEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'NodeIdsToRemove': [
                            'string',
                        ],
                        'Nodes': [
                            {
                                'NodeId': 'string',
                                'Endpoint': {
                                    'Address': 'string',
                                    'Port': 123
                                },
                                'NodeCreateTime': datetime(2015, 1, 1),
                                'AvailabilityZone': 'string',
                                'NodeStatus': 'string',
                                'ParameterGroupStatus': 'string'
                            },
                        ],
                        'PreferredMaintenanceWindow': 'string',
                        'NotificationConfiguration': {
                            'TopicArn': 'string',
                            'TopicStatus': 'string'
                        },
                        'SubnetGroup': 'string',
                        'SecurityGroups': [
                            {
                                'SecurityGroupIdentifier': 'string',
                                'Status': 'string'
                            },
                        ],
                        'IamRoleArn': 'string',
                        'ParameterGroup': {
                            'ParameterGroupName': 'string',
                            'ParameterApplyStatus': 'string',
                            'NodeIdsToReboot': [
                                'string',
                            ]
                        },
                        'SSEDescription': {
                            'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
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
                  A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role's permissions to access DynamoDB on your behalf.
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
        :type ClusterNames: list
        :param ClusterNames:
          The names of the DAX clusters being described.
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


class DescribeDefaultParameters(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DAX.Client.describe_default_parameters`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DescribeDefaultParameters>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Parameters': [
                    {
                        'ParameterName': 'string',
                        'ParameterType': 'DEFAULT'|'NODE_TYPE_SPECIFIC',
                        'ParameterValue': 'string',
                        'NodeTypeSpecificValues': [
                            {
                                'NodeType': 'string',
                                'Value': 'string'
                            },
                        ],
                        'Description': 'string',
                        'Source': 'string',
                        'DataType': 'string',
                        'AllowedValues': 'string',
                        'IsModifiable': 'TRUE'|'FALSE'|'CONDITIONAL',
                        'ChangeType': 'IMMEDIATE'|'REQUIRES_REBOOT'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
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


class DescribeEvents(Paginator):
    def paginate(self, SourceName: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DAX.Client.describe_events`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DescribeEvents>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SourceName='string',
              SourceType='CLUSTER'|'PARAMETER_GROUP'|'SUBNET_GROUP',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Duration=123,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Events': [
                    {
                        'SourceName': 'string',
                        'SourceType': 'CLUSTER'|'PARAMETER_GROUP'|'SUBNET_GROUP',
                        'Message': 'string',
                        'Date': datetime(2015, 1, 1)
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
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


class DescribeParameterGroups(Paginator):
    def paginate(self, ParameterGroupNames: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DAX.Client.describe_parameter_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DescribeParameterGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ParameterGroupNames=[
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
                'ParameterGroups': [
                    {
                        'ParameterGroupName': 'string',
                        'Description': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ParameterGroups** *(list) --* 
              An array of parameter groups. Each element in the array represents one parameter group.
              - *(dict) --* 
                A named set of parameters that are applied to all of the nodes in a DAX cluster.
                - **ParameterGroupName** *(string) --* 
                  The name of the parameter group.
                - **Description** *(string) --* 
                  A description of the parameter group.
        :type ParameterGroupNames: list
        :param ParameterGroupNames:
          The names of the parameter groups.
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


class DescribeParameters(Paginator):
    def paginate(self, ParameterGroupName: str, Source: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DAX.Client.describe_parameters`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DescribeParameters>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ParameterGroupName='string',
              Source='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Parameters': [
                    {
                        'ParameterName': 'string',
                        'ParameterType': 'DEFAULT'|'NODE_TYPE_SPECIFIC',
                        'ParameterValue': 'string',
                        'NodeTypeSpecificValues': [
                            {
                                'NodeType': 'string',
                                'Value': 'string'
                            },
                        ],
                        'Description': 'string',
                        'Source': 'string',
                        'DataType': 'string',
                        'AllowedValues': 'string',
                        'IsModifiable': 'TRUE'|'FALSE'|'CONDITIONAL',
                        'ChangeType': 'IMMEDIATE'|'REQUIRES_REBOOT'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
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
        :type ParameterGroupName: string
        :param ParameterGroupName: **[REQUIRED]**
          The name of the parameter group.
        :type Source: string
        :param Source:
          How the parameter is defined. For example, ``system`` denotes a system-defined parameter.
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


class DescribeSubnetGroups(Paginator):
    def paginate(self, SubnetGroupNames: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DAX.Client.describe_subnet_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DescribeSubnetGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SubnetGroupNames=[
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
                'SubnetGroups': [
                    {
                        'SubnetGroupName': 'string',
                        'Description': 'string',
                        'VpcId': 'string',
                        'Subnets': [
                            {
                                'SubnetIdentifier': 'string',
                                'SubnetAvailabilityZone': 'string'
                            },
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
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
        :type SubnetGroupNames: list
        :param SubnetGroupNames:
          The name of the subnet group.
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


class ListTags(Paginator):
    def paginate(self, ResourceName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DAX.Client.list_tags`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/ListTags>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ResourceName='string',
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
                        'Value': 'string'
                    },
                ],
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
        :type ResourceName: string
        :param ResourceName: **[REQUIRED]**
          The name of the DAX resource to which the tags belong.
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
