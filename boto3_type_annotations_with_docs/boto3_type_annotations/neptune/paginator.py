from datetime import datetime
from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeDBEngineVersions(Paginator):
    def paginate(self, Engine: str = None, EngineVersion: str = None, DBParameterGroupFamily: str = None, Filters: List = None, DefaultOnly: bool = None, ListSupportedCharacterSets: bool = None, ListSupportedTimezones: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBEngineVersions>`_
        
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
                        \'SupportsReadReplica\': True|False
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
        
                    A time zone associated with a  DBInstance . This data type is an element in the response to the  DescribeDBInstances , and the  DescribeDBEngineVersions actions. 
        
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
        
        """
        pass


class DescribeDBInstances(Paginator):
    def paginate(self, DBInstanceIdentifier: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBInstances>`_
        
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
                            }
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
                        \'EnabledCloudwatchLogsExports\': [
                            \'string\',
                        ]
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
        
                    This data type is used as a response element in the following actions:
        
                    *  ModifyDBInstance   
                     
                    *  RebootDBInstance   
                     
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
        
                      This data type is used as a response element in the  DescribeDBSubnetGroups action. 
        
                      - **SubnetIdentifier** *(string) --* 
        
                        Specifies the identifier of the subnet.
        
                      - **SubnetAvailabilityZone** *(dict) --* 
        
                        Contains Availability Zone information.
        
                        This data type is used as an element in the following data type:
        
                        *  OrderableDBInstanceOption   
                         
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
        
                    A list of the log types whose configuration is still pending. In other words, these log types are in the process of being activated or deactivated.
        
                    - **LogTypesToEnable** *(list) --* 
        
                      Log types that are in the process of being deactivated. After they are deactivated, these log types aren\'t exported to CloudWatch Logs.
        
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
        
                      The status of the DB instance\'s option group membership. Valid values are: ``in-sync`` , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` , ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` . 
        
                - **CharacterSetName** *(string) --* 
        
                  If present, specifies the name of the character set that this instance is associated with.
        
                - **SecondaryAvailabilityZone** *(string) --* 
        
                  If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.
        
                - **PubliclyAccessible** *(boolean) --* 
        
                  This parameter is not supported.
        
                - **StatusInfos** *(list) --* 
        
                  The status of a Read Replica. If the instance is not a Read Replica, this is blank.
        
                  - *(dict) --* 
        
                    Provides a list of status information for a DB instance.
        
                    - **StatusType** *(string) --* 
        
                      This value is currently \"read replication.\"
        
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
        
                  Specifies whether the DB instance is encrypted.
        
                - **KmsKeyId** *(string) --* 
        
                  If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB instance. 
        
                - **DbiResourceId** *(string) --* 
        
                  The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.
        
                - **CACertificateIdentifier** *(string) --* 
        
                  The identifier of the CA certificate for this DB instance.
        
                - **DomainMemberships** *(list) --* 
        
                  Not supported
        
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
        
        """
        pass


class DescribeDBParameterGroups(Paginator):
    def paginate(self, DBParameterGroupName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBParameterGroups>`_
        
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
        
        """
        pass


class DescribeDBParameters(Paginator):
    def paginate(self, DBParameterGroupName: str, Source: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBParameters>`_
        
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
                        \'ApplyMethod\': \'immediate\'|\'pending-reboot\'
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
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeDBSubnetGroups(Paginator):
    def paginate(self, DBSubnetGroupName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBSubnetGroups>`_
        
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
        
                    This data type is used as a response element in the  DescribeDBSubnetGroups action. 
        
                    - **SubnetIdentifier** *(string) --* 
        
                      Specifies the identifier of the subnet.
        
                    - **SubnetAvailabilityZone** *(dict) --* 
        
                      Contains Availability Zone information.
        
                      This data type is used as an element in the following data type:
        
                      *  OrderableDBInstanceOption   
                       
                      - **Name** *(string) --* 
        
                        The name of the availability zone.
        
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
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeEngineDefaultParameters>`_
        
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
                            \'ApplyMethod\': \'immediate\'|\'pending-reboot\'
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
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeEventSubscriptions(Paginator):
    def paginate(self, SubscriptionName: str = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeEventSubscriptions>`_
        
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
        
                  The AWS customer account associated with the event notification subscription.
        
                - **CustSubscriptionId** *(string) --* 
        
                  The event notification subscription Id.
        
                - **SnsTopicArn** *(string) --* 
        
                  The topic ARN of the event notification subscription.
        
                - **Status** *(string) --* 
        
                  The status of the event notification subscription.
        
                  Constraints:
        
                  Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
        
                  The status \"no-permission\" indicates that Neptune no longer has permission to post to the SNS topic. The status \"topic-not-exist\" indicates that the topic was deleted after the subscription was created.
        
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
        
        """
        pass


class DescribeEvents(Paginator):
    def paginate(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, EventCategories: List = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeEvents>`_
        
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


class DescribeOrderableDBInstanceOptions(Paginator):
    def paginate(self, Engine: str, EngineVersion: str = None, DBInstanceClass: str = None, LicenseModel: str = None, Vpc: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeOrderableDBInstanceOptions>`_
        
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
                        \'MaxIopsPerGib\': 123.0
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
        
        """
        pass
