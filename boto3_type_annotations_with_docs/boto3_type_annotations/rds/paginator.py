from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeDBClusterSnapshots(Paginator):
    def paginate(self, DBClusterIdentifier: str = None, DBClusterSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, IncludeShared: bool = None, IncludePublic: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBClusterSnapshots>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DBClusterIdentifier=\'string\',
              DBClusterSnapshotIdentifier=\'string\',
              SnapshotType=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              IncludeShared=True|False,
              IncludePublic=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
        
          * ``automated`` - Return all DB cluster snapshots that have been automatically taken by Amazon RDS for my AWS account. 
           
          * ``manual`` - Return all DB cluster snapshots that have been taken by my AWS account. 
           
          * ``shared`` - Return all manual DB cluster snapshots that have been shared to my AWS account. 
           
          * ``public`` - Return all DB cluster snapshots that have been marked as public. 
           
          If you don\'t specify a ``SnapshotType`` value, then both automated and manual DB cluster snapshots are returned. You can include shared DB cluster snapshots with these results by setting the ``IncludeShared`` parameter to ``true`` . You can include public DB cluster snapshots with these results by setting the ``IncludePublic`` parameter to ``true`` .
        
          The ``IncludeShared`` and ``IncludePublic`` parameters don\'t apply for ``SnapshotType`` values of ``manual`` or ``automated`` . The ``IncludePublic`` parameter doesn\'t apply when ``SnapshotType`` is set to ``shared`` . The ``IncludeShared`` parameter doesn\'t apply when ``SnapshotType`` is set to ``public`` .
        
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              One or more filter values. Filter values are case-sensitive.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBClusterSnapshots\': [
                    {
                        \'AvailabilityZones\': [
                            \'string\',
                        ],
                        \'DBClusterSnapshotIdentifier\': \'string\',
                        \'DBClusterIdentifier\': \'string\',
                        \'SnapshotCreateTime\': datetime(2015, 1, 1),
                        \'Engine\': \'string\',
                        \'AllocatedStorage\': 123,
                        \'Status\': \'string\',
                        \'Port\': 123,
                        \'VpcId\': \'string\',
                        \'ClusterCreateTime\': datetime(2015, 1, 1),
                        \'MasterUsername\': \'string\',
                        \'EngineVersion\': \'string\',
                        \'LicenseModel\': \'string\',
                        \'SnapshotType\': \'string\',
                        \'PercentProgress\': 123,
                        \'StorageEncrypted\': True|False,
                        \'KmsKeyId\': \'string\',
                        \'DBClusterSnapshotArn\': \'string\',
                        \'SourceDBClusterSnapshotArn\': \'string\',
                        \'IAMDatabaseAuthenticationEnabled\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Provides a list of DB cluster snapshots for the user as the result of a call to the  DescribeDBClusterSnapshots action. 
        
            - **DBClusterSnapshots** *(list) --* 
        
              Provides a list of DB cluster snapshots for the user.
        
              - *(dict) --* 
        
                Contains the details for an Amazon RDS DB cluster snapshot 
        
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
        
        """
        pass


class DescribeDBClusters(Paginator):
    def paginate(self, DBClusterIdentifier: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBClusters>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DBClusterIdentifier=\'string\',
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
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
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
                \'DBClusters\': [
                    {
                        \'AllocatedStorage\': 123,
                        \'AvailabilityZones\': [
                            \'string\',
                        ],
                        \'BackupRetentionPeriod\': 123,
                        \'CharacterSetName\': \'string\',
                        \'DatabaseName\': \'string\',
                        \'DBClusterIdentifier\': \'string\',
                        \'DBClusterParameterGroup\': \'string\',
                        \'DBSubnetGroup\': \'string\',
                        \'Status\': \'string\',
                        \'PercentProgress\': \'string\',
                        \'EarliestRestorableTime\': datetime(2015, 1, 1),
                        \'Endpoint\': \'string\',
                        \'ReaderEndpoint\': \'string\',
                        \'CustomEndpoints\': [
                            \'string\',
                        ],
                        \'MultiAZ\': True|False,
                        \'Engine\': \'string\',
                        \'EngineVersion\': \'string\',
                        \'LatestRestorableTime\': datetime(2015, 1, 1),
                        \'Port\': 123,
                        \'MasterUsername\': \'string\',
                        \'DBClusterOptionGroupMemberships\': [
                            {
                                \'DBClusterOptionGroupName\': \'string\',
                                \'Status\': \'string\'
                            },
                        ],
                        \'PreferredBackupWindow\': \'string\',
                        \'PreferredMaintenanceWindow\': \'string\',
                        \'ReplicationSourceIdentifier\': \'string\',
                        \'ReadReplicaIdentifiers\': [
                            \'string\',
                        ],
                        \'DBClusterMembers\': [
                            {
                                \'DBInstanceIdentifier\': \'string\',
                                \'IsClusterWriter\': True|False,
                                \'DBClusterParameterGroupStatus\': \'string\',
                                \'PromotionTier\': 123
                            },
                        ],
                        \'VpcSecurityGroups\': [
                            {
                                \'VpcSecurityGroupId\': \'string\',
                                \'Status\': \'string\'
                            },
                        ],
                        \'HostedZoneId\': \'string\',
                        \'StorageEncrypted\': True|False,
                        \'KmsKeyId\': \'string\',
                        \'DbClusterResourceId\': \'string\',
                        \'DBClusterArn\': \'string\',
                        \'AssociatedRoles\': [
                            {
                                \'RoleArn\': \'string\',
                                \'Status\': \'string\',
                                \'FeatureName\': \'string\'
                            },
                        ],
                        \'IAMDatabaseAuthenticationEnabled\': True|False,
                        \'CloneGroupId\': \'string\',
                        \'ClusterCreateTime\': datetime(2015, 1, 1),
                        \'EarliestBacktrackTime\': datetime(2015, 1, 1),
                        \'BacktrackWindow\': 123,
                        \'BacktrackConsumedChangeRecords\': 123,
                        \'EnabledCloudwatchLogsExports\': [
                            \'string\',
                        ],
                        \'Capacity\': 123,
                        \'EngineMode\': \'string\',
                        \'ScalingConfigurationInfo\': {
                            \'MinCapacity\': 123,
                            \'MaxCapacity\': 123,
                            \'AutoPause\': True|False,
                            \'SecondsUntilAutoPause\': 123
                        },
                        \'DeletionProtection\': True|False
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeDBClusters action.
        
            - **DBClusters** *(list) --* 
        
              Contains a list of DB clusters for the user.
        
              - *(dict) --* 
        
                Contains the details of an Amazon Aurora DB cluster. 
        
                This data type is used as a response element in the  DescribeDBClusters ,  StopDBCluster , and  StartDBCluster actions. 
        
                - **AllocatedStorage** *(integer) --* 
        
                  For all database engines except Amazon Aurora, ``AllocatedStorage`` specifies the allocated storage size in gibibytes (GiB). For Aurora, ``AllocatedStorage`` always returns 1, because Aurora DB cluster storage size is not fixed, but instead automatically adjusts as needed.
        
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
        
                  The earliest time to which a database can be restored with point-in-time restore.
        
                - **Endpoint** *(string) --* 
        
                  Specifies the connection endpoint for the primary instance of the DB cluster.
        
                - **ReaderEndpoint** *(string) --* 
        
                  The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Aurora Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Aurora distributes the connection requests among the Aurora Replicas in the DB cluster. This functionality can help balance your read workload across multiple Aurora Replicas in your DB cluster. 
        
                  If a failover occurs, and the Aurora Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Aurora Replicas in the cluster, you can then reconnect to the reader endpoint.
        
                - **CustomEndpoints** *(list) --* 
        
                  Identifies all custom endpoints associated with the cluster.
        
                  - *(string) --* 
              
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
        
                  Contains the identifier of the source DB cluster if this DB cluster is a Read Replica.
        
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
        
                      A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see `Fault Tolerance for an Aurora DB Cluster <http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.FaultTolerance>`__ in the *Amazon Aurora User Guide* . 
        
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
                       
                    - **FeatureName** *(string) --* 
                
                - **IAMDatabaseAuthenticationEnabled** *(boolean) --* 
        
                  True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.
        
                - **CloneGroupId** *(string) --* 
        
                  Identifies the clone group to which the DB cluster is associated.
        
                - **ClusterCreateTime** *(datetime) --* 
        
                  Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).
        
                - **EarliestBacktrackTime** *(datetime) --* 
        
                  The earliest time to which a DB cluster can be backtracked.
        
                - **BacktrackWindow** *(integer) --* 
        
                  The target backtrack window, in seconds. If this value is set to 0, backtracking is disabled for the DB cluster. Otherwise, backtracking is enabled.
        
                - **BacktrackConsumedChangeRecords** *(integer) --* 
        
                  The number of change records stored for Backtrack.
        
                - **EnabledCloudwatchLogsExports** *(list) --* 
        
                  A list of log types that this DB cluster is configured to export to CloudWatch Logs.
        
                  Log types vary by DB engine. For information about the log types for each DB engine, see `Amazon RDS Database Log Files <http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html>`__ in the *Amazon Aurora User Guide.*  
        
                  - *(string) --* 
              
                - **Capacity** *(integer) --* 
                
                - **EngineMode** *(string) --* 
        
                  The DB engine mode of the DB cluster, either ``provisioned`` , ``serverless`` , or ``parallelquery`` .
        
                - **ScalingConfigurationInfo** *(dict) --* 
        
                  Shows the scaling configuration for an Aurora DB cluster in ``serverless`` DB engine mode.
        
                  For more information, see `Using Amazon Aurora Serverless <http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html>`__ in the *Amazon Aurora User Guide* .
        
                  - **MinCapacity** *(integer) --* 
        
                    The maximum capacity for the Aurora DB cluster in ``serverless`` DB engine mode.
        
                  - **MaxCapacity** *(integer) --* 
        
                    The maximum capacity for an Aurora DB cluster in ``serverless`` DB engine mode.
        
                  - **AutoPause** *(boolean) --* 
        
                    A value that indicates whether automatic pause is allowed for the Aurora DB cluster in ``serverless`` DB engine mode. 
        
                  - **SecondsUntilAutoPause** *(integer) --* 
        
                    The remaining amount of time, in seconds, before the Aurora DB cluster in ``serverless`` mode is paused. A DB cluster can be paused only when it\'s idle (it has no connections).
        
                - **DeletionProtection** *(boolean) --* 
        
                  Indicates if the DB cluster has deletion protection enabled. The database can\'t be deleted when this value is set to true. 
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeDBEngineVersions(Paginator):
    def paginate(self, Engine: str = None, EngineVersion: str = None, DBParameterGroupFamily: str = None, Filters: List = None, DefaultOnly: bool = None, ListSupportedCharacterSets: bool = None, ListSupportedTimezones: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBEngineVersions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Engine=\'string\',
              EngineVersion=\'string\',
              DBParameterGroupFamily=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DefaultOnly=True|False,
              ListSupportedCharacterSets=True|False,
              ListSupportedTimezones=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              One or more filter values. Filter values are case-sensitive.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBEngineVersions\': [
                    {
                        \'Engine\': \'string\',
                        \'EngineVersion\': \'string\',
                        \'DBParameterGroupFamily\': \'string\',
                        \'DBEngineDescription\': \'string\',
                        \'DBEngineVersionDescription\': \'string\',
                        \'DefaultCharacterSet\': {
                            \'CharacterSetName\': \'string\',
                            \'CharacterSetDescription\': \'string\'
                        },
                        \'SupportedCharacterSets\': [
                            {
                                \'CharacterSetName\': \'string\',
                                \'CharacterSetDescription\': \'string\'
                            },
                        ],
                        \'ValidUpgradeTarget\': [
                            {
                                \'Engine\': \'string\',
                                \'EngineVersion\': \'string\',
                                \'Description\': \'string\',
                                \'AutoUpgrade\': True|False,
                                \'IsMajorVersionUpgrade\': True|False
                            },
                        ],
                        \'SupportedTimezones\': [
                            {
                                \'TimezoneName\': \'string\'
                            },
                        ],
                        \'ExportableLogTypes\': [
                            \'string\',
                        ],
                        \'SupportsLogExportsToCloudwatchLogs\': True|False,
                        \'SupportsReadReplica\': True|False,
                        \'SupportedEngineModes\': [
                            \'string\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeDBEngineVersions action. 
        
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
        
                    This data type is used as a response element in the action  DescribeDBEngineVersions . 
        
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
        
                    A time zone associated with a  DBInstance or a  DBSnapshot . This data type is an element in the response to the  DescribeDBInstances , the  DescribeDBSnapshots , and the  DescribeDBEngineVersions actions. 
        
                    - **TimezoneName** *(string) --* 
        
                      The name of the time zone.
        
                - **ExportableLogTypes** *(list) --* 
        
                  The types of logs that the database engine has available for export to CloudWatch Logs.
        
                  - *(string) --* 
              
                - **SupportsLogExportsToCloudwatchLogs** *(boolean) --* 
        
                  A value that indicates whether the engine version supports exporting the log types specified by ExportableLogTypes to CloudWatch Logs.
        
                - **SupportsReadReplica** *(boolean) --* 
        
                  Indicates whether the database engine version supports read replicas.
        
                - **SupportedEngineModes** *(list) --* 
        
                  A list of the supported DB engine modes.
        
                  - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeDBInstances(Paginator):
    def paginate(self, DBInstanceIdentifier: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBInstances>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DBInstanceIdentifier=\'string\',
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
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
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
                \'DBInstances\': [
                    {
                        \'DBInstanceIdentifier\': \'string\',
                        \'DBInstanceClass\': \'string\',
                        \'Engine\': \'string\',
                        \'DBInstanceStatus\': \'string\',
                        \'MasterUsername\': \'string\',
                        \'DBName\': \'string\',
                        \'Endpoint\': {
                            \'Address\': \'string\',
                            \'Port\': 123,
                            \'HostedZoneId\': \'string\'
                        },
                        \'AllocatedStorage\': 123,
                        \'InstanceCreateTime\': datetime(2015, 1, 1),
                        \'PreferredBackupWindow\': \'string\',
                        \'BackupRetentionPeriod\': 123,
                        \'DBSecurityGroups\': [
                            {
                                \'DBSecurityGroupName\': \'string\',
                                \'Status\': \'string\'
                            },
                        ],
                        \'VpcSecurityGroups\': [
                            {
                                \'VpcSecurityGroupId\': \'string\',
                                \'Status\': \'string\'
                            },
                        ],
                        \'DBParameterGroups\': [
                            {
                                \'DBParameterGroupName\': \'string\',
                                \'ParameterApplyStatus\': \'string\'
                            },
                        ],
                        \'AvailabilityZone\': \'string\',
                        \'DBSubnetGroup\': {
                            \'DBSubnetGroupName\': \'string\',
                            \'DBSubnetGroupDescription\': \'string\',
                            \'VpcId\': \'string\',
                            \'SubnetGroupStatus\': \'string\',
                            \'Subnets\': [
                                {
                                    \'SubnetIdentifier\': \'string\',
                                    \'SubnetAvailabilityZone\': {
                                        \'Name\': \'string\'
                                    },
                                    \'SubnetStatus\': \'string\'
                                },
                            ],
                            \'DBSubnetGroupArn\': \'string\'
                        },
                        \'PreferredMaintenanceWindow\': \'string\',
                        \'PendingModifiedValues\': {
                            \'DBInstanceClass\': \'string\',
                            \'AllocatedStorage\': 123,
                            \'MasterUserPassword\': \'string\',
                            \'Port\': 123,
                            \'BackupRetentionPeriod\': 123,
                            \'MultiAZ\': True|False,
                            \'EngineVersion\': \'string\',
                            \'LicenseModel\': \'string\',
                            \'Iops\': 123,
                            \'DBInstanceIdentifier\': \'string\',
                            \'StorageType\': \'string\',
                            \'CACertificateIdentifier\': \'string\',
                            \'DBSubnetGroupName\': \'string\',
                            \'PendingCloudwatchLogsExports\': {
                                \'LogTypesToEnable\': [
                                    \'string\',
                                ],
                                \'LogTypesToDisable\': [
                                    \'string\',
                                ]
                            },
                            \'ProcessorFeatures\': [
                                {
                                    \'Name\': \'string\',
                                    \'Value\': \'string\'
                                },
                            ]
                        },
                        \'LatestRestorableTime\': datetime(2015, 1, 1),
                        \'MultiAZ\': True|False,
                        \'EngineVersion\': \'string\',
                        \'AutoMinorVersionUpgrade\': True|False,
                        \'ReadReplicaSourceDBInstanceIdentifier\': \'string\',
                        \'ReadReplicaDBInstanceIdentifiers\': [
                            \'string\',
                        ],
                        \'ReadReplicaDBClusterIdentifiers\': [
                            \'string\',
                        ],
                        \'LicenseModel\': \'string\',
                        \'Iops\': 123,
                        \'OptionGroupMemberships\': [
                            {
                                \'OptionGroupName\': \'string\',
                                \'Status\': \'string\'
                            },
                        ],
                        \'CharacterSetName\': \'string\',
                        \'SecondaryAvailabilityZone\': \'string\',
                        \'PubliclyAccessible\': True|False,
                        \'StatusInfos\': [
                            {
                                \'StatusType\': \'string\',
                                \'Normal\': True|False,
                                \'Status\': \'string\',
                                \'Message\': \'string\'
                            },
                        ],
                        \'StorageType\': \'string\',
                        \'TdeCredentialArn\': \'string\',
                        \'DbInstancePort\': 123,
                        \'DBClusterIdentifier\': \'string\',
                        \'StorageEncrypted\': True|False,
                        \'KmsKeyId\': \'string\',
                        \'DbiResourceId\': \'string\',
                        \'CACertificateIdentifier\': \'string\',
                        \'DomainMemberships\': [
                            {
                                \'Domain\': \'string\',
                                \'Status\': \'string\',
                                \'FQDN\': \'string\',
                                \'IAMRoleName\': \'string\'
                            },
                        ],
                        \'CopyTagsToSnapshot\': True|False,
                        \'MonitoringInterval\': 123,
                        \'EnhancedMonitoringResourceArn\': \'string\',
                        \'MonitoringRoleArn\': \'string\',
                        \'PromotionTier\': 123,
                        \'DBInstanceArn\': \'string\',
                        \'Timezone\': \'string\',
                        \'IAMDatabaseAuthenticationEnabled\': True|False,
                        \'PerformanceInsightsEnabled\': True|False,
                        \'PerformanceInsightsKMSKeyId\': \'string\',
                        \'PerformanceInsightsRetentionPeriod\': 123,
                        \'EnabledCloudwatchLogsExports\': [
                            \'string\',
                        ],
                        \'ProcessorFeatures\': [
                            {
                                \'Name\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'DeletionProtection\': True|False,
                        \'ListenerEndpoint\': {
                            \'Address\': \'string\',
                            \'Port\': 123,
                            \'HostedZoneId\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeDBInstances action. 
        
            - **DBInstances** *(list) --* 
        
              A list of  DBInstance instances. 
        
              - *(dict) --* 
        
                Contains the details of an Amazon RDS DB instance. 
        
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
        
                  The meaning of this parameter differs according to the database engine you use. For example, this value returns MySQL, MariaDB, or PostgreSQL information when returning values from CreateDBInstanceReadReplica since Read Replicas are only supported for these engines.
        
                   **MySQL, MariaDB, SQL Server, PostgreSQL**  
        
                  Contains the name of the initial database of this instance that was provided at create time, if one was specified when the DB instance was created. This same name is returned for the life of the DB instance.
        
                  Type: String
        
                   **Oracle**  
        
                  Contains the Oracle System ID (SID) of the created DB instance. Not shown when the returned parameters do not apply to an Oracle DB instance.
        
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
        
                    This data type is used as a response element in the following actions:
        
                    *  ModifyDBInstance   
                     
                    *  RebootDBInstance   
                     
                    *  RestoreDBInstanceFromDBSnapshot   
                     
                    *  RestoreDBInstanceToPointInTime   
                     
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
                     
                    *  CreateDBInstanceReadReplica   
                     
                    *  DeleteDBInstance   
                     
                    *  ModifyDBInstance   
                     
                    *  RebootDBInstance   
                     
                    *  RestoreDBInstanceFromDBSnapshot   
                     
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
        
                      This data type is used as a response element in the  DescribeDBSubnetGroups action. 
        
                      - **SubnetIdentifier** *(string) --* 
        
                        Specifies the identifier of the subnet.
        
                      - **SubnetAvailabilityZone** *(dict) --* 
        
                        Contains Availability Zone information.
        
                        This data type is used as an element in the following data type:
        
                        *  OrderableDBInstanceOption   
                         
                        - **Name** *(string) --* 
        
                          The name of the Availability Zone.
        
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
        
                    A list of the log types whose configuration is still pending. In other words, these log types are in the process of being activated or deactivated.
        
                    - **LogTypesToEnable** *(list) --* 
        
                      Log types that are in the process of being deactivated. After they are deactivated, these log types aren\'t exported to CloudWatch Logs.
        
                      - *(string) --* 
                  
                    - **LogTypesToDisable** *(list) --* 
        
                      Log types that are in the process of being enabled. After they are enabled, these log types are exported to CloudWatch Logs.
        
                      - *(string) --* 
                  
                  - **ProcessorFeatures** *(list) --* 
        
                    The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.
        
                    - *(dict) --* 
        
                      Contains the processor features of a DB instance class.
        
                      To specify the number of CPU cores, use the ``coreCount`` feature name for the ``Name`` parameter. To specify the number of threads per core, use the ``threadsPerCore`` feature name for the ``Name`` parameter.
        
                      You can set the processor features of the DB instance class for a DB instance when you call one of the following actions:
        
                      *  CreateDBInstance   
                       
                      *  ModifyDBInstance   
                       
                      *  RestoreDBInstanceFromDBSnapshot   
                       
                      *  RestoreDBInstanceFromS3   
                       
                      *  RestoreDBInstanceToPointInTime   
                       
                      You can view the valid processor values for a particular instance class by calling the  DescribeOrderableDBInstanceOptions action and specifying the instance class for the ``DBInstanceClass`` parameter.
        
                      In addition, you can use the following actions for DB instance class processor information:
        
                      *  DescribeDBInstances   
                       
                      *  DescribeDBSnapshots   
                       
                      *  DescribeValidDBInstanceModifications   
                       
                      For more information, see `Configuring the Processor of the DB Instance Class <http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor>`__ in the *Amazon RDS User Guide.*  
        
                      - **Name** *(string) --* 
        
                        The name of the processor feature. Valid names are ``coreCount`` and ``threadsPerCore`` .
        
                      - **Value** *(string) --* 
        
                        The value of a processor feature name.
        
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
        
                  Contains one or more identifiers of Aurora DB clusters to which the RDS DB instance is replicated as a Read Replica. For example, when you create an Aurora Read Replica of an RDS MySQL DB instance, the Aurora MySQL DB cluster for the Aurora Read Replica is shown. This output does not contain information about cross region Aurora Read Replicas.
        
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
        
                      The status of the DB instance\'s option group membership. Valid values are: ``in-sync`` , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` , ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` . 
        
                - **CharacterSetName** *(string) --* 
        
                  If present, specifies the name of the character set that this instance is associated with.
        
                - **SecondaryAvailabilityZone** *(string) --* 
        
                  If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  Specifies the accessibility options for the DB instance. A value of true specifies an Internet-facing instance with a publicly resolvable DNS name, which resolves to a public IP address. A value of false specifies an internal instance with a DNS name that resolves to a private IP address.
        
                - **StatusInfos** *(list) --* 
        
                  The status of a Read Replica. If the instance is not a Read Replica, this is blank.
        
                  - *(dict) --* 
        
                    Provides a list of status information for a DB instance.
        
                    - **StatusType** *(string) --* 
        
                      This value is currently \"read replication.\"
        
                    - **Normal** *(boolean) --* 
        
                      Boolean value that is true if the instance is operating normally, or false if the instance is in an error state.
        
                    - **Status** *(string) --* 
        
                      Status of the DB instance. For a StatusType of read replica, the values can be replicating, replication stop point set, replication stop point reached, error, stopped, or terminated.
        
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
        
                  Specifies whether the DB instance is encrypted.
        
                - **KmsKeyId** *(string) --* 
        
                  If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB instance. 
        
                - **DbiResourceId** *(string) --* 
        
                  The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.
        
                - **CACertificateIdentifier** *(string) --* 
        
                  The identifier of the CA certificate for this DB instance.
        
                - **DomainMemberships** *(list) --* 
        
                  The Active Directory Domain membership records associated with the DB instance.
        
                  - *(dict) --* 
        
                    An Active Directory Domain membership record associated with the DB instance.
        
                    - **Domain** *(string) --* 
        
                      The identifier of the Active Directory Domain.
        
                    - **Status** *(string) --* 
        
                      The status of the DB instance\'s Active Directory Domain membership, such as joined, pending-join, failed etc).
        
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
        
                  The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.
        
                - **PromotionTier** *(integer) --* 
        
                  A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see `Fault Tolerance for an Aurora DB Cluster <http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html#Aurora.Managing.FaultTolerance>`__ in the *Amazon Aurora User Guide* . 
        
                - **DBInstanceArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) for the DB instance.
        
                - **Timezone** *(string) --* 
        
                  The time zone of the DB instance. In most cases, the ``Timezone`` element is empty. ``Timezone`` content appears only for Microsoft SQL Server DB instances that were created with a time zone specified. 
        
                - **IAMDatabaseAuthenticationEnabled** *(boolean) --* 
        
                  True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.
        
                  IAM database authentication can be enabled for the following database engines
        
                  * For MySQL 5.6, minor version 5.6.34 or higher 
                   
                  * For MySQL 5.7, minor version 5.7.16 or higher 
                   
                  * Aurora 5.6 or higher. To enable IAM database authentication for Aurora, see DBCluster Type. 
                   
                - **PerformanceInsightsEnabled** *(boolean) --* 
        
                  True if Performance Insights is enabled for the DB instance, and otherwise false.
        
                - **PerformanceInsightsKMSKeyId** *(string) --* 
        
                  The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.
        
                - **PerformanceInsightsRetentionPeriod** *(integer) --* 
        
                  The amount of time, in days, to retain Performance Insights data. Valid values are 7 or 731 (2 years). 
        
                - **EnabledCloudwatchLogsExports** *(list) --* 
        
                  A list of log types that this DB instance is configured to export to CloudWatch Logs.
        
                  Log types vary by DB engine. For information about the log types for each DB engine, see `Amazon RDS Database Log Files <http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html>`__ in the *Amazon RDS User Guide.*  
        
                  - *(string) --* 
              
                - **ProcessorFeatures** *(list) --* 
        
                  The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.
        
                  - *(dict) --* 
        
                    Contains the processor features of a DB instance class.
        
                    To specify the number of CPU cores, use the ``coreCount`` feature name for the ``Name`` parameter. To specify the number of threads per core, use the ``threadsPerCore`` feature name for the ``Name`` parameter.
        
                    You can set the processor features of the DB instance class for a DB instance when you call one of the following actions:
        
                    *  CreateDBInstance   
                     
                    *  ModifyDBInstance   
                     
                    *  RestoreDBInstanceFromDBSnapshot   
                     
                    *  RestoreDBInstanceFromS3   
                     
                    *  RestoreDBInstanceToPointInTime   
                     
                    You can view the valid processor values for a particular instance class by calling the  DescribeOrderableDBInstanceOptions action and specifying the instance class for the ``DBInstanceClass`` parameter.
        
                    In addition, you can use the following actions for DB instance class processor information:
        
                    *  DescribeDBInstances   
                     
                    *  DescribeDBSnapshots   
                     
                    *  DescribeValidDBInstanceModifications   
                     
                    For more information, see `Configuring the Processor of the DB Instance Class <http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor>`__ in the *Amazon RDS User Guide.*  
        
                    - **Name** *(string) --* 
        
                      The name of the processor feature. Valid names are ``coreCount`` and ``threadsPerCore`` .
        
                    - **Value** *(string) --* 
        
                      The value of a processor feature name.
        
                - **DeletionProtection** *(boolean) --* 
        
                  Indicates if the DB instance has deletion protection enabled. The database can\'t be deleted when this value is set to true. For more information, see `Deleting a DB Instance <http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html>`__ . 
        
                - **ListenerEndpoint** *(dict) --* 
        
                  Specifies the listener connection endpoint for SQL Server Always On.
        
                  - **Address** *(string) --* 
        
                    Specifies the DNS address of the DB instance.
        
                  - **Port** *(integer) --* 
        
                    Specifies the port that the database engine is listening on.
        
                  - **HostedZoneId** *(string) --* 
        
                    Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeDBLogFiles(Paginator):
    def paginate(self, DBInstanceIdentifier: str, FilenameContains: str = None, FileLastWritten: int = None, FileSize: int = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBLogFiles>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DBInstanceIdentifier=\'string\',
              FilenameContains=\'string\',
              FileLastWritten=123,
              FileSize=123,
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
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: **[REQUIRED]** 
        
          The customer-assigned name of the DB instance that contains the log files you want to list.
        
          Constraints:
        
          * Must match the identifier of an existing DBInstance. 
           
        :type FilenameContains: string
        :param FilenameContains: 
        
          Filters the available log files for log file names that contain the specified string.
        
        :type FileLastWritten: integer
        :param FileLastWritten: 
        
          Filters the available log files for files written since the specified date, in POSIX timestamp format with milliseconds.
        
        :type FileSize: integer
        :param FileSize: 
        
          Filters the available log files for files larger than the specified size.
        
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
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
                \'DescribeDBLogFiles\': [
                    {
                        \'LogFileName\': \'string\',
                        \'LastWritten\': 123,
                        \'Size\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The response from a call to  DescribeDBLogFiles . 
        
            - **DescribeDBLogFiles** *(list) --* 
        
              The DB log files returned.
        
              - *(dict) --* 
        
                This data type is used as a response element to  DescribeDBLogFiles .
        
                - **LogFileName** *(string) --* 
        
                  The name of the log file for the specified DB instance.
        
                - **LastWritten** *(integer) --* 
        
                  A POSIX timestamp when the last log entry was written.
        
                - **Size** *(integer) --* 
        
                  The size, in bytes, of the log file for the specified DB instance.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeDBParameterGroups(Paginator):
    def paginate(self, DBParameterGroupName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBParameterGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DBParameterGroupName=\'string\',
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
        :type DBParameterGroupName: string
        :param DBParameterGroupName: 
        
          The name of a specific DB parameter group to return details for.
        
          Constraints:
        
          * If supplied, must match the name of an existing DBClusterParameterGroup. 
           
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
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
                \'DBParameterGroups\': [
                    {
                        \'DBParameterGroupName\': \'string\',
                        \'DBParameterGroupFamily\': \'string\',
                        \'Description\': \'string\',
                        \'DBParameterGroupArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeDBParameterGroups action. 
        
            - **DBParameterGroups** *(list) --* 
        
              A list of  DBParameterGroup instances. 
        
              - *(dict) --* 
        
                Contains the details of an Amazon RDS DB parameter group. 
        
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
        
        """
        pass


class DescribeDBParameters(Paginator):
    def paginate(self, DBParameterGroupName: str, Source: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBParameters>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DBParameterGroupName=\'string\',
              Source=\'string\',
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
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
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
                \'Parameters\': [
                    {
                        \'ParameterName\': \'string\',
                        \'ParameterValue\': \'string\',
                        \'Description\': \'string\',
                        \'Source\': \'string\',
                        \'ApplyType\': \'string\',
                        \'DataType\': \'string\',
                        \'AllowedValues\': \'string\',
                        \'IsModifiable\': True|False,
                        \'MinimumEngineVersion\': \'string\',
                        \'ApplyMethod\': \'immediate\'|\'pending-reboot\',
                        \'SupportedEngineModes\': [
                            \'string\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeDBParameters action. 
        
            - **Parameters** *(list) --* 
        
              A list of  Parameter values. 
        
              - *(dict) --* 
        
                This data type is used as a request parameter in the  ModifyDBParameterGroup and  ResetDBParameterGroup actions. 
        
                This data type is used as a response element in the  DescribeEngineDefaultParameters and  DescribeDBParameters actions.
        
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
        
                - **SupportedEngineModes** *(list) --* 
        
                  The valid DB engine modes.
        
                  - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeDBSecurityGroups(Paginator):
    def paginate(self, DBSecurityGroupName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBSecurityGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DBSecurityGroupName=\'string\',
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
        :type DBSecurityGroupName: string
        :param DBSecurityGroupName: 
        
          The name of the DB security group to return details for.
        
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
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
                \'DBSecurityGroups\': [
                    {
                        \'OwnerId\': \'string\',
                        \'DBSecurityGroupName\': \'string\',
                        \'DBSecurityGroupDescription\': \'string\',
                        \'VpcId\': \'string\',
                        \'EC2SecurityGroups\': [
                            {
                                \'Status\': \'string\',
                                \'EC2SecurityGroupName\': \'string\',
                                \'EC2SecurityGroupId\': \'string\',
                                \'EC2SecurityGroupOwnerId\': \'string\'
                            },
                        ],
                        \'IPRanges\': [
                            {
                                \'Status\': \'string\',
                                \'CIDRIP\': \'string\'
                            },
                        ],
                        \'DBSecurityGroupArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeDBSecurityGroups action. 
        
            - **DBSecurityGroups** *(list) --* 
        
              A list of  DBSecurityGroup instances. 
        
              - *(dict) --* 
        
                Contains the details for an Amazon RDS DB security group. 
        
                This data type is used as a response element in the  DescribeDBSecurityGroups action. 
        
                - **OwnerId** *(string) --* 
        
                  Provides the AWS ID of the owner of a specific DB security group.
        
                - **DBSecurityGroupName** *(string) --* 
        
                  Specifies the name of the DB security group.
        
                - **DBSecurityGroupDescription** *(string) --* 
        
                  Provides the description of the DB security group.
        
                - **VpcId** *(string) --* 
        
                  Provides the VpcId of the DB security group.
        
                - **EC2SecurityGroups** *(list) --* 
        
                  Contains a list of  EC2SecurityGroup elements. 
        
                  - *(dict) --* 
        
                    This data type is used as a response element in the following actions:
        
                    *  AuthorizeDBSecurityGroupIngress   
                     
                    *  DescribeDBSecurityGroups   
                     
                    *  RevokeDBSecurityGroupIngress   
                     
                    - **Status** *(string) --* 
        
                      Provides the status of the EC2 security group. Status can be \"authorizing\", \"authorized\", \"revoking\", and \"revoked\".
        
                    - **EC2SecurityGroupName** *(string) --* 
        
                      Specifies the name of the EC2 security group.
        
                    - **EC2SecurityGroupId** *(string) --* 
        
                      Specifies the id of the EC2 security group.
        
                    - **EC2SecurityGroupOwnerId** *(string) --* 
        
                      Specifies the AWS ID of the owner of the EC2 security group specified in the ``EC2SecurityGroupName`` field. 
        
                - **IPRanges** *(list) --* 
        
                  Contains a list of  IPRange elements. 
        
                  - *(dict) --* 
        
                    This data type is used as a response element in the  DescribeDBSecurityGroups action. 
        
                    - **Status** *(string) --* 
        
                      Specifies the status of the IP range. Status can be \"authorizing\", \"authorized\", \"revoking\", and \"revoked\".
        
                    - **CIDRIP** *(string) --* 
        
                      Specifies the IP range.
        
                - **DBSecurityGroupArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) for the DB security group.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeDBSnapshots(Paginator):
    def paginate(self, DBInstanceIdentifier: str = None, DBSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, IncludeShared: bool = None, IncludePublic: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBSnapshots>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DBInstanceIdentifier=\'string\',
              DBSnapshotIdentifier=\'string\',
              SnapshotType=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              IncludeShared=True|False,
              IncludePublic=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: 
        
          The ID of the DB instance to retrieve the list of DB snapshots for. This parameter can\'t be used in conjunction with ``DBSnapshotIdentifier`` . This parameter is not case-sensitive. 
        
          Constraints:
        
          * If supplied, must match the identifier of an existing DBInstance. 
           
        :type DBSnapshotIdentifier: string
        :param DBSnapshotIdentifier: 
        
          A specific DB snapshot identifier to describe. This parameter can\'t be used in conjunction with ``DBInstanceIdentifier`` . This value is stored as a lowercase string. 
        
          Constraints:
        
          * If supplied, must match the identifier of an existing DBSnapshot. 
           
          * If this identifier is for an automated snapshot, the ``SnapshotType`` parameter must also be specified. 
           
        :type SnapshotType: string
        :param SnapshotType: 
        
          The type of snapshots to be returned. You can specify one of the following values:
        
          * ``automated`` - Return all DB snapshots that have been automatically taken by Amazon RDS for my AWS account. 
           
          * ``manual`` - Return all DB snapshots that have been taken by my AWS account. 
           
          * ``shared`` - Return all manual DB snapshots that have been shared to my AWS account. 
           
          * ``public`` - Return all DB snapshots that have been marked as public. 
           
          If you don\'t specify a ``SnapshotType`` value, then both automated and manual snapshots are returned. Shared and public DB snapshots are not included in the returned results by default. You can include shared snapshots with these results by setting the ``IncludeShared`` parameter to ``true`` . You can include public snapshots with these results by setting the ``IncludePublic`` parameter to ``true`` .
        
          The ``IncludeShared`` and ``IncludePublic`` parameters don\'t apply for ``SnapshotType`` values of ``manual`` or ``automated`` . The ``IncludePublic`` parameter doesn\'t apply when ``SnapshotType`` is set to ``shared`` . The ``IncludeShared`` parameter doesn\'t apply when ``SnapshotType`` is set to ``public`` .
        
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type IncludeShared: boolean
        :param IncludeShared: 
        
          True to include shared manual DB snapshots from other AWS accounts that this AWS account has been given permission to copy or restore, and otherwise false. The default is ``false`` .
        
          You can give an AWS account permission to restore a manual DB snapshot from another AWS account by using the  ModifyDBSnapshotAttribute API action.
        
        :type IncludePublic: boolean
        :param IncludePublic: 
        
          True to include manual DB snapshots that are public and can be copied or restored by any AWS account, and otherwise false. The default is false.
        
          You can share a manual DB snapshot as public by using the  ModifyDBSnapshotAttribute API.
        
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
                \'DBSnapshots\': [
                    {
                        \'DBSnapshotIdentifier\': \'string\',
                        \'DBInstanceIdentifier\': \'string\',
                        \'SnapshotCreateTime\': datetime(2015, 1, 1),
                        \'Engine\': \'string\',
                        \'AllocatedStorage\': 123,
                        \'Status\': \'string\',
                        \'Port\': 123,
                        \'AvailabilityZone\': \'string\',
                        \'VpcId\': \'string\',
                        \'InstanceCreateTime\': datetime(2015, 1, 1),
                        \'MasterUsername\': \'string\',
                        \'EngineVersion\': \'string\',
                        \'LicenseModel\': \'string\',
                        \'SnapshotType\': \'string\',
                        \'Iops\': 123,
                        \'OptionGroupName\': \'string\',
                        \'PercentProgress\': 123,
                        \'SourceRegion\': \'string\',
                        \'SourceDBSnapshotIdentifier\': \'string\',
                        \'StorageType\': \'string\',
                        \'TdeCredentialArn\': \'string\',
                        \'Encrypted\': True|False,
                        \'KmsKeyId\': \'string\',
                        \'DBSnapshotArn\': \'string\',
                        \'Timezone\': \'string\',
                        \'IAMDatabaseAuthenticationEnabled\': True|False,
                        \'ProcessorFeatures\': [
                            {
                                \'Name\': \'string\',
                                \'Value\': \'string\'
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeDBSnapshots action. 
        
            - **DBSnapshots** *(list) --* 
        
              A list of  DBSnapshot instances. 
        
              - *(dict) --* 
        
                Contains the details of an Amazon RDS DB snapshot. 
        
                This data type is used as a response element in the  DescribeDBSnapshots action. 
        
                - **DBSnapshotIdentifier** *(string) --* 
        
                  Specifies the identifier for the DB snapshot.
        
                - **DBInstanceIdentifier** *(string) --* 
        
                  Specifies the DB instance identifier of the DB instance this DB snapshot was created from.
        
                - **SnapshotCreateTime** *(datetime) --* 
        
                  Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).
        
                - **Engine** *(string) --* 
        
                  Specifies the name of the database engine.
        
                - **AllocatedStorage** *(integer) --* 
        
                  Specifies the allocated storage size in gibibytes (GiB).
        
                - **Status** *(string) --* 
        
                  Specifies the status of this DB snapshot.
        
                - **Port** *(integer) --* 
        
                  Specifies the port that the database engine was listening on at the time of the snapshot.
        
                - **AvailabilityZone** *(string) --* 
        
                  Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.
        
                - **VpcId** *(string) --* 
        
                  Provides the VPC ID associated with the DB snapshot.
        
                - **InstanceCreateTime** *(datetime) --* 
        
                  Specifies the time when the snapshot was taken, in Universal Coordinated Time (UTC).
        
                - **MasterUsername** *(string) --* 
        
                  Provides the master username for the DB snapshot.
        
                - **EngineVersion** *(string) --* 
        
                  Specifies the version of the database engine.
        
                - **LicenseModel** *(string) --* 
        
                  License model information for the restored DB instance.
        
                - **SnapshotType** *(string) --* 
        
                  Provides the type of the DB snapshot.
        
                - **Iops** *(integer) --* 
        
                  Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.
        
                - **OptionGroupName** *(string) --* 
        
                  Provides the option group name for the DB snapshot.
        
                - **PercentProgress** *(integer) --* 
        
                  The percentage of the estimated data that has been transferred.
        
                - **SourceRegion** *(string) --* 
        
                  The AWS Region that the DB snapshot was created in or copied from.
        
                - **SourceDBSnapshotIdentifier** *(string) --* 
        
                  The DB snapshot Amazon Resource Name (ARN) that the DB snapshot was copied from. It only has value in case of cross-customer or cross-region copy.
        
                - **StorageType** *(string) --* 
        
                  Specifies the storage type associated with DB snapshot.
        
                - **TdeCredentialArn** *(string) --* 
        
                  The ARN from the key store with which to associate the instance for TDE encryption.
        
                - **Encrypted** *(boolean) --* 
        
                  Specifies whether the DB snapshot is encrypted.
        
                - **KmsKeyId** *(string) --* 
        
                  If ``Encrypted`` is true, the AWS KMS key identifier for the encrypted DB snapshot. 
        
                - **DBSnapshotArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) for the DB snapshot.
        
                - **Timezone** *(string) --* 
        
                  The time zone of the DB snapshot. In most cases, the ``Timezone`` element is empty. ``Timezone`` content appears only for snapshots taken from Microsoft SQL Server DB instances that were created with a time zone specified. 
        
                - **IAMDatabaseAuthenticationEnabled** *(boolean) --* 
        
                  True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.
        
                - **ProcessorFeatures** *(list) --* 
        
                  The number of CPU cores and the number of threads per core for the DB instance class of the DB instance when the DB snapshot was created.
        
                  - *(dict) --* 
        
                    Contains the processor features of a DB instance class.
        
                    To specify the number of CPU cores, use the ``coreCount`` feature name for the ``Name`` parameter. To specify the number of threads per core, use the ``threadsPerCore`` feature name for the ``Name`` parameter.
        
                    You can set the processor features of the DB instance class for a DB instance when you call one of the following actions:
        
                    *  CreateDBInstance   
                     
                    *  ModifyDBInstance   
                     
                    *  RestoreDBInstanceFromDBSnapshot   
                     
                    *  RestoreDBInstanceFromS3   
                     
                    *  RestoreDBInstanceToPointInTime   
                     
                    You can view the valid processor values for a particular instance class by calling the  DescribeOrderableDBInstanceOptions action and specifying the instance class for the ``DBInstanceClass`` parameter.
        
                    In addition, you can use the following actions for DB instance class processor information:
        
                    *  DescribeDBInstances   
                     
                    *  DescribeDBSnapshots   
                     
                    *  DescribeValidDBInstanceModifications   
                     
                    For more information, see `Configuring the Processor of the DB Instance Class <http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor>`__ in the *Amazon RDS User Guide.*  
        
                    - **Name** *(string) --* 
        
                      The name of the processor feature. Valid names are ``coreCount`` and ``threadsPerCore`` .
        
                    - **Value** *(string) --* 
        
                      The value of a processor feature name.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeDBSubnetGroups(Paginator):
    def paginate(self, DBSubnetGroupName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBSubnetGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DBSubnetGroupName=\'string\',
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
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName: 
        
          The name of the DB subnet group to return details for.
        
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
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
                \'DBSubnetGroups\': [
                    {
                        \'DBSubnetGroupName\': \'string\',
                        \'DBSubnetGroupDescription\': \'string\',
                        \'VpcId\': \'string\',
                        \'SubnetGroupStatus\': \'string\',
                        \'Subnets\': [
                            {
                                \'SubnetIdentifier\': \'string\',
                                \'SubnetAvailabilityZone\': {
                                    \'Name\': \'string\'
                                },
                                \'SubnetStatus\': \'string\'
                            },
                        ],
                        \'DBSubnetGroupArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeDBSubnetGroups action. 
        
            - **DBSubnetGroups** *(list) --* 
        
              A list of  DBSubnetGroup instances. 
        
              - *(dict) --* 
        
                Contains the details of an Amazon RDS DB subnet group. 
        
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
        
                    This data type is used as a response element in the  DescribeDBSubnetGroups action. 
        
                    - **SubnetIdentifier** *(string) --* 
        
                      Specifies the identifier of the subnet.
        
                    - **SubnetAvailabilityZone** *(dict) --* 
        
                      Contains Availability Zone information.
        
                      This data type is used as an element in the following data type:
        
                      *  OrderableDBInstanceOption   
                       
                      - **Name** *(string) --* 
        
                        The name of the Availability Zone.
        
                    - **SubnetStatus** *(string) --* 
        
                      Specifies the status of the subnet.
        
                - **DBSubnetGroupArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) for the DB subnet group.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeEngineDefaultParameters(Paginator):
    def paginate(self, DBParameterGroupFamily: str, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeEngineDefaultParameters>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DBParameterGroupFamily=\'string\',
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
        :type DBParameterGroupFamily: string
        :param DBParameterGroupFamily: **[REQUIRED]** 
        
          The name of the DB parameter group family.
        
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
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
                \'EngineDefaults\': {
                    \'DBParameterGroupFamily\': \'string\',
                    \'Marker\': \'string\',
                    \'Parameters\': [
                        {
                            \'ParameterName\': \'string\',
                            \'ParameterValue\': \'string\',
                            \'Description\': \'string\',
                            \'Source\': \'string\',
                            \'ApplyType\': \'string\',
                            \'DataType\': \'string\',
                            \'AllowedValues\': \'string\',
                            \'IsModifiable\': True|False,
                            \'MinimumEngineVersion\': \'string\',
                            \'ApplyMethod\': \'immediate\'|\'pending-reboot\',
                            \'SupportedEngineModes\': [
                                \'string\',
                            ]
                        },
                    ]
                },
                \'NextToken\': \'string\'
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
        
                  This data type is used as a request parameter in the  ModifyDBParameterGroup and  ResetDBParameterGroup actions. 
        
                  This data type is used as a response element in the  DescribeEngineDefaultParameters and  DescribeDBParameters actions.
        
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
        
                  - **SupportedEngineModes** *(list) --* 
        
                    The valid DB engine modes.
        
                    - *(string) --* 
                
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeEventSubscriptions(Paginator):
    def paginate(self, SubscriptionName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeEventSubscriptions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SubscriptionName=\'string\',
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
        :type SubscriptionName: string
        :param SubscriptionName: 
        
          The name of the RDS event notification subscription you want to describe.
        
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
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
                \'EventSubscriptionsList\': [
                    {
                        \'CustomerAwsId\': \'string\',
                        \'CustSubscriptionId\': \'string\',
                        \'SnsTopicArn\': \'string\',
                        \'Status\': \'string\',
                        \'SubscriptionCreationTime\': \'string\',
                        \'SourceType\': \'string\',
                        \'SourceIdsList\': [
                            \'string\',
                        ],
                        \'EventCategoriesList\': [
                            \'string\',
                        ],
                        \'Enabled\': True|False,
                        \'EventSubscriptionArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Data returned by the **DescribeEventSubscriptions** action.
        
            - **EventSubscriptionsList** *(list) --* 
        
              A list of EventSubscriptions data types.
        
              - *(dict) --* 
        
                Contains the results of a successful invocation of the  DescribeEventSubscriptions action.
        
                - **CustomerAwsId** *(string) --* 
        
                  The AWS customer account associated with the RDS event notification subscription.
        
                - **CustSubscriptionId** *(string) --* 
        
                  The RDS event notification subscription Id.
        
                - **SnsTopicArn** *(string) --* 
        
                  The topic ARN of the RDS event notification subscription.
        
                - **Status** *(string) --* 
        
                  The status of the RDS event notification subscription.
        
                  Constraints:
        
                  Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
        
                  The status \"no-permission\" indicates that RDS no longer has permission to post to the SNS topic. The status \"topic-not-exist\" indicates that the topic was deleted after the subscription was created.
        
                - **SubscriptionCreationTime** *(string) --* 
        
                  The time the RDS event notification subscription was created.
        
                - **SourceType** *(string) --* 
        
                  The source type for the RDS event notification subscription.
        
                - **SourceIdsList** *(list) --* 
        
                  A list of source IDs for the RDS event notification subscription.
        
                  - *(string) --* 
              
                - **EventCategoriesList** *(list) --* 
        
                  A list of event categories for the RDS event notification subscription.
        
                  - *(string) --* 
              
                - **Enabled** *(boolean) --* 
        
                  A Boolean value indicating if the subscription is enabled. True indicates the subscription is enabled.
        
                - **EventSubscriptionArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) for the event subscription.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeEvents(Paginator):
    def paginate(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, EventCategories: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeEvents>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SourceIdentifier=\'string\',
              SourceType=\'db-instance\'|\'db-parameter-group\'|\'db-security-group\'|\'db-snapshot\'|\'db-cluster\'|\'db-cluster-snapshot\',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Duration=123,
              EventCategories=[
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
        :type SourceIdentifier: string
        :param SourceIdentifier: 
        
          The identifier of the event source for which events are returned. If not specified, then all sources are included in the response.
        
          Constraints:
        
          * If SourceIdentifier is supplied, SourceType must also be provided. 
           
          * If the source type is ``DBInstance`` , then a ``DBInstanceIdentifier`` must be supplied. 
           
          * If the source type is ``DBSecurityGroup`` , a ``DBSecurityGroupName`` must be supplied. 
           
          * If the source type is ``DBParameterGroup`` , a ``DBParameterGroupName`` must be supplied. 
           
          * If the source type is ``DBSnapshot`` , a ``DBSnapshotIdentifier`` must be supplied. 
           
          * Can\'t end with a hyphen or contain two consecutive hyphens. 
           
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
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
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
                \'Events\': [
                    {
                        \'SourceIdentifier\': \'string\',
                        \'SourceType\': \'db-instance\'|\'db-parameter-group\'|\'db-security-group\'|\'db-snapshot\'|\'db-cluster\'|\'db-cluster-snapshot\',
                        \'Message\': \'string\',
                        \'EventCategories\': [
                            \'string\',
                        ],
                        \'Date\': datetime(2015, 1, 1),
                        \'SourceArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeEvents action. 
        
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
        
        """
        pass


class DescribeOptionGroupOptions(Paginator):
    def paginate(self, EngineName: str, MajorEngineVersion: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeOptionGroupOptions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              EngineName=\'string\',
              MajorEngineVersion=\'string\',
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
        :type EngineName: string
        :param EngineName: **[REQUIRED]** 
        
          A required parameter. Options available for the given engine name are described.
        
        :type MajorEngineVersion: string
        :param MajorEngineVersion: 
        
          If specified, filters the results to include only options for the specified major engine version.
        
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
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
                \'OptionGroupOptions\': [
                    {
                        \'Name\': \'string\',
                        \'Description\': \'string\',
                        \'EngineName\': \'string\',
                        \'MajorEngineVersion\': \'string\',
                        \'MinimumRequiredMinorEngineVersion\': \'string\',
                        \'PortRequired\': True|False,
                        \'DefaultPort\': 123,
                        \'OptionsDependedOn\': [
                            \'string\',
                        ],
                        \'OptionsConflictsWith\': [
                            \'string\',
                        ],
                        \'Persistent\': True|False,
                        \'Permanent\': True|False,
                        \'RequiresAutoMinorEngineVersionUpgrade\': True|False,
                        \'VpcOnly\': True|False,
                        \'SupportsOptionVersionDowngrade\': True|False,
                        \'OptionGroupOptionSettings\': [
                            {
                                \'SettingName\': \'string\',
                                \'SettingDescription\': \'string\',
                                \'DefaultValue\': \'string\',
                                \'ApplyType\': \'string\',
                                \'AllowedValues\': \'string\',
                                \'IsModifiable\': True|False,
                                \'IsRequired\': True|False,
                                \'MinimumEngineVersionPerAllowedValue\': [
                                    {
                                        \'AllowedValue\': \'string\',
                                        \'MinimumEngineVersion\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'OptionGroupOptionVersions\': [
                            {
                                \'Version\': \'string\',
                                \'IsDefault\': True|False
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **OptionGroupOptions** *(list) --* 
        
              List of available option group options.
        
              - *(dict) --* 
        
                Available option.
        
                - **Name** *(string) --* 
        
                  The name of the option.
        
                - **Description** *(string) --* 
        
                  The description of the option.
        
                - **EngineName** *(string) --* 
        
                  The name of the engine that this option can be applied to.
        
                - **MajorEngineVersion** *(string) --* 
        
                  Indicates the major engine version that the option is available for.
        
                - **MinimumRequiredMinorEngineVersion** *(string) --* 
        
                  The minimum required engine version for the option to be applied.
        
                - **PortRequired** *(boolean) --* 
        
                  Specifies whether the option requires a port.
        
                - **DefaultPort** *(integer) --* 
        
                  If the option requires a port, specifies the default port for the option.
        
                - **OptionsDependedOn** *(list) --* 
        
                  The options that are prerequisites for this option.
        
                  - *(string) --* 
              
                - **OptionsConflictsWith** *(list) --* 
        
                  The options that conflict with this option.
        
                  - *(string) --* 
              
                - **Persistent** *(boolean) --* 
        
                  Persistent options can\'t be removed from an option group while DB instances are associated with the option group. If you disassociate all DB instances from the option group, your can remove the persistent option from the option group.
        
                - **Permanent** *(boolean) --* 
        
                  Permanent options can never be removed from an option group. An option group containing a permanent option can\'t be removed from a DB instance.
        
                - **RequiresAutoMinorEngineVersionUpgrade** *(boolean) --* 
        
                  If true, you must enable the Auto Minor Version Upgrade setting for your DB instance before you can use this option. You can enable Auto Minor Version Upgrade when you first create your DB instance, or by modifying your DB instance later. 
        
                - **VpcOnly** *(boolean) --* 
        
                  If true, you can only use this option with a DB instance that is in a VPC. 
        
                - **SupportsOptionVersionDowngrade** *(boolean) --* 
        
                  If true, you can change the option to an earlier version of the option. This only applies to options that have different versions available. 
        
                - **OptionGroupOptionSettings** *(list) --* 
        
                  The option settings that are available (and the default value) for each option in an option group.
        
                  - *(dict) --* 
        
                    Option group option settings are used to display settings available for each option with their default values and other information. These values are used with the DescribeOptionGroupOptions action.
        
                    - **SettingName** *(string) --* 
        
                      The name of the option group option.
        
                    - **SettingDescription** *(string) --* 
        
                      The description of the option group option.
        
                    - **DefaultValue** *(string) --* 
        
                      The default value for the option group option.
        
                    - **ApplyType** *(string) --* 
        
                      The DB engine specific parameter type for the option group option.
        
                    - **AllowedValues** *(string) --* 
        
                      Indicates the acceptable values for the option group option.
        
                    - **IsModifiable** *(boolean) --* 
        
                      Boolean value where true indicates that this option group option can be changed from the default value.
        
                    - **IsRequired** *(boolean) --* 
        
                      Boolean value where true indicates that a value must be specified for this option setting of the option group option.
        
                    - **MinimumEngineVersionPerAllowedValue** *(list) --* 
        
                      The minimum DB engine version required for the corresponding allowed value for this option setting.
        
                      - *(dict) --* 
        
                        The minimum DB engine version required for each corresponding allowed value for an option setting.
        
                        - **AllowedValue** *(string) --* 
        
                          The allowed value for an option setting.
        
                        - **MinimumEngineVersion** *(string) --* 
        
                          The minimum DB engine version required for the allowed value.
        
                - **OptionGroupOptionVersions** *(list) --* 
        
                  The versions that are available for the option.
        
                  - *(dict) --* 
        
                    The version for an option. Option group option versions are returned by the  DescribeOptionGroupOptions action.
        
                    - **Version** *(string) --* 
        
                      The version of the option.
        
                    - **IsDefault** *(boolean) --* 
        
                      True if the version is the default version of the option, and otherwise false.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeOptionGroups(Paginator):
    def paginate(self, OptionGroupName: str = None, Filters: List = None, EngineName: str = None, MajorEngineVersion: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeOptionGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              OptionGroupName=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              EngineName=\'string\',
              MajorEngineVersion=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type OptionGroupName: string
        :param OptionGroupName: 
        
          The name of the option group to describe. Can\'t be supplied together with EngineName or MajorEngineVersion.
        
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type EngineName: string
        :param EngineName: 
        
          Filters the list of option groups to only include groups associated with a specific database engine.
        
        :type MajorEngineVersion: string
        :param MajorEngineVersion: 
        
          Filters the list of option groups to only include groups associated with a specific database engine version. If specified, then EngineName must also be specified.
        
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
                \'OptionGroupsList\': [
                    {
                        \'OptionGroupName\': \'string\',
                        \'OptionGroupDescription\': \'string\',
                        \'EngineName\': \'string\',
                        \'MajorEngineVersion\': \'string\',
                        \'Options\': [
                            {
                                \'OptionName\': \'string\',
                                \'OptionDescription\': \'string\',
                                \'Persistent\': True|False,
                                \'Permanent\': True|False,
                                \'Port\': 123,
                                \'OptionVersion\': \'string\',
                                \'OptionSettings\': [
                                    {
                                        \'Name\': \'string\',
                                        \'Value\': \'string\',
                                        \'DefaultValue\': \'string\',
                                        \'Description\': \'string\',
                                        \'ApplyType\': \'string\',
                                        \'DataType\': \'string\',
                                        \'AllowedValues\': \'string\',
                                        \'IsModifiable\': True|False,
                                        \'IsCollection\': True|False
                                    },
                                ],
                                \'DBSecurityGroupMemberships\': [
                                    {
                                        \'DBSecurityGroupName\': \'string\',
                                        \'Status\': \'string\'
                                    },
                                ],
                                \'VpcSecurityGroupMemberships\': [
                                    {
                                        \'VpcSecurityGroupId\': \'string\',
                                        \'Status\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'AllowsVpcAndNonVpcInstanceMemberships\': True|False,
                        \'VpcId\': \'string\',
                        \'OptionGroupArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            List of option groups.
        
            - **OptionGroupsList** *(list) --* 
        
              List of option groups.
        
              - *(dict) --* 
        
                - **OptionGroupName** *(string) --* 
        
                  Specifies the name of the option group.
        
                - **OptionGroupDescription** *(string) --* 
        
                  Provides a description of the option group.
        
                - **EngineName** *(string) --* 
        
                  Indicates the name of the engine that this option group can be applied to.
        
                - **MajorEngineVersion** *(string) --* 
        
                  Indicates the major engine version associated with this option group.
        
                - **Options** *(list) --* 
        
                  Indicates what options are available in the option group.
        
                  - *(dict) --* 
        
                    Option details.
        
                    - **OptionName** *(string) --* 
        
                      The name of the option.
        
                    - **OptionDescription** *(string) --* 
        
                      The description of the option.
        
                    - **Persistent** *(boolean) --* 
        
                      Indicate if this option is persistent.
        
                    - **Permanent** *(boolean) --* 
        
                      Indicate if this option is permanent.
        
                    - **Port** *(integer) --* 
        
                      If required, the port configured for this option to use.
        
                    - **OptionVersion** *(string) --* 
        
                      The version of the option.
        
                    - **OptionSettings** *(list) --* 
        
                      The option settings for this option.
        
                      - *(dict) --* 
        
                        Option settings are the actual settings being applied or configured for that option. It is used when you modify an option group or describe option groups. For example, the NATIVE_NETWORK_ENCRYPTION option has a setting called SQLNET.ENCRYPTION_SERVER that can have several different values.
        
                        - **Name** *(string) --* 
        
                          The name of the option that has settings that you can set.
        
                        - **Value** *(string) --* 
        
                          The current value of the option setting.
        
                        - **DefaultValue** *(string) --* 
        
                          The default value of the option setting.
        
                        - **Description** *(string) --* 
        
                          The description of the option setting.
        
                        - **ApplyType** *(string) --* 
        
                          The DB engine specific parameter type.
        
                        - **DataType** *(string) --* 
        
                          The data type of the option setting.
        
                        - **AllowedValues** *(string) --* 
        
                          The allowed values of the option setting.
        
                        - **IsModifiable** *(boolean) --* 
        
                          A Boolean value that, when true, indicates the option setting can be modified from the default.
        
                        - **IsCollection** *(boolean) --* 
        
                          Indicates if the option setting is part of a collection.
        
                    - **DBSecurityGroupMemberships** *(list) --* 
        
                      If the option requires access to a port, then this DB security group allows access to the port.
        
                      - *(dict) --* 
        
                        This data type is used as a response element in the following actions:
        
                        *  ModifyDBInstance   
                         
                        *  RebootDBInstance   
                         
                        *  RestoreDBInstanceFromDBSnapshot   
                         
                        *  RestoreDBInstanceToPointInTime   
                         
                        - **DBSecurityGroupName** *(string) --* 
        
                          The name of the DB security group.
        
                        - **Status** *(string) --* 
        
                          The status of the DB security group.
        
                    - **VpcSecurityGroupMemberships** *(list) --* 
        
                      If the option requires access to a port, then this VPC security group allows access to the port.
        
                      - *(dict) --* 
        
                        This data type is used as a response element for queries on VPC security group membership.
        
                        - **VpcSecurityGroupId** *(string) --* 
        
                          The name of the VPC security group.
        
                        - **Status** *(string) --* 
        
                          The status of the VPC security group.
        
                - **AllowsVpcAndNonVpcInstanceMemberships** *(boolean) --* 
        
                  Indicates whether this option group can be applied to both VPC and non-VPC instances. The value ``true`` indicates the option group can be applied to both VPC and non-VPC instances. 
        
                - **VpcId** *(string) --* 
        
                  If **AllowsVpcAndNonVpcInstanceMemberships** is ``false`` , this field is blank. If **AllowsVpcAndNonVpcInstanceMemberships** is ``true`` and this field is blank, then this option group can be applied to both VPC and non-VPC instances. If this field contains a value, then this option group can only be applied to instances that are in the VPC indicated by this field. 
        
                - **OptionGroupArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) for the option group.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeOrderableDBInstanceOptions(Paginator):
    def paginate(self, Engine: str, EngineVersion: str = None, DBInstanceClass: str = None, LicenseModel: str = None, Vpc: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeOrderableDBInstanceOptions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Engine=\'string\',
              EngineVersion=\'string\',
              DBInstanceClass=\'string\',
              LicenseModel=\'string\',
              Vpc=True|False,
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
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
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
                \'OrderableDBInstanceOptions\': [
                    {
                        \'Engine\': \'string\',
                        \'EngineVersion\': \'string\',
                        \'DBInstanceClass\': \'string\',
                        \'LicenseModel\': \'string\',
                        \'AvailabilityZones\': [
                            {
                                \'Name\': \'string\'
                            },
                        ],
                        \'MultiAZCapable\': True|False,
                        \'ReadReplicaCapable\': True|False,
                        \'Vpc\': True|False,
                        \'SupportsStorageEncryption\': True|False,
                        \'StorageType\': \'string\',
                        \'SupportsIops\': True|False,
                        \'SupportsEnhancedMonitoring\': True|False,
                        \'SupportsIAMDatabaseAuthentication\': True|False,
                        \'SupportsPerformanceInsights\': True|False,
                        \'MinStorageSize\': 123,
                        \'MaxStorageSize\': 123,
                        \'MinIopsPerDbInstance\': 123,
                        \'MaxIopsPerDbInstance\': 123,
                        \'MinIopsPerGib\': 123.0,
                        \'MaxIopsPerGib\': 123.0,
                        \'AvailableProcessorFeatures\': [
                            {
                                \'Name\': \'string\',
                                \'DefaultValue\': \'string\',
                                \'AllowedValues\': \'string\'
                            },
                        ],
                        \'SupportedEngineModes\': [
                            \'string\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeOrderableDBInstanceOptions action. 
        
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
        
                    Contains Availability Zone information.
        
                    This data type is used as an element in the following data type:
        
                    *  OrderableDBInstanceOption   
                     
                    - **Name** *(string) --* 
        
                      The name of the Availability Zone.
        
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
        
                - **AvailableProcessorFeatures** *(list) --* 
        
                  A list of the available processor features for the DB instance class of a DB instance.
        
                  - *(dict) --* 
        
                    Contains the available processor feature information for the DB instance class of a DB instance.
        
                    For more information, see `Configuring the Processor of the DB Instance Class <http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor>`__ in the *Amazon RDS User Guide.*  
        
                    - **Name** *(string) --* 
        
                      The name of the processor feature. Valid names are ``coreCount`` and ``threadsPerCore`` .
        
                    - **DefaultValue** *(string) --* 
        
                      The default value for the processor feature of the DB instance class.
        
                    - **AllowedValues** *(string) --* 
        
                      The allowed values for the processor feature of the DB instance class.
        
                - **SupportedEngineModes** *(list) --* 
        
                  A list of the supported DB engine modes.
        
                  - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeReservedDBInstances(Paginator):
    def paginate(self, ReservedDBInstanceId: str = None, ReservedDBInstancesOfferingId: str = None, DBInstanceClass: str = None, Duration: str = None, ProductDescription: str = None, OfferingType: str = None, MultiAZ: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeReservedDBInstances>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ReservedDBInstanceId=\'string\',
              ReservedDBInstancesOfferingId=\'string\',
              DBInstanceClass=\'string\',
              Duration=\'string\',
              ProductDescription=\'string\',
              OfferingType=\'string\',
              MultiAZ=True|False,
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
        :type ReservedDBInstanceId: string
        :param ReservedDBInstanceId: 
        
          The reserved DB instance identifier filter value. Specify this parameter to show only the reservation that matches the specified reservation ID.
        
        :type ReservedDBInstancesOfferingId: string
        :param ReservedDBInstancesOfferingId: 
        
          The offering identifier filter value. Specify this parameter to show only purchased reservations matching the specified offering identifier.
        
        :type DBInstanceClass: string
        :param DBInstanceClass: 
        
          The DB instance class filter value. Specify this parameter to show only those reservations matching the specified DB instances class.
        
        :type Duration: string
        :param Duration: 
        
          The duration filter value, specified in years or seconds. Specify this parameter to show only reservations for this duration.
        
          Valid Values: ``1 | 3 | 31536000 | 94608000``  
        
        :type ProductDescription: string
        :param ProductDescription: 
        
          The product description filter value. Specify this parameter to show only those reservations matching the specified product description.
        
        :type OfferingType: string
        :param OfferingType: 
        
          The offering type filter value. Specify this parameter to show only the available offerings matching the specified offering type.
        
          Valid Values: ``\"Partial Upfront\" | \"All Upfront\" | \"No Upfront\"``  
        
        :type MultiAZ: boolean
        :param MultiAZ: 
        
          The Multi-AZ filter value. Specify this parameter to show only those reservations matching the specified Multi-AZ parameter.
        
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
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
                \'ReservedDBInstances\': [
                    {
                        \'ReservedDBInstanceId\': \'string\',
                        \'ReservedDBInstancesOfferingId\': \'string\',
                        \'DBInstanceClass\': \'string\',
                        \'StartTime\': datetime(2015, 1, 1),
                        \'Duration\': 123,
                        \'FixedPrice\': 123.0,
                        \'UsagePrice\': 123.0,
                        \'CurrencyCode\': \'string\',
                        \'DBInstanceCount\': 123,
                        \'ProductDescription\': \'string\',
                        \'OfferingType\': \'string\',
                        \'MultiAZ\': True|False,
                        \'State\': \'string\',
                        \'RecurringCharges\': [
                            {
                                \'RecurringChargeAmount\': 123.0,
                                \'RecurringChargeFrequency\': \'string\'
                            },
                        ],
                        \'ReservedDBInstanceArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeReservedDBInstances action. 
        
            - **ReservedDBInstances** *(list) --* 
        
              A list of reserved DB instances.
        
              - *(dict) --* 
        
                This data type is used as a response element in the  DescribeReservedDBInstances and  PurchaseReservedDBInstancesOffering actions. 
        
                - **ReservedDBInstanceId** *(string) --* 
        
                  The unique identifier for the reservation.
        
                - **ReservedDBInstancesOfferingId** *(string) --* 
        
                  The offering identifier.
        
                - **DBInstanceClass** *(string) --* 
        
                  The DB instance class for the reserved DB instance.
        
                - **StartTime** *(datetime) --* 
        
                  The time the reservation started.
        
                - **Duration** *(integer) --* 
        
                  The duration of the reservation in seconds.
        
                - **FixedPrice** *(float) --* 
        
                  The fixed price charged for this reserved DB instance.
        
                - **UsagePrice** *(float) --* 
        
                  The hourly price charged for this reserved DB instance.
        
                - **CurrencyCode** *(string) --* 
        
                  The currency code for the reserved DB instance.
        
                - **DBInstanceCount** *(integer) --* 
        
                  The number of reserved DB instances.
        
                - **ProductDescription** *(string) --* 
        
                  The description of the reserved DB instance.
        
                - **OfferingType** *(string) --* 
        
                  The offering type of this reserved DB instance.
        
                - **MultiAZ** *(boolean) --* 
        
                  Indicates if the reservation applies to Multi-AZ deployments.
        
                - **State** *(string) --* 
        
                  The state of the reserved DB instance.
        
                - **RecurringCharges** *(list) --* 
        
                  The recurring price charged to run this reserved DB instance.
        
                  - *(dict) --* 
        
                    This data type is used as a response element in the  DescribeReservedDBInstances and  DescribeReservedDBInstancesOfferings actions. 
        
                    - **RecurringChargeAmount** *(float) --* 
        
                      The amount of the recurring charge.
        
                    - **RecurringChargeFrequency** *(string) --* 
        
                      The frequency of the recurring charge.
        
                - **ReservedDBInstanceArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) for the reserved DB instance.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeReservedDBInstancesOfferings(Paginator):
    def paginate(self, ReservedDBInstancesOfferingId: str = None, DBInstanceClass: str = None, Duration: str = None, ProductDescription: str = None, OfferingType: str = None, MultiAZ: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeReservedDBInstancesOfferings>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ReservedDBInstancesOfferingId=\'string\',
              DBInstanceClass=\'string\',
              Duration=\'string\',
              ProductDescription=\'string\',
              OfferingType=\'string\',
              MultiAZ=True|False,
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
        :type ReservedDBInstancesOfferingId: string
        :param ReservedDBInstancesOfferingId: 
        
          The offering identifier filter value. Specify this parameter to show only the available offering that matches the specified reservation identifier.
        
          Example: ``438012d3-4052-4cc7-b2e3-8d3372e0e706``  
        
        :type DBInstanceClass: string
        :param DBInstanceClass: 
        
          The DB instance class filter value. Specify this parameter to show only the available offerings matching the specified DB instance class.
        
        :type Duration: string
        :param Duration: 
        
          Duration filter value, specified in years or seconds. Specify this parameter to show only reservations for this duration.
        
          Valid Values: ``1 | 3 | 31536000 | 94608000``  
        
        :type ProductDescription: string
        :param ProductDescription: 
        
          Product description filter value. Specify this parameter to show only the available offerings that contain the specified product description.
        
          .. note::
        
            The results show offerings that partially match the filter value.
        
        :type OfferingType: string
        :param OfferingType: 
        
          The offering type filter value. Specify this parameter to show only the available offerings matching the specified offering type.
        
          Valid Values: ``\"Partial Upfront\" | \"All Upfront\" | \"No Upfront\"``  
        
        :type MultiAZ: boolean
        :param MultiAZ: 
        
          The Multi-AZ filter value. Specify this parameter to show only the available offerings matching the specified Multi-AZ parameter.
        
        :type Filters: list
        :param Filters: 
        
          This parameter is not currently supported.
        
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.
        
            .. note::
        
              Currently, wildcards are not supported in filters.
        
            The following actions can be filtered:
        
            *  DescribeDBClusterBacktracks   
             
            *  DescribeDBClusterEndpoints   
             
            *  DescribeDBClusters   
             
            *  DescribeDBInstances   
             
            *  DescribePendingMaintenanceActions   
             
            - **Name** *(string) --* **[REQUIRED]** 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
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
                \'ReservedDBInstancesOfferings\': [
                    {
                        \'ReservedDBInstancesOfferingId\': \'string\',
                        \'DBInstanceClass\': \'string\',
                        \'Duration\': 123,
                        \'FixedPrice\': 123.0,
                        \'UsagePrice\': 123.0,
                        \'CurrencyCode\': \'string\',
                        \'ProductDescription\': \'string\',
                        \'OfferingType\': \'string\',
                        \'MultiAZ\': True|False,
                        \'RecurringCharges\': [
                            {
                                \'RecurringChargeAmount\': 123.0,
                                \'RecurringChargeFrequency\': \'string\'
                            },
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeReservedDBInstancesOfferings action. 
        
            - **ReservedDBInstancesOfferings** *(list) --* 
        
              A list of reserved DB instance offerings.
        
              - *(dict) --* 
        
                This data type is used as a response element in the  DescribeReservedDBInstancesOfferings action. 
        
                - **ReservedDBInstancesOfferingId** *(string) --* 
        
                  The offering identifier.
        
                - **DBInstanceClass** *(string) --* 
        
                  The DB instance class for the reserved DB instance.
        
                - **Duration** *(integer) --* 
        
                  The duration of the offering in seconds.
        
                - **FixedPrice** *(float) --* 
        
                  The fixed price charged for this offering.
        
                - **UsagePrice** *(float) --* 
        
                  The hourly price charged for this offering.
        
                - **CurrencyCode** *(string) --* 
        
                  The currency code for the reserved DB instance offering.
        
                - **ProductDescription** *(string) --* 
        
                  The database engine used by the offering.
        
                - **OfferingType** *(string) --* 
        
                  The offering type.
        
                - **MultiAZ** *(boolean) --* 
        
                  Indicates if the offering applies to Multi-AZ deployments.
        
                - **RecurringCharges** *(list) --* 
        
                  The recurring price charged to run this reserved DB instance.
        
                  - *(dict) --* 
        
                    This data type is used as a response element in the  DescribeReservedDBInstances and  DescribeReservedDBInstancesOfferings actions. 
        
                    - **RecurringChargeAmount** *(float) --* 
        
                      The amount of the recurring charge.
        
                    - **RecurringChargeFrequency** *(string) --* 
        
                      The frequency of the recurring charge.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DownloadDBLogFilePortion(Paginator):
    def paginate(self, DBInstanceIdentifier: str, LogFileName: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DownloadDBLogFilePortion>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DBInstanceIdentifier=\'string\',
              LogFileName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: **[REQUIRED]** 
        
          The customer-assigned name of the DB instance that contains the log files you want to list.
        
          Constraints:
        
          * Must match the identifier of an existing DBInstance. 
           
        :type LogFileName: string
        :param LogFileName: **[REQUIRED]** 
        
          The name of the log file to be downloaded.
        
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
                \'LogFileData\': \'string\',
                \'AdditionalDataPending\': True|False,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            This data type is used as a response element to  DownloadDBLogFilePortion .
        
            - **LogFileData** *(string) --* 
        
              Entries from the specified log file.
        
            - **AdditionalDataPending** *(boolean) --* 
        
              Boolean value that if true, indicates there is more data to be downloaded.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
