from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
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

    def cancel_rotate_secret(self, SecretId: str) -> Dict:
        """
        
        To re-enable scheduled rotation, call  RotateSecret with ``AutomaticallyRotateAfterDays`` set to a value greater than 0. This will immediately rotate your secret and then enable the automatic schedule.
        
        .. note::
        
          If you cancel a rotation that is in progress, it can leave the ``VersionStage`` labels in an unexpected state. Depending on what step of the rotation was in progress, you might need to remove the staging label ``AWSPENDING`` from the partially created version, specified by the ``VersionId`` response value. You should also evaluate the partially rotated new version to see if it should be deleted, which you can do by removing all staging labels from the new version\'s ``VersionStage`` field.
        
        To successfully start a rotation, the staging label ``AWSPENDING`` must be in one of the following states:
        
        * Not be attached to any version at all 
         
        * Attached to the same version as the staging label ``AWSCURRENT``   
         
        If the staging label ``AWSPENDING`` is attached to a different version than the version with ``AWSCURRENT`` then the attempt to rotate fails.
        
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:CancelRotateSecret 
         
         **Related operations**  
        
        * To configure rotation for a secret or to manually trigger a rotation, use  RotateSecret . 
         
        * To get the rotation configuration details for a secret, use  DescribeSecret . 
         
        * To list all of the currently available secrets, use  ListSecrets . 
         
        * To list all of the versions currently associated with a secret, use  ListSecretVersionIds . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/CancelRotateSecret>`_
        
        **Request Syntax** 
        ::
        
          response = client.cancel_rotate_secret(
              SecretId=\'string\'
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          Specifies the secret for which you want to cancel a rotation request. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ARN\': \'string\',
                \'Name\': \'string\',
                \'VersionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ARN** *(string) --* 
        
              The ARN of the secret for which rotation was canceled.
        
            - **Name** *(string) --* 
        
              The friendly name of the secret for which rotation was canceled.
        
            - **VersionId** *(string) --* 
        
              The unique identifier of the version of the secret that was created during the rotation. This version might not be complete, and should be evaluated for possible deletion. At the very least, you should remove the ``VersionStage`` value ``AWSPENDING`` to enable this version to be deleted. Failing to clean up a cancelled rotation can block you from successfully starting future rotations.
        
        """
        pass

    def create_secret(self, Name: str, ClientRequestToken: str = None, Description: str = None, KmsKeyId: str = None, SecretBinary: bytes = None, SecretString: str = None, Tags: List = None) -> Dict:
        """
        
        Secrets Manager stores the encrypted secret data in one of a collection of \"versions\" associated with the secret. Each version contains a copy of the encrypted secret data. Each version is associated with one or more \"staging labels\" that identify where the version is in the rotation cycle. The ``SecretVersionsToStages`` field of the secret contains the mapping of staging labels to the active versions of the secret. Versions without a staging label are considered deprecated and are not included in the list.
        
        You provide the secret data to be encrypted by putting text in either the ``SecretString`` parameter or binary data in the ``SecretBinary`` parameter, but not both. If you include ``SecretString`` or ``SecretBinary`` then Secrets Manager also creates an initial secret version and automatically attaches the staging label ``AWSCURRENT`` to the new version.
        
        .. note::
        
          * If you call an operation that needs to encrypt or decrypt the ``SecretString`` or ``SecretBinary`` for a secret in the same account as the calling user and that secret doesn\'t specify a AWS KMS encryption key, Secrets Manager uses the account\'s default AWS managed customer master key (CMK) with the alias ``aws/secretsmanager`` . If this key doesn\'t already exist in your account then Secrets Manager creates it for you automatically. All users and roles in the same AWS account automatically have access to use the default CMK. Note that if an Secrets Manager API call results in AWS having to create the account\'s AWS-managed CMK, it can result in a one-time significant delay in returning the result. 
           
          * If the secret is in a different AWS account from the credentials calling an API that requires encryption or decryption of the secret value then you must create and use a custom AWS KMS CMK because you can\'t access the default CMK for the account using credentials from a different AWS account. Store the ARN of the CMK in the secret when you create the secret or when you update it by including it in the ``KMSKeyId`` . If you call an API that must encrypt or decrypt ``SecretString`` or ``SecretBinary`` using credentials from a different account then the AWS KMS key policy must grant cross-account access to that other account\'s user or role for both the kms:GenerateDataKey and kms:Decrypt operations. 
           
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:CreateSecret 
         
        * kms:GenerateDataKey - needed only if you use a customer-managed AWS KMS key to encrypt the secret. You do not need this permission to use the account\'s default AWS managed CMK for Secrets Manager. 
         
        * kms:Decrypt - needed only if you use a customer-managed AWS KMS key to encrypt the secret. You do not need this permission to use the account\'s default AWS managed CMK for Secrets Manager. 
         
        * secretsmanager:TagResource - needed only if you include the ``Tags`` parameter.  
         
         **Related operations**  
        
        * To delete a secret, use  DeleteSecret . 
         
        * To modify an existing secret, use  UpdateSecret . 
         
        * To create a new version of a secret, use  PutSecretValue . 
         
        * To retrieve the encrypted secure string and secure binary values, use  GetSecretValue . 
         
        * To retrieve all other details for a secret, use  DescribeSecret . This does not include the encrypted secure string and secure binary values. 
         
        * To retrieve the list of secret versions associated with the current secret, use  DescribeSecret and examine the ``SecretVersionsToStages`` response value. 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/CreateSecret>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_secret(
              Name=\'string\',
              ClientRequestToken=\'string\',
              Description=\'string\',
              KmsKeyId=\'string\',
              SecretBinary=b\'bytes\',
              SecretString=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          Specifies the friendly name of the new secret.
        
          The secret name must be ASCII letters, digits, or the following characters : /_+=.@-
        
          .. note::
        
            Don\'t end your secret name with a hyphen followed by six characters. If you do so, you risk confusion and unexpected results when searching for a secret by partial ARN. This is because Secrets Manager automatically adds a hyphen and six random characters at the end of the ARN.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          (Optional) If you include ``SecretString`` or ``SecretBinary`` , then an initial version is created as part of the secret, and this parameter specifies a unique identifier for the new version. 
        
          .. note::
        
            If you use the AWS CLI or one of the AWS SDK to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request. If you don\'t use the SDK and instead generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a ``ClientRequestToken`` yourself for the new version and include that value in the request.
        
          This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a `UUID-type <https://wikipedia.org/wiki/Universally_unique_identifier>`__ value to ensure uniqueness of your versions within the specified secret. 
        
          * If the ``ClientRequestToken`` value isn\'t already associated with a version of the secret then a new version of the secret is created.  
           
          * If a version with this value already exists and that version\'s ``SecretString`` and ``SecretBinary`` values are the same as those in the request, then the request is ignored (the operation is idempotent). 
           
          * If a version with this value already exists and that version\'s ``SecretString`` and ``SecretBinary`` values are different from those in the request then the request fails because you cannot modify an existing version. Instead, use  PutSecretValue to create a new version. 
           
          This value becomes the ``VersionId`` of the new version.
        
          This field is autopopulated if not provided.
        
        :type Description: string
        :param Description: 
        
          (Optional) Specifies a user-provided description of the secret.
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          (Optional) Specifies the ARN, Key ID, or alias of the AWS KMS customer master key (CMK) to be used to encrypt the ``SecretString`` or ``SecretBinary`` values in the versions stored in this secret.
        
          You can specify any of the supported ways to identify a AWS KMS key ID. If you need to reference a CMK in a different account, you can use only the key ARN or the alias ARN.
        
          If you don\'t specify this value, then Secrets Manager defaults to using the AWS account\'s default CMK (the one named ``aws/secretsmanager`` ). If a AWS KMS CMK with that name doesn\'t yet exist, then Secrets Manager creates it for you automatically the first time it needs to encrypt a version\'s ``SecretString`` or ``SecretBinary`` fields.
        
          .. warning::
        
            You can use the account\'s default CMK to encrypt and decrypt only if you call this operation using credentials from the same account that owns the secret. If the secret is in a different account, then you must create a custom CMK and specify the ARN in this field. 
        
        :type SecretBinary: bytes
        :param SecretBinary: 
        
          (Optional) Specifies binary data that you want to encrypt and store in the new version of the secret. To use this parameter in the command-line tools, we recommend that you store your binary data in a file and then use the appropriate technique for your tool to pass the contents of the file as a parameter.
        
          Either ``SecretString`` or ``SecretBinary`` must have a value, but not both. They cannot both be empty.
        
          This parameter is not available using the Secrets Manager console. It can be accessed only by using the AWS CLI or one of the AWS SDKs.
        
        :type SecretString: string
        :param SecretString: 
        
          (Optional) Specifies text data that you want to encrypt and store in this new version of the secret.
        
          Either ``SecretString`` or ``SecretBinary`` must have a value, but not both. They cannot both be empty.
        
          If you create a secret by using the Secrets Manager console then Secrets Manager puts the protected secret text in only the ``SecretString`` parameter. The Secrets Manager console stores the information as a JSON structure of key/value pairs that the Lambda rotation function knows how to parse.
        
          For storing multiple values, we recommend that you use a JSON text string argument and specify key/value pairs. For information on how to format a JSON parameter for the various command line tool environments, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ in the *AWS CLI User Guide* . For example:
        
           ``[{\"username\":\"bob\"},{\"password\":\"abc123xyz456\"}]``  
        
          If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text. 
        
        :type Tags: list
        :param Tags: 
        
          (Optional) Specifies a list of user-defined tags that are attached to the secret. Each tag is a \"Key\" and \"Value\" pair of strings. This operation only appends tags to the existing list of tags. To remove tags, you must use  UntagResource .
        
          .. warning::
        
            * Secrets Manager tag key names are case sensitive. A tag with the key \"ABC\" is a different tag from one with key \"abc\". 
             
            * If you check tags in IAM policy ``Condition`` elements as part of your security strategy, then adding or removing a tag can change permissions. If the successful completion of this operation would result in you losing your permissions for this secret, then this operation is blocked and returns an ``Access Denied`` error. 
             
          This parameter requires a JSON text string argument. For information on how to format a JSON parameter for the various command line tool environments, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ in the *AWS CLI User Guide* . For example:
        
           ``[{\"Key\":\"CostCenter\",\"Value\":\"12345\"},{\"Key\":\"environment\",\"Value\":\"production\"}]``  
        
          If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text. 
        
          The following basic restrictions apply to tags:
        
          * Maximum number of tags per secret—50 
           
          * Maximum key length—127 Unicode characters in UTF-8 
           
          * Maximum value length—255 Unicode characters in UTF-8 
           
          * Tag keys and values are case sensitive. 
           
          * Do not use the ``aws:`` prefix in your tag names or values because it is reserved for AWS use. You can\'t edit or delete tag names or values with this prefix. Tags with this prefix do not count against your tags per secret limit. 
           
          * If your tagging schema will be used across multiple services and resources, remember that other services might have restrictions on allowed characters. Generally allowed characters are: letters, spaces, and numbers representable in UTF-8, plus the following special characters: + - = . _ : / @. 
           
          - *(dict) --* 
        
            A structure that contains information about a tag.
        
            - **Key** *(string) --* 
        
              The key identifier, or name, of the tag.
        
            - **Value** *(string) --* 
        
              The string value that\'s associated with the key of the tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ARN\': \'string\',
                \'Name\': \'string\',
                \'VersionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ARN** *(string) --* 
        
              The Amazon Resource Name (ARN) of the secret that you just created.
        
              .. note::
        
                Secrets Manager automatically adds several random characters to the name at the end of the ARN when you initially create a secret. This affects only the ARN and not the actual friendly name. This ensures that if you create a new secret with the same name as an old secret that you previously deleted, then users with access to the old secret *don\'t* automatically get access to the new secret because the ARNs are different.
        
            - **Name** *(string) --* 
        
              The friendly name of the secret that you just created.
        
            - **VersionId** *(string) --* 
        
              The unique identifier that\'s associated with the version of the secret you just created.
        
        """
        pass

    def delete_resource_policy(self, SecretId: str) -> Dict:
        """
        
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:DeleteResourcePolicy 
         
         **Related operations**  
        
        * To attach a resource policy to a secret, use  PutResourcePolicy . 
         
        * To retrieve the current resource-based policy that\'s attached to a secret, use  GetResourcePolicy . 
         
        * To list all of the currently available secrets, use  ListSecrets . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/DeleteResourcePolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_resource_policy(
              SecretId=\'string\'
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          Specifies the secret that you want to delete the attached resource-based policy for. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ARN\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ARN** *(string) --* 
        
              The ARN of the secret that the resource-based policy was deleted for.
        
            - **Name** *(string) --* 
        
              The friendly name of the secret that the resource-based policy was deleted for.
        
        """
        pass

    def delete_secret(self, SecretId: str, RecoveryWindowInDays: int = None, ForceDeleteWithoutRecovery: bool = None) -> Dict:
        """
        
        At any time before recovery window ends, you can use  RestoreSecret to remove the ``DeletionDate`` and cancel the deletion of the secret.
        
        You cannot access the encrypted secret information in any secret that is scheduled for deletion. If you need to access that information, you must cancel the deletion with  RestoreSecret and then retrieve the information.
        
        .. note::
        
          * There is no explicit operation to delete a version of a secret. Instead, remove all staging labels from the ``VersionStage`` field of a version. That marks the version as deprecated and allows Secrets Manager to delete it as needed. Versions that do not have any staging labels do not show up in  ListSecretVersionIds unless you specify ``IncludeDeprecated`` . 
           
          * The permanent secret deletion at the end of the waiting period is performed as a background task with low priority. There is no guarantee of a specific time after the recovery window for the actual delete operation to occur. 
           
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:DeleteSecret 
         
         **Related operations**  
        
        * To create a secret, use  CreateSecret . 
         
        * To cancel deletion of a version of a secret before the recovery window has expired, use  RestoreSecret . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/DeleteSecret>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_secret(
              SecretId=\'string\',
              RecoveryWindowInDays=123,
              ForceDeleteWithoutRecovery=True|False
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          Specifies the secret that you want to delete. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :type RecoveryWindowInDays: integer
        :param RecoveryWindowInDays: 
        
          (Optional) Specifies the number of days that Secrets Manager waits before it can delete the secret. You can\'t use both this parameter and the ``ForceDeleteWithoutRecovery`` parameter in the same API call.
        
          This value can range from 7 to 30 days. The default value is 30.
        
        :type ForceDeleteWithoutRecovery: boolean
        :param ForceDeleteWithoutRecovery: 
        
          (Optional) Specifies that the secret is to be deleted without any recovery window. You can\'t use both this parameter and the ``RecoveryWindowInDays`` parameter in the same API call.
        
          An asynchronous background process performs the actual deletion, so there can be a short delay before the operation completes. If you write code to delete and then immediately recreate a secret with the same name, ensure that your code includes appropriate back off and retry logic.
        
          .. warning::
        
            Use this parameter with caution. This parameter causes the operation to skip the normal waiting period before the permanent deletion that AWS would normally impose with the ``RecoveryWindowInDays`` parameter. If you delete a secret with the ``ForceDeleteWithouRecovery`` parameter, then you have no opportunity to recover the secret. It is permanently lost.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ARN\': \'string\',
                \'Name\': \'string\',
                \'DeletionDate\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ARN** *(string) --* 
        
              The ARN of the secret that is now scheduled for deletion.
        
            - **Name** *(string) --* 
        
              The friendly name of the secret that is now scheduled for deletion.
        
            - **DeletionDate** *(datetime) --* 
        
              The date and time after which this secret can be deleted by Secrets Manager and can no longer be restored. This value is the date and time of the delete request plus the number of days specified in ``RecoveryWindowInDays`` .
        
        """
        pass

    def describe_secret(self, SecretId: str) -> Dict:
        """
        
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:DescribeSecret 
         
         **Related operations**  
        
        * To create a secret, use  CreateSecret . 
         
        * To modify a secret, use  UpdateSecret . 
         
        * To retrieve the encrypted secret information in a version of the secret, use  GetSecretValue . 
         
        * To list all of the secrets in the AWS account, use  ListSecrets . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/DescribeSecret>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_secret(
              SecretId=\'string\'
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          The identifier of the secret whose details you want to retrieve. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ARN\': \'string\',
                \'Name\': \'string\',
                \'Description\': \'string\',
                \'KmsKeyId\': \'string\',
                \'RotationEnabled\': True|False,
                \'RotationLambdaARN\': \'string\',
                \'RotationRules\': {
                    \'AutomaticallyAfterDays\': 123
                },
                \'LastRotatedDate\': datetime(2015, 1, 1),
                \'LastChangedDate\': datetime(2015, 1, 1),
                \'LastAccessedDate\': datetime(2015, 1, 1),
                \'DeletedDate\': datetime(2015, 1, 1),
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ],
                \'VersionIdsToStages\': {
                    \'string\': [
                        \'string\',
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ARN** *(string) --* 
        
              The ARN of the secret.
        
            - **Name** *(string) --* 
        
              The user-provided friendly name of the secret.
        
            - **Description** *(string) --* 
        
              The user-provided description of the secret.
        
            - **KmsKeyId** *(string) --* 
        
              The ARN or alias of the AWS KMS customer master key (CMK) that\'s used to encrypt the ``SecretString`` or ``SecretBinary`` fields in each version of the secret. If you don\'t provide a key, then Secrets Manager defaults to encrypting the secret fields with the default AWS KMS CMK (the one named ``awssecretsmanager`` ) for this account.
        
            - **RotationEnabled** *(boolean) --* 
        
              Specifies whether automatic rotation is enabled for this secret.
        
              To enable rotation, use  RotateSecret with ``AutomaticallyRotateAfterDays`` set to a value greater than 0. To disable rotation, use  CancelRotateSecret .
        
            - **RotationLambdaARN** *(string) --* 
        
              The ARN of a Lambda function that\'s invoked by Secrets Manager to rotate the secret either automatically per the schedule or manually by a call to ``RotateSecret`` .
        
            - **RotationRules** *(dict) --* 
        
              A structure that contains the rotation configuration for this secret.
        
              - **AutomaticallyAfterDays** *(integer) --* 
        
                Specifies the number of days between automatic scheduled rotations of the secret.
        
                Secrets Manager schedules the next rotation when the previous one is complete. Secrets Manager schedules the date by adding the rotation interval (number of days) to the actual date of the last rotation. The service chooses the hour within that 24-hour date window randomly. The minute is also chosen somewhat randomly, but weighted towards the top of the hour and influenced by a variety of factors that help distribute load.
        
            - **LastRotatedDate** *(datetime) --* 
        
              The most recent date and time that the Secrets Manager rotation process was successfully completed. This value is null if the secret has never rotated.
        
            - **LastChangedDate** *(datetime) --* 
        
              The last date and time that this secret was modified in any way.
        
            - **LastAccessedDate** *(datetime) --* 
        
              The last date that this secret was accessed. This value is truncated to midnight of the date and therefore shows only the date, not the time.
        
            - **DeletedDate** *(datetime) --* 
        
              This value exists if the secret is scheduled for deletion. Some time after the specified date and time, Secrets Manager deletes the secret and all of its versions.
        
              If a secret is scheduled for deletion, then its details, including the encrypted secret information, is not accessible. To cancel a scheduled deletion and restore access, use  RestoreSecret .
        
            - **Tags** *(list) --* 
        
              The list of user-defined tags that are associated with the secret. To add tags to a secret, use  TagResource . To remove tags, use  UntagResource .
        
              - *(dict) --* 
        
                A structure that contains information about a tag.
        
                - **Key** *(string) --* 
        
                  The key identifier, or name, of the tag.
        
                - **Value** *(string) --* 
        
                  The string value that\'s associated with the key of the tag.
        
            - **VersionIdsToStages** *(dict) --* 
        
              A list of all of the currently assigned ``VersionStage`` staging labels and the ``VersionId`` that each is attached to. Staging labels are used to keep track of the different versions during the rotation process.
        
              .. note::
        
                A version that does not have any staging labels attached is considered deprecated and subject to deletion. Such versions are not included in this list.
        
              - *(string) --* 
                
                - *(list) --* 
                  
                  - *(string) --* 
              
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
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

    def get_random_password(self, PasswordLength: int = None, ExcludeCharacters: str = None, ExcludeNumbers: bool = None, ExcludePunctuation: bool = None, ExcludeUppercase: bool = None, ExcludeLowercase: bool = None, IncludeSpace: bool = None, RequireEachIncludedType: bool = None) -> Dict:
        """
        
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:GetRandomPassword 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/GetRandomPassword>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_random_password(
              PasswordLength=123,
              ExcludeCharacters=\'string\',
              ExcludeNumbers=True|False,
              ExcludePunctuation=True|False,
              ExcludeUppercase=True|False,
              ExcludeLowercase=True|False,
              IncludeSpace=True|False,
              RequireEachIncludedType=True|False
          )
        :type PasswordLength: integer
        :param PasswordLength: 
        
          The desired length of the generated password. The default value if you do not include this parameter is 32 characters.
        
        :type ExcludeCharacters: string
        :param ExcludeCharacters: 
        
          A string that includes characters that should not be included in the generated password. The default is that all characters from the included sets can be used.
        
        :type ExcludeNumbers: boolean
        :param ExcludeNumbers: 
        
          Specifies that the generated password should not include digits. The default if you do not include this switch parameter is that digits can be included.
        
        :type ExcludePunctuation: boolean
        :param ExcludePunctuation: 
        
          Specifies that the generated password should not include punctuation characters. The default if you do not include this switch parameter is that punctuation characters can be included.
        
          The following are the punctuation characters that *can* be included in the generated password if you don\'t explicitly exclude them with ``ExcludeCharacters`` or ``ExcludePunctuation`` :
        
           ``! \" # $ % & \' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~``  
        
        :type ExcludeUppercase: boolean
        :param ExcludeUppercase: 
        
          Specifies that the generated password should not include uppercase letters. The default if you do not include this switch parameter is that uppercase letters can be included.
        
        :type ExcludeLowercase: boolean
        :param ExcludeLowercase: 
        
          Specifies that the generated password should not include lowercase letters. The default if you do not include this switch parameter is that lowercase letters can be included.
        
        :type IncludeSpace: boolean
        :param IncludeSpace: 
        
          Specifies that the generated password can include the space character. The default if you do not include this switch parameter is that the space character is not included.
        
        :type RequireEachIncludedType: boolean
        :param RequireEachIncludedType: 
        
          A boolean value that specifies whether the generated password must include at least one of every allowed character type. The default value is ``True`` and the operation requires at least one of every character type.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RandomPassword\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **RandomPassword** *(string) --* 
        
              A string with the generated password.
        
        """
        pass

    def get_resource_policy(self, SecretId: str) -> Dict:
        """
        
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:GetResourcePolicy 
         
         **Related operations**  
        
        * To attach a resource policy to a secret, use  PutResourcePolicy . 
         
        * To delete the resource-based policy that\'s attached to a secret, use  DeleteResourcePolicy . 
         
        * To list all of the currently available secrets, use  ListSecrets . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/GetResourcePolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_resource_policy(
              SecretId=\'string\'
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          Specifies the secret that you want to retrieve the attached resource-based policy for. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ARN\': \'string\',
                \'Name\': \'string\',
                \'ResourcePolicy\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ARN** *(string) --* 
        
              The ARN of the secret that the resource-based policy was retrieved for.
        
            - **Name** *(string) --* 
        
              The friendly name of the secret that the resource-based policy was retrieved for.
        
            - **ResourcePolicy** *(string) --* 
        
              A JSON-formatted string that describes the permissions that are associated with the attached secret. These permissions are combined with any permissions that are associated with the user or role that attempts to access this secret. The combined permissions specify who can access the secret and what actions they can perform. For more information, see `Authentication and Access Control for AWS Secrets Manager <http://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html>`__ in the *AWS Secrets Manager User Guide* .
        
        """
        pass

    def get_secret_value(self, SecretId: str, VersionId: str = None, VersionStage: str = None) -> Dict:
        """
        
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:GetSecretValue 
         
        * kms:Decrypt - required only if you use a customer-managed AWS KMS key to encrypt the secret. You do not need this permission to use the account\'s default AWS managed CMK for Secrets Manager. 
         
         **Related operations**  
        
        * To create a new version of the secret with different encrypted information, use  PutSecretValue . 
         
        * To retrieve the non-encrypted details for the secret, use  DescribeSecret . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/GetSecretValue>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_secret_value(
              SecretId=\'string\',
              VersionId=\'string\',
              VersionStage=\'string\'
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          Specifies the secret containing the version that you want to retrieve. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :type VersionId: string
        :param VersionId: 
        
          Specifies the unique identifier of the version of the secret that you want to retrieve. If you specify this parameter then don\'t specify ``VersionStage`` . If you don\'t specify either a ``VersionStage`` or ``VersionId`` then the default is to perform the operation on the version with the ``VersionStage`` value of ``AWSCURRENT`` .
        
          This value is typically a `UUID-type <https://wikipedia.org/wiki/Universally_unique_identifier>`__ value with 32 hexadecimal digits.
        
        :type VersionStage: string
        :param VersionStage: 
        
          Specifies the secret version that you want to retrieve by the staging label attached to the version.
        
          Staging labels are used to keep track of different versions during the rotation process. If you use this parameter then don\'t specify ``VersionId`` . If you don\'t specify either a ``VersionStage`` or ``VersionId`` , then the default is to perform the operation on the version with the ``VersionStage`` value of ``AWSCURRENT`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ARN\': \'string\',
                \'Name\': \'string\',
                \'VersionId\': \'string\',
                \'SecretBinary\': b\'bytes\',
                \'SecretString\': \'string\',
                \'VersionStages\': [
                    \'string\',
                ],
                \'CreatedDate\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ARN** *(string) --* 
        
              The ARN of the secret.
        
            - **Name** *(string) --* 
        
              The friendly name of the secret.
        
            - **VersionId** *(string) --* 
        
              The unique identifier of this version of the secret.
        
            - **SecretBinary** *(bytes) --* 
        
              The decrypted part of the protected secret information that was originally provided as binary data in the form of a byte array. The response parameter represents the binary data as a `base64-encoded <https://tools.ietf.org/html/rfc4648#section-4>`__ string.
        
              This parameter is not used if the secret is created by the Secrets Manager console.
        
              If you store custom information in this field of the secret, then you must code your Lambda rotation function to parse and interpret whatever you store in the ``SecretString`` or ``SecretBinary`` fields.
        
            - **SecretString** *(string) --* 
        
              The decrypted part of the protected secret information that was originally provided as a string.
        
              If you create this secret by using the Secrets Manager console then only the ``SecretString`` parameter contains data. Secrets Manager stores the information as a JSON structure of key/value pairs that the Lambda rotation function knows how to parse.
        
              If you store custom information in the secret by using the  CreateSecret ,  UpdateSecret , or  PutSecretValue API operations instead of the Secrets Manager console, or by using the **Other secret type** in the console, then you must code your Lambda rotation function to parse and interpret those values.
        
            - **VersionStages** *(list) --* 
        
              A list of all of the staging labels currently attached to this version of the secret.
        
              - *(string) --* 
          
            - **CreatedDate** *(datetime) --* 
        
              The date and time that this version of the secret was created.
        
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

    def list_secret_version_ids(self, SecretId: str, MaxResults: int = None, NextToken: str = None, IncludeDeprecated: bool = None) -> Dict:
        """
        
        .. note::
        
          Always check the ``NextToken`` response parameter when calling any of the ``List*`` operations. These operations can occasionally return an empty or shorter than expected list of results even when there are more results available. When this happens, the ``NextToken`` response parameter contains a value to pass to the next call to the same API to request the next part of the list.
        
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:ListSecretVersionIds 
         
         **Related operations**  
        
        * To list the secrets in an account, use  ListSecrets . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/ListSecretVersionIds>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_secret_version_ids(
              SecretId=\'string\',
              MaxResults=123,
              NextToken=\'string\',
              IncludeDeprecated=True|False
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          The identifier for the secret containing the versions you want to list. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          (Optional) Limits the number of results that you want to include in the response. If you don\'t include this parameter, it defaults to a value that\'s specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (isn\'t null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Secrets Manager might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.
        
        :type NextToken: string
        :param NextToken: 
        
          (Optional) Use this parameter in a request if you receive a ``NextToken`` response in a previous request that indicates that there\'s more output available. In a subsequent call, set it to the value of the previous call\'s ``NextToken`` response to indicate where the output should continue from.
        
        :type IncludeDeprecated: boolean
        :param IncludeDeprecated: 
        
          (Optional) Specifies that you want the results to include versions that do not have any staging labels attached to them. Such versions are considered deprecated and are subject to deletion by Secrets Manager as needed.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Versions\': [
                    {
                        \'VersionId\': \'string\',
                        \'VersionStages\': [
                            \'string\',
                        ],
                        \'LastAccessedDate\': datetime(2015, 1, 1),
                        \'CreatedDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\',
                \'ARN\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Versions** *(list) --* 
        
              The list of the currently available versions of the specified secret.
        
              - *(dict) --* 
        
                A structure that contains information about one version of a secret.
        
                - **VersionId** *(string) --* 
        
                  The unique version identifier of this version of the secret.
        
                - **VersionStages** *(list) --* 
        
                  An array of staging labels that are currently associated with this version of the secret.
        
                  - *(string) --* 
              
                - **LastAccessedDate** *(datetime) --* 
        
                  The date that this version of the secret was last accessed. Note that the resolution of this field is at the date level and does not include the time.
        
                - **CreatedDate** *(datetime) --* 
        
                  The date and time this version of the secret was created.
        
            - **NextToken** *(string) --* 
        
              If present in the response, this value indicates that there\'s more output available than what\'s included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a very long list. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to continue processing and get the next part of the output. You should repeat this until the ``NextToken`` response element comes back empty (as ``null`` ).
        
            - **ARN** *(string) --* 
        
              The Amazon Resource Name (ARN) for the secret.
        
              .. note::
        
                Secrets Manager automatically adds several random characters to the name at the end of the ARN when you initially create a secret. This affects only the ARN and not the actual friendly name. This ensures that if you create a new secret with the same name as an old secret that you previously deleted, then users with access to the old secret *don\'t* automatically get access to the new secret because the ARNs are different.
        
            - **Name** *(string) --* 
        
              The friendly name of the secret.
        
        """
        pass

    def list_secrets(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        .. note::
        
          Always check the ``NextToken`` response parameter when calling any of the ``List*`` operations. These operations can occasionally return an empty or shorter than expected list of results even when there are more results available. When this happens, the ``NextToken`` response parameter contains a value to pass to the next call to the same API to request the next part of the list.
        
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:ListSecrets 
         
         **Related operations**  
        
        * To list the versions attached to a secret, use  ListSecretVersionIds . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/ListSecrets>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_secrets(
              MaxResults=123,
              NextToken=\'string\'
          )
        :type MaxResults: integer
        :param MaxResults: 
        
          (Optional) Limits the number of results that you want to include in the response. If you don\'t include this parameter, it defaults to a value that\'s specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (isn\'t null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Secrets Manager might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.
        
        :type NextToken: string
        :param NextToken: 
        
          (Optional) Use this parameter in a request if you receive a ``NextToken`` response in a previous request that indicates that there\'s more output available. In a subsequent call, set it to the value of the previous call\'s ``NextToken`` response to indicate where the output should continue from.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SecretList\': [
                    {
                        \'ARN\': \'string\',
                        \'Name\': \'string\',
                        \'Description\': \'string\',
                        \'KmsKeyId\': \'string\',
                        \'RotationEnabled\': True|False,
                        \'RotationLambdaARN\': \'string\',
                        \'RotationRules\': {
                            \'AutomaticallyAfterDays\': 123
                        },
                        \'LastRotatedDate\': datetime(2015, 1, 1),
                        \'LastChangedDate\': datetime(2015, 1, 1),
                        \'LastAccessedDate\': datetime(2015, 1, 1),
                        \'DeletedDate\': datetime(2015, 1, 1),
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ],
                        \'SecretVersionsToStages\': {
                            \'string\': [
                                \'string\',
                            ]
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SecretList** *(list) --* 
        
              A list of the secrets in the account.
        
              - *(dict) --* 
        
                A structure that contains the details about a secret. It does not include the encrypted ``SecretString`` and ``SecretBinary`` values. To get those values, use the  GetSecretValue operation.
        
                - **ARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the secret.
        
                  For more information about ARNs in Secrets Manager, see `Policy Resources <http://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources>`__ in the *AWS Secrets Manager User Guide* .
        
                - **Name** *(string) --* 
        
                  The friendly name of the secret. You can use forward slashes in the name to represent a path hierarchy. For example, ``/prod/databases/dbserver1`` could represent the secret for a server named ``dbserver1`` in the folder ``databases`` in the folder ``prod`` . 
        
                - **Description** *(string) --* 
        
                  The user-provided description of the secret.
        
                - **KmsKeyId** *(string) --* 
        
                  The ARN or alias of the AWS KMS customer master key (CMK) that\'s used to encrypt the ``SecretString`` and ``SecretBinary`` fields in each version of the secret. If you don\'t provide a key, then Secrets Manager defaults to encrypting the secret fields with the default KMS CMK (the one named ``awssecretsmanager`` ) for this account.
        
                - **RotationEnabled** *(boolean) --* 
        
                  Indicated whether automatic, scheduled rotation is enabled for this secret.
        
                - **RotationLambdaARN** *(string) --* 
        
                  The ARN of an AWS Lambda function that\'s invoked by Secrets Manager to rotate and expire the secret either automatically per the schedule or manually by a call to  RotateSecret .
        
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
        
                      The string value that\'s associated with the key of the tag.
        
                - **SecretVersionsToStages** *(dict) --* 
        
                  A list of all of the currently assigned ``SecretVersionStage`` staging labels and the ``SecretVersionId`` that each is attached to. Staging labels are used to keep track of the different versions during the rotation process.
        
                  .. note::
        
                    A version that does not have any ``SecretVersionStage`` is considered deprecated and subject to deletion. Such versions are not included in this list.
        
                  - *(string) --* 
                    
                    - *(list) --* 
                      
                      - *(string) --* 
                  
            - **NextToken** *(string) --* 
        
              If present in the response, this value indicates that there\'s more output available than what\'s included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a very long list. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to continue processing and get the next part of the output. You should repeat this until the ``NextToken`` response element comes back empty (as ``null`` ).
        
        """
        pass

    def put_resource_policy(self, SecretId: str, ResourcePolicy: str) -> Dict:
        """
        
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:PutResourcePolicy 
         
         **Related operations**  
        
        * To retrieve the resource policy that\'s attached to a secret, use  GetResourcePolicy . 
         
        * To delete the resource-based policy that\'s attached to a secret, use  DeleteResourcePolicy . 
         
        * To list all of the currently available secrets, use  ListSecrets . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/PutResourcePolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_resource_policy(
              SecretId=\'string\',
              ResourcePolicy=\'string\'
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          Specifies the secret that you want to attach the resource-based policy to. You can specify either the ARN or the friendly name of the secret.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :type ResourcePolicy: string
        :param ResourcePolicy: **[REQUIRED]** 
        
          A JSON-formatted string that\'s constructed according to the grammar and syntax for an AWS resource-based policy. The policy in the string identifies who can access or manage this secret and its versions. For information on how to format a JSON parameter for the various command line tool environments, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ in the *AWS CLI User Guide* .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ARN\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ARN** *(string) --* 
        
              The ARN of the secret that the resource-based policy was retrieved for.
        
            - **Name** *(string) --* 
        
              The friendly name of the secret that the resource-based policy was retrieved for.
        
        """
        pass

    def put_secret_value(self, SecretId: str, ClientRequestToken: str = None, SecretBinary: bytes = None, SecretString: str = None, VersionStages: List = None) -> Dict:
        """
        
        .. note::
        
          The Secrets Manager console uses only the ``SecretString`` field. To add binary data to a secret with the ``SecretBinary`` field you must use the AWS CLI or one of the AWS SDKs.
        
        * If this operation creates the first version for the secret then Secrets Manager automatically attaches the staging label ``AWSCURRENT`` to the new version. 
         
        * If another version of this secret already exists, then this operation does not automatically move any staging labels other than those that you explicitly specify in the ``VersionStages`` parameter. 
         
        * If this operation moves the staging label ``AWSCURRENT`` from another version to this version (because you included it in the ``StagingLabels`` parameter) then Secrets Manager also automatically moves the staging label ``AWSPREVIOUS`` to the version that ``AWSCURRENT`` was removed from. 
         
        * This operation is idempotent. If a version with a ``VersionId`` with the same value as the ``ClientRequestToken`` parameter already exists and you specify the same secret data, the operation succeeds but does nothing. However, if the secret data is different, then the operation fails because you cannot modify an existing version; you can only create new ones. 
         
        .. note::
        
          * If you call an operation that needs to encrypt or decrypt the ``SecretString`` or ``SecretBinary`` for a secret in the same account as the calling user and that secret doesn\'t specify a AWS KMS encryption key, Secrets Manager uses the account\'s default AWS managed customer master key (CMK) with the alias ``aws/secretsmanager`` . If this key doesn\'t already exist in your account then Secrets Manager creates it for you automatically. All users and roles in the same AWS account automatically have access to use the default CMK. Note that if an Secrets Manager API call results in AWS having to create the account\'s AWS-managed CMK, it can result in a one-time significant delay in returning the result. 
           
          * If the secret is in a different AWS account from the credentials calling an API that requires encryption or decryption of the secret value then you must create and use a custom AWS KMS CMK because you can\'t access the default CMK for the account using credentials from a different AWS account. Store the ARN of the CMK in the secret when you create the secret or when you update it by including it in the ``KMSKeyId`` . If you call an API that must encrypt or decrypt ``SecretString`` or ``SecretBinary`` using credentials from a different account then the AWS KMS key policy must grant cross-account access to that other account\'s user or role for both the kms:GenerateDataKey and kms:Decrypt operations. 
           
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:PutSecretValue 
         
        * kms:GenerateDataKey - needed only if you use a customer-managed AWS KMS key to encrypt the secret. You do not need this permission to use the account\'s default AWS managed CMK for Secrets Manager. 
         
         **Related operations**  
        
        * To retrieve the encrypted value you store in the version of a secret, use  GetSecretValue . 
         
        * To create a secret, use  CreateSecret . 
         
        * To get the details for a secret, use  DescribeSecret . 
         
        * To list the versions attached to a secret, use  ListSecretVersionIds . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/PutSecretValue>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_secret_value(
              SecretId=\'string\',
              ClientRequestToken=\'string\',
              SecretBinary=b\'bytes\',
              SecretString=\'string\',
              VersionStages=[
                  \'string\',
              ]
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          (Optional) Specifies a unique identifier for the new version of the secret. 
        
          .. note::
        
            If you use the AWS CLI or one of the AWS SDK to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes that in the request. If you don\'t use the SDK and instead generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a ``ClientRequestToken`` yourself for new versions and include that value in the request. 
        
          This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during the Lambda rotation function\'s processing. We recommend that you generate a `UUID-type <https://wikipedia.org/wiki/Universally_unique_identifier>`__ value to ensure uniqueness within the specified secret. 
        
          * If the ``ClientRequestToken`` value isn\'t already associated with a version of the secret then a new version of the secret is created.  
           
          * If a version with this value already exists and that version\'s ``SecretString`` or ``SecretBinary`` values are the same as those in the request then the request is ignored (the operation is idempotent).  
           
          * If a version with this value already exists and that version\'s ``SecretString`` and ``SecretBinary`` values are different from those in the request then the request fails because you cannot modify an existing secret version. You can only create new versions to store new secret values. 
           
          This value becomes the ``VersionId`` of the new version.
        
          This field is autopopulated if not provided.
        
        :type SecretBinary: bytes
        :param SecretBinary: 
        
          (Optional) Specifies binary data that you want to encrypt and store in the new version of the secret. To use this parameter in the command-line tools, we recommend that you store your binary data in a file and then use the appropriate technique for your tool to pass the contents of the file as a parameter. Either ``SecretBinary`` or ``SecretString`` must have a value, but not both. They cannot both be empty.
        
          This parameter is not accessible if the secret using the Secrets Manager console.
        
        :type SecretString: string
        :param SecretString: 
        
          (Optional) Specifies text data that you want to encrypt and store in this new version of the secret. Either ``SecretString`` or ``SecretBinary`` must have a value, but not both. They cannot both be empty.
        
          If you create this secret by using the Secrets Manager console then Secrets Manager puts the protected secret text in only the ``SecretString`` parameter. The Secrets Manager console stores the information as a JSON structure of key/value pairs that the default Lambda rotation function knows how to parse.
        
          For storing multiple values, we recommend that you use a JSON text string argument and specify key/value pairs. For information on how to format a JSON parameter for the various command line tool environments, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ in the *AWS CLI User Guide* .
        
          For example:
        
           ``[{\"username\":\"bob\"},{\"password\":\"abc123xyz456\"}]``  
        
          If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text.
        
        :type VersionStages: list
        :param VersionStages: 
        
          (Optional) Specifies a list of staging labels that are attached to this version of the secret. These staging labels are used to track the versions through the rotation process by the Lambda rotation function.
        
          A staging label must be unique to a single version of the secret. If you specify a staging label that\'s already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version.
        
          If you do not specify a value for ``VersionStages`` then Secrets Manager automatically moves the staging label ``AWSCURRENT`` to this new version.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ARN\': \'string\',
                \'Name\': \'string\',
                \'VersionId\': \'string\',
                \'VersionStages\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ARN** *(string) --* 
        
              The Amazon Resource Name (ARN) for the secret for which you just created a version.
        
            - **Name** *(string) --* 
        
              The friendly name of the secret for which you just created or updated a version.
        
            - **VersionId** *(string) --* 
        
              The unique identifier of the version of the secret you just created or updated.
        
            - **VersionStages** *(list) --* 
        
              The list of staging labels that are currently attached to this version of the secret. Staging labels are used to track a version as it progresses through the secret rotation process.
        
              - *(string) --* 
          
        """
        pass

    def restore_secret(self, SecretId: str) -> Dict:
        """
        
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:RestoreSecret 
         
         **Related operations**  
        
        * To delete a secret, use  DeleteSecret . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/RestoreSecret>`_
        
        **Request Syntax** 
        ::
        
          response = client.restore_secret(
              SecretId=\'string\'
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          Specifies the secret that you want to restore from a previously scheduled deletion. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ARN\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ARN** *(string) --* 
        
              The ARN of the secret that was restored.
        
            - **Name** *(string) --* 
        
              The friendly name of the secret that was restored.
        
        """
        pass

    def rotate_secret(self, SecretId: str, ClientRequestToken: str = None, RotationLambdaARN: str = None, RotationRules: Dict = None) -> Dict:
        """
        
        This required configuration information includes the ARN of an AWS Lambda function and the time between scheduled rotations. The Lambda rotation function creates a new version of the secret and creates or updates the credentials on the protected service to match. After testing the new credentials, the function marks the new secret with the staging label ``AWSCURRENT`` so that your clients all immediately begin to use the new version. For more information about rotating secrets and how to configure a Lambda function to rotate the secrets for your protected service, see `Rotating Secrets in AWS Secrets Manager <http://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html>`__ in the *AWS Secrets Manager User Guide* .
        
        Secrets Manager schedules the next rotation when the previous one is complete. Secrets Manager schedules the date by adding the rotation interval (number of days) to the actual date of the last rotation. The service chooses the hour within that 24-hour date window randomly. The minute is also chosen somewhat randomly, but weighted towards the top of the hour and influenced by a variety of factors that help distribute load.
        
        The rotation function must end with the versions of the secret in one of two states:
        
        * The ``AWSPENDING`` and ``AWSCURRENT`` staging labels are attached to the same version of the secret, or 
         
        * The ``AWSPENDING`` staging label is not attached to any version of the secret. 
         
        If instead the ``AWSPENDING`` staging label is present but is not attached to the same version as ``AWSCURRENT`` then any later invocation of ``RotateSecret`` assumes that a previous rotation request is still in progress and returns an error.
        
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:RotateSecret 
         
        * lambda:InvokeFunction (on the function specified in the secret\'s metadata) 
         
         **Related operations**  
        
        * To list the secrets in your account, use  ListSecrets . 
         
        * To get the details for a version of a secret, use  DescribeSecret . 
         
        * To create a new version of a secret, use  CreateSecret . 
         
        * To attach staging labels to or remove staging labels from a version of a secret, use  UpdateSecretVersionStage . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/RotateSecret>`_
        
        **Request Syntax** 
        ::
        
          response = client.rotate_secret(
              SecretId=\'string\',
              ClientRequestToken=\'string\',
              RotationLambdaARN=\'string\',
              RotationRules={
                  \'AutomaticallyAfterDays\': 123
              }
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          Specifies the secret that you want to rotate. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          (Optional) Specifies a unique identifier for the new version of the secret that helps ensure idempotency. 
        
          If you use the AWS CLI or one of the AWS SDK to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes that in the request for this parameter. If you don\'t use the SDK and instead generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a ``ClientRequestToken`` yourself for new versions and include that value in the request.
        
          You only need to specify your own value if you are implementing your own retry logic and want to ensure that a given secret is not created twice. We recommend that you generate a `UUID-type <https://wikipedia.org/wiki/Universally_unique_identifier>`__ value to ensure uniqueness within the specified secret. 
        
          Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during the function\'s processing. This value becomes the ``VersionId`` of the new version.
        
          This field is autopopulated if not provided.
        
        :type RotationLambdaARN: string
        :param RotationLambdaARN: 
        
          (Optional) Specifies the ARN of the Lambda function that can rotate the secret.
        
        :type RotationRules: dict
        :param RotationRules: 
        
          A structure that defines the rotation configuration for this secret.
        
          - **AutomaticallyAfterDays** *(integer) --* 
        
            Specifies the number of days between automatic scheduled rotations of the secret.
        
            Secrets Manager schedules the next rotation when the previous one is complete. Secrets Manager schedules the date by adding the rotation interval (number of days) to the actual date of the last rotation. The service chooses the hour within that 24-hour date window randomly. The minute is also chosen somewhat randomly, but weighted towards the top of the hour and influenced by a variety of factors that help distribute load.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ARN\': \'string\',
                \'Name\': \'string\',
                \'VersionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ARN** *(string) --* 
        
              The ARN of the secret.
        
            - **Name** *(string) --* 
        
              The friendly name of the secret.
        
            - **VersionId** *(string) --* 
        
              The ID of the new version of the secret created by the rotation started by this request.
        
        """
        pass

    def tag_resource(self, SecretId: str, Tags: List):
        """
        
        The following basic restrictions apply to tags:
        
        * Maximum number of tags per secret—50 
         
        * Maximum key length—127 Unicode characters in UTF-8 
         
        * Maximum value length—255 Unicode characters in UTF-8 
         
        * Tag keys and values are case sensitive. 
         
        * Do not use the ``aws:`` prefix in your tag names or values because it is reserved for AWS use. You can\'t edit or delete tag names or values with this prefix. Tags with this prefix do not count against your tags per secret limit. 
         
        * If your tagging schema will be used across multiple services and resources, remember that other services might have restrictions on allowed characters. Generally allowed characters are: letters, spaces, and numbers representable in UTF-8, plus the following special characters: + - = . _ : / @. 
         
        .. warning::
        
          If you use tags as part of your security strategy, then adding or removing a tag can change permissions. If successfully completing this operation would result in you losing your permissions for this secret, then the operation is blocked and returns an Access Denied error.
        
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:TagResource 
         
         **Related operations**  
        
        * To remove one or more tags from the collection attached to a secret, use  UntagResource . 
         
        * To view the list of tags attached to a secret, use  DescribeSecret . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/TagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.tag_resource(
              SecretId=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          The identifier for the secret that you want to attach tags to. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          The tags to attach to the secret. Each element in the list consists of a ``Key`` and a ``Value`` .
        
          This parameter to the API requires a JSON text string argument. For information on how to format a JSON parameter for the various command line tool environments, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ in the *AWS CLI User Guide* . For the AWS CLI, you can also use the syntax: ``--Tags Key=\"Key1\",Value=\"Value1\",Key=\"Key2\",Value=\"Value2\"[,…]``  
        
          - *(dict) --* 
        
            A structure that contains information about a tag.
        
            - **Key** *(string) --* 
        
              The key identifier, or name, of the tag.
        
            - **Value** *(string) --* 
        
              The string value that\'s associated with the key of the tag.
        
        :returns: None
        """
        pass

    def untag_resource(self, SecretId: str, TagKeys: List):
        """
        
        This operation is idempotent. If a requested tag is not attached to the secret, no error is returned and the secret metadata is unchanged.
        
        .. warning::
        
          If you use tags as part of your security strategy, then removing a tag can change permissions. If successfully completing this operation would result in you losing your permissions for this secret, then the operation is blocked and returns an Access Denied error.
        
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:UntagResource 
         
         **Related operations**  
        
        * To add one or more tags to the collection attached to a secret, use  TagResource . 
         
        * To view the list of tags attached to a secret, use  DescribeSecret . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/UntagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.untag_resource(
              SecretId=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          The identifier for the secret that you want to remove tags from. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          A list of tag key names to remove from the secret. You don\'t specify the value. Both the key and its associated value are removed.
        
          This parameter to the API requires a JSON text string argument. For information on how to format a JSON parameter for the various command line tool environments, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ in the *AWS CLI User Guide* .
        
          - *(string) --* 
        
        :returns: None
        """
        pass

    def update_secret(self, SecretId: str, ClientRequestToken: str = None, Description: str = None, KmsKeyId: str = None, SecretBinary: bytes = None, SecretString: str = None) -> Dict:
        """
        
        To modify the rotation configuration of a secret, use  RotateSecret instead.
        
        .. note::
        
          The Secrets Manager console uses only the ``SecretString`` parameter and therefore limits you to encrypting and storing only a text string. To encrypt and store binary data as part of the version of a secret, you must use either the AWS CLI or one of the AWS SDKs.
        
        * If a version with a ``VersionId`` with the same value as the ``ClientRequestToken`` parameter already exists, the operation results in an error. You cannot modify an existing version, you can only create a new version. 
         
        * If you include ``SecretString`` or ``SecretBinary`` to create a new secret version, Secrets Manager automatically attaches the staging label ``AWSCURRENT`` to the new version.  
         
        .. note::
        
          * If you call an operation that needs to encrypt or decrypt the ``SecretString`` or ``SecretBinary`` for a secret in the same account as the calling user and that secret doesn\'t specify a AWS KMS encryption key, Secrets Manager uses the account\'s default AWS managed customer master key (CMK) with the alias ``aws/secretsmanager`` . If this key doesn\'t already exist in your account then Secrets Manager creates it for you automatically. All users and roles in the same AWS account automatically have access to use the default CMK. Note that if an Secrets Manager API call results in AWS having to create the account\'s AWS-managed CMK, it can result in a one-time significant delay in returning the result. 
           
          * If the secret is in a different AWS account from the credentials calling an API that requires encryption or decryption of the secret value then you must create and use a custom AWS KMS CMK because you can\'t access the default CMK for the account using credentials from a different AWS account. Store the ARN of the CMK in the secret when you create the secret or when you update it by including it in the ``KMSKeyId`` . If you call an API that must encrypt or decrypt ``SecretString`` or ``SecretBinary`` using credentials from a different account then the AWS KMS key policy must grant cross-account access to that other account\'s user or role for both the kms:GenerateDataKey and kms:Decrypt operations. 
           
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:UpdateSecret 
         
        * kms:GenerateDataKey - needed only if you use a custom AWS KMS key to encrypt the secret. You do not need this permission to use the account\'s AWS managed CMK for Secrets Manager. 
         
        * kms:Decrypt - needed only if you use a custom AWS KMS key to encrypt the secret. You do not need this permission to use the account\'s AWS managed CMK for Secrets Manager. 
         
         **Related operations**  
        
        * To create a new secret, use  CreateSecret . 
         
        * To add only a new version to an existing secret, use  PutSecretValue . 
         
        * To get the details for a secret, use  DescribeSecret . 
         
        * To list the versions contained in a secret, use  ListSecretVersionIds . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/UpdateSecret>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_secret(
              SecretId=\'string\',
              ClientRequestToken=\'string\',
              Description=\'string\',
              KmsKeyId=\'string\',
              SecretBinary=b\'bytes\',
              SecretString=\'string\'
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          Specifies the secret that you want to modify or to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :type ClientRequestToken: string
        :param ClientRequestToken: 
        
          (Optional) If you want to add a new version to the secret, this parameter specifies a unique identifier for the new version that helps ensure idempotency. 
        
          If you use the AWS CLI or one of the AWS SDK to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes that in the request. If you don\'t use the SDK and instead generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a ``ClientRequestToken`` yourself for new versions and include that value in the request.
        
          You typically only need to interact with this value if you implement your own retry logic and want to ensure that a given secret is not created twice. We recommend that you generate a `UUID-type <https://wikipedia.org/wiki/Universally_unique_identifier>`__ value to ensure uniqueness within the specified secret. 
        
          Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during the Lambda rotation function\'s processing.
        
          * If the ``ClientRequestToken`` value isn\'t already associated with a version of the secret then a new version of the secret is created.  
           
          * If a version with this value already exists and that version\'s ``SecretString`` and ``SecretBinary`` values are the same as those in the request then the request is ignored (the operation is idempotent).  
           
          * If a version with this value already exists and that version\'s ``SecretString`` and ``SecretBinary`` values are different from the request then an error occurs because you cannot modify an existing secret value. 
           
          This value becomes the ``VersionId`` of the new version.
        
          This field is autopopulated if not provided.
        
        :type Description: string
        :param Description: 
        
          (Optional) Specifies an updated user-provided description of the secret.
        
        :type KmsKeyId: string
        :param KmsKeyId: 
        
          (Optional) Specifies an updated ARN or alias of the AWS KMS customer master key (CMK) to be used to encrypt the protected text in new versions of this secret.
        
          .. warning::
        
            You can only use the account\'s default CMK to encrypt and decrypt if you call this operation using credentials from the same account that owns the secret. If the secret is in a different account, then you must create a custom CMK and provide the ARN of that CMK in this field. The user making the call must have permissions to both the secret and the CMK in their respective accounts.
        
        :type SecretBinary: bytes
        :param SecretBinary: 
        
          (Optional) Specifies updated binary data that you want to encrypt and store in the new version of the secret. To use this parameter in the command-line tools, we recommend that you store your binary data in a file and then use the appropriate technique for your tool to pass the contents of the file as a parameter. Either ``SecretBinary`` or ``SecretString`` must have a value, but not both. They cannot both be empty.
        
          This parameter is not accessible using the Secrets Manager console.
        
        :type SecretString: string
        :param SecretString: 
        
          (Optional) Specifies updated text data that you want to encrypt and store in this new version of the secret. Either ``SecretBinary`` or ``SecretString`` must have a value, but not both. They cannot both be empty.
        
          If you create this secret by using the Secrets Manager console then Secrets Manager puts the protected secret text in only the ``SecretString`` parameter. The Secrets Manager console stores the information as a JSON structure of key/value pairs that the default Lambda rotation function knows how to parse.
        
          For storing multiple values, we recommend that you use a JSON text string argument and specify key/value pairs. For information on how to format a JSON parameter for the various command line tool environments, see `Using JSON for Parameters <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json>`__ in the *AWS CLI User Guide* . For example:
        
           ``[{\"username\":\"bob\"},{\"password\":\"abc123xyz456\"}]``  
        
          If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text. You can also \'escape\' the double quote character in the embedded JSON text by prefacing each with a backslash. For example, the following string is surrounded by double-quotes. All of the embedded double quotes are escaped:
        
           ``\"[{\\"username\\":\\"bob\\"},{\\"password\\":\\"abc123xyz456\\"}]\"``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ARN\': \'string\',
                \'Name\': \'string\',
                \'VersionId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ARN** *(string) --* 
        
              The ARN of the secret that was updated.
        
              .. note::
        
                Secrets Manager automatically adds several random characters to the name at the end of the ARN when you initially create a secret. This affects only the ARN and not the actual friendly name. This ensures that if you create a new secret with the same name as an old secret that you previously deleted, then users with access to the old secret *don\'t* automatically get access to the new secret because the ARNs are different.
        
            - **Name** *(string) --* 
        
              The friendly name of the secret that was updated.
        
            - **VersionId** *(string) --* 
        
              If a new version of the secret was created by this operation, then ``VersionId`` contains the unique identifier of the new version.
        
        """
        pass

    def update_secret_version_stage(self, SecretId: str, VersionStage: str, RemoveFromVersionId: str = None, MoveToVersionId: str = None) -> Dict:
        """
        
        The staging labels that you specify in the ``VersionStage`` parameter are added to the existing list of staging labels--they don\'t replace it.
        
        You can move the ``AWSCURRENT`` staging label to this version by including it in this call.
        
        .. note::
        
          Whenever you move ``AWSCURRENT`` , Secrets Manager automatically moves the label ``AWSPREVIOUS`` to the version that ``AWSCURRENT`` was removed from.
        
        If this action results in the last label being removed from a version, then the version is considered to be \'deprecated\' and can be deleted by Secrets Manager.
        
         **Minimum permissions**  
        
        To run this command, you must have the following permissions:
        
        * secretsmanager:UpdateSecretVersionStage 
         
         **Related operations**  
        
        * To get the list of staging labels that are currently associated with a version of a secret, use ``  DescribeSecret `` and examine the ``SecretVersionsToStages`` response value.  
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/UpdateSecretVersionStage>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_secret_version_stage(
              SecretId=\'string\',
              VersionStage=\'string\',
              RemoveFromVersionId=\'string\',
              MoveToVersionId=\'string\'
          )
        :type SecretId: string
        :param SecretId: **[REQUIRED]** 
        
          Specifies the secret with the version whose list of staging labels you want to modify. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
        
          .. note::
        
            If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN too—for example, if you don’t include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that you’re specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you don’t create secret names that end with a hyphen followed by six characters.
        
        :type VersionStage: string
        :param VersionStage: **[REQUIRED]** 
        
          The staging label to add to this version.
        
        :type RemoveFromVersionId: string
        :param RemoveFromVersionId: 
        
          Specifies the secret version ID of the version that the staging label is to be removed from. If the staging label you are trying to attach to one version is already attached to a different version, then you must include this parameter and specify the version that the label is to be removed from. If the label is attached and you either do not specify this parameter, or the version ID does not match, then the operation fails.
        
        :type MoveToVersionId: string
        :param MoveToVersionId: 
        
          (Optional) The secret version ID that you want to add the staging label to. If you want to remove a label from a version, then do not specify this parameter.
        
          If the staging label is already attached to a different version of the secret, then you must also specify the ``RemoveFromVersionId`` parameter. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ARN\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ARN** *(string) --* 
        
              The ARN of the secret with the staging label that was modified.
        
            - **Name** *(string) --* 
        
              The friendly name of the secret with the staging label that was modified.
        
        """
        pass
