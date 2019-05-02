from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
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

    def create_job(self, AccountId: str, Operation: Dict, Report: Dict, ClientRequestToken: str, Manifest: Dict, Priority: int, RoleArn: str, ConfirmationRequired: bool = None, Description: str = None) -> Dict:
        """
        Creates an Amazon S3 batch operations job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/CreateJob>`_
        
        **Request Syntax**
        ::
          response = client.create_job(
              AccountId='string',
              ConfirmationRequired=True|False,
              Operation={
                  'LambdaInvoke': {
                      'FunctionArn': 'string'
                  },
                  'S3PutObjectCopy': {
                      'TargetResource': 'string',
                      'CannedAccessControlList': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control',
                      'AccessControlGrants': [
                          {
                              'Grantee': {
                                  'TypeIdentifier': 'id'|'emailAddress'|'uri',
                                  'Identifier': 'string',
                                  'DisplayName': 'string'
                              },
                              'Permission': 'FULL_CONTROL'|'READ'|'WRITE'|'READ_ACP'|'WRITE_ACP'
                          },
                      ],
                      'MetadataDirective': 'COPY'|'REPLACE',
                      'ModifiedSinceConstraint': datetime(2015, 1, 1),
                      'NewObjectMetadata': {
                          'CacheControl': 'string',
                          'ContentDisposition': 'string',
                          'ContentEncoding': 'string',
                          'ContentLanguage': 'string',
                          'UserMetadata': {
                              'string': 'string'
                          },
                          'ContentLength': 123,
                          'ContentMD5': 'string',
                          'ContentType': 'string',
                          'HttpExpiresDate': datetime(2015, 1, 1),
                          'RequesterCharged': True|False,
                          'SSEAlgorithm': 'AES256'|'KMS'
                      },
                      'NewObjectTagging': [
                          {
                              'Key': 'string',
                              'Value': 'string'
                          },
                      ],
                      'RedirectLocation': 'string',
                      'RequesterPays': True|False,
                      'StorageClass': 'STANDARD'|'STANDARD_IA'|'ONEZONE_IA'|'GLACIER'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
                      'UnModifiedSinceConstraint': datetime(2015, 1, 1),
                      'SSEAwsKmsKeyId': 'string',
                      'TargetKeyPrefix': 'string',
                      'ObjectLockLegalHoldStatus': 'OFF'|'ON',
                      'ObjectLockMode': 'COMPLIANCE'|'GOVERNANCE',
                      'ObjectLockRetainUntilDate': datetime(2015, 1, 1)
                  },
                  'S3PutObjectAcl': {
                      'AccessControlPolicy': {
                          'AccessControlList': {
                              'Owner': {
                                  'ID': 'string',
                                  'DisplayName': 'string'
                              },
                              'Grants': [
                                  {
                                      'Grantee': {
                                          'TypeIdentifier': 'id'|'emailAddress'|'uri',
                                          'Identifier': 'string',
                                          'DisplayName': 'string'
                                      },
                                      'Permission': 'FULL_CONTROL'|'READ'|'WRITE'|'READ_ACP'|'WRITE_ACP'
                                  },
                              ]
                          },
                          'CannedAccessControlList': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'
                      }
                  },
                  'S3PutObjectTagging': {
                      'TagSet': [
                          {
                              'Key': 'string',
                              'Value': 'string'
                          },
                      ]
                  },
                  'S3InitiateRestoreObject': {
                      'ExpirationInDays': 123,
                      'GlacierJobTier': 'BULK'|'STANDARD'
                  }
              },
              Report={
                  'Bucket': 'string',
                  'Format': 'Report_CSV_20180820',
                  'Enabled': True|False,
                  'Prefix': 'string',
                  'ReportScope': 'AllTasks'|'FailedTasksOnly'
              },
              ClientRequestToken='string',
              Manifest={
                  'Spec': {
                      'Format': 'S3BatchOperations_CSV_20180820'|'S3InventoryReport_CSV_20161130',
                      'Fields': [
                          'Ignore'|'Bucket'|'Key'|'VersionId',
                      ]
                  },
                  'Location': {
                      'ObjectArn': 'string',
                      'ObjectVersionId': 'string',
                      'ETag': 'string'
                  }
              },
              Description='string',
              Priority=123,
              RoleArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'JobId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **JobId** *(string) --* 
              The ID for this job. Amazon S3 generates this ID automatically and returns it after a successful ``Create Job`` request.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
        :type ConfirmationRequired: boolean
        :param ConfirmationRequired:
          Indicates whether confirmation is required before Amazon S3 runs the job. Confirmation is only required for jobs created through the Amazon S3 console.
        :type Operation: dict
        :param Operation: **[REQUIRED]**
          The operation that you want this job to perform on each object listed in the manifest. For more information about the available operations, see `Available Operations <https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-operations.html>`__ in the *Amazon Simple Storage Service Developer Guide* .
          - **LambdaInvoke** *(dict) --*
            Directs the specified job to invoke an AWS Lambda function on each object in the manifest.
            - **FunctionArn** *(string) --*
              The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will invoke for each object in the manifest.
          - **S3PutObjectCopy** *(dict) --*
            Directs the specified job to execute a PUT Copy object call on each object in the manifest.
            - **TargetResource** *(string) --*
            - **CannedAccessControlList** *(string) --*
            - **AccessControlGrants** *(list) --*
              - *(dict) --*
                - **Grantee** *(dict) --*
                  - **TypeIdentifier** *(string) --*
                  - **Identifier** *(string) --*
                  - **DisplayName** *(string) --*
                - **Permission** *(string) --*
            - **MetadataDirective** *(string) --*
            - **ModifiedSinceConstraint** *(datetime) --*
            - **NewObjectMetadata** *(dict) --*
              - **CacheControl** *(string) --*
              - **ContentDisposition** *(string) --*
              - **ContentEncoding** *(string) --*
              - **ContentLanguage** *(string) --*
              - **UserMetadata** *(dict) --*
                - *(string) --*
                  - *(string) --*
              - **ContentLength** *(integer) --*
              - **ContentMD5** *(string) --*
              - **ContentType** *(string) --*
              - **HttpExpiresDate** *(datetime) --*
              - **RequesterCharged** *(boolean) --*
              - **SSEAlgorithm** *(string) --*
            - **NewObjectTagging** *(list) --*
              - *(dict) --*
                - **Key** *(string) --* **[REQUIRED]**
                - **Value** *(string) --* **[REQUIRED]**
            - **RedirectLocation** *(string) --*
            - **RequesterPays** *(boolean) --*
            - **StorageClass** *(string) --*
            - **UnModifiedSinceConstraint** *(datetime) --*
            - **SSEAwsKmsKeyId** *(string) --*
            - **TargetKeyPrefix** *(string) --*
            - **ObjectLockLegalHoldStatus** *(string) --*
            - **ObjectLockMode** *(string) --*
            - **ObjectLockRetainUntilDate** *(datetime) --*
          - **S3PutObjectAcl** *(dict) --*
            Directs the specified job to execute a PUT Object acl call on each object in the manifest.
            - **AccessControlPolicy** *(dict) --*
              - **AccessControlList** *(dict) --*
                - **Owner** *(dict) --* **[REQUIRED]**
                  - **ID** *(string) --*
                  - **DisplayName** *(string) --*
                - **Grants** *(list) --*
                  - *(dict) --*
                    - **Grantee** *(dict) --*
                      - **TypeIdentifier** *(string) --*
                      - **Identifier** *(string) --*
                      - **DisplayName** *(string) --*
                    - **Permission** *(string) --*
              - **CannedAccessControlList** *(string) --*
          - **S3PutObjectTagging** *(dict) --*
            Directs the specified job to execute a PUT Object tagging call on each object in the manifest.
            - **TagSet** *(list) --*
              - *(dict) --*
                - **Key** *(string) --* **[REQUIRED]**
                - **Value** *(string) --* **[REQUIRED]**
          - **S3InitiateRestoreObject** *(dict) --*
            Directs the specified job to execute an Initiate Glacier Restore call on each object in the manifest.
            - **ExpirationInDays** *(integer) --*
            - **GlacierJobTier** *(string) --*
        :type Report: dict
        :param Report: **[REQUIRED]**
          Configuration parameters for the optional job-completion report.
          - **Bucket** *(string) --*
            The bucket where specified job-completion report will be stored.
          - **Format** *(string) --*
            The format of the specified job-completion report.
          - **Enabled** *(boolean) --* **[REQUIRED]**
            Indicates whether the specified job will generate a job-completion report.
          - **Prefix** *(string) --*
            An optional prefix to describe where in the specified bucket the job-completion report will be stored. Amazon S3 will store the job-completion report at <prefix>/job-<job-id>/report.json.
          - **ReportScope** *(string) --*
            Indicates whether the job-completion report will include details of all tasks or only failed tasks.
        :type ClientRequestToken: string
        :param ClientRequestToken: **[REQUIRED]**
          An idempotency token to ensure that you don\'t accidentally submit the same request twice. You can use any string up to the maximum length.
          This field is autopopulated if not provided.
        :type Manifest: dict
        :param Manifest: **[REQUIRED]**
          Configuration parameters for the manifest.
          - **Spec** *(dict) --* **[REQUIRED]**
            Describes the format of the specified job\'s manifest. If the manifest is in CSV format, also describes the columns contained within the manifest.
            - **Format** *(string) --* **[REQUIRED]**
              Indicates which of the available formats the specified manifest uses.
            - **Fields** *(list) --*
              If the specified manifest object is in the ``S3BatchOperations_CSV_20180820`` format, this element describes which columns contain the required data.
              - *(string) --*
          - **Location** *(dict) --* **[REQUIRED]**
            Contains the information required to locate the specified job\'s manifest.
            - **ObjectArn** *(string) --* **[REQUIRED]**
              The Amazon Resource Name (ARN) for a manifest object.
            - **ObjectVersionId** *(string) --*
              The optional version ID to identify a specific version of the manifest object.
            - **ETag** *(string) --* **[REQUIRED]**
              The ETag for the specified manifest object.
        :type Description: string
        :param Description:
          A description for this job. You can use any string within the permitted length. Descriptions don\'t need to be unique and can be used for multiple jobs.
        :type Priority: integer
        :param Priority: **[REQUIRED]**
          The numerical priority for this job. Higher numbers indicate higher priority.
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) for the Identity and Access Management (IAM) Role that batch operations will use to execute this job\'s operation on each object in the manifest.
        :rtype: dict
        :returns:
        """
        pass

    def delete_public_access_block(self, AccountId: str):
        """
        Deletes the block public access configuration for the specified account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/DeletePublicAccessBlock>`_
        
        **Request Syntax**
        ::
          response = client.delete_public_access_block(
              AccountId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The account ID for the AWS account whose block public access configuration you want to delete.
        :returns: None
        """
        pass

    def describe_job(self, AccountId: str, JobId: str) -> Dict:
        """
        Retrieves the configuration parameters and status for a batch operations job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/DescribeJob>`_
        
        **Request Syntax**
        ::
          response = client.describe_job(
              AccountId='string',
              JobId='string'
          )
        
        **Response Syntax**
        ::
            {
                'Job': {
                    'JobId': 'string',
                    'ConfirmationRequired': True|False,
                    'Description': 'string',
                    'JobArn': 'string',
                    'Status': 'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'|'Failed'|'Failing'|'New'|'Paused'|'Pausing'|'Preparing'|'Ready'|'Suspended',
                    'Manifest': {
                        'Spec': {
                            'Format': 'S3BatchOperations_CSV_20180820'|'S3InventoryReport_CSV_20161130',
                            'Fields': [
                                'Ignore'|'Bucket'|'Key'|'VersionId',
                            ]
                        },
                        'Location': {
                            'ObjectArn': 'string',
                            'ObjectVersionId': 'string',
                            'ETag': 'string'
                        }
                    },
                    'Operation': {
                        'LambdaInvoke': {
                            'FunctionArn': 'string'
                        },
                        'S3PutObjectCopy': {
                            'TargetResource': 'string',
                            'CannedAccessControlList': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control',
                            'AccessControlGrants': [
                                {
                                    'Grantee': {
                                        'TypeIdentifier': 'id'|'emailAddress'|'uri',
                                        'Identifier': 'string',
                                        'DisplayName': 'string'
                                    },
                                    'Permission': 'FULL_CONTROL'|'READ'|'WRITE'|'READ_ACP'|'WRITE_ACP'
                                },
                            ],
                            'MetadataDirective': 'COPY'|'REPLACE',
                            'ModifiedSinceConstraint': datetime(2015, 1, 1),
                            'NewObjectMetadata': {
                                'CacheControl': 'string',
                                'ContentDisposition': 'string',
                                'ContentEncoding': 'string',
                                'ContentLanguage': 'string',
                                'UserMetadata': {
                                    'string': 'string'
                                },
                                'ContentLength': 123,
                                'ContentMD5': 'string',
                                'ContentType': 'string',
                                'HttpExpiresDate': datetime(2015, 1, 1),
                                'RequesterCharged': True|False,
                                'SSEAlgorithm': 'AES256'|'KMS'
                            },
                            'NewObjectTagging': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ],
                            'RedirectLocation': 'string',
                            'RequesterPays': True|False,
                            'StorageClass': 'STANDARD'|'STANDARD_IA'|'ONEZONE_IA'|'GLACIER'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
                            'UnModifiedSinceConstraint': datetime(2015, 1, 1),
                            'SSEAwsKmsKeyId': 'string',
                            'TargetKeyPrefix': 'string',
                            'ObjectLockLegalHoldStatus': 'OFF'|'ON',
                            'ObjectLockMode': 'COMPLIANCE'|'GOVERNANCE',
                            'ObjectLockRetainUntilDate': datetime(2015, 1, 1)
                        },
                        'S3PutObjectAcl': {
                            'AccessControlPolicy': {
                                'AccessControlList': {
                                    'Owner': {
                                        'ID': 'string',
                                        'DisplayName': 'string'
                                    },
                                    'Grants': [
                                        {
                                            'Grantee': {
                                                'TypeIdentifier': 'id'|'emailAddress'|'uri',
                                                'Identifier': 'string',
                                                'DisplayName': 'string'
                                            },
                                            'Permission': 'FULL_CONTROL'|'READ'|'WRITE'|'READ_ACP'|'WRITE_ACP'
                                        },
                                    ]
                                },
                                'CannedAccessControlList': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'
                            }
                        },
                        'S3PutObjectTagging': {
                            'TagSet': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        },
                        'S3InitiateRestoreObject': {
                            'ExpirationInDays': 123,
                            'GlacierJobTier': 'BULK'|'STANDARD'
                        }
                    },
                    'Priority': 123,
                    'ProgressSummary': {
                        'TotalNumberOfTasks': 123,
                        'NumberOfTasksSucceeded': 123,
                        'NumberOfTasksFailed': 123
                    },
                    'StatusUpdateReason': 'string',
                    'FailureReasons': [
                        {
                            'FailureCode': 'string',
                            'FailureReason': 'string'
                        },
                    ],
                    'Report': {
                        'Bucket': 'string',
                        'Format': 'Report_CSV_20180820',
                        'Enabled': True|False,
                        'Prefix': 'string',
                        'ReportScope': 'AllTasks'|'FailedTasksOnly'
                    },
                    'CreationTime': datetime(2015, 1, 1),
                    'TerminationDate': datetime(2015, 1, 1),
                    'RoleArn': 'string',
                    'SuspendedDate': datetime(2015, 1, 1),
                    'SuspendedCause': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Job** *(dict) --* 
              Contains the configuration parameters and status for the job specified in the ``Describe Job`` request.
              - **JobId** *(string) --* 
                The ID for the specified job.
              - **ConfirmationRequired** *(boolean) --* 
                Indicates whether confirmation is required before Amazon S3 begins running the specified job. Confirmation is required only for jobs created through the Amazon S3 console.
              - **Description** *(string) --* 
                The description for this job, if one was provided in this job's ``Create Job`` request.
              - **JobArn** *(string) --* 
                The Amazon Resource Name (ARN) for this job.
              - **Status** *(string) --* 
                The current status of the specified job.
              - **Manifest** *(dict) --* 
                The configuration information for the specified job's manifest object.
                - **Spec** *(dict) --* 
                  Describes the format of the specified job's manifest. If the manifest is in CSV format, also describes the columns contained within the manifest.
                  - **Format** *(string) --* 
                    Indicates which of the available formats the specified manifest uses.
                  - **Fields** *(list) --* 
                    If the specified manifest object is in the ``S3BatchOperations_CSV_20180820`` format, this element describes which columns contain the required data.
                    - *(string) --* 
                - **Location** *(dict) --* 
                  Contains the information required to locate the specified job's manifest.
                  - **ObjectArn** *(string) --* 
                    The Amazon Resource Name (ARN) for a manifest object.
                  - **ObjectVersionId** *(string) --* 
                    The optional version ID to identify a specific version of the manifest object.
                  - **ETag** *(string) --* 
                    The ETag for the specified manifest object.
              - **Operation** *(dict) --* 
                The operation that the specified job is configured to execute on the objects listed in the manifest.
                - **LambdaInvoke** *(dict) --* 
                  Directs the specified job to invoke an AWS Lambda function on each object in the manifest.
                  - **FunctionArn** *(string) --* 
                    The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will invoke for each object in the manifest.
                - **S3PutObjectCopy** *(dict) --* 
                  Directs the specified job to execute a PUT Copy object call on each object in the manifest.
                  - **TargetResource** *(string) --* 
                  - **CannedAccessControlList** *(string) --* 
                  - **AccessControlGrants** *(list) --* 
                    - *(dict) --* 
                      - **Grantee** *(dict) --* 
                        - **TypeIdentifier** *(string) --* 
                        - **Identifier** *(string) --* 
                        - **DisplayName** *(string) --* 
                      - **Permission** *(string) --* 
                  - **MetadataDirective** *(string) --* 
                  - **ModifiedSinceConstraint** *(datetime) --* 
                  - **NewObjectMetadata** *(dict) --* 
                    - **CacheControl** *(string) --* 
                    - **ContentDisposition** *(string) --* 
                    - **ContentEncoding** *(string) --* 
                    - **ContentLanguage** *(string) --* 
                    - **UserMetadata** *(dict) --* 
                      - *(string) --* 
                        - *(string) --* 
                    - **ContentLength** *(integer) --* 
                    - **ContentMD5** *(string) --* 
                    - **ContentType** *(string) --* 
                    - **HttpExpiresDate** *(datetime) --* 
                    - **RequesterCharged** *(boolean) --* 
                    - **SSEAlgorithm** *(string) --* 
                  - **NewObjectTagging** *(list) --* 
                    - *(dict) --* 
                      - **Key** *(string) --* 
                      - **Value** *(string) --* 
                  - **RedirectLocation** *(string) --* 
                  - **RequesterPays** *(boolean) --* 
                  - **StorageClass** *(string) --* 
                  - **UnModifiedSinceConstraint** *(datetime) --* 
                  - **SSEAwsKmsKeyId** *(string) --* 
                  - **TargetKeyPrefix** *(string) --* 
                  - **ObjectLockLegalHoldStatus** *(string) --* 
                  - **ObjectLockMode** *(string) --* 
                  - **ObjectLockRetainUntilDate** *(datetime) --* 
                - **S3PutObjectAcl** *(dict) --* 
                  Directs the specified job to execute a PUT Object acl call on each object in the manifest.
                  - **AccessControlPolicy** *(dict) --* 
                    - **AccessControlList** *(dict) --* 
                      - **Owner** *(dict) --* 
                        - **ID** *(string) --* 
                        - **DisplayName** *(string) --* 
                      - **Grants** *(list) --* 
                        - *(dict) --* 
                          - **Grantee** *(dict) --* 
                            - **TypeIdentifier** *(string) --* 
                            - **Identifier** *(string) --* 
                            - **DisplayName** *(string) --* 
                          - **Permission** *(string) --* 
                    - **CannedAccessControlList** *(string) --* 
                - **S3PutObjectTagging** *(dict) --* 
                  Directs the specified job to execute a PUT Object tagging call on each object in the manifest.
                  - **TagSet** *(list) --* 
                    - *(dict) --* 
                      - **Key** *(string) --* 
                      - **Value** *(string) --* 
                - **S3InitiateRestoreObject** *(dict) --* 
                  Directs the specified job to execute an Initiate Glacier Restore call on each object in the manifest.
                  - **ExpirationInDays** *(integer) --* 
                  - **GlacierJobTier** *(string) --* 
              - **Priority** *(integer) --* 
                The priority of the specified job.
              - **ProgressSummary** *(dict) --* 
                Describes the total number of tasks that the specified job has executed, the number of tasks that succeeded, and the number of tasks that failed.
                - **TotalNumberOfTasks** *(integer) --* 
                - **NumberOfTasksSucceeded** *(integer) --* 
                - **NumberOfTasksFailed** *(integer) --* 
              - **StatusUpdateReason** *(string) --* 
              - **FailureReasons** *(list) --* 
                If the specified job failed, this field contains information describing the failure.
                - *(dict) --* 
                  If this job failed, this element indicates why the job failed.
                  - **FailureCode** *(string) --* 
                    The failure code, if any, for the specified job.
                  - **FailureReason** *(string) --* 
                    The failure reason, if any, for the specified job.
              - **Report** *(dict) --* 
                Contains the configuration information for the job-completion report if you requested one in the ``Create Job`` request.
                - **Bucket** *(string) --* 
                  The bucket where specified job-completion report will be stored.
                - **Format** *(string) --* 
                  The format of the specified job-completion report.
                - **Enabled** *(boolean) --* 
                  Indicates whether the specified job will generate a job-completion report.
                - **Prefix** *(string) --* 
                  An optional prefix to describe where in the specified bucket the job-completion report will be stored. Amazon S3 will store the job-completion report at <prefix>/job-<job-id>/report.json.
                - **ReportScope** *(string) --* 
                  Indicates whether the job-completion report will include details of all tasks or only failed tasks.
              - **CreationTime** *(datetime) --* 
                A timestamp indicating when this job was created.
              - **TerminationDate** *(datetime) --* 
                A timestamp indicating when this job terminated. A job's termination date is the date and time when it succeeded, failed, or was canceled.
              - **RoleArn** *(string) --* 
                The Amazon Resource Name (ARN) for the Identity and Access Management (IAM) Role assigned to execute the tasks for this job.
              - **SuspendedDate** *(datetime) --* 
                The timestamp when this job was suspended, if it has been suspended.
              - **SuspendedCause** *(string) --* 
                The reason why the specified job was suspended. A job is only suspended if you create it through the Amazon S3 console. When you create the job, it enters the ``Suspended`` state to await confirmation before running. After you confirm the job, it automatically exits the ``Suspended`` state.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
        :type JobId: string
        :param JobId: **[REQUIRED]**
          The ID for the job whose information you want to retrieve.
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

    def get_public_access_block(self, AccountId: str) -> Dict:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/GetPublicAccessBlock>`_
        
        **Request Syntax**
        ::
          response = client.get_public_access_block(
              AccountId='string'
          )
        
        **Response Syntax**
        ::
            {
                'PublicAccessBlockConfiguration': {
                    'BlockPublicAcls': True|False,
                    'IgnorePublicAcls': True|False,
                    'BlockPublicPolicy': True|False,
                    'RestrictPublicBuckets': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PublicAccessBlockConfiguration** *(dict) --* 
              - **BlockPublicAcls** *(boolean) --* 
              - **IgnorePublicAcls** *(boolean) --* 
              - **BlockPublicPolicy** *(boolean) --* 
              - **RestrictPublicBuckets** *(boolean) --* 
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
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

    def list_jobs(self, AccountId: str, JobStatuses: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Lists current jobs and jobs that have ended within the last 30 days for the AWS account making the request.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/ListJobs>`_
        
        **Request Syntax**
        ::
          response = client.list_jobs(
              AccountId='string',
              JobStatuses=[
                  'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'|'Failed'|'Failing'|'New'|'Paused'|'Pausing'|'Preparing'|'Ready'|'Suspended',
              ],
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'NextToken': 'string',
                'Jobs': [
                    {
                        'JobId': 'string',
                        'Description': 'string',
                        'Operation': 'LambdaInvoke'|'S3PutObjectCopy'|'S3PutObjectAcl'|'S3PutObjectTagging'|'S3InitiateRestoreObject',
                        'Priority': 123,
                        'Status': 'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'|'Failed'|'Failing'|'New'|'Paused'|'Pausing'|'Preparing'|'Ready'|'Suspended',
                        'CreationTime': datetime(2015, 1, 1),
                        'TerminationDate': datetime(2015, 1, 1),
                        'ProgressSummary': {
                            'TotalNumberOfTasks': 123,
                            'NumberOfTasksSucceeded': 123,
                            'NumberOfTasksFailed': 123
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NextToken** *(string) --* 
              If the ``List Jobs`` request produced more than the maximum number of results, you can pass this value into a subsequent ``List Jobs`` request in order to retrieve the next page of results.
            - **Jobs** *(list) --* 
              The list of current jobs and jobs that have ended within the last 30 days.
              - *(dict) --* 
                Contains the configuration and status information for a single job retrieved as part of a job list.
                - **JobId** *(string) --* 
                  The ID for the specified job.
                - **Description** *(string) --* 
                  The user-specified description that was included in the specified job's ``Create Job`` request.
                - **Operation** *(string) --* 
                  The operation that the specified job is configured to run on each object listed in the manifest.
                - **Priority** *(integer) --* 
                  The current priority for the specified job.
                - **Status** *(string) --* 
                  The specified job's current status.
                - **CreationTime** *(datetime) --* 
                  A timestamp indicating when the specified job was created.
                - **TerminationDate** *(datetime) --* 
                  A timestamp indicating when the specified job terminated. A job's termination date is the date and time when it succeeded, failed, or was canceled.
                - **ProgressSummary** *(dict) --* 
                  Describes the total number of tasks that the specified job has executed, the number of tasks that succeeded, and the number of tasks that failed.
                  - **TotalNumberOfTasks** *(integer) --* 
                  - **NumberOfTasksSucceeded** *(integer) --* 
                  - **NumberOfTasksFailed** *(integer) --* 
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
        :type JobStatuses: list
        :param JobStatuses:
          The ``List Jobs`` request returns jobs that match the statuses listed in this element.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          A pagination token to request the next page of results. Use the token that Amazon S3 returned in the ``NextToken`` element of the ``ListJobsResult`` from the previous ``List Jobs`` request.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of jobs that Amazon S3 will include in the ``List Jobs`` response. If there are more jobs than this number, the response will include a pagination token in the ``NextToken`` field to enable you to retrieve the next page of results.
        :rtype: dict
        :returns:
        """
        pass

    def put_public_access_block(self, PublicAccessBlockConfiguration: Dict, AccountId: str):
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/PutPublicAccessBlock>`_
        
        **Request Syntax**
        ::
          response = client.put_public_access_block(
              PublicAccessBlockConfiguration={
                  'BlockPublicAcls': True|False,
                  'IgnorePublicAcls': True|False,
                  'BlockPublicPolicy': True|False,
                  'RestrictPublicBuckets': True|False
              },
              AccountId='string'
          )
        :type PublicAccessBlockConfiguration: dict
        :param PublicAccessBlockConfiguration: **[REQUIRED]**
          - **BlockPublicAcls** *(boolean) --*
          - **IgnorePublicAcls** *(boolean) --*
          - **BlockPublicPolicy** *(boolean) --*
          - **RestrictPublicBuckets** *(boolean) --*
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
        :returns: None
        """
        pass

    def update_job_priority(self, AccountId: str, JobId: str, Priority: int) -> Dict:
        """
        Updates an existing job's priority.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/UpdateJobPriority>`_
        
        **Request Syntax**
        ::
          response = client.update_job_priority(
              AccountId='string',
              JobId='string',
              Priority=123
          )
        
        **Response Syntax**
        ::
            {
                'JobId': 'string',
                'Priority': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **JobId** *(string) --* 
              The ID for the job whose priority Amazon S3 updated.
            - **Priority** *(integer) --* 
              The new priority assigned to the specified job.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
        :type JobId: string
        :param JobId: **[REQUIRED]**
          The ID for the job whose priority you want to update.
        :type Priority: integer
        :param Priority: **[REQUIRED]**
          The priority you want to assign to this job.
        :rtype: dict
        :returns:
        """
        pass

    def update_job_status(self, AccountId: str, JobId: str, RequestedJobStatus: str, StatusUpdateReason: str = None) -> Dict:
        """
        Updates the status for the specified job. Use this operation to confirm that you want to run a job or to cancel an existing job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/UpdateJobStatus>`_
        
        **Request Syntax**
        ::
          response = client.update_job_status(
              AccountId='string',
              JobId='string',
              RequestedJobStatus='Cancelled'|'Ready',
              StatusUpdateReason='string'
          )
        
        **Response Syntax**
        ::
            {
                'JobId': 'string',
                'Status': 'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'|'Failed'|'Failing'|'New'|'Paused'|'Pausing'|'Preparing'|'Ready'|'Suspended',
                'StatusUpdateReason': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **JobId** *(string) --* 
              The ID for the job whose status was updated.
            - **Status** *(string) --* 
              The current status for the specified job.
            - **StatusUpdateReason** *(string) --* 
              The reason that the specified job's status was updated.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
        :type JobId: string
        :param JobId: **[REQUIRED]**
          The ID of the job whose status you want to update.
        :type RequestedJobStatus: string
        :param RequestedJobStatus: **[REQUIRED]**
          The status that you want to move the specified job to.
        :type StatusUpdateReason: string
        :param StatusUpdateReason:
          A description of the reason why you want to change the specified job\'s status. This field can be any string up to the maximum length.
        :rtype: dict
        :returns:
        """
        pass
