from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from datetime import datetime
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
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

    def create_backup_plan(self, BackupPlan: Dict, BackupPlanTags: Dict = None, CreatorRequestId: str = None) -> Dict:
        """
        Backup plans are documents that contain information that AWS Backup uses to schedule tasks that create recovery points of resources.
        If you call ``CreateBackupPlan`` with a plan that already exists, the existing ``backupPlanId`` is returned.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/CreateBackupPlan>`_
        
        **Request Syntax**
        ::
          response = client.create_backup_plan(
              BackupPlan={
                  'BackupPlanName': 'string',
                  'Rules': [
                      {
                          'RuleName': 'string',
                          'TargetBackupVaultName': 'string',
                          'ScheduleExpression': 'string',
                          'StartWindowMinutes': 123,
                          'CompletionWindowMinutes': 123,
                          'Lifecycle': {
                              'MoveToColdStorageAfterDays': 123,
                              'DeleteAfterDays': 123
                          },
                          'RecoveryPointTags': {
                              'string': 'string'
                          }
                      },
                  ]
              },
              BackupPlanTags={
                  'string': 'string'
              },
              CreatorRequestId='string'
          )
        
        **Response Syntax**
        ::
            {
                'BackupPlanId': 'string',
                'BackupPlanArn': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'VersionId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupPlanId** *(string) --* 
              Uniquely identifies a backup plan.
            - **BackupPlanArn** *(string) --* 
              An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .
            - **CreationDate** *(datetime) --* 
              The date and time that a backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **VersionId** *(string) --* 
              Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1024 bytes long. They cannot be edited.
        :type BackupPlan: dict
        :param BackupPlan: **[REQUIRED]**
          Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of ``Rules`` .
          - **BackupPlanName** *(string) --* **[REQUIRED]**
            The display name of a backup plan.
          - **Rules** *(list) --* **[REQUIRED]**
            An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used to back up a selection of resources.
            - *(dict) --*
              Specifies a scheduled task used to back up a selection of resources.
              - **RuleName** *(string) --* **[REQUIRED]**
                >An optional display name for a backup rule.
              - **TargetBackupVaultName** *(string) --* **[REQUIRED]**
                The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
              - **ScheduleExpression** *(string) --*
                A CRON expression specifying when AWS Backup initiates a backup job.
              - **StartWindowMinutes** *(integer) --*
                The amount of time in minutes before beginning a backup.
              - **CompletionWindowMinutes** *(integer) --*
                The amount of time AWS Backup attempts a backup before canceling the job and returning an error.
              - **Lifecycle** *(dict) --*
                The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup will transition and expire backups automatically according to the lifecycle that you define.
                Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold after days”. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold.
                - **MoveToColdStorageAfterDays** *(integer) --*
                  Specifies the number of days after creation that a recovery point is moved to cold storage.
                - **DeleteAfterDays** *(integer) --*
                  Specifies the number of days after creation that a recovery point is deleted. Must be greater than ``MoveToColdStorageAfterDays`` .
              - **RecoveryPointTags** *(dict) --*
                To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair.
                - *(string) --*
                  - *(string) --*
        :type BackupPlanTags: dict
        :param BackupPlanTags:
          To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair. The specified tags are assigned to all backups created with this plan.
          - *(string) --*
            - *(string) --*
        :type CreatorRequestId: string
        :param CreatorRequestId:
          Identifies the request and allows failed requests to be retried without the risk of executing the operation twice. If the request includes a ``CreatorRequestId`` that matches an existing backup plan, that plan is returned. This parameter is optional.
        :rtype: dict
        :returns:
        """
        pass

    def create_backup_selection(self, BackupPlanId: str, BackupSelection: Dict, CreatorRequestId: str = None) -> Dict:
        """
        Creates a JSON document that specifies a set of resources to assign to a backup plan. Resources can be included by specifying patterns for a ``ListOfTags`` and selected ``Resources`` . 
        For example, consider the following patterns:
        * ``Resources: "arn:aws:ec2:region:account-id:volume/volume-id"``   
        * ``ConditionKey:"department"``    ``ConditionValue:"finance"``    ``ConditionType:"StringEquals"``   
        * ``ConditionKey:"importance"``    ``ConditionValue:"critical"``    ``ConditionType:"StringEquals"``   
        Using these patterns would back up all Amazon Elastic Block Store (Amazon EBS) volumes that are tagged as ``"department=finance"`` , ``"importance=critical"`` , in addition to an EBS volume with the specified volume Id.
        Resources and conditions are additive in that all resources that match the pattern are selected. This shouldn't be confused with a logical AND, where all conditions must match. The matching patterns are logically 'put together using the OR operator. In other words, all patterns that match are selected for backup.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/CreateBackupSelection>`_
        
        **Request Syntax**
        ::
          response = client.create_backup_selection(
              BackupPlanId='string',
              BackupSelection={
                  'SelectionName': 'string',
                  'IamRoleArn': 'string',
                  'Resources': [
                      'string',
                  ],
                  'ListOfTags': [
                      {
                          'ConditionType': 'STRINGEQUALS',
                          'ConditionKey': 'string',
                          'ConditionValue': 'string'
                      },
                  ]
              },
              CreatorRequestId='string'
          )
        
        **Response Syntax**
        ::
            {
                'SelectionId': 'string',
                'BackupPlanId': 'string',
                'CreationDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SelectionId** *(string) --* 
              Uniquely identifies the body of a request to assign a set of resources to a backup plan.
            - **BackupPlanId** *(string) --* 
              Uniquely identifies a backup plan.
            - **CreationDate** *(datetime) --* 
              The date and time a backup selection is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
        :type BackupPlanId: string
        :param BackupPlanId: **[REQUIRED]**
          Uniquely identifies the backup plan to be associated with the selection of resources.
        :type BackupSelection: dict
        :param BackupSelection: **[REQUIRED]**
          Specifies the body of a request to assign a set of resources to a backup plan.
          It includes an array of resources, an optional array of patterns to exclude resources, an optional role to provide access to the AWS service the resource belongs to, and an optional array of tags used to identify a set of resources.
          - **SelectionName** *(string) --* **[REQUIRED]**
            The display name of a resource selection document.
          - **IamRoleArn** *(string) --* **[REQUIRED]**
            The ARN of the IAM role that AWS Backup uses to authenticate when restoring the target resource; for example, ``arn:aws:iam::123456789012:role/S3Access`` .
          - **Resources** *(list) --*
            An array of strings that either contain Amazon Resource Names (ARNs) or match patterns such as \"``arn:aws:ec2:us-east-1:123456789012:volume/*`` \" of resources to assign to a backup plan.
            - *(string) --*
          - **ListOfTags** *(list) --*
            An array of conditions used to specify a set of resources to assign to a backup plan; for example, ``\"StringEquals\": {\"ec2:ResourceTag/Department\": \"accounting\"`` .
            - *(dict) --*
              Contains an array of triplets made up of a condition type (such as ``StringEquals`` ), a key, and a value. Conditions are used to filter resources in a selection that is assigned to a backup plan.
              - **ConditionType** *(string) --* **[REQUIRED]**
                An operation, such as ``StringEquals`` , that is applied to a key-value pair used to filter resources in a selection.
              - **ConditionKey** *(string) --* **[REQUIRED]**
                The key in a key-value pair. For example, in ``\"ec2:ResourceTag/Department\": \"accounting\"`` , ``\"ec2:ResourceTag/Department\"`` is the key.
              - **ConditionValue** *(string) --* **[REQUIRED]**
                The value in a key-value pair. For example, in ``\"ec2:ResourceTag/Department\": \"accounting\"`` , ``\"accounting\"`` is the value.
        :type CreatorRequestId: string
        :param CreatorRequestId:
          A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.
        :rtype: dict
        :returns:
        """
        pass

    def create_backup_vault(self, BackupVaultName: str, BackupVaultTags: Dict = None, EncryptionKeyArn: str = None, CreatorRequestId: str = None) -> Dict:
        """
        Creates a logical container where backups are stored. A ``CreateBackupVault`` request includes a name, optionally one or more resource tags, an encryption key, and a request ID.
        .. note::
          Sensitive data, such as passport numbers, should not be included the name of a backup vault.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/CreateBackupVault>`_
        
        **Request Syntax**
        ::
          response = client.create_backup_vault(
              BackupVaultName='string',
              BackupVaultTags={
                  'string': 'string'
              },
              EncryptionKeyArn='string',
              CreatorRequestId='string'
          )
        
        **Response Syntax**
        ::
            {
                'BackupVaultName': 'string',
                'BackupVaultArn': 'string',
                'CreationDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupVaultName** *(string) --* 
              The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.
            - **BackupVaultArn** *(string) --* 
              An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .
            - **CreationDate** *(datetime) --* 
              The date and time a backup vault is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :type BackupVaultTags: dict
        :param BackupVaultTags:
          Metadata that you can assign to help organize the resources that you create. Each tag is a key-value pair.
          - *(string) --*
            - *(string) --*
        :type EncryptionKeyArn: string
        :param EncryptionKeyArn:
          The server-side encryption key that is used to protect your backups; for example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .
        :type CreatorRequestId: string
        :param CreatorRequestId:
          A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.
        :rtype: dict
        :returns:
        """
        pass

    def delete_backup_plan(self, BackupPlanId: str) -> Dict:
        """
        Deletes a backup plan. A backup plan can only be deleted after all associated selections of resources have been deleted. Deleting a backup plan deletes the current version of a backup plan. Previous versions, if any, will still exist.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/DeleteBackupPlan>`_
        
        **Request Syntax**
        ::
          response = client.delete_backup_plan(
              BackupPlanId='string'
          )
        
        **Response Syntax**
        ::
            {
                'BackupPlanId': 'string',
                'BackupPlanArn': 'string',
                'DeletionDate': datetime(2015, 1, 1),
                'VersionId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupPlanId** *(string) --* 
              Uniquely identifies a backup plan.
            - **BackupPlanArn** *(string) --* 
              An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .
            - **DeletionDate** *(datetime) --* 
              The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **VersionId** *(string) --* 
              Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version Ids cannot be edited.
        :type BackupPlanId: string
        :param BackupPlanId: **[REQUIRED]**
          Uniquely identifies a backup plan.
        :rtype: dict
        :returns:
        """
        pass

    def delete_backup_selection(self, BackupPlanId: str, SelectionId: str):
        """
        Deletes the resource selection associated with a backup plan that is specified by the ``SelectionId`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/DeleteBackupSelection>`_
        
        **Request Syntax**
        ::
          response = client.delete_backup_selection(
              BackupPlanId='string',
              SelectionId='string'
          )
        :type BackupPlanId: string
        :param BackupPlanId: **[REQUIRED]**
          Uniquely identifies a backup plan.
        :type SelectionId: string
        :param SelectionId: **[REQUIRED]**
          Uniquely identifies the body of a request to assign a set of resources to a backup plan.
        :returns: None
        """
        pass

    def delete_backup_vault(self, BackupVaultName: str):
        """
        Deletes the backup vault identified by its name. A vault can be deleted only if it is empty.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/DeleteBackupVault>`_
        
        **Request Syntax**
        ::
          response = client.delete_backup_vault(
              BackupVaultName='string'
          )
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and theAWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :returns: None
        """
        pass

    def delete_backup_vault_access_policy(self, BackupVaultName: str):
        """
        Deletes the policy document that manages permissions on a backup vault.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/DeleteBackupVaultAccessPolicy>`_
        
        **Request Syntax**
        ::
          response = client.delete_backup_vault_access_policy(
              BackupVaultName='string'
          )
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :returns: None
        """
        pass

    def delete_backup_vault_notifications(self, BackupVaultName: str):
        """
        Deletes event notifications for the specified backup vault.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/DeleteBackupVaultNotifications>`_
        
        **Request Syntax**
        ::
          response = client.delete_backup_vault_notifications(
              BackupVaultName='string'
          )
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :returns: None
        """
        pass

    def delete_recovery_point(self, BackupVaultName: str, RecoveryPointArn: str):
        """
        Deletes the recovery point specified by a recovery point ID.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/DeleteRecoveryPoint>`_
        
        **Request Syntax**
        ::
          response = client.delete_recovery_point(
              BackupVaultName='string',
              RecoveryPointArn='string'
          )
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :type RecoveryPointArn: string
        :param RecoveryPointArn: **[REQUIRED]**
          An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
        :returns: None
        """
        pass

    def describe_backup_job(self, BackupJobId: str) -> Dict:
        """
        Returns metadata associated with creating a backup of a resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/DescribeBackupJob>`_
        
        **Request Syntax**
        ::
          response = client.describe_backup_job(
              BackupJobId='string'
          )
        
        **Response Syntax**
        ::
            {
                'BackupJobId': 'string',
                'BackupVaultName': 'string',
                'BackupVaultArn': 'string',
                'RecoveryPointArn': 'string',
                'ResourceArn': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'CompletionDate': datetime(2015, 1, 1),
                'State': 'CREATED'|'PENDING'|'RUNNING'|'ABORTING'|'ABORTED'|'COMPLETED'|'FAILED'|'EXPIRED',
                'StatusMessage': 'string',
                'PercentDone': 'string',
                'BackupSizeInBytes': 123,
                'IamRoleArn': 'string',
                'CreatedBy': {
                    'BackupPlanId': 'string',
                    'BackupPlanArn': 'string',
                    'BackupPlanVersion': 'string',
                    'BackupRuleId': 'string'
                },
                'ResourceType': 'string',
                'BytesTransferred': 123,
                'ExpectedCompletionDate': datetime(2015, 1, 1),
                'StartBy': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupJobId** *(string) --* 
              Uniquely identifies a request to AWS Backup to back up a resource.
            - **BackupVaultName** *(string) --* 
              The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
            - **BackupVaultArn** *(string) --* 
              An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .
            - **RecoveryPointArn** *(string) --* 
              An ARN that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
            - **ResourceArn** *(string) --* 
              An ARN that uniquely identifies a saved resource. The format of the ARN depends on the resource type.
            - **CreationDate** *(datetime) --* 
              The date and time that a backup job is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **CompletionDate** *(datetime) --* 
              The date and time that a job to create a backup job is completed, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **State** *(string) --* 
              The current state of a resource recovery point.
            - **StatusMessage** *(string) --* 
              A detailed message explaining the status of the job to back up a resource.
            - **PercentDone** *(string) --* 
              Contains an estimated percentage that is complete of a job at the time the job status was queried.
            - **BackupSizeInBytes** *(integer) --* 
              The size, in bytes, of a backup.
            - **IamRoleArn** *(string) --* 
              Specifies the IAM role ARN used to create the target recovery point; for example, ``arn:aws:iam::123456789012:role/S3Access`` .
            - **CreatedBy** *(dict) --* 
              Contains identifying information about the creation of a backup job, including the ``BackupPlanArn`` , ``BackupPlanId`` , ``BackupPlanVersion`` , and ``BackupRuleId`` of the backup plan that is used to create it.
              - **BackupPlanId** *(string) --* 
                Uniquely identifies a backup plan.
              - **BackupPlanArn** *(string) --* 
                An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .
              - **BackupPlanVersion** *(string) --* 
                Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.
              - **BackupRuleId** *(string) --* 
                Uniquely identifies a rule used to schedule the backup of a selection of resources.
            - **ResourceType** *(string) --* 
              The type of AWS resource to be backed-up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.
            - **BytesTransferred** *(integer) --* 
              The size in bytes transferred to a backup vault at the time that the job status was queried.
            - **ExpectedCompletionDate** *(datetime) --* 
              The date and time that a job to back up resources is expected to be completed, in Unix format and Coordinated Universal Time (UTC). The value of ``ExpectedCompletionDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **StartBy** *(datetime) --* 
              Specifies the time in Unix format and Coordinated Universal Time (UTC) when a backup job must be started before it is canceled. The value is calculated by adding the start window to the scheduled time. So if the scheduled time were 6:00 PM and the start window is 2 hours, the ``StartBy`` time would be 8:00 PM on the date specified. The value of ``StartBy`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
        :type BackupJobId: string
        :param BackupJobId: **[REQUIRED]**
          Uniquely identifies a request to AWS Backup to back up a resource.
        :rtype: dict
        :returns:
        """
        pass

    def describe_backup_vault(self, BackupVaultName: str) -> Dict:
        """
        Returns metadata about a backup vault specified by its name.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/DescribeBackupVault>`_
        
        **Request Syntax**
        ::
          response = client.describe_backup_vault(
              BackupVaultName='string'
          )
        
        **Response Syntax**
        ::
            {
                'BackupVaultName': 'string',
                'BackupVaultArn': 'string',
                'EncryptionKeyArn': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'CreatorRequestId': 'string',
                'NumberOfRecoveryPoints': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupVaultName** *(string) --* 
              The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.
            - **BackupVaultArn** *(string) --* 
              An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .
            - **EncryptionKeyArn** *(string) --* 
              The server-side encryption key that is used to protect your backups; for example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .
            - **CreationDate** *(datetime) --* 
              The date and time that a backup vault is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **CreatorRequestId** *(string) --* 
              A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.
            - **NumberOfRecoveryPoints** *(integer) --* 
              The number of recovery points that are stored in a backup vault.
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :rtype: dict
        :returns:
        """
        pass

    def describe_protected_resource(self, ResourceArn: str) -> Dict:
        """
        Returns information about a saved resource, including the last time it was backed-up, its Amazon Resource Name (ARN), and the AWS service type of the saved resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/DescribeProtectedResource>`_
        
        **Request Syntax**
        ::
          response = client.describe_protected_resource(
              ResourceArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'ResourceArn': 'string',
                'ResourceType': 'string',
                'LastBackupTime': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ResourceArn** *(string) --* 
              An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.
            - **ResourceType** *(string) --* 
              The type of AWS resource saved as a recovery point; for example, an EBS volume or an Amazon RDS database.
            - **LastBackupTime** *(datetime) --* 
              The date and time that a resource was last backed up, in Unix format and Coordinated Universal Time (UTC). The value of ``LastBackupTime`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
        :rtype: dict
        :returns:
        """
        pass

    def describe_recovery_point(self, BackupVaultName: str, RecoveryPointArn: str) -> Dict:
        """
        Returns metadata associated with a recovery point, including ID, status, encryption, and lifecycle.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/DescribeRecoveryPoint>`_
        
        **Request Syntax**
        ::
          response = client.describe_recovery_point(
              BackupVaultName='string',
              RecoveryPointArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'RecoveryPointArn': 'string',
                'BackupVaultName': 'string',
                'BackupVaultArn': 'string',
                'ResourceArn': 'string',
                'ResourceType': 'string',
                'CreatedBy': {
                    'BackupPlanId': 'string',
                    'BackupPlanArn': 'string',
                    'BackupPlanVersion': 'string',
                    'BackupRuleId': 'string'
                },
                'IamRoleArn': 'string',
                'Status': 'COMPLETED'|'PARTIAL'|'DELETING'|'EXPIRED',
                'CreationDate': datetime(2015, 1, 1),
                'CompletionDate': datetime(2015, 1, 1),
                'BackupSizeInBytes': 123,
                'CalculatedLifecycle': {
                    'MoveToColdStorageAt': datetime(2015, 1, 1),
                    'DeleteAt': datetime(2015, 1, 1)
                },
                'Lifecycle': {
                    'MoveToColdStorageAfterDays': 123,
                    'DeleteAfterDays': 123
                },
                'EncryptionKeyArn': 'string',
                'IsEncrypted': True|False,
                'StorageClass': 'WARM'|'COLD'|'DELETED',
                'LastRestoreTime': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RecoveryPointArn** *(string) --* 
              An ARN that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
            - **BackupVaultName** *(string) --* 
              The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.
            - **BackupVaultArn** *(string) --* 
              An ARN that uniquely identifies a backup vault; for example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .
            - **ResourceArn** *(string) --* 
              An ARN that uniquely identifies a saved resource. The format of the ARN depends on the resource type.
            - **ResourceType** *(string) --* 
              The type of AWS resource to save as a recovery point; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.
            - **CreatedBy** *(dict) --* 
              Contains identifying information about the creation of a recovery point, including the ``BackupPlanArn`` , ``BackupPlanId`` , ``BackupPlanVersion`` , and ``BackupRuleId`` of the backup plan used to create it.
              - **BackupPlanId** *(string) --* 
                Uniquely identifies a backup plan.
              - **BackupPlanArn** *(string) --* 
                An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .
              - **BackupPlanVersion** *(string) --* 
                Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.
              - **BackupRuleId** *(string) --* 
                Uniquely identifies a rule used to schedule the backup of a selection of resources.
            - **IamRoleArn** *(string) --* 
              Specifies the IAM role ARN used to create the target recovery point; for example, ``arn:aws:iam::123456789012:role/S3Access`` .
            - **Status** *(string) --* 
              A status code specifying the state of the recovery point.
              .. note::
                A partial status indicates that the recovery point was not successfully re-created and must be retried.
            - **CreationDate** *(datetime) --* 
              The date and time that a recovery point is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **CompletionDate** *(datetime) --* 
              The date and time that a job to create a recovery point is completed, in Unix format and Coordinated Universal Time (UTC). The value of ``CompletionDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **BackupSizeInBytes** *(integer) --* 
              The size, in bytes, of a backup.
            - **CalculatedLifecycle** *(dict) --* 
              A ``CalculatedLifecycle`` object containing ``DeleteAt`` and ``MoveToColdStorageAt`` timestamps.
              - **MoveToColdStorageAt** *(datetime) --* 
                A timestamp that specifies when to transition a recovery point to cold storage.
              - **DeleteAt** *(datetime) --* 
                A timestamp that specifies when to delete a recovery point.
            - **Lifecycle** *(dict) --* 
              The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define. 
              Backups that are transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. 
              - **MoveToColdStorageAfterDays** *(integer) --* 
                Specifies the number of days after creation that a recovery point is moved to cold storage.
              - **DeleteAfterDays** *(integer) --* 
                Specifies the number of days after creation that a recovery point is deleted. Must be greater than ``MoveToColdStorageAfterDays`` .
            - **EncryptionKeyArn** *(string) --* 
              The server-side encryption key used to protect your backups; for example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .
            - **IsEncrypted** *(boolean) --* 
              A Boolean value that is returned as ``TRUE`` if the specified recovery point is encrypted, or ``FALSE`` if the recovery point is not encrypted.
            - **StorageClass** *(string) --* 
              Specifies the storage class of the recovery point. Valid values are ``WARM`` or ``COLD`` .
            - **LastRestoreTime** *(datetime) --* 
              The date and time that a recovery point was last restored, in Unix format and Coordinated Universal Time (UTC). The value of ``LastRestoreTime`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :type RecoveryPointArn: string
        :param RecoveryPointArn: **[REQUIRED]**
          An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_restore_job(self, RestoreJobId: str) -> Dict:
        """
        Returns metadata associated with a restore job that is specified by a job ID.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/DescribeRestoreJob>`_
        
        **Request Syntax**
        ::
          response = client.describe_restore_job(
              RestoreJobId='string'
          )
        
        **Response Syntax**
        ::
            {
                'RestoreJobId': 'string',
                'RecoveryPointArn': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'CompletionDate': datetime(2015, 1, 1),
                'Status': 'PENDING'|'RUNNING'|'COMPLETED'|'ABORTED'|'FAILED',
                'StatusMessage': 'string',
                'PercentDone': 'string',
                'BackupSizeInBytes': 123,
                'IamRoleArn': 'string',
                'ExpectedCompletionTimeMinutes': 123,
                'CreatedResourceArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RestoreJobId** *(string) --* 
              Uniquely identifies the job that restores a recovery point.
            - **RecoveryPointArn** *(string) --* 
              An ARN that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
            - **CreationDate** *(datetime) --* 
              The date and time that a restore job is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **CompletionDate** *(datetime) --* 
              The date and time that a job to restore a recovery point is completed, in Unix format and Coordinated Universal Time (UTC). The value of ``CompletionDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **Status** *(string) --* 
              Status code specifying the state of the job that is initiated by AWS Backup to restore a recovery point.
            - **StatusMessage** *(string) --* 
              A detailed message explaining the status of a job to restore a recovery point.
            - **PercentDone** *(string) --* 
              Contains an estimated percentage that is complete of a job at the time the job status was queried.
            - **BackupSizeInBytes** *(integer) --* 
              The size, in bytes, of the restored resource.
            - **IamRoleArn** *(string) --* 
              Specifies the IAM role ARN used to create the target recovery point; for example, ``arn:aws:iam::123456789012:role/S3Access`` .
            - **ExpectedCompletionTimeMinutes** *(integer) --* 
              The amount of time in minutes that a job restoring a recovery point is expected to take.
            - **CreatedResourceArn** *(string) --* 
              An Amazon Resource Name (ARN) that uniquely identifies a resource whose recovery point is being restored. The format of the ARN depends on the resource type of the backed-up resource.
        :type RestoreJobId: string
        :param RestoreJobId: **[REQUIRED]**
          Uniquely identifies the job that restores a recovery point.
        :rtype: dict
        :returns:
        """
        pass

    def export_backup_plan_template(self, BackupPlanId: str) -> Dict:
        """
        Returns the backup plan that is specified by the plan ID as a backup template.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ExportBackupPlanTemplate>`_
        
        **Request Syntax**
        ::
          response = client.export_backup_plan_template(
              BackupPlanId='string'
          )
        
        **Response Syntax**
        ::
            {
                'BackupPlanTemplateJson': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupPlanTemplateJson** *(string) --* 
              The body of a backup plan template in JSON format.
              .. note::
                This is a signed JSON document that cannot be modified before being passed to ``GetBackupPlanFromJSON.``  
        :type BackupPlanId: string
        :param BackupPlanId: **[REQUIRED]**
          Uniquely identifies a backup plan.
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

    def get_backup_plan(self, BackupPlanId: str, VersionId: str = None) -> Dict:
        """
        Returns the body of a backup plan in JSON format, in addition to plan metadata.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/GetBackupPlan>`_
        
        **Request Syntax**
        ::
          response = client.get_backup_plan(
              BackupPlanId='string',
              VersionId='string'
          )
        
        **Response Syntax**
        ::
            {
                'BackupPlan': {
                    'BackupPlanName': 'string',
                    'Rules': [
                        {
                            'RuleName': 'string',
                            'TargetBackupVaultName': 'string',
                            'ScheduleExpression': 'string',
                            'StartWindowMinutes': 123,
                            'CompletionWindowMinutes': 123,
                            'Lifecycle': {
                                'MoveToColdStorageAfterDays': 123,
                                'DeleteAfterDays': 123
                            },
                            'RecoveryPointTags': {
                                'string': 'string'
                            },
                            'RuleId': 'string'
                        },
                    ]
                },
                'BackupPlanId': 'string',
                'BackupPlanArn': 'string',
                'VersionId': 'string',
                'CreatorRequestId': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'DeletionDate': datetime(2015, 1, 1),
                'LastExecutionDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupPlan** *(dict) --* 
              Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of ``Rules`` .
              - **BackupPlanName** *(string) --* 
                The display name of a backup plan.
              - **Rules** *(list) --* 
                An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used to back up a selection of resources.
                - *(dict) --* 
                  Specifies a scheduled task used to back up a selection of resources.
                  - **RuleName** *(string) --* 
                    An optional display name for a backup rule.
                  - **TargetBackupVaultName** *(string) --* 
                    The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
                  - **ScheduleExpression** *(string) --* 
                    A CRON expression specifying when AWS Backup initiates a backup job.
                  - **StartWindowMinutes** *(integer) --* 
                    An optional value that specifies a period of time in minutes after a backup is scheduled before a job is canceled if it doesn't start successfully.
                  - **CompletionWindowMinutes** *(integer) --* 
                    A value in minutes after a backup job is successfully started before it must be completed or it is canceled by AWS Backup. This value is optional.
                  - **Lifecycle** *(dict) --* 
                    The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define. 
                    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. 
                    - **MoveToColdStorageAfterDays** *(integer) --* 
                      Specifies the number of days after creation that a recovery point is moved to cold storage.
                    - **DeleteAfterDays** *(integer) --* 
                      Specifies the number of days after creation that a recovery point is deleted. Must be greater than ``MoveToColdStorageAfterDays`` .
                  - **RecoveryPointTags** *(dict) --* 
                    An array of key-value pair strings that are assigned to resources that are associated with this rule when restored from backup.
                    - *(string) --* 
                      - *(string) --* 
                  - **RuleId** *(string) --* 
                    Uniquely identifies a rule that is used to schedule the backup of a selection of resources.
            - **BackupPlanId** *(string) --* 
              Uniquely identifies a backup plan.
            - **BackupPlanArn** *(string) --* 
              An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .
            - **VersionId** *(string) --* 
              Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.
            - **CreatorRequestId** *(string) --* 
              A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.
            - **CreationDate** *(datetime) --* 
              The date and time that a backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **DeletionDate** *(datetime) --* 
              The date and time that a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **LastExecutionDate** *(datetime) --* 
              The last time a job to back up resources was executed with this backup plan. A date and time, in Unix format and Coordinated Universal Time (UTC). The value of ``LastExecutionDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
        :type BackupPlanId: string
        :param BackupPlanId: **[REQUIRED]**
          Uniquely identifies a backup plan.
        :type VersionId: string
        :param VersionId:
          Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.
        :rtype: dict
        :returns:
        """
        pass

    def get_backup_plan_from_json(self, BackupPlanTemplateJson: str) -> Dict:
        """
        Returns a valid JSON document specifying a backup plan or an error.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/GetBackupPlanFromJSON>`_
        
        **Request Syntax**
        ::
          response = client.get_backup_plan_from_json(
              BackupPlanTemplateJson='string'
          )
        
        **Response Syntax**
        ::
            {
                'BackupPlan': {
                    'BackupPlanName': 'string',
                    'Rules': [
                        {
                            'RuleName': 'string',
                            'TargetBackupVaultName': 'string',
                            'ScheduleExpression': 'string',
                            'StartWindowMinutes': 123,
                            'CompletionWindowMinutes': 123,
                            'Lifecycle': {
                                'MoveToColdStorageAfterDays': 123,
                                'DeleteAfterDays': 123
                            },
                            'RecoveryPointTags': {
                                'string': 'string'
                            },
                            'RuleId': 'string'
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupPlan** *(dict) --* 
              Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of ``Rules`` .
              - **BackupPlanName** *(string) --* 
                The display name of a backup plan.
              - **Rules** *(list) --* 
                An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used to back up a selection of resources.
                - *(dict) --* 
                  Specifies a scheduled task used to back up a selection of resources.
                  - **RuleName** *(string) --* 
                    An optional display name for a backup rule.
                  - **TargetBackupVaultName** *(string) --* 
                    The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
                  - **ScheduleExpression** *(string) --* 
                    A CRON expression specifying when AWS Backup initiates a backup job.
                  - **StartWindowMinutes** *(integer) --* 
                    An optional value that specifies a period of time in minutes after a backup is scheduled before a job is canceled if it doesn't start successfully.
                  - **CompletionWindowMinutes** *(integer) --* 
                    A value in minutes after a backup job is successfully started before it must be completed or it is canceled by AWS Backup. This value is optional.
                  - **Lifecycle** *(dict) --* 
                    The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define. 
                    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. 
                    - **MoveToColdStorageAfterDays** *(integer) --* 
                      Specifies the number of days after creation that a recovery point is moved to cold storage.
                    - **DeleteAfterDays** *(integer) --* 
                      Specifies the number of days after creation that a recovery point is deleted. Must be greater than ``MoveToColdStorageAfterDays`` .
                  - **RecoveryPointTags** *(dict) --* 
                    An array of key-value pair strings that are assigned to resources that are associated with this rule when restored from backup.
                    - *(string) --* 
                      - *(string) --* 
                  - **RuleId** *(string) --* 
                    Uniquely identifies a rule that is used to schedule the backup of a selection of resources.
        :type BackupPlanTemplateJson: string
        :param BackupPlanTemplateJson: **[REQUIRED]**
          A customer-supplied backup plan document in JSON format.
        :rtype: dict
        :returns:
        """
        pass

    def get_backup_plan_from_template(self, BackupPlanTemplateId: str) -> Dict:
        """
        Returns the template specified by its ``templateId`` as a backup plan.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/GetBackupPlanFromTemplate>`_
        
        **Request Syntax**
        ::
          response = client.get_backup_plan_from_template(
              BackupPlanTemplateId='string'
          )
        
        **Response Syntax**
        ::
            {
                'BackupPlanDocument': {
                    'BackupPlanName': 'string',
                    'Rules': [
                        {
                            'RuleName': 'string',
                            'TargetBackupVaultName': 'string',
                            'ScheduleExpression': 'string',
                            'StartWindowMinutes': 123,
                            'CompletionWindowMinutes': 123,
                            'Lifecycle': {
                                'MoveToColdStorageAfterDays': 123,
                                'DeleteAfterDays': 123
                            },
                            'RecoveryPointTags': {
                                'string': 'string'
                            },
                            'RuleId': 'string'
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupPlanDocument** *(dict) --* 
              Returns the body of a backup plan based on the target template, including the name, rules, and backup vault of the plan.
              - **BackupPlanName** *(string) --* 
                The display name of a backup plan.
              - **Rules** *(list) --* 
                An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used to back up a selection of resources.
                - *(dict) --* 
                  Specifies a scheduled task used to back up a selection of resources.
                  - **RuleName** *(string) --* 
                    An optional display name for a backup rule.
                  - **TargetBackupVaultName** *(string) --* 
                    The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
                  - **ScheduleExpression** *(string) --* 
                    A CRON expression specifying when AWS Backup initiates a backup job.
                  - **StartWindowMinutes** *(integer) --* 
                    An optional value that specifies a period of time in minutes after a backup is scheduled before a job is canceled if it doesn't start successfully.
                  - **CompletionWindowMinutes** *(integer) --* 
                    A value in minutes after a backup job is successfully started before it must be completed or it is canceled by AWS Backup. This value is optional.
                  - **Lifecycle** *(dict) --* 
                    The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define. 
                    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. 
                    - **MoveToColdStorageAfterDays** *(integer) --* 
                      Specifies the number of days after creation that a recovery point is moved to cold storage.
                    - **DeleteAfterDays** *(integer) --* 
                      Specifies the number of days after creation that a recovery point is deleted. Must be greater than ``MoveToColdStorageAfterDays`` .
                  - **RecoveryPointTags** *(dict) --* 
                    An array of key-value pair strings that are assigned to resources that are associated with this rule when restored from backup.
                    - *(string) --* 
                      - *(string) --* 
                  - **RuleId** *(string) --* 
                    Uniquely identifies a rule that is used to schedule the backup of a selection of resources.
        :type BackupPlanTemplateId: string
        :param BackupPlanTemplateId: **[REQUIRED]**
          Uniquely identifies a stored backup plan template.
        :rtype: dict
        :returns:
        """
        pass

    def get_backup_selection(self, BackupPlanId: str, SelectionId: str) -> Dict:
        """
        Returns selection metadata and a document in JSON format that specifies a list of resources that are associated with a backup plan.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/GetBackupSelection>`_
        
        **Request Syntax**
        ::
          response = client.get_backup_selection(
              BackupPlanId='string',
              SelectionId='string'
          )
        
        **Response Syntax**
        ::
            {
                'BackupSelection': {
                    'SelectionName': 'string',
                    'IamRoleArn': 'string',
                    'Resources': [
                        'string',
                    ],
                    'ListOfTags': [
                        {
                            'ConditionType': 'STRINGEQUALS',
                            'ConditionKey': 'string',
                            'ConditionValue': 'string'
                        },
                    ]
                },
                'SelectionId': 'string',
                'BackupPlanId': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'CreatorRequestId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupSelection** *(dict) --* 
              Specifies the body of a request to assign a set of resources to a backup plan.
              It includes an array of resources, an optional array of patterns to exclude resources, an optional role to provide access to the AWS service that the resource belongs to, and an optional array of tags used to identify a set of resources.
              - **SelectionName** *(string) --* 
                The display name of a resource selection document.
              - **IamRoleArn** *(string) --* 
                The ARN of the IAM role that AWS Backup uses to authenticate when restoring the target resource; for example, ``arn:aws:iam::123456789012:role/S3Access`` .
              - **Resources** *(list) --* 
                An array of strings that either contain Amazon Resource Names (ARNs) or match patterns such as "``arn:aws:ec2:us-east-1:123456789012:volume/*`` " of resources to assign to a backup plan.
                - *(string) --* 
              - **ListOfTags** *(list) --* 
                An array of conditions used to specify a set of resources to assign to a backup plan; for example, ``"StringEquals": {"ec2:ResourceTag/Department": "accounting"`` .
                - *(dict) --* 
                  Contains an array of triplets made up of a condition type (such as ``StringEquals`` ), a key, and a value. Conditions are used to filter resources in a selection that is assigned to a backup plan.
                  - **ConditionType** *(string) --* 
                    An operation, such as ``StringEquals`` , that is applied to a key-value pair used to filter resources in a selection.
                  - **ConditionKey** *(string) --* 
                    The key in a key-value pair. For example, in ``"ec2:ResourceTag/Department": "accounting"`` , ``"ec2:ResourceTag/Department"`` is the key.
                  - **ConditionValue** *(string) --* 
                    The value in a key-value pair. For example, in ``"ec2:ResourceTag/Department": "accounting"`` , ``"accounting"`` is the value.
            - **SelectionId** *(string) --* 
              Uniquely identifies the body of a request to assign a set of resources to a backup plan.
            - **BackupPlanId** *(string) --* 
              Uniquely identifies a backup plan.
            - **CreationDate** *(datetime) --* 
              The date and time a backup selection is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **CreatorRequestId** *(string) --* 
              A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.
        :type BackupPlanId: string
        :param BackupPlanId: **[REQUIRED]**
          Uniquely identifies a backup plan.
        :type SelectionId: string
        :param SelectionId: **[REQUIRED]**
          Uniquely identifies the body of a request to assign a set of resources to a backup plan.
        :rtype: dict
        :returns:
        """
        pass

    def get_backup_vault_access_policy(self, BackupVaultName: str) -> Dict:
        """
        Returns the access policy document that is associated with the named backup vault.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/GetBackupVaultAccessPolicy>`_
        
        **Request Syntax**
        ::
          response = client.get_backup_vault_access_policy(
              BackupVaultName='string'
          )
        
        **Response Syntax**
        ::
            {
                'BackupVaultName': 'string',
                'BackupVaultArn': 'string',
                'Policy': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupVaultName** *(string) --* 
              The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.
            - **BackupVaultArn** *(string) --* 
              An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .
            - **Policy** *(string) --* 
              The backup vault access policy document in JSON format.
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :rtype: dict
        :returns:
        """
        pass

    def get_backup_vault_notifications(self, BackupVaultName: str) -> Dict:
        """
        Returns event notifications for the specified backup vault.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/GetBackupVaultNotifications>`_
        
        **Request Syntax**
        ::
          response = client.get_backup_vault_notifications(
              BackupVaultName='string'
          )
        
        **Response Syntax**
        ::
            {
                'BackupVaultName': 'string',
                'BackupVaultArn': 'string',
                'SNSTopicArn': 'string',
                'BackupVaultEvents': [
                    'BACKUP_JOB_STARTED'|'BACKUP_JOB_COMPLETED'|'RESTORE_JOB_STARTED'|'RESTORE_JOB_COMPLETED'|'RECOVERY_POINT_MODIFIED'|'BACKUP_PLAN_CREATED'|'BACKUP_PLAN_MODIFIED',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupVaultName** *(string) --* 
              The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.
            - **BackupVaultArn** *(string) --* 
              An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .
            - **SNSTopicArn** *(string) --* 
              An ARN that uniquely identifies an Amazon Simple Notification Service (Amazon SNS) topic; for example, ``arn:aws:sns:us-west-2:111122223333:MyTopic`` .
            - **BackupVaultEvents** *(list) --* 
              An array of events that indicate the status of jobs to back up resources to the backup vault.
              - *(string) --* 
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :rtype: dict
        :returns:
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

    def get_recovery_point_restore_metadata(self, BackupVaultName: str, RecoveryPointArn: str) -> Dict:
        """
        Returns two sets of metadata key-value pairs. The first set lists the metadata that the recovery point was created with. The second set lists the metadata key-value pairs that are required to restore the recovery point.
        These sets can be the same, or the restore metadata set can contain different values if the target service to be restored has changed since the recovery point was created and now requires additional or different information in order to be restored.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/GetRecoveryPointRestoreMetadata>`_
        
        **Request Syntax**
        ::
          response = client.get_recovery_point_restore_metadata(
              BackupVaultName='string',
              RecoveryPointArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'BackupVaultArn': 'string',
                'RecoveryPointArn': 'string',
                'RestoreMetadata': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupVaultArn** *(string) --* 
              An ARN that uniquely identifies a backup vault; for example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .
            - **RecoveryPointArn** *(string) --* 
              An ARN that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
            - **RestoreMetadata** *(dict) --* 
              A set of metadata key-value pairs that lists the metadata key-value pairs that are required to restore the recovery point.
              - *(string) --* 
                - *(string) --* 
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :type RecoveryPointArn: string
        :param RecoveryPointArn: **[REQUIRED]**
          An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
        :rtype: dict
        :returns:
        """
        pass

    def get_supported_resource_types(self) -> Dict:
        """
        Returns the AWS resource types supported by AWS Backup.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/GetSupportedResourceTypes>`_
        
        **Request Syntax**
        ::
          response = client.get_supported_resource_types()
        
        **Response Syntax**
        ::
            {
                'ResourceTypes': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ResourceTypes** *(list) --* 
              Contains a string with the supported AWS resource types:
              * ``EBS`` for Amazon Elastic Block Store 
              * ``SGW`` for AWS Storage Gateway 
              * ``RDS`` for Amazon Relational Database Service 
              * ``DDB`` for Amazon DynamoDB 
              * ``EFS`` for Amazon Elastic File System 
              - *(string) --* 
        :rtype: dict
        :returns:
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

    def list_backup_jobs(self, NextToken: str = None, MaxResults: int = None, ByResourceArn: str = None, ByState: str = None, ByBackupVaultName: str = None, ByCreatedBefore: datetime = None, ByCreatedAfter: datetime = None, ByResourceType: str = None) -> Dict:
        """
        Returns metadata about your backup jobs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ListBackupJobs>`_
        
        **Request Syntax**
        ::
          response = client.list_backup_jobs(
              NextToken='string',
              MaxResults=123,
              ByResourceArn='string',
              ByState='CREATED'|'PENDING'|'RUNNING'|'ABORTING'|'ABORTED'|'COMPLETED'|'FAILED'|'EXPIRED',
              ByBackupVaultName='string',
              ByCreatedBefore=datetime(2015, 1, 1),
              ByCreatedAfter=datetime(2015, 1, 1),
              ByResourceType='string'
          )
        
        **Response Syntax**
        ::
            {
                'BackupJobs': [
                    {
                        'BackupJobId': 'string',
                        'BackupVaultName': 'string',
                        'BackupVaultArn': 'string',
                        'RecoveryPointArn': 'string',
                        'ResourceArn': 'string',
                        'CreationDate': datetime(2015, 1, 1),
                        'CompletionDate': datetime(2015, 1, 1),
                        'State': 'CREATED'|'PENDING'|'RUNNING'|'ABORTING'|'ABORTED'|'COMPLETED'|'FAILED'|'EXPIRED',
                        'StatusMessage': 'string',
                        'PercentDone': 'string',
                        'BackupSizeInBytes': 123,
                        'IamRoleArn': 'string',
                        'CreatedBy': {
                            'BackupPlanId': 'string',
                            'BackupPlanArn': 'string',
                            'BackupPlanVersion': 'string',
                            'BackupRuleId': 'string'
                        },
                        'ExpectedCompletionDate': datetime(2015, 1, 1),
                        'StartBy': datetime(2015, 1, 1),
                        'ResourceType': 'string',
                        'BytesTransferred': 123
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupJobs** *(list) --* 
              An array of structures containing metadata about your backup jobs returned in JSON format.
              - *(dict) --* 
                Contains detailed information about a backup job.
                - **BackupJobId** *(string) --* 
                  Uniquely identifies a request to AWS Backup to back up a resource.
                - **BackupVaultName** *(string) --* 
                  The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
                - **BackupVaultArn** *(string) --* 
                  An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .
                - **RecoveryPointArn** *(string) --* 
                  An ARN that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
                - **ResourceArn** *(string) --* 
                  An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.
                - **CreationDate** *(datetime) --* 
                  The date and time a backup job is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **CompletionDate** *(datetime) --* 
                  The date and time a job to create a backup job is completed, in Unix format and Coordinated Universal Time (UTC). The value of ``CompletionDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **State** *(string) --* 
                  The current state of a resource recovery point.
                - **StatusMessage** *(string) --* 
                  A detailed message explaining the status of the job to back up a resource.
                - **PercentDone** *(string) --* 
                  Contains an estimated percentage complete of a job at the time the job status was queried.
                - **BackupSizeInBytes** *(integer) --* 
                  The size, in bytes, of a backup.
                - **IamRoleArn** *(string) --* 
                  Specifies the IAM role ARN used to create the target recovery point; for example, ``arn:aws:iam::123456789012:role/S3Access`` .
                - **CreatedBy** *(dict) --* 
                  Contains identifying information about the creation of a backup job, including the ``BackupPlanArn`` , ``BackupPlanId`` , ``BackupPlanVersion`` , and ``BackupRuleId`` of the backup plan used to create it.
                  - **BackupPlanId** *(string) --* 
                    Uniquely identifies a backup plan.
                  - **BackupPlanArn** *(string) --* 
                    An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .
                  - **BackupPlanVersion** *(string) --* 
                    Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.
                  - **BackupRuleId** *(string) --* 
                    Uniquely identifies a rule used to schedule the backup of a selection of resources.
                - **ExpectedCompletionDate** *(datetime) --* 
                  The date and time a job to back up resources is expected to be completed, in Unix format and Coordinated Universal Time (UTC). The value of ``ExpectedCompletionDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **StartBy** *(datetime) --* 
                  Specifies the time in Unix format and Coordinated Universal Time (UTC) when a backup job must be started before it is canceled. The value is calculated by adding the start window to the scheduled time. So if the scheduled time were 6:00 PM and the start window is 2 hours, the ``StartBy`` time would be 8:00 PM on the date specified. The value of ``StartBy`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **ResourceType** *(string) --* 
                  The type of AWS resource to be backed-up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.
                - **BytesTransferred** *(integer) --* 
                  The size in bytes transferred to a backup vault at the time that the job status was queried.
            - **NextToken** *(string) --* 
              The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type NextToken: string
        :param NextToken:
          The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of items to be returned.
        :type ByResourceArn: string
        :param ByResourceArn:
          Returns only backup jobs that match the specified resource Amazon Resource Name (ARN).
        :type ByState: string
        :param ByState:
          Returns only backup jobs that are in the specified state.
        :type ByBackupVaultName: string
        :param ByBackupVaultName:
          Returns only backup jobs that will be stored in the specified backup vault. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :type ByCreatedBefore: datetime
        :param ByCreatedBefore:
          Returns only backup jobs that were created before the specified date.
        :type ByCreatedAfter: datetime
        :param ByCreatedAfter:
          Returns only backup jobs that were created after the specified date.
        :type ByResourceType: string
        :param ByResourceType:
          Returns only backup jobs for the specified resources:
          * ``EBS`` for Amazon Elastic Block Store
          * ``SGW`` for AWS Storage Gateway
          * ``RDS`` for Amazon Relational Database Service
          * ``DDB`` for Amazon DynamoDB
          * ``EFS`` for Amazon Elastic File System
        :rtype: dict
        :returns:
        """
        pass

    def list_backup_plan_templates(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Returns metadata of your saved backup plan templates, including the template ID, name, and the creation and deletion dates.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ListBackupPlanTemplates>`_
        
        **Request Syntax**
        ::
          response = client.list_backup_plan_templates(
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'NextToken': 'string',
                'BackupPlanTemplatesList': [
                    {
                        'BackupPlanTemplateId': 'string',
                        'BackupPlanTemplateName': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NextToken** *(string) --* 
              The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
            - **BackupPlanTemplatesList** *(list) --* 
              An array of template list items containing metadata about your saved templates.
              - *(dict) --* 
                An object specifying metadata associated with a backup plan template.
                - **BackupPlanTemplateId** *(string) --* 
                  Uniquely identifies a stored backup plan template.
                - **BackupPlanTemplateName** *(string) --* 
                  The optional display name of a backup plan template.
        :type NextToken: string
        :param NextToken:
          The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of items to be returned.
        :rtype: dict
        :returns:
        """
        pass

    def list_backup_plan_versions(self, BackupPlanId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Returns version metadata of your backup plans, including Amazon Resource Names (ARNs), backup plan IDs, creation and deletion dates, plan names, and version IDs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ListBackupPlanVersions>`_
        
        **Request Syntax**
        ::
          response = client.list_backup_plan_versions(
              BackupPlanId='string',
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'NextToken': 'string',
                'BackupPlanVersionsList': [
                    {
                        'BackupPlanArn': 'string',
                        'BackupPlanId': 'string',
                        'CreationDate': datetime(2015, 1, 1),
                        'DeletionDate': datetime(2015, 1, 1),
                        'VersionId': 'string',
                        'BackupPlanName': 'string',
                        'CreatorRequestId': 'string',
                        'LastExecutionDate': datetime(2015, 1, 1)
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NextToken** *(string) --* 
              The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
            - **BackupPlanVersionsList** *(list) --* 
              An array of version list items containing metadata about your backup plans.
              - *(dict) --* 
                Contains metadata about a backup plan.
                - **BackupPlanArn** *(string) --* 
                  An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .
                - **BackupPlanId** *(string) --* 
                  Uniquely identifies a backup plan.
                - **CreationDate** *(datetime) --* 
                  The date and time a resource backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **DeletionDate** *(datetime) --* 
                  The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of ``DeletionDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **VersionId** *(string) --* 
                  Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.
                - **BackupPlanName** *(string) --* 
                  The display name of a saved backup plan.
                - **CreatorRequestId** *(string) --* 
                  A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.
                - **LastExecutionDate** *(datetime) --* 
                  The last time a job to back up resources was executed with this rule. A date and time, in Unix format and Coordinated Universal Time (UTC). The value of ``LastExecutionDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
        :type BackupPlanId: string
        :param BackupPlanId: **[REQUIRED]**
          Uniquely identifies a backup plan.
        :type NextToken: string
        :param NextToken:
          The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of items to be returned.
        :rtype: dict
        :returns:
        """
        pass

    def list_backup_plans(self, NextToken: str = None, MaxResults: int = None, IncludeDeleted: bool = None) -> Dict:
        """
        Returns metadata of your saved backup plans, including Amazon Resource Names (ARNs), plan IDs, creation and deletion dates, version IDs, plan names, and creator request IDs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ListBackupPlans>`_
        
        **Request Syntax**
        ::
          response = client.list_backup_plans(
              NextToken='string',
              MaxResults=123,
              IncludeDeleted=True|False
          )
        
        **Response Syntax**
        ::
            {
                'NextToken': 'string',
                'BackupPlansList': [
                    {
                        'BackupPlanArn': 'string',
                        'BackupPlanId': 'string',
                        'CreationDate': datetime(2015, 1, 1),
                        'DeletionDate': datetime(2015, 1, 1),
                        'VersionId': 'string',
                        'BackupPlanName': 'string',
                        'CreatorRequestId': 'string',
                        'LastExecutionDate': datetime(2015, 1, 1)
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NextToken** *(string) --* 
              The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
            - **BackupPlansList** *(list) --* 
              An array of backup plan list items containing metadata about your saved backup plans.
              - *(dict) --* 
                Contains metadata about a backup plan.
                - **BackupPlanArn** *(string) --* 
                  An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .
                - **BackupPlanId** *(string) --* 
                  Uniquely identifies a backup plan.
                - **CreationDate** *(datetime) --* 
                  The date and time a resource backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **DeletionDate** *(datetime) --* 
                  The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of ``DeletionDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **VersionId** *(string) --* 
                  Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.
                - **BackupPlanName** *(string) --* 
                  The display name of a saved backup plan.
                - **CreatorRequestId** *(string) --* 
                  A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.
                - **LastExecutionDate** *(datetime) --* 
                  The last time a job to back up resources was executed with this rule. A date and time, in Unix format and Coordinated Universal Time (UTC). The value of ``LastExecutionDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
        :type NextToken: string
        :param NextToken:
          The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of items to be returned.
        :type IncludeDeleted: boolean
        :param IncludeDeleted:
          A Boolean value with a default value of ``FALSE`` that returns deleted backup plans when set to ``TRUE`` .
        :rtype: dict
        :returns:
        """
        pass

    def list_backup_selections(self, BackupPlanId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Returns an array containing metadata of the resources associated with the target backup plan.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ListBackupSelections>`_
        
        **Request Syntax**
        ::
          response = client.list_backup_selections(
              BackupPlanId='string',
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'NextToken': 'string',
                'BackupSelectionsList': [
                    {
                        'SelectionId': 'string',
                        'SelectionName': 'string',
                        'BackupPlanId': 'string',
                        'CreationDate': datetime(2015, 1, 1),
                        'CreatorRequestId': 'string',
                        'IamRoleArn': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NextToken** *(string) --* 
              The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
            - **BackupSelectionsList** *(list) --* 
              An array of backup selection list items containing metadata about each resource in the list.
              - *(dict) --* 
                Contains metadata about a ``BackupSelection`` object.
                - **SelectionId** *(string) --* 
                  Uniquely identifies a request to assign a set of resources to a backup plan.
                - **SelectionName** *(string) --* 
                  The display name of a resource selection document.
                - **BackupPlanId** *(string) --* 
                  Uniquely identifies a backup plan.
                - **CreationDate** *(datetime) --* 
                  The date and time a backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **CreatorRequestId** *(string) --* 
                  A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.
                - **IamRoleArn** *(string) --* 
                  Specifies the IAM role Amazon Resource Name (ARN) to create the target recovery point; for example, ``arn:aws:iam::123456789012:role/S3Access`` .
        :type BackupPlanId: string
        :param BackupPlanId: **[REQUIRED]**
          Uniquely identifies a backup plan.
        :type NextToken: string
        :param NextToken:
          The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of items to be returned.
        :rtype: dict
        :returns:
        """
        pass

    def list_backup_vaults(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Returns a list of recovery point storage containers along with information about them.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ListBackupVaults>`_
        
        **Request Syntax**
        ::
          response = client.list_backup_vaults(
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'BackupVaultList': [
                    {
                        'BackupVaultName': 'string',
                        'BackupVaultArn': 'string',
                        'CreationDate': datetime(2015, 1, 1),
                        'EncryptionKeyArn': 'string',
                        'CreatorRequestId': 'string',
                        'NumberOfRecoveryPoints': 123
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupVaultList** *(list) --* 
              An array of backup vault list members containing vault metadata, including Amazon Resource Name (ARN), display name, creation date, number of saved recovery points, and encryption information if the resources saved in the backup vault are encrypted.
              - *(dict) --* 
                Contains metadata about a backup vault.
                - **BackupVaultName** *(string) --* 
                  The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
                - **BackupVaultArn** *(string) --* 
                  An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .
                - **CreationDate** *(datetime) --* 
                  The date and time a resource backup is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **EncryptionKeyArn** *(string) --* 
                  The server-side encryption key that is used to protect your backups; for example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .
                - **CreatorRequestId** *(string) --* 
                  A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.
                - **NumberOfRecoveryPoints** *(integer) --* 
                  The number of recovery points that are stored in a backup vault.
            - **NextToken** *(string) --* 
              The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type NextToken: string
        :param NextToken:
          The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of items to be returned.
        :rtype: dict
        :returns:
        """
        pass

    def list_protected_resources(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Returns an array of resources successfully backed up by AWS Backup, including the time the resource was saved, an Amazon Resource Name (ARN) of the resource, and a resource type.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ListProtectedResources>`_
        
        **Request Syntax**
        ::
          response = client.list_protected_resources(
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'Results': [
                    {
                        'ResourceArn': 'string',
                        'ResourceType': 'string',
                        'LastBackupTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Results** *(list) --* 
              An array of resources successfully backed up by AWS Backup including the time the resource was saved, an Amazon Resource Name (ARN) of the resource, and a resource type.
              - *(dict) --* 
                A structure that contains information about a backed-up resource.
                - **ResourceArn** *(string) --* 
                  An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
                - **ResourceType** *(string) --* 
                  The type of AWS resource; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.
                - **LastBackupTime** *(datetime) --* 
                  The date and time a resource was last backed up, in Unix format and Coordinated Universal Time (UTC). The value of ``LastBackupTime`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **NextToken** *(string) --* 
              The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type NextToken: string
        :param NextToken:
          The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of items to be returned.
        :rtype: dict
        :returns:
        """
        pass

    def list_recovery_points_by_backup_vault(self, BackupVaultName: str, NextToken: str = None, MaxResults: int = None, ByResourceArn: str = None, ByResourceType: str = None, ByBackupPlanId: str = None, ByCreatedBefore: datetime = None, ByCreatedAfter: datetime = None) -> Dict:
        """
        Returns detailed information about the recovery points stored in a backup vault.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ListRecoveryPointsByBackupVault>`_
        
        **Request Syntax**
        ::
          response = client.list_recovery_points_by_backup_vault(
              BackupVaultName='string',
              NextToken='string',
              MaxResults=123,
              ByResourceArn='string',
              ByResourceType='string',
              ByBackupPlanId='string',
              ByCreatedBefore=datetime(2015, 1, 1),
              ByCreatedAfter=datetime(2015, 1, 1)
          )
        
        **Response Syntax**
        ::
            {
                'NextToken': 'string',
                'RecoveryPoints': [
                    {
                        'RecoveryPointArn': 'string',
                        'BackupVaultName': 'string',
                        'BackupVaultArn': 'string',
                        'ResourceArn': 'string',
                        'ResourceType': 'string',
                        'CreatedBy': {
                            'BackupPlanId': 'string',
                            'BackupPlanArn': 'string',
                            'BackupPlanVersion': 'string',
                            'BackupRuleId': 'string'
                        },
                        'IamRoleArn': 'string',
                        'Status': 'COMPLETED'|'PARTIAL'|'DELETING'|'EXPIRED',
                        'CreationDate': datetime(2015, 1, 1),
                        'CompletionDate': datetime(2015, 1, 1),
                        'BackupSizeInBytes': 123,
                        'CalculatedLifecycle': {
                            'MoveToColdStorageAt': datetime(2015, 1, 1),
                            'DeleteAt': datetime(2015, 1, 1)
                        },
                        'Lifecycle': {
                            'MoveToColdStorageAfterDays': 123,
                            'DeleteAfterDays': 123
                        },
                        'EncryptionKeyArn': 'string',
                        'IsEncrypted': True|False,
                        'LastRestoreTime': datetime(2015, 1, 1)
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NextToken** *(string) --* 
              The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
            - **RecoveryPoints** *(list) --* 
              An array of objects that contain detailed information about recovery points saved in a backup vault.
              - *(dict) --* 
                Contains detailed information about the recovery points stored in a backup vault.
                - **RecoveryPointArn** *(string) --* 
                  An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
                - **BackupVaultName** *(string) --* 
                  The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
                - **BackupVaultArn** *(string) --* 
                  An ARN that uniquely identifies a backup vault; for example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .
                - **ResourceArn** *(string) --* 
                  An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.
                - **ResourceType** *(string) --* 
                  The type of AWS resource saved as a recovery point; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.
                - **CreatedBy** *(dict) --* 
                  Contains identifying information about the creation of a recovery point, including the ``BackupPlanArn`` , ``BackupPlanId`` , ``BackupPlanVersion`` , and ``BackupRuleId`` of the backup plan that is used to create it.
                  - **BackupPlanId** *(string) --* 
                    Uniquely identifies a backup plan.
                  - **BackupPlanArn** *(string) --* 
                    An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .
                  - **BackupPlanVersion** *(string) --* 
                    Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.
                  - **BackupRuleId** *(string) --* 
                    Uniquely identifies a rule used to schedule the backup of a selection of resources.
                - **IamRoleArn** *(string) --* 
                  Specifies the IAM role ARN used to create the target recovery point; for example, ``arn:aws:iam::123456789012:role/S3Access`` .
                - **Status** *(string) --* 
                  A status code specifying the state of the recovery point.
                - **CreationDate** *(datetime) --* 
                  The date and time a recovery point is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **CompletionDate** *(datetime) --* 
                  The date and time a job to restore a recovery point is completed, in Unix format and Coordinated Universal Time (UTC). The value of ``CompletionDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **BackupSizeInBytes** *(integer) --* 
                  The size, in bytes, of a backup.
                - **CalculatedLifecycle** *(dict) --* 
                  A ``CalculatedLifecycle`` object containing ``DeleteAt`` and ``MoveToColdStorageAt`` timestamps.
                  - **MoveToColdStorageAt** *(datetime) --* 
                    A timestamp that specifies when to transition a recovery point to cold storage.
                  - **DeleteAt** *(datetime) --* 
                    A timestamp that specifies when to delete a recovery point.
                - **Lifecycle** *(dict) --* 
                  The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define. 
                  Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. 
                  - **MoveToColdStorageAfterDays** *(integer) --* 
                    Specifies the number of days after creation that a recovery point is moved to cold storage.
                  - **DeleteAfterDays** *(integer) --* 
                    Specifies the number of days after creation that a recovery point is deleted. Must be greater than ``MoveToColdStorageAfterDays`` .
                - **EncryptionKeyArn** *(string) --* 
                  The server-side encryption key that is used to protect your backups; for example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .
                - **IsEncrypted** *(boolean) --* 
                  A Boolean value that is returned as ``TRUE`` if the specified recovery point is encrypted, or ``FALSE`` if the recovery point is not encrypted.
                - **LastRestoreTime** *(datetime) --* 
                  The date and time a recovery point was last restored, in Unix format and Coordinated Universal Time (UTC). The value of ``LastRestoreTime`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :type NextToken: string
        :param NextToken:
          The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of items to be returned.
        :type ByResourceArn: string
        :param ByResourceArn:
          Returns only recovery points that match the specified resource Amazon Resource Name (ARN).
        :type ByResourceType: string
        :param ByResourceType:
          Returns only recovery points that match the specified resource type.
        :type ByBackupPlanId: string
        :param ByBackupPlanId:
          Returns only recovery points that match the specified backup plan ID.
        :type ByCreatedBefore: datetime
        :param ByCreatedBefore:
          Returns only recovery points that were created before the specified timestamp.
        :type ByCreatedAfter: datetime
        :param ByCreatedAfter:
          Returns only recovery points that were created after the specified timestamp.
        :rtype: dict
        :returns:
        """
        pass

    def list_recovery_points_by_resource(self, ResourceArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Returns detailed information about recovery points of the type specified by a resource Amazon Resource Name (ARN).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ListRecoveryPointsByResource>`_
        
        **Request Syntax**
        ::
          response = client.list_recovery_points_by_resource(
              ResourceArn='string',
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'NextToken': 'string',
                'RecoveryPoints': [
                    {
                        'RecoveryPointArn': 'string',
                        'CreationDate': datetime(2015, 1, 1),
                        'Status': 'COMPLETED'|'PARTIAL'|'DELETING'|'EXPIRED',
                        'EncryptionKeyArn': 'string',
                        'BackupSizeBytes': 123,
                        'BackupVaultName': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NextToken** *(string) --* 
              The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
            - **RecoveryPoints** *(list) --* 
              An array of objects that contain detailed information about recovery points of the specified resource type.
              - *(dict) --* 
                Contains detailed information about a saved recovery point.
                - **RecoveryPointArn** *(string) --* 
                  An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
                - **CreationDate** *(datetime) --* 
                  The date and time a recovery point is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **Status** *(string) --* 
                  A status code specifying the state of the recovery point.
                - **EncryptionKeyArn** *(string) --* 
                  The server-side encryption key that is used to protect your backups; for example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .
                - **BackupSizeBytes** *(integer) --* 
                  The size, in bytes, of a backup.
                - **BackupVaultName** *(string) --* 
                  The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.
        :type NextToken: string
        :param NextToken:
          The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of items to be returned.
        :rtype: dict
        :returns:
        """
        pass

    def list_restore_jobs(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Returns a list of jobs that AWS Backup initiated to restore a saved resource, including metadata about the recovery process.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ListRestoreJobs>`_
        
        **Request Syntax**
        ::
          response = client.list_restore_jobs(
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'RestoreJobs': [
                    {
                        'RestoreJobId': 'string',
                        'RecoveryPointArn': 'string',
                        'CreationDate': datetime(2015, 1, 1),
                        'CompletionDate': datetime(2015, 1, 1),
                        'Status': 'PENDING'|'RUNNING'|'COMPLETED'|'ABORTED'|'FAILED',
                        'StatusMessage': 'string',
                        'PercentDone': 'string',
                        'BackupSizeInBytes': 123,
                        'IamRoleArn': 'string',
                        'ExpectedCompletionTimeMinutes': 123,
                        'CreatedResourceArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RestoreJobs** *(list) --* 
              An array of objects that contain detailed information about jobs to restore saved resources.
              - *(dict) --* 
                Contains metadata about a restore job.
                - **RestoreJobId** *(string) --* 
                  Uniquely identifies the job that restores a recovery point.
                - **RecoveryPointArn** *(string) --* 
                  An ARN that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
                - **CreationDate** *(datetime) --* 
                  The date and time a restore job is created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **CompletionDate** *(datetime) --* 
                  The date and time a job to restore a recovery point is completed, in Unix format and Coordinated Universal Time (UTC). The value of ``CompletionDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
                - **Status** *(string) --* 
                  A status code specifying the state of the job initiated by AWS Backup to restore a recovery point.
                - **StatusMessage** *(string) --* 
                  A detailed message explaining the status of the job to restore a recovery point.
                - **PercentDone** *(string) --* 
                  Contains an estimated percentage complete of a job at the time the job status was queried.
                - **BackupSizeInBytes** *(integer) --* 
                  The size, in bytes, of the restored resource.
                - **IamRoleArn** *(string) --* 
                  Specifies the IAM role ARN used to create the target recovery point; for example, ``arn:aws:iam::123456789012:role/S3Access`` .
                - **ExpectedCompletionTimeMinutes** *(integer) --* 
                  The amount of time in minutes that a job restoring a recovery point is expected to take.
                - **CreatedResourceArn** *(string) --* 
                  An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
            - **NextToken** *(string) --* 
              The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type NextToken: string
        :param NextToken:
          The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of items to be returned.
        :rtype: dict
        :returns:
        """
        pass

    def list_tags(self, ResourceArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Returns a list of key-value pairs assigned to a target recovery point, backup plan, or backup vault.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ListTags>`_
        
        **Request Syntax**
        ::
          response = client.list_tags(
              ResourceArn='string',
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'NextToken': 'string',
                'Tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NextToken** *(string) --* 
              The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
            - **Tags** *(dict) --* 
              To help organize your resources, you can assign your own metadata to the resources you create. Each tag is a key-value pair.
              - *(string) --* 
                - *(string) --* 
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the type of resource. Valid targets for ``ListTags`` are recovery points, backup plans, and backup vaults.
        :type NextToken: string
        :param NextToken:
          The next item following a partial list of returned items. For example, if a request is made to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in your list starting at the location pointed to by the next token.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of items to be returned.
        :rtype: dict
        :returns:
        """
        pass

    def put_backup_vault_access_policy(self, BackupVaultName: str, Policy: str = None):
        """
        Sets a resource-based policy that is used to manage access permissions on the target backup vault. Requires a backup vault name and an access policy document in JSON format.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/PutBackupVaultAccessPolicy>`_
        
        **Request Syntax**
        ::
          response = client.put_backup_vault_access_policy(
              BackupVaultName='string',
              Policy='string'
          )
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :type Policy: string
        :param Policy:
          The backup vault access policy document in JSON format.
        :returns: None
        """
        pass

    def put_backup_vault_notifications(self, BackupVaultName: str, SNSTopicArn: str, BackupVaultEvents: List):
        """
        Turns on notifications on a backup vault for the specified topic and events.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/PutBackupVaultNotifications>`_
        
        **Request Syntax**
        ::
          response = client.put_backup_vault_notifications(
              BackupVaultName='string',
              SNSTopicArn='string',
              BackupVaultEvents=[
                  'BACKUP_JOB_STARTED'|'BACKUP_JOB_COMPLETED'|'RESTORE_JOB_STARTED'|'RESTORE_JOB_COMPLETED'|'RECOVERY_POINT_MODIFIED'|'BACKUP_PLAN_CREATED'|'BACKUP_PLAN_MODIFIED',
              ]
          )
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :type SNSTopicArn: string
        :param SNSTopicArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that specifies the topic for a backup vault’s events; for example, ``arn:aws:sns:us-west-2:111122223333:MyVaultTopic`` .
        :type BackupVaultEvents: list
        :param BackupVaultEvents: **[REQUIRED]**
          An array of events that indicate the status of jobs to back up resources to the backup vault.
          - *(string) --*
        :returns: None
        """
        pass

    def start_backup_job(self, BackupVaultName: str, ResourceArn: str, IamRoleArn: str, IdempotencyToken: str = None, StartWindowMinutes: int = None, CompleteWindowMinutes: int = None, Lifecycle: Dict = None, RecoveryPointTags: Dict = None) -> Dict:
        """
        Starts a job to create a one-time backup of the specified resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/StartBackupJob>`_
        
        **Request Syntax**
        ::
          response = client.start_backup_job(
              BackupVaultName='string',
              ResourceArn='string',
              IamRoleArn='string',
              IdempotencyToken='string',
              StartWindowMinutes=123,
              CompleteWindowMinutes=123,
              Lifecycle={
                  'MoveToColdStorageAfterDays': 123,
                  'DeleteAfterDays': 123
              },
              RecoveryPointTags={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'BackupJobId': 'string',
                'RecoveryPointArn': 'string',
                'CreationDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupJobId** *(string) --* 
              Uniquely identifies a request to AWS Backup to back up a resource.
            - **RecoveryPointArn** *(string) --* 
              An ARN that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
            - **CreationDate** *(datetime) --* 
              The date and time that a backup job is started, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
        :type IamRoleArn: string
        :param IamRoleArn: **[REQUIRED]**
          Specifies the IAM role ARN used to create the target recovery point; for example, ``arn:aws:iam::123456789012:role/S3Access`` .
        :type IdempotencyToken: string
        :param IdempotencyToken:
          A customer chosen string that can be used to distinguish between calls to ``StartBackupJob`` . Idempotency tokens time out after one hour. Therefore, if you call ``StartBackupJob`` multiple times with the same idempotency token within one hour, AWS Backup recognizes that you are requesting only one backup job and initiates only one. If you change the idempotency token for each call, AWS Backup recognizes that you are requesting to start multiple backups.
        :type StartWindowMinutes: integer
        :param StartWindowMinutes:
          The amount of time in minutes before beginning a backup.
        :type CompleteWindowMinutes: integer
        :param CompleteWindowMinutes:
          The amount of time AWS Backup attempts a backup before canceling the job and returning an error.
        :type Lifecycle: dict
        :param Lifecycle:
          The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup will transition and expire backups automatically according to the lifecycle that you define.
          Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold.
          - **MoveToColdStorageAfterDays** *(integer) --*
            Specifies the number of days after creation that a recovery point is moved to cold storage.
          - **DeleteAfterDays** *(integer) --*
            Specifies the number of days after creation that a recovery point is deleted. Must be greater than ``MoveToColdStorageAfterDays`` .
        :type RecoveryPointTags: dict
        :param RecoveryPointTags:
          To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair.
          - *(string) --*
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def start_restore_job(self, RecoveryPointArn: str, Metadata: Dict, IamRoleArn: str, IdempotencyToken: str = None, ResourceType: str = None) -> Dict:
        """
        Recovers the saved resource identified by an Amazon Resource Name (ARN). 
        If the resource ARN is included in the request, then the last complete backup of that resource is recovered. If the ARN of a recovery point is supplied, then that recovery point is restored.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/StartRestoreJob>`_
        
        **Request Syntax**
        ::
          response = client.start_restore_job(
              RecoveryPointArn='string',
              Metadata={
                  'string': 'string'
              },
              IamRoleArn='string',
              IdempotencyToken='string',
              ResourceType='string'
          )
        
        **Response Syntax**
        ::
            {
                'RestoreJobId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RestoreJobId** *(string) --* 
              Uniquely identifies the job that restores a recovery point.
        :type RecoveryPointArn: string
        :param RecoveryPointArn: **[REQUIRED]**
          An ARN that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
        :type Metadata: dict
        :param Metadata: **[REQUIRED]**
          A set of metadata key-value pairs. Lists the metadata that the recovery point was created with.
          - *(string) --*
            - *(string) --*
        :type IamRoleArn: string
        :param IamRoleArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the IAM role that AWS Backup uses to create the target recovery point; for example, ``arn:aws:iam::123456789012:role/S3Access`` .
        :type IdempotencyToken: string
        :param IdempotencyToken:
          A customer chosen string that can be used to distinguish between calls to ``StartRestoreJob`` . Idempotency tokens time out after one hour. Therefore, if you call ``StartRestoreJob`` multiple times with the same idempotency token within one hour, AWS Backup recognizes that you are requesting only one restore job and initiates only one. If you change the idempotency token for each call, AWS Backup recognizes that you are requesting to start multiple restores.
        :type ResourceType: string
        :param ResourceType:
          Starts a job to restore a recovery point for one of the following resources:
          * ``EBS`` for Amazon Elastic Block Store
          * ``SGW`` for AWS Storage Gateway
          * ``RDS`` for Amazon Relational Database Service
          * ``DDB`` for Amazon DynamoDB
          * ``EFS`` for Amazon Elastic File System
        :rtype: dict
        :returns:
        """
        pass

    def stop_backup_job(self, BackupJobId: str):
        """
        Attempts to cancel a job to create a one-time backup of a resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/StopBackupJob>`_
        
        **Request Syntax**
        ::
          response = client.stop_backup_job(
              BackupJobId='string'
          )
        :type BackupJobId: string
        :param BackupJobId: **[REQUIRED]**
          Uniquely identifies a request to AWS Backup to back up a resource.
        :returns: None
        """
        pass

    def tag_resource(self, ResourceArn: str, Tags: Dict):
        """
        Assigns a set of key-value pairs to a recovery point, backup plan, or backup vault identified by an Amazon Resource Name (ARN).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/TagResource>`_
        
        **Request Syntax**
        ::
          response = client.tag_resource(
              ResourceArn='string',
              Tags={
                  'string': 'string'
              }
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          An ARN that uniquely identifies a resource. The format of the ARN depends on the type of the tagged resource.
        :type Tags: dict
        :param Tags: **[REQUIRED]**
          Key-value pairs that are used to help organize your resources. You can assign your own metadata to the resources you create.
          - *(string) --*
            - *(string) --*
        :returns: None
        """
        pass

    def untag_resource(self, ResourceArn: str, TagKeyList: List):
        """
        Removes a set of key-value pairs from a recovery point, backup plan, or backup vault identified by an Amazon Resource Name (ARN)
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/UntagResource>`_
        
        **Request Syntax**
        ::
          response = client.untag_resource(
              ResourceArn='string',
              TagKeyList=[
                  'string',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**
          An ARN that uniquely identifies a resource. The format of the ARN depends on the type of the tagged resource.
        :type TagKeyList: list
        :param TagKeyList: **[REQUIRED]**
          A list of keys to identify which key-value tags to remove from a resource.
          - *(string) --*
        :returns: None
        """
        pass

    def update_backup_plan(self, BackupPlanId: str, BackupPlan: Dict) -> Dict:
        """
        Replaces the body of a saved backup plan identified by its ``backupPlanId`` with the input document in JSON format. The new version is uniquely identified by a ``VersionId`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/UpdateBackupPlan>`_
        
        **Request Syntax**
        ::
          response = client.update_backup_plan(
              BackupPlanId='string',
              BackupPlan={
                  'BackupPlanName': 'string',
                  'Rules': [
                      {
                          'RuleName': 'string',
                          'TargetBackupVaultName': 'string',
                          'ScheduleExpression': 'string',
                          'StartWindowMinutes': 123,
                          'CompletionWindowMinutes': 123,
                          'Lifecycle': {
                              'MoveToColdStorageAfterDays': 123,
                              'DeleteAfterDays': 123
                          },
                          'RecoveryPointTags': {
                              'string': 'string'
                          }
                      },
                  ]
              }
          )
        
        **Response Syntax**
        ::
            {
                'BackupPlanId': 'string',
                'BackupPlanArn': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'VersionId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupPlanId** *(string) --* 
              Uniquely identifies a backup plan.
            - **BackupPlanArn** *(string) --* 
              An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .
            - **CreationDate** *(datetime) --* 
              The date and time a backup plan is updated, in Unix format and Coordinated Universal Time (UTC). The value of ``CreationDate`` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
            - **VersionId** *(string) --* 
              Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version Ids cannot be edited.
        :type BackupPlanId: string
        :param BackupPlanId: **[REQUIRED]**
          Uniquely identifies a backup plan.
        :type BackupPlan: dict
        :param BackupPlan: **[REQUIRED]**
          Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of ``Rules`` .
          - **BackupPlanName** *(string) --* **[REQUIRED]**
            The display name of a backup plan.
          - **Rules** *(list) --* **[REQUIRED]**
            An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used to back up a selection of resources.
            - *(dict) --*
              Specifies a scheduled task used to back up a selection of resources.
              - **RuleName** *(string) --* **[REQUIRED]**
                >An optional display name for a backup rule.
              - **TargetBackupVaultName** *(string) --* **[REQUIRED]**
                The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
              - **ScheduleExpression** *(string) --*
                A CRON expression specifying when AWS Backup initiates a backup job.
              - **StartWindowMinutes** *(integer) --*
                The amount of time in minutes before beginning a backup.
              - **CompletionWindowMinutes** *(integer) --*
                The amount of time AWS Backup attempts a backup before canceling the job and returning an error.
              - **Lifecycle** *(dict) --*
                The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup will transition and expire backups automatically according to the lifecycle that you define.
                Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold after days”. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold.
                - **MoveToColdStorageAfterDays** *(integer) --*
                  Specifies the number of days after creation that a recovery point is moved to cold storage.
                - **DeleteAfterDays** *(integer) --*
                  Specifies the number of days after creation that a recovery point is deleted. Must be greater than ``MoveToColdStorageAfterDays`` .
              - **RecoveryPointTags** *(dict) --*
                To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair.
                - *(string) --*
                  - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_recovery_point_lifecycle(self, BackupVaultName: str, RecoveryPointArn: str, Lifecycle: Dict = None) -> Dict:
        """
        Sets the transition lifecycle of a recovery point.
        The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define. 
        Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/UpdateRecoveryPointLifecycle>`_
        
        **Request Syntax**
        ::
          response = client.update_recovery_point_lifecycle(
              BackupVaultName='string',
              RecoveryPointArn='string',
              Lifecycle={
                  'MoveToColdStorageAfterDays': 123,
                  'DeleteAfterDays': 123
              }
          )
        
        **Response Syntax**
        ::
            {
                'BackupVaultArn': 'string',
                'RecoveryPointArn': 'string',
                'Lifecycle': {
                    'MoveToColdStorageAfterDays': 123,
                    'DeleteAfterDays': 123
                },
                'CalculatedLifecycle': {
                    'MoveToColdStorageAt': datetime(2015, 1, 1),
                    'DeleteAt': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BackupVaultArn** *(string) --* 
              An ARN that uniquely identifies a backup vault; for example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .
            - **RecoveryPointArn** *(string) --* 
              An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
            - **Lifecycle** *(dict) --* 
              The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define. 
              Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. 
              - **MoveToColdStorageAfterDays** *(integer) --* 
                Specifies the number of days after creation that a recovery point is moved to cold storage.
              - **DeleteAfterDays** *(integer) --* 
                Specifies the number of days after creation that a recovery point is deleted. Must be greater than ``MoveToColdStorageAfterDays`` .
            - **CalculatedLifecycle** *(dict) --* 
              A ``CalculatedLifecycle`` object containing ``DeleteAt`` and ``MoveToColdStorageAt`` timestamps.
              - **MoveToColdStorageAt** *(datetime) --* 
                A timestamp that specifies when to transition a recovery point to cold storage.
              - **DeleteAt** *(datetime) --* 
                A timestamp that specifies when to delete a recovery point.
        :type BackupVaultName: string
        :param BackupVaultName: **[REQUIRED]**
          The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :type RecoveryPointArn: string
        :param RecoveryPointArn: **[REQUIRED]**
          An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`` .
        :type Lifecycle: dict
        :param Lifecycle:
          The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.
          Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold.
          - **MoveToColdStorageAfterDays** *(integer) --*
            Specifies the number of days after creation that a recovery point is moved to cold storage.
          - **DeleteAfterDays** *(integer) --*
            Specifies the number of days after creation that a recovery point is deleted. Must be greater than ``MoveToColdStorageAfterDays`` .
        :rtype: dict
        :returns:
        """
        pass
