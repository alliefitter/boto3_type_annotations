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
    def add_role_to_db_cluster(self, DBClusterIdentifier: str, RoleArn: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/AddRoleToDBCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_role_to_db_cluster(
              DBClusterIdentifier=\'string\',
              RoleArn=\'string\'
          )
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]** 
        
          The name of the DB cluster to associate the IAM role with.
        
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the IAM role to associate with the Neptune DB cluster, for example ``arn:aws:iam::123456789012:role/NeptuneAccessRole`` .
        
        :returns: None
        """
        pass

    def add_source_identifier_to_subscription(self, SubscriptionName: str, SourceIdentifier: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/AddSourceIdentifierToSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_source_identifier_to_subscription(
              SubscriptionName=\'string\',
              SourceIdentifier=\'string\'
          )
        :type SubscriptionName: string
        :param SubscriptionName: **[REQUIRED]** 
        
          The name of the event notification subscription you want to add a source identifier to.
        
        :type SourceIdentifier: string
        :param SourceIdentifier: **[REQUIRED]** 
        
          The identifier of the event source to be added.
        
          Constraints:
        
          * If the source type is a DB instance, then a ``DBInstanceIdentifier`` must be supplied. 
           
          * If the source type is a DB security group, a ``DBSecurityGroupName`` must be supplied. 
           
          * If the source type is a DB parameter group, a ``DBParameterGroupName`` must be supplied. 
           
          * If the source type is a DB snapshot, a ``DBSnapshotIdentifier`` must be supplied. 
           
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EventSubscription\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EventSubscription** *(dict) --* 
        
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
        
        """
        pass

    def add_tags_to_resource(self, ResourceName: str, Tags: List) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/AddTagsToResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_tags_to_resource(
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
        
          The Amazon Neptune resource that the tags are added to. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see `Constructing an Amazon Resource Name (ARN) <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing>`__ .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          The tags to be assigned to the Amazon Neptune resource.
        
          - *(dict) --* 
        
            Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :returns: None
        """
        pass

    def apply_pending_maintenance_action(self, ResourceIdentifier: str, ApplyAction: str, OptInType: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/ApplyPendingMaintenanceAction>`_
        
        **Request Syntax** 
        ::
        
          response = client.apply_pending_maintenance_action(
              ResourceIdentifier=\'string\',
              ApplyAction=\'string\',
              OptInType=\'string\'
          )
        :type ResourceIdentifier: string
        :param ResourceIdentifier: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to. For information about creating an ARN, see `Constructing an Amazon Resource Name (ARN) <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing>`__ .
        
        :type ApplyAction: string
        :param ApplyAction: **[REQUIRED]** 
        
          The pending maintenance action to apply to this resource.
        
          Valid values: ``system-update`` , ``db-upgrade``  
        
        :type OptInType: string
        :param OptInType: **[REQUIRED]** 
        
          A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type ``immediate`` can\'t be undone.
        
          Valid values:
        
          * ``immediate`` - Apply the maintenance action immediately. 
           
          * ``next-maintenance`` - Apply the maintenance action during the next maintenance window for the resource. 
           
          * ``undo-opt-in`` - Cancel any existing ``next-maintenance`` opt-in requests. 
           
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ResourcePendingMaintenanceActions\': {
                    \'ResourceIdentifier\': \'string\',
                    \'PendingMaintenanceActionDetails\': [
                        {
                            \'Action\': \'string\',
                            \'AutoAppliedAfterDate\': datetime(2015, 1, 1),
                            \'ForcedApplyDate\': datetime(2015, 1, 1),
                            \'OptInStatus\': \'string\',
                            \'CurrentApplyDate\': datetime(2015, 1, 1),
                            \'Description\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ResourcePendingMaintenanceActions** *(dict) --* 
        
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
        
        """
        pass

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

    def copy_db_cluster_parameter_group(self, SourceDBClusterParameterGroupIdentifier: str, TargetDBClusterParameterGroupIdentifier: str, TargetDBClusterParameterGroupDescription: str, Tags: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/CopyDBClusterParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.copy_db_cluster_parameter_group(
              SourceDBClusterParameterGroupIdentifier=\'string\',
              TargetDBClusterParameterGroupIdentifier=\'string\',
              TargetDBClusterParameterGroupDescription=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type SourceDBClusterParameterGroupIdentifier: string
        :param SourceDBClusterParameterGroupIdentifier: **[REQUIRED]** 
        
          The identifier or Amazon Resource Name (ARN) for the source DB cluster parameter group. For information about creating an ARN, see `Constructing an Amazon Resource Name (ARN) <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing>`__ . 
        
          Constraints:
        
          * Must specify a valid DB cluster parameter group. 
           
          * If the source DB cluster parameter group is in the same AWS Region as the copy, specify a valid DB parameter group identifier, for example ``my-db-cluster-param-group`` , or a valid ARN. 
           
          * If the source DB parameter group is in a different AWS Region than the copy, specify a valid DB cluster parameter group ARN, for example ``arn:aws:rds:us-east-1:123456789012:cluster-pg:custom-cluster-group1`` . 
           
        :type TargetDBClusterParameterGroupIdentifier: string
        :param TargetDBClusterParameterGroupIdentifier: **[REQUIRED]** 
        
          The identifier for the copied DB cluster parameter group.
        
          Constraints:
        
          * Cannot be null, empty, or blank 
           
          * Must contain from 1 to 255 letters, numbers, or hyphens 
           
          * First character must be a letter 
           
          * Cannot end with a hyphen or contain two consecutive hyphens 
           
          Example: ``my-cluster-param-group1``  
        
        :type TargetDBClusterParameterGroupDescription: string
        :param TargetDBClusterParameterGroupDescription: **[REQUIRED]** 
        
          A description for the copied DB cluster parameter group.
        
        :type Tags: list
        :param Tags: 
        
          A list of tags. For more information, see `Tagging Amazon Neptune Resources <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html>`__ . 
        
          - *(dict) --* 
        
            Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBClusterParameterGroup\': {
                    \'DBClusterParameterGroupName\': \'string\',
                    \'DBParameterGroupFamily\': \'string\',
                    \'Description\': \'string\',
                    \'DBClusterParameterGroupArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBClusterParameterGroup** *(dict) --* 
        
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
        
        """
        pass

    def copy_db_cluster_snapshot(self, SourceDBClusterSnapshotIdentifier: str, TargetDBClusterSnapshotIdentifier: str, KmsKeyId: str = None, PreSignedUrl: str = None, CopyTags: bool = None, Tags: List = None, SourceRegion: str = None) -> Dict:
        """
        
        To copy a DB cluster snapshot from a shared manual DB cluster snapshot, ``SourceDBClusterSnapshotIdentifier`` must be the Amazon Resource Name (ARN) of the shared DB cluster snapshot.
        
        You can copy an encrypted DB cluster snapshot from another AWS Region. In that case, the AWS Region where you call the ``CopyDBClusterSnapshot`` action is the destination AWS Region for the encrypted DB cluster snapshot to be copied to. To copy an encrypted DB cluster snapshot from another AWS Region, you must provide the following values:
        
        * ``KmsKeyId`` - The AWS Key Management System (AWS KMS) key identifier for the key to use to encrypt the copy of the DB cluster snapshot in the destination AWS Region. 
         
        * ``PreSignedUrl`` - A URL that contains a Signature Version 4 signed request for the ``CopyDBClusterSnapshot`` action to be called in the source AWS Region where the DB cluster snapshot is copied from. The pre-signed URL must be a valid request for the ``CopyDBClusterSnapshot`` API action that can be executed in the source AWS Region that contains the encrypted DB cluster snapshot to be copied. The pre-signed URL request must contain the following parameter values: 
        
          * ``KmsKeyId`` - The KMS key identifier for the key to use to encrypt the copy of the DB cluster snapshot in the destination AWS Region. This is the same identifier for both the ``CopyDBClusterSnapshot`` action that is called in the destination AWS Region, and the action contained in the pre-signed URL. 
           
          * ``DestinationRegion`` - The name of the AWS Region that the DB cluster snapshot will be created in. 
           
          * ``SourceDBClusterSnapshotIdentifier`` - The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB cluster snapshot from the us-west-2 AWS Region, then your ``SourceDBClusterSnapshotIdentifier`` looks like the following example: ``arn:aws:rds:us-west-2:123456789012:cluster-snapshot:neptune-cluster1-snapshot-20161115`` . 
           
        To learn how to generate a Signature Version 4 signed request, see `Authenticating Requests\: Using Query Parameters (AWS Signature Version 4) <http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html>`__ and `Signature Version 4 Signing Process <http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>`__ .
        
        * ``TargetDBClusterSnapshotIdentifier`` - The identifier for the new copy of the DB cluster snapshot in the destination AWS Region. 
         
        * ``SourceDBClusterSnapshotIdentifier`` - The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the ARN format for the source AWS Region and is the same value as the ``SourceDBClusterSnapshotIdentifier`` in the pre-signed URL.  
         
        To cancel the copy operation once it is in progress, delete the target DB cluster snapshot identified by ``TargetDBClusterSnapshotIdentifier`` while that DB cluster snapshot is in \"copying\" status.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/CopyDBClusterSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.copy_db_cluster_snapshot(
              SourceDBClusterSnapshotIdentifier=\'string\',
              TargetDBClusterSnapshotIdentifier=\'string\',
              KmsKeyId=\'string\',
              CopyTags=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              SourceRegion=\'string\'
          )
        :type SourceDBClusterSnapshotIdentifier: string
        :param SourceDBClusterSnapshotIdentifier: **[REQUIRED]** 
        
          The identifier of the DB cluster snapshot to copy. This parameter is not case-sensitive.
        
          You can\'t copy an encrypted, shared DB cluster snapshot from one AWS Region to another.
        
          Constraints:
        
          * Must specify a valid system snapshot in the \"available\" state. 
           
          * If the source snapshot is in the same AWS Region as the copy, specify a valid DB snapshot identifier. 
           
          * If the source snapshot is in a different AWS Region than the copy, specify a valid DB cluster snapshot ARN.  
           
          Example: ``my-cluster-snapshot1``  
        
        :type TargetDBClusterSnapshotIdentifier: string
        :param TargetDBClusterSnapshotIdentifier: **[REQUIRED]** 
        
          The identifier of the new DB cluster snapshot to create from the source DB cluster snapshot. This parameter is not case-sensitive.
        
          Constraints:
        
          * Must contain from 1 to 63 letters, numbers, or hyphens. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
          Example: ``my-cluster-snapshot2``  
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          The AWS AWS KMS key ID for an encrypted DB cluster snapshot. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key. 
        
          If you copy an unencrypted DB cluster snapshot and specify a value for the ``KmsKeyId`` parameter, Amazon Neptune encrypts the target DB cluster snapshot using the specified KMS encryption key. 
        
          If you copy an encrypted DB cluster snapshot from your AWS account, you can specify a value for ``KmsKeyId`` to encrypt the copy with a new KMS encryption key. If you don\'t specify a value for ``KmsKeyId`` , then the copy of the DB cluster snapshot is encrypted with the same KMS key as the source DB cluster snapshot. 
        
          If you copy an encrypted DB cluster snapshot that is shared from another AWS account, then you must specify a value for ``KmsKeyId`` . 
        
          To copy an encrypted DB cluster snapshot to another AWS Region, you must set ``KmsKeyId`` to the KMS key ID you want to use to encrypt the copy of the DB cluster snapshot in the destination AWS Region. KMS encryption keys are specific to the AWS Region that they are created in, and you can\'t use encryption keys from one AWS Region in another AWS Region.
        
        :type PreSignedUrl: string
        :param PreSignedUrl: 
        
          The URL that contains a Signature Version 4 signed request for the ``CopyDBClusterSnapshot`` API action in the AWS Region that contains the source DB cluster snapshot to copy. The ``PreSignedUrl`` parameter must be used when copying an encrypted DB cluster snapshot from another AWS Region.
        
          The pre-signed URL must be a valid request for the ``CopyDBSClusterSnapshot`` API action that can be executed in the source AWS Region that contains the encrypted DB cluster snapshot to be copied. The pre-signed URL request must contain the following parameter values:
        
          * ``KmsKeyId`` - The AWS KMS key identifier for the key to use to encrypt the copy of the DB cluster snapshot in the destination AWS Region. This is the same identifier for both the ``CopyDBClusterSnapshot`` action that is called in the destination AWS Region, and the action contained in the pre-signed URL. 
           
          * ``DestinationRegion`` - The name of the AWS Region that the DB cluster snapshot will be created in. 
           
          * ``SourceDBClusterSnapshotIdentifier`` - The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB cluster snapshot from the us-west-2 AWS Region, then your ``SourceDBClusterSnapshotIdentifier`` looks like the following example: ``arn:aws:rds:us-west-2:123456789012:cluster-snapshot:neptune-cluster1-snapshot-20161115`` . 
           
          To learn how to generate a Signature Version 4 signed request, see `Authenticating Requests\: Using Query Parameters (AWS Signature Version 4) <http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html>`__ and `Signature Version 4 Signing Process <http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>`__ .
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type CopyTags: boolean
        :param CopyTags: 
        
          True to copy all tags from the source DB cluster snapshot to the target DB cluster snapshot, and otherwise false. The default is false.
        
        :type Tags: list
        :param Tags: 
        
          A list of tags. For more information, see `Tagging Amazon Neptune Resources <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html>`__ . 
        
          - *(dict) --* 
        
            Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :type SourceRegion: string
        :param SourceRegion: 
        
          The ID of the region that contains the snapshot to be copied.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBClusterSnapshot\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBClusterSnapshot** *(dict) --* 
        
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
        
        """
        pass

    def copy_db_parameter_group(self, SourceDBParameterGroupIdentifier: str, TargetDBParameterGroupIdentifier: str, TargetDBParameterGroupDescription: str, Tags: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/CopyDBParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.copy_db_parameter_group(
              SourceDBParameterGroupIdentifier=\'string\',
              TargetDBParameterGroupIdentifier=\'string\',
              TargetDBParameterGroupDescription=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type SourceDBParameterGroupIdentifier: string
        :param SourceDBParameterGroupIdentifier: **[REQUIRED]** 
        
          The identifier or ARN for the source DB parameter group. For information about creating an ARN, see `Constructing an Amazon Resource Name (ARN) <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing>`__ . 
        
          Constraints:
        
          * Must specify a valid DB parameter group. 
           
          * Must specify a valid DB parameter group identifier, for example ``my-db-param-group`` , or a valid ARN. 
           
        :type TargetDBParameterGroupIdentifier: string
        :param TargetDBParameterGroupIdentifier: **[REQUIRED]** 
        
          The identifier for the copied DB parameter group.
        
          Constraints:
        
          * Cannot be null, empty, or blank 
           
          * Must contain from 1 to 255 letters, numbers, or hyphens 
           
          * First character must be a letter 
           
          * Cannot end with a hyphen or contain two consecutive hyphens 
           
          Example: ``my-db-parameter-group``  
        
        :type TargetDBParameterGroupDescription: string
        :param TargetDBParameterGroupDescription: **[REQUIRED]** 
        
          A description for the copied DB parameter group.
        
        :type Tags: list
        :param Tags: 
        
          A list of tags. For more information, see `Tagging Amazon Neptune Resources <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html>`__ . 
        
          - *(dict) --* 
        
            Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBParameterGroup\': {
                    \'DBParameterGroupName\': \'string\',
                    \'DBParameterGroupFamily\': \'string\',
                    \'Description\': \'string\',
                    \'DBParameterGroupArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBParameterGroup** *(dict) --* 
        
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
        
        """
        pass

    def create_db_cluster(self, DBClusterIdentifier: str, Engine: str, AvailabilityZones: List = None, BackupRetentionPeriod: int = None, CharacterSetName: str = None, DatabaseName: str = None, DBClusterParameterGroupName: str = None, VpcSecurityGroupIds: List = None, DBSubnetGroupName: str = None, EngineVersion: str = None, Port: int = None, MasterUsername: str = None, MasterUserPassword: str = None, OptionGroupName: str = None, PreferredBackupWindow: str = None, PreferredMaintenanceWindow: str = None, ReplicationSourceIdentifier: str = None, Tags: List = None, StorageEncrypted: bool = None, KmsKeyId: str = None, PreSignedUrl: str = None, EnableIAMDatabaseAuthentication: bool = None, SourceRegion: str = None) -> Dict:
        """
        
        You can use the ``ReplicationSourceIdentifier`` parameter to create the DB cluster as a Read Replica of another DB cluster or Amazon Neptune DB instance. For cross-region replication where the DB cluster identified by ``ReplicationSourceIdentifier`` is encrypted, you must also specify the ``PreSignedUrl`` parameter.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/CreateDBCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_db_cluster(
              AvailabilityZones=[
                  \'string\',
              ],
              BackupRetentionPeriod=123,
              CharacterSetName=\'string\',
              DatabaseName=\'string\',
              DBClusterIdentifier=\'string\',
              DBClusterParameterGroupName=\'string\',
              VpcSecurityGroupIds=[
                  \'string\',
              ],
              DBSubnetGroupName=\'string\',
              Engine=\'string\',
              EngineVersion=\'string\',
              Port=123,
              MasterUsername=\'string\',
              MasterUserPassword=\'string\',
              OptionGroupName=\'string\',
              PreferredBackupWindow=\'string\',
              PreferredMaintenanceWindow=\'string\',
              ReplicationSourceIdentifier=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              StorageEncrypted=True|False,
              KmsKeyId=\'string\',
              EnableIAMDatabaseAuthentication=True|False,
              SourceRegion=\'string\'
          )
        :type AvailabilityZones: list
        :param AvailabilityZones: 
        
          A list of EC2 Availability Zones that instances in the DB cluster can be created in. 
        
          - *(string) --* 
        
        :type BackupRetentionPeriod: integer
        :param BackupRetentionPeriod: 
        
          The number of days for which automated backups are retained. You must specify a minimum value of 1.
        
          Default: 1
        
          Constraints:
        
          * Must be a value from 1 to 35 
           
        :type CharacterSetName: string
        :param CharacterSetName: 
        
          A value that indicates that the DB cluster should be associated with the specified CharacterSet.
        
        :type DatabaseName: string
        :param DatabaseName: 
        
          The name for your database of up to 64 alpha-numeric characters. If you do not provide a name, Amazon Neptune will not create a database in the DB cluster you are creating.
        
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]** 
        
          The DB cluster identifier. This parameter is stored as a lowercase string.
        
          Constraints:
        
          * Must contain from 1 to 63 letters, numbers, or hyphens. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
          Example: ``my-cluster1``  
        
        :type DBClusterParameterGroupName: string
        :param DBClusterParameterGroupName: 
        
          The name of the DB cluster parameter group to associate with this DB cluster. If this argument is omitted, the default is used. 
        
          Constraints:
        
          * If supplied, must match the name of an existing DBClusterParameterGroup. 
           
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds: 
        
          A list of EC2 VPC security groups to associate with this DB cluster.
        
          - *(string) --* 
        
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName: 
        
          A DB subnet group to associate with this DB cluster.
        
          Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.
        
          Example: ``mySubnetgroup``  
        
        :type Engine: string
        :param Engine: **[REQUIRED]** 
        
          The name of the database engine to be used for this DB cluster.
        
          Valid Values: ``neptune``  
        
        :type EngineVersion: string
        :param EngineVersion: 
        
          The version number of the database engine to use.
        
          Example: ``1.0.1``  
        
        :type Port: integer
        :param Port: 
        
          The port number on which the instances in the DB cluster accept connections.
        
          Default: ``8182``  
        
        :type MasterUsername: string
        :param MasterUsername: 
        
          The name of the master user for the DB cluster.
        
          Constraints:
        
          * Must be 1 to 16 letters or numbers. 
           
          * First character must be a letter. 
           
          * Cannot be a reserved word for the chosen database engine. 
           
        :type MasterUserPassword: string
        :param MasterUserPassword: 
        
          The password for the master database user. This password can contain any printable ASCII character except \"/\", \"\"\", or \"@\".
        
          Constraints: Must contain from 8 to 41 characters.
        
        :type OptionGroupName: string
        :param OptionGroupName: 
        
          A value that indicates that the DB cluster should be associated with the specified option group.
        
          Permanent options can\'t be removed from an option group. The option group can\'t be removed from a DB cluster once it is associated with a DB cluster.
        
        :type PreferredBackupWindow: string
        :param PreferredBackupWindow: 
        
          The daily time range during which automated backups are created if automated backups are enabled using the ``BackupRetentionPeriod`` parameter. 
        
          The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see `Adjusting the Preferred Maintenance Window <http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AdjustingTheMaintenanceWindow.html>`__ in the *Amazon Neptune User Guide.*  
        
          Constraints:
        
          * Must be in the format ``hh24:mi-hh24:mi`` . 
           
          * Must be in Universal Coordinated Time (UTC). 
           
          * Must not conflict with the preferred maintenance window. 
           
          * Must be at least 30 minutes. 
           
        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow: 
        
          The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
        
          Format: ``ddd:hh24:mi-ddd:hh24:mi``  
        
          The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see `Adjusting the Preferred Maintenance Window <http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AdjustingTheMaintenanceWindow.html>`__ in the *Amazon Neptune User Guide.*  
        
          Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
        
          Constraints: Minimum 30-minute window.
        
        :type ReplicationSourceIdentifier: string
        :param ReplicationSourceIdentifier: 
        
          The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.
        
        :type Tags: list
        :param Tags: 
        
          A list of tags. For more information, see `Tagging Amazon Neptune Resources <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html>`__ . 
        
          - *(dict) --* 
        
            Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :type StorageEncrypted: boolean
        :param StorageEncrypted: 
        
          Specifies whether the DB cluster is encrypted.
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          The AWS KMS key identifier for an encrypted DB cluster.
        
          The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB cluster with the same AWS account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.
        
          If an encryption key is not specified in ``KmsKeyId`` :
        
          * If ``ReplicationSourceIdentifier`` identifies an encrypted source, then Amazon Neptune will use the encryption key used to encrypt the source. Otherwise, Amazon Neptune will use your default encryption key.  
           
          * If the ``StorageEncrypted`` parameter is true and ``ReplicationSourceIdentifier`` is not specified, then Amazon Neptune will use your default encryption key. 
           
          AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
        
          If you create a Read Replica of an encrypted DB cluster in another AWS Region, you must set ``KmsKeyId`` to a KMS key ID that is valid in the destination AWS Region. This key is used to encrypt the Read Replica in that AWS Region.
        
        :type PreSignedUrl: string
        :param PreSignedUrl: 
        
          A URL that contains a Signature Version 4 signed request for the ``CreateDBCluster`` action to be called in the source AWS Region where the DB cluster is replicated from. You only need to specify ``PreSignedUrl`` when you are performing cross-region replication from an encrypted DB cluster.
        
          The pre-signed URL must be a valid request for the ``CreateDBCluster`` API action that can be executed in the source AWS Region that contains the encrypted DB cluster to be copied.
        
          The pre-signed URL request must contain the following parameter values:
        
          * ``KmsKeyId`` - The AWS KMS key identifier for the key to use to encrypt the copy of the DB cluster in the destination AWS Region. This should refer to the same KMS key for both the ``CreateDBCluster`` action that is called in the destination AWS Region, and the action contained in the pre-signed URL. 
           
          * ``DestinationRegion`` - The name of the AWS Region that Read Replica will be created in. 
           
          * ``ReplicationSourceIdentifier`` - The DB cluster identifier for the encrypted DB cluster to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB cluster from the us-west-2 AWS Region, then your ``ReplicationSourceIdentifier`` would look like Example: ``arn:aws:rds:us-west-2:123456789012:cluster:neptune-cluster1`` . 
           
          To learn how to generate a Signature Version 4 signed request, see `Authenticating Requests\: Using Query Parameters (AWS Signature Version 4) <http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html>`__ and `Signature Version 4 Signing Process <http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>`__ .
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type EnableIAMDatabaseAuthentication: boolean
        :param EnableIAMDatabaseAuthentication: 
        
          True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.
        
          Default: ``false``  
        
        :type SourceRegion: string
        :param SourceRegion: 
        
          The ID of the region that contains the source for the db cluster.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBCluster\': {
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
                            \'Status\': \'string\'
                        },
                    ],
                    \'IAMDatabaseAuthenticationEnabled\': True|False,
                    \'CloneGroupId\': \'string\',
                    \'ClusterCreateTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBCluster** *(dict) --* 
        
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
        
        """
        pass

    def create_db_cluster_parameter_group(self, DBClusterParameterGroupName: str, DBParameterGroupFamily: str, Description: str, Tags: List = None) -> Dict:
        """
        
        Parameters in a DB cluster parameter group apply to all of the instances in a DB cluster.
        
        A DB cluster parameter group is initially created with the default parameters for the database engine used by instances in the DB cluster. To provide custom values for any of the parameters, you must modify the group after creating it using  ModifyDBClusterParameterGroup . Once you\'ve created a DB cluster parameter group, you need to associate it with your DB cluster using  ModifyDBCluster . When you associate a new DB cluster parameter group with a running DB cluster, you need to reboot the DB instances in the DB cluster without failover for the new DB cluster parameter group and associated settings to take effect. 
        
        .. warning::
        
          After you create a DB cluster parameter group, you should wait at least 5 minutes before creating your first DB cluster that uses that DB cluster parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the DB cluster parameter group is used as the default for a new DB cluster. This is especially important for parameters that are critical when creating the default database for a DB cluster, such as the character set for the default database defined by the ``character_set_database`` parameter. You can use the *Parameter Groups* option of the `Amazon Neptune console <https://console.aws.amazon.com/rds/>`__ or the  DescribeDBClusterParameters command to verify that your DB cluster parameter group has been created or modified.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/CreateDBClusterParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_db_cluster_parameter_group(
              DBClusterParameterGroupName=\'string\',
              DBParameterGroupFamily=\'string\',
              Description=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DBClusterParameterGroupName: string
        :param DBClusterParameterGroupName: **[REQUIRED]** 
        
          The name of the DB cluster parameter group.
        
          Constraints:
        
          * Must match the name of an existing DBClusterParameterGroup. 
           
          .. note::
        
            This value is stored as a lowercase string.
        
        :type DBParameterGroupFamily: string
        :param DBParameterGroupFamily: **[REQUIRED]** 
        
          The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a database engine and engine version compatible with that DB cluster parameter group family.
        
        :type Description: string
        :param Description: **[REQUIRED]** 
        
          The description for the DB cluster parameter group.
        
        :type Tags: list
        :param Tags: 
        
          A list of tags. For more information, see `Tagging Amazon Neptune Resources <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html>`__ . 
        
          - *(dict) --* 
        
            Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBClusterParameterGroup\': {
                    \'DBClusterParameterGroupName\': \'string\',
                    \'DBParameterGroupFamily\': \'string\',
                    \'Description\': \'string\',
                    \'DBClusterParameterGroupArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBClusterParameterGroup** *(dict) --* 
        
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
        
        """
        pass

    def create_db_cluster_snapshot(self, DBClusterSnapshotIdentifier: str, DBClusterIdentifier: str, Tags: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/CreateDBClusterSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_db_cluster_snapshot(
              DBClusterSnapshotIdentifier=\'string\',
              DBClusterIdentifier=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DBClusterSnapshotIdentifier: string
        :param DBClusterSnapshotIdentifier: **[REQUIRED]** 
        
          The identifier of the DB cluster snapshot. This parameter is stored as a lowercase string.
        
          Constraints:
        
          * Must contain from 1 to 63 letters, numbers, or hyphens. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
          Example: ``my-cluster1-snapshot1``  
        
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]** 
        
          The identifier of the DB cluster to create a snapshot for. This parameter is not case-sensitive.
        
          Constraints:
        
          * Must match the identifier of an existing DBCluster. 
           
          Example: ``my-cluster1``  
        
        :type Tags: list
        :param Tags: 
        
          The tags to be assigned to the DB cluster snapshot.
        
          - *(dict) --* 
        
            Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBClusterSnapshot\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBClusterSnapshot** *(dict) --* 
        
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
        
        """
        pass

    def create_db_instance(self, DBInstanceIdentifier: str, DBInstanceClass: str, Engine: str, DBName: str = None, AllocatedStorage: int = None, MasterUsername: str = None, MasterUserPassword: str = None, DBSecurityGroups: List = None, VpcSecurityGroupIds: List = None, AvailabilityZone: str = None, DBSubnetGroupName: str = None, PreferredMaintenanceWindow: str = None, DBParameterGroupName: str = None, BackupRetentionPeriod: int = None, PreferredBackupWindow: str = None, Port: int = None, MultiAZ: bool = None, EngineVersion: str = None, AutoMinorVersionUpgrade: bool = None, LicenseModel: str = None, Iops: int = None, OptionGroupName: str = None, CharacterSetName: str = None, PubliclyAccessible: bool = None, Tags: List = None, DBClusterIdentifier: str = None, StorageType: str = None, TdeCredentialArn: str = None, TdeCredentialPassword: str = None, StorageEncrypted: bool = None, KmsKeyId: str = None, Domain: str = None, CopyTagsToSnapshot: bool = None, MonitoringInterval: int = None, MonitoringRoleArn: str = None, DomainIAMRoleName: str = None, PromotionTier: int = None, Timezone: str = None, EnableIAMDatabaseAuthentication: bool = None, EnablePerformanceInsights: bool = None, PerformanceInsightsKMSKeyId: str = None, EnableCloudwatchLogsExports: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/CreateDBInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_db_instance(
              DBName=\'string\',
              DBInstanceIdentifier=\'string\',
              AllocatedStorage=123,
              DBInstanceClass=\'string\',
              Engine=\'string\',
              MasterUsername=\'string\',
              MasterUserPassword=\'string\',
              DBSecurityGroups=[
                  \'string\',
              ],
              VpcSecurityGroupIds=[
                  \'string\',
              ],
              AvailabilityZone=\'string\',
              DBSubnetGroupName=\'string\',
              PreferredMaintenanceWindow=\'string\',
              DBParameterGroupName=\'string\',
              BackupRetentionPeriod=123,
              PreferredBackupWindow=\'string\',
              Port=123,
              MultiAZ=True|False,
              EngineVersion=\'string\',
              AutoMinorVersionUpgrade=True|False,
              LicenseModel=\'string\',
              Iops=123,
              OptionGroupName=\'string\',
              CharacterSetName=\'string\',
              PubliclyAccessible=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              DBClusterIdentifier=\'string\',
              StorageType=\'string\',
              TdeCredentialArn=\'string\',
              TdeCredentialPassword=\'string\',
              StorageEncrypted=True|False,
              KmsKeyId=\'string\',
              Domain=\'string\',
              CopyTagsToSnapshot=True|False,
              MonitoringInterval=123,
              MonitoringRoleArn=\'string\',
              DomainIAMRoleName=\'string\',
              PromotionTier=123,
              Timezone=\'string\',
              EnableIAMDatabaseAuthentication=True|False,
              EnablePerformanceInsights=True|False,
              PerformanceInsightsKMSKeyId=\'string\',
              EnableCloudwatchLogsExports=[
                  \'string\',
              ]
          )
        :type DBName: string
        :param DBName: 
        
          The database name. 
        
          Type: String
        
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: **[REQUIRED]** 
        
          The DB instance identifier. This parameter is stored as a lowercase string.
        
          Constraints:
        
          * Must contain from 1 to 63 letters, numbers, or hyphens. 
           
          * First character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
          Example: ``mydbinstance``  
        
        :type AllocatedStorage: integer
        :param AllocatedStorage: 
        
          The amount of storage (in gibibytes) to allocate for the DB instance.
        
          Type: Integer
        
          Not applicable. Neptune cluster volumes automatically grow as the amount of data in your database increases, though you are only charged for the space that you use in a Neptune cluster volume.
        
        :type DBInstanceClass: string
        :param DBInstanceClass: **[REQUIRED]** 
        
          The compute and memory capacity of the DB instance, for example, ``db.m4.large`` . Not all DB instance classes are available in all AWS Regions. 
        
        :type Engine: string
        :param Engine: **[REQUIRED]** 
        
          The name of the database engine to be used for this instance. 
        
          Valid Values: ``neptune``  
        
        :type MasterUsername: string
        :param MasterUsername: 
        
          The name for the master user. Not used.
        
        :type MasterUserPassword: string
        :param MasterUserPassword: 
        
          The password for the master user. The password can include any printable ASCII character except \"/\", \"\"\", or \"@\".
        
          Not used. 
        
        :type DBSecurityGroups: list
        :param DBSecurityGroups: 
        
          A list of DB security groups to associate with this DB instance.
        
          Default: The default DB security group for the database engine.
        
          - *(string) --* 
        
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds: 
        
          A list of EC2 VPC security groups to associate with this DB instance.
        
          Not applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see  CreateDBCluster .
        
          Default: The default EC2 VPC security group for the DB subnet group\'s VPC.
        
          - *(string) --* 
        
        :type AvailabilityZone: string
        :param AvailabilityZone: 
        
          The EC2 Availability Zone that the DB instance is created in. 
        
          Default: A random, system-chosen Availability Zone in the endpoint\'s AWS Region.
        
          Example: ``us-east-1d``  
        
          Constraint: The AvailabilityZone parameter can\'t be specified if the MultiAZ parameter is set to ``true`` . The specified Availability Zone must be in the same AWS Region as the current endpoint. 
        
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName: 
        
          A DB subnet group to associate with this DB instance.
        
          If there is no DB subnet group, then it is a non-VPC DB instance.
        
        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow: 
        
          The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC). 
        
          Format: ``ddd:hh24:mi-ddd:hh24:mi``  
        
          The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. 
        
          Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
        
          Constraints: Minimum 30-minute window.
        
        :type DBParameterGroupName: string
        :param DBParameterGroupName: 
        
          The name of the DB parameter group to associate with this DB instance. If this argument is omitted, the default DBParameterGroup for the specified engine is used.
        
          Constraints:
        
          * Must be 1 to 255 letters, numbers, or hyphens. 
           
          * First character must be a letter 
           
          * Cannot end with a hyphen or contain two consecutive hyphens 
           
        :type BackupRetentionPeriod: integer
        :param BackupRetentionPeriod: 
        
          The number of days for which automated backups are retained.
        
          Not applicable. The retention period for automated backups is managed by the DB cluster. For more information, see  CreateDBCluster .
        
          Default: 1
        
          Constraints:
        
          * Must be a value from 0 to 35 
           
          * Cannot be set to 0 if the DB instance is a source to Read Replicas 
           
        :type PreferredBackupWindow: string
        :param PreferredBackupWindow: 
        
          The daily time range during which automated backups are created. 
        
          Not applicable. The daily time range for creating automated backups is managed by the DB cluster. For more information, see  CreateDBCluster .
        
        :type Port: integer
        :param Port: 
        
          The port number on which the database accepts connections.
        
          Not applicable. The port is managed by the DB cluster. For more information, see  CreateDBCluster .
        
          Default: ``8182``  
        
          Type: Integer
        
        :type MultiAZ: boolean
        :param MultiAZ: 
        
          Specifies if the DB instance is a Multi-AZ deployment. You can\'t set the AvailabilityZone parameter if the MultiAZ parameter is set to true.
        
        :type EngineVersion: string
        :param EngineVersion: 
        
          The version number of the database engine to use.
        
        :type AutoMinorVersionUpgrade: boolean
        :param AutoMinorVersionUpgrade: 
        
          Indicates that minor engine upgrades are applied automatically to the DB instance during the maintenance window.
        
          Default: ``true``  
        
        :type LicenseModel: string
        :param LicenseModel: 
        
          License model information for this DB instance.
        
          Valid values: ``license-included`` | ``bring-your-own-license`` | ``general-public-license``  
        
        :type Iops: integer
        :param Iops: 
        
          The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for the DB instance. 
        
        :type OptionGroupName: string
        :param OptionGroupName: 
        
          Indicates that the DB instance should be associated with the specified option group.
        
          Permanent options, such as the TDE option for Oracle Advanced Security TDE, can\'t be removed from an option group, and that option group can\'t be removed from a DB instance once it is associated with a DB instance
        
        :type CharacterSetName: string
        :param CharacterSetName: 
        
          Indicates that the DB instance should be associated with the specified CharacterSet.
        
          Not applicable. The character set is managed by the DB cluster. For more information, see  CreateDBCluster .
        
        :type PubliclyAccessible: boolean
        :param PubliclyAccessible: 
        
          This parameter is not supported.
        
        :type Tags: list
        :param Tags: 
        
          A list of tags. For more information, see `Tagging Amazon Neptune Resources <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html>`__ . 
        
          - *(dict) --* 
        
            Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: 
        
          The identifier of the DB cluster that the instance will belong to.
        
          For information on creating a DB cluster, see  CreateDBCluster .
        
          Type: String
        
        :type StorageType: string
        :param StorageType: 
        
          Specifies the storage type to be associated with the DB instance.
        
          Not applicable. Storage is managed by the DB Cluster.
        
        :type TdeCredentialArn: string
        :param TdeCredentialArn: 
        
          The ARN from the key store with which to associate the instance for TDE encryption.
        
        :type TdeCredentialPassword: string
        :param TdeCredentialPassword: 
        
          The password for the given ARN from the key store in order to access the device.
        
        :type StorageEncrypted: boolean
        :param StorageEncrypted: 
        
          Specifies whether the DB instance is encrypted.
        
          Not applicable. The encryption for DB instances is managed by the DB cluster. For more information, see  CreateDBCluster .
        
          Default: false
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          The AWS KMS key identifier for an encrypted DB instance.
        
          The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB instance with the same AWS account that owns the KMS encryption key used to encrypt the new DB instance, then you can use the KMS key alias instead of the ARN for the KM encryption key.
        
          Not applicable. The KMS key identifier is managed by the DB cluster. For more information, see  CreateDBCluster .
        
          If the ``StorageEncrypted`` parameter is true, and you do not specify a value for the ``KmsKeyId`` parameter, then Amazon Neptune will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
        
        :type Domain: string
        :param Domain: 
        
          Specify the Active Directory Domain to create the instance in.
        
        :type CopyTagsToSnapshot: boolean
        :param CopyTagsToSnapshot: 
        
          True to copy all tags from the DB instance to snapshots of the DB instance, and otherwise false. The default is false.
        
        :type MonitoringInterval: integer
        :param MonitoringInterval: 
        
          The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
        
          If ``MonitoringRoleArn`` is specified, then you must also set ``MonitoringInterval`` to a value other than 0.
        
          Valid Values: ``0, 1, 5, 10, 15, 30, 60``  
        
        :type MonitoringRoleArn: string
        :param MonitoringRoleArn: 
        
          The ARN for the IAM role that permits Neptune to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, ``arn:aws:iam:123456789012:role/emaccess`` .
        
          If ``MonitoringInterval`` is set to a value other than 0, then you must supply a ``MonitoringRoleArn`` value.
        
        :type DomainIAMRoleName: string
        :param DomainIAMRoleName: 
        
          Specify the name of the IAM role to be used when making API calls to the Directory Service.
        
        :type PromotionTier: integer
        :param PromotionTier: 
        
          A value that specifies the order in which an Read Replica is promoted to the primary instance after a failure of the existing primary instance. 
        
          Default: 1
        
          Valid Values: 0 - 15
        
        :type Timezone: string
        :param Timezone: 
        
          The time zone of the DB instance. 
        
        :type EnableIAMDatabaseAuthentication: boolean
        :param EnableIAMDatabaseAuthentication: 
        
          True to enable AWS Identity and Access Management (IAM) authentication for Neptune.
        
          Default: ``false``  
        
        :type EnablePerformanceInsights: boolean
        :param EnablePerformanceInsights: 
        
          True to enable Performance Insights for the DB instance, and otherwise false. 
        
        :type PerformanceInsightsKMSKeyId: string
        :param PerformanceInsightsKMSKeyId: 
        
          The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.
        
        :type EnableCloudwatchLogsExports: list
        :param EnableCloudwatchLogsExports: 
        
          The list of log types that need to be enabled for exporting to CloudWatch Logs.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBInstance\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBInstance** *(dict) --* 
        
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
            
        """
        pass

    def create_db_parameter_group(self, DBParameterGroupName: str, DBParameterGroupFamily: str, Description: str, Tags: List = None) -> Dict:
        """
        
        A DB parameter group is initially created with the default parameters for the database engine used by the DB instance. To provide custom values for any of the parameters, you must modify the group after creating it using *ModifyDBParameterGroup* . Once you\'ve created a DB parameter group, you need to associate it with your DB instance using *ModifyDBInstance* . When you associate a new DB parameter group with a running DB instance, you need to reboot the DB instance without failover for the new DB parameter group and associated settings to take effect. 
        
        .. warning::
        
          After you create a DB parameter group, you should wait at least 5 minutes before creating your first DB instance that uses that DB parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the parameter group is used as the default for a new DB instance. This is especially important for parameters that are critical when creating the default database for a DB instance, such as the character set for the default database defined by the ``character_set_database`` parameter. You can use the *Parameter Groups* option of the Amazon Neptune console or the *DescribeDBParameters* command to verify that your DB parameter group has been created or modified.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/CreateDBParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_db_parameter_group(
              DBParameterGroupName=\'string\',
              DBParameterGroupFamily=\'string\',
              Description=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DBParameterGroupName: string
        :param DBParameterGroupName: **[REQUIRED]** 
        
          The name of the DB parameter group.
        
          Constraints:
        
          * Must be 1 to 255 letters, numbers, or hyphens. 
           
          * First character must be a letter 
           
          * Cannot end with a hyphen or contain two consecutive hyphens 
           
          .. note::
        
            This value is stored as a lowercase string.
        
        :type DBParameterGroupFamily: string
        :param DBParameterGroupFamily: **[REQUIRED]** 
        
          The DB parameter group family name. A DB parameter group can be associated with one and only one DB parameter group family, and can be applied only to a DB instance running a database engine and engine version compatible with that DB parameter group family.
        
        :type Description: string
        :param Description: **[REQUIRED]** 
        
          The description for the DB parameter group.
        
        :type Tags: list
        :param Tags: 
        
          A list of tags. For more information, see `Tagging Amazon Neptune Resources <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html>`__ . 
        
          - *(dict) --* 
        
            Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBParameterGroup\': {
                    \'DBParameterGroupName\': \'string\',
                    \'DBParameterGroupFamily\': \'string\',
                    \'Description\': \'string\',
                    \'DBParameterGroupArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBParameterGroup** *(dict) --* 
        
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
        
        """
        pass

    def create_db_subnet_group(self, DBSubnetGroupName: str, DBSubnetGroupDescription: str, SubnetIds: List, Tags: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/CreateDBSubnetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_db_subnet_group(
              DBSubnetGroupName=\'string\',
              DBSubnetGroupDescription=\'string\',
              SubnetIds=[
                  \'string\',
              ],
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
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
        
          The EC2 Subnet IDs for the DB subnet group.
        
          - *(string) --* 
        
        :type Tags: list
        :param Tags: 
        
          A list of tags. For more information, see `Tagging Amazon Neptune Resources <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html>`__ . 
        
          - *(dict) --* 
        
            Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBSubnetGroup** *(dict) --* 
        
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
        
        """
        pass

    def create_event_subscription(self, SubscriptionName: str, SnsTopicArn: str, SourceType: str = None, EventCategories: List = None, SourceIds: List = None, Enabled: bool = None, Tags: List = None) -> Dict:
        """
        
        You can specify the type of source (SourceType) you want to be notified of, provide a list of Neptune sources (SourceIds) that triggers the events, and provide a list of event categories (EventCategories) for events you want to be notified of. For example, you can specify SourceType = db-instance, SourceIds = mydbinstance1, mydbinstance2 and EventCategories = Availability, Backup.
        
        If you specify both the SourceType and SourceIds, such as SourceType = db-instance and SourceIdentifier = myDBInstance1, you are notified of all the db-instance events for the specified source. If you specify a SourceType but do not specify a SourceIdentifier, you receive notice of the events for that source type for all your Neptune sources. If you do not specify either the SourceType nor the SourceIdentifier, you are notified of events generated from all Neptune sources belonging to your customer account.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/CreateEventSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_event_subscription(
              SubscriptionName=\'string\',
              SnsTopicArn=\'string\',
              SourceType=\'string\',
              EventCategories=[
                  \'string\',
              ],
              SourceIds=[
                  \'string\',
              ],
              Enabled=True|False,
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type SubscriptionName: string
        :param SubscriptionName: **[REQUIRED]** 
        
          The name of the subscription.
        
          Constraints: The name must be less than 255 characters.
        
        :type SnsTopicArn: string
        :param SnsTopicArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
        
        :type SourceType: string
        :param SourceType: 
        
          The type of source that is generating the events. For example, if you want to be notified of events generated by a DB instance, you would set this parameter to db-instance. if this value is not specified, all events are returned.
        
          Valid values: ``db-instance`` | ``db-cluster`` | ``db-parameter-group`` | ``db-security-group`` | ``db-snapshot`` | ``db-cluster-snapshot``  
        
        :type EventCategories: list
        :param EventCategories: 
        
          A list of event categories for a SourceType that you want to subscribe to. You can see a list of the categories for a given SourceType by using the **DescribeEventCategories** action. 
        
          - *(string) --* 
        
        :type SourceIds: list
        :param SourceIds: 
        
          The list of identifiers of the event sources for which events are returned. If not specified, then all sources are included in the response. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can\'t end with a hyphen or contain two consecutive hyphens.
        
          Constraints:
        
          * If SourceIds are supplied, SourceType must also be provided. 
           
          * If the source type is a DB instance, then a ``DBInstanceIdentifier`` must be supplied. 
           
          * If the source type is a DB security group, a ``DBSecurityGroupName`` must be supplied. 
           
          * If the source type is a DB parameter group, a ``DBParameterGroupName`` must be supplied. 
           
          * If the source type is a DB snapshot, a ``DBSnapshotIdentifier`` must be supplied. 
           
          - *(string) --* 
        
        :type Enabled: boolean
        :param Enabled: 
        
          A Boolean value; set to **true** to activate the subscription, set to **false** to create the subscription but not active it. 
        
        :type Tags: list
        :param Tags: 
        
          A list of tags. For more information, see `Tagging Amazon Neptune Resources <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html>`__ . 
        
          - *(dict) --* 
        
            Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EventSubscription\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EventSubscription** *(dict) --* 
        
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
        
        """
        pass

    def delete_db_cluster(self, DBClusterIdentifier: str, SkipFinalSnapshot: bool = None, FinalDBSnapshotIdentifier: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DeleteDBCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_db_cluster(
              DBClusterIdentifier=\'string\',
              SkipFinalSnapshot=True|False,
              FinalDBSnapshotIdentifier=\'string\'
          )
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]** 
        
          The DB cluster identifier for the DB cluster to be deleted. This parameter isn\'t case-sensitive.
        
          Constraints:
        
          * Must match an existing DBClusterIdentifier. 
           
        :type SkipFinalSnapshot: boolean
        :param SkipFinalSnapshot: 
        
          Determines whether a final DB cluster snapshot is created before the DB cluster is deleted. If ``true`` is specified, no DB cluster snapshot is created. If ``false`` is specified, a DB cluster snapshot is created before the DB cluster is deleted. 
        
          .. note::
        
            You must specify a ``FinalDBSnapshotIdentifier`` parameter if ``SkipFinalSnapshot`` is ``false`` .
        
          Default: ``false``  
        
        :type FinalDBSnapshotIdentifier: string
        :param FinalDBSnapshotIdentifier: 
        
          The DB cluster snapshot identifier of the new DB cluster snapshot created when ``SkipFinalSnapshot`` is set to ``false`` . 
        
          .. note::
        
            Specifying this parameter and also setting the ``SkipFinalShapshot`` parameter to true results in an error. 
        
          Constraints:
        
          * Must be 1 to 255 letters, numbers, or hyphens. 
           
          * First character must be a letter 
           
          * Cannot end with a hyphen or contain two consecutive hyphens 
           
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBCluster\': {
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
                            \'Status\': \'string\'
                        },
                    ],
                    \'IAMDatabaseAuthenticationEnabled\': True|False,
                    \'CloneGroupId\': \'string\',
                    \'ClusterCreateTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBCluster** *(dict) --* 
        
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
        
        """
        pass

    def delete_db_cluster_parameter_group(self, DBClusterParameterGroupName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DeleteDBClusterParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_db_cluster_parameter_group(
              DBClusterParameterGroupName=\'string\'
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
        
        .. note::
        
          The DB cluster snapshot must be in the ``available`` state to be deleted.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DeleteDBClusterSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_db_cluster_snapshot(
              DBClusterSnapshotIdentifier=\'string\'
          )
        :type DBClusterSnapshotIdentifier: string
        :param DBClusterSnapshotIdentifier: **[REQUIRED]** 
        
          The identifier of the DB cluster snapshot to delete.
        
          Constraints: Must be the name of an existing DB cluster snapshot in the ``available`` state.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBClusterSnapshot\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBClusterSnapshot** *(dict) --* 
        
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
        
        """
        pass

    def delete_db_instance(self, DBInstanceIdentifier: str, SkipFinalSnapshot: bool = None, FinalDBSnapshotIdentifier: str = None) -> Dict:
        """
        
        If you request a final DB snapshot the status of the Amazon Neptune DB instance is ``deleting`` until the DB snapshot is created. The API action ``DescribeDBInstance`` is used to monitor the status of this operation. The action can\'t be canceled or reverted once submitted. 
        
        Note that when a DB instance is in a failure state and has a status of ``failed`` , ``incompatible-restore`` , or ``incompatible-network`` , you can only delete it when the ``SkipFinalSnapshot`` parameter is set to ``true`` .
        
        If the specified DB instance is part of a DB cluster, you can\'t delete the DB instance if both of the following conditions are true:
        
        * The DB cluster is a Read Replica of another DB cluster. 
         
        * The DB instance is the only instance in the DB cluster. 
         
        To delete a DB instance in this case, first call the  PromoteReadReplicaDBCluster API action to promote the DB cluster so it\'s no longer a Read Replica. After the promotion completes, then call the ``DeleteDBInstance`` API action to delete the final instance in the DB cluster.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DeleteDBInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_db_instance(
              DBInstanceIdentifier=\'string\',
              SkipFinalSnapshot=True|False,
              FinalDBSnapshotIdentifier=\'string\'
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: **[REQUIRED]** 
        
          The DB instance identifier for the DB instance to be deleted. This parameter isn\'t case-sensitive.
        
          Constraints:
        
          * Must match the name of an existing DB instance. 
           
        :type SkipFinalSnapshot: boolean
        :param SkipFinalSnapshot: 
        
          Determines whether a final DB snapshot is created before the DB instance is deleted. If ``true`` is specified, no DBSnapshot is created. If ``false`` is specified, a DB snapshot is created before the DB instance is deleted. 
        
          Note that when a DB instance is in a failure state and has a status of \'failed\', \'incompatible-restore\', or \'incompatible-network\', it can only be deleted when the SkipFinalSnapshot parameter is set to \"true\".
        
          Specify ``true`` when deleting a Read Replica.
        
          .. note::
        
            The FinalDBSnapshotIdentifier parameter must be specified if SkipFinalSnapshot is ``false`` .
        
          Default: ``false``  
        
        :type FinalDBSnapshotIdentifier: string
        :param FinalDBSnapshotIdentifier: 
        
          The DBSnapshotIdentifier of the new DBSnapshot created when SkipFinalSnapshot is set to ``false`` . 
        
          .. note::
        
            Specifying this parameter and also setting the SkipFinalShapshot parameter to true results in an error.
        
          Constraints:
        
          * Must be 1 to 255 letters or numbers. 
           
          * First character must be a letter 
           
          * Cannot end with a hyphen or contain two consecutive hyphens 
           
          * Cannot be specified when deleting a Read Replica. 
           
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBInstance\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBInstance** *(dict) --* 
        
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
            
        """
        pass

    def delete_db_parameter_group(self, DBParameterGroupName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DeleteDBParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_db_parameter_group(
              DBParameterGroupName=\'string\'
          )
        :type DBParameterGroupName: string
        :param DBParameterGroupName: **[REQUIRED]** 
        
          The name of the DB parameter group.
        
          Constraints:
        
          * Must be the name of an existing DB parameter group 
           
          * You can\'t delete a default DB parameter group 
           
          * Cannot be associated with any DB instances 
           
        :returns: None
        """
        pass

    def delete_db_subnet_group(self, DBSubnetGroupName: str) -> NoReturn:
        """
        
        .. note::
        
          The specified database subnet group must not be associated with any DB instances.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DeleteDBSubnetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_db_subnet_group(
              DBSubnetGroupName=\'string\'
          )
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName: **[REQUIRED]** 
        
          The name of the database subnet group to delete.
        
          .. note::
        
            You can\'t delete the default subnet group.
        
          Constraints:
        
          Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.
        
          Example: ``mySubnetgroup``  
        
        :returns: None
        """
        pass

    def delete_event_subscription(self, SubscriptionName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DeleteEventSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_event_subscription(
              SubscriptionName=\'string\'
          )
        :type SubscriptionName: string
        :param SubscriptionName: **[REQUIRED]** 
        
          The name of the event notification subscription you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EventSubscription\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EventSubscription** *(dict) --* 
        
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
        
        """
        pass

    def describe_db_cluster_parameter_groups(self, DBClusterParameterGroupName: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBClusterParameterGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_db_cluster_parameter_groups(
              DBClusterParameterGroupName=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
          )
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribeDBClusterParameterGroups`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'DBClusterParameterGroups\': [
                    {
                        \'DBClusterParameterGroupName\': \'string\',
                        \'DBParameterGroupFamily\': \'string\',
                        \'Description\': \'string\',
                        \'DBClusterParameterGroupArn\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous ``DescribeDBClusterParameterGroups`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_db_cluster_parameters(self, DBClusterParameterGroupName: str, Source: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBClusterParameters>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_db_cluster_parameters(
              DBClusterParameterGroupName=\'string\',
              Source=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
          )
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribeDBClusterParameters`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
                \'Marker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Provides details about a DB cluster parameter group including the parameters in the DB cluster parameter group.
        
            - **Parameters** *(list) --* 
        
              Provides a list of parameters for the DB cluster parameter group.
        
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
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous DescribeDBClusterParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        """
        pass

    def describe_db_cluster_snapshot_attributes(self, DBClusterSnapshotIdentifier: str) -> Dict:
        """
        
        When sharing snapshots with other AWS accounts, ``DescribeDBClusterSnapshotAttributes`` returns the ``restore`` attribute and a list of IDs for the AWS accounts that are authorized to copy or restore the manual DB cluster snapshot. If ``all`` is included in the list of values for the ``restore`` attribute, then the manual DB cluster snapshot is public and can be copied or restored by all AWS accounts.
        
        To add or remove access for an AWS account to copy or restore a manual DB cluster snapshot, or to make the manual DB cluster snapshot public or private, use the  ModifyDBClusterSnapshotAttribute API action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBClusterSnapshotAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_db_cluster_snapshot_attributes(
              DBClusterSnapshotIdentifier=\'string\'
          )
        :type DBClusterSnapshotIdentifier: string
        :param DBClusterSnapshotIdentifier: **[REQUIRED]** 
        
          The identifier for the DB cluster snapshot to describe the attributes for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBClusterSnapshotAttributesResult\': {
                    \'DBClusterSnapshotIdentifier\': \'string\',
                    \'DBClusterSnapshotAttributes\': [
                        {
                            \'AttributeName\': \'string\',
                            \'AttributeValues\': [
                                \'string\',
                            ]
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBClusterSnapshotAttributesResult** *(dict) --* 
        
              Contains the results of a successful call to the  DescribeDBClusterSnapshotAttributes API action.
        
              Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or restore a manual DB cluster snapshot. For more information, see the  ModifyDBClusterSnapshotAttribute API action.
        
              - **DBClusterSnapshotIdentifier** *(string) --* 
        
                The identifier of the manual DB cluster snapshot that the attributes apply to.
        
              - **DBClusterSnapshotAttributes** *(list) --* 
        
                The list of attributes and values for the manual DB cluster snapshot.
        
                - *(dict) --* 
        
                  Contains the name and values of a manual DB cluster snapshot attribute.
        
                  Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore a manual DB cluster snapshot. For more information, see the  ModifyDBClusterSnapshotAttribute API action.
        
                  - **AttributeName** *(string) --* 
        
                    The name of the manual DB cluster snapshot attribute.
        
                    The attribute named ``restore`` refers to the list of AWS accounts that have permission to copy or restore the manual DB cluster snapshot. For more information, see the  ModifyDBClusterSnapshotAttribute API action.
        
                  - **AttributeValues** *(list) --* 
        
                    The value(s) for the manual DB cluster snapshot attribute.
        
                    If the ``AttributeName`` field is set to ``restore`` , then this element returns a list of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is public and available for any AWS account to copy or restore.
        
                    - *(string) --* 
                
        """
        pass

    def describe_db_cluster_snapshots(self, DBClusterIdentifier: str = None, DBClusterSnapshotIdentifier: str = None, SnapshotType: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, IncludeShared: bool = None, IncludePublic: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBClusterSnapshots>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_db_cluster_snapshots(
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
              MaxRecords=123,
              Marker=\'string\',
              IncludeShared=True|False,
              IncludePublic=True|False
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribeDBClusterSnapshots`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :type IncludeShared: boolean
        :param IncludeShared: 
        
          True to include shared manual DB cluster snapshots from other AWS accounts that this AWS account has been given permission to copy or restore, and otherwise false. The default is ``false`` .
        
          You can give an AWS account permission to restore a manual DB cluster snapshot from another AWS account by the  ModifyDBClusterSnapshotAttribute API action.
        
        :type IncludePublic: boolean
        :param IncludePublic: 
        
          True to include manual DB cluster snapshots that are public and can be copied or restored by any AWS account, and otherwise false. The default is ``false`` . The default is false.
        
          You can share a manual DB cluster snapshot as public by using the  ModifyDBClusterSnapshotAttribute API action.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Provides a list of DB cluster snapshots for the user as the result of a call to the  DescribeDBClusterSnapshots action. 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous  DescribeDBClusterSnapshots request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_db_clusters(self, DBClusterIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBClusters>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_db_clusters(
              DBClusterIdentifier=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
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
        
            This type is not currently supported.
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              This parameter is not currently supported.
        
            - **Values** *(list) --* **[REQUIRED]** 
        
              This parameter is not currently supported.
        
              - *(string) --* 
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous  DescribeDBClusters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
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
                                \'Status\': \'string\'
                            },
                        ],
                        \'IAMDatabaseAuthenticationEnabled\': True|False,
                        \'CloneGroupId\': \'string\',
                        \'ClusterCreateTime\': datetime(2015, 1, 1)
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeDBClusters action.
        
            - **Marker** *(string) --* 
        
              A pagination token that can be used in a subsequent DescribeDBClusters request.
        
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
        
        """
        pass

    def describe_db_engine_versions(self, Engine: str = None, EngineVersion: str = None, DBParameterGroupFamily: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None, DefaultOnly: bool = None, ListSupportedCharacterSets: bool = None, ListSupportedTimezones: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBEngineVersions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_db_engine_versions(
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
              MaxRecords=123,
              Marker=\'string\',
              DefaultOnly=True|False,
              ListSupportedCharacterSets=True|False,
              ListSupportedTimezones=True|False
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more than the ``MaxRecords`` value is available, a pagination token called a marker is included in the response so that the following results can be retrieved. 
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeDBEngineVersions action. 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_db_instances(self, DBInstanceIdentifier: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBInstances>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_db_instances(
              DBInstanceIdentifier=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribeDBInstances`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeDBInstances action. 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
              
        """
        pass

    def describe_db_parameter_groups(self, DBParameterGroupName: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBParameterGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_db_parameter_groups(
              DBParameterGroupName=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribeDBParameterGroups`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
                \'DBParameterGroups\': [
                    {
                        \'DBParameterGroupName\': \'string\',
                        \'DBParameterGroupFamily\': \'string\',
                        \'Description\': \'string\',
                        \'DBParameterGroupArn\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeDBParameterGroups action. 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_db_parameters(self, DBParameterGroupName: str, Source: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBParameters>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_db_parameters(
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
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribeDBParameters`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
                \'Marker\': \'string\'
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
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        """
        pass

    def describe_db_subnet_groups(self, DBSubnetGroupName: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        For an overview of CIDR ranges, go to the `Wikipedia Tutorial <http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBSubnetGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_db_subnet_groups(
              DBSubnetGroupName=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous DescribeDBSubnetGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeDBSubnetGroups action. 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_engine_default_cluster_parameters(self, DBParameterGroupFamily: str, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeEngineDefaultClusterParameters>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_engine_default_cluster_parameters(
              DBParameterGroupFamily=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
          )
        :type DBParameterGroupFamily: string
        :param DBParameterGroupFamily: **[REQUIRED]** 
        
          The name of the DB cluster parameter group family to return engine parameter information for.
        
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribeEngineDefaultClusterParameters`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
                }
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
        
        """
        pass

    def describe_engine_default_parameters(self, DBParameterGroupFamily: str, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeEngineDefaultParameters>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_engine_default_parameters(
              DBParameterGroupFamily=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribeEngineDefaultParameters`` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
                }
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
        
        """
        pass

    def describe_event_categories(self, SourceType: str = None, Filters: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeEventCategories>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_event_categories(
              SourceType=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ]
          )
        :type SourceType: string
        :param SourceType: 
        
          The type of source that is generating the events.
        
          Valid values: db-instance | db-parameter-group | db-security-group | db-snapshot
        
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
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EventCategoriesMapList\': [
                    {
                        \'SourceType\': \'string\',
                        \'EventCategories\': [
                            \'string\',
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Data returned from the **DescribeEventCategories** action.
        
            - **EventCategoriesMapList** *(list) --* 
        
              A list of EventCategoriesMap data types.
        
              - *(dict) --* 
        
                Contains the results of a successful invocation of the  DescribeEventCategories action.
        
                - **SourceType** *(string) --* 
        
                  The source type that the returned categories belong to
        
                - **EventCategories** *(list) --* 
        
                  The event categories for the specified source type
        
                  - *(string) --* 
              
        """
        pass

    def describe_event_subscriptions(self, SubscriptionName: str = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        If you specify a SubscriptionName, lists the description for that subscription.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeEventSubscriptions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_event_subscriptions(
              SubscriptionName=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Data returned by the **DescribeEventSubscriptions** action.
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_events(self, SourceIdentifier: str = None, SourceType: str = None, StartTime: datetime = None, EndTime: datetime = None, Duration: int = None, EventCategories: List = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_events(
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
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous DescribeEvents request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Marker\': \'string\',
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
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  DescribeEvents action. 
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous Events request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
        
        """
        pass

    def describe_orderable_db_instance_options(self, Engine: str, EngineVersion: str = None, DBInstanceClass: str = None, LicenseModel: str = None, Vpc: bool = None, Filters: List = None, MaxRecords: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeOrderableDBInstanceOptions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_orderable_db_instance_options(
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
              MaxRecords=123,
              Marker=\'string\'
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
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
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
                \'Marker\': \'string\'
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
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous OrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` . 
        
        """
        pass

    def describe_pending_maintenance_actions(self, ResourceIdentifier: str = None, Filters: List = None, Marker: str = None, MaxRecords: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribePendingMaintenanceActions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_pending_maintenance_actions(
              ResourceIdentifier=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              Marker=\'string\',
              MaxRecords=123
          )
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
        
        :type Marker: string
        :param Marker: 
        
          An optional pagination token provided by a previous ``DescribePendingMaintenanceActions`` request. If this parameter is specified, the response includes only records beyond the marker, up to a number of records specified by ``MaxRecords`` . 
        
        :type MaxRecords: integer
        :param MaxRecords: 
        
          The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. 
        
          Default: 100
        
          Constraints: Minimum 20, maximum 100.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PendingMaintenanceActions\': [
                    {
                        \'ResourceIdentifier\': \'string\',
                        \'PendingMaintenanceActionDetails\': [
                            {
                                \'Action\': \'string\',
                                \'AutoAppliedAfterDate\': datetime(2015, 1, 1),
                                \'ForcedApplyDate\': datetime(2015, 1, 1),
                                \'OptInStatus\': \'string\',
                                \'CurrentApplyDate\': datetime(2015, 1, 1),
                                \'Description\': \'string\'
                            },
                        ]
                    },
                ],
                \'Marker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Data returned from the **DescribePendingMaintenanceActions** action.
        
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
        
            - **Marker** *(string) --* 
        
              An optional pagination token provided by a previous ``DescribePendingMaintenanceActions`` request. If this parameter is specified, the response includes only records beyond the marker, up to a number of records specified by ``MaxRecords`` . 
        
        """
        pass

    def describe_valid_db_instance_modifications(self, DBInstanceIdentifier: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeValidDBInstanceModifications>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_valid_db_instance_modifications(
              DBInstanceIdentifier=\'string\'
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: **[REQUIRED]** 
        
          The customer identifier or the ARN of your DB instance. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ValidDBInstanceModificationsMessage\': {
                    \'Storage\': [
                        {
                            \'StorageType\': \'string\',
                            \'StorageSize\': [
                                {
                                    \'From\': 123,
                                    \'To\': 123,
                                    \'Step\': 123
                                },
                            ],
                            \'ProvisionedIops\': [
                                {
                                    \'From\': 123,
                                    \'To\': 123,
                                    \'Step\': 123
                                },
                            ],
                            \'IopsToStorageRatio\': [
                                {
                                    \'From\': 123.0,
                                    \'To\': 123.0
                                },
                            ]
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ValidDBInstanceModificationsMessage** *(dict) --* 
        
              Information about valid modifications that you can make to your DB instance. Contains the result of a successful call to the  DescribeValidDBInstanceModifications action. You can use this information when you call  ModifyDBInstance . 
        
              - **Storage** *(list) --* 
        
                Valid storage options for your DB instance. 
        
                - *(dict) --* 
        
                  Information about valid modifications that you can make to your DB instance. Contains the result of a successful call to the  DescribeValidDBInstanceModifications action. 
        
                  - **StorageType** *(string) --* 
        
                    The valid storage types for your DB instance. For example, gp2, io1. 
        
                  - **StorageSize** *(list) --* 
        
                    The valid range of storage in gibibytes. For example, 100 to 16384. 
        
                    - *(dict) --* 
        
                      A range of integer values.
        
                      - **From** *(integer) --* 
        
                        The minimum value in the range.
        
                      - **To** *(integer) --* 
        
                        The maximum value in the range.
        
                      - **Step** *(integer) --* 
        
                        The step value for the range. For example, if you have a range of 5,000 to 10,000, with a step value of 1,000, the valid values start at 5,000 and step up by 1,000. Even though 7,500 is within the range, it isn\'t a valid value for the range. The valid values are 5,000, 6,000, 7,000, 8,000... 
        
                  - **ProvisionedIops** *(list) --* 
        
                    The valid range of provisioned IOPS. For example, 1000-20000. 
        
                    - *(dict) --* 
        
                      A range of integer values.
        
                      - **From** *(integer) --* 
        
                        The minimum value in the range.
        
                      - **To** *(integer) --* 
        
                        The maximum value in the range.
        
                      - **Step** *(integer) --* 
        
                        The step value for the range. For example, if you have a range of 5,000 to 10,000, with a step value of 1,000, the valid values start at 5,000 and step up by 1,000. Even though 7,500 is within the range, it isn\'t a valid value for the range. The valid values are 5,000, 6,000, 7,000, 8,000... 
        
                  - **IopsToStorageRatio** *(list) --* 
        
                    The valid range of Provisioned IOPS to gibibytes of storage multiplier. For example, 3-10, which means that provisioned IOPS can be between 3 and 10 times storage. 
        
                    - *(dict) --* 
        
                      A range of double values.
        
                      - **From** *(float) --* 
        
                        The minimum value in the range.
        
                      - **To** *(float) --* 
        
                        The maximum value in the range.
        
        """
        pass

    def failover_db_cluster(self, DBClusterIdentifier: str = None, TargetDBInstanceIdentifier: str = None) -> Dict:
        """
        
        A failover for a DB cluster promotes one of the Read Replicas (read-only instances) in the DB cluster to be the primary instance (the cluster writer).
        
        Amazon Neptune will automatically fail over to a Read Replica, if one exists, when the primary instance fails. You can force a failover when you want to simulate a failure of a primary instance for testing. Because each instance in a DB cluster has its own endpoint address, you will need to clean up and re-establish any existing connections that use those endpoint addresses when the failover is complete.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/FailoverDBCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.failover_db_cluster(
              DBClusterIdentifier=\'string\',
              TargetDBInstanceIdentifier=\'string\'
          )
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: 
        
          A DB cluster identifier to force a failover for. This parameter is not case-sensitive.
        
          Constraints:
        
          * Must match the identifier of an existing DBCluster. 
           
        :type TargetDBInstanceIdentifier: string
        :param TargetDBInstanceIdentifier: 
        
          The name of the instance to promote to the primary instance.
        
          You must specify the instance identifier for an Read Replica in the DB cluster. For example, ``mydbcluster-replica1`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBCluster\': {
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
                            \'Status\': \'string\'
                        },
                    ],
                    \'IAMDatabaseAuthenticationEnabled\': True|False,
                    \'CloneGroupId\': \'string\',
                    \'ClusterCreateTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBCluster** *(dict) --* 
        
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

    def list_tags_for_resource(self, ResourceName: str, Filters: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/ListTagsForResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags_for_resource(
              ResourceName=\'string\',
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ]
          )
        :type ResourceName: string
        :param ResourceName: **[REQUIRED]** 
        
          The Amazon Neptune resource with tags to be listed. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see `Constructing an Amazon Resource Name (ARN) <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing>`__ .
        
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
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TagList\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **TagList** *(list) --* 
        
              List of tags returned by the ListTagsForResource operation.
        
              - *(dict) --* 
        
                Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
        
                - **Key** *(string) --* 
        
                  A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
                - **Value** *(string) --* 
        
                  A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        """
        pass

    def modify_db_cluster(self, DBClusterIdentifier: str, NewDBClusterIdentifier: str = None, ApplyImmediately: bool = None, BackupRetentionPeriod: int = None, DBClusterParameterGroupName: str = None, VpcSecurityGroupIds: List = None, Port: int = None, MasterUserPassword: str = None, OptionGroupName: str = None, PreferredBackupWindow: str = None, PreferredMaintenanceWindow: str = None, EnableIAMDatabaseAuthentication: bool = None, EngineVersion: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/ModifyDBCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_db_cluster(
              DBClusterIdentifier=\'string\',
              NewDBClusterIdentifier=\'string\',
              ApplyImmediately=True|False,
              BackupRetentionPeriod=123,
              DBClusterParameterGroupName=\'string\',
              VpcSecurityGroupIds=[
                  \'string\',
              ],
              Port=123,
              MasterUserPassword=\'string\',
              OptionGroupName=\'string\',
              PreferredBackupWindow=\'string\',
              PreferredMaintenanceWindow=\'string\',
              EnableIAMDatabaseAuthentication=True|False,
              EngineVersion=\'string\'
          )
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]** 
        
          The DB cluster identifier for the cluster being modified. This parameter is not case-sensitive.
        
          Constraints:
        
          * Must match the identifier of an existing DBCluster. 
           
        :type NewDBClusterIdentifier: string
        :param NewDBClusterIdentifier: 
        
          The new DB cluster identifier for the DB cluster when renaming a DB cluster. This value is stored as a lowercase string.
        
          Constraints:
        
          * Must contain from 1 to 63 letters, numbers, or hyphens 
           
          * The first character must be a letter 
           
          * Cannot end with a hyphen or contain two consecutive hyphens 
           
          Example: ``my-cluster2``  
        
        :type ApplyImmediately: boolean
        :param ApplyImmediately: 
        
          A value that specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the ``PreferredMaintenanceWindow`` setting for the DB cluster. If this parameter is set to ``false`` , changes to the DB cluster are applied during the next maintenance window.
        
          The ``ApplyImmediately`` parameter only affects the ``NewDBClusterIdentifier`` and ``MasterUserPassword`` values. If you set the ``ApplyImmediately`` parameter value to false, then changes to the ``NewDBClusterIdentifier`` and ``MasterUserPassword`` values are applied during the next maintenance window. All other changes are applied immediately, regardless of the value of the ``ApplyImmediately`` parameter.
        
          Default: ``false``  
        
        :type BackupRetentionPeriod: integer
        :param BackupRetentionPeriod: 
        
          The number of days for which automated backups are retained. You must specify a minimum value of 1.
        
          Default: 1
        
          Constraints:
        
          * Must be a value from 1 to 35 
           
        :type DBClusterParameterGroupName: string
        :param DBClusterParameterGroupName: 
        
          The name of the DB cluster parameter group to use for the DB cluster.
        
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds: 
        
          A list of VPC security groups that the DB cluster will belong to.
        
          - *(string) --* 
        
        :type Port: integer
        :param Port: 
        
          The port number on which the DB cluster accepts connections.
        
          Constraints: Value must be ``1150-65535``  
        
          Default: The same port as the original DB cluster.
        
        :type MasterUserPassword: string
        :param MasterUserPassword: 
        
          The new password for the master database user. This password can contain any printable ASCII character except \"/\", \"\"\", or \"@\".
        
          Constraints: Must contain from 8 to 41 characters.
        
        :type OptionGroupName: string
        :param OptionGroupName: 
        
          A value that indicates that the DB cluster should be associated with the specified option group. Changing this parameter doesn\'t result in an outage except in the following case, and the change is applied during the next maintenance window unless the ``ApplyImmediately`` parameter is set to ``true`` for this request. If the parameter change results in an option group that enables OEM, this change can cause a brief (sub-second) period during which new connections are rejected but existing connections are not interrupted. 
        
          Permanent options can\'t be removed from an option group. The option group can\'t be removed from a DB cluster once it is associated with a DB cluster.
        
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
        
          Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
        
          Constraints: Minimum 30-minute window.
        
        :type EnableIAMDatabaseAuthentication: boolean
        :param EnableIAMDatabaseAuthentication: 
        
          True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.
        
          Default: ``false``  
        
        :type EngineVersion: string
        :param EngineVersion: 
        
          The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true.
        
          For a list of valid engine versions, see  CreateDBInstance , or call  DescribeDBEngineVersions .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBCluster\': {
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
                            \'Status\': \'string\'
                        },
                    ],
                    \'IAMDatabaseAuthenticationEnabled\': True|False,
                    \'CloneGroupId\': \'string\',
                    \'ClusterCreateTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBCluster** *(dict) --* 
        
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
        
        """
        pass

    def modify_db_cluster_parameter_group(self, DBClusterParameterGroupName: str, Parameters: List) -> Dict:
        """
        
        .. note::
        
          Changes to dynamic parameters are applied immediately. Changes to static parameters require a reboot without failover to the DB cluster associated with the parameter group before the change can take effect.
        
        .. warning::
        
          After you create a DB cluster parameter group, you should wait at least 5 minutes before creating your first DB cluster that uses that DB cluster parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the parameter group is used as the default for a new DB cluster. This is especially important for parameters that are critical when creating the default database for a DB cluster, such as the character set for the default database defined by the ``character_set_database`` parameter. You can use the *Parameter Groups* option of the Amazon Neptune console or the  DescribeDBClusterParameters command to verify that your DB cluster parameter group has been created or modified.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/ModifyDBClusterParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_db_cluster_parameter_group(
              DBClusterParameterGroupName=\'string\',
              Parameters=[
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
          )
        :type DBClusterParameterGroupName: string
        :param DBClusterParameterGroupName: **[REQUIRED]** 
        
          The name of the DB cluster parameter group to modify.
        
        :type Parameters: list
        :param Parameters: **[REQUIRED]** 
        
          A list of parameters in the DB cluster parameter group to modify.
        
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
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBClusterParameterGroupName\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **DBClusterParameterGroupName** *(string) --* 
        
              The name of the DB cluster parameter group.
        
              Constraints:
        
              * Must be 1 to 255 letters or numbers. 
               
              * First character must be a letter 
               
              * Cannot end with a hyphen or contain two consecutive hyphens 
               
              .. note::
        
                This value is stored as a lowercase string.
        
        """
        pass

    def modify_db_cluster_snapshot_attribute(self, DBClusterSnapshotIdentifier: str, AttributeName: str, ValuesToAdd: List = None, ValuesToRemove: List = None) -> Dict:
        """
        
        To share a manual DB cluster snapshot with other AWS accounts, specify ``restore`` as the ``AttributeName`` and use the ``ValuesToAdd`` parameter to add a list of IDs of the AWS accounts that are authorized to restore the manual DB cluster snapshot. Use the value ``all`` to make the manual DB cluster snapshot public, which means that it can be copied or restored by all AWS accounts. Do not add the ``all`` value for any manual DB cluster snapshots that contain private information that you don\'t want available to all AWS accounts. If a manual DB cluster snapshot is encrypted, it can be shared, but only by specifying a list of authorized AWS account IDs for the ``ValuesToAdd`` parameter. You can\'t use ``all`` as a value for that parameter in this case.
        
        To view which AWS accounts have access to copy or restore a manual DB cluster snapshot, or whether a manual DB cluster snapshot public or private, use the  DescribeDBClusterSnapshotAttributes API action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/ModifyDBClusterSnapshotAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_db_cluster_snapshot_attribute(
              DBClusterSnapshotIdentifier=\'string\',
              AttributeName=\'string\',
              ValuesToAdd=[
                  \'string\',
              ],
              ValuesToRemove=[
                  \'string\',
              ]
          )
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
        
          To authorize other AWS accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more AWS account IDs, or ``all`` to make the manual DB cluster snapshot restorable by any AWS account. Do not add the ``all`` value for any manual DB cluster snapshots that contain private information that you don\'t want available to all AWS accounts.
        
          - *(string) --* 
        
        :type ValuesToRemove: list
        :param ValuesToRemove: 
        
          A list of DB cluster snapshot attributes to remove from the attribute specified by ``AttributeName`` .
        
          To remove authorization for other AWS accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more AWS account identifiers, or ``all`` to remove authorization for any AWS account to copy or restore the DB cluster snapshot. If you specify ``all`` , an AWS account whose account ID is explicitly added to the ``restore`` attribute can still copy or restore a manual DB cluster snapshot.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBClusterSnapshotAttributesResult\': {
                    \'DBClusterSnapshotIdentifier\': \'string\',
                    \'DBClusterSnapshotAttributes\': [
                        {
                            \'AttributeName\': \'string\',
                            \'AttributeValues\': [
                                \'string\',
                            ]
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBClusterSnapshotAttributesResult** *(dict) --* 
        
              Contains the results of a successful call to the  DescribeDBClusterSnapshotAttributes API action.
        
              Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or restore a manual DB cluster snapshot. For more information, see the  ModifyDBClusterSnapshotAttribute API action.
        
              - **DBClusterSnapshotIdentifier** *(string) --* 
        
                The identifier of the manual DB cluster snapshot that the attributes apply to.
        
              - **DBClusterSnapshotAttributes** *(list) --* 
        
                The list of attributes and values for the manual DB cluster snapshot.
        
                - *(dict) --* 
        
                  Contains the name and values of a manual DB cluster snapshot attribute.
        
                  Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore a manual DB cluster snapshot. For more information, see the  ModifyDBClusterSnapshotAttribute API action.
        
                  - **AttributeName** *(string) --* 
        
                    The name of the manual DB cluster snapshot attribute.
        
                    The attribute named ``restore`` refers to the list of AWS accounts that have permission to copy or restore the manual DB cluster snapshot. For more information, see the  ModifyDBClusterSnapshotAttribute API action.
        
                  - **AttributeValues** *(list) --* 
        
                    The value(s) for the manual DB cluster snapshot attribute.
        
                    If the ``AttributeName`` field is set to ``restore`` , then this element returns a list of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is public and available for any AWS account to copy or restore.
        
                    - *(string) --* 
                
        """
        pass

    def modify_db_instance(self, DBInstanceIdentifier: str, AllocatedStorage: int = None, DBInstanceClass: str = None, DBSubnetGroupName: str = None, DBSecurityGroups: List = None, VpcSecurityGroupIds: List = None, ApplyImmediately: bool = None, MasterUserPassword: str = None, DBParameterGroupName: str = None, BackupRetentionPeriod: int = None, PreferredBackupWindow: str = None, PreferredMaintenanceWindow: str = None, MultiAZ: bool = None, EngineVersion: str = None, AllowMajorVersionUpgrade: bool = None, AutoMinorVersionUpgrade: bool = None, LicenseModel: str = None, Iops: int = None, OptionGroupName: str = None, NewDBInstanceIdentifier: str = None, StorageType: str = None, TdeCredentialArn: str = None, TdeCredentialPassword: str = None, CACertificateIdentifier: str = None, Domain: str = None, CopyTagsToSnapshot: bool = None, MonitoringInterval: int = None, DBPortNumber: int = None, PubliclyAccessible: bool = None, MonitoringRoleArn: str = None, DomainIAMRoleName: str = None, PromotionTier: int = None, EnableIAMDatabaseAuthentication: bool = None, EnablePerformanceInsights: bool = None, PerformanceInsightsKMSKeyId: str = None, CloudwatchLogsExportConfiguration: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/ModifyDBInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_db_instance(
              DBInstanceIdentifier=\'string\',
              AllocatedStorage=123,
              DBInstanceClass=\'string\',
              DBSubnetGroupName=\'string\',
              DBSecurityGroups=[
                  \'string\',
              ],
              VpcSecurityGroupIds=[
                  \'string\',
              ],
              ApplyImmediately=True|False,
              MasterUserPassword=\'string\',
              DBParameterGroupName=\'string\',
              BackupRetentionPeriod=123,
              PreferredBackupWindow=\'string\',
              PreferredMaintenanceWindow=\'string\',
              MultiAZ=True|False,
              EngineVersion=\'string\',
              AllowMajorVersionUpgrade=True|False,
              AutoMinorVersionUpgrade=True|False,
              LicenseModel=\'string\',
              Iops=123,
              OptionGroupName=\'string\',
              NewDBInstanceIdentifier=\'string\',
              StorageType=\'string\',
              TdeCredentialArn=\'string\',
              TdeCredentialPassword=\'string\',
              CACertificateIdentifier=\'string\',
              Domain=\'string\',
              CopyTagsToSnapshot=True|False,
              MonitoringInterval=123,
              DBPortNumber=123,
              PubliclyAccessible=True|False,
              MonitoringRoleArn=\'string\',
              DomainIAMRoleName=\'string\',
              PromotionTier=123,
              EnableIAMDatabaseAuthentication=True|False,
              EnablePerformanceInsights=True|False,
              PerformanceInsightsKMSKeyId=\'string\',
              CloudwatchLogsExportConfiguration={
                  \'EnableLogTypes\': [
                      \'string\',
                  ],
                  \'DisableLogTypes\': [
                      \'string\',
                  ]
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: **[REQUIRED]** 
        
          The DB instance identifier. This value is stored as a lowercase string.
        
          Constraints:
        
          * Must match the identifier of an existing DBInstance. 
           
        :type AllocatedStorage: integer
        :param AllocatedStorage: 
        
          The new amount of storage (in gibibytes) to allocate for the DB instance. 
        
          Not applicable. Storage is managed by the DB Cluster.
        
        :type DBInstanceClass: string
        :param DBInstanceClass: 
        
          The new compute and memory capacity of the DB instance, for example, ``db.m4.large`` . Not all DB instance classes are available in all AWS Regions. 
        
          If you modify the DB instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless ``ApplyImmediately`` is specified as ``true`` for this request. 
        
          Default: Uses existing setting
        
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName: 
        
          The new DB subnet group for the DB instance. You can use this parameter to move your DB instance to a different VPC. 
        
          Changing the subnet group causes an outage during the change. The change is applied during the next maintenance window, unless you specify ``true`` for the ``ApplyImmediately`` parameter. 
        
          Constraints: If supplied, must match the name of an existing DBSubnetGroup.
        
          Example: ``mySubnetGroup``  
        
        :type DBSecurityGroups: list
        :param DBSecurityGroups: 
        
          A list of DB security groups to authorize on this DB instance. Changing this setting doesn\'t result in an outage and the change is asynchronously applied as soon as possible.
        
          Constraints:
        
          * If supplied, must match existing DBSecurityGroups. 
           
          - *(string) --* 
        
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds: 
        
          A list of EC2 VPC security groups to authorize on this DB instance. This change is asynchronously applied as soon as possible.
        
          Not applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see  ModifyDBCluster .
        
          Constraints:
        
          * If supplied, must match existing VpcSecurityGroupIds. 
           
          - *(string) --* 
        
        :type ApplyImmediately: boolean
        :param ApplyImmediately: 
        
          Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the ``PreferredMaintenanceWindow`` setting for the DB instance. 
        
          If this parameter is set to ``false`` , changes to the DB instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next call to  RebootDBInstance , or the next failure reboot. 
        
          Default: ``false``  
        
        :type MasterUserPassword: string
        :param MasterUserPassword: 
        
          The new password for the master user. The password can include any printable ASCII character except \"/\", \"\"\", or \"@\".
        
          Not applicable. 
        
          Default: Uses existing setting
        
        :type DBParameterGroupName: string
        :param DBParameterGroupName: 
        
          The name of the DB parameter group to apply to the DB instance. Changing this setting doesn\'t result in an outage. The parameter group name itself is changed immediately, but the actual parameter changes are not applied until you reboot the instance without failover. The db instance will NOT be rebooted automatically and the parameter changes will NOT be applied during the next maintenance window.
        
          Default: Uses existing setting
        
          Constraints: The DB parameter group must be in the same DB parameter group family as this DB instance.
        
        :type BackupRetentionPeriod: integer
        :param BackupRetentionPeriod: 
        
          The number of days to retain automated backups. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.
        
          Not applicable. The retention period for automated backups is managed by the DB cluster. For more information, see  ModifyDBCluster .
        
          Default: Uses existing setting
        
        :type PreferredBackupWindow: string
        :param PreferredBackupWindow: 
        
          The daily time range during which automated backups are created if automated backups are enabled. 
        
          Not applicable. The daily time range for creating automated backups is managed by the DB cluster. For more information, see  ModifyDBCluster .
        
          Constraints:
        
          * Must be in the format hh24:mi-hh24:mi 
           
          * Must be in Universal Time Coordinated (UTC) 
           
          * Must not conflict with the preferred maintenance window 
           
          * Must be at least 30 minutes 
           
        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow: 
        
          The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter doesn\'t result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, then changing this parameter will cause a reboot of the DB instance. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.
        
          Default: Uses existing setting
        
          Format: ddd:hh24:mi-ddd:hh24:mi
        
          Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
        
          Constraints: Must be at least 30 minutes
        
        :type MultiAZ: boolean
        :param MultiAZ: 
        
          Specifies if the DB instance is a Multi-AZ deployment. Changing this parameter doesn\'t result in an outage and the change is applied during the next maintenance window unless the ``ApplyImmediately`` parameter is set to ``true`` for this request. 
        
        :type EngineVersion: string
        :param EngineVersion: 
        
          The version number of the database engine to upgrade to. Changing this parameter results in an outage and the change is applied during the next maintenance window unless the ``ApplyImmediately`` parameter is set to ``true`` for this request. 
        
          For major version upgrades, if a nondefault DB parameter group is currently in use, a new DB parameter group in the DB parameter group family for the new engine version must be specified. The new DB parameter group can be the default for that DB parameter group family.
        
        :type AllowMajorVersionUpgrade: boolean
        :param AllowMajorVersionUpgrade: 
        
          Indicates that major version upgrades are allowed. Changing this parameter doesn\'t result in an outage and the change is asynchronously applied as soon as possible.
        
          Constraints: This parameter must be set to true when specifying a value for the EngineVersion parameter that is a different major version than the DB instance\'s current version.
        
        :type AutoMinorVersionUpgrade: boolean
        :param AutoMinorVersionUpgrade: 
        
          Indicates that minor version upgrades are applied automatically to the DB instance during the maintenance window. Changing this parameter doesn\'t result in an outage except in the following case and the change is asynchronously applied as soon as possible. An outage will result if this parameter is set to ``true`` during the maintenance window, and a newer minor version is available, and Neptune has enabled auto patching for that engine version. 
        
        :type LicenseModel: string
        :param LicenseModel: 
        
          The license model for the DB instance.
        
          Valid values: ``license-included`` | ``bring-your-own-license`` | ``general-public-license``  
        
        :type Iops: integer
        :param Iops: 
        
          The new Provisioned IOPS (I/O operations per second) value for the instance. 
        
          Changing this setting doesn\'t result in an outage and the change is applied during the next maintenance window unless the ``ApplyImmediately`` parameter is set to ``true`` for this request.
        
          Default: Uses existing setting
        
        :type OptionGroupName: string
        :param OptionGroupName: 
        
          Indicates that the DB instance should be associated with the specified option group. Changing this parameter doesn\'t result in an outage except in the following case and the change is applied during the next maintenance window unless the ``ApplyImmediately`` parameter is set to ``true`` for this request. If the parameter change results in an option group that enables OEM, this change can cause a brief (sub-second) period during which new connections are rejected but existing connections are not interrupted. 
        
          Permanent options, such as the TDE option for Oracle Advanced Security TDE, can\'t be removed from an option group, and that option group can\'t be removed from a DB instance once it is associated with a DB instance
        
        :type NewDBInstanceIdentifier: string
        :param NewDBInstanceIdentifier: 
        
          The new DB instance identifier for the DB instance when renaming a DB instance. When you change the DB instance identifier, an instance reboot will occur immediately if you set ``Apply Immediately`` to true, or will occur during the next maintenance window if ``Apply Immediately`` to false. This value is stored as a lowercase string. 
        
          Constraints:
        
          * Must contain from 1 to 63 letters, numbers, or hyphens. 
           
          * The first character must be a letter. 
           
          * Cannot end with a hyphen or contain two consecutive hyphens. 
           
          Example: ``mydbinstance``  
        
        :type StorageType: string
        :param StorageType: 
        
          Specifies the storage type to be associated with the DB instance. 
        
          If you specify Provisioned IOPS (``io1`` ), you must also include a value for the ``Iops`` parameter. 
        
          If you choose to migrate your DB instance from using standard storage to using Provisioned IOPS, or from using Provisioned IOPS to using standard storage, the process can take time. The duration of the migration depends on several factors such as database load, storage size, storage type (standard or Provisioned IOPS), amount of IOPS provisioned (if any), and the number of prior scale storage operations. Typical migration times are under 24 hours, but the process can take up to several days in some cases. During the migration, the DB instance is available for use, but might experience performance degradation. While the migration takes place, nightly backups for the instance are suspended. No other Amazon Neptune operations can take place for the instance, including modifying the instance, rebooting the instance, deleting the instance, creating a Read Replica for the instance, and creating a DB snapshot of the instance. 
        
          Valid values: ``standard | gp2 | io1``  
        
          Default: ``io1`` if the ``Iops`` parameter is specified, otherwise ``standard``  
        
        :type TdeCredentialArn: string
        :param TdeCredentialArn: 
        
          The ARN from the key store with which to associate the instance for TDE encryption.
        
        :type TdeCredentialPassword: string
        :param TdeCredentialPassword: 
        
          The password for the given ARN from the key store in order to access the device.
        
        :type CACertificateIdentifier: string
        :param CACertificateIdentifier: 
        
          Indicates the certificate that needs to be associated with the instance.
        
        :type Domain: string
        :param Domain: 
        
          Not supported. 
        
        :type CopyTagsToSnapshot: boolean
        :param CopyTagsToSnapshot: 
        
          True to copy all tags from the DB instance to snapshots of the DB instance, and otherwise false. The default is false.
        
        :type MonitoringInterval: integer
        :param MonitoringInterval: 
        
          The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
        
          If ``MonitoringRoleArn`` is specified, then you must also set ``MonitoringInterval`` to a value other than 0.
        
          Valid Values: ``0, 1, 5, 10, 15, 30, 60``  
        
        :type DBPortNumber: integer
        :param DBPortNumber: 
        
          The port number on which the database accepts connections.
        
          The value of the ``DBPortNumber`` parameter must not match any of the port values specified for options in the option group for the DB instance.
        
          Your database will restart when you change the ``DBPortNumber`` value regardless of the value of the ``ApplyImmediately`` parameter.
        
          Default: ``8182``  
        
        :type PubliclyAccessible: boolean
        :param PubliclyAccessible: 
        
          This parameter is not supported.
        
        :type MonitoringRoleArn: string
        :param MonitoringRoleArn: 
        
          The ARN for the IAM role that permits Neptune to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, ``arn:aws:iam:123456789012:role/emaccess`` . 
        
          If ``MonitoringInterval`` is set to a value other than 0, then you must supply a ``MonitoringRoleArn`` value.
        
        :type DomainIAMRoleName: string
        :param DomainIAMRoleName: 
        
          Not supported
        
        :type PromotionTier: integer
        :param PromotionTier: 
        
          A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance. 
        
          Default: 1
        
          Valid Values: 0 - 15
        
        :type EnableIAMDatabaseAuthentication: boolean
        :param EnableIAMDatabaseAuthentication: 
        
          True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.
        
          You can enable IAM database authentication for the following database engines
        
          Not applicable. Mapping AWS IAM accounts to database accounts is managed by the DB cluster. For more information, see  ModifyDBCluster .
        
          Default: ``false``  
        
        :type EnablePerformanceInsights: boolean
        :param EnablePerformanceInsights: 
        
          True to enable Performance Insights for the DB instance, and otherwise false.
        
        :type PerformanceInsightsKMSKeyId: string
        :param PerformanceInsightsKMSKeyId: 
        
          The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.
        
        :type CloudwatchLogsExportConfiguration: dict
        :param CloudwatchLogsExportConfiguration: 
        
          The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB instance or DB cluster.
        
          - **EnableLogTypes** *(list) --* 
        
            The list of log types to enable.
        
            - *(string) --* 
        
          - **DisableLogTypes** *(list) --* 
        
            The list of log types to disable.
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBInstance\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBInstance** *(dict) --* 
        
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
            
        """
        pass

    def modify_db_parameter_group(self, DBParameterGroupName: str, Parameters: List) -> Dict:
        """
        
        .. note::
        
          Changes to dynamic parameters are applied immediately. Changes to static parameters require a reboot without failover to the DB instance associated with the parameter group before the change can take effect.
        
        .. warning::
        
          After you modify a DB parameter group, you should wait at least 5 minutes before creating your first DB instance that uses that DB parameter group as the default parameter group. This allows Amazon Neptune to fully complete the modify action before the parameter group is used as the default for a new DB instance. This is especially important for parameters that are critical when creating the default database for a DB instance, such as the character set for the default database defined by the ``character_set_database`` parameter. You can use the *Parameter Groups* option of the Amazon Neptune console or the *DescribeDBParameters* command to verify that your DB parameter group has been created or modified.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/ModifyDBParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_db_parameter_group(
              DBParameterGroupName=\'string\',
              Parameters=[
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
          )
        :type DBParameterGroupName: string
        :param DBParameterGroupName: **[REQUIRED]** 
        
          The name of the DB parameter group.
        
          Constraints:
        
          * If supplied, must match the name of an existing DBParameterGroup. 
           
        :type Parameters: list
        :param Parameters: **[REQUIRED]** 
        
          An array of parameter names, values, and the apply method for the parameter update. At least one parameter name, value, and apply method must be supplied; subsequent arguments are optional. A maximum of 20 parameters can be modified in a single request.
        
          Valid Values (for the application method): ``immediate | pending-reboot``  
        
          .. note::
        
            You can use the immediate value with dynamic parameters only. You can use the pending-reboot value for both dynamic and static parameters, and changes are applied when you reboot the DB instance without failover.
        
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
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBParameterGroupName\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  ModifyDBParameterGroup or  ResetDBParameterGroup action. 
        
            - **DBParameterGroupName** *(string) --* 
        
              Provides the name of the DB parameter group.
        
        """
        pass

    def modify_db_subnet_group(self, DBSubnetGroupName: str, SubnetIds: List, DBSubnetGroupDescription: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/ModifyDBSubnetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_db_subnet_group(
              DBSubnetGroupName=\'string\',
              DBSubnetGroupDescription=\'string\',
              SubnetIds=[
                  \'string\',
              ]
          )
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName: **[REQUIRED]** 
        
          The name for the DB subnet group. This value is stored as a lowercase string. You can\'t modify the default subnet group. 
        
          Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.
        
          Example: ``mySubnetgroup``  
        
        :type DBSubnetGroupDescription: string
        :param DBSubnetGroupDescription: 
        
          The description for the DB subnet group.
        
        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]** 
        
          The EC2 subnet IDs for the DB subnet group.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBSubnetGroup** *(dict) --* 
        
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
        
        """
        pass

    def modify_event_subscription(self, SubscriptionName: str, SnsTopicArn: str = None, SourceType: str = None, EventCategories: List = None, Enabled: bool = None) -> Dict:
        """
        
        You can see a list of the event categories for a given SourceType by using the **DescribeEventCategories** action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/ModifyEventSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_event_subscription(
              SubscriptionName=\'string\',
              SnsTopicArn=\'string\',
              SourceType=\'string\',
              EventCategories=[
                  \'string\',
              ],
              Enabled=True|False
          )
        :type SubscriptionName: string
        :param SubscriptionName: **[REQUIRED]** 
        
          The name of the event notification subscription.
        
        :type SnsTopicArn: string
        :param SnsTopicArn: 
        
          The Amazon Resource Name (ARN) of the SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
        
        :type SourceType: string
        :param SourceType: 
        
          The type of source that is generating the events. For example, if you want to be notified of events generated by a DB instance, you would set this parameter to db-instance. if this value is not specified, all events are returned.
        
          Valid values: db-instance | db-parameter-group | db-security-group | db-snapshot
        
        :type EventCategories: list
        :param EventCategories: 
        
          A list of event categories for a SourceType that you want to subscribe to. You can see a list of the categories for a given SourceType by using the **DescribeEventCategories** action. 
        
          - *(string) --* 
        
        :type Enabled: boolean
        :param Enabled: 
        
          A Boolean value; set to **true** to activate the subscription. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EventSubscription\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EventSubscription** *(dict) --* 
        
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
        
        """
        pass

    def promote_read_replica_db_cluster(self, DBClusterIdentifier: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/PromoteReadReplicaDBCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.promote_read_replica_db_cluster(
              DBClusterIdentifier=\'string\'
          )
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]** 
        
          The identifier of the DB cluster Read Replica to promote. This parameter is not case-sensitive. 
        
          Constraints:
        
          * Must match the identifier of an existing DBCluster Read Replica. 
           
          Example: ``my-cluster-replica1``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBCluster\': {
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
                            \'Status\': \'string\'
                        },
                    ],
                    \'IAMDatabaseAuthenticationEnabled\': True|False,
                    \'CloneGroupId\': \'string\',
                    \'ClusterCreateTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBCluster** *(dict) --* 
        
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
        
        """
        pass

    def reboot_db_instance(self, DBInstanceIdentifier: str, ForceFailover: bool = None) -> Dict:
        """
        
        Rebooting a DB instance restarts the database engine service. Rebooting a DB instance results in a momentary outage, during which the DB instance status is set to rebooting. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/RebootDBInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.reboot_db_instance(
              DBInstanceIdentifier=\'string\',
              ForceFailover=True|False
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier: **[REQUIRED]** 
        
          The DB instance identifier. This parameter is stored as a lowercase string.
        
          Constraints:
        
          * Must match the identifier of an existing DBInstance. 
           
        :type ForceFailover: boolean
        :param ForceFailover: 
        
          When ``true`` , the reboot is conducted through a MultiAZ failover. 
        
          Constraint: You can\'t specify ``true`` if the instance is not configured for MultiAZ.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBInstance\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBInstance** *(dict) --* 
        
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
            
        """
        pass

    def remove_role_from_db_cluster(self, DBClusterIdentifier: str, RoleArn: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/RemoveRoleFromDBCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_role_from_db_cluster(
              DBClusterIdentifier=\'string\',
              RoleArn=\'string\'
          )
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]** 
        
          The name of the DB cluster to disassociate the IAM role from.
        
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the IAM role to disassociate from the DB cluster, for example ``arn:aws:iam::123456789012:role/NeptuneAccessRole`` .
        
        :returns: None
        """
        pass

    def remove_source_identifier_from_subscription(self, SubscriptionName: str, SourceIdentifier: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/RemoveSourceIdentifierFromSubscription>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_source_identifier_from_subscription(
              SubscriptionName=\'string\',
              SourceIdentifier=\'string\'
          )
        :type SubscriptionName: string
        :param SubscriptionName: **[REQUIRED]** 
        
          The name of the event notification subscription you want to remove a source identifier from.
        
        :type SourceIdentifier: string
        :param SourceIdentifier: **[REQUIRED]** 
        
          The source identifier to be removed from the subscription, such as the **DB instance identifier** for a DB instance or the name of a security group. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'EventSubscription\': {
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
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EventSubscription** *(dict) --* 
        
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
        
        """
        pass

    def remove_tags_from_resource(self, ResourceName: str, TagKeys: List) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/RemoveTagsFromResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_tags_from_resource(
              ResourceName=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type ResourceName: string
        :param ResourceName: **[REQUIRED]** 
        
          The Amazon Neptune resource that the tags are removed from. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see `Constructing an Amazon Resource Name (ARN) <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing>`__ .
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          The tag key (name) of the tag to be removed.
        
          - *(string) --* 
        
        :returns: None
        """
        pass

    def reset_db_cluster_parameter_group(self, DBClusterParameterGroupName: str, ResetAllParameters: bool = None, Parameters: List = None) -> Dict:
        """
        
        When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to ``pending-reboot`` to take effect on the next DB instance restart or  RebootDBInstance request. You must call  RebootDBInstance for every DB instance in your DB cluster that you want the updated static parameter to apply to.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/ResetDBClusterParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.reset_db_cluster_parameter_group(
              DBClusterParameterGroupName=\'string\',
              ResetAllParameters=True|False,
              Parameters=[
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
          )
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
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBClusterParameterGroupName\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            - **DBClusterParameterGroupName** *(string) --* 
        
              The name of the DB cluster parameter group.
        
              Constraints:
        
              * Must be 1 to 255 letters or numbers. 
               
              * First character must be a letter 
               
              * Cannot end with a hyphen or contain two consecutive hyphens 
               
              .. note::
        
                This value is stored as a lowercase string.
        
        """
        pass

    def reset_db_parameter_group(self, DBParameterGroupName: str, ResetAllParameters: bool = None, Parameters: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/ResetDBParameterGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.reset_db_parameter_group(
              DBParameterGroupName=\'string\',
              ResetAllParameters=True|False,
              Parameters=[
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
          )
        :type DBParameterGroupName: string
        :param DBParameterGroupName: **[REQUIRED]** 
        
          The name of the DB parameter group.
        
          Constraints:
        
          * Must match the name of an existing DBParameterGroup. 
           
        :type ResetAllParameters: boolean
        :param ResetAllParameters: 
        
          Specifies whether (``true`` ) or not (``false`` ) to reset all parameters in the DB parameter group to default values. 
        
          Default: ``true``  
        
        :type Parameters: list
        :param Parameters: 
        
          To reset the entire DB parameter group, specify the ``DBParameterGroup`` name and ``ResetAllParameters`` parameters. To reset specific parameters, provide a list of the following: ``ParameterName`` and ``ApplyMethod`` . A maximum of 20 parameters can be modified in a single request.
        
          Valid Values (for Apply method): ``pending-reboot``  
        
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
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBParameterGroupName\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the result of a successful invocation of the  ModifyDBParameterGroup or  ResetDBParameterGroup action. 
        
            - **DBParameterGroupName** *(string) --* 
        
              Provides the name of the DB parameter group.
        
        """
        pass

    def restore_db_cluster_from_snapshot(self, DBClusterIdentifier: str, SnapshotIdentifier: str, Engine: str, AvailabilityZones: List = None, EngineVersion: str = None, Port: int = None, DBSubnetGroupName: str = None, DatabaseName: str = None, OptionGroupName: str = None, VpcSecurityGroupIds: List = None, Tags: List = None, KmsKeyId: str = None, EnableIAMDatabaseAuthentication: bool = None) -> Dict:
        """
        
        If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.
        
        If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/RestoreDBClusterFromSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.restore_db_cluster_from_snapshot(
              AvailabilityZones=[
                  \'string\',
              ],
              DBClusterIdentifier=\'string\',
              SnapshotIdentifier=\'string\',
              Engine=\'string\',
              EngineVersion=\'string\',
              Port=123,
              DBSubnetGroupName=\'string\',
              DatabaseName=\'string\',
              OptionGroupName=\'string\',
              VpcSecurityGroupIds=[
                  \'string\',
              ],
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              KmsKeyId=\'string\',
              EnableIAMDatabaseAuthentication=True|False
          )
        :type AvailabilityZones: list
        :param AvailabilityZones: 
        
          Provides the list of EC2 Availability Zones that instances in the restored DB cluster can be created in.
        
          - *(string) --* 
        
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]** 
        
          The name of the DB cluster to create from the DB snapshot or DB cluster snapshot. This parameter isn\'t case-sensitive.
        
          Constraints:
        
          * Must contain from 1 to 63 letters, numbers, or hyphens 
           
          * First character must be a letter 
           
          * Cannot end with a hyphen or contain two consecutive hyphens 
           
          Example: ``my-snapshot-id``  
        
        :type SnapshotIdentifier: string
        :param SnapshotIdentifier: **[REQUIRED]** 
        
          The identifier for the DB snapshot or DB cluster snapshot to restore from.
        
          You can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.
        
          Constraints:
        
          * Must match the identifier of an existing Snapshot. 
           
        :type Engine: string
        :param Engine: **[REQUIRED]** 
        
          The database engine to use for the new DB cluster.
        
          Default: The same as source
        
          Constraint: Must be compatible with the engine of the source
        
        :type EngineVersion: string
        :param EngineVersion: 
        
          The version of the database engine to use for the new DB cluster.
        
        :type Port: integer
        :param Port: 
        
          The port number on which the new DB cluster accepts connections.
        
          Constraints: Value must be ``1150-65535``  
        
          Default: The same port as the original DB cluster.
        
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName: 
        
          The name of the DB subnet group to use for the new DB cluster.
        
          Constraints: If supplied, must match the name of an existing DBSubnetGroup.
        
          Example: ``mySubnetgroup``  
        
        :type DatabaseName: string
        :param DatabaseName: 
        
          The database name for the restored DB cluster.
        
        :type OptionGroupName: string
        :param OptionGroupName: 
        
          The name of the option group to use for the restored DB cluster.
        
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds: 
        
          A list of VPC security groups that the new DB cluster will belong to.
        
          - *(string) --* 
        
        :type Tags: list
        :param Tags: 
        
          The tags to be assigned to the restored DB cluster.
        
          - *(dict) --* 
        
            Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          The AWS KMS key identifier to use when restoring an encrypted DB cluster from a DB snapshot or DB cluster snapshot.
        
          The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a DB cluster with the same AWS account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.
        
          If you do not specify a value for the ``KmsKeyId`` parameter, then the following will occur:
        
          * If the DB snapshot or DB cluster snapshot in ``SnapshotIdentifier`` is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the DB snapshot or DB cluster snapshot. 
           
          * If the DB snapshot or DB cluster snapshot in ``SnapshotIdentifier`` is not encrypted, then the restored DB cluster is not encrypted. 
           
        :type EnableIAMDatabaseAuthentication: boolean
        :param EnableIAMDatabaseAuthentication: 
        
          True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.
        
          Default: ``false``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBCluster\': {
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
                            \'Status\': \'string\'
                        },
                    ],
                    \'IAMDatabaseAuthenticationEnabled\': True|False,
                    \'CloneGroupId\': \'string\',
                    \'ClusterCreateTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBCluster** *(dict) --* 
        
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
        
        """
        pass

    def restore_db_cluster_to_point_in_time(self, DBClusterIdentifier: str, SourceDBClusterIdentifier: str, RestoreType: str = None, RestoreToTime: datetime = None, UseLatestRestorableTime: bool = None, Port: int = None, DBSubnetGroupName: str = None, OptionGroupName: str = None, VpcSecurityGroupIds: List = None, Tags: List = None, KmsKeyId: str = None, EnableIAMDatabaseAuthentication: bool = None) -> Dict:
        """
        
        .. note::
        
          This action only restores the DB cluster, not the DB instances for that DB cluster. You must invoke the  CreateDBInstance action to create DB instances for the restored DB cluster, specifying the identifier of the restored DB cluster in ``DBClusterIdentifier`` . You can create DB instances only after the ``RestoreDBClusterToPointInTime`` action has completed and the DB cluster is available.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/RestoreDBClusterToPointInTime>`_
        
        **Request Syntax** 
        ::
        
          response = client.restore_db_cluster_to_point_in_time(
              DBClusterIdentifier=\'string\',
              RestoreType=\'string\',
              SourceDBClusterIdentifier=\'string\',
              RestoreToTime=datetime(2015, 1, 1),
              UseLatestRestorableTime=True|False,
              Port=123,
              DBSubnetGroupName=\'string\',
              OptionGroupName=\'string\',
              VpcSecurityGroupIds=[
                  \'string\',
              ],
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              KmsKeyId=\'string\',
              EnableIAMDatabaseAuthentication=True|False
          )
        :type DBClusterIdentifier: string
        :param DBClusterIdentifier: **[REQUIRED]** 
        
          The name of the new DB cluster to be created.
        
          Constraints:
        
          * Must contain from 1 to 63 letters, numbers, or hyphens 
           
          * First character must be a letter 
           
          * Cannot end with a hyphen or contain two consecutive hyphens 
           
        :type RestoreType: string
        :param RestoreType: 
        
          The type of restore to be performed. You can specify one of the following values:
        
          * ``full-copy`` - The new DB cluster is restored as a full copy of the source DB cluster. 
           
          * ``copy-on-write`` - The new DB cluster is restored as a clone of the source DB cluster. 
           
          Constraints: You can\'t specify ``copy-on-write`` if the engine version of the source DB cluster is earlier than 1.11.
        
          If you don\'t specify a ``RestoreType`` value, then the new DB cluster is restored as a full copy of the source DB cluster.
        
        :type SourceDBClusterIdentifier: string
        :param SourceDBClusterIdentifier: **[REQUIRED]** 
        
          The identifier of the source DB cluster from which to restore.
        
          Constraints:
        
          * Must match the identifier of an existing DBCluster. 
           
        :type RestoreToTime: datetime
        :param RestoreToTime: 
        
          The date and time to restore the DB cluster to.
        
          Valid Values: Value must be a time in Universal Coordinated Time (UTC) format
        
          Constraints:
        
          * Must be before the latest restorable time for the DB instance 
           
          * Must be specified if ``UseLatestRestorableTime`` parameter is not provided 
           
          * Cannot be specified if ``UseLatestRestorableTime`` parameter is true 
           
          * Cannot be specified if ``RestoreType`` parameter is ``copy-on-write``   
           
          Example: ``2015-03-07T23:45:00Z``  
        
        :type UseLatestRestorableTime: boolean
        :param UseLatestRestorableTime: 
        
          A value that is set to ``true`` to restore the DB cluster to the latest restorable backup time, and ``false`` otherwise. 
        
          Default: ``false``  
        
          Constraints: Cannot be specified if ``RestoreToTime`` parameter is provided.
        
        :type Port: integer
        :param Port: 
        
          The port number on which the new DB cluster accepts connections.
        
          Constraints: Value must be ``1150-65535``  
        
          Default: The same port as the original DB cluster.
        
        :type DBSubnetGroupName: string
        :param DBSubnetGroupName: 
        
          The DB subnet group name to use for the new DB cluster.
        
          Constraints: If supplied, must match the name of an existing DBSubnetGroup.
        
          Example: ``mySubnetgroup``  
        
        :type OptionGroupName: string
        :param OptionGroupName: 
        
          The name of the option group for the new DB cluster.
        
        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds: 
        
          A list of VPC security groups that the new DB cluster belongs to.
        
          - *(string) --* 
        
        :type Tags: list
        :param Tags: 
        
          A list of tags. For more information, see `Tagging Amazon Neptune Resources <http://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html>`__ . 
        
          - *(dict) --* 
        
            Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
        
            - **Key** *(string) --* 
        
              A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
            - **Value** *(string) --* 
        
              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with \"aws:\" or \"rds:\". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: \"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$\").
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          The AWS KMS key identifier to use when restoring an encrypted DB cluster from an encrypted DB cluster.
        
          The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a DB cluster with the same AWS account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.
        
          You can restore to a new DB cluster and encrypt the new DB cluster with a KMS key that is different than the KMS key used to encrypt the source DB cluster. The new DB cluster is encrypted with the KMS key identified by the ``KmsKeyId`` parameter.
        
          If you do not specify a value for the ``KmsKeyId`` parameter, then the following will occur:
        
          * If the DB cluster is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the source DB cluster. 
           
          * If the DB cluster is not encrypted, then the restored DB cluster is not encrypted. 
           
          If ``DBClusterIdentifier`` refers to a DB cluster that is not encrypted, then the restore request is rejected.
        
        :type EnableIAMDatabaseAuthentication: boolean
        :param EnableIAMDatabaseAuthentication: 
        
          True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.
        
          Default: ``false``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DBCluster\': {
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
                            \'Status\': \'string\'
                        },
                    ],
                    \'IAMDatabaseAuthenticationEnabled\': True|False,
                    \'CloneGroupId\': \'string\',
                    \'ClusterCreateTime\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DBCluster** *(dict) --* 
        
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
        
        """
        pass
