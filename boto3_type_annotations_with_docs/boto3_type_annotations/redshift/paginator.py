from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class DescribeClusterDbRevisions(Paginator):
    def paginate(self, ClusterIdentifier: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_cluster_db_revisions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterDbRevisions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClusterIdentifier='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ClusterDbRevisions': [
                    {
                        'ClusterIdentifier': 'string',
                        'CurrentDatabaseRevision': 'string',
                        'DatabaseRevisionReleaseDate': datetime(2015, 1, 1),
                        'RevisionTargets': [
                            {
                                'DatabaseRevision': 'string',
                                'Description': 'string',
                                'DatabaseRevisionReleaseDate': datetime(2015, 1, 1)
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ClusterDbRevisions** *(list) --* 
              A list of revisions.
              - *(dict) --* 
                Describes a ``ClusterDbRevision`` .
                - **ClusterIdentifier** *(string) --* 
                  The unique identifier of the cluster.
                - **CurrentDatabaseRevision** *(string) --* 
                  A string representing the current cluster version.
                - **DatabaseRevisionReleaseDate** *(datetime) --* 
                  The date on which the database revision was released.
                - **RevisionTargets** *(list) --* 
                  A list of ``RevisionTarget`` objects, where each object describes the database revision that a cluster can be updated to.
                  - *(dict) --* 
                    Describes a ``RevisionTarget`` .
                    - **DatabaseRevision** *(string) --* 
                      A unique string that identifies the version to update the cluster to. You can use this value in  ModifyClusterDbRevision .
                    - **Description** *(string) --* 
                      A string that describes the changes and features that will be applied to the cluster when it is updated to the corresponding  ClusterDbRevision .
                    - **DatabaseRevisionReleaseDate** *(datetime) --* 
                      The date on which the database revision was released.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ClusterIdentifier: string
        :param ClusterIdentifier:
          A unique identifier for a cluster whose ``ClusterDbRevisions`` you are requesting. This parameter is case sensitive. All clusters defined for an account are returned by default.
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


class DescribeClusterParameterGroups(Paginator):
    def paginate(self, ParameterGroupName: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_cluster_parameter_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterParameterGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ParameterGroupName='string',
              TagKeys=[
                  'string',
              ],
              TagValues=[
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
                        'ParameterGroupFamily': 'string',
                        'Description': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output from the  DescribeClusterParameterGroups action. 
            - **ParameterGroups** *(list) --* 
              A list of  ClusterParameterGroup instances. Each instance describes one cluster parameter group. 
              - *(dict) --* 
                Describes a parameter group.
                - **ParameterGroupName** *(string) --* 
                  The name of the cluster parameter group.
                - **ParameterGroupFamily** *(string) --* 
                  The name of the cluster parameter group family that this cluster parameter group is compatible with.
                - **Description** *(string) --* 
                  The description of the parameter group.
                - **Tags** *(list) --* 
                  The list of tags for the cluster parameter group.
                  - *(dict) --* 
                    A tag consisting of a name/value pair for a resource.
                    - **Key** *(string) --* 
                      The key, or name, for the resource tag.
                    - **Value** *(string) --* 
                      The value for the resource tag.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ParameterGroupName: string
        :param ParameterGroupName:
          The name of a specific parameter group for which to return details. By default, details about all parameter groups and the default parameter group are returned.
        :type TagKeys: list
        :param TagKeys:
          A tag key or keys for which you want to return all matching cluster parameter groups that are associated with the specified key or keys. For example, suppose that you have parameter groups that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag keys associated with them.
          - *(string) --*
        :type TagValues: list
        :param TagValues:
          A tag value or values for which you want to return all matching cluster parameter groups that are associated with the specified tag value or values. For example, suppose that you have parameter groups that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag values associated with them.
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


class DescribeClusterParameters(Paginator):
    def paginate(self, ParameterGroupName: str, Source: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_cluster_parameters`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterParameters>`_
        
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
                        'ParameterValue': 'string',
                        'Description': 'string',
                        'Source': 'string',
                        'DataType': 'string',
                        'AllowedValues': 'string',
                        'ApplyType': 'static'|'dynamic',
                        'IsModifiable': True|False,
                        'MinimumEngineVersion': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output from the  DescribeClusterParameters action. 
            - **Parameters** *(list) --* 
              A list of  Parameter instances. Each instance lists the parameters of one cluster parameter group. 
              - *(dict) --* 
                Describes a parameter in a cluster parameter group.
                - **ParameterName** *(string) --* 
                  The name of the parameter.
                - **ParameterValue** *(string) --* 
                  The value of the parameter.
                - **Description** *(string) --* 
                  A description of the parameter.
                - **Source** *(string) --* 
                  The source of the parameter value, such as "engine-default" or "user".
                - **DataType** *(string) --* 
                  The data type of the parameter.
                - **AllowedValues** *(string) --* 
                  The valid range of values for the parameter.
                - **ApplyType** *(string) --* 
                  Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
                - **IsModifiable** *(boolean) --* 
                  If ``true`` , the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed. 
                - **MinimumEngineVersion** *(string) --* 
                  The earliest engine version to which the parameter can apply.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ParameterGroupName: string
        :param ParameterGroupName: **[REQUIRED]**
          The name of a cluster parameter group for which to return details.
        :type Source: string
        :param Source:
          The parameter types to return. Specify ``user`` to show parameters that are different form the default. Similarly, specify ``engine-default`` to show parameters that are the same as the default parameter group.
          Default: All parameter types returned.
          Valid Values: ``user`` | ``engine-default``
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


class DescribeClusterSecurityGroups(Paginator):
    def paginate(self, ClusterSecurityGroupName: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_cluster_security_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterSecurityGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClusterSecurityGroupName='string',
              TagKeys=[
                  'string',
              ],
              TagValues=[
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
                'ClusterSecurityGroups': [
                    {
                        'ClusterSecurityGroupName': 'string',
                        'Description': 'string',
                        'EC2SecurityGroups': [
                            {
                                'Status': 'string',
                                'EC2SecurityGroupName': 'string',
                                'EC2SecurityGroupOwnerId': 'string',
                                'Tags': [
                                    {
                                        'Key': 'string',
                                        'Value': 'string'
                                    },
                                ]
                            },
                        ],
                        'IPRanges': [
                            {
                                'Status': 'string',
                                'CIDRIP': 'string',
                                'Tags': [
                                    {
                                        'Key': 'string',
                                        'Value': 'string'
                                    },
                                ]
                            },
                        ],
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ClusterSecurityGroups** *(list) --* 
              A list of  ClusterSecurityGroup instances. 
              - *(dict) --* 
                Describes a security group.
                - **ClusterSecurityGroupName** *(string) --* 
                  The name of the cluster security group to which the operation was applied.
                - **Description** *(string) --* 
                  A description of the security group.
                - **EC2SecurityGroups** *(list) --* 
                  A list of EC2 security groups that are permitted to access clusters associated with this cluster security group.
                  - *(dict) --* 
                    Describes an Amazon EC2 security group.
                    - **Status** *(string) --* 
                      The status of the EC2 security group.
                    - **EC2SecurityGroupName** *(string) --* 
                      The name of the EC2 Security Group.
                    - **EC2SecurityGroupOwnerId** *(string) --* 
                      The AWS ID of the owner of the EC2 security group specified in the ``EC2SecurityGroupName`` field. 
                    - **Tags** *(list) --* 
                      The list of tags for the EC2 security group.
                      - *(dict) --* 
                        A tag consisting of a name/value pair for a resource.
                        - **Key** *(string) --* 
                          The key, or name, for the resource tag.
                        - **Value** *(string) --* 
                          The value for the resource tag.
                - **IPRanges** *(list) --* 
                  A list of IP ranges (CIDR blocks) that are permitted to access clusters associated with this cluster security group.
                  - *(dict) --* 
                    Describes an IP range used in a security group.
                    - **Status** *(string) --* 
                      The status of the IP range, for example, "authorized".
                    - **CIDRIP** *(string) --* 
                      The IP range in Classless Inter-Domain Routing (CIDR) notation.
                    - **Tags** *(list) --* 
                      The list of tags for the IP range.
                      - *(dict) --* 
                        A tag consisting of a name/value pair for a resource.
                        - **Key** *(string) --* 
                          The key, or name, for the resource tag.
                        - **Value** *(string) --* 
                          The value for the resource tag.
                - **Tags** *(list) --* 
                  The list of tags for the cluster security group.
                  - *(dict) --* 
                    A tag consisting of a name/value pair for a resource.
                    - **Key** *(string) --* 
                      The key, or name, for the resource tag.
                    - **Value** *(string) --* 
                      The value for the resource tag.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ClusterSecurityGroupName: string
        :param ClusterSecurityGroupName:
          The name of a cluster security group for which you are requesting details. You can specify either the **Marker** parameter or a **ClusterSecurityGroupName** parameter, but not both.
          Example: ``securitygroup1``
        :type TagKeys: list
        :param TagKeys:
          A tag key or keys for which you want to return all matching cluster security groups that are associated with the specified key or keys. For example, suppose that you have security groups that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag keys associated with them.
          - *(string) --*
        :type TagValues: list
        :param TagValues:
          A tag value or values for which you want to return all matching cluster security groups that are associated with the specified tag value or values. For example, suppose that you have security groups that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag values associated with them.
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


class DescribeClusterSnapshots(Paginator):
    def paginate(self, ClusterIdentifier: str = None, SnapshotIdentifier: str = None, SnapshotType: str = None, StartTime: datetime = None, EndTime: datetime = None, OwnerAccount: str = None, TagKeys: List = None, TagValues: List = None, ClusterExists: bool = None, SortingEntities: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_cluster_snapshots`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterSnapshots>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClusterIdentifier='string',
              SnapshotIdentifier='string',
              SnapshotType='string',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              OwnerAccount='string',
              TagKeys=[
                  'string',
              ],
              TagValues=[
                  'string',
              ],
              ClusterExists=True|False,
              SortingEntities=[
                  {
                      'Attribute': 'SOURCE_TYPE'|'TOTAL_SIZE'|'CREATE_TIME',
                      'SortOrder': 'ASC'|'DESC'
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
                'Snapshots': [
                    {
                        'SnapshotIdentifier': 'string',
                        'ClusterIdentifier': 'string',
                        'SnapshotCreateTime': datetime(2015, 1, 1),
                        'Status': 'string',
                        'Port': 123,
                        'AvailabilityZone': 'string',
                        'ClusterCreateTime': datetime(2015, 1, 1),
                        'MasterUsername': 'string',
                        'ClusterVersion': 'string',
                        'SnapshotType': 'string',
                        'NodeType': 'string',
                        'NumberOfNodes': 123,
                        'DBName': 'string',
                        'VpcId': 'string',
                        'Encrypted': True|False,
                        'KmsKeyId': 'string',
                        'EncryptedWithHSM': True|False,
                        'AccountsWithRestoreAccess': [
                            {
                                'AccountId': 'string',
                                'AccountAlias': 'string'
                            },
                        ],
                        'OwnerAccount': 'string',
                        'TotalBackupSizeInMegaBytes': 123.0,
                        'ActualIncrementalBackupSizeInMegaBytes': 123.0,
                        'BackupProgressInMegaBytes': 123.0,
                        'CurrentBackupRateInMegaBytesPerSecond': 123.0,
                        'EstimatedSecondsToCompletion': 123,
                        'ElapsedTimeInSeconds': 123,
                        'SourceRegion': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'RestorableNodeTypes': [
                            'string',
                        ],
                        'EnhancedVpcRouting': True|False,
                        'MaintenanceTrackName': 'string',
                        'ManualSnapshotRetentionPeriod': 123,
                        'ManualSnapshotRemainingDays': 123,
                        'SnapshotRetentionStartTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output from the  DescribeClusterSnapshots action. 
            - **Snapshots** *(list) --* 
              A list of  Snapshot instances. 
              - *(dict) --* 
                Describes a snapshot.
                - **SnapshotIdentifier** *(string) --* 
                  The snapshot identifier that is provided in the request.
                - **ClusterIdentifier** *(string) --* 
                  The identifier of the cluster for which the snapshot was taken.
                - **SnapshotCreateTime** *(datetime) --* 
                  The time (in UTC format) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.
                - **Status** *(string) --* 
                  The snapshot status. The value of the status depends on the API operation used: 
                  *  CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".  
                  *  DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed". 
                  *  DeleteClusterSnapshot returns status as "deleted". 
                - **Port** *(integer) --* 
                  The port that the cluster is listening on.
                - **AvailabilityZone** *(string) --* 
                  The Availability Zone in which the cluster was created.
                - **ClusterCreateTime** *(datetime) --* 
                  The time (UTC) when the cluster was originally created.
                - **MasterUsername** *(string) --* 
                  The master user name for the cluster.
                - **ClusterVersion** *(string) --* 
                  The version ID of the Amazon Redshift engine that is running on the cluster.
                - **SnapshotType** *(string) --* 
                  The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot are of type "manual". 
                - **NodeType** *(string) --* 
                  The node type of the nodes in the cluster.
                - **NumberOfNodes** *(integer) --* 
                  The number of nodes in the cluster.
                - **DBName** *(string) --* 
                  The name of the database that was created when the cluster was created.
                - **VpcId** *(string) --* 
                  The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.
                - **Encrypted** *(boolean) --* 
                  If ``true`` , the data in the snapshot is encrypted at rest.
                - **KmsKeyId** *(string) --* 
                  The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.
                - **EncryptedWithHSM** *(boolean) --* 
                  A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. ``true`` indicates that the data is encrypted using HSM keys.
                - **AccountsWithRestoreAccess** *(list) --* 
                  A list of the AWS customer accounts authorized to restore the snapshot. Returns ``null`` if no accounts are authorized. Visible only to the snapshot owner. 
                  - *(dict) --* 
                    Describes an AWS customer account authorized to restore a snapshot.
                    - **AccountId** *(string) --* 
                      The identifier of an AWS customer account authorized to restore a snapshot.
                    - **AccountAlias** *(string) --* 
                      The identifier of an AWS support account authorized to restore a snapshot. For AWS support, the identifier is ``amazon-redshift-support`` . 
                - **OwnerAccount** *(string) --* 
                  For manual snapshots, the AWS customer account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.
                - **TotalBackupSizeInMegaBytes** *(float) --* 
                  The size of the complete set of backup data that would be used to restore the cluster.
                - **ActualIncrementalBackupSizeInMegaBytes** *(float) --* 
                  The size of the incremental backup.
                - **BackupProgressInMegaBytes** *(float) --* 
                  The number of megabytes that have been transferred to the snapshot backup.
                - **CurrentBackupRateInMegaBytesPerSecond** *(float) --* 
                  The number of megabytes per second being transferred to the snapshot backup. Returns ``0`` for a completed backup. 
                - **EstimatedSecondsToCompletion** *(integer) --* 
                  The estimate of the time remaining before the snapshot backup will complete. Returns ``0`` for a completed backup. 
                - **ElapsedTimeInSeconds** *(integer) --* 
                  The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.
                - **SourceRegion** *(string) --* 
                  The source region from which the snapshot was copied.
                - **Tags** *(list) --* 
                  The list of tags for the cluster snapshot.
                  - *(dict) --* 
                    A tag consisting of a name/value pair for a resource.
                    - **Key** *(string) --* 
                      The key, or name, for the resource tag.
                    - **Value** *(string) --* 
                      The value for the resource tag.
                - **RestorableNodeTypes** *(list) --* 
                  The list of node types that this cluster snapshot is able to restore into.
                  - *(string) --* 
                - **EnhancedVpcRouting** *(boolean) --* 
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
                  If this option is ``true`` , enhanced VPC routing is enabled. 
                  Default: false
                - **MaintenanceTrackName** *(string) --* 
                  The name of the maintenance track for the snapshot.
                - **ManualSnapshotRetentionPeriod** *(integer) --* 
                  The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely. 
                  The value must be either -1 or an integer between 1 and 3,653.
                - **ManualSnapshotRemainingDays** *(integer) --* 
                  The number of days until a manual snapshot will pass its retention period.
                - **SnapshotRetentionStartTime** *(datetime) --* 
                  A timestamp representing the start of the retention period for the snapshot.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ClusterIdentifier: string
        :param ClusterIdentifier:
          The identifier of the cluster which generated the requested snapshots.
        :type SnapshotIdentifier: string
        :param SnapshotIdentifier:
          The snapshot identifier of the snapshot about which to return information.
        :type SnapshotType: string
        :param SnapshotType:
          The type of snapshots for which you are requesting information. By default, snapshots of all types are returned.
          Valid Values: ``automated`` | ``manual``
        :type StartTime: datetime
        :param StartTime:
          A value that requests only snapshots created at or after the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the `ISO8601 Wikipedia page. <http://en.wikipedia.org/wiki/ISO_8601>`__
          Example: ``2012-07-16T18:00:00Z``
        :type EndTime: datetime
        :param EndTime:
          A time value that requests only snapshots created at or before the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the `ISO8601 Wikipedia page. <http://en.wikipedia.org/wiki/ISO_8601>`__
          Example: ``2012-07-16T18:00:00Z``
        :type OwnerAccount: string
        :param OwnerAccount:
          The AWS customer account used to create or copy the snapshot. Use this field to filter the results to snapshots owned by a particular account. To describe snapshots you own, either specify your AWS customer account, or do not specify the parameter.
        :type TagKeys: list
        :param TagKeys:
          A tag key or keys for which you want to return all matching cluster snapshots that are associated with the specified key or keys. For example, suppose that you have snapshots that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag keys associated with them.
          - *(string) --*
        :type TagValues: list
        :param TagValues:
          A tag value or values for which you want to return all matching cluster snapshots that are associated with the specified tag value or values. For example, suppose that you have snapshots that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag values associated with them.
          - *(string) --*
        :type ClusterExists: boolean
        :param ClusterExists:
          A value that indicates whether to return snapshots only for an existing cluster. You can perform table-level restore only by using a snapshot of an existing cluster, that is, a cluster that has not been deleted. Values for this parameter work as follows:
          * If ``ClusterExists`` is set to ``true`` , ``ClusterIdentifier`` is required.
          * If ``ClusterExists`` is set to ``false`` and ``ClusterIdentifier`` isn\'t specified, all snapshots associated with deleted clusters (orphaned snapshots) are returned.
          * If ``ClusterExists`` is set to ``false`` and ``ClusterIdentifier`` is specified for a deleted cluster, snapshots associated with that cluster are returned.
          * If ``ClusterExists`` is set to ``false`` and ``ClusterIdentifier`` is specified for an existing cluster, no snapshots are returned.
        :type SortingEntities: list
        :param SortingEntities:
          - *(dict) --*
            Describes a sorting entity
            - **Attribute** *(string) --* **[REQUIRED]**
              The category for sorting the snapshots.
            - **SortOrder** *(string) --*
              The order for listing the attributes.
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


class DescribeClusterSubnetGroups(Paginator):
    def paginate(self, ClusterSubnetGroupName: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_cluster_subnet_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterSubnetGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClusterSubnetGroupName='string',
              TagKeys=[
                  'string',
              ],
              TagValues=[
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
                'ClusterSubnetGroups': [
                    {
                        'ClusterSubnetGroupName': 'string',
                        'Description': 'string',
                        'VpcId': 'string',
                        'SubnetGroupStatus': 'string',
                        'Subnets': [
                            {
                                'SubnetIdentifier': 'string',
                                'SubnetAvailabilityZone': {
                                    'Name': 'string',
                                    'SupportedPlatforms': [
                                        {
                                            'Name': 'string'
                                        },
                                    ]
                                },
                                'SubnetStatus': 'string'
                            },
                        ],
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output from the  DescribeClusterSubnetGroups action. 
            - **ClusterSubnetGroups** *(list) --* 
              A list of  ClusterSubnetGroup instances. 
              - *(dict) --* 
                Describes a subnet group.
                - **ClusterSubnetGroupName** *(string) --* 
                  The name of the cluster subnet group.
                - **Description** *(string) --* 
                  The description of the cluster subnet group.
                - **VpcId** *(string) --* 
                  The VPC ID of the cluster subnet group.
                - **SubnetGroupStatus** *(string) --* 
                  The status of the cluster subnet group. Possible values are ``Complete`` , ``Incomplete`` and ``Invalid`` . 
                - **Subnets** *(list) --* 
                  A list of the VPC  Subnet elements. 
                  - *(dict) --* 
                    Describes a subnet.
                    - **SubnetIdentifier** *(string) --* 
                      The identifier of the subnet.
                    - **SubnetAvailabilityZone** *(dict) --* 
                      - **Name** *(string) --* 
                        The name of the availability zone.
                      - **SupportedPlatforms** *(list) --* 
                        - *(dict) --* 
                          A list of supported platforms for orderable clusters.
                          - **Name** *(string) --* 
                    - **SubnetStatus** *(string) --* 
                      The status of the subnet.
                - **Tags** *(list) --* 
                  The list of tags for the cluster subnet group.
                  - *(dict) --* 
                    A tag consisting of a name/value pair for a resource.
                    - **Key** *(string) --* 
                      The key, or name, for the resource tag.
                    - **Value** *(string) --* 
                      The value for the resource tag.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ClusterSubnetGroupName: string
        :param ClusterSubnetGroupName:
          The name of the cluster subnet group for which information is requested.
        :type TagKeys: list
        :param TagKeys:
          A tag key or keys for which you want to return all matching cluster subnet groups that are associated with the specified key or keys. For example, suppose that you have subnet groups that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag keys associated with them.
          - *(string) --*
        :type TagValues: list
        :param TagValues:
          A tag value or values for which you want to return all matching cluster subnet groups that are associated with the specified tag value or values. For example, suppose that you have subnet groups that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag values associated with them.
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


class DescribeClusterTracks(Paginator):
    def paginate(self, MaintenanceTrackName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_cluster_tracks`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterTracks>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              MaintenanceTrackName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'MaintenanceTracks': [
                    {
                        'MaintenanceTrackName': 'string',
                        'DatabaseVersion': 'string',
                        'UpdateTargets': [
                            {
                                'MaintenanceTrackName': 'string',
                                'DatabaseVersion': 'string',
                                'SupportedOperations': [
                                    {
                                        'OperationName': 'string'
                                    },
                                ]
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **MaintenanceTracks** *(list) --* 
              A list of maintenance tracks output by the ``DescribeClusterTracks`` operation. 
              - *(dict) --* 
                Defines a maintenance track that determines which Amazon Redshift version to apply during a maintenance window. If the value for ``MaintenanceTrack`` is ``current`` , the cluster is updated to the most recently certified maintenance release. If the value is ``trailing`` , the cluster is updated to the previously certified maintenance release. 
                - **MaintenanceTrackName** *(string) --* 
                  The name of the maintenance track. Possible values are ``current`` and ``trailing`` .
                - **DatabaseVersion** *(string) --* 
                  The version number for the cluster release.
                - **UpdateTargets** *(list) --* 
                  An array of  UpdateTarget objects to update with the maintenance track. 
                  - *(dict) --* 
                    A maintenance track that you can switch the current track to.
                    - **MaintenanceTrackName** *(string) --* 
                      The name of the new maintenance track.
                    - **DatabaseVersion** *(string) --* 
                      The cluster version for the new maintenance track.
                    - **SupportedOperations** *(list) --* 
                      A list of operations supported by the maintenance track.
                      - *(dict) --* 
                        Describes the operations that are allowed on a maintenance track.
                        - **OperationName** *(string) --* 
                          A list of the supported operations.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type MaintenanceTrackName: string
        :param MaintenanceTrackName:
          The name of the maintenance track.
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


class DescribeClusterVersions(Paginator):
    def paginate(self, ClusterVersion: str = None, ClusterParameterGroupFamily: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_cluster_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusterVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClusterVersion='string',
              ClusterParameterGroupFamily='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ClusterVersions': [
                    {
                        'ClusterVersion': 'string',
                        'ClusterParameterGroupFamily': 'string',
                        'Description': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output from the  DescribeClusterVersions action. 
            - **ClusterVersions** *(list) --* 
              A list of ``Version`` elements. 
              - *(dict) --* 
                Describes a cluster version, including the parameter group family and description of the version.
                - **ClusterVersion** *(string) --* 
                  The version number used by the cluster.
                - **ClusterParameterGroupFamily** *(string) --* 
                  The name of the cluster parameter group family for the cluster.
                - **Description** *(string) --* 
                  The description of the cluster version.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ClusterVersion: string
        :param ClusterVersion:
          The specific cluster version to return.
          Example: ``1.0``
        :type ClusterParameterGroupFamily: string
        :param ClusterParameterGroupFamily:
          The name of a specific cluster parameter group family to return details for.
          Constraints:
          * Must be 1 to 255 alphanumeric characters
          * First character must be a letter
          * Cannot end with a hyphen or contain two consecutive hyphens
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


class DescribeClusters(Paginator):
    def paginate(self, ClusterIdentifier: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_clusters`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeClusters>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClusterIdentifier='string',
              TagKeys=[
                  'string',
              ],
              TagValues=[
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
                        'ClusterIdentifier': 'string',
                        'NodeType': 'string',
                        'ClusterStatus': 'string',
                        'ModifyStatus': 'string',
                        'MasterUsername': 'string',
                        'DBName': 'string',
                        'Endpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'ClusterCreateTime': datetime(2015, 1, 1),
                        'AutomatedSnapshotRetentionPeriod': 123,
                        'ManualSnapshotRetentionPeriod': 123,
                        'ClusterSecurityGroups': [
                            {
                                'ClusterSecurityGroupName': 'string',
                                'Status': 'string'
                            },
                        ],
                        'VpcSecurityGroups': [
                            {
                                'VpcSecurityGroupId': 'string',
                                'Status': 'string'
                            },
                        ],
                        'ClusterParameterGroups': [
                            {
                                'ParameterGroupName': 'string',
                                'ParameterApplyStatus': 'string',
                                'ClusterParameterStatusList': [
                                    {
                                        'ParameterName': 'string',
                                        'ParameterApplyStatus': 'string',
                                        'ParameterApplyErrorDescription': 'string'
                                    },
                                ]
                            },
                        ],
                        'ClusterSubnetGroupName': 'string',
                        'VpcId': 'string',
                        'AvailabilityZone': 'string',
                        'PreferredMaintenanceWindow': 'string',
                        'PendingModifiedValues': {
                            'MasterUserPassword': 'string',
                            'NodeType': 'string',
                            'NumberOfNodes': 123,
                            'ClusterType': 'string',
                            'ClusterVersion': 'string',
                            'AutomatedSnapshotRetentionPeriod': 123,
                            'ClusterIdentifier': 'string',
                            'PubliclyAccessible': True|False,
                            'EnhancedVpcRouting': True|False,
                            'MaintenanceTrackName': 'string',
                            'EncryptionType': 'string'
                        },
                        'ClusterVersion': 'string',
                        'AllowVersionUpgrade': True|False,
                        'NumberOfNodes': 123,
                        'PubliclyAccessible': True|False,
                        'Encrypted': True|False,
                        'RestoreStatus': {
                            'Status': 'string',
                            'CurrentRestoreRateInMegaBytesPerSecond': 123.0,
                            'SnapshotSizeInMegaBytes': 123,
                            'ProgressInMegaBytes': 123,
                            'ElapsedTimeInSeconds': 123,
                            'EstimatedTimeToCompletionInSeconds': 123
                        },
                        'DataTransferProgress': {
                            'Status': 'string',
                            'CurrentRateInMegaBytesPerSecond': 123.0,
                            'TotalDataInMegaBytes': 123,
                            'DataTransferredInMegaBytes': 123,
                            'EstimatedTimeToCompletionInSeconds': 123,
                            'ElapsedTimeInSeconds': 123
                        },
                        'HsmStatus': {
                            'HsmClientCertificateIdentifier': 'string',
                            'HsmConfigurationIdentifier': 'string',
                            'Status': 'string'
                        },
                        'ClusterSnapshotCopyStatus': {
                            'DestinationRegion': 'string',
                            'RetentionPeriod': 123,
                            'ManualSnapshotRetentionPeriod': 123,
                            'SnapshotCopyGrantName': 'string'
                        },
                        'ClusterPublicKey': 'string',
                        'ClusterNodes': [
                            {
                                'NodeRole': 'string',
                                'PrivateIPAddress': 'string',
                                'PublicIPAddress': 'string'
                            },
                        ],
                        'ElasticIpStatus': {
                            'ElasticIp': 'string',
                            'Status': 'string'
                        },
                        'ClusterRevisionNumber': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'KmsKeyId': 'string',
                        'EnhancedVpcRouting': True|False,
                        'IamRoles': [
                            {
                                'IamRoleArn': 'string',
                                'ApplyStatus': 'string'
                            },
                        ],
                        'PendingActions': [
                            'string',
                        ],
                        'MaintenanceTrackName': 'string',
                        'ElasticResizeNumberOfNodeOptions': 'string',
                        'DeferredMaintenanceWindows': [
                            {
                                'DeferMaintenanceIdentifier': 'string',
                                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                            },
                        ],
                        'SnapshotScheduleIdentifier': 'string',
                        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
                        'ResizeInfo': {
                            'ResizeType': 'string',
                            'AllowCancelResize': True|False
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output from the  DescribeClusters action. 
            - **Clusters** *(list) --* 
              A list of ``Cluster`` objects, where each object describes one cluster. 
              - *(dict) --* 
                Describes a cluster.
                - **ClusterIdentifier** *(string) --* 
                  The unique identifier of the cluster.
                - **NodeType** *(string) --* 
                  The node type for the nodes in the cluster.
                - **ClusterStatus** *(string) --* 
                  The current state of the cluster. Possible values are the following:
                  * ``available``   
                  * ``available, prep-for-resize``   
                  * ``available, resize-cleanup``   
                  * ``cancelling-resize``   
                  * ``creating``   
                  * ``deleting``   
                  * ``final-snapshot``   
                  * ``hardware-failure``   
                  * ``incompatible-hsm``   
                  * ``incompatible-network``   
                  * ``incompatible-parameters``   
                  * ``incompatible-restore``   
                  * ``modifying``   
                  * ``rebooting``   
                  * ``renaming``   
                  * ``resizing``   
                  * ``rotating-keys``   
                  * ``storage-full``   
                  * ``updating-hsm``   
                - **ModifyStatus** *(string) --* 
                  The status of a modify operation, if any, initiated for the cluster.
                - **MasterUsername** *(string) --* 
                  The master user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter. 
                - **DBName** *(string) --* 
                  The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named ``dev`` dev was created by default. 
                - **Endpoint** *(dict) --* 
                  The connection endpoint.
                  - **Address** *(string) --* 
                    The DNS address of the Cluster.
                  - **Port** *(integer) --* 
                    The port that the database engine is listening on.
                - **ClusterCreateTime** *(datetime) --* 
                  The date and time that the cluster was created.
                - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
                  The number of days that automatic cluster snapshots are retained.
                - **ManualSnapshotRetentionPeriod** *(integer) --* 
                  The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots.
                  The value must be either -1 or an integer between 1 and 3,653.
                - **ClusterSecurityGroups** *(list) --* 
                  A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ``ClusterSecurityGroup.Name`` and ``ClusterSecurityGroup.Status`` subelements. 
                  Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter. 
                  - *(dict) --* 
                    Describes a cluster security group.
                    - **ClusterSecurityGroupName** *(string) --* 
                      The name of the cluster security group.
                    - **Status** *(string) --* 
                      The status of the cluster security group.
                - **VpcSecurityGroups** *(list) --* 
                  A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
                  - *(dict) --* 
                    Describes the members of a VPC security group.
                    - **VpcSecurityGroupId** *(string) --* 
                      The identifier of the VPC security group.
                    - **Status** *(string) --* 
                      The status of the VPC security group.
                - **ClusterParameterGroups** *(list) --* 
                  The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
                  - *(dict) --* 
                    Describes the status of a parameter group.
                    - **ParameterGroupName** *(string) --* 
                      The name of the cluster parameter group.
                    - **ParameterApplyStatus** *(string) --* 
                      The status of parameter updates.
                    - **ClusterParameterStatusList** *(list) --* 
                      The list of parameter statuses.
                      For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
                      - *(dict) --* 
                        Describes the status of a parameter group.
                        - **ParameterName** *(string) --* 
                          The name of the parameter.
                        - **ParameterApplyStatus** *(string) --* 
                          The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
                          The following are possible statuses and descriptions.
                          * ``in-sync`` : The parameter value is in sync with the database. 
                          * ``pending-reboot`` : The parameter value will be applied after the cluster reboots. 
                          * ``applying`` : The parameter value is being applied to the database. 
                          * ``invalid-parameter`` : Cannot apply the parameter value because it has an invalid value or syntax. 
                          * ``apply-deferred`` : The parameter contains static property changes. The changes are deferred until the cluster reboots. 
                          * ``apply-error`` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots. 
                          * ``unknown-error`` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots. 
                        - **ParameterApplyErrorDescription** *(string) --* 
                          The error that prevented the parameter from being applied to the database.
                - **ClusterSubnetGroupName** *(string) --* 
                  The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
                - **VpcId** *(string) --* 
                  The identifier of the VPC the cluster is in, if the cluster is in a VPC.
                - **AvailabilityZone** *(string) --* 
                  The name of the Availability Zone in which the cluster is located.
                - **PreferredMaintenanceWindow** *(string) --* 
                  The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
                - **PendingModifiedValues** *(dict) --* 
                  A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
                  - **MasterUserPassword** *(string) --* 
                    The pending or in-progress change of the master user password for the cluster.
                  - **NodeType** *(string) --* 
                    The pending or in-progress change of the cluster's node type.
                  - **NumberOfNodes** *(integer) --* 
                    The pending or in-progress change of the number of nodes in the cluster.
                  - **ClusterType** *(string) --* 
                    The pending or in-progress change of the cluster type.
                  - **ClusterVersion** *(string) --* 
                    The pending or in-progress change of the service version.
                  - **AutomatedSnapshotRetentionPeriod** *(integer) --* 
                    The pending or in-progress change of the automated snapshot retention period.
                  - **ClusterIdentifier** *(string) --* 
                    The pending or in-progress change of the new identifier for the cluster.
                  - **PubliclyAccessible** *(boolean) --* 
                    The pending or in-progress change of the ability to connect to the cluster from the public network.
                  - **EnhancedVpcRouting** *(boolean) --* 
                    An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
                    If this option is ``true`` , enhanced VPC routing is enabled. 
                    Default: false
                  - **MaintenanceTrackName** *(string) --* 
                    The name of the maintenance track that the cluster will change to during the next maintenance window.
                  - **EncryptionType** *(string) --* 
                    The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy. 
                - **ClusterVersion** *(string) --* 
                  The version ID of the Amazon Redshift engine that is running on the cluster.
                - **AllowVersionUpgrade** *(boolean) --* 
                  A boolean value that, if ``true`` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. 
                - **NumberOfNodes** *(integer) --* 
                  The number of compute nodes in the cluster.
                - **PubliclyAccessible** *(boolean) --* 
                  A boolean value that, if ``true`` , indicates that the cluster can be accessed from a public network.
                - **Encrypted** *(boolean) --* 
                  A boolean value that, if ``true`` , indicates that data in the cluster is encrypted at rest.
                - **RestoreStatus** *(dict) --* 
                  A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
                  - **Status** *(string) --* 
                    The status of the restore action. Returns starting, restoring, completed, or failed.
                  - **CurrentRestoreRateInMegaBytesPerSecond** *(float) --* 
                    The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
                  - **SnapshotSizeInMegaBytes** *(integer) --* 
                    The size of the set of snapshot data used to restore the cluster.
                  - **ProgressInMegaBytes** *(integer) --* 
                    The number of megabytes that have been transferred from snapshot storage.
                  - **ElapsedTimeInSeconds** *(integer) --* 
                    The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
                  - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
                    The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
                - **DataTransferProgress** *(dict) --* 
                  - **Status** *(string) --* 
                    Describes the status of the cluster. While the transfer is in progress the status is ``transferringdata`` .
                  - **CurrentRateInMegaBytesPerSecond** *(float) --* 
                    Describes the data transfer rate in MB's per second.
                  - **TotalDataInMegaBytes** *(integer) --* 
                    Describes the total amount of data to be transfered in megabytes.
                  - **DataTransferredInMegaBytes** *(integer) --* 
                    Describes the total amount of data that has been transfered in MB's.
                  - **EstimatedTimeToCompletionInSeconds** *(integer) --* 
                    Describes the estimated number of seconds remaining to complete the transfer.
                  - **ElapsedTimeInSeconds** *(integer) --* 
                    Describes the number of seconds that have elapsed during the data transfer.
                - **HsmStatus** *(dict) --* 
                  A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
                  Values: active, applying
                  - **HsmClientCertificateIdentifier** *(string) --* 
                    Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
                  - **HsmConfigurationIdentifier** *(string) --* 
                    Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
                  - **Status** *(string) --* 
                    Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
                    Values: active, applying
                - **ClusterSnapshotCopyStatus** *(dict) --* 
                  A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
                  - **DestinationRegion** *(string) --* 
                    The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
                  - **RetentionPeriod** *(integer) --* 
                    The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
                  - **ManualSnapshotRetentionPeriod** *(integer) --* 
                    The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely. 
                    The value must be either -1 or an integer between 1 and 3,653.
                  - **SnapshotCopyGrantName** *(string) --* 
                    The name of the snapshot copy grant.
                - **ClusterPublicKey** *(string) --* 
                  The public key for the cluster.
                - **ClusterNodes** *(list) --* 
                  The nodes in the cluster.
                  - *(dict) --* 
                    The identifier of a node in a cluster.
                    - **NodeRole** *(string) --* 
                      Whether the node is a leader node or a compute node.
                    - **PrivateIPAddress** *(string) --* 
                      The private IP address of a node within a cluster.
                    - **PublicIPAddress** *(string) --* 
                      The public IP address of a node within a cluster.
                - **ElasticIpStatus** *(dict) --* 
                  The status of the elastic IP (EIP) address.
                  - **ElasticIp** *(string) --* 
                    The elastic IP (EIP) address for the cluster.
                  - **Status** *(string) --* 
                    The status of the elastic IP (EIP) address.
                - **ClusterRevisionNumber** *(string) --* 
                  The specific revision number of the database in the cluster.
                - **Tags** *(list) --* 
                  The list of tags for the cluster.
                  - *(dict) --* 
                    A tag consisting of a name/value pair for a resource.
                    - **Key** *(string) --* 
                      The key, or name, for the resource tag.
                    - **Value** *(string) --* 
                      The value for the resource tag.
                - **KmsKeyId** *(string) --* 
                  The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
                - **EnhancedVpcRouting** *(boolean) --* 
                  An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`__ in the Amazon Redshift Cluster Management Guide.
                  If this option is ``true`` , enhanced VPC routing is enabled. 
                  Default: false
                - **IamRoles** *(list) --* 
                  A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
                  - *(dict) --* 
                    An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
                    - **IamRoleArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the IAM role, for example, ``arn:aws:iam::123456789012:role/RedshiftCopyUnload`` . 
                    - **ApplyStatus** *(string) --* 
                      A value that describes the status of the IAM role's association with an Amazon Redshift cluster.
                      The following are possible statuses and descriptions.
                      * ``in-sync`` : The role is available for use by the cluster. 
                      * ``adding`` : The role is in the process of being associated with the cluster. 
                      * ``removing`` : The role is in the process of being disassociated with the cluster. 
                - **PendingActions** *(list) --* 
                  Cluster operations that are waiting to be started.
                  - *(string) --* 
                - **MaintenanceTrackName** *(string) --* 
                  The name of the maintenance track for the cluster.
                - **ElasticResizeNumberOfNodeOptions** *(string) --* 
                  The number of nodes that you can resize the cluster to with the elastic resize method. 
                - **DeferredMaintenanceWindows** *(list) --* 
                  Describes a group of ``DeferredMaintenanceWindow`` objects.
                  - *(dict) --* 
                    Describes a deferred maintenance window
                    - **DeferMaintenanceIdentifier** *(string) --* 
                      A unique identifier for the maintenance window.
                    - **DeferMaintenanceStartTime** *(datetime) --* 
                      A timestamp for the beginning of the time period when we defer maintenance.
                    - **DeferMaintenanceEndTime** *(datetime) --* 
                      A timestamp for the end of the time period when we defer maintenance.
                - **SnapshotScheduleIdentifier** *(string) --* 
                  A unique identifier for the cluster snapshot schedule.
                - **SnapshotScheduleState** *(string) --* 
                  The current state of the cluster snapshot schedule.
                - **ResizeInfo** *(dict) --* 
                  Returns the following:
                  * AllowCancelResize: a boolean value indicating if the resize operation can be cancelled. 
                  * ResizeType: Returns ClassicResize 
                  - **ResizeType** *(string) --* 
                    Returns the value ``ClassicResize`` .
                  - **AllowCancelResize** *(boolean) --* 
                    A boolean value indicating if the resize operation can be cancelled.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ClusterIdentifier: string
        :param ClusterIdentifier:
          The unique identifier of a cluster whose properties you are requesting. This parameter is case sensitive.
          The default is that all clusters defined for an account are returned.
        :type TagKeys: list
        :param TagKeys:
          A tag key or keys for which you want to return all matching clusters that are associated with the specified key or keys. For example, suppose that you have clusters that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag keys associated with them.
          - *(string) --*
        :type TagValues: list
        :param TagValues:
          A tag value or values for which you want to return all matching clusters that are associated with the specified tag value or values. For example, suppose that you have clusters that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag values associated with them.
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


class DescribeDefaultClusterParameters(Paginator):
    def paginate(self, ParameterGroupFamily: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_default_cluster_parameters`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeDefaultClusterParameters>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ParameterGroupFamily='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'DefaultClusterParameters': {
                    'ParameterGroupFamily': 'string',
                    'Marker': 'string',
                    'Parameters': [
                        {
                            'ParameterName': 'string',
                            'ParameterValue': 'string',
                            'Description': 'string',
                            'Source': 'string',
                            'DataType': 'string',
                            'AllowedValues': 'string',
                            'ApplyType': 'static'|'dynamic',
                            'IsModifiable': True|False,
                            'MinimumEngineVersion': 'string'
                        },
                    ]
                },
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DefaultClusterParameters** *(dict) --* 
              Describes the default cluster parameters for a parameter group family.
              - **ParameterGroupFamily** *(string) --* 
                The name of the cluster parameter group family to which the engine default parameters apply.
              - **Marker** *(string) --* 
                A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the ``Marker`` parameter and retrying the command. If the ``Marker`` field is empty, all response records have been retrieved for the request. 
              - **Parameters** *(list) --* 
                The list of cluster default parameters.
                - *(dict) --* 
                  Describes a parameter in a cluster parameter group.
                  - **ParameterName** *(string) --* 
                    The name of the parameter.
                  - **ParameterValue** *(string) --* 
                    The value of the parameter.
                  - **Description** *(string) --* 
                    A description of the parameter.
                  - **Source** *(string) --* 
                    The source of the parameter value, such as "engine-default" or "user".
                  - **DataType** *(string) --* 
                    The data type of the parameter.
                  - **AllowedValues** *(string) --* 
                    The valid range of values for the parameter.
                  - **ApplyType** *(string) --* 
                    Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to `Amazon Redshift Parameter Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`__ in the *Amazon Redshift Cluster Management Guide* .
                  - **IsModifiable** *(boolean) --* 
                    If ``true`` , the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed. 
                  - **MinimumEngineVersion** *(string) --* 
                    The earliest engine version to which the parameter can apply.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ParameterGroupFamily: string
        :param ParameterGroupFamily: **[REQUIRED]**
          The name of the cluster parameter group family.
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


class DescribeEventSubscriptions(Paginator):
    def paginate(self, SubscriptionName: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_event_subscriptions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeEventSubscriptions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SubscriptionName='string',
              TagKeys=[
                  'string',
              ],
              TagValues=[
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
                'EventSubscriptionsList': [
                    {
                        'CustomerAwsId': 'string',
                        'CustSubscriptionId': 'string',
                        'SnsTopicArn': 'string',
                        'Status': 'string',
                        'SubscriptionCreationTime': datetime(2015, 1, 1),
                        'SourceType': 'string',
                        'SourceIdsList': [
                            'string',
                        ],
                        'EventCategoriesList': [
                            'string',
                        ],
                        'Severity': 'string',
                        'Enabled': True|False,
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EventSubscriptionsList** *(list) --* 
              A list of event subscriptions.
              - *(dict) --* 
                Describes event subscriptions.
                - **CustomerAwsId** *(string) --* 
                  The AWS customer account associated with the Amazon Redshift event notification subscription.
                - **CustSubscriptionId** *(string) --* 
                  The name of the Amazon Redshift event notification subscription.
                - **SnsTopicArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the Amazon SNS topic used by the event notification subscription.
                - **Status** *(string) --* 
                  The status of the Amazon Redshift event notification subscription.
                  Constraints:
                  * Can be one of the following: active | no-permission | topic-not-exist 
                  * The status "no-permission" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created. 
                - **SubscriptionCreationTime** *(datetime) --* 
                  The date and time the Amazon Redshift event notification subscription was created.
                - **SourceType** *(string) --* 
                  The source type of the events returned the Amazon Redshift event notification, such as cluster, or cluster-snapshot.
                - **SourceIdsList** *(list) --* 
                  A list of the sources that publish events to the Amazon Redshift event notification subscription.
                  - *(string) --* 
                - **EventCategoriesList** *(list) --* 
                  The list of Amazon Redshift event categories specified in the event notification subscription.
                  Values: Configuration, Management, Monitoring, Security
                  - *(string) --* 
                - **Severity** *(string) --* 
                  The event severity specified in the Amazon Redshift event notification subscription.
                  Values: ERROR, INFO
                - **Enabled** *(boolean) --* 
                  A boolean value indicating whether the subscription is enabled; ``true`` indicates that the subscription is enabled.
                - **Tags** *(list) --* 
                  The list of tags for the event subscription.
                  - *(dict) --* 
                    A tag consisting of a name/value pair for a resource.
                    - **Key** *(string) --* 
                      The key, or name, for the resource tag.
                    - **Value** *(string) --* 
                      The value for the resource tag.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type SubscriptionName: string
        :param SubscriptionName:
          The name of the Amazon Redshift event notification subscription to be described.
        :type TagKeys: list
        :param TagKeys:
          A tag key or keys for which you want to return all matching event notification subscriptions that are associated with the specified key or keys. For example, suppose that you have subscriptions that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subscriptions that have either or both of these tag keys associated with them.
          - *(string) --*
        :type TagValues: list
        :param TagValues:
          A tag value or values for which you want to return all matching event notification subscriptions that are associated with the specified tag value or values. For example, suppose that you have subscriptions that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the subscriptions that have either or both of these tag values associated with them.
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


class DescribeEvents(Paginator):
    def paginate(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_events`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeEvents>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SourceIdentifier='string',
              SourceType='cluster'|'cluster-parameter-group'|'cluster-security-group'|'cluster-snapshot',
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
                        'SourceIdentifier': 'string',
                        'SourceType': 'cluster'|'cluster-parameter-group'|'cluster-security-group'|'cluster-snapshot',
                        'Message': 'string',
                        'EventCategories': [
                            'string',
                        ],
                        'Severity': 'string',
                        'Date': datetime(2015, 1, 1),
                        'EventId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Events** *(list) --* 
              A list of ``Event`` instances. 
              - *(dict) --* 
                Describes an event.
                - **SourceIdentifier** *(string) --* 
                  The identifier for the source of the event.
                - **SourceType** *(string) --* 
                  The source type for this event.
                - **Message** *(string) --* 
                  The text of this event.
                - **EventCategories** *(list) --* 
                  A list of the event categories.
                  Values: Configuration, Management, Monitoring, Security
                  - *(string) --* 
                - **Severity** *(string) --* 
                  The severity of the event.
                  Values: ERROR, INFO
                - **Date** *(datetime) --* 
                  The date and time of the event.
                - **EventId** *(string) --* 
                  The identifier of the event.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type SourceIdentifier: string
        :param SourceIdentifier:
          The identifier of the event source for which events will be returned. If this parameter is not specified, then all sources are included in the response.
          Constraints:
          If *SourceIdentifier* is supplied, *SourceType* must also be provided.
          * Specify a cluster identifier when *SourceType* is ``cluster`` .
          * Specify a cluster security group name when *SourceType* is ``cluster-security-group`` .
          * Specify a cluster parameter group name when *SourceType* is ``cluster-parameter-group`` .
          * Specify a cluster snapshot identifier when *SourceType* is ``cluster-snapshot`` .
        :type SourceType: string
        :param SourceType:
          The event source to retrieve events for. If no value is specified, all events are returned.
          Constraints:
          If *SourceType* is supplied, *SourceIdentifier* must also be provided.
          * Specify ``cluster`` when *SourceIdentifier* is a cluster identifier.
          * Specify ``cluster-security-group`` when *SourceIdentifier* is a cluster security group name.
          * Specify ``cluster-parameter-group`` when *SourceIdentifier* is a cluster parameter group name.
          * Specify ``cluster-snapshot`` when *SourceIdentifier* is a cluster snapshot identifier.
        :type StartTime: datetime
        :param StartTime:
          The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the `ISO8601 Wikipedia page. <http://en.wikipedia.org/wiki/ISO_8601>`__
          Example: ``2009-07-08T18:00Z``
        :type EndTime: datetime
        :param EndTime:
          The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the `ISO8601 Wikipedia page. <http://en.wikipedia.org/wiki/ISO_8601>`__
          Example: ``2009-07-08T18:00Z``
        :type Duration: integer
        :param Duration:
          The number of minutes prior to the time of the request for which to retrieve events. For example, if the request is sent at 18:00 and you specify a duration of 60, then only events which have occurred after 17:00 will be returned.
          Default: ``60``
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


class DescribeHsmClientCertificates(Paginator):
    def paginate(self, HsmClientCertificateIdentifier: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_hsm_client_certificates`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeHsmClientCertificates>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              HsmClientCertificateIdentifier='string',
              TagKeys=[
                  'string',
              ],
              TagValues=[
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
                'HsmClientCertificates': [
                    {
                        'HsmClientCertificateIdentifier': 'string',
                        'HsmClientCertificatePublicKey': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **HsmClientCertificates** *(list) --* 
              A list of the identifiers for one or more HSM client certificates used by Amazon Redshift clusters to store and retrieve database encryption keys in an HSM.
              - *(dict) --* 
                Returns information about an HSM client certificate. The certificate is stored in a secure Hardware Storage Module (HSM), and used by the Amazon Redshift cluster to encrypt data files.
                - **HsmClientCertificateIdentifier** *(string) --* 
                  The identifier of the HSM client certificate.
                - **HsmClientCertificatePublicKey** *(string) --* 
                  The public key that the Amazon Redshift cluster will use to connect to the HSM. You must register the public key in the HSM.
                - **Tags** *(list) --* 
                  The list of tags for the HSM client certificate.
                  - *(dict) --* 
                    A tag consisting of a name/value pair for a resource.
                    - **Key** *(string) --* 
                      The key, or name, for the resource tag.
                    - **Value** *(string) --* 
                      The value for the resource tag.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type HsmClientCertificateIdentifier: string
        :param HsmClientCertificateIdentifier:
          The identifier of a specific HSM client certificate for which you want information. If no identifier is specified, information is returned for all HSM client certificates owned by your AWS customer account.
        :type TagKeys: list
        :param TagKeys:
          A tag key or keys for which you want to return all matching HSM client certificates that are associated with the specified key or keys. For example, suppose that you have HSM client certificates that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM client certificates that have either or both of these tag keys associated with them.
          - *(string) --*
        :type TagValues: list
        :param TagValues:
          A tag value or values for which you want to return all matching HSM client certificates that are associated with the specified tag value or values. For example, suppose that you have HSM client certificates that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM client certificates that have either or both of these tag values associated with them.
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


class DescribeHsmConfigurations(Paginator):
    def paginate(self, HsmConfigurationIdentifier: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_hsm_configurations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeHsmConfigurations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              HsmConfigurationIdentifier='string',
              TagKeys=[
                  'string',
              ],
              TagValues=[
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
                'HsmConfigurations': [
                    {
                        'HsmConfigurationIdentifier': 'string',
                        'Description': 'string',
                        'HsmIpAddress': 'string',
                        'HsmPartitionName': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **HsmConfigurations** *(list) --* 
              A list of ``HsmConfiguration`` objects.
              - *(dict) --* 
                Returns information about an HSM configuration, which is an object that describes to Amazon Redshift clusters the information they require to connect to an HSM where they can store database encryption keys.
                - **HsmConfigurationIdentifier** *(string) --* 
                  The name of the Amazon Redshift HSM configuration.
                - **Description** *(string) --* 
                  A text description of the HSM configuration.
                - **HsmIpAddress** *(string) --* 
                  The IP address that the Amazon Redshift cluster must use to access the HSM.
                - **HsmPartitionName** *(string) --* 
                  The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.
                - **Tags** *(list) --* 
                  The list of tags for the HSM configuration.
                  - *(dict) --* 
                    A tag consisting of a name/value pair for a resource.
                    - **Key** *(string) --* 
                      The key, or name, for the resource tag.
                    - **Value** *(string) --* 
                      The value for the resource tag.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type HsmConfigurationIdentifier: string
        :param HsmConfigurationIdentifier:
          The identifier of a specific Amazon Redshift HSM configuration to be described. If no identifier is specified, information is returned for all HSM configurations owned by your AWS customer account.
        :type TagKeys: list
        :param TagKeys:
          A tag key or keys for which you want to return all matching HSM configurations that are associated with the specified key or keys. For example, suppose that you have HSM configurations that are tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag keys associated with them.
          - *(string) --*
        :type TagValues: list
        :param TagValues:
          A tag value or values for which you want to return all matching HSM configurations that are associated with the specified tag value or values. For example, suppose that you have HSM configurations that are tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag values associated with them.
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


class DescribeOrderableClusterOptions(Paginator):
    def paginate(self, ClusterVersion: str = None, NodeType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_orderable_cluster_options`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeOrderableClusterOptions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClusterVersion='string',
              NodeType='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'OrderableClusterOptions': [
                    {
                        'ClusterVersion': 'string',
                        'ClusterType': 'string',
                        'NodeType': 'string',
                        'AvailabilityZones': [
                            {
                                'Name': 'string',
                                'SupportedPlatforms': [
                                    {
                                        'Name': 'string'
                                    },
                                ]
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output from the  DescribeOrderableClusterOptions action. 
            - **OrderableClusterOptions** *(list) --* 
              An ``OrderableClusterOption`` structure containing information about orderable options for the cluster.
              - *(dict) --* 
                Describes an orderable cluster option.
                - **ClusterVersion** *(string) --* 
                  The version of the orderable cluster.
                - **ClusterType** *(string) --* 
                  The cluster type, for example ``multi-node`` . 
                - **NodeType** *(string) --* 
                  The node type for the orderable cluster.
                - **AvailabilityZones** *(list) --* 
                  A list of availability zones for the orderable cluster.
                  - *(dict) --* 
                    Describes an availability zone.
                    - **Name** *(string) --* 
                      The name of the availability zone.
                    - **SupportedPlatforms** *(list) --* 
                      - *(dict) --* 
                        A list of supported platforms for orderable clusters.
                        - **Name** *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ClusterVersion: string
        :param ClusterVersion:
          The version filter value. Specify this parameter to show only the available offerings matching the specified version.
          Default: All versions.
          Constraints: Must be one of the version returned from  DescribeClusterVersions .
        :type NodeType: string
        :param NodeType:
          The node type filter value. Specify this parameter to show only the available offerings matching the specified node type.
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


class DescribeReservedNodeOfferings(Paginator):
    def paginate(self, ReservedNodeOfferingId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_reserved_node_offerings`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeReservedNodeOfferings>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ReservedNodeOfferingId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ReservedNodeOfferings': [
                    {
                        'ReservedNodeOfferingId': 'string',
                        'NodeType': 'string',
                        'Duration': 123,
                        'FixedPrice': 123.0,
                        'UsagePrice': 123.0,
                        'CurrencyCode': 'string',
                        'OfferingType': 'string',
                        'RecurringCharges': [
                            {
                                'RecurringChargeAmount': 123.0,
                                'RecurringChargeFrequency': 'string'
                            },
                        ],
                        'ReservedNodeOfferingType': 'Regular'|'Upgradable'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ReservedNodeOfferings** *(list) --* 
              A list of ``ReservedNodeOffering`` objects.
              - *(dict) --* 
                Describes a reserved node offering.
                - **ReservedNodeOfferingId** *(string) --* 
                  The offering identifier.
                - **NodeType** *(string) --* 
                  The node type offered by the reserved node offering.
                - **Duration** *(integer) --* 
                  The duration, in seconds, for which the offering will reserve the node.
                - **FixedPrice** *(float) --* 
                  The upfront fixed charge you will pay to purchase the specific reserved node offering.
                - **UsagePrice** *(float) --* 
                  The rate you are charged for each hour the cluster that is using the offering is running.
                - **CurrencyCode** *(string) --* 
                  The currency code for the compute nodes offering.
                - **OfferingType** *(string) --* 
                  The anticipated utilization of the reserved node, as defined in the reserved node offering.
                - **RecurringCharges** *(list) --* 
                  The charge to your account regardless of whether you are creating any clusters using the node offering. Recurring charges are only in effect for heavy-utilization reserved nodes.
                  - *(dict) --* 
                    Describes a recurring charge.
                    - **RecurringChargeAmount** *(float) --* 
                      The amount charged per the period of time specified by the recurring charge frequency.
                    - **RecurringChargeFrequency** *(string) --* 
                      The frequency at which the recurring charge amount is applied.
                - **ReservedNodeOfferingType** *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ReservedNodeOfferingId: string
        :param ReservedNodeOfferingId:
          The unique identifier for the offering.
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


class DescribeReservedNodes(Paginator):
    def paginate(self, ReservedNodeId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_reserved_nodes`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeReservedNodes>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ReservedNodeId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ReservedNodes': [
                    {
                        'ReservedNodeId': 'string',
                        'ReservedNodeOfferingId': 'string',
                        'NodeType': 'string',
                        'StartTime': datetime(2015, 1, 1),
                        'Duration': 123,
                        'FixedPrice': 123.0,
                        'UsagePrice': 123.0,
                        'CurrencyCode': 'string',
                        'NodeCount': 123,
                        'State': 'string',
                        'OfferingType': 'string',
                        'RecurringCharges': [
                            {
                                'RecurringChargeAmount': 123.0,
                                'RecurringChargeFrequency': 'string'
                            },
                        ],
                        'ReservedNodeOfferingType': 'Regular'|'Upgradable'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ReservedNodes** *(list) --* 
              The list of ``ReservedNode`` objects.
              - *(dict) --* 
                Describes a reserved node. You can call the  DescribeReservedNodeOfferings API to obtain the available reserved node offerings. 
                - **ReservedNodeId** *(string) --* 
                  The unique identifier for the reservation.
                - **ReservedNodeOfferingId** *(string) --* 
                  The identifier for the reserved node offering.
                - **NodeType** *(string) --* 
                  The node type of the reserved node.
                - **StartTime** *(datetime) --* 
                  The time the reservation started. You purchase a reserved node offering for a duration. This is the start time of that duration.
                - **Duration** *(integer) --* 
                  The duration of the node reservation in seconds.
                - **FixedPrice** *(float) --* 
                  The fixed cost Amazon Redshift charges you for this reserved node.
                - **UsagePrice** *(float) --* 
                  The hourly rate Amazon Redshift charges you for this reserved node.
                - **CurrencyCode** *(string) --* 
                  The currency code for the reserved cluster.
                - **NodeCount** *(integer) --* 
                  The number of reserved compute nodes.
                - **State** *(string) --* 
                  The state of the reserved compute node.
                  Possible Values:
                  * pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed. 
                  * active-This reserved node is owned by the caller and is available for use. 
                  * payment-failed-Payment failed for the purchase attempt. 
                  * retired-The reserved node is no longer available.  
                  * exchanging-The owner is exchanging the reserved node for another reserved node. 
                - **OfferingType** *(string) --* 
                  The anticipated utilization of the reserved node, as defined in the reserved node offering.
                - **RecurringCharges** *(list) --* 
                  The recurring charges for the reserved node.
                  - *(dict) --* 
                    Describes a recurring charge.
                    - **RecurringChargeAmount** *(float) --* 
                      The amount charged per the period of time specified by the recurring charge frequency.
                    - **RecurringChargeFrequency** *(string) --* 
                      The frequency at which the recurring charge amount is applied.
                - **ReservedNodeOfferingType** *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ReservedNodeId: string
        :param ReservedNodeId:
          Identifier for the node reservation.
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


class DescribeSnapshotCopyGrants(Paginator):
    def paginate(self, SnapshotCopyGrantName: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_snapshot_copy_grants`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeSnapshotCopyGrants>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SnapshotCopyGrantName='string',
              TagKeys=[
                  'string',
              ],
              TagValues=[
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
                'SnapshotCopyGrants': [
                    {
                        'SnapshotCopyGrantName': 'string',
                        'KmsKeyId': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SnapshotCopyGrants** *(list) --* 
              The list of ``SnapshotCopyGrant`` objects.
              - *(dict) --* 
                The snapshot copy grant that grants Amazon Redshift permission to encrypt copied snapshots with the specified customer master key (CMK) from AWS KMS in the destination region.
                For more information about managing snapshot copy grants, go to `Amazon Redshift Database Encryption <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html>`__ in the *Amazon Redshift Cluster Management Guide* . 
                - **SnapshotCopyGrantName** *(string) --* 
                  The name of the snapshot copy grant.
                - **KmsKeyId** *(string) --* 
                  The unique identifier of the customer master key (CMK) in AWS KMS to which Amazon Redshift is granted permission.
                - **Tags** *(list) --* 
                  A list of tag instances.
                  - *(dict) --* 
                    A tag consisting of a name/value pair for a resource.
                    - **Key** *(string) --* 
                      The key, or name, for the resource tag.
                    - **Value** *(string) --* 
                      The value for the resource tag.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type SnapshotCopyGrantName: string
        :param SnapshotCopyGrantName:
          The name of the snapshot copy grant.
        :type TagKeys: list
        :param TagKeys:
          A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.
          - *(string) --*
        :type TagValues: list
        :param TagValues:
          A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.
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


class DescribeSnapshotSchedules(Paginator):
    def paginate(self, ClusterIdentifier: str = None, ScheduleIdentifier: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_snapshot_schedules`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeSnapshotSchedules>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClusterIdentifier='string',
              ScheduleIdentifier='string',
              TagKeys=[
                  'string',
              ],
              TagValues=[
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
                'SnapshotSchedules': [
                    {
                        'ScheduleDefinitions': [
                            'string',
                        ],
                        'ScheduleIdentifier': 'string',
                        'ScheduleDescription': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'NextInvocations': [
                            datetime(2015, 1, 1),
                        ],
                        'AssociatedClusterCount': 123,
                        'AssociatedClusters': [
                            {
                                'ClusterIdentifier': 'string',
                                'ScheduleAssociationState': 'MODIFYING'|'ACTIVE'|'FAILED'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SnapshotSchedules** *(list) --* 
              A list of SnapshotSchedules.
              - *(dict) --* 
                Describes a snapshot schedule. You can set a regular interval for creating snapshots of a cluster. You can also schedule snapshots for specific dates. 
                - **ScheduleDefinitions** *(list) --* 
                  A list of ScheduleDefinitions.
                  - *(string) --* 
                - **ScheduleIdentifier** *(string) --* 
                  A unique identifier for the schedule.
                - **ScheduleDescription** *(string) --* 
                  The description of the schedule.
                - **Tags** *(list) --* 
                  An optional set of tags describing the schedule.
                  - *(dict) --* 
                    A tag consisting of a name/value pair for a resource.
                    - **Key** *(string) --* 
                      The key, or name, for the resource tag.
                    - **Value** *(string) --* 
                      The value for the resource tag.
                - **NextInvocations** *(list) --* 
                  - *(datetime) --* 
                - **AssociatedClusterCount** *(integer) --* 
                  The number of clusters associated with the schedule.
                - **AssociatedClusters** *(list) --* 
                  A list of clusters associated with the schedule. A maximum of 100 clusters is returned.
                  - *(dict) --* 
                    - **ClusterIdentifier** *(string) --* 
                    - **ScheduleAssociationState** *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ClusterIdentifier: string
        :param ClusterIdentifier:
          The unique identifier for the cluster whose snapshot schedules you want to view.
        :type ScheduleIdentifier: string
        :param ScheduleIdentifier:
          A unique identifier for a snapshot schedule.
        :type TagKeys: list
        :param TagKeys:
          The key value for a snapshot schedule tag.
          - *(string) --*
        :type TagValues: list
        :param TagValues:
          The value corresponding to the key of the snapshot schedule tag.
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


class DescribeTableRestoreStatus(Paginator):
    def paginate(self, ClusterIdentifier: str = None, TableRestoreRequestId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_table_restore_status`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeTableRestoreStatus>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ClusterIdentifier='string',
              TableRestoreRequestId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'TableRestoreStatusDetails': [
                    {
                        'TableRestoreRequestId': 'string',
                        'Status': 'PENDING'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'CANCELED',
                        'Message': 'string',
                        'RequestTime': datetime(2015, 1, 1),
                        'ProgressInMegaBytes': 123,
                        'TotalDataInMegaBytes': 123,
                        'ClusterIdentifier': 'string',
                        'SnapshotIdentifier': 'string',
                        'SourceDatabaseName': 'string',
                        'SourceSchemaName': 'string',
                        'SourceTableName': 'string',
                        'TargetDatabaseName': 'string',
                        'TargetSchemaName': 'string',
                        'NewTableName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TableRestoreStatusDetails** *(list) --* 
              A list of status details for one or more table restore requests.
              - *(dict) --* 
                Describes the status of a  RestoreTableFromClusterSnapshot operation.
                - **TableRestoreRequestId** *(string) --* 
                  The unique identifier for the table restore request.
                - **Status** *(string) --* 
                  A value that describes the current state of the table restore request.
                  Valid Values: ``SUCCEEDED`` , ``FAILED`` , ``CANCELED`` , ``PENDING`` , ``IN_PROGRESS``  
                - **Message** *(string) --* 
                  A description of the status of the table restore request. Status values include ``SUCCEEDED`` , ``FAILED`` , ``CANCELED`` , ``PENDING`` , ``IN_PROGRESS`` .
                - **RequestTime** *(datetime) --* 
                  The time that the table restore request was made, in Universal Coordinated Time (UTC).
                - **ProgressInMegaBytes** *(integer) --* 
                  The amount of data restored to the new table so far, in megabytes (MB).
                - **TotalDataInMegaBytes** *(integer) --* 
                  The total amount of data to restore to the new table, in megabytes (MB).
                - **ClusterIdentifier** *(string) --* 
                  The identifier of the Amazon Redshift cluster that the table is being restored to.
                - **SnapshotIdentifier** *(string) --* 
                  The identifier of the snapshot that the table is being restored from.
                - **SourceDatabaseName** *(string) --* 
                  The name of the source database that contains the table being restored.
                - **SourceSchemaName** *(string) --* 
                  The name of the source schema that contains the table being restored.
                - **SourceTableName** *(string) --* 
                  The name of the source table being restored.
                - **TargetDatabaseName** *(string) --* 
                  The name of the database to restore the table to.
                - **TargetSchemaName** *(string) --* 
                  The name of the schema to restore the table to.
                - **NewTableName** *(string) --* 
                  The name of the table to create as a result of the table restore request.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ClusterIdentifier: string
        :param ClusterIdentifier:
          The Amazon Redshift cluster that the table is being restored to.
        :type TableRestoreRequestId: string
        :param TableRestoreRequestId:
          The identifier of the table restore request to return status for. If you don\'t specify a ``TableRestoreRequestId`` value, then ``DescribeTableRestoreStatus`` returns the status of all in-progress table restore requests.
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
    def paginate(self, ResourceName: str = None, ResourceType: str = None, TagKeys: List = None, TagValues: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.describe_tags`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeTags>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ResourceName='string',
              ResourceType='string',
              TagKeys=[
                  'string',
              ],
              TagValues=[
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
                'TaggedResources': [
                    {
                        'Tag': {
                            'Key': 'string',
                            'Value': 'string'
                        },
                        'ResourceName': 'string',
                        'ResourceType': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TaggedResources** *(list) --* 
              A list of tags with their associated resources.
              - *(dict) --* 
                A tag and its associated resource.
                - **Tag** *(dict) --* 
                  The tag for the resource.
                  - **Key** *(string) --* 
                    The key, or name, for the resource tag.
                  - **Value** *(string) --* 
                    The value for the resource tag.
                - **ResourceName** *(string) --* 
                  The Amazon Resource Name (ARN) with which the tag is associated, for example: ``arn:aws:redshift:us-east-1:123456789:cluster:t1`` .
                - **ResourceType** *(string) --* 
                  The type of resource with which the tag is associated. Valid resource types are: 
                  * Cluster 
                  * CIDR/IP 
                  * EC2 security group 
                  * Snapshot 
                  * Cluster security group 
                  * Subnet group 
                  * HSM connection 
                  * HSM certificate 
                  * Parameter group 
                  For more information about Amazon Redshift resource types and constructing ARNs, go to `Constructing an Amazon Redshift Amazon Resource Name (ARN) <https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-iam-access-control-specify-actions>`__ in the Amazon Redshift Cluster Management Guide. 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ResourceName: string
        :param ResourceName:
          The Amazon Resource Name (ARN) for which you want to describe the tag or tags. For example, ``arn:aws:redshift:us-east-1:123456789:cluster:t1`` .
        :type ResourceType: string
        :param ResourceType:
          The type of resource with which you want to view tags. Valid resource types are:
          * Cluster
          * CIDR/IP
          * EC2 security group
          * Snapshot
          * Cluster security group
          * Subnet group
          * HSM connection
          * HSM certificate
          * Parameter group
          * Snapshot copy grant
          For more information about Amazon Redshift resource types and constructing ARNs, go to `Specifying Policy Elements\: Actions, Effects, Resources, and Principals <https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-iam-access-control-specify-actions>`__ in the Amazon Redshift Cluster Management Guide.
        :type TagKeys: list
        :param TagKeys:
          A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called ``owner`` and ``environment`` . If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.
          - *(string) --*
        :type TagValues: list
        :param TagValues:
          A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called ``admin`` and ``test`` . If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.
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


class GetReservedNodeExchangeOfferings(Paginator):
    def paginate(self, ReservedNodeId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Redshift.Client.get_reserved_node_exchange_offerings`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/GetReservedNodeExchangeOfferings>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ReservedNodeId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ReservedNodeOfferings': [
                    {
                        'ReservedNodeOfferingId': 'string',
                        'NodeType': 'string',
                        'Duration': 123,
                        'FixedPrice': 123.0,
                        'UsagePrice': 123.0,
                        'CurrencyCode': 'string',
                        'OfferingType': 'string',
                        'RecurringCharges': [
                            {
                                'RecurringChargeAmount': 123.0,
                                'RecurringChargeFrequency': 'string'
                            },
                        ],
                        'ReservedNodeOfferingType': 'Regular'|'Upgradable'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ReservedNodeOfferings** *(list) --* 
              Returns an array of  ReservedNodeOffering objects.
              - *(dict) --* 
                Describes a reserved node offering.
                - **ReservedNodeOfferingId** *(string) --* 
                  The offering identifier.
                - **NodeType** *(string) --* 
                  The node type offered by the reserved node offering.
                - **Duration** *(integer) --* 
                  The duration, in seconds, for which the offering will reserve the node.
                - **FixedPrice** *(float) --* 
                  The upfront fixed charge you will pay to purchase the specific reserved node offering.
                - **UsagePrice** *(float) --* 
                  The rate you are charged for each hour the cluster that is using the offering is running.
                - **CurrencyCode** *(string) --* 
                  The currency code for the compute nodes offering.
                - **OfferingType** *(string) --* 
                  The anticipated utilization of the reserved node, as defined in the reserved node offering.
                - **RecurringCharges** *(list) --* 
                  The charge to your account regardless of whether you are creating any clusters using the node offering. Recurring charges are only in effect for heavy-utilization reserved nodes.
                  - *(dict) --* 
                    Describes a recurring charge.
                    - **RecurringChargeAmount** *(float) --* 
                      The amount charged per the period of time specified by the recurring charge frequency.
                    - **RecurringChargeFrequency** *(string) --* 
                      The frequency at which the recurring charge amount is applied.
                - **ReservedNodeOfferingType** *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ReservedNodeId: string
        :param ReservedNodeId: **[REQUIRED]**
          A string representing the node identifier for the DC1 Reserved Node to be exchanged.
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
