from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class DescribeDBClusterParameterGroups(Paginator):
    def paginate(self, DBClusterParameterGroupName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Neptune.Client.describe_db_cluster_parameter_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBClusterParameterGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DBClusterParameterGroupName='string',
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
                'DBClusterParameterGroups': [
                    {
                        'DBClusterParameterGroupName': 'string',
                        'DBParameterGroupFamily': 'string',
                        'Description': 'string',
                        'DBClusterParameterGroupArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBClusterParameterGroups** *(list) --* 
              A list of DB cluster parameter groups.
              - *(dict) --* 
                Contains the details of an Amazon Neptune DB cluster parameter group.
                This data type is used as a response element in the  DescribeDBClusterParameterGroups action.
                - **DBClusterParameterGroupName** *(string) --* 
                  Provides the name of the DB cluster parameter group.
                - **DBParameterGroupFamily** *(string) --* 
                  Provides the name of the DB parameter group family that this DB cluster parameter group is compatible with.
                - **Description** *(string) --* 
                  Provides the customer-specified description for this DB cluster parameter group.
                - **DBClusterParameterGroupArn** *(string) --* 
                  The Amazon Resource Name (ARN) for the DB cluster parameter group.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type DBClusterParameterGroupName: string
        :param DBClusterParameterGroupName:
          The name of a specific DB cluster parameter group to return details for.
          Constraints:
          * If supplied, must match the name of an existing DBClusterParameterGroup.
        :type Filters: list
        :param Filters:
          This parameter is not currently supported.
          - *(dict) --*
            This type is not currently supported.
            - **Name** *(string) --* **[REQUIRED]**
              This parameter is not currently supported.
            - **Values** *(list) --* **[REQUIRED]**
              This parameter is not currently supported.
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


class DescribeDBClusterParameters(Paginator):
    def paginate(self, DBClusterParameterGroupName: str, Source: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Neptune.Client.describe_db_cluster_parameters`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBClusterParameters>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DBClusterParameterGroupName='string',
              Source='string',
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
                'Parameters': [
                    {
                        'ParameterName': 'string',
                        'ParameterValue': 'string',
                        'Description': 'string',
                        'Source': 'string',
                        'ApplyType': 'string',
                        'DataType': 'string',
                        'AllowedValues': 'string',
                        'IsModifiable': True|False,
                        'MinimumEngineVersion': 'string',
                        'ApplyMethod': 'immediate'|'pending-reboot'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Parameters** *(list) --* 
              Provides a list of parameters for the DB cluster parameter group.
              - *(dict) --* 
                Specifies a parameter.
                - **ParameterName** *(string) --* 
                  Specifies the name of the parameter.
                - **ParameterValue** *(string) --* 
                  Specifies the value of the parameter.
                - **Description** *(string) --* 
                  Provides a description of the parameter.
                - **Source** *(string) --* 
                  Indicates the source of the parameter value.
                - **ApplyType** *(string) --* 
                  Specifies the engine specific parameters type.
                - **DataType** *(string) --* 
                  Specifies the valid data type for the parameter.
                - **AllowedValues** *(string) --* 
                  Specifies the valid range of values for the parameter.
                - **IsModifiable** *(boolean) --* 
                  Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
                - **MinimumEngineVersion** *(string) --* 
                  The earliest engine version to which the parameter can apply.
                - **ApplyMethod** *(string) --* 
                  Indicates when to apply parameter updates.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type DBClusterParameterGroupName: string
        :param DBClusterParameterGroupName: **[REQUIRED]**
          The name of a specific DB cluster parameter group to return parameter details for.
          Constraints:
          * If supplied, must match the name of an existing DBClusterParameterGroup.
        :type Source: string
        :param Source:
          A value that indicates to return only parameters for a specific source. Parameter sources can be ``engine`` , ``service`` , or ``customer`` .
        :type Filters: list
        :param Filters:
          This parameter is not currently supported.
          - *(dict) --*
            This type is not currently supported.
            - **Name** *(string) --* **[REQUIRED]**
              This parameter is not currently supported.
            - **Values** *(list) --* **[REQUIRED]**
              This parameter is not currently supported.
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


class DescribeDBClusterSnapshots(Paginator):
    def paginate(self, DBClusterIdentifier: str = None, DBClusterSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, IncludeShared: bool = None, IncludePublic: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Neptune.Client.describe_db_cluster_snapshots`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBClusterSnapshots>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DBClusterIdentifier='string',
              DBClusterSnapshotIdentifier='string',
              SnapshotType='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              IncludeShared=True|False,
              IncludePublic=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'DBClusterSnapshots': [
                    {
                        'AvailabilityZones': [
                            'string',
                        ],
                        'DBClusterSnapshotIdentifier': 'string',
                        'DBClusterIdentifier': 'string',
                        'SnapshotCreateTime': datetime(2015, 1, 1),
                        'Engine': 'string',
                        'AllocatedStorage': 123,
                        'Status': 'string',
                        'Port': 123,
                        'VpcId': 'string',
                        'ClusterCreateTime': datetime(2015, 1, 1),
                        'MasterUsername': 'string',
                        'EngineVersion': 'string',
                        'LicenseModel': 'string',
                        'SnapshotType': 'string',
                        'PercentProgress': 123,
                        'StorageEncrypted': True|False,
                        'KmsKeyId': 'string',
                        'DBClusterSnapshotArn': 'string',
                        'SourceDBClusterSnapshotArn': 'string',
                        'IAMDatabaseAuthenticationEnabled': True|False
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBClusterSnapshots** *(list) --* 
              Provides a list of DB cluster snapshots for the user.
              - *(dict) --* 
                Contains the details for an Amazon Neptune DB cluster snapshot
                This data type is used as a response element in the  DescribeDBClusterSnapshots action.
                - **AvailabilityZones** *(list) --* 
                  Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.
                  - *(string) --* 
                - **DBClusterSnapshotIdentifier** *(string) --* 
                  Specifies the identifier for the DB cluster snapshot.
                - **DBClusterIdentifier** *(string) --* 
                  Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.
                - **SnapshotCreateTime** *(datetime) --* 
                  Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).
                - **Engine** *(string) --* 
                  Specifies the name of the database engine.
                - **AllocatedStorage** *(integer) --* 
                  Specifies the allocated storage size in gibibytes (GiB).
                - **Status** *(string) --* 
                  Specifies the status of this DB cluster snapshot.
                - **Port** *(integer) --* 
                  Specifies the port that the DB cluster was listening on at the time of the snapshot.
                - **VpcId** *(string) --* 
                  Provides the VPC ID associated with the DB cluster snapshot.
                - **ClusterCreateTime** *(datetime) --* 
                  Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).
                - **MasterUsername** *(string) --* 
                  Provides the master username for the DB cluster snapshot.
                - **EngineVersion** *(string) --* 
                  Provides the version of the database engine for this DB cluster snapshot.
                - **LicenseModel** *(string) --* 
                  Provides the license model information for this DB cluster snapshot.
                - **SnapshotType** *(string) --* 
                  Provides the type of the DB cluster snapshot.
                - **PercentProgress** *(integer) --* 
                  Specifies the percentage of the estimated data that has been transferred.
                - **StorageEncrypted** *(boolean) --* 
                  Specifies whether the DB cluster snapshot is encrypted.
                - **KmsKeyId** *(string) --* 
                  If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.
                - **DBClusterSnapshotArn** *(string) --* 
                  The Amazon Resource Name (ARN) for the DB cluster snapshot.
                - **SourceDBClusterSnapshotArn** *(string) --* 
                  If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.
                - **IAMDatabaseAuthenticationEnabled** *(boolean) --* 
                  True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier:
          The ID of the DB cluster to retrieve the list of DB cluster snapshots for. This parameter can\'t be used in conjunction with the ``DBClusterSnapshotIdentifier`` parameter. This parameter is not case-sensitive.
          Constraints:
          * If supplied, must match the identifier of an existing DBCluster.
        :type DBClusterSnapshotIdentifier: string
        :param DBClusterSnapshotIdentifier:
          A specific DB cluster snapshot identifier to describe. This parameter can\'t be used in conjunction with the ``DBClusterIdentifier`` parameter. This value is stored as a lowercase string.
          Constraints:
          * If supplied, must match the identifier of an existing DBClusterSnapshot.
          * If this identifier is for an automated snapshot, the ``SnapshotType`` parameter must also be specified.
        :type SnapshotType: string
        :param SnapshotType:
          The type of DB cluster snapshots to be returned. You can specify one of the following values:
          * ``automated`` - Return all DB cluster snapshots that have been automatically taken by Amazon Neptune for my AWS account.
          * ``manual`` - Return all DB cluster snapshots that have been taken by my AWS account.
          * ``shared`` - Return all manual DB cluster snapshots that have been shared to my AWS account.
          * ``public`` - Return all DB cluster snapshots that have been marked as public.
          If you don\'t specify a ``SnapshotType`` value, then both automated and manual DB cluster snapshots are returned. You can include shared DB cluster snapshots with these results by setting the ``IncludeShared`` parameter to ``true`` . You can include public DB cluster snapshots with these results by setting the ``IncludePublic`` parameter to ``true`` .
          The ``IncludeShared`` and ``IncludePublic`` parameters don\'t apply for ``SnapshotType`` values of ``manual`` or ``automated`` . The ``IncludePublic`` parameter doesn\'t apply when ``SnapshotType`` is set to ``shared`` . The ``IncludeShared`` parameter doesn\'t apply when ``SnapshotType`` is set to ``public`` .
        :type Filters: list
        :param Filters:
          This parameter is not currently supported.
          - *(dict) --*
            This type is not currently supported.
            - **Name** *(string) --* **[REQUIRED]**
              This parameter is not currently supported.
            - **Values** *(list) --* **[REQUIRED]**
              This parameter is not currently supported.
              - *(string) --*
        :type IncludeShared: boolean
        :param IncludeShared:
          True to include shared manual DB cluster snapshots from other AWS accounts that this AWS account has been given permission to copy or restore, and otherwise false. The default is ``false`` .
          You can give an AWS account permission to restore a manual DB cluster snapshot from another AWS account by the  ModifyDBClusterSnapshotAttribute API action.
        :type IncludePublic: boolean
        :param IncludePublic:
          True to include manual DB cluster snapshots that are public and can be copied or restored by any AWS account, and otherwise false. The default is ``false`` . The default is false.
          You can share a manual DB cluster snapshot as public by using the  ModifyDBClusterSnapshotAttribute API action.
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


class DescribeDBClusters(Paginator):
    def paginate(self, DBClusterIdentifier: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Neptune.Client.describe_db_clusters`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBClusters>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DBClusterIdentifier='string',
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
                'DBClusters': [
                    {
                        'AllocatedStorage': 123,
                        'AvailabilityZones': [
                            'string',
                        ],
                        'BackupRetentionPeriod': 123,
                        'CharacterSetName': 'string',
                        'DatabaseName': 'string',
                        'DBClusterIdentifier': 'string',
                        'DBClusterParameterGroup': 'string',
                        'DBSubnetGroup': 'string',
                        'Status': 'string',
                        'PercentProgress': 'string',
                        'EarliestRestorableTime': datetime(2015, 1, 1),
                        'Endpoint': 'string',
                        'ReaderEndpoint': 'string',
                        'MultiAZ': True|False,
                        'Engine': 'string',
                        'EngineVersion': 'string',
                        'LatestRestorableTime': datetime(2015, 1, 1),
                        'Port': 123,
                        'MasterUsername': 'string',
                        'DBClusterOptionGroupMemberships': [
                            {
                                'DBClusterOptionGroupName': 'string',
                                'Status': 'string'
                            },
                        ],
                        'PreferredBackupWindow': 'string',
                        'PreferredMaintenanceWindow': 'string',
                        'ReplicationSourceIdentifier': 'string',
                        'ReadReplicaIdentifiers': [
                            'string',
                        ],
                        'DBClusterMembers': [
                            {
                                'DBInstanceIdentifier': 'string',
                                'IsClusterWriter': True|False,
                                'DBClusterParameterGroupStatus': 'string',
                                'PromotionTier': 123
                            },
                        ],
                        'VpcSecurityGroups': [
                            {
                                'VpcSecurityGroupId': 'string',
                                'Status': 'string'
                            },
                        ],
                        'HostedZoneId': 'string',
                        'StorageEncrypted': True|False,
                        'KmsKeyId': 'string',
                        'DbClusterResourceId': 'string',
                        'DBClusterArn': 'string',
                        'AssociatedRoles': [
                            {
                                'RoleArn': 'string',
                                'Status': 'string'
                            },
                        ],
                        'IAMDatabaseAuthenticationEnabled': True|False,
                        'CloneGroupId': 'string',
                        'ClusterCreateTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBClusters** *(list) --* 
              Contains a list of DB clusters for the user.
              - *(dict) --* 
                Contains the details of an Amazon Neptune DB cluster.
                This data type is used as a response element in the  DescribeDBClusters action.
                - **AllocatedStorage** *(integer) --* 
                   ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not fixed, but instead automatically adjusts as needed.
                - **AvailabilityZones** *(list) --* 
                  Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.
                  - *(string) --* 
                - **BackupRetentionPeriod** *(integer) --* 
                  Specifies the number of days for which automatic DB snapshots are retained.
                - **CharacterSetName** *(string) --* 
                  If present, specifies the name of the character set that this cluster is associated with.
                - **DatabaseName** *(string) --* 
                  Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.
                - **DBClusterIdentifier** *(string) --* 
                  Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.
                - **DBClusterParameterGroup** *(string) --* 
                  Specifies the name of the DB cluster parameter group for the DB cluster.
                - **DBSubnetGroup** *(string) --* 
                  Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.
                - **Status** *(string) --* 
                  Specifies the current state of this DB cluster.
                - **PercentProgress** *(string) --* 
                  Specifies the progress of the operation as a percentage.
                - **EarliestRestorableTime** *(datetime) --* 
                  Specifies the earliest time to which a database can be restored with point-in-time restore.
                - **Endpoint** *(string) --* 
                  Specifies the connection endpoint for the primary instance of the DB cluster.
                - **ReaderEndpoint** *(string) --* 
                  The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Read Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Neptune distributes the connection requests among the Read Replicas in the DB cluster. This functionality can help balance your read workload across multiple Read Replicas in your DB cluster.
                  If a failover occurs, and the Read Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.
                - **MultiAZ** *(boolean) --* 
                  Specifies whether the DB cluster has instances in multiple Availability Zones.
                - **Engine** *(string) --* 
                  Provides the name of the database engine to be used for this DB cluster.
                - **EngineVersion** *(string) --* 
                  Indicates the database engine version.
                - **LatestRestorableTime** *(datetime) --* 
                  Specifies the latest time to which a database can be restored with point-in-time restore.
                - **Port** *(integer) --* 
                  Specifies the port that the database engine is listening on.
                - **MasterUsername** *(string) --* 
                  Contains the master username for the DB cluster.
                - **DBClusterOptionGroupMemberships** *(list) --* 
                  Provides the list of option group memberships for this DB cluster.
                  - *(dict) --* 
                    Contains status information for a DB cluster option group.
                    - **DBClusterOptionGroupName** *(string) --* 
                      Specifies the name of the DB cluster option group.
                    - **Status** *(string) --* 
                      Specifies the status of the DB cluster option group.
                - **PreferredBackupWindow** *(string) --* 
                  Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the ``BackupRetentionPeriod`` .
                - **PreferredMaintenanceWindow** *(string) --* 
                  Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
                - **ReplicationSourceIdentifier** *(string) --* 
                  Not supported by Neptune.
                - **ReadReplicaIdentifiers** *(list) --* 
                  Contains one or more identifiers of the Read Replicas associated with this DB cluster.
                  - *(string) --* 
                - **DBClusterMembers** *(list) --* 
                  Provides the list of instances that make up the DB cluster.
                  - *(dict) --* 
                    Contains information about an instance that is part of a DB cluster.
                    - **DBInstanceIdentifier** *(string) --* 
                      Specifies the instance identifier for this member of the DB cluster.
                    - **IsClusterWriter** *(boolean) --* 
                      Value that is ``true`` if the cluster member is the primary instance for the DB cluster and ``false`` otherwise.
                    - **DBClusterParameterGroupStatus** *(string) --* 
                      Specifies the status of the DB cluster parameter group for this member of the DB cluster.
                    - **PromotionTier** *(integer) --* 
                      A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.
                - **VpcSecurityGroups** *(list) --* 
                  Provides a list of VPC security groups that the DB cluster belongs to.
                  - *(dict) --* 
                    This data type is used as a response element for queries on VPC security group membership.
                    - **VpcSecurityGroupId** *(string) --* 
                      The name of the VPC security group.
                    - **Status** *(string) --* 
                      The status of the VPC security group.
                - **HostedZoneId** *(string) --* 
                  Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
                - **StorageEncrypted** *(boolean) --* 
                  Specifies whether the DB cluster is encrypted.
                - **KmsKeyId** *(string) --* 
                  If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.
                - **DbClusterResourceId** *(string) --* 
                  The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.
                - **DBClusterArn** *(string) --* 
                  The Amazon Resource Name (ARN) for the DB cluster.
                - **AssociatedRoles** *(list) --* 
                  Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.
                  - *(dict) --* 
                    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB cluster.
                    - **RoleArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.
                    - **Status** *(string) --* 
                      Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:
                      * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf. 
                      * ``PENDING`` - the IAM role ARN is being associated with the DB cluster. 
                      * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other AWS services on your behalf. 
                - **IAMDatabaseAuthenticationEnabled** *(boolean) --* 
                  True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.
                - **CloneGroupId** *(string) --* 
                  Identifies the clone group to which the DB cluster is associated.
                - **ClusterCreateTime** *(datetime) --* 
                  Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier:
          The user-supplied DB cluster identifier. If this parameter is specified, information from only the specific DB cluster is returned. This parameter isn\'t case-sensitive.
          Constraints:
          * If supplied, must match an existing DBClusterIdentifier.
        :type Filters: list
        :param Filters:
          A filter that specifies one or more DB clusters to describe.
          Supported filters:
          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB clusters identified by these ARNs.
          - *(dict) --*
            This type is not currently supported.
            - **Name** *(string) --* **[REQUIRED]**
              This parameter is not currently supported.
            - **Values** *(list) --* **[REQUIRED]**
              This parameter is not currently supported.
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


class DescribeDBEngineVersions(Paginator):
    def paginate(self, Engine: str = None, EngineVersion: str = None, DBParameterGroupFamily: str = None, Filters: List = None, DefaultOnly: bool = None, ListSupportedCharacterSets: bool = None, ListSupportedTimezones: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Neptune.Client.describe_db_engine_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBEngineVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Engine='string',
              EngineVersion='string',
              DBParameterGroupFamily='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              DefaultOnly=True|False,
              ListSupportedCharacterSets=True|False,
              ListSupportedTimezones=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'DBEngineVersions': [
                    {
                        'Engine': 'string',
                        'EngineVersion': 'string',
                        'DBParameterGroupFamily': 'string',
                        'DBEngineDescription': 'string',
                        'DBEngineVersionDescription': 'string',
                        'DefaultCharacterSet': {
                            'CharacterSetName': 'string',
                            'CharacterSetDescription': 'string'
                        },
                        'SupportedCharacterSets': [
                            {
                                'CharacterSetName': 'string',
                                'CharacterSetDescription': 'string'
                            },
                        ],
                        'ValidUpgradeTarget': [
                            {
                                'Engine': 'string',
                                'EngineVersion': 'string',
                                'Description': 'string',
                                'AutoUpgrade': True|False,
                                'IsMajorVersionUpgrade': True|False
                            },
                        ],
                        'SupportedTimezones': [
                            {
                                'TimezoneName': 'string'
                            },
                        ],
                        'ExportableLogTypes': [
                            'string',
                        ],
                        'SupportsLogExportsToCloudwatchLogs': True|False,
                        'SupportsReadReplica': True|False
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBEngineVersions** *(list) --* 
              A list of ``DBEngineVersion`` elements.
              - *(dict) --* 
                This data type is used as a response element in the action  DescribeDBEngineVersions .
                - **Engine** *(string) --* 
                  The name of the database engine.
                - **EngineVersion** *(string) --* 
                  The version number of the database engine.
                - **DBParameterGroupFamily** *(string) --* 
                  The name of the DB parameter group family for the database engine.
                - **DBEngineDescription** *(string) --* 
                  The description of the database engine.
                - **DBEngineVersionDescription** *(string) --* 
                  The description of the database engine version.
                - **DefaultCharacterSet** *(dict) --* 
                  The default character set for new instances of this engine version, if the ``CharacterSetName`` parameter of the CreateDBInstance API is not specified.
                  - **CharacterSetName** *(string) --* 
                    The name of the character set.
                  - **CharacterSetDescription** *(string) --* 
                    The description of the character set.
                - **SupportedCharacterSets** *(list) --* 
                  A list of the character sets supported by this engine for the ``CharacterSetName`` parameter of the ``CreateDBInstance`` action.
                  - *(dict) --* 
                    Specifies a character set.
                    - **CharacterSetName** *(string) --* 
                      The name of the character set.
                    - **CharacterSetDescription** *(string) --* 
                      The description of the character set.
                - **ValidUpgradeTarget** *(list) --* 
                  A list of engine versions that this database engine version can be upgraded to.
                  - *(dict) --* 
                    The version of the database engine that a DB instance can be upgraded to.
                    - **Engine** *(string) --* 
                      The name of the upgrade target database engine.
                    - **EngineVersion** *(string) --* 
                      The version number of the upgrade target database engine.
                    - **Description** *(string) --* 
                      The version of the database engine that a DB instance can be upgraded to.
                    - **AutoUpgrade** *(boolean) --* 
                      A value that indicates whether the target version is applied to any source DB instances that have AutoMinorVersionUpgrade set to true.
                    - **IsMajorVersionUpgrade** *(boolean) --* 
                      A value that indicates whether a database engine is upgraded to a major version.
                - **SupportedTimezones** *(list) --* 
                  A list of the time zones supported by this engine for the ``Timezone`` parameter of the ``CreateDBInstance`` action.
                  - *(dict) --* 
                    A time zone associated with a  DBInstance .
                    - **TimezoneName** *(string) --* 
                      The name of the time zone.
                - **ExportableLogTypes** *(list) --* 
                  The types of logs that the database engine has available for export to CloudWatch Logs.
                  - *(string) --* 
                - **SupportsLogExportsToCloudwatchLogs** *(boolean) --* 
                  A value that indicates whether the engine version supports exporting the log types specified by ExportableLogTypes to CloudWatch Logs.
                - **SupportsReadReplica** *(boolean) --* 
                  Indicates whether the database engine version supports read replicas.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type Engine: string
        :param Engine:
          The database engine to return.
        :type EngineVersion: string
        :param EngineVersion:
          The database engine version to return.
          Example: ``5.1.49``
        :type DBParameterGroupFamily: string
        :param DBParameterGroupFamily:
          The name of a specific DB parameter group family to return details for.
          Constraints:
          * If supplied, must match an existing DBParameterGroupFamily.
        :type Filters: list
        :param Filters:
          Not currently supported.
          - *(dict) --*
            This type is not currently supported.
            - **Name** *(string) --* **[REQUIRED]**
              This parameter is not currently supported.
            - **Values** *(list) --* **[REQUIRED]**
              This parameter is not currently supported.
              - *(string) --*
        :type DefaultOnly: boolean
        :param DefaultOnly:
          Indicates that only the default version of the specified engine or engine and major version combination is returned.
        :type ListSupportedCharacterSets: boolean
        :param ListSupportedCharacterSets:
          If this parameter is specified and the requested engine supports the ``CharacterSetName`` parameter for ``CreateDBInstance`` , the response includes a list of supported character sets for each engine version.
        :type ListSupportedTimezones: boolean
        :param ListSupportedTimezones:
          If this parameter is specified and the requested engine supports the ``TimeZone`` parameter for ``CreateDBInstance`` , the response includes a list of supported time zones for each engine version.
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


class DescribeDBInstances(Paginator):
    def paginate(self, DBInstanceIdentifier: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Neptune.Client.describe_db_instances`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBInstances>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DBInstanceIdentifier='string',
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
                'DBInstances': [
                    {
                        'DBInstanceIdentifier': 'string',
                        'DBInstanceClass': 'string',
                        'Engine': 'string',
                        'DBInstanceStatus': 'string',
                        'MasterUsername': 'string',
                        'DBName': 'string',
                        'Endpoint': {
                            'Address': 'string',
                            'Port': 123,
                            'HostedZoneId': 'string'
                        },
                        'AllocatedStorage': 123,
                        'InstanceCreateTime': datetime(2015, 1, 1),
                        'PreferredBackupWindow': 'string',
                        'BackupRetentionPeriod': 123,
                        'DBSecurityGroups': [
                            {
                                'DBSecurityGroupName': 'string',
                                'Status': 'string'
                            },
                        ],
                        'VpcSecurityGroups': [
                            {
                                'VpcSecurityGroupId': 'string',
                                'Status': 'string'
                            },
                        ],
                        'DBParameterGroups': [
                            {
                                'DBParameterGroupName': 'string',
                                'ParameterApplyStatus': 'string'
                            },
                        ],
                        'AvailabilityZone': 'string',
                        'DBSubnetGroup': {
                            'DBSubnetGroupName': 'string',
                            'DBSubnetGroupDescription': 'string',
                            'VpcId': 'string',
                            'SubnetGroupStatus': 'string',
                            'Subnets': [
                                {
                                    'SubnetIdentifier': 'string',
                                    'SubnetAvailabilityZone': {
                                        'Name': 'string'
                                    },
                                    'SubnetStatus': 'string'
                                },
                            ],
                            'DBSubnetGroupArn': 'string'
                        },
                        'PreferredMaintenanceWindow': 'string',
                        'PendingModifiedValues': {
                            'DBInstanceClass': 'string',
                            'AllocatedStorage': 123,
                            'MasterUserPassword': 'string',
                            'Port': 123,
                            'BackupRetentionPeriod': 123,
                            'MultiAZ': True|False,
                            'EngineVersion': 'string',
                            'LicenseModel': 'string',
                            'Iops': 123,
                            'DBInstanceIdentifier': 'string',
                            'StorageType': 'string',
                            'CACertificateIdentifier': 'string',
                            'DBSubnetGroupName': 'string',
                            'PendingCloudwatchLogsExports': {
                                'LogTypesToEnable': [
                                    'string',
                                ],
                                'LogTypesToDisable': [
                                    'string',
                                ]
                            }
                        },
                        'LatestRestorableTime': datetime(2015, 1, 1),
                        'MultiAZ': True|False,
                        'EngineVersion': 'string',
                        'AutoMinorVersionUpgrade': True|False,
                        'ReadReplicaSourceDBInstanceIdentifier': 'string',
                        'ReadReplicaDBInstanceIdentifiers': [
                            'string',
                        ],
                        'ReadReplicaDBClusterIdentifiers': [
                            'string',
                        ],
                        'LicenseModel': 'string',
                        'Iops': 123,
                        'OptionGroupMemberships': [
                            {
                                'OptionGroupName': 'string',
                                'Status': 'string'
                            },
                        ],
                        'CharacterSetName': 'string',
                        'SecondaryAvailabilityZone': 'string',
                        'PubliclyAccessible': True|False,
                        'StatusInfos': [
                            {
                                'StatusType': 'string',
                                'Normal': True|False,
                                'Status': 'string',
                                'Message': 'string'
                            },
                        ],
                        'StorageType': 'string',
                        'TdeCredentialArn': 'string',
                        'DbInstancePort': 123,
                        'DBClusterIdentifier': 'string',
                        'StorageEncrypted': True|False,
                        'KmsKeyId': 'string',
                        'DbiResourceId': 'string',
                        'CACertificateIdentifier': 'string',
                        'DomainMemberships': [
                            {
                                'Domain': 'string',
                                'Status': 'string',
                                'FQDN': 'string',
                                'IAMRoleName': 'string'
                            },
                        ],
                        'CopyTagsToSnapshot': True|False,
                        'MonitoringInterval': 123,
                        'EnhancedMonitoringResourceArn': 'string',
                        'MonitoringRoleArn': 'string',
                        'PromotionTier': 123,
                        'DBInstanceArn': 'string',
                        'Timezone': 'string',
                        'IAMDatabaseAuthenticationEnabled': True|False,
                        'PerformanceInsightsEnabled': True|False,
                        'PerformanceInsightsKMSKeyId': 'string',
                        'EnabledCloudwatchLogsExports': [
                            'string',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBInstances** *(list) --* 
              A list of  DBInstance instances.
              - *(dict) --* 
                Contains the details of an Amazon Neptune DB instance.
                This data type is used as a response element in the  DescribeDBInstances action.
                - **DBInstanceIdentifier** *(string) --* 
                  Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.
                - **DBInstanceClass** *(string) --* 
                  Contains the name of the compute and memory capacity class of the DB instance.
                - **Engine** *(string) --* 
                  Provides the name of the database engine to be used for this DB instance.
                - **DBInstanceStatus** *(string) --* 
                  Specifies the current state of this database.
                - **MasterUsername** *(string) --* 
                  Contains the master username for the DB instance.
                - **DBName** *(string) --* 
                  The database name.
                - **Endpoint** *(dict) --* 
                  Specifies the connection endpoint.
                  - **Address** *(string) --* 
                    Specifies the DNS address of the DB instance.
                  - **Port** *(integer) --* 
                    Specifies the port that the database engine is listening on.
                  - **HostedZoneId** *(string) --* 
                    Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
                - **AllocatedStorage** *(integer) --* 
                  Specifies the allocated storage size specified in gibibytes.
                - **InstanceCreateTime** *(datetime) --* 
                  Provides the date and time the DB instance was created.
                - **PreferredBackupWindow** *(string) --* 
                  Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the ``BackupRetentionPeriod`` .
                - **BackupRetentionPeriod** *(integer) --* 
                  Specifies the number of days for which automatic DB snapshots are retained.
                - **DBSecurityGroups** *(list) --* 
                  Provides List of DB security group elements containing only ``DBSecurityGroup.Name`` and ``DBSecurityGroup.Status`` subelements.
                  - *(dict) --* 
                    Specifies membership in a designated DB security group.
                    - **DBSecurityGroupName** *(string) --* 
                      The name of the DB security group.
                    - **Status** *(string) --* 
                      The status of the DB security group.
                - **VpcSecurityGroups** *(list) --* 
                  Provides a list of VPC security group elements that the DB instance belongs to.
                  - *(dict) --* 
                    This data type is used as a response element for queries on VPC security group membership.
                    - **VpcSecurityGroupId** *(string) --* 
                      The name of the VPC security group.
                    - **Status** *(string) --* 
                      The status of the VPC security group.
                - **DBParameterGroups** *(list) --* 
                  Provides the list of DB parameter groups applied to this DB instance.
                  - *(dict) --* 
                    The status of the DB parameter group.
                    This data type is used as a response element in the following actions:
                    *  CreateDBInstance   
                    *  DeleteDBInstance   
                    *  ModifyDBInstance   
                    *  RebootDBInstance   
                    - **DBParameterGroupName** *(string) --* 
                      The name of the DP parameter group.
                    - **ParameterApplyStatus** *(string) --* 
                      The status of parameter updates.
                - **AvailabilityZone** *(string) --* 
                  Specifies the name of the Availability Zone the DB instance is located in.
                - **DBSubnetGroup** *(dict) --* 
                  Specifies information on the subnet group associated with the DB instance, including the name, description, and subnets in the subnet group.
                  - **DBSubnetGroupName** *(string) --* 
                    The name of the DB subnet group.
                  - **DBSubnetGroupDescription** *(string) --* 
                    Provides the description of the DB subnet group.
                  - **VpcId** *(string) --* 
                    Provides the VpcId of the DB subnet group.
                  - **SubnetGroupStatus** *(string) --* 
                    Provides the status of the DB subnet group.
                  - **Subnets** *(list) --* 
                    Contains a list of  Subnet elements.
                    - *(dict) --* 
                      Specifies a subnet.
                      This data type is used as a response element in the  DescribeDBSubnetGroups action.
                      - **SubnetIdentifier** *(string) --* 
                        Specifies the identifier of the subnet.
                      - **SubnetAvailabilityZone** *(dict) --* 
                        Specifies the EC2 Availability Zone that the subnet is in.
                        - **Name** *(string) --* 
                          The name of the availability zone.
                      - **SubnetStatus** *(string) --* 
                        Specifies the status of the subnet.
                  - **DBSubnetGroupArn** *(string) --* 
                    The Amazon Resource Name (ARN) for the DB subnet group.
                - **PreferredMaintenanceWindow** *(string) --* 
                  Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
                - **PendingModifiedValues** *(dict) --* 
                  Specifies that changes to the DB instance are pending. This element is only included when changes are pending. Specific changes are identified by subelements.
                  - **DBInstanceClass** *(string) --* 
                    Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is currently being applied.
                  - **AllocatedStorage** *(integer) --* 
                    Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is currently being applied.
                  - **MasterUserPassword** *(string) --* 
                    Contains the pending or currently-in-progress change of the master credentials for the DB instance.
                  - **Port** *(integer) --* 
                    Specifies the pending port for the DB instance.
                  - **BackupRetentionPeriod** *(integer) --* 
                    Specifies the pending number of days for which automated backups are retained.
                  - **MultiAZ** *(boolean) --* 
                    Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.
                  - **EngineVersion** *(string) --* 
                    Indicates the database engine version.
                  - **LicenseModel** *(string) --* 
                    The license model for the DB instance.
                    Valid values: ``license-included`` | ``bring-your-own-license`` | ``general-public-license``  
                  - **Iops** *(integer) --* 
                    Specifies the new Provisioned IOPS value for the DB instance that will be applied or is currently being applied.
                  - **DBInstanceIdentifier** *(string) --* 
                    Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is currently being applied.
                  - **StorageType** *(string) --* 
                    Specifies the storage type to be associated with the DB instance.
                  - **CACertificateIdentifier** *(string) --* 
                    Specifies the identifier of the CA certificate for the DB instance.
                  - **DBSubnetGroupName** *(string) --* 
                    The new DB subnet group for the DB instance.
                  - **PendingCloudwatchLogsExports** *(dict) --* 
                    Specifies the CloudWatch logs to be exported.
                    - **LogTypesToEnable** *(list) --* 
                      Log types that are in the process of being deactivated. After they are deactivated, these log types aren't exported to CloudWatch Logs.
                      - *(string) --* 
                    - **LogTypesToDisable** *(list) --* 
                      Log types that are in the process of being enabled. After they are enabled, these log types are exported to CloudWatch Logs.
                      - *(string) --* 
                - **LatestRestorableTime** *(datetime) --* 
                  Specifies the latest time to which a database can be restored with point-in-time restore.
                - **MultiAZ** *(boolean) --* 
                  Specifies if the DB instance is a Multi-AZ deployment.
                - **EngineVersion** *(string) --* 
                  Indicates the database engine version.
                - **AutoMinorVersionUpgrade** *(boolean) --* 
                  Indicates that minor version patches are applied automatically.
                - **ReadReplicaSourceDBInstanceIdentifier** *(string) --* 
                  Contains the identifier of the source DB instance if this DB instance is a Read Replica.
                - **ReadReplicaDBInstanceIdentifiers** *(list) --* 
                  Contains one or more identifiers of the Read Replicas associated with this DB instance.
                  - *(string) --* 
                - **ReadReplicaDBClusterIdentifiers** *(list) --* 
                  Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.
                  - *(string) --* 
                - **LicenseModel** *(string) --* 
                  License model information for this DB instance.
                - **Iops** *(integer) --* 
                  Specifies the Provisioned IOPS (I/O operations per second) value.
                - **OptionGroupMemberships** *(list) --* 
                  Provides the list of option group memberships for this DB instance.
                  - *(dict) --* 
                    Provides information on the option groups the DB instance is a member of.
                    - **OptionGroupName** *(string) --* 
                      The name of the option group that the instance belongs to.
                    - **Status** *(string) --* 
                      The status of the DB instance's option group membership. Valid values are: ``in-sync`` , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` , ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .
                - **CharacterSetName** *(string) --* 
                  If present, specifies the name of the character set that this instance is associated with.
                - **SecondaryAvailabilityZone** *(string) --* 
                  If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.
                - **PubliclyAccessible** *(boolean) --* 
                  This flag should no longer be used.
                - **StatusInfos** *(list) --* 
                  The status of a Read Replica. If the instance is not a Read Replica, this is blank.
                  - *(dict) --* 
                    Provides a list of status information for a DB instance.
                    - **StatusType** *(string) --* 
                      This value is currently "read replication."
                    - **Normal** *(boolean) --* 
                      Boolean value that is true if the instance is operating normally, or false if the instance is in an error state.
                    - **Status** *(string) --* 
                      Status of the DB instance. For a StatusType of read replica, the values can be replicating, error, stopped, or terminated.
                    - **Message** *(string) --* 
                      Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.
                - **StorageType** *(string) --* 
                  Specifies the storage type associated with DB instance.
                - **TdeCredentialArn** *(string) --* 
                  The ARN from the key store with which the instance is associated for TDE encryption.
                - **DbInstancePort** *(integer) --* 
                  Specifies the port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.
                - **DBClusterIdentifier** *(string) --* 
                  If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.
                - **StorageEncrypted** *(boolean) --* 
                  Not supported: The encryption for DB instances is managed by the DB cluster.
                - **KmsKeyId** *(string) --* 
                  Not supported: The encryption for DB instances is managed by the DB cluster.
                - **DbiResourceId** *(string) --* 
                  The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.
                - **CACertificateIdentifier** *(string) --* 
                  The identifier of the CA certificate for this DB instance.
                - **DomainMemberships** *(list) --* 
                  Not supported
                  - *(dict) --* 
                    An Active Directory Domain membership record associated with a DB instance.
                    - **Domain** *(string) --* 
                      The identifier of the Active Directory Domain.
                    - **Status** *(string) --* 
                      The status of the DB instance's Active Directory Domain membership, such as joined, pending-join, failed etc).
                    - **FQDN** *(string) --* 
                      The fully qualified domain name of the Active Directory Domain.
                    - **IAMRoleName** *(string) --* 
                      The name of the IAM role to be used when making API calls to the Directory Service.
                - **CopyTagsToSnapshot** *(boolean) --* 
                  Specifies whether tags are copied from the DB instance to snapshots of the DB instance.
                - **MonitoringInterval** *(integer) --* 
                  The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.
                - **EnhancedMonitoringResourceArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the Enhanced Monitoring metrics data for the DB instance.
                - **MonitoringRoleArn** *(string) --* 
                  The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.
                - **PromotionTier** *(integer) --* 
                  A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance. 
                - **DBInstanceArn** *(string) --* 
                  The Amazon Resource Name (ARN) for the DB instance.
                - **Timezone** *(string) --* 
                  Not supported.
                - **IAMDatabaseAuthenticationEnabled** *(boolean) --* 
                  True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise false.
                - **PerformanceInsightsEnabled** *(boolean) --* 
                  True if Performance Insights is enabled for the DB instance, and otherwise false.
                - **PerformanceInsightsKMSKeyId** *(string) --* 
                  The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.
                - **EnabledCloudwatchLogsExports** *(list) --* 
                  A list of log types that this DB instance is configured to export to CloudWatch Logs.
                  - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier:
          The user-supplied instance identifier. If this parameter is specified, information from only the specific DB instance is returned. This parameter isn\'t case-sensitive.
          Constraints:
          * If supplied, must match the identifier of an existing DBInstance.
        :type Filters: list
        :param Filters:
          A filter that specifies one or more DB instances to describe.
          Supported filters:
          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB instances associated with the DB clusters identified by these ARNs.
          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance Amazon Resource Names (ARNs). The results list will only include information about the DB instances identified by these ARNs.
          - *(dict) --*
            This type is not currently supported.
            - **Name** *(string) --* **[REQUIRED]**
              This parameter is not currently supported.
            - **Values** *(list) --* **[REQUIRED]**
              This parameter is not currently supported.
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


class DescribeDBParameterGroups(Paginator):
    def paginate(self, DBParameterGroupName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Neptune.Client.describe_db_parameter_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBParameterGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DBParameterGroupName='string',
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
                'DBParameterGroups': [
                    {
                        'DBParameterGroupName': 'string',
                        'DBParameterGroupFamily': 'string',
                        'Description': 'string',
                        'DBParameterGroupArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBParameterGroups** *(list) --* 
              A list of  DBParameterGroup instances.
              - *(dict) --* 
                Contains the details of an Amazon Neptune DB parameter group.
                This data type is used as a response element in the  DescribeDBParameterGroups action.
                - **DBParameterGroupName** *(string) --* 
                  Provides the name of the DB parameter group.
                - **DBParameterGroupFamily** *(string) --* 
                  Provides the name of the DB parameter group family that this DB parameter group is compatible with.
                - **Description** *(string) --* 
                  Provides the customer-specified description for this DB parameter group.
                - **DBParameterGroupArn** *(string) --* 
                  The Amazon Resource Name (ARN) for the DB parameter group.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type DBParameterGroupName: string
        :param DBParameterGroupName:
          The name of a specific DB parameter group to return details for.
          Constraints:
          * If supplied, must match the name of an existing DBClusterParameterGroup.
        :type Filters: list
        :param Filters:
          This parameter is not currently supported.
          - *(dict) --*
            This type is not currently supported.
            - **Name** *(string) --* **[REQUIRED]**
              This parameter is not currently supported.
            - **Values** *(list) --* **[REQUIRED]**
              This parameter is not currently supported.
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


class DescribeDBParameters(Paginator):
    def paginate(self, DBParameterGroupName: str, Source: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Neptune.Client.describe_db_parameters`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBParameters>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DBParameterGroupName='string',
              Source='string',
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
                'Parameters': [
                    {
                        'ParameterName': 'string',
                        'ParameterValue': 'string',
                        'Description': 'string',
                        'Source': 'string',
                        'ApplyType': 'string',
                        'DataType': 'string',
                        'AllowedValues': 'string',
                        'IsModifiable': True|False,
                        'MinimumEngineVersion': 'string',
                        'ApplyMethod': 'immediate'|'pending-reboot'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Parameters** *(list) --* 
              A list of  Parameter values.
              - *(dict) --* 
                Specifies a parameter.
                - **ParameterName** *(string) --* 
                  Specifies the name of the parameter.
                - **ParameterValue** *(string) --* 
                  Specifies the value of the parameter.
                - **Description** *(string) --* 
                  Provides a description of the parameter.
                - **Source** *(string) --* 
                  Indicates the source of the parameter value.
                - **ApplyType** *(string) --* 
                  Specifies the engine specific parameters type.
                - **DataType** *(string) --* 
                  Specifies the valid data type for the parameter.
                - **AllowedValues** *(string) --* 
                  Specifies the valid range of values for the parameter.
                - **IsModifiable** *(boolean) --* 
                  Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
                - **MinimumEngineVersion** *(string) --* 
                  The earliest engine version to which the parameter can apply.
                - **ApplyMethod** *(string) --* 
                  Indicates when to apply parameter updates.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type DBParameterGroupName: string
        :param DBParameterGroupName: **[REQUIRED]**
          The name of a specific DB parameter group to return details for.
          Constraints:
          * If supplied, must match the name of an existing DBParameterGroup.
        :type Source: string
        :param Source:
          The parameter types to return.
          Default: All parameter types returned
          Valid Values: ``user | system | engine-default``
        :type Filters: list
        :param Filters:
          This parameter is not currently supported.
          - *(dict) --*
            This type is not currently supported.
            - **Name** *(string) --* **[REQUIRED]**
              This parameter is not currently supported.
            - **Values** *(list) --* **[REQUIRED]**
              This parameter is not currently supported.
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


class DescribeDBSubnetGroups(Paginator):
    def paginate(self, DBSubnetGroupName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Neptune.Client.describe_db_subnet_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBSubnetGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DBSubnetGroupName='string',
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
                'DBSubnetGroups': [
                    {
                        'DBSubnetGroupName': 'string',
                        'DBSubnetGroupDescription': 'string',
                        'VpcId': 'string',
                        'SubnetGroupStatus': 'string',
                        'Subnets': [
                            {
                                'SubnetIdentifier': 'string',
                                'SubnetAvailabilityZone': {
                                    'Name': 'string'
                                },
                                'SubnetStatus': 'string'
                            },
                        ],
                        'DBSubnetGroupArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBSubnetGroups** *(list) --* 
              A list of  DBSubnetGroup instances.
              - *(dict) --* 
                Contains the details of an Amazon Neptune DB subnet group.
                This data type is used as a response element in the  DescribeDBSubnetGroups action.
                - **DBSubnetGroupName** *(string) --* 
                  The name of the DB subnet group.
                - **DBSubnetGroupDescription** *(string) --* 
                  Provides the description of the DB subnet group.
                - **VpcId** *(string) --* 
                  Provides the VpcId of the DB subnet group.
                - **SubnetGroupStatus** *(string) --* 
                  Provides the status of the DB subnet group.
                - **Subnets** *(list) --* 
                  Contains a list of  Subnet elements.
                  - *(dict) --* 
                    Specifies a subnet.
                    This data type is used as a response element in the  DescribeDBSubnetGroups action.
                    - **SubnetIdentifier** *(string) --* 
                      Specifies the identifier of the subnet.
                    - **SubnetAvailabilityZone** *(dict) --* 
                      Specifies the EC2 Availability Zone that the subnet is in.
                      - **Name** *(string) --* 
                        The name of the availability zone.
                    - **SubnetStatus** *(string) --* 
                      Specifies the status of the subnet.
                - **DBSubnetGroupArn** *(string) --* 
                  The Amazon Resource Name (ARN) for the DB subnet group.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName:
          The name of the DB subnet group to return details for.
        :type Filters: list
        :param Filters:
          This parameter is not currently supported.
          - *(dict) --*
            This type is not currently supported.
            - **Name** *(string) --* **[REQUIRED]**
              This parameter is not currently supported.
            - **Values** *(list) --* **[REQUIRED]**
              This parameter is not currently supported.
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


class DescribeEngineDefaultParameters(Paginator):
    def paginate(self, DBParameterGroupFamily: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Neptune.Client.describe_engine_default_parameters`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeEngineDefaultParameters>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DBParameterGroupFamily='string',
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
                'EngineDefaults': {
                    'DBParameterGroupFamily': 'string',
                    'Marker': 'string',
                    'Parameters': [
                        {
                            'ParameterName': 'string',
                            'ParameterValue': 'string',
                            'Description': 'string',
                            'Source': 'string',
                            'ApplyType': 'string',
                            'DataType': 'string',
                            'AllowedValues': 'string',
                            'IsModifiable': True|False,
                            'MinimumEngineVersion': 'string',
                            'ApplyMethod': 'immediate'|'pending-reboot'
                        },
                    ]
                },
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EngineDefaults** *(dict) --* 
              Contains the result of a successful invocation of the  DescribeEngineDefaultParameters action.
              - **DBParameterGroupFamily** *(string) --* 
                Specifies the name of the DB parameter group family that the engine default parameters apply to.
              - **Marker** *(string) --* 
                An optional pagination token provided by a previous EngineDefaults request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
              - **Parameters** *(list) --* 
                Contains a list of engine default parameters.
                - *(dict) --* 
                  Specifies a parameter.
                  - **ParameterName** *(string) --* 
                    Specifies the name of the parameter.
                  - **ParameterValue** *(string) --* 
                    Specifies the value of the parameter.
                  - **Description** *(string) --* 
                    Provides a description of the parameter.
                  - **Source** *(string) --* 
                    Indicates the source of the parameter value.
                  - **ApplyType** *(string) --* 
                    Specifies the engine specific parameters type.
                  - **DataType** *(string) --* 
                    Specifies the valid data type for the parameter.
                  - **AllowedValues** *(string) --* 
                    Specifies the valid range of values for the parameter.
                  - **IsModifiable** *(boolean) --* 
                    Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
                  - **MinimumEngineVersion** *(string) --* 
                    The earliest engine version to which the parameter can apply.
                  - **ApplyMethod** *(string) --* 
                    Indicates when to apply parameter updates.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type DBParameterGroupFamily: string
        :param DBParameterGroupFamily: **[REQUIRED]**
          The name of the DB parameter group family.
        :type Filters: list
        :param Filters:
          Not currently supported.
          - *(dict) --*
            This type is not currently supported.
            - **Name** *(string) --* **[REQUIRED]**
              This parameter is not currently supported.
            - **Values** *(list) --* **[REQUIRED]**
              This parameter is not currently supported.
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


class DescribeEventSubscriptions(Paginator):
    def paginate(self, SubscriptionName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Neptune.Client.describe_event_subscriptions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeEventSubscriptions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SubscriptionName='string',
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
                'EventSubscriptionsList': [
                    {
                        'CustomerAwsId': 'string',
                        'CustSubscriptionId': 'string',
                        'SnsTopicArn': 'string',
                        'Status': 'string',
                        'SubscriptionCreationTime': 'string',
                        'SourceType': 'string',
                        'SourceIdsList': [
                            'string',
                        ],
                        'EventCategoriesList': [
                            'string',
                        ],
                        'Enabled': True|False,
                        'EventSubscriptionArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EventSubscriptionsList** *(list) --* 
              A list of EventSubscriptions data types.
              - *(dict) --* 
                Contains the results of a successful invocation of the  DescribeEventSubscriptions action.
                - **CustomerAwsId** *(string) --* 
                  The AWS customer account associated with the event notification subscription.
                - **CustSubscriptionId** *(string) --* 
                  The event notification subscription Id.
                - **SnsTopicArn** *(string) --* 
                  The topic ARN of the event notification subscription.
                - **Status** *(string) --* 
                  The status of the event notification subscription.
                  Constraints:
                  Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
                  The status "no-permission" indicates that Neptune no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.
                - **SubscriptionCreationTime** *(string) --* 
                  The time the event notification subscription was created.
                - **SourceType** *(string) --* 
                  The source type for the event notification subscription.
                - **SourceIdsList** *(list) --* 
                  A list of source IDs for the event notification subscription.
                  - *(string) --* 
                - **EventCategoriesList** *(list) --* 
                  A list of event categories for the event notification subscription.
                  - *(string) --* 
                - **Enabled** *(boolean) --* 
                  A Boolean value indicating if the subscription is enabled. True indicates the subscription is enabled.
                - **EventSubscriptionArn** *(string) --* 
                  The Amazon Resource Name (ARN) for the event subscription.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type SubscriptionName: string
        :param SubscriptionName:
          The name of the event notification subscription you want to describe.
        :type Filters: list
        :param Filters:
          This parameter is not currently supported.
          - *(dict) --*
            This type is not currently supported.
            - **Name** *(string) --* **[REQUIRED]**
              This parameter is not currently supported.
            - **Values** *(list) --* **[REQUIRED]**
              This parameter is not currently supported.
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
    def paginate(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, EventCategories: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Neptune.Client.describe_events`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeEvents>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              SourceIdentifier='string',
              SourceType='db-instance'|'db-parameter-group'|'db-security-group'|'db-snapshot'|'db-cluster'|'db-cluster-snapshot',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Duration=123,
              EventCategories=[
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
                'Events': [
                    {
                        'SourceIdentifier': 'string',
                        'SourceType': 'db-instance'|'db-parameter-group'|'db-security-group'|'db-snapshot'|'db-cluster'|'db-cluster-snapshot',
                        'Message': 'string',
                        'EventCategories': [
                            'string',
                        ],
                        'Date': datetime(2015, 1, 1),
                        'SourceArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Events** *(list) --* 
              A list of  Event instances.
              - *(dict) --* 
                This data type is used as a response element in the  DescribeEvents action.
                - **SourceIdentifier** *(string) --* 
                  Provides the identifier for the source of the event.
                - **SourceType** *(string) --* 
                  Specifies the source type for this event.
                - **Message** *(string) --* 
                  Provides the text of this event.
                - **EventCategories** *(list) --* 
                  Specifies the category for the event.
                  - *(string) --* 
                - **Date** *(datetime) --* 
                  Specifies the date and time of the event.
                - **SourceArn** *(string) --* 
                  The Amazon Resource Name (ARN) for the event.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type SourceIdentifier: string
        :param SourceIdentifier:
          The identifier of the event source for which events are returned. If not specified, then all sources are included in the response.
          Constraints:
          * If SourceIdentifier is supplied, SourceType must also be provided.
          * If the source type is ``DBInstance`` , then a ``DBInstanceIdentifier`` must be supplied.
          * If the source type is ``DBSecurityGroup`` , a ``DBSecurityGroupName`` must be supplied.
          * If the source type is ``DBParameterGroup`` , a ``DBParameterGroupName`` must be supplied.
          * If the source type is ``DBSnapshot`` , a ``DBSnapshotIdentifier`` must be supplied.
          * Cannot end with a hyphen or contain two consecutive hyphens.
        :type SourceType: string
        :param SourceType:
          The event source to retrieve events for. If no value is specified, all events are returned.
        :type StartTime: datetime
        :param StartTime:
          The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the `ISO8601 Wikipedia page. <http://en.wikipedia.org/wiki/ISO_8601>`__
          Example: 2009-07-08T18:00Z
        :type EndTime: datetime
        :param EndTime:
          The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the `ISO8601 Wikipedia page. <http://en.wikipedia.org/wiki/ISO_8601>`__
          Example: 2009-07-08T18:00Z
        :type Duration: integer
        :param Duration:
          The number of minutes to retrieve events for.
          Default: 60
        :type EventCategories: list
        :param EventCategories:
          A list of event categories that trigger notifications for a event notification subscription.
          - *(string) --*
        :type Filters: list
        :param Filters:
          This parameter is not currently supported.
          - *(dict) --*
            This type is not currently supported.
            - **Name** *(string) --* **[REQUIRED]**
              This parameter is not currently supported.
            - **Values** *(list) --* **[REQUIRED]**
              This parameter is not currently supported.
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


class DescribeOrderableDBInstanceOptions(Paginator):
    def paginate(self, Engine: str, EngineVersion: str = None, DBInstanceClass: str = None, LicenseModel: str = None, Vpc: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Neptune.Client.describe_orderable_db_instance_options`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeOrderableDBInstanceOptions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Engine='string',
              EngineVersion='string',
              DBInstanceClass='string',
              LicenseModel='string',
              Vpc=True|False,
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
                'OrderableDBInstanceOptions': [
                    {
                        'Engine': 'string',
                        'EngineVersion': 'string',
                        'DBInstanceClass': 'string',
                        'LicenseModel': 'string',
                        'AvailabilityZones': [
                            {
                                'Name': 'string'
                            },
                        ],
                        'MultiAZCapable': True|False,
                        'ReadReplicaCapable': True|False,
                        'Vpc': True|False,
                        'SupportsStorageEncryption': True|False,
                        'StorageType': 'string',
                        'SupportsIops': True|False,
                        'SupportsEnhancedMonitoring': True|False,
                        'SupportsIAMDatabaseAuthentication': True|False,
                        'SupportsPerformanceInsights': True|False,
                        'MinStorageSize': 123,
                        'MaxStorageSize': 123,
                        'MinIopsPerDbInstance': 123,
                        'MaxIopsPerDbInstance': 123,
                        'MinIopsPerGib': 123.0,
                        'MaxIopsPerGib': 123.0
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **OrderableDBInstanceOptions** *(list) --* 
              An  OrderableDBInstanceOption structure containing information about orderable options for the DB instance.
              - *(dict) --* 
                Contains a list of available options for a DB instance.
                This data type is used as a response element in the  DescribeOrderableDBInstanceOptions action.
                - **Engine** *(string) --* 
                  The engine type of a DB instance.
                - **EngineVersion** *(string) --* 
                  The engine version of a DB instance.
                - **DBInstanceClass** *(string) --* 
                  The DB instance class for a DB instance.
                - **LicenseModel** *(string) --* 
                  The license model for a DB instance.
                - **AvailabilityZones** *(list) --* 
                  A list of Availability Zones for a DB instance.
                  - *(dict) --* 
                    Specifies an Availability Zone.
                    - **Name** *(string) --* 
                      The name of the availability zone.
                - **MultiAZCapable** *(boolean) --* 
                  Indicates whether a DB instance is Multi-AZ capable.
                - **ReadReplicaCapable** *(boolean) --* 
                  Indicates whether a DB instance can have a Read Replica.
                - **Vpc** *(boolean) --* 
                  Indicates whether a DB instance is in a VPC.
                - **SupportsStorageEncryption** *(boolean) --* 
                  Indicates whether a DB instance supports encrypted storage.
                - **StorageType** *(string) --* 
                  Indicates the storage type for a DB instance.
                - **SupportsIops** *(boolean) --* 
                  Indicates whether a DB instance supports provisioned IOPS.
                - **SupportsEnhancedMonitoring** *(boolean) --* 
                  Indicates whether a DB instance supports Enhanced Monitoring at intervals from 1 to 60 seconds.
                - **SupportsIAMDatabaseAuthentication** *(boolean) --* 
                  Indicates whether a DB instance supports IAM database authentication.
                - **SupportsPerformanceInsights** *(boolean) --* 
                  True if a DB instance supports Performance Insights, otherwise false.
                - **MinStorageSize** *(integer) --* 
                  Minimum storage size for a DB instance.
                - **MaxStorageSize** *(integer) --* 
                  Maximum storage size for a DB instance.
                - **MinIopsPerDbInstance** *(integer) --* 
                  Minimum total provisioned IOPS for a DB instance.
                - **MaxIopsPerDbInstance** *(integer) --* 
                  Maximum total provisioned IOPS for a DB instance.
                - **MinIopsPerGib** *(float) --* 
                  Minimum provisioned IOPS per GiB for a DB instance.
                - **MaxIopsPerGib** *(float) --* 
                  Maximum provisioned IOPS per GiB for a DB instance.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type Engine: string
        :param Engine: **[REQUIRED]**
          The name of the engine to retrieve DB instance options for.
        :type EngineVersion: string
        :param EngineVersion:
          The engine version filter value. Specify this parameter to show only the available offerings matching the specified engine version.
        :type DBInstanceClass: string
        :param DBInstanceClass:
          The DB instance class filter value. Specify this parameter to show only the available offerings matching the specified DB instance class.
        :type LicenseModel: string
        :param LicenseModel:
          The license model filter value. Specify this parameter to show only the available offerings matching the specified license model.
        :type Vpc: boolean
        :param Vpc:
          The VPC filter value. Specify this parameter to show only the available VPC or non-VPC offerings.
        :type Filters: list
        :param Filters:
          This parameter is not currently supported.
          - *(dict) --*
            This type is not currently supported.
            - **Name** *(string) --* **[REQUIRED]**
              This parameter is not currently supported.
            - **Values** *(list) --* **[REQUIRED]**
              This parameter is not currently supported.
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


class DescribePendingMaintenanceActions(Paginator):
    def paginate(self, ResourceIdentifier: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Neptune.Client.describe_pending_maintenance_actions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribePendingMaintenanceActions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ResourceIdentifier='string',
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
                'PendingMaintenanceActions': [
                    {
                        'ResourceIdentifier': 'string',
                        'PendingMaintenanceActionDetails': [
                            {
                                'Action': 'string',
                                'AutoAppliedAfterDate': datetime(2015, 1, 1),
                                'ForcedApplyDate': datetime(2015, 1, 1),
                                'OptInStatus': 'string',
                                'CurrentApplyDate': datetime(2015, 1, 1),
                                'Description': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PendingMaintenanceActions** *(list) --* 
              A list of the pending maintenance actions for the resource.
              - *(dict) --* 
                Describes the pending maintenance actions for a resource.
                - **ResourceIdentifier** *(string) --* 
                  The ARN of the resource that has pending maintenance actions.
                - **PendingMaintenanceActionDetails** *(list) --* 
                  A list that provides details about the pending maintenance actions for the resource.
                  - *(dict) --* 
                    Provides information about a pending maintenance action for a resource.
                    - **Action** *(string) --* 
                      The type of pending maintenance action that is available for the resource.
                    - **AutoAppliedAfterDate** *(datetime) --* 
                      The date of the maintenance window when the action is applied. The maintenance action is applied to the resource during its first maintenance window after this date. If this date is specified, any ``next-maintenance`` opt-in requests are ignored.
                    - **ForcedApplyDate** *(datetime) --* 
                      The date when the maintenance action is automatically applied. The maintenance action is applied to the resource on this date regardless of the maintenance window for the resource. If this date is specified, any ``immediate`` opt-in requests are ignored.
                    - **OptInStatus** *(string) --* 
                      Indicates the type of opt-in request that has been received for the resource.
                    - **CurrentApplyDate** *(datetime) --* 
                      The effective date when the pending maintenance action is applied to the resource. This date takes into account opt-in requests received from the  ApplyPendingMaintenanceAction API, the ``AutoAppliedAfterDate`` , and the ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .
                    - **Description** *(string) --* 
                      A description providing more detail about the maintenance action.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type ResourceIdentifier: string
        :param ResourceIdentifier:
          The ARN of a resource to return pending maintenance actions for.
        :type Filters: list
        :param Filters:
          A filter that specifies one or more resources to return pending maintenance actions for.
          Supported filters:
          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include pending maintenance actions for the DB clusters identified by these ARNs.
          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance ARNs. The results list will only include pending maintenance actions for the DB instances identified by these ARNs.
          - *(dict) --*
            This type is not currently supported.
            - **Name** *(string) --* **[REQUIRED]**
              This parameter is not currently supported.
            - **Values** *(list) --* **[REQUIRED]**
              This parameter is not currently supported.
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
