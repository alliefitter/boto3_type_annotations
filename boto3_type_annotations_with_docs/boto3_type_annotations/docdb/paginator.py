from typing import List
from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class DescribeDBClusters(Paginator):
    def paginate(self, DBClusterIdentifier: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DocDB.Client.describe_db_clusters`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBClusters>`_
        
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
                        'AvailabilityZones': [
                            'string',
                        ],
                        'BackupRetentionPeriod': 123,
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
                        'PreferredBackupWindow': 'string',
                        'PreferredMaintenanceWindow': 'string',
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
                        'ClusterCreateTime': datetime(2015, 1, 1),
                        'EnabledCloudwatchLogsExports': [
                            'string',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  DescribeDBClusters .
            - **DBClusters** *(list) --* 
              A list of DB clusters.
              - *(dict) --* 
                Detailed information about a DB cluster. 
                - **AvailabilityZones** *(list) --* 
                  Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be created in.
                  - *(string) --* 
                - **BackupRetentionPeriod** *(integer) --* 
                  Specifies the number of days for which automatic DB snapshots are retained.
                - **DBClusterIdentifier** *(string) --* 
                  Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.
                - **DBClusterParameterGroup** *(string) --* 
                  Specifies the name of the DB cluster parameter group for the DB cluster.
                - **DBSubnetGroup** *(string) --* 
                  Specifies information on the subnet group that is associated with the DB cluster, including the name, description, and subnets in the subnet group.
                - **Status** *(string) --* 
                  Specifies the current state of this DB cluster.
                - **PercentProgress** *(string) --* 
                  Specifies the progress of the operation as a percentage.
                - **EarliestRestorableTime** *(datetime) --* 
                  The earliest time to which a database can be restored with point-in-time restore.
                - **Endpoint** *(string) --* 
                  Specifies the connection endpoint for the primary instance of the DB cluster.
                - **ReaderEndpoint** *(string) --* 
                  The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances connections across the Amazon DocumentDB replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB distributes the connection requests among the Amazon DocumentDB replicas in the DB cluster. This functionality can help balance your read workload across multiple Amazon DocumentDB replicas in your DB cluster. 
                  If a failover occurs, and the Amazon DocumentDB replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to the reader endpoint.
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
                  Contains the master user name for the DB cluster.
                - **PreferredBackupWindow** *(string) --* 
                  Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the ``BackupRetentionPeriod`` . 
                - **PreferredMaintenanceWindow** *(string) --* 
                  Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
                - **DBClusterMembers** *(list) --* 
                  Provides the list of instances that make up the DB cluster.
                  - *(dict) --* 
                    Contains information about an instance that is part of a DB cluster.
                    - **DBInstanceIdentifier** *(string) --* 
                      Specifies the instance identifier for this member of the DB cluster.
                    - **IsClusterWriter** *(boolean) --* 
                      A value that is ``true`` if the cluster member is the primary instance for the DB cluster and ``false`` otherwise.
                    - **DBClusterParameterGroupStatus** *(string) --* 
                      Specifies the status of the DB cluster parameter group for this member of the DB cluster.
                    - **PromotionTier** *(integer) --* 
                      A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance. 
                - **VpcSecurityGroups** *(list) --* 
                  Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs to.
                  - *(dict) --* 
                    Used as a response element for queries on virtual private cloud (VPC) security group membership.
                    - **VpcSecurityGroupId** *(string) --* 
                      The name of the VPC security group.
                    - **Status** *(string) --* 
                      The status of the VPC security group.
                - **HostedZoneId** *(string) --* 
                  Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
                - **StorageEncrypted** *(boolean) --* 
                  Specifies whether the DB cluster is encrypted.
                - **KmsKeyId** *(string) --* 
                  If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB cluster.
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
                      Describes the state of association between the IAM role and the DB cluster. The ``Status`` property returns one of the following values:
                      * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf. 
                      * ``PENDING`` - The IAM role ARN is being associated with the DB cluster. 
                      * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster cannot assume the IAM role to access other AWS services on your behalf. 
                - **ClusterCreateTime** *(datetime) --* 
                  Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).
                - **EnabledCloudwatchLogsExports** *(list) --* 
                  A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.
                  - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier:
          The user-provided DB cluster identifier. If this parameter is specified, information from only the specific DB cluster is returned. This parameter isn\'t case sensitive.
          Constraints:
          * If provided, must match an existing ``DBClusterIdentifier`` .
        :type Filters: list
        :param Filters:
          A filter that specifies one or more DB clusters to describe.
          Supported filters:
          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list only includes information about the DB clusters identified by these ARNs.
          - *(dict) --*
            A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.
            Wildcards are not supported in filters.
            - **Name** *(string) --* **[REQUIRED]**
              The name of the filter. Filter names are case sensitive.
            - **Values** *(list) --* **[REQUIRED]**
              One or more filter values. Filter values are case sensitive.
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
        Creates an iterator that will paginate through responses from :py:meth:`DocDB.Client.describe_db_engine_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBEngineVersions>`_
        
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
                        'ValidUpgradeTarget': [
                            {
                                'Engine': 'string',
                                'EngineVersion': 'string',
                                'Description': 'string',
                                'AutoUpgrade': True|False,
                                'IsMajorVersionUpgrade': True|False
                            },
                        ],
                        'ExportableLogTypes': [
                            'string',
                        ],
                        'SupportsLogExportsToCloudwatchLogs': True|False
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  DescribeDBEngineVersions .
            - **DBEngineVersions** *(list) --* 
              Detailed information about one or more DB engine versions.
              - *(dict) --* 
                Detailed information about a DB engine version. 
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
                      A value that indicates whether the target version is applied to any source DB instances that have ``AutoMinorVersionUpgrade`` set to ``true`` .
                    - **IsMajorVersionUpgrade** *(boolean) --* 
                      A value that indicates whether a database engine is upgraded to a major version.
                - **ExportableLogTypes** *(list) --* 
                  The types of logs that the database engine has available for export to Amazon CloudWatch Logs.
                  - *(string) --* 
                - **SupportsLogExportsToCloudwatchLogs** *(boolean) --* 
                  A value that indicates whether the engine version supports exporting the log types specified by ``ExportableLogTypes`` to CloudWatch Logs.
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
          * If provided, must match an existing ``DBParameterGroupFamily`` .
        :type Filters: list
        :param Filters:
          This parameter is not currently supported.
          - *(dict) --*
            A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.
            Wildcards are not supported in filters.
            - **Name** *(string) --* **[REQUIRED]**
              The name of the filter. Filter names are case sensitive.
            - **Values** *(list) --* **[REQUIRED]**
              One or more filter values. Filter values are case sensitive.
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
        Creates an iterator that will paginate through responses from :py:meth:`DocDB.Client.describe_db_instances`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBInstances>`_
        
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
                        'Endpoint': {
                            'Address': 'string',
                            'Port': 123,
                            'HostedZoneId': 'string'
                        },
                        'InstanceCreateTime': datetime(2015, 1, 1),
                        'PreferredBackupWindow': 'string',
                        'BackupRetentionPeriod': 123,
                        'VpcSecurityGroups': [
                            {
                                'VpcSecurityGroupId': 'string',
                                'Status': 'string'
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
                        'EngineVersion': 'string',
                        'AutoMinorVersionUpgrade': True|False,
                        'PubliclyAccessible': True|False,
                        'StatusInfos': [
                            {
                                'StatusType': 'string',
                                'Normal': True|False,
                                'Status': 'string',
                                'Message': 'string'
                            },
                        ],
                        'DBClusterIdentifier': 'string',
                        'StorageEncrypted': True|False,
                        'KmsKeyId': 'string',
                        'DbiResourceId': 'string',
                        'PromotionTier': 123,
                        'DBInstanceArn': 'string',
                        'EnabledCloudwatchLogsExports': [
                            'string',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  DescribeDBInstances .
            - **DBInstances** *(list) --* 
              Detailed information about one or more DB instances. 
              - *(dict) --* 
                Detailed information about a DB instance. 
                - **DBInstanceIdentifier** *(string) --* 
                  Contains a user-provided database identifier. This identifier is the unique key that identifies a DB instance.
                - **DBInstanceClass** *(string) --* 
                  Contains the name of the compute and memory capacity class of the DB instance.
                - **Engine** *(string) --* 
                  Provides the name of the database engine to be used for this DB instance.
                - **DBInstanceStatus** *(string) --* 
                  Specifies the current state of this database.
                - **Endpoint** *(dict) --* 
                  Specifies the connection endpoint.
                  - **Address** *(string) --* 
                    Specifies the DNS address of the DB instance.
                  - **Port** *(integer) --* 
                    Specifies the port that the database engine is listening on.
                  - **HostedZoneId** *(string) --* 
                    Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
                - **InstanceCreateTime** *(datetime) --* 
                  Provides the date and time that the DB instance was created.
                - **PreferredBackupWindow** *(string) --* 
                  Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the ``BackupRetentionPeriod`` . 
                - **BackupRetentionPeriod** *(integer) --* 
                  Specifies the number of days for which automatic DB snapshots are retained.
                - **VpcSecurityGroups** *(list) --* 
                  Provides a list of VPC security group elements that the DB instance belongs to.
                  - *(dict) --* 
                    Used as a response element for queries on virtual private cloud (VPC) security group membership.
                    - **VpcSecurityGroupId** *(string) --* 
                      The name of the VPC security group.
                    - **Status** *(string) --* 
                      The status of the VPC security group.
                - **AvailabilityZone** *(string) --* 
                  Specifies the name of the Availability Zone that the DB instance is located in.
                - **DBSubnetGroup** *(dict) --* 
                  Specifies information on the subnet group that is associated with the DB instance, including the name, description, and subnets in the subnet group.
                  - **DBSubnetGroupName** *(string) --* 
                    The name of the DB subnet group.
                  - **DBSubnetGroupDescription** *(string) --* 
                    Provides the description of the DB subnet group.
                  - **VpcId** *(string) --* 
                    Provides the virtual private cloud (VPC) ID of the DB subnet group.
                  - **SubnetGroupStatus** *(string) --* 
                    Provides the status of the DB subnet group.
                  - **Subnets** *(list) --* 
                    Detailed information about one or more subnets within a DB subnet group.
                    - *(dict) --* 
                      Detailed information about a subnet. 
                      - **SubnetIdentifier** *(string) --* 
                        Specifies the identifier of the subnet.
                      - **SubnetAvailabilityZone** *(dict) --* 
                        Specifies the Availability Zone for the subnet.
                        - **Name** *(string) --* 
                          The name of the Availability Zone.
                      - **SubnetStatus** *(string) --* 
                        Specifies the status of the subnet.
                  - **DBSubnetGroupArn** *(string) --* 
                    The Amazon Resource Identifier (ARN) for the DB subnet group.
                - **PreferredMaintenanceWindow** *(string) --* 
                  Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
                - **PendingModifiedValues** *(dict) --* 
                  Specifies that changes to the DB instance are pending. This element is included only when changes are pending. Specific changes are identified by subelements.
                  - **DBInstanceClass** *(string) --* 
                    Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is currently being applied. 
                  - **AllocatedStorage** *(integer) --* 
                    Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is currently being applied. 
                  - **MasterUserPassword** *(string) --* 
                    Contains the pending or currently in-progress change of the master credentials for the DB instance.
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
                    Valid values: ``license-included`` , ``bring-your-own-license`` , ``general-public-license``  
                  - **Iops** *(integer) --* 
                    Specifies the new Provisioned IOPS value for the DB instance that will be applied or is currently being applied.
                  - **DBInstanceIdentifier** *(string) --* 
                    Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is currently being applied. 
                  - **StorageType** *(string) --* 
                    Specifies the storage type to be associated with the DB instance.
                  - **CACertificateIdentifier** *(string) --* 
                    Specifies the identifier of the certificate authority (CA) certificate for the DB instance.
                  - **DBSubnetGroupName** *(string) --* 
                    The new DB subnet group for the DB instance. 
                  - **PendingCloudwatchLogsExports** *(dict) --* 
                    A list of the log types whose configuration is still pending. These log types are in the process of being activated or deactivated.
                    - **LogTypesToEnable** *(list) --* 
                      Log types that are in the process of being deactivated. After they are deactivated, these log types aren't exported to CloudWatch Logs.
                      - *(string) --* 
                    - **LogTypesToDisable** *(list) --* 
                      Log types that are in the process of being enabled. After they are enabled, these log types are exported to Amazon CloudWatch Logs.
                      - *(string) --* 
                - **LatestRestorableTime** *(datetime) --* 
                  Specifies the latest time to which a database can be restored with point-in-time restore.
                - **EngineVersion** *(string) --* 
                  Indicates the database engine version.
                - **AutoMinorVersionUpgrade** *(boolean) --* 
                  Indicates that minor version patches are applied automatically.
                - **PubliclyAccessible** *(boolean) --* 
                  Specifies the availability options for the DB instance. A value of ``true`` specifies an internet-facing instance with a publicly resolvable DNS name, which resolves to a public IP address. A value of ``false`` specifies an internal instance with a DNS name that resolves to a private IP address.
                - **StatusInfos** *(list) --* 
                  The status of a read replica. If the instance is not a read replica, this is blank.
                  - *(dict) --* 
                    Provides a list of status information for a DB instance.
                    - **StatusType** *(string) --* 
                      This value is currently "``read replication`` ."
                    - **Normal** *(boolean) --* 
                      A Boolean value that is ``true`` if the instance is operating normally, or ``false`` if the instance is in an error state.
                    - **Status** *(string) --* 
                      Status of the DB instance. For a ``StatusType`` of read replica, the values can be ``replicating`` , error, ``stopped`` , or ``terminated`` .
                    - **Message** *(string) --* 
                      Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.
                - **DBClusterIdentifier** *(string) --* 
                  Contains the name of the DB cluster that the DB instance is a member of if the DB instance is a member of a DB cluster.
                - **StorageEncrypted** *(boolean) --* 
                  Specifies whether the DB instance is encrypted.
                - **KmsKeyId** *(string) --* 
                  If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB instance. 
                - **DbiResourceId** *(string) --* 
                  The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.
                - **PromotionTier** *(integer) --* 
                  A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.
                - **DBInstanceArn** *(string) --* 
                  The Amazon Resource Name (ARN) for the DB instance.
                - **EnabledCloudwatchLogsExports** *(list) --* 
                  A list of log types that this DB instance is configured to export to Amazon CloudWatch Logs.
                  - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier:
          The user-provided instance identifier. If this parameter is specified, information from only the specific DB instance is returned. This parameter isn\'t case sensitive.
          Constraints:
          * If provided, must match the identifier of an existing ``DBInstance`` .
        :type Filters: list
        :param Filters:
          A filter that specifies one or more DB instances to describe.
          Supported filters:
          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list includes only the information about the DB instances that are associated with the DB clusters that are identified by these ARNs.
          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance ARNs. The results list includes only the information about the DB instances that are identified by these ARNs.
          - *(dict) --*
            A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.
            Wildcards are not supported in filters.
            - **Name** *(string) --* **[REQUIRED]**
              The name of the filter. Filter names are case sensitive.
            - **Values** *(list) --* **[REQUIRED]**
              One or more filter values. Filter values are case sensitive.
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
        Creates an iterator that will paginate through responses from :py:meth:`DocDB.Client.describe_db_subnet_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBSubnetGroups>`_
        
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
            Represents the output of  DescribeDBSubnetGroups .
            - **DBSubnetGroups** *(list) --* 
              Detailed information about one or more DB subnet groups.
              - *(dict) --* 
                Detailed information about a DB subnet group. 
                - **DBSubnetGroupName** *(string) --* 
                  The name of the DB subnet group.
                - **DBSubnetGroupDescription** *(string) --* 
                  Provides the description of the DB subnet group.
                - **VpcId** *(string) --* 
                  Provides the virtual private cloud (VPC) ID of the DB subnet group.
                - **SubnetGroupStatus** *(string) --* 
                  Provides the status of the DB subnet group.
                - **Subnets** *(list) --* 
                  Detailed information about one or more subnets within a DB subnet group.
                  - *(dict) --* 
                    Detailed information about a subnet. 
                    - **SubnetIdentifier** *(string) --* 
                      Specifies the identifier of the subnet.
                    - **SubnetAvailabilityZone** *(dict) --* 
                      Specifies the Availability Zone for the subnet.
                      - **Name** *(string) --* 
                        The name of the Availability Zone.
                    - **SubnetStatus** *(string) --* 
                      Specifies the status of the subnet.
                - **DBSubnetGroupArn** *(string) --* 
                  The Amazon Resource Identifier (ARN) for the DB subnet group.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName:
          The name of the DB subnet group to return details for.
        :type Filters: list
        :param Filters:
          This parameter is not currently supported.
          - *(dict) --*
            A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.
            Wildcards are not supported in filters.
            - **Name** *(string) --* **[REQUIRED]**
              The name of the filter. Filter names are case sensitive.
            - **Values** *(list) --* **[REQUIRED]**
              One or more filter values. Filter values are case sensitive.
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
        Creates an iterator that will paginate through responses from :py:meth:`DocDB.Client.describe_events`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeEvents>`_
        
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
            Represents the output of  DescribeEvents .
            - **Events** *(list) --* 
              Detailed information about one or more events. 
              - *(dict) --* 
                Detailed information about an event.
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
          * If ``SourceIdentifier`` is provided, ``SourceType`` must also be provided.
          * If the source type is ``DBInstance`` , a ``DBInstanceIdentifier`` must be provided.
          * If the source type is ``DBSecurityGroup`` , a ``DBSecurityGroupName`` must be provided.
          * If the source type is ``DBParameterGroup`` , a ``DBParameterGroupName`` must be provided.
          * If the source type is ``DBSnapshot`` , a ``DBSnapshotIdentifier`` must be provided.
          * Cannot end with a hyphen or contain two consecutive hyphens.
        :type SourceType: string
        :param SourceType:
          The event source to retrieve events for. If no value is specified, all events are returned.
        :type StartTime: datetime
        :param StartTime:
          The beginning of the time interval to retrieve events for, specified in ISO 8601 format.
          Example: 2009-07-08T18:00Z
        :type EndTime: datetime
        :param EndTime:
          The end of the time interval for which to retrieve events, specified in ISO 8601 format.
          Example: 2009-07-08T18:00Z
        :type Duration: integer
        :param Duration:
          The number of minutes to retrieve events for.
          Default: 60
        :type EventCategories: list
        :param EventCategories:
          A list of event categories that trigger notifications for an event notification subscription.
          - *(string) --*
        :type Filters: list
        :param Filters:
          This parameter is not currently supported.
          - *(dict) --*
            A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.
            Wildcards are not supported in filters.
            - **Name** *(string) --* **[REQUIRED]**
              The name of the filter. Filter names are case sensitive.
            - **Values** *(list) --* **[REQUIRED]**
              One or more filter values. Filter values are case sensitive.
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
        Creates an iterator that will paginate through responses from :py:meth:`DocDB.Client.describe_orderable_db_instance_options`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeOrderableDBInstanceOptions>`_
        
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
                        'Vpc': True|False
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  DescribeOrderableDBInstanceOptions .
            - **OrderableDBInstanceOptions** *(list) --* 
              The options that are available for a particular orderable DB instance.
              - *(dict) --* 
                The options that are available for a DB instance.
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
                    Information about an Availability Zone.
                    - **Name** *(string) --* 
                      The name of the Availability Zone.
                - **Vpc** *(boolean) --* 
                  Indicates whether a DB instance is in a virtual private cloud (VPC).
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type Engine: string
        :param Engine: **[REQUIRED]**
          The name of the engine to retrieve DB instance options for.
        :type EngineVersion: string
        :param EngineVersion:
          The engine version filter value. Specify this parameter to show only the available offerings that match the specified engine version.
        :type DBInstanceClass: string
        :param DBInstanceClass:
          The DB instance class filter value. Specify this parameter to show only the available offerings that match the specified DB instance class.
        :type LicenseModel: string
        :param LicenseModel:
          The license model filter value. Specify this parameter to show only the available offerings that match the specified license model.
        :type Vpc: boolean
        :param Vpc:
          The virtual private cloud (VPC) filter value. Specify this parameter to show only the available VPC or non-VPC offerings.
        :type Filters: list
        :param Filters:
          This parameter is not currently supported.
          - *(dict) --*
            A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.
            Wildcards are not supported in filters.
            - **Name** *(string) --* **[REQUIRED]**
              The name of the filter. Filter names are case sensitive.
            - **Values** *(list) --* **[REQUIRED]**
              One or more filter values. Filter values are case sensitive.
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
