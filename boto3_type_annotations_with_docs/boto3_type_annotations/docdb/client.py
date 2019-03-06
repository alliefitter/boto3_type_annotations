from typing import Union
from typing import List
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Optional
from typing import Dict
from datetime import datetime
from botocore.client import BaseClient


class Client(BaseClient):
    def add_tags_to_resource(self, ResourceName: str, Tags: List):
        """
        Adds metadata tags to an Amazon DocumentDB resource. You can use these tags with cost allocation reporting to track costs that are associated with Amazon DocumentDB resources. or in a ``Condition`` statement in an AWS Identity and Access Management (IAM) policy for Amazon DocumentDB.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/AddTagsToResource>`_
        
        **Request Syntax**
        ::
          response = client.add_tags_to_resource(
              ResourceName='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ResourceName: string
        :param ResourceName: **[REQUIRED]**
          The Amazon DocumentDB resource that the tags are added to. This value is an Amazon Resource Name (ARN).
        :type Tags: list
        :param Tags: **[REQUIRED]**
          The tags to be assigned to the Amazon DocumentDB resource.
          - *(dict) --*
            Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
            - **Key** *(string) --*
              The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
            - **Value** *(string) --*
              The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        :returns: None
        """
        pass

    def apply_pending_maintenance_action(self, ResourceIdentifier: str, ApplyAction: str, OptInType: str) -> Dict:
        """
        Applies a pending maintenance action to a resource (for example, to a DB instance).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/ApplyPendingMaintenanceAction>`_
        
        **Request Syntax**
        ::
          response = client.apply_pending_maintenance_action(
              ResourceIdentifier='string',
              ApplyAction='string',
              OptInType='string'
          )
        
        **Response Syntax**
        ::
            {
                'ResourcePendingMaintenanceActions': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ResourcePendingMaintenanceActions** *(dict) --* 
              Represents the output of  ApplyPendingMaintenanceAction .
              - **ResourceIdentifier** *(string) --* 
                The Amazon Resource Name (ARN) of the resource that has pending maintenance actions.
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
                    The effective date when the pending maintenance action is applied to the resource.
                  - **Description** *(string) --* 
                    A description providing more detail about the maintenance action.
        :type ResourceIdentifier: string
        :param ResourceIdentifier: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to.
        :type ApplyAction: string
        :param ApplyAction: **[REQUIRED]**
          The pending maintenance action to apply to this resource.
          Valid values: ``system-update`` , ``db-upgrade``
        :type OptInType: string
        :param OptInType: **[REQUIRED]**
          A value that specifies the type of opt-in request or undoes an opt-in request. An opt-in request of type ``immediate`` can\'t be undone.
          Valid values:
          * ``immediate`` - Apply the maintenance action immediately.
          * ``next-maintenance`` - Apply the maintenance action during the next maintenance window for the resource.
          * ``undo-opt-in`` - Cancel any existing ``next-maintenance`` opt-in requests.
        :rtype: dict
        :returns:
        """
        pass

    def can_paginate(self, operation_name: str = None):
        """
        Check if an operation can be paginated.
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

    def copy_db_cluster_parameter_group(self, SourceDBClusterParameterGroupIdentifier: str, TargetDBClusterParameterGroupIdentifier: str, TargetDBClusterParameterGroupDescription: str, Tags: List = None) -> Dict:
        """
        Copies the specified DB cluster parameter group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/CopyDBClusterParameterGroup>`_
        
        **Request Syntax**
        ::
          response = client.copy_db_cluster_parameter_group(
              SourceDBClusterParameterGroupIdentifier='string',
              TargetDBClusterParameterGroupIdentifier='string',
              TargetDBClusterParameterGroupDescription='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'DBClusterParameterGroup': {
                    'DBClusterParameterGroupName': 'string',
                    'DBParameterGroupFamily': 'string',
                    'Description': 'string',
                    'DBClusterParameterGroupArn': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBClusterParameterGroup** *(dict) --* 
              Detailed information about a DB cluster parameter group. 
              - **DBClusterParameterGroupName** *(string) --* 
                Provides the name of the DB cluster parameter group.
              - **DBParameterGroupFamily** *(string) --* 
                Provides the name of the DB parameter group family that this DB cluster parameter group is compatible with.
              - **Description** *(string) --* 
                Provides the customer-specified description for this DB cluster parameter group.
              - **DBClusterParameterGroupArn** *(string) --* 
                The Amazon Resource Name (ARN) for the DB cluster parameter group.
        :type SourceDBClusterParameterGroupIdentifier: string
        :param SourceDBClusterParameterGroupIdentifier: **[REQUIRED]**
          The identifier or Amazon Resource Name (ARN) for the source DB cluster parameter group.
          Constraints:
          * Must specify a valid DB cluster parameter group.
          * If the source DB cluster parameter group is in the same AWS Region as the copy, specify a valid DB parameter group identifier; for example, ``my-db-cluster-param-group`` , or a valid ARN.
          * If the source DB parameter group is in a different AWS Region than the copy, specify a valid DB cluster parameter group ARN; for example, ``arn:aws:rds:us-east-1:123456789012:cluster-pg:custom-cluster-group1`` .
        :type TargetDBClusterParameterGroupIdentifier: string
        :param TargetDBClusterParameterGroupIdentifier: **[REQUIRED]**
          The identifier for the copied DB cluster parameter group.
          Constraints:
          * Cannot be null, empty, or blank.
          * Must contain from 1 to 255 letters, numbers, or hyphens.
          * The first character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
          Example: ``my-cluster-param-group1``
        :type TargetDBClusterParameterGroupDescription: string
        :param TargetDBClusterParameterGroupDescription: **[REQUIRED]**
          A description for the copied DB cluster parameter group.
        :type Tags: list
        :param Tags:
          The tags that are to be assigned to the parameter group.
          - *(dict) --*
            Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
            - **Key** *(string) --*
              The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
            - **Value** *(string) --*
              The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        :rtype: dict
        :returns:
        """
        pass

    def copy_db_cluster_snapshot(self, SourceDBClusterSnapshotIdentifier: str, TargetDBClusterSnapshotIdentifier: str, KmsKeyId: str = None, PreSignedUrl: str = None, CopyTags: bool = None, Tags: List = None) -> Dict:
        """
        Copies a snapshot of a DB cluster.
        To copy a DB cluster snapshot from a shared manual DB cluster snapshot, ``SourceDBClusterSnapshotIdentifier`` must be the Amazon Resource Name (ARN) of the shared DB cluster snapshot.
        To cancel the copy operation after it is in progress, delete the target DB cluster snapshot identified by ``TargetDBClusterSnapshotIdentifier`` while that DB cluster snapshot is in the *copying* status.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/CopyDBClusterSnapshot>`_
        
        **Request Syntax**
        ::
          response = client.copy_db_cluster_snapshot(
              SourceDBClusterSnapshotIdentifier='string',
              TargetDBClusterSnapshotIdentifier='string',
              KmsKeyId='string',
              PreSignedUrl='string',
              CopyTags=True|False,
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'DBClusterSnapshot': {
                    'AvailabilityZones': [
                        'string',
                    ],
                    'DBClusterSnapshotIdentifier': 'string',
                    'DBClusterIdentifier': 'string',
                    'SnapshotCreateTime': datetime(2015, 1, 1),
                    'Engine': 'string',
                    'Status': 'string',
                    'Port': 123,
                    'VpcId': 'string',
                    'ClusterCreateTime': datetime(2015, 1, 1),
                    'MasterUsername': 'string',
                    'EngineVersion': 'string',
                    'SnapshotType': 'string',
                    'PercentProgress': 123,
                    'StorageEncrypted': True|False,
                    'KmsKeyId': 'string',
                    'DBClusterSnapshotArn': 'string',
                    'SourceDBClusterSnapshotArn': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBClusterSnapshot** *(dict) --* 
              Detailed information about a DB cluster snapshot. 
              - **AvailabilityZones** *(list) --* 
                Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.
                - *(string) --* 
              - **DBClusterSnapshotIdentifier** *(string) --* 
                Specifies the identifier for the DB cluster snapshot.
              - **DBClusterIdentifier** *(string) --* 
                Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.
              - **SnapshotCreateTime** *(datetime) --* 
                Provides the time when the snapshot was taken, in UTC.
              - **Engine** *(string) --* 
                Specifies the name of the database engine.
              - **Status** *(string) --* 
                Specifies the status of this DB cluster snapshot.
              - **Port** *(integer) --* 
                Specifies the port that the DB cluster was listening on at the time of the snapshot.
              - **VpcId** *(string) --* 
                Provides the virtual private cloud (VPC) ID that is associated with the DB cluster snapshot.
              - **ClusterCreateTime** *(datetime) --* 
                Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).
              - **MasterUsername** *(string) --* 
                Provides the master user name for the DB cluster snapshot.
              - **EngineVersion** *(string) --* 
                Provides the version of the database engine for this DB cluster snapshot.
              - **SnapshotType** *(string) --* 
                Provides the type of the DB cluster snapshot.
              - **PercentProgress** *(integer) --* 
                Specifies the percentage of the estimated data that has been transferred.
              - **StorageEncrypted** *(boolean) --* 
                Specifies whether the DB cluster snapshot is encrypted.
              - **KmsKeyId** *(string) --* 
                If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB cluster snapshot.
              - **DBClusterSnapshotArn** *(string) --* 
                The Amazon Resource Name (ARN) for the DB cluster snapshot.
              - **SourceDBClusterSnapshotArn** *(string) --* 
                If the DB cluster snapshot was copied from a source DB cluster snapshot, the ARN for the source DB cluster snapshot; otherwise, a null value.
        :type SourceDBClusterSnapshotIdentifier: string
        :param SourceDBClusterSnapshotIdentifier: **[REQUIRED]**
          The identifier of the DB cluster snapshot to copy. This parameter is not case sensitive.
          You can\'t copy an encrypted, shared DB cluster snapshot from one AWS Region to another.
          Constraints:
          * Must specify a valid system snapshot in the \"available\" state.
          * If the source snapshot is in the same AWS Region as the copy, specify a valid DB snapshot identifier.
          * If the source snapshot is in a different AWS Region than the copy, specify a valid DB cluster snapshot ARN.
          Example: ``my-cluster-snapshot1``
        :type TargetDBClusterSnapshotIdentifier: string
        :param TargetDBClusterSnapshotIdentifier: **[REQUIRED]**
          The identifier of the new DB cluster snapshot to create from the source DB cluster snapshot. This parameter is not case sensitive.
          Constraints:
          * Must contain from 1 to 63 letters, numbers, or hyphens.
          * The first character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
          Example: ``my-cluster-snapshot2``
        :type KmsKeyId: string
        :param KmsKeyId:
          The AWS KMS key ID for an encrypted DB cluster snapshot. The AWS KMS key ID is the Amazon Resource Name (ARN), AWS KMS key identifier, or the AWS KMS key alias for the AWS KMS encryption key.
          If you copy an encrypted DB cluster snapshot from your AWS account, you can specify a value for ``KmsKeyId`` to encrypt the copy with a new AWS KMS encryption key. If you don\'t specify a value for ``KmsKeyId`` , then the copy of the DB cluster snapshot is encrypted with the same AWS KMS key as the source DB cluster snapshot.
          If you copy an encrypted DB cluster snapshot that is shared from another AWS account, then you must specify a value for ``KmsKeyId`` .
          To copy an encrypted DB cluster snapshot to another AWS Region, set ``KmsKeyId`` to the AWS KMS key ID that you want to use to encrypt the copy of the DB cluster snapshot in the destination Region. AWS KMS encryption keys are specific to the AWS Region that they are created in, and you can\'t use encryption keys from one Region in another Region.
          If you copy an unencrypted DB cluster snapshot and specify a value for the ``KmsKeyId`` parameter, an error is returned.
        :type PreSignedUrl: string
        :param PreSignedUrl:
          The URL that contains a Signature Version 4 signed request for the ``CopyDBClusterSnapshot`` API action in the AWS Region that contains the source DB cluster snapshot to copy. You must use the ``PreSignedUrl`` parameter when copying an encrypted DB cluster snapshot from another AWS Region.
          The presigned URL must be a valid request for the ``CopyDBSClusterSnapshot`` API action that can be executed in the source AWS Region that contains the encrypted DB cluster snapshot to be copied. The presigned URL request must contain the following parameter values:
          * ``KmsKeyId`` - The AWS KMS key identifier for the key to use to encrypt the copy of the DB cluster snapshot in the destination AWS Region. This is the same identifier for both the ``CopyDBClusterSnapshot`` action that is called in the destination AWS Region, and the action contained in the presigned URL.
          * ``DestinationRegion`` - The name of the AWS Region that the DB cluster snapshot will be created in.
          * ``SourceDBClusterSnapshotIdentifier`` - The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB cluster snapshot from the us-west-2 AWS Region, then your ``SourceDBClusterSnapshotIdentifier`` looks like the following example: ``arn:aws:rds:us-west-2:123456789012:cluster-snapshot:my-cluster-snapshot-20161115`` .
        :type CopyTags: boolean
        :param CopyTags:
          Set to ``true`` to copy all tags from the source DB cluster snapshot to the target DB cluster snapshot, and otherwise ``false`` . The default is ``false`` .
        :type Tags: list
        :param Tags:
          The tags to be assigned to the DB cluster snapshot.
          - *(dict) --*
            Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
            - **Key** *(string) --*
              The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
            - **Value** *(string) --*
              The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        :rtype: dict
        :returns:
        """
        pass

    def create_db_cluster(self, DBClusterIdentifier: str, Engine: str, AvailabilityZones: List = None, BackupRetentionPeriod: int = None, DBClusterParameterGroupName: str = None, VpcSecurityGroupIds: List = None, DBSubnetGroupName: str = None, EngineVersion: str = None, Port: int = None, MasterUsername: str = None, MasterUserPassword: str = None, PreferredBackupWindow: str = None, PreferredMaintenanceWindow: str = None, Tags: List = None, StorageEncrypted: bool = None, KmsKeyId: str = None, EnableCloudwatchLogsExports: List = None) -> Dict:
        """
        Creates a new Amazon DocumentDB DB cluster.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/CreateDBCluster>`_
        
        **Request Syntax**
        ::
          response = client.create_db_cluster(
              AvailabilityZones=[
                  'string',
              ],
              BackupRetentionPeriod=123,
              DBClusterIdentifier='string',
              DBClusterParameterGroupName='string',
              VpcSecurityGroupIds=[
                  'string',
              ],
              DBSubnetGroupName='string',
              Engine='string',
              EngineVersion='string',
              Port=123,
              MasterUsername='string',
              MasterUserPassword='string',
              PreferredBackupWindow='string',
              PreferredMaintenanceWindow='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              StorageEncrypted=True|False,
              KmsKeyId='string',
              EnableCloudwatchLogsExports=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'DBCluster': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBCluster** *(dict) --* 
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
        :type AvailabilityZones: list
        :param AvailabilityZones:
          A list of Amazon EC2 Availability Zones that instances in the DB cluster can be created in.
          - *(string) --*
        :type BackupRetentionPeriod: integer
        :param BackupRetentionPeriod:
          The number of days for which automated backups are retained. You must specify a minimum value of 1.
          Default: 1
          Constraints:
          * Must be a value from 1 to 35.
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]**
          The DB cluster identifier. This parameter is stored as a lowercase string.
          Constraints:
          * Must contain from 1 to 63 letters, numbers, or hyphens.
          * The first character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
          Example: ``my-cluster``
        :type DBClusterParameterGroupName: string
        :param DBClusterParameterGroupName:
          The name of the DB cluster parameter group to associate with this DB cluster.
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds:
          A list of EC2 VPC security groups to associate with this DB cluster.
          - *(string) --*
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName:
          A DB subnet group to associate with this DB cluster.
          Constraints: Must match the name of an existing ``DBSubnetGroup`` . Must not be default.
          Example: ``mySubnetgroup``
        :type Engine: string
        :param Engine: **[REQUIRED]**
          The name of the database engine to be used for this DB cluster.
          Valid values: ``docdb``
        :type EngineVersion: string
        :param EngineVersion:
          The version number of the database engine to use.
        :type Port: integer
        :param Port:
          The port number on which the instances in the DB cluster accept connections.
        :type MasterUsername: string
        :param MasterUsername:
          The name of the master user for the DB cluster.
          Constraints:
          * Must be from 1 to 16 letters or numbers.
          * The first character must be a letter.
          * Cannot be a reserved word for the chosen database engine.
        :type MasterUserPassword: string
        :param MasterUserPassword:
          The password for the master database user. This password can contain any printable ASCII character except \"/\", \"\"\", or \"@\".
          Constraints: Must contain from 8 to 41 characters.
        :type PreferredBackupWindow: string
        :param PreferredBackupWindow:
          The daily time range during which automated backups are created if automated backups are enabled using the ``BackupRetentionPeriod`` parameter.
          The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region.
          Constraints:
          * Must be in the format ``hh24:mi-hh24:mi`` .
          * Must be in Universal Coordinated Time (UTC).
          * Must not conflict with the preferred maintenance window.
          * Must be at least 30 minutes.
        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow:
          The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
          Format: ``ddd:hh24:mi-ddd:hh24:mi``
          The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
          Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
          Constraints: Minimum 30-minute window.
        :type Tags: list
        :param Tags:
          The tags to be assigned to the DB cluster.
          - *(dict) --*
            Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
            - **Key** *(string) --*
              The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
            - **Value** *(string) --*
              The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        :type StorageEncrypted: boolean
        :param StorageEncrypted:
          Specifies whether the DB cluster is encrypted.
        :type KmsKeyId: string
        :param KmsKeyId:
          The AWS KMS key identifier for an encrypted DB cluster.
          The AWS KMS key identifier is the Amazon Resource Name (ARN) for the AWS KMS encryption key. If you are creating a DB cluster using the same AWS account that owns the AWS KMS encryption key that is used to encrypt the new DB cluster, you can use the AWS KMS key alias instead of the ARN for the AWS KMS encryption key.
          If an encryption key is not specified in ``KmsKeyId`` :
          * If ``ReplicationSourceIdentifier`` identifies an encrypted source, then Amazon DocumentDB uses the encryption key that is used to encrypt the source. Otherwise, Amazon DocumentDB uses your default encryption key.
          * If the ``StorageEncrypted`` parameter is ``true`` and ``ReplicationSourceIdentifier`` is not specified, Amazon DocumentDB uses your default encryption key.
          AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
          If you create a replica of an encrypted DB cluster in another AWS Region, you must set ``KmsKeyId`` to a KMS key ID that is valid in the destination AWS Region. This key is used to encrypt the replica in that AWS Region.
        :type EnableCloudwatchLogsExports: list
        :param EnableCloudwatchLogsExports:
          A list of log types that need to be enabled for exporting to Amazon CloudWatch Logs.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def create_db_cluster_parameter_group(self, DBClusterParameterGroupName: str, DBParameterGroupFamily: str, Description: str, Tags: List = None) -> Dict:
        """
        Creates a new DB cluster parameter group.
        Parameters in a DB cluster parameter group apply to all of the instances in a DB cluster.
        A DB cluster parameter group is initially created with the default parameters for the database engine used by instances in the DB cluster. To provide custom values for any of the parameters, you must modify the group after you create it. After you create a DB cluster parameter group, you must associate it with your DB cluster. For the new DB cluster parameter group and associated settings to take effect, you must then reboot the DB instances in the DB cluster without failover.
        .. warning::
          After you create a DB cluster parameter group, you should wait at least 5 minutes before creating your first DB cluster that uses that DB cluster parameter group as the default parameter group. This allows Amazon DocumentDB to fully complete the create action before the DB cluster parameter group is used as the default for a new DB cluster. This step is especially important for parameters that are critical when creating the default database for a DB cluster, such as the character set for the default database defined by the ``character_set_database`` parameter.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/CreateDBClusterParameterGroup>`_
        
        **Request Syntax**
        ::
          response = client.create_db_cluster_parameter_group(
              DBClusterParameterGroupName='string',
              DBParameterGroupFamily='string',
              Description='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'DBClusterParameterGroup': {
                    'DBClusterParameterGroupName': 'string',
                    'DBParameterGroupFamily': 'string',
                    'Description': 'string',
                    'DBClusterParameterGroupArn': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBClusterParameterGroup** *(dict) --* 
              Detailed information about a DB cluster parameter group. 
              - **DBClusterParameterGroupName** *(string) --* 
                Provides the name of the DB cluster parameter group.
              - **DBParameterGroupFamily** *(string) --* 
                Provides the name of the DB parameter group family that this DB cluster parameter group is compatible with.
              - **Description** *(string) --* 
                Provides the customer-specified description for this DB cluster parameter group.
              - **DBClusterParameterGroupArn** *(string) --* 
                The Amazon Resource Name (ARN) for the DB cluster parameter group.
        :type DBClusterParameterGroupName: string
        :param DBClusterParameterGroupName: **[REQUIRED]**
          The name of the DB cluster parameter group.
          Constraints:
          * Must match the name of an existing ``DBClusterParameterGroup`` .
          .. note::
            This value is stored as a lowercase string.
        :type DBParameterGroupFamily: string
        :param DBParameterGroupFamily: **[REQUIRED]**
          The DB cluster parameter group family name.
        :type Description: string
        :param Description: **[REQUIRED]**
          The description for the DB cluster parameter group.
        :type Tags: list
        :param Tags:
          The tags to be assigned to the DB cluster parameter group.
          - *(dict) --*
            Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
            - **Key** *(string) --*
              The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
            - **Value** *(string) --*
              The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        :rtype: dict
        :returns:
        """
        pass

    def create_db_cluster_snapshot(self, DBClusterSnapshotIdentifier: str, DBClusterIdentifier: str, Tags: List = None) -> Dict:
        """
        Creates a snapshot of a DB cluster. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/CreateDBClusterSnapshot>`_
        
        **Request Syntax**
        ::
          response = client.create_db_cluster_snapshot(
              DBClusterSnapshotIdentifier='string',
              DBClusterIdentifier='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'DBClusterSnapshot': {
                    'AvailabilityZones': [
                        'string',
                    ],
                    'DBClusterSnapshotIdentifier': 'string',
                    'DBClusterIdentifier': 'string',
                    'SnapshotCreateTime': datetime(2015, 1, 1),
                    'Engine': 'string',
                    'Status': 'string',
                    'Port': 123,
                    'VpcId': 'string',
                    'ClusterCreateTime': datetime(2015, 1, 1),
                    'MasterUsername': 'string',
                    'EngineVersion': 'string',
                    'SnapshotType': 'string',
                    'PercentProgress': 123,
                    'StorageEncrypted': True|False,
                    'KmsKeyId': 'string',
                    'DBClusterSnapshotArn': 'string',
                    'SourceDBClusterSnapshotArn': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBClusterSnapshot** *(dict) --* 
              Detailed information about a DB cluster snapshot. 
              - **AvailabilityZones** *(list) --* 
                Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.
                - *(string) --* 
              - **DBClusterSnapshotIdentifier** *(string) --* 
                Specifies the identifier for the DB cluster snapshot.
              - **DBClusterIdentifier** *(string) --* 
                Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.
              - **SnapshotCreateTime** *(datetime) --* 
                Provides the time when the snapshot was taken, in UTC.
              - **Engine** *(string) --* 
                Specifies the name of the database engine.
              - **Status** *(string) --* 
                Specifies the status of this DB cluster snapshot.
              - **Port** *(integer) --* 
                Specifies the port that the DB cluster was listening on at the time of the snapshot.
              - **VpcId** *(string) --* 
                Provides the virtual private cloud (VPC) ID that is associated with the DB cluster snapshot.
              - **ClusterCreateTime** *(datetime) --* 
                Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).
              - **MasterUsername** *(string) --* 
                Provides the master user name for the DB cluster snapshot.
              - **EngineVersion** *(string) --* 
                Provides the version of the database engine for this DB cluster snapshot.
              - **SnapshotType** *(string) --* 
                Provides the type of the DB cluster snapshot.
              - **PercentProgress** *(integer) --* 
                Specifies the percentage of the estimated data that has been transferred.
              - **StorageEncrypted** *(boolean) --* 
                Specifies whether the DB cluster snapshot is encrypted.
              - **KmsKeyId** *(string) --* 
                If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB cluster snapshot.
              - **DBClusterSnapshotArn** *(string) --* 
                The Amazon Resource Name (ARN) for the DB cluster snapshot.
              - **SourceDBClusterSnapshotArn** *(string) --* 
                If the DB cluster snapshot was copied from a source DB cluster snapshot, the ARN for the source DB cluster snapshot; otherwise, a null value.
        :type DBClusterSnapshotIdentifier: string
        :param DBClusterSnapshotIdentifier: **[REQUIRED]**
          The identifier of the DB cluster snapshot. This parameter is stored as a lowercase string.
          Constraints:
          * Must contain from 1 to 63 letters, numbers, or hyphens.
          * The first character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
          Example: ``my-cluster-snapshot1``
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]**
          The identifier of the DB cluster to create a snapshot for. This parameter is not case sensitive.
          Constraints:
          * Must match the identifier of an existing ``DBCluster`` .
          Example: ``my-cluster``
        :type Tags: list
        :param Tags:
          The tags to be assigned to the DB cluster snapshot.
          - *(dict) --*
            Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
            - **Key** *(string) --*
              The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
            - **Value** *(string) --*
              The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        :rtype: dict
        :returns:
        """
        pass

    def create_db_instance(self, DBInstanceIdentifier: str, DBInstanceClass: str, Engine: str, DBClusterIdentifier: str, AvailabilityZone: str = None, PreferredMaintenanceWindow: str = None, AutoMinorVersionUpgrade: bool = None, Tags: List = None, PromotionTier: int = None) -> Dict:
        """
        Creates a new DB instance.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/CreateDBInstance>`_
        
        **Request Syntax**
        ::
          response = client.create_db_instance(
              DBInstanceIdentifier='string',
              DBInstanceClass='string',
              Engine='string',
              AvailabilityZone='string',
              PreferredMaintenanceWindow='string',
              AutoMinorVersionUpgrade=True|False,
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              DBClusterIdentifier='string',
              PromotionTier=123
          )
        
        **Response Syntax**
        ::
            {
                'DBInstance': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBInstance** *(dict) --* 
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
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: **[REQUIRED]**
          The DB instance identifier. This parameter is stored as a lowercase string.
          Constraints:
          * Must contain from 1 to 63 letters, numbers, or hyphens.
          * The first character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
          Example: ``mydbinstance``
        :type DBInstanceClass: string
        :param DBInstanceClass: **[REQUIRED]**
          The compute and memory capacity of the DB instance; for example, ``db.m4.large`` .
        :type Engine: string
        :param Engine: **[REQUIRED]**
          The name of the database engine to be used for this instance.
          Valid value: ``docdb``
        :type AvailabilityZone: string
        :param AvailabilityZone:
          The Amazon EC2 Availability Zone that the DB instance is created in.
          Default: A random, system-chosen Availability Zone in the endpoint\'s AWS Region.
          Example: ``us-east-1d``
          Constraint: The ``AvailabilityZone`` parameter can\'t be specified if the ``MultiAZ`` parameter is set to ``true`` . The specified Availability Zone must be in the same AWS Region as the current endpoint.
        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow:
          The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC).
          Format: ``ddd:hh24:mi-ddd:hh24:mi``
          The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
          Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
          Constraints: Minimum 30-minute window.
        :type AutoMinorVersionUpgrade: boolean
        :param AutoMinorVersionUpgrade:
          Indicates that minor engine upgrades are applied automatically to the DB instance during the maintenance window.
          Default: ``true``
        :type Tags: list
        :param Tags:
          The tags to be assigned to the DB instance.
          - *(dict) --*
            Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
            - **Key** *(string) --*
              The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
            - **Value** *(string) --*
              The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]**
          The identifier of the DB cluster that the instance will belong to.
        :type PromotionTier: integer
        :param PromotionTier:
          A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.
          Default: 1
          Valid values: 0-15
        :rtype: dict
        :returns:
        """
        pass

    def create_db_subnet_group(self, DBSubnetGroupName: str, DBSubnetGroupDescription: str, SubnetIds: List, Tags: List = None) -> Dict:
        """
        Creates a new DB subnet group. DB subnet groups must contain at least one subnet in at least two Availability Zones in the AWS Region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/CreateDBSubnetGroup>`_
        
        **Request Syntax**
        ::
          response = client.create_db_subnet_group(
              DBSubnetGroupName='string',
              DBSubnetGroupDescription='string',
              SubnetIds=[
                  'string',
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBSubnetGroup** *(dict) --* 
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
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName: **[REQUIRED]**
          The name for the DB subnet group. This value is stored as a lowercase string.
          Constraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.
          Example: ``mySubnetgroup``
        :type DBSubnetGroupDescription: string
        :param DBSubnetGroupDescription: **[REQUIRED]**
          The description for the DB subnet group.
        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]**
          The Amazon EC2 subnet IDs for the DB subnet group.
          - *(string) --*
        :type Tags: list
        :param Tags:
          The tags to be assigned to the DB subnet group.
          - *(dict) --*
            Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
            - **Key** *(string) --*
              The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
            - **Value** *(string) --*
              The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        :rtype: dict
        :returns:
        """
        pass

    def delete_db_cluster(self, DBClusterIdentifier: str, SkipFinalSnapshot: bool = None, FinalDBSnapshotIdentifier: str = None) -> Dict:
        """
        Deletes a previously provisioned DB cluster. When you delete a DB cluster, all automated backups for that DB cluster are deleted and can't be recovered. Manual DB cluster snapshots of the specified DB cluster are not deleted.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DeleteDBCluster>`_
        
        **Request Syntax**
        ::
          response = client.delete_db_cluster(
              DBClusterIdentifier='string',
              SkipFinalSnapshot=True|False,
              FinalDBSnapshotIdentifier='string'
          )
        
        **Response Syntax**
        ::
            {
                'DBCluster': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBCluster** *(dict) --* 
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
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]**
          The DB cluster identifier for the DB cluster to be deleted. This parameter isn\'t case sensitive.
          Constraints:
          * Must match an existing ``DBClusterIdentifier`` .
        :type SkipFinalSnapshot: boolean
        :param SkipFinalSnapshot:
          Determines whether a final DB cluster snapshot is created before the DB cluster is deleted. If ``true`` is specified, no DB cluster snapshot is created. If ``false`` is specified, a DB cluster snapshot is created before the DB cluster is deleted.
          .. note::
            If ``SkipFinalSnapshot`` is ``false`` , you must specify a ``FinalDBSnapshotIdentifier`` parameter.
          Default: ``false``
        :type FinalDBSnapshotIdentifier: string
        :param FinalDBSnapshotIdentifier:
          The DB cluster snapshot identifier of the new DB cluster snapshot created when ``SkipFinalSnapshot`` is set to ``false`` .
          .. note::
            Specifying this parameter and also setting the ``SkipFinalShapshot`` parameter to ``true`` results in an error.
          Constraints:
          * Must be from 1 to 255 letters, numbers, or hyphens.
          * The first character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
        :rtype: dict
        :returns:
        """
        pass

    def delete_db_cluster_parameter_group(self, DBClusterParameterGroupName: str):
        """
        Deletes a specified DB cluster parameter group. The DB cluster parameter group to be deleted can't be associated with any DB clusters.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DeleteDBClusterParameterGroup>`_
        
        **Request Syntax**
        ::
          response = client.delete_db_cluster_parameter_group(
              DBClusterParameterGroupName='string'
          )
        :type DBClusterParameterGroupName: string
        :param DBClusterParameterGroupName: **[REQUIRED]**
          The name of the DB cluster parameter group.
          Constraints:
          * Must be the name of an existing DB cluster parameter group.
          * You can\'t delete a default DB cluster parameter group.
          * Cannot be associated with any DB clusters.
        :returns: None
        """
        pass

    def delete_db_cluster_snapshot(self, DBClusterSnapshotIdentifier: str) -> Dict:
        """
        Deletes a DB cluster snapshot. If the snapshot is being copied, the copy operation is terminated.
        .. note::
          The DB cluster snapshot must be in the ``available`` state to be deleted.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DeleteDBClusterSnapshot>`_
        
        **Request Syntax**
        ::
          response = client.delete_db_cluster_snapshot(
              DBClusterSnapshotIdentifier='string'
          )
        
        **Response Syntax**
        ::
            {
                'DBClusterSnapshot': {
                    'AvailabilityZones': [
                        'string',
                    ],
                    'DBClusterSnapshotIdentifier': 'string',
                    'DBClusterIdentifier': 'string',
                    'SnapshotCreateTime': datetime(2015, 1, 1),
                    'Engine': 'string',
                    'Status': 'string',
                    'Port': 123,
                    'VpcId': 'string',
                    'ClusterCreateTime': datetime(2015, 1, 1),
                    'MasterUsername': 'string',
                    'EngineVersion': 'string',
                    'SnapshotType': 'string',
                    'PercentProgress': 123,
                    'StorageEncrypted': True|False,
                    'KmsKeyId': 'string',
                    'DBClusterSnapshotArn': 'string',
                    'SourceDBClusterSnapshotArn': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBClusterSnapshot** *(dict) --* 
              Detailed information about a DB cluster snapshot. 
              - **AvailabilityZones** *(list) --* 
                Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.
                - *(string) --* 
              - **DBClusterSnapshotIdentifier** *(string) --* 
                Specifies the identifier for the DB cluster snapshot.
              - **DBClusterIdentifier** *(string) --* 
                Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.
              - **SnapshotCreateTime** *(datetime) --* 
                Provides the time when the snapshot was taken, in UTC.
              - **Engine** *(string) --* 
                Specifies the name of the database engine.
              - **Status** *(string) --* 
                Specifies the status of this DB cluster snapshot.
              - **Port** *(integer) --* 
                Specifies the port that the DB cluster was listening on at the time of the snapshot.
              - **VpcId** *(string) --* 
                Provides the virtual private cloud (VPC) ID that is associated with the DB cluster snapshot.
              - **ClusterCreateTime** *(datetime) --* 
                Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).
              - **MasterUsername** *(string) --* 
                Provides the master user name for the DB cluster snapshot.
              - **EngineVersion** *(string) --* 
                Provides the version of the database engine for this DB cluster snapshot.
              - **SnapshotType** *(string) --* 
                Provides the type of the DB cluster snapshot.
              - **PercentProgress** *(integer) --* 
                Specifies the percentage of the estimated data that has been transferred.
              - **StorageEncrypted** *(boolean) --* 
                Specifies whether the DB cluster snapshot is encrypted.
              - **KmsKeyId** *(string) --* 
                If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB cluster snapshot.
              - **DBClusterSnapshotArn** *(string) --* 
                The Amazon Resource Name (ARN) for the DB cluster snapshot.
              - **SourceDBClusterSnapshotArn** *(string) --* 
                If the DB cluster snapshot was copied from a source DB cluster snapshot, the ARN for the source DB cluster snapshot; otherwise, a null value.
        :type DBClusterSnapshotIdentifier: string
        :param DBClusterSnapshotIdentifier: **[REQUIRED]**
          The identifier of the DB cluster snapshot to delete.
          Constraints: Must be the name of an existing DB cluster snapshot in the ``available`` state.
        :rtype: dict
        :returns:
        """
        pass

    def delete_db_instance(self, DBInstanceIdentifier: str) -> Dict:
        """
        Deletes a previously provisioned DB instance. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DeleteDBInstance>`_
        
        **Request Syntax**
        ::
          response = client.delete_db_instance(
              DBInstanceIdentifier='string'
          )
        
        **Response Syntax**
        ::
            {
                'DBInstance': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBInstance** *(dict) --* 
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
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: **[REQUIRED]**
          The DB instance identifier for the DB instance to be deleted. This parameter isn\'t case sensitive.
          Constraints:
          * Must match the name of an existing DB instance.
        :rtype: dict
        :returns:
        """
        pass

    def delete_db_subnet_group(self, DBSubnetGroupName: str):
        """
        Deletes a DB subnet group.
        .. note::
          The specified database subnet group must not be associated with any DB instances.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DeleteDBSubnetGroup>`_
        
        **Request Syntax**
        ::
          response = client.delete_db_subnet_group(
              DBSubnetGroupName='string'
          )
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName: **[REQUIRED]**
          The name of the database subnet group to delete.
          .. note::
            You can\'t delete the default subnet group.
          Constraints:
          Must match the name of an existing ``DBSubnetGroup`` . Must not be default.
          Example: ``mySubnetgroup``
        :returns: None
        """
        pass

    def describe_db_cluster_parameter_groups(self, DBClusterParameterGroupName: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        Returns a list of ``DBClusterParameterGroup`` descriptions. If a ``DBClusterParameterGroupName`` parameter is specified, the list contains only the description of the specified DB cluster parameter group. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBClusterParameterGroups>`_
        
        **Request Syntax**
        ::
          response = client.describe_db_cluster_parameter_groups(
              DBClusterParameterGroupName='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string'
          )
        
        **Response Syntax**
        ::
            {
                'Marker': 'string',
                'DBClusterParameterGroups': [
                    {
                        'DBClusterParameterGroupName': 'string',
                        'DBParameterGroupFamily': 'string',
                        'Description': 'string',
                        'DBClusterParameterGroupArn': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  DBClusterParameterGroups .
            - **Marker** *(string) --* 
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
            - **DBClusterParameterGroups** *(list) --* 
              A list of DB cluster parameter groups.
              - *(dict) --* 
                Detailed information about a DB cluster parameter group. 
                - **DBClusterParameterGroupName** *(string) --* 
                  Provides the name of the DB cluster parameter group.
                - **DBParameterGroupFamily** *(string) --* 
                  Provides the name of the DB parameter group family that this DB cluster parameter group is compatible with.
                - **Description** *(string) --* 
                  Provides the customer-specified description for this DB cluster parameter group.
                - **DBClusterParameterGroupArn** *(string) --* 
                  The Amazon Resource Name (ARN) for the DB cluster parameter group.
        :type DBClusterParameterGroupName: string
        :param DBClusterParameterGroupName:
          The name of a specific DB cluster parameter group to return details for.
          Constraints:
          * If provided, must match the name of an existing ``DBClusterParameterGroup`` .
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
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.
          Default: 100
          Constraints: Minimum 20, maximum 100.
        :type Marker: string
        :param Marker:
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_db_cluster_parameters(self, DBClusterParameterGroupName: str, Source: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        Returns the detailed parameter list for a particular DB cluster parameter group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBClusterParameters>`_
        
        **Request Syntax**
        ::
          response = client.describe_db_cluster_parameters(
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
              MaxRecords=123,
              Marker='string'
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
                'Marker': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  DBClusterParameterGroup .
            - **Parameters** *(list) --* 
              Provides a list of parameters for the DB cluster parameter group.
              - *(dict) --* 
                Detailed information about an individual parameter.
                - **ParameterName** *(string) --* 
                  Specifies the name of the parameter.
                - **ParameterValue** *(string) --* 
                  Specifies the value of the parameter.
                - **Description** *(string) --* 
                  Provides a description of the parameter.
                - **Source** *(string) --* 
                  Indicates the source of the parameter value.
                - **ApplyType** *(string) --* 
                  Specifies the engine-specific parameters type.
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
            - **Marker** *(string) --* 
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        :type DBClusterParameterGroupName: string
        :param DBClusterParameterGroupName: **[REQUIRED]**
          The name of a specific DB cluster parameter group to return parameter details for.
          Constraints:
          * If provided, must match the name of an existing ``DBClusterParameterGroup`` .
        :type Source: string
        :param Source:
          A value that indicates to return only parameters for a specific source. Parameter sources can be ``engine`` , ``service`` , or ``customer`` .
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
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.
          Default: 100
          Constraints: Minimum 20, maximum 100.
        :type Marker: string
        :param Marker:
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_db_cluster_snapshot_attributes(self, DBClusterSnapshotIdentifier: str) -> Dict:
        """
        Returns a list of DB cluster snapshot attribute names and values for a manual DB cluster snapshot.
        When you share snapshots with other AWS accounts, ``DescribeDBClusterSnapshotAttributes`` returns the ``restore`` attribute and a list of IDs for the AWS accounts that are authorized to copy or restore the manual DB cluster snapshot. If ``all`` is included in the list of values for the ``restore`` attribute, then the manual DB cluster snapshot is public and can be copied or restored by all AWS accounts.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes>`_
        
        **Request Syntax**
        ::
          response = client.describe_db_cluster_snapshot_attributes(
              DBClusterSnapshotIdentifier='string'
          )
        
        **Response Syntax**
        ::
            {
                'DBClusterSnapshotAttributesResult': {
                    'DBClusterSnapshotIdentifier': 'string',
                    'DBClusterSnapshotAttributes': [
                        {
                            'AttributeName': 'string',
                            'AttributeValues': [
                                'string',
                            ]
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBClusterSnapshotAttributesResult** *(dict) --* 
              Detailed information about the attributes that are associated with a DB cluster snapshot.
              - **DBClusterSnapshotIdentifier** *(string) --* 
                The identifier of the DB cluster snapshot that the attributes apply to.
              - **DBClusterSnapshotAttributes** *(list) --* 
                The list of attributes and values for the DB cluster snapshot.
                - *(dict) --* 
                  Contains the name and values of a manual DB cluster snapshot attribute.
                  Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore a manual DB cluster snapshot.
                  - **AttributeName** *(string) --* 
                    The name of the manual DB cluster snapshot attribute.
                    The attribute named ``restore`` refers to the list of AWS accounts that have permission to copy or restore the manual DB cluster snapshot.
                  - **AttributeValues** *(list) --* 
                    The values for the manual DB cluster snapshot attribute.
                    If the ``AttributeName`` field is set to ``restore`` , then this element returns a list of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is public and available for any AWS account to copy or restore.
                    - *(string) --* 
        :type DBClusterSnapshotIdentifier: string
        :param DBClusterSnapshotIdentifier: **[REQUIRED]**
          The identifier for the DB cluster snapshot to describe the attributes for.
        :rtype: dict
        :returns:
        """
        pass

    def describe_db_cluster_snapshots(self, DBClusterIdentifier: str = None, DBClusterSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, IncludeShared: bool = None, IncludePublic: bool = None) -> Dict:
        """
        Returns information about DB cluster snapshots. This API operation supports pagination.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBClusterSnapshots>`_
        
        **Request Syntax**
        ::
          response = client.describe_db_cluster_snapshots(
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
              MaxRecords=123,
              Marker='string',
              IncludeShared=True|False,
              IncludePublic=True|False
          )
        
        **Response Syntax**
        ::
            {
                'Marker': 'string',
                'DBClusterSnapshots': [
                    {
                        'AvailabilityZones': [
                            'string',
                        ],
                        'DBClusterSnapshotIdentifier': 'string',
                        'DBClusterIdentifier': 'string',
                        'SnapshotCreateTime': datetime(2015, 1, 1),
                        'Engine': 'string',
                        'Status': 'string',
                        'Port': 123,
                        'VpcId': 'string',
                        'ClusterCreateTime': datetime(2015, 1, 1),
                        'MasterUsername': 'string',
                        'EngineVersion': 'string',
                        'SnapshotType': 'string',
                        'PercentProgress': 123,
                        'StorageEncrypted': True|False,
                        'KmsKeyId': 'string',
                        'DBClusterSnapshotArn': 'string',
                        'SourceDBClusterSnapshotArn': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  DescribeDBClusterSnapshots .
            - **Marker** *(string) --* 
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
            - **DBClusterSnapshots** *(list) --* 
              Provides a list of DB cluster snapshots.
              - *(dict) --* 
                Detailed information about a DB cluster snapshot. 
                - **AvailabilityZones** *(list) --* 
                  Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.
                  - *(string) --* 
                - **DBClusterSnapshotIdentifier** *(string) --* 
                  Specifies the identifier for the DB cluster snapshot.
                - **DBClusterIdentifier** *(string) --* 
                  Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.
                - **SnapshotCreateTime** *(datetime) --* 
                  Provides the time when the snapshot was taken, in UTC.
                - **Engine** *(string) --* 
                  Specifies the name of the database engine.
                - **Status** *(string) --* 
                  Specifies the status of this DB cluster snapshot.
                - **Port** *(integer) --* 
                  Specifies the port that the DB cluster was listening on at the time of the snapshot.
                - **VpcId** *(string) --* 
                  Provides the virtual private cloud (VPC) ID that is associated with the DB cluster snapshot.
                - **ClusterCreateTime** *(datetime) --* 
                  Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).
                - **MasterUsername** *(string) --* 
                  Provides the master user name for the DB cluster snapshot.
                - **EngineVersion** *(string) --* 
                  Provides the version of the database engine for this DB cluster snapshot.
                - **SnapshotType** *(string) --* 
                  Provides the type of the DB cluster snapshot.
                - **PercentProgress** *(integer) --* 
                  Specifies the percentage of the estimated data that has been transferred.
                - **StorageEncrypted** *(boolean) --* 
                  Specifies whether the DB cluster snapshot is encrypted.
                - **KmsKeyId** *(string) --* 
                  If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB cluster snapshot.
                - **DBClusterSnapshotArn** *(string) --* 
                  The Amazon Resource Name (ARN) for the DB cluster snapshot.
                - **SourceDBClusterSnapshotArn** *(string) --* 
                  If the DB cluster snapshot was copied from a source DB cluster snapshot, the ARN for the source DB cluster snapshot; otherwise, a null value.
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier:
          The ID of the DB cluster to retrieve the list of DB cluster snapshots for. This parameter can\'t be used with the ``DBClusterSnapshotIdentifier`` parameter. This parameter is not case sensitive.
          Constraints:
          * If provided, must match the identifier of an existing ``DBCluster`` .
        :type DBClusterSnapshotIdentifier: string
        :param DBClusterSnapshotIdentifier:
          A specific DB cluster snapshot identifier to describe. This parameter can\'t be used with the ``DBClusterIdentifier`` parameter. This value is stored as a lowercase string.
          Constraints:
          * If provided, must match the identifier of an existing ``DBClusterSnapshot`` .
          * If this identifier is for an automated snapshot, the ``SnapshotType`` parameter must also be specified.
        :type SnapshotType: string
        :param SnapshotType:
          The type of DB cluster snapshots to be returned. You can specify one of the following values:
          * ``automated`` - Return all DB cluster snapshots that Amazon DocumentDB has automatically created for your AWS account.
          * ``manual`` - Return all DB cluster snapshots that you have manually created for your AWS account.
          * ``shared`` - Return all manual DB cluster snapshots that have been shared to your AWS account.
          * ``public`` - Return all DB cluster snapshots that have been marked as public.
          If you don\'t specify a ``SnapshotType`` value, then both automated and manual DB cluster snapshots are returned. You can include shared DB cluster snapshots with these results by setting the ``IncludeShared`` parameter to ``true`` . You can include public DB cluster snapshots with these results by setting the ``IncludePublic`` parameter to ``true`` .
          The ``IncludeShared`` and ``IncludePublic`` parameters don\'t apply for ``SnapshotType`` values of ``manual`` or ``automated`` . The ``IncludePublic`` parameter doesn\'t apply when ``SnapshotType`` is set to ``shared`` . The ``IncludeShared`` parameter doesn\'t apply when ``SnapshotType`` is set to ``public`` .
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
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.
          Default: 100
          Constraints: Minimum 20, maximum 100.
        :type Marker: string
        :param Marker:
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        :type IncludeShared: boolean
        :param IncludeShared:
          Set to ``true`` to include shared manual DB cluster snapshots from other AWS accounts that this AWS account has been given permission to copy or restore, and otherwise ``false`` . The default is ``false`` .
        :type IncludePublic: boolean
        :param IncludePublic:
          Set to ``true`` to include manual DB cluster snapshots that are public and can be copied or restored by any AWS account, and otherwise ``false`` . The default is ``false`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_db_clusters(self, DBClusterIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        Returns information about provisioned Amazon DocumentDB DB clusters. This API operation supports pagination.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBClusters>`_
        
        **Request Syntax**
        ::
          response = client.describe_db_clusters(
              DBClusterIdentifier='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string'
          )
        
        **Response Syntax**
        ::
            {
                'Marker': 'string',
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
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  DescribeDBClusters .
            - **Marker** *(string) --* 
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
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
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.
          Default: 100
          Constraints: Minimum 20, maximum 100.
        :type Marker: string
        :param Marker:
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_db_engine_versions(self, Engine: str = None, EngineVersion: str = None, DBParameterGroupFamily: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, DefaultOnly: bool = None, ListSupportedCharacterSets: bool = None, ListSupportedTimezones: bool = None) -> Dict:
        """
        Returns a list of the available DB engines.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBEngineVersions>`_
        
        **Request Syntax**
        ::
          response = client.describe_db_engine_versions(
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
              MaxRecords=123,
              Marker='string',
              DefaultOnly=True|False,
              ListSupportedCharacterSets=True|False,
              ListSupportedTimezones=True|False
          )
        
        **Response Syntax**
        ::
            {
                'Marker': 'string',
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
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  DescribeDBEngineVersions .
            - **Marker** *(string) --* 
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
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
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.
          Default: 100
          Constraints: Minimum 20, maximum 100.
        :type Marker: string
        :param Marker:
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        :type DefaultOnly: boolean
        :param DefaultOnly:
          Indicates that only the default version of the specified engine or engine and major version combination is returned.
        :type ListSupportedCharacterSets: boolean
        :param ListSupportedCharacterSets:
          If this parameter is specified and the requested engine supports the ``CharacterSetName`` parameter for ``CreateDBInstance`` , the response includes a list of supported character sets for each engine version.
        :type ListSupportedTimezones: boolean
        :param ListSupportedTimezones:
          If this parameter is specified and the requested engine supports the ``TimeZone`` parameter for ``CreateDBInstance`` , the response includes a list of supported time zones for each engine version.
        :rtype: dict
        :returns:
        """
        pass

    def describe_db_instances(self, DBInstanceIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        Returns information about provisioned Amazon DocumentDB instances. This API supports pagination.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBInstances>`_
        
        **Request Syntax**
        ::
          response = client.describe_db_instances(
              DBInstanceIdentifier='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string'
          )
        
        **Response Syntax**
        ::
            {
                'Marker': 'string',
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
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  DescribeDBInstances .
            - **Marker** *(string) --* 
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
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
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.
          Default: 100
          Constraints: Minimum 20, maximum 100.
        :type Marker: string
        :param Marker:
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_db_subnet_groups(self, DBSubnetGroupName: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        Returns a list of ``DBSubnetGroup`` descriptions. If a ``DBSubnetGroupName`` is specified, the list will contain only the descriptions of the specified ``DBSubnetGroup`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeDBSubnetGroups>`_
        
        **Request Syntax**
        ::
          response = client.describe_db_subnet_groups(
              DBSubnetGroupName='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string'
          )
        
        **Response Syntax**
        ::
            {
                'Marker': 'string',
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
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  DescribeDBSubnetGroups .
            - **Marker** *(string) --* 
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
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
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.
          Default: 100
          Constraints: Minimum 20, maximum 100.
        :type Marker: string
        :param Marker:
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_engine_default_cluster_parameters(self, DBParameterGroupFamily: str, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        Returns the default engine and system parameter information for the cluster database engine.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeEngineDefaultClusterParameters>`_
        
        **Request Syntax**
        ::
          response = client.describe_engine_default_cluster_parameters(
              DBParameterGroupFamily='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string'
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EngineDefaults** *(dict) --* 
              Contains the result of a successful invocation of the ``DescribeEngineDefaultClusterParameters`` operation. 
              - **DBParameterGroupFamily** *(string) --* 
                The name of the DB cluster parameter group family to return the engine parameter information for.
              - **Marker** *(string) --* 
                An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
              - **Parameters** *(list) --* 
                The parameters of a particular DB cluster parameter group family.
                - *(dict) --* 
                  Detailed information about an individual parameter.
                  - **ParameterName** *(string) --* 
                    Specifies the name of the parameter.
                  - **ParameterValue** *(string) --* 
                    Specifies the value of the parameter.
                  - **Description** *(string) --* 
                    Provides a description of the parameter.
                  - **Source** *(string) --* 
                    Indicates the source of the parameter value.
                  - **ApplyType** *(string) --* 
                    Specifies the engine-specific parameters type.
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
        :type DBParameterGroupFamily: string
        :param DBParameterGroupFamily: **[REQUIRED]**
          The name of the DB cluster parameter group family to return the engine parameter information for.
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
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.
          Default: 100
          Constraints: Minimum 20, maximum 100.
        :type Marker: string
        :param Marker:
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_event_categories(self, SourceType: str = None, Filters: List = None) -> Dict:
        """
        Displays a list of categories for all event source types, or, if specified, for a specified source type. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeEventCategories>`_
        
        **Request Syntax**
        ::
          response = client.describe_event_categories(
              SourceType='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'EventCategoriesMapList': [
                    {
                        'SourceType': 'string',
                        'EventCategories': [
                            'string',
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  DescribeEventCategories .
            - **EventCategoriesMapList** *(list) --* 
              A list of event category maps.
              - *(dict) --* 
                An event source type, accompanied by one or more event category names.
                - **SourceType** *(string) --* 
                  The source type that the returned categories belong to.
                - **EventCategories** *(list) --* 
                  The event categories for the specified source type.
                  - *(string) --* 
        :type SourceType: string
        :param SourceType:
          The type of source that is generating the events.
          Valid values: ``db-instance`` , ``db-parameter-group`` , ``db-security-group`` , ``db-snapshot``
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
        :rtype: dict
        :returns:
        """
        pass

    def describe_events(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, EventCategories: List = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        Returns events related to DB instances, DB security groups, DB snapshots, and DB parameter groups for the past 14 days. You can obtain events specific to a particular DB instance, DB security group, DB snapshot, or DB parameter group by providing the name as a parameter. By default, the events of the past hour are returned.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeEvents>`_
        
        **Request Syntax**
        ::
          response = client.describe_events(
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
              MaxRecords=123,
              Marker='string'
          )
        
        **Response Syntax**
        ::
            {
                'Marker': 'string',
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
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  DescribeEvents .
            - **Marker** *(string) --* 
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
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
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.
          Default: 100
          Constraints: Minimum 20, maximum 100.
        :type Marker: string
        :param Marker:
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_orderable_db_instance_options(self, Engine: str, EngineVersion: str = None, DBInstanceClass: str = None, LicenseModel: str = None, Vpc: bool = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        Returns a list of orderable DB instance options for the specified engine.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribeOrderableDBInstanceOptions>`_
        
        **Request Syntax**
        ::
          response = client.describe_orderable_db_instance_options(
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
              MaxRecords=123,
              Marker='string'
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
                'Marker': 'string'
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
            - **Marker** *(string) --* 
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
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
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.
          Default: 100
          Constraints: Minimum 20, maximum 100.
        :type Marker: string
        :param Marker:
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_pending_maintenance_actions(self, ResourceIdentifier: str = None, Filters: List = None, Marker: str = None, MaxRecords: int = None) -> Dict:
        """
        Returns a list of resources (for example, DB instances) that have at least one pending maintenance action.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/DescribePendingMaintenanceActions>`_
        
        **Request Syntax**
        ::
          response = client.describe_pending_maintenance_actions(
              ResourceIdentifier='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              Marker='string',
              MaxRecords=123
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
                'Marker': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  DescribePendingMaintenanceActions .
            - **PendingMaintenanceActions** *(list) --* 
              The maintenance actions to be applied.
              - *(dict) --* 
                Represents the output of  ApplyPendingMaintenanceAction .
                - **ResourceIdentifier** *(string) --* 
                  The Amazon Resource Name (ARN) of the resource that has pending maintenance actions.
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
                      The effective date when the pending maintenance action is applied to the resource.
                    - **Description** *(string) --* 
                      A description providing more detail about the maintenance action.
            - **Marker** *(string) --* 
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        :type ResourceIdentifier: string
        :param ResourceIdentifier:
          The ARN of a resource to return pending maintenance actions for.
        :type Filters: list
        :param Filters:
          A filter that specifies one or more resources to return pending maintenance actions for.
          Supported filters:
          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list includes only pending maintenance actions for the DB clusters identified by these ARNs.
          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance ARNs. The results list includes only pending maintenance actions for the DB instances identified by these ARNs.
          - *(dict) --*
            A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.
            Wildcards are not supported in filters.
            - **Name** *(string) --* **[REQUIRED]**
              The name of the filter. Filter names are case sensitive.
            - **Values** *(list) --* **[REQUIRED]**
              One or more filter values. Filter values are case sensitive.
              - *(string) --*
        :type Marker: string
        :param Marker:
          An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.
          Default: 100
          Constraints: Minimum 20, maximum 100.
        :rtype: dict
        :returns:
        """
        pass

    def failover_db_cluster(self, DBClusterIdentifier: str = None, TargetDBInstanceIdentifier: str = None) -> Dict:
        """
        Forces a failover for a DB cluster.
        A failover for a DB cluster promotes one of the Amazon DocumentDB replicas (read-only instances) in the DB cluster to be the primary instance (the cluster writer).
        If the primary instance fails, Amazon DocumentDB automatically fails over to an Amazon DocumentDB replica, if one exists. You can force a failover when you want to simulate a failure of a primary instance for testing.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/FailoverDBCluster>`_
        
        **Request Syntax**
        ::
          response = client.failover_db_cluster(
              DBClusterIdentifier='string',
              TargetDBInstanceIdentifier='string'
          )
        
        **Response Syntax**
        ::
            {
                'DBCluster': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBCluster** *(dict) --* 
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
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier:
          A DB cluster identifier to force a failover for. This parameter is not case sensitive.
          Constraints:
          * Must match the identifier of an existing ``DBCluster`` .
        :type TargetDBInstanceIdentifier: string
        :param TargetDBInstanceIdentifier:
          The name of the instance to promote to the primary instance.
          You must specify the instance identifier for an Amazon DocumentDB replica in the DB cluster. For example, ``mydbcluster-replica1`` .
        :rtype: dict
        :returns:
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        """
        Generate a presigned url given a client, its method, and arguments
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
        Create a paginator for an operation.
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
        Returns an object that can wait for some condition.
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_tags_for_resource(self, ResourceName: str, Filters: List = None) -> Dict:
        """
        Lists all tags on an Amazon DocumentDB resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response = client.list_tags_for_resource(
              ResourceName='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'TagList': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the output of  ListTagsForResource .
            - **TagList** *(list) --* 
              A list of one or more tags.
              - *(dict) --* 
                Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
                - **Key** *(string) --* 
                  The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
                - **Value** *(string) --* 
                  The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
        :type ResourceName: string
        :param ResourceName: **[REQUIRED]**
          The Amazon DocumentDB resource with tags to be listed. This value is an Amazon Resource Name (ARN).
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
        :rtype: dict
        :returns:
        """
        pass

    def modify_db_cluster(self, DBClusterIdentifier: str, NewDBClusterIdentifier: str = None, ApplyImmediately: bool = None, BackupRetentionPeriod: int = None, DBClusterParameterGroupName: str = None, VpcSecurityGroupIds: List = None, Port: int = None, MasterUserPassword: str = None, PreferredBackupWindow: str = None, PreferredMaintenanceWindow: str = None, CloudwatchLogsExportConfiguration: Dict = None, EngineVersion: str = None) -> Dict:
        """
        Modifies a setting for an Amazon DocumentDB DB cluster. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/ModifyDBCluster>`_
        
        **Request Syntax**
        ::
          response = client.modify_db_cluster(
              DBClusterIdentifier='string',
              NewDBClusterIdentifier='string',
              ApplyImmediately=True|False,
              BackupRetentionPeriod=123,
              DBClusterParameterGroupName='string',
              VpcSecurityGroupIds=[
                  'string',
              ],
              Port=123,
              MasterUserPassword='string',
              PreferredBackupWindow='string',
              PreferredMaintenanceWindow='string',
              CloudwatchLogsExportConfiguration={
                  'EnableLogTypes': [
                      'string',
                  ],
                  'DisableLogTypes': [
                      'string',
                  ]
              },
              EngineVersion='string'
          )
        
        **Response Syntax**
        ::
            {
                'DBCluster': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBCluster** *(dict) --* 
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
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]**
          The DB cluster identifier for the cluster that is being modified. This parameter is not case sensitive.
          Constraints:
          * Must match the identifier of an existing ``DBCluster`` .
        :type NewDBClusterIdentifier: string
        :param NewDBClusterIdentifier:
          The new DB cluster identifier for the DB cluster when renaming a DB cluster. This value is stored as a lowercase string.
          Constraints:
          * Must contain from 1 to 63 letters, numbers, or hyphens.
          * The first character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
          Example: ``my-cluster2``
        :type ApplyImmediately: boolean
        :param ApplyImmediately:
          A value that specifies whether the changes in this request and any pending changes are asynchronously applied as soon as possible, regardless of the ``PreferredMaintenanceWindow`` setting for the DB cluster. If this parameter is set to ``false`` , changes to the DB cluster are applied during the next maintenance window.
          The ``ApplyImmediately`` parameter affects only the ``NewDBClusterIdentifier`` and ``MasterUserPassword`` values. If you set this parameter value to ``false`` , the changes to the ``NewDBClusterIdentifier`` and ``MasterUserPassword`` values are applied during the next maintenance window. All other changes are applied immediately, regardless of the value of the ``ApplyImmediately`` parameter.
          Default: ``false``
        :type BackupRetentionPeriod: integer
        :param BackupRetentionPeriod:
          The number of days for which automated backups are retained. You must specify a minimum value of 1.
          Default: 1
          Constraints:
          * Must be a value from 1 to 35.
        :type DBClusterParameterGroupName: string
        :param DBClusterParameterGroupName:
          The name of the DB cluster parameter group to use for the DB cluster.
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds:
          A list of virtual private cloud (VPC) security groups that the DB cluster will belong to.
          - *(string) --*
        :type Port: integer
        :param Port:
          The port number on which the DB cluster accepts connections.
          Constraints: Must be a value from ``1150`` to ``65535`` .
          Default: The same port as the original DB cluster.
        :type MasterUserPassword: string
        :param MasterUserPassword:
          The new password for the master database user. This password can contain any printable ASCII character except \"``/`` \", \"``\"`` \", or \"``@`` \".
          Constraints: Must contain from 8 to 41 characters.
        :type PreferredBackupWindow: string
        :param PreferredBackupWindow:
          The daily time range during which automated backups are created if automated backups are enabled, using the ``BackupRetentionPeriod`` parameter.
          The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region.
          Constraints:
          * Must be in the format ``hh24:mi-hh24:mi`` .
          * Must be in Universal Coordinated Time (UTC).
          * Must not conflict with the preferred maintenance window.
          * Must be at least 30 minutes.
        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow:
          The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
          Format: ``ddd:hh24:mi-ddd:hh24:mi``
          The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
          Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
          Constraints: Minimum 30-minute window.
        :type CloudwatchLogsExportConfiguration: dict
        :param CloudwatchLogsExportConfiguration:
          The configuration setting for the log types to be enabled for export to Amazon CloudWatch Logs for a specific DB instance or DB cluster. The ``EnableLogTypes`` and ``DisableLogTypes`` arrays determine which logs are exported (or not exported) to CloudWatch Logs.
          - **EnableLogTypes** *(list) --*
            The list of log types to enable.
            - *(string) --*
          - **DisableLogTypes** *(list) --*
            The list of log types to disable.
            - *(string) --*
        :type EngineVersion: string
        :param EngineVersion:
          The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless the ``ApplyImmediately`` parameter is set to ``true`` .
        :rtype: dict
        :returns:
        """
        pass

    def modify_db_cluster_parameter_group(self, DBClusterParameterGroupName: str, Parameters: List) -> Dict:
        """
        Modifies the parameters of a DB cluster parameter group. To modify more than one parameter, submit a list of the following: ``ParameterName`` , ``ParameterValue`` , and ``ApplyMethod`` . A maximum of 20 parameters can be modified in a single request. 
        .. note::
          Changes to dynamic parameters are applied immediately. Changes to static parameters require a reboot or maintenance window before the change can take effect.
        .. warning::
          After you create a DB cluster parameter group, you should wait at least 5 minutes before creating your first DB cluster that uses that DB cluster parameter group as the default parameter group. This allows Amazon DocumentDB to fully complete the create action before the parameter group is used as the default for a new DB cluster. This step is especially important for parameters that are critical when creating the default database for a DB cluster, such as the character set for the default database defined by the ``character_set_database`` parameter.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/ModifyDBClusterParameterGroup>`_
        
        **Request Syntax**
        ::
          response = client.modify_db_cluster_parameter_group(
              DBClusterParameterGroupName='string',
              Parameters=[
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
          )
        
        **Response Syntax**
        ::
            {
                'DBClusterParameterGroupName': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the name of a DB cluster parameter group.
            - **DBClusterParameterGroupName** *(string) --* 
              The name of a DB cluster parameter group.
              Constraints:
              * Must be from 1 to 255 letters or numbers. 
              * The first character must be a letter. 
              * Cannot end with a hyphen or contain two consecutive hyphens. 
              .. note::
                This value is stored as a lowercase string.
        :type DBClusterParameterGroupName: string
        :param DBClusterParameterGroupName: **[REQUIRED]**
          The name of the DB cluster parameter group to modify.
        :type Parameters: list
        :param Parameters: **[REQUIRED]**
          A list of parameters in the DB cluster parameter group to modify.
          - *(dict) --*
            Detailed information about an individual parameter.
            - **ParameterName** *(string) --*
              Specifies the name of the parameter.
            - **ParameterValue** *(string) --*
              Specifies the value of the parameter.
            - **Description** *(string) --*
              Provides a description of the parameter.
            - **Source** *(string) --*
              Indicates the source of the parameter value.
            - **ApplyType** *(string) --*
              Specifies the engine-specific parameters type.
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
        :rtype: dict
        :returns:
        """
        pass

    def modify_db_cluster_snapshot_attribute(self, DBClusterSnapshotIdentifier: str, AttributeName: str, ValuesToAdd: List = None, ValuesToRemove: List = None) -> Dict:
        """
        Adds an attribute and values to, or removes an attribute and values from, a manual DB cluster snapshot.
        To share a manual DB cluster snapshot with other AWS accounts, specify ``restore`` as the ``AttributeName`` , and use the ``ValuesToAdd`` parameter to add a list of IDs of the AWS accounts that are authorized to restore the manual DB cluster snapshot. Use the value ``all`` to make the manual DB cluster snapshot public, which means that it can be copied or restored by all AWS accounts. Do not add the ``all`` value for any manual DB cluster snapshots that contain private information that you don't want available to all AWS accounts. If a manual DB cluster snapshot is encrypted, it can be shared, but only by specifying a list of authorized AWS account IDs for the ``ValuesToAdd`` parameter. You can't use ``all`` as a value for that parameter in this case.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/ModifyDBClusterSnapshotAttribute>`_
        
        **Request Syntax**
        ::
          response = client.modify_db_cluster_snapshot_attribute(
              DBClusterSnapshotIdentifier='string',
              AttributeName='string',
              ValuesToAdd=[
                  'string',
              ],
              ValuesToRemove=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'DBClusterSnapshotAttributesResult': {
                    'DBClusterSnapshotIdentifier': 'string',
                    'DBClusterSnapshotAttributes': [
                        {
                            'AttributeName': 'string',
                            'AttributeValues': [
                                'string',
                            ]
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBClusterSnapshotAttributesResult** *(dict) --* 
              Detailed information about the attributes that are associated with a DB cluster snapshot.
              - **DBClusterSnapshotIdentifier** *(string) --* 
                The identifier of the DB cluster snapshot that the attributes apply to.
              - **DBClusterSnapshotAttributes** *(list) --* 
                The list of attributes and values for the DB cluster snapshot.
                - *(dict) --* 
                  Contains the name and values of a manual DB cluster snapshot attribute.
                  Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore a manual DB cluster snapshot.
                  - **AttributeName** *(string) --* 
                    The name of the manual DB cluster snapshot attribute.
                    The attribute named ``restore`` refers to the list of AWS accounts that have permission to copy or restore the manual DB cluster snapshot.
                  - **AttributeValues** *(list) --* 
                    The values for the manual DB cluster snapshot attribute.
                    If the ``AttributeName`` field is set to ``restore`` , then this element returns a list of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is public and available for any AWS account to copy or restore.
                    - *(string) --* 
        :type DBClusterSnapshotIdentifier: string
        :param DBClusterSnapshotIdentifier: **[REQUIRED]**
          The identifier for the DB cluster snapshot to modify the attributes for.
        :type AttributeName: string
        :param AttributeName: **[REQUIRED]**
          The name of the DB cluster snapshot attribute to modify.
          To manage authorization for other AWS accounts to copy or restore a manual DB cluster snapshot, set this value to ``restore`` .
        :type ValuesToAdd: list
        :param ValuesToAdd:
          A list of DB cluster snapshot attributes to add to the attribute specified by ``AttributeName`` .
          To authorize other AWS accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more AWS account IDs. To make the manual DB cluster snapshot restorable by any AWS account, set it to ``all`` . Do not add the ``all`` value for any manual DB cluster snapshots that contain private information that you don\'t want to be available to all AWS accounts.
          - *(string) --*
        :type ValuesToRemove: list
        :param ValuesToRemove:
          A list of DB cluster snapshot attributes to remove from the attribute specified by ``AttributeName`` .
          To remove authorization for other AWS accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more AWS account identifiers. To remove authorization for any AWS account to copy or restore the DB cluster snapshot, set it to ``all`` . If you specify ``all`` , an AWS account whose account ID is explicitly added to the ``restore`` attribute can still copy or restore a manual DB cluster snapshot.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def modify_db_instance(self, DBInstanceIdentifier: str, DBInstanceClass: str = None, ApplyImmediately: bool = None, PreferredMaintenanceWindow: str = None, AutoMinorVersionUpgrade: bool = None, NewDBInstanceIdentifier: str = None, PromotionTier: int = None) -> Dict:
        """
        Modifies settings for a DB instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/ModifyDBInstance>`_
        
        **Request Syntax**
        ::
          response = client.modify_db_instance(
              DBInstanceIdentifier='string',
              DBInstanceClass='string',
              ApplyImmediately=True|False,
              PreferredMaintenanceWindow='string',
              AutoMinorVersionUpgrade=True|False,
              NewDBInstanceIdentifier='string',
              PromotionTier=123
          )
        
        **Response Syntax**
        ::
            {
                'DBInstance': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBInstance** *(dict) --* 
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
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: **[REQUIRED]**
          The DB instance identifier. This value is stored as a lowercase string.
          Constraints:
          * Must match the identifier of an existing ``DBInstance`` .
        :type DBInstanceClass: string
        :param DBInstanceClass:
          The new compute and memory capacity of the DB instance; for example, ``db.m4.large`` . Not all DB instance classes are available in all AWS Regions.
          If you modify the DB instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless ``ApplyImmediately`` is specified as ``true`` for this request.
          Default: Uses existing setting.
        :type ApplyImmediately: boolean
        :param ApplyImmediately:
          Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the ``PreferredMaintenanceWindow`` setting for the DB instance.
          If this parameter is set to ``false`` , changes to the DB instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next reboot.
          Default: ``false``
        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow:
          The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter doesn\'t result in an outage except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, changing this parameter causes a reboot of the DB instance. If you are moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure that pending changes are applied.
          Default: Uses existing setting.
          Format: ``ddd:hh24:mi-ddd:hh24:mi``
          Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
          Constraints: Must be at least 30 minutes.
        :type AutoMinorVersionUpgrade: boolean
        :param AutoMinorVersionUpgrade:
          Indicates that minor version upgrades are applied automatically to the DB instance during the maintenance window. Changing this parameter doesn\'t result in an outage except in the following case, and the change is asynchronously applied as soon as possible. An outage results if this parameter is set to ``true`` during the maintenance window, and a newer minor version is available, and Amazon DocumentDB has enabled automatic patching for that engine version.
        :type NewDBInstanceIdentifier: string
        :param NewDBInstanceIdentifier:
          The new DB instance identifier for the DB instance when renaming a DB instance. When you change the DB instance identifier, an instance reboot occurs immediately if you set ``Apply Immediately`` to ``true`` . It occurs during the next maintenance window if you set ``Apply Immediately`` to ``false`` . This value is stored as a lowercase string.
          Constraints:
          * Must contain from 1 to 63 letters, numbers, or hyphens.
          * The first character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
          Example: ``mydbinstance``
        :type PromotionTier: integer
        :param PromotionTier:
          A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.
          Default: 1
          Valid values: 0-15
        :rtype: dict
        :returns:
        """
        pass

    def modify_db_subnet_group(self, DBSubnetGroupName: str, SubnetIds: List, DBSubnetGroupDescription: str = None) -> Dict:
        """
        Modifies an existing DB subnet group. DB subnet groups must contain at least one subnet in at least two Availability Zones in the AWS Region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/ModifyDBSubnetGroup>`_
        
        **Request Syntax**
        ::
          response = client.modify_db_subnet_group(
              DBSubnetGroupName='string',
              DBSubnetGroupDescription='string',
              SubnetIds=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBSubnetGroup** *(dict) --* 
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
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName: **[REQUIRED]**
          The name for the DB subnet group. This value is stored as a lowercase string. You can\'t modify the default subnet group.
          Constraints: Must match the name of an existing ``DBSubnetGroup`` . Must not be default.
          Example: ``mySubnetgroup``
        :type DBSubnetGroupDescription: string
        :param DBSubnetGroupDescription:
          The description for the DB subnet group.
        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]**
          The Amazon EC2 subnet IDs for the DB subnet group.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def reboot_db_instance(self, DBInstanceIdentifier: str, ForceFailover: bool = None) -> Dict:
        """
        You might need to reboot your DB instance, usually for maintenance reasons. For example, if you make certain changes, or if you change the DB cluster parameter group that is associated with the DB instance, you must reboot the instance for the changes to take effect. 
        Rebooting a DB instance restarts the database engine service. Rebooting a DB instance results in a momentary outage, during which the DB instance status is set to *rebooting* . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/RebootDBInstance>`_
        
        **Request Syntax**
        ::
          response = client.reboot_db_instance(
              DBInstanceIdentifier='string',
              ForceFailover=True|False
          )
        
        **Response Syntax**
        ::
            {
                'DBInstance': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBInstance** *(dict) --* 
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
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: **[REQUIRED]**
          The DB instance identifier. This parameter is stored as a lowercase string.
          Constraints:
          * Must match the identifier of an existing ``DBInstance`` .
        :type ForceFailover: boolean
        :param ForceFailover:
          When ``true`` , the reboot is conducted through a Multi-AZ failover.
          Constraint: You can\'t specify ``true`` if the instance is not configured for Multi-AZ.
        :rtype: dict
        :returns:
        """
        pass

    def remove_tags_from_resource(self, ResourceName: str, TagKeys: List):
        """
        Removes metadata tags from an Amazon DocumentDB resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/RemoveTagsFromResource>`_
        
        **Request Syntax**
        ::
          response = client.remove_tags_from_resource(
              ResourceName='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceName: string
        :param ResourceName: **[REQUIRED]**
          The Amazon DocumentDB resource that the tags are removed from. This value is an Amazon Resource Name (ARN).
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**
          The tag key (name) of the tag to be removed.
          - *(string) --*
        :returns: None
        """
        pass

    def reset_db_cluster_parameter_group(self, DBClusterParameterGroupName: str, ResetAllParameters: bool = None, Parameters: List = None) -> Dict:
        """
        Modifies the parameters of a DB cluster parameter group to the default value. To reset specific parameters, submit a list of the following: ``ParameterName`` and ``ApplyMethod`` . To reset the entire DB cluster parameter group, specify the ``DBClusterParameterGroupName`` and ``ResetAllParameters`` parameters. 
        When you reset the entire group, dynamic parameters are updated immediately and static parameters are set to ``pending-reboot`` to take effect on the next DB instance reboot.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/ResetDBClusterParameterGroup>`_
        
        **Request Syntax**
        ::
          response = client.reset_db_cluster_parameter_group(
              DBClusterParameterGroupName='string',
              ResetAllParameters=True|False,
              Parameters=[
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
          )
        
        **Response Syntax**
        ::
            {
                'DBClusterParameterGroupName': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the name of a DB cluster parameter group.
            - **DBClusterParameterGroupName** *(string) --* 
              The name of a DB cluster parameter group.
              Constraints:
              * Must be from 1 to 255 letters or numbers. 
              * The first character must be a letter. 
              * Cannot end with a hyphen or contain two consecutive hyphens. 
              .. note::
                This value is stored as a lowercase string.
        :type DBClusterParameterGroupName: string
        :param DBClusterParameterGroupName: **[REQUIRED]**
          The name of the DB cluster parameter group to reset.
        :type ResetAllParameters: boolean
        :param ResetAllParameters:
          A value that is set to ``true`` to reset all parameters in the DB cluster parameter group to their default values, and ``false`` otherwise. You can\'t use this parameter if there is a list of parameter names specified for the ``Parameters`` parameter.
        :type Parameters: list
        :param Parameters:
          A list of parameter names in the DB cluster parameter group to reset to the default values. You can\'t use this parameter if the ``ResetAllParameters`` parameter is set to ``true`` .
          - *(dict) --*
            Detailed information about an individual parameter.
            - **ParameterName** *(string) --*
              Specifies the name of the parameter.
            - **ParameterValue** *(string) --*
              Specifies the value of the parameter.
            - **Description** *(string) --*
              Provides a description of the parameter.
            - **Source** *(string) --*
              Indicates the source of the parameter value.
            - **ApplyType** *(string) --*
              Specifies the engine-specific parameters type.
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
        :rtype: dict
        :returns:
        """
        pass

    def restore_db_cluster_from_snapshot(self, DBClusterIdentifier: str, SnapshotIdentifier: str, Engine: str, AvailabilityZones: List = None, EngineVersion: str = None, Port: int = None, DBSubnetGroupName: str = None, VpcSecurityGroupIds: List = None, Tags: List = None, KmsKeyId: str = None, EnableCloudwatchLogsExports: List = None) -> Dict:
        """
        Creates a new DB cluster from a DB snapshot or DB cluster snapshot.
        If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.
        If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/RestoreDBClusterFromSnapshot>`_
        
        **Request Syntax**
        ::
          response = client.restore_db_cluster_from_snapshot(
              AvailabilityZones=[
                  'string',
              ],
              DBClusterIdentifier='string',
              SnapshotIdentifier='string',
              Engine='string',
              EngineVersion='string',
              Port=123,
              DBSubnetGroupName='string',
              VpcSecurityGroupIds=[
                  'string',
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              KmsKeyId='string',
              EnableCloudwatchLogsExports=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'DBCluster': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBCluster** *(dict) --* 
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
        :type AvailabilityZones: list
        :param AvailabilityZones:
          Provides the list of Amazon EC2 Availability Zones that instances in the restored DB cluster can be created in.
          - *(string) --*
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]**
          The name of the DB cluster to create from the DB snapshot or DB cluster snapshot. This parameter isn\'t case sensitive.
          Constraints:
          * Must contain from 1 to 63 letters, numbers, or hyphens.
          * The first character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
          Example: ``my-snapshot-id``
        :type SnapshotIdentifier: string
        :param SnapshotIdentifier: **[REQUIRED]**
          The identifier for the DB snapshot or DB cluster snapshot to restore from.
          You can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.
          Constraints:
          * Must match the identifier of an existing snapshot.
        :type Engine: string
        :param Engine: **[REQUIRED]**
          The database engine to use for the new DB cluster.
          Default: The same as source.
          Constraint: Must be compatible with the engine of the source.
        :type EngineVersion: string
        :param EngineVersion:
          The version of the database engine to use for the new DB cluster.
        :type Port: integer
        :param Port:
          The port number on which the new DB cluster accepts connections.
          Constraints: Must be a value from ``1150`` to ``65535`` .
          Default: The same port as the original DB cluster.
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName:
          The name of the DB subnet group to use for the new DB cluster.
          Constraints: If provided, must match the name of an existing ``DBSubnetGroup`` .
          Example: ``mySubnetgroup``
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds:
          A list of virtual private cloud (VPC) security groups that the new DB cluster will belong to.
          - *(string) --*
        :type Tags: list
        :param Tags:
          The tags to be assigned to the restored DB cluster.
          - *(dict) --*
            Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
            - **Key** *(string) --*
              The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
            - **Value** *(string) --*
              The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        :type KmsKeyId: string
        :param KmsKeyId:
          The AWS KMS key identifier to use when restoring an encrypted DB cluster from a DB snapshot or DB cluster snapshot.
          The AWS KMS key identifier is the Amazon Resource Name (ARN) for the AWS KMS encryption key. If you are restoring a DB cluster with the same AWS account that owns the AWS KMS encryption key used to encrypt the new DB cluster, then you can use the AWS KMS key alias instead of the ARN for the AWS KMS encryption key.
          If you do not specify a value for the ``KmsKeyId`` parameter, then the following occurs:
          * If the DB snapshot or DB cluster snapshot in ``SnapshotIdentifier`` is encrypted, then the restored DB cluster is encrypted using the AWS KMS key that was used to encrypt the DB snapshot or the DB cluster snapshot.
          * If the DB snapshot or the DB cluster snapshot in ``SnapshotIdentifier`` is not encrypted, then the restored DB cluster is not encrypted.
        :type EnableCloudwatchLogsExports: list
        :param EnableCloudwatchLogsExports:
          A list of log types that must be enabled for exporting to Amazon CloudWatch Logs.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def restore_db_cluster_to_point_in_time(self, DBClusterIdentifier: str, SourceDBClusterIdentifier: str, RestoreToTime: datetime = None, UseLatestRestorableTime: bool = None, Port: int = None, DBSubnetGroupName: str = None, VpcSecurityGroupIds: List = None, Tags: List = None, KmsKeyId: str = None, EnableCloudwatchLogsExports: List = None) -> Dict:
        """
        Restores a DB cluster to an arbitrary point in time. Users can restore to any point in time before ``LatestRestorableTime`` for up to ``BackupRetentionPeriod`` days. The target DB cluster is created from the source DB cluster with the same configuration as the original DB cluster, except that the new DB cluster is created with the default DB security group. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-2014-10-31/RestoreDBClusterToPointInTime>`_
        
        **Request Syntax**
        ::
          response = client.restore_db_cluster_to_point_in_time(
              DBClusterIdentifier='string',
              SourceDBClusterIdentifier='string',
              RestoreToTime=datetime(2015, 1, 1),
              UseLatestRestorableTime=True|False,
              Port=123,
              DBSubnetGroupName='string',
              VpcSecurityGroupIds=[
                  'string',
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              KmsKeyId='string',
              EnableCloudwatchLogsExports=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'DBCluster': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DBCluster** *(dict) --* 
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
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]**
          The name of the new DB cluster to be created.
          Constraints:
          * Must contain from 1 to 63 letters, numbers, or hyphens.
          * The first character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
        :type SourceDBClusterIdentifier: string
        :param SourceDBClusterIdentifier: **[REQUIRED]**
          The identifier of the source DB cluster from which to restore.
          Constraints:
          * Must match the identifier of an existing ``DBCluster`` .
        :type RestoreToTime: datetime
        :param RestoreToTime:
          The date and time to restore the DB cluster to.
          Valid values: A time in Universal Coordinated Time (UTC) format.
          Constraints:
          * Must be before the latest restorable time for the DB instance.
          * Must be specified if the ``UseLatestRestorableTime`` parameter is not provided.
          * Cannot be specified if the ``UseLatestRestorableTime`` parameter is ``true`` .
          * Cannot be specified if the ``RestoreType`` parameter is ``copy-on-write`` .
          Example: ``2015-03-07T23:45:00Z``
        :type UseLatestRestorableTime: boolean
        :param UseLatestRestorableTime:
          A value that is set to ``true`` to restore the DB cluster to the latest restorable backup time, and ``false`` otherwise.
          Default: ``false``
          Constraints: Cannot be specified if the ``RestoreToTime`` parameter is provided.
        :type Port: integer
        :param Port:
          The port number on which the new DB cluster accepts connections.
          Constraints: Must be a value from ``1150`` to ``65535`` .
          Default: The default port for the engine.
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName:
          The DB subnet group name to use for the new DB cluster.
          Constraints: If provided, must match the name of an existing ``DBSubnetGroup`` .
          Example: ``mySubnetgroup``
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds:
          A list of VPC security groups that the new DB cluster belongs to.
          - *(string) --*
        :type Tags: list
        :param Tags:
          The tags to be assigned to the restored DB cluster.
          - *(dict) --*
            Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
            - **Key** *(string) --*
              The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
            - **Value** *(string) --*
              The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        :type KmsKeyId: string
        :param KmsKeyId:
          The AWS KMS key identifier to use when restoring an encrypted DB cluster from an encrypted DB cluster.
          The AWS KMS key identifier is the Amazon Resource Name (ARN) for the AWS KMS encryption key. If you are restoring a DB cluster with the same AWS account that owns the AWS KMS encryption key used to encrypt the new DB cluster, then you can use the AWS KMS key alias instead of the ARN for the AWS KMS encryption key.
          You can restore to a new DB cluster and encrypt the new DB cluster with an AWS KMS key that is different from the AWS KMS key used to encrypt the source DB cluster. The new DB cluster is encrypted with the AWS KMS key identified by the ``KmsKeyId`` parameter.
          If you do not specify a value for the ``KmsKeyId`` parameter, then the following occurs:
          * If the DB cluster is encrypted, then the restored DB cluster is encrypted using the AWS KMS key that was used to encrypt the source DB cluster.
          * If the DB cluster is not encrypted, then the restored DB cluster is not encrypted.
          If ``DBClusterIdentifier`` refers to a DB cluster that is not encrypted, then the restore request is rejected.
        :type EnableCloudwatchLogsExports: list
        :param EnableCloudwatchLogsExports:
          A list of log types that must be enabled for exporting to Amazon CloudWatch Logs.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass
