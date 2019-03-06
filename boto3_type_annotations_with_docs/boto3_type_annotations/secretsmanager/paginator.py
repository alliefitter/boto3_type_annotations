from typing import Dict
from botocore.paginate import Paginator


class ListSecrets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SecretsManager.Client.list_secrets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/ListSecrets>`_
        
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
                'SecretList': [
                    {
                        'ARN': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'KmsKeyId': 'string',
                        'RotationEnabled': True|False,
                        'RotationLambdaARN': 'string',
                        'RotationRules': {
                            'AutomaticallyAfterDays': 123
                        },
                        'LastRotatedDate': datetime(2015, 1, 1),
                        'LastChangedDate': datetime(2015, 1, 1),
                        'LastAccessedDate': datetime(2015, 1, 1),
                        'DeletedDate': datetime(2015, 1, 1),
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'SecretVersionsToStages': {
                            'string': [
                                'string',
                            ]
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SecretList** *(list) --* 
              A list of the secrets in the account.
              - *(dict) --* 
                A structure that contains the details about a secret. It does not include the encrypted ``SecretString`` and ``SecretBinary`` values. To get those values, use the  GetSecretValue operation.
                - **ARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the secret.
                  For more information about ARNs in Secrets Manager, see `Policy Resources <https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources>`__ in the *AWS Secrets Manager User Guide* .
                - **Name** *(string) --* 
                  The friendly name of the secret. You can use forward slashes in the name to represent a path hierarchy. For example, ``/prod/databases/dbserver1`` could represent the secret for a server named ``dbserver1`` in the folder ``databases`` in the folder ``prod`` . 
                - **Description** *(string) --* 
                  The user-provided description of the secret.
                - **KmsKeyId** *(string) --* 
                  The ARN or alias of the AWS KMS customer master key (CMK) that's used to encrypt the ``SecretString`` and ``SecretBinary`` fields in each version of the secret. If you don't provide a key, then Secrets Manager defaults to encrypting the secret fields with the default KMS CMK (the one named ``awssecretsmanager`` ) for this account.
                - **RotationEnabled** *(boolean) --* 
                  Indicated whether automatic, scheduled rotation is enabled for this secret.
                - **RotationLambdaARN** *(string) --* 
                  The ARN of an AWS Lambda function that's invoked by Secrets Manager to rotate and expire the secret either automatically per the schedule or manually by a call to  RotateSecret .
                - **RotationRules** *(dict) --* 
                  A structure that defines the rotation configuration for the secret.
                  - **AutomaticallyAfterDays** *(integer) --* 
                    Specifies the number of days between automatic scheduled rotations of the secret.
                    Secrets Manager schedules the next rotation when the previous one is complete. Secrets Manager schedules the date by adding the rotation interval (number of days) to the actual date of the last rotation. The service chooses the hour within that 24-hour date window randomly. The minute is also chosen somewhat randomly, but weighted towards the top of the hour and influenced by a variety of factors that help distribute load.
                - **LastRotatedDate** *(datetime) --* 
                  The last date and time that the rotation process for this secret was invoked.
                - **LastChangedDate** *(datetime) --* 
                  The last date and time that this secret was modified in any way.
                - **LastAccessedDate** *(datetime) --* 
                  The last date that this secret was accessed. This value is truncated to midnight of the date and therefore shows only the date, not the time.
                - **DeletedDate** *(datetime) --* 
                  The date and time on which this secret was deleted. Not present on active secrets. The secret can be recovered until the number of days in the recovery window has passed, as specified in the ``RecoveryWindowInDays`` parameter of the  DeleteSecret operation.
                - **Tags** *(list) --* 
                  The list of user-defined tags that are associated with the secret. To add tags to a secret, use  TagResource . To remove tags, use  UntagResource .
                  - *(dict) --* 
                    A structure that contains information about a tag.
                    - **Key** *(string) --* 
                      The key identifier, or name, of the tag.
                    - **Value** *(string) --* 
                      The string value that's associated with the key of the tag.
                - **SecretVersionsToStages** *(dict) --* 
                  A list of all of the currently assigned ``SecretVersionStage`` staging labels and the ``SecretVersionId`` that each is attached to. Staging labels are used to keep track of the different versions during the rotation process.
                  .. note::
                    A version that does not have any ``SecretVersionStage`` is considered deprecated and subject to deletion. Such versions are not included in this list.
                  - *(string) --* 
                    - *(list) --* 
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
