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

    def cancel_key_deletion(self, KeyId: str) -> Dict:
        """
        
        For more information about scheduling and canceling deletion of a CMK, see `Deleting Customer Master Keys <http://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CancelKeyDeletion>`_
        
        **Request Syntax** 
        ::
        
          response = client.cancel_key_deletion(
              KeyId=\'string\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          The unique identifier for the customer master key (CMK) for which to cancel deletion.
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'KeyId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **KeyId** *(string) --* 
        
              The unique identifier of the master key for which deletion is canceled.
        
        """
        pass

    def create_alias(self, AliasName: str, TargetKeyId: str) -> NoReturn:
        """
        
        Each CMK can have multiple aliases, but each alias points to only one CMK. The alias name must be unique in the AWS account and region. To simplify code that runs in multiple regions, use the same alias name, but point it to a different CMK in each region. 
        
        Because an alias is not a property of a CMK, you can delete and change the aliases of a CMK without affecting the CMK. Also, aliases do not appear in the response from the  DescribeKey operation. To get the aliases of all CMKs, use the  ListAliases operation.
        
        The alias name can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). Alias names cannot begin with **aws/** . That alias name prefix is reserved for AWS managed CMKs.
        
        The alias and the CMK it is mapped to must be in the same AWS account and the same region. You cannot perform this operation on an alias in a different AWS account.
        
        To map an existing alias to a different CMK, call  UpdateAlias .
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_alias(
              AliasName=\'string\',
              TargetKeyId=\'string\'
          )
        :type AliasName: string
        :param AliasName: **[REQUIRED]** 
        
          Specifies the alias name. This value must begin with ``alias/`` followed by the alias name, such as ``alias/ExampleAlias`` . The alias name cannot begin with ``aws/`` . The ``alias/aws/`` prefix is reserved for AWS managed CMKs.
        
        :type TargetKeyId: string
        :param TargetKeyId: **[REQUIRED]** 
        
          Identifies the CMK for which you are creating the alias. This value cannot be an alias.
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :returns: None
        """
        pass

    def create_grant(self, KeyId: str, GranteePrincipal: str, Operations: List, RetiringPrincipal: str = None, Constraints: Dict = None, GrantTokens: List = None, Name: str = None) -> Dict:
        """
        
        To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the ``KeyId`` parameter. For more information about grants, see `Grants <http://docs.aws.amazon.com/kms/latest/developerguide/grants.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateGrant>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_grant(
              KeyId=\'string\',
              GranteePrincipal=\'string\',
              RetiringPrincipal=\'string\',
              Operations=[
                  \'Decrypt\'|\'Encrypt\'|\'GenerateDataKey\'|\'GenerateDataKeyWithoutPlaintext\'|\'ReEncryptFrom\'|\'ReEncryptTo\'|\'CreateGrant\'|\'RetireGrant\'|\'DescribeKey\',
              ],
              Constraints={
                  \'EncryptionContextSubset\': {
                      \'string\': \'string\'
                  },
                  \'EncryptionContextEquals\': {
                      \'string\': \'string\'
                  }
              },
              GrantTokens=[
                  \'string\',
              ],
              Name=\'string\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          The unique identifier for the customer master key (CMK) that the grant applies to.
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :type GranteePrincipal: string
        :param GranteePrincipal: **[REQUIRED]** 
        
          The principal that is given permission to perform the operations that the grant permits.
        
          To specify the principal, use the `Amazon Resource Name (ARN) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, IAM roles, federated users, and assumed role users. For examples of the ARN syntax to use for specifying a principal, see `AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__ in the Example ARNs section of the *AWS General Reference* .
        
        :type RetiringPrincipal: string
        :param RetiringPrincipal: 
        
          The principal that is given permission to retire the grant by using  RetireGrant operation.
        
          To specify the principal, use the `Amazon Resource Name (ARN) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, federated users, and assumed role users. For examples of the ARN syntax to use for specifying a principal, see `AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__ in the Example ARNs section of the *AWS General Reference* .
        
        :type Operations: list
        :param Operations: **[REQUIRED]** 
        
          A list of operations that the grant permits.
        
          - *(string) --* 
        
        :type Constraints: dict
        :param Constraints: 
        
          A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see `Encryption Context <http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html>`__ in the *AWS Key Management Service Developer Guide* .
        
          - **EncryptionContextSubset** *(dict) --* 
        
            A list of key-value pairs, all of which must be present in the encryption context of certain subsequent operations that the grant allows. When certain subsequent operations allowed by the grant include encryption context that matches this list or is a superset of this list, the grant allows the operation. Otherwise, the grant does not allow the operation.
        
            - *(string) --* 
        
              - *(string) --* 
        
          - **EncryptionContextEquals** *(dict) --* 
        
            A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows. When certain subsequent operations allowed by the grant include encryption context that matches this list, the grant allows the operation. Otherwise, the grant does not allow the operation.
        
            - *(string) --* 
        
              - *(string) --* 
        
        :type GrantTokens: list
        :param GrantTokens: 
        
          A list of grant tokens.
        
          For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .
        
          - *(string) --* 
        
        :type Name: string
        :param Name: 
        
          A friendly name for identifying the grant. Use this value to prevent the unintended creation of duplicate grants when retrying this request.
        
          When this value is absent, all ``CreateGrant`` requests result in a new grant with a unique ``GrantId`` even if all the supplied parameters are identical. This can result in unintended duplicates when you retry the ``CreateGrant`` request.
        
          When this value is present, you can retry a ``CreateGrant`` request with identical parameters; if the grant already exists, the original ``GrantId`` is returned without creating a new grant. Note that the returned grant token is unique with every ``CreateGrant`` request, even when a duplicate ``GrantId`` is returned. All grant tokens obtained in this way can be used interchangeably.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GrantToken\': \'string\',
                \'GrantId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **GrantToken** *(string) --* 
        
              The grant token.
        
              For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .
        
            - **GrantId** *(string) --* 
        
              The unique identifier for the grant.
        
              You can use the ``GrantId`` in a subsequent  RetireGrant or  RevokeGrant operation.
        
        """
        pass

    def create_key(self, Policy: str = None, Description: str = None, KeyUsage: str = None, Origin: str = None, BypassPolicyLockoutSafetyCheck: bool = None, Tags: List = None) -> Dict:
        """
        
        You can use a CMK to encrypt small amounts of data (4 KiB or less) directly. But CMKs are more commonly used to encrypt data encryption keys (DEKs), which are used to encrypt raw data. For more information about DEKs and the difference between CMKs and DEKs, see the following:
        
        * The  GenerateDataKey operation 
         
        * `AWS Key Management Service Concepts <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ in the *AWS Key Management Service Developer Guide*   
         
        You cannot use this operation to create a CMK in a different AWS account.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateKey>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_key(
              Policy=\'string\',
              Description=\'string\',
              KeyUsage=\'ENCRYPT_DECRYPT\',
              Origin=\'AWS_KMS\'|\'EXTERNAL\',
              BypassPolicyLockoutSafetyCheck=True|False,
              Tags=[
                  {
                      \'TagKey\': \'string\',
                      \'TagValue\': \'string\'
                  },
              ]
          )
        :type Policy: string
        :param Policy: 
        
          The key policy to attach to the CMK.
        
          If you provide a key policy, it must meet the following criteria:
        
          * If you don\'t set ``BypassPolicyLockoutSafetyCheck`` to true, the key policy must allow the principal that is making the ``CreateKey`` request to make a subsequent  PutKeyPolicy request on the CMK. This reduces the risk that the CMK becomes unmanageable. For more information, refer to the scenario in the `Default Key Policy <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`__ section of the *AWS Key Management Service Developer Guide* . 
           
          * Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy. The reason for this is that the new principal might not be immediately visible to AWS KMS. For more information, see `Changes that I make are not always immediately visible <http://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency>`__ in the *AWS Identity and Access Management User Guide* . 
           
          If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK. For more information, see `Default Key Policy <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default>`__ in the *AWS Key Management Service Developer Guide* .
        
          The key policy size limit is 32 kilobytes (32768 bytes).
        
        :type Description: string
        :param Description: 
        
          A description of the CMK.
        
          Use a description that helps you decide whether the CMK is appropriate for a task.
        
        :type KeyUsage: string
        :param KeyUsage: 
        
          The intended use of the CMK.
        
          You can use CMKs only for symmetric encryption and decryption.
        
        :type Origin: string
        :param Origin: 
        
          The source of the CMK\'s key material.
        
          The default is ``AWS_KMS`` , which means AWS KMS creates the key material. When this parameter is set to ``EXTERNAL`` , the request creates a CMK without key material so that you can import key material from your existing key management infrastructure. For more information about importing key material into AWS KMS, see `Importing Key Material <http://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ in the *AWS Key Management Service Developer Guide* .
        
          The CMK\'s ``Origin`` is immutable and is set when the CMK is created.
        
        :type BypassPolicyLockoutSafetyCheck: boolean
        :param BypassPolicyLockoutSafetyCheck: 
        
          A flag to indicate whether to bypass the key policy lockout safety check.
        
          .. warning::
        
            Setting this value to true increases the risk that the CMK becomes unmanageable. Do not set this value to true indiscriminately.
        
            For more information, refer to the scenario in the `Default Key Policy <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`__ section in the *AWS Key Management Service Developer Guide* .
        
          Use this parameter only when you include a policy in the request and you intend to prevent the principal that is making the request from making a subsequent  PutKeyPolicy request on the CMK.
        
          The default value is false.
        
        :type Tags: list
        :param Tags: 
        
          One or more tags. Each tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.
        
          Use this parameter to tag the CMK when it is created. Alternately, you can omit this parameter and instead tag the CMK after it is created using  TagResource .
        
          - *(dict) --* 
        
            A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.
        
            For information about the rules that apply to tag keys and tag values, see `User-Defined Tag Restrictions <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__ in the *AWS Billing and Cost Management User Guide* .
        
            - **TagKey** *(string) --* **[REQUIRED]** 
        
              The key of the tag.
        
            - **TagValue** *(string) --* **[REQUIRED]** 
        
              The value of the tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'KeyMetadata\': {
                    \'AWSAccountId\': \'string\',
                    \'KeyId\': \'string\',
                    \'Arn\': \'string\',
                    \'CreationDate\': datetime(2015, 1, 1),
                    \'Enabled\': True|False,
                    \'Description\': \'string\',
                    \'KeyUsage\': \'ENCRYPT_DECRYPT\',
                    \'KeyState\': \'Enabled\'|\'Disabled\'|\'PendingDeletion\'|\'PendingImport\',
                    \'DeletionDate\': datetime(2015, 1, 1),
                    \'ValidTo\': datetime(2015, 1, 1),
                    \'Origin\': \'AWS_KMS\'|\'EXTERNAL\',
                    \'ExpirationModel\': \'KEY_MATERIAL_EXPIRES\'|\'KEY_MATERIAL_DOES_NOT_EXPIRE\',
                    \'KeyManager\': \'AWS\'|\'CUSTOMER\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **KeyMetadata** *(dict) --* 
        
              Metadata associated with the CMK.
        
              - **AWSAccountId** *(string) --* 
        
                The twelve-digit account ID of the AWS account that owns the CMK.
        
              - **KeyId** *(string) --* 
        
                The globally unique identifier for the CMK.
        
              - **Arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the CMK. For examples, see `AWS Key Management Service (AWS KMS) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms>`__ in the Example ARNs section of the *AWS General Reference* .
        
              - **CreationDate** *(datetime) --* 
        
                The date and time when the CMK was created.
        
              - **Enabled** *(boolean) --* 
        
                Specifies whether the CMK is enabled. When ``KeyState`` is ``Enabled`` this value is true, otherwise it is false.
        
              - **Description** *(string) --* 
        
                The description of the CMK.
        
              - **KeyUsage** *(string) --* 
        
                The cryptographic operations for which you can use the CMK. Currently the only allowed value is ``ENCRYPT_DECRYPT`` , which means you can use the CMK for the  Encrypt and  Decrypt operations.
        
              - **KeyState** *(string) --* 
        
                The state of the CMK.
        
                For more information about how key state affects the use of a CMK, see `How Key State Affects the Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
              - **DeletionDate** *(datetime) --* 
        
                The date and time after which AWS KMS deletes the CMK. This value is present only when ``KeyState`` is ``PendingDeletion`` , otherwise this value is omitted.
        
              - **ValidTo** *(datetime) --* 
        
                The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. This value is present only for CMKs whose ``Origin`` is ``EXTERNAL`` and whose ``ExpirationModel`` is ``KEY_MATERIAL_EXPIRES`` , otherwise this value is omitted.
        
              - **Origin** *(string) --* 
        
                The source of the CMK\'s key material. When this value is ``AWS_KMS`` , AWS KMS created the key material. When this value is ``EXTERNAL`` , the key material was imported from your existing key management infrastructure or the CMK lacks key material.
        
              - **ExpirationModel** *(string) --* 
        
                Specifies whether the CMK\'s key material expires. This value is present only when ``Origin`` is ``EXTERNAL`` , otherwise this value is omitted.
        
              - **KeyManager** *(string) --* 
        
                The CMK\'s manager. CMKs are either customer managed or AWS managed. For more information about the difference, see `Customer Master Keys <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ in the *AWS Key Management Service Developer Guide* .
        
        """
        pass

    def decrypt(self, CiphertextBlob: bytes, EncryptionContext: Dict = None, GrantTokens: List = None) -> Dict:
        """
        Decrypts ciphertext. Ciphertext is plaintext that has been previously encrypted by using any of the following operations:
        
        *  GenerateDataKey   
         
        *  GenerateDataKeyWithoutPlaintext   
         
        *  Encrypt   
         
        Whenever possible, use key policies to give users permission to call the Decrypt operation on the CMK, instead of IAM policies. Otherwise, you might create an IAM user policy that gives the user Decrypt permission on all CMKs. This user could decrypt ciphertext that was encrypted by CMKs in other accounts if the key policy for the cross-account CMK permits it. If you must use an IAM policy for ``Decrypt`` permissions, limit the user to particular CMKs or particular trusted accounts.
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/Decrypt>`_
        
        **Request Syntax** 
        ::
        
          response = client.decrypt(
              CiphertextBlob=b\'bytes\',
              EncryptionContext={
                  \'string\': \'string\'
              },
              GrantTokens=[
                  \'string\',
              ]
          )
        :type CiphertextBlob: bytes
        :param CiphertextBlob: **[REQUIRED]** 
        
          Ciphertext to be decrypted. The blob includes metadata.
        
        :type EncryptionContext: dict
        :param EncryptionContext: 
        
          The encryption context. If this was specified in the  Encrypt function, it must be specified here or the decryption operation will fail. For more information, see `Encryption Context <http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html>`__ .
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type GrantTokens: list
        :param GrantTokens: 
        
          A list of grant tokens.
        
          For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'KeyId\': \'string\',
                \'Plaintext\': b\'bytes\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **KeyId** *(string) --* 
        
              ARN of the key used to perform the decryption. This value is returned if no errors are encountered during the operation.
        
            - **Plaintext** *(bytes) --* 
        
              Decrypted plaintext data. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded.
        
        """
        pass

    def delete_alias(self, AliasName: str) -> NoReturn:
        """
        
        Because an alias is not a property of a CMK, you can delete and change the aliases of a CMK without affecting the CMK. Also, aliases do not appear in the response from the  DescribeKey operation. To get the aliases of all CMKs, use the  ListAliases operation. 
        
        Each CMK can have multiple aliases. To change the alias of a CMK, use  DeleteAlias to delete the current alias and  CreateAlias to create a new alias. To associate an existing alias with a different customer master key (CMK), call  UpdateAlias .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DeleteAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_alias(
              AliasName=\'string\'
          )
        :type AliasName: string
        :param AliasName: **[REQUIRED]** 
        
          The alias to be deleted. The name must start with the word \"alias\" followed by a forward slash (alias/). Aliases that begin with \"alias/aws\" are reserved.
        
        :returns: None
        """
        pass

    def delete_imported_key_material(self, KeyId: str) -> NoReturn:
        """
        
        When the specified CMK is in the ``PendingDeletion`` state, this operation does not change the CMK\'s state. Otherwise, it changes the CMK\'s state to ``PendingImport`` .
        
        After you delete key material, you can use  ImportKeyMaterial to reimport the same key material into the CMK.
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DeleteImportedKeyMaterial>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_imported_key_material(
              KeyId=\'string\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          The identifier of the CMK whose key material to delete. The CMK\'s ``Origin`` must be ``EXTERNAL`` .
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :returns: None
        """
        pass

    def describe_key(self, KeyId: str, GrantTokens: List = None) -> Dict:
        """
        
        You can use ``DescribeKey`` on a predefined AWS alias, that is, an AWS alias with no key ID. When you do, AWS KMS associates the alias with an `AWS managed CMK <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ and returns its ``KeyId`` and ``Arn`` in the response.
        
        To perform this operation on a CMK in a different AWS account, specify the key ARN or alias ARN in the value of the KeyId parameter.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DescribeKey>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_key(
              KeyId=\'string\',
              GrantTokens=[
                  \'string\',
              ]
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          Describes the specified customer master key (CMK). 
        
          If you specify a predefined AWS alias (an AWS alias with no key ID), KMS associates the alias with an `AWS managed CMK <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ and returns its ``KeyId`` and ``Arn`` in the response.
        
          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with ``\"alias/\"`` . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Alias name: ``alias/ExampleAlias``   
           
          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .
        
        :type GrantTokens: list
        :param GrantTokens: 
        
          A list of grant tokens.
        
          For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'KeyMetadata\': {
                    \'AWSAccountId\': \'string\',
                    \'KeyId\': \'string\',
                    \'Arn\': \'string\',
                    \'CreationDate\': datetime(2015, 1, 1),
                    \'Enabled\': True|False,
                    \'Description\': \'string\',
                    \'KeyUsage\': \'ENCRYPT_DECRYPT\',
                    \'KeyState\': \'Enabled\'|\'Disabled\'|\'PendingDeletion\'|\'PendingImport\',
                    \'DeletionDate\': datetime(2015, 1, 1),
                    \'ValidTo\': datetime(2015, 1, 1),
                    \'Origin\': \'AWS_KMS\'|\'EXTERNAL\',
                    \'ExpirationModel\': \'KEY_MATERIAL_EXPIRES\'|\'KEY_MATERIAL_DOES_NOT_EXPIRE\',
                    \'KeyManager\': \'AWS\'|\'CUSTOMER\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **KeyMetadata** *(dict) --* 
        
              Metadata associated with the key.
        
              - **AWSAccountId** *(string) --* 
        
                The twelve-digit account ID of the AWS account that owns the CMK.
        
              - **KeyId** *(string) --* 
        
                The globally unique identifier for the CMK.
        
              - **Arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the CMK. For examples, see `AWS Key Management Service (AWS KMS) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms>`__ in the Example ARNs section of the *AWS General Reference* .
        
              - **CreationDate** *(datetime) --* 
        
                The date and time when the CMK was created.
        
              - **Enabled** *(boolean) --* 
        
                Specifies whether the CMK is enabled. When ``KeyState`` is ``Enabled`` this value is true, otherwise it is false.
        
              - **Description** *(string) --* 
        
                The description of the CMK.
        
              - **KeyUsage** *(string) --* 
        
                The cryptographic operations for which you can use the CMK. Currently the only allowed value is ``ENCRYPT_DECRYPT`` , which means you can use the CMK for the  Encrypt and  Decrypt operations.
        
              - **KeyState** *(string) --* 
        
                The state of the CMK.
        
                For more information about how key state affects the use of a CMK, see `How Key State Affects the Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
              - **DeletionDate** *(datetime) --* 
        
                The date and time after which AWS KMS deletes the CMK. This value is present only when ``KeyState`` is ``PendingDeletion`` , otherwise this value is omitted.
        
              - **ValidTo** *(datetime) --* 
        
                The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. This value is present only for CMKs whose ``Origin`` is ``EXTERNAL`` and whose ``ExpirationModel`` is ``KEY_MATERIAL_EXPIRES`` , otherwise this value is omitted.
        
              - **Origin** *(string) --* 
        
                The source of the CMK\'s key material. When this value is ``AWS_KMS`` , AWS KMS created the key material. When this value is ``EXTERNAL`` , the key material was imported from your existing key management infrastructure or the CMK lacks key material.
        
              - **ExpirationModel** *(string) --* 
        
                Specifies whether the CMK\'s key material expires. This value is present only when ``Origin`` is ``EXTERNAL`` , otherwise this value is omitted.
        
              - **KeyManager** *(string) --* 
        
                The CMK\'s manager. CMKs are either customer managed or AWS managed. For more information about the difference, see `Customer Master Keys <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ in the *AWS Key Management Service Developer Guide* .
        
        """
        pass

    def disable_key(self, KeyId: str) -> NoReturn:
        """
        
        For more information about how key state affects the use of a CMK, see `How Key State Affects the Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DisableKey>`_
        
        **Request Syntax** 
        ::
        
          response = client.disable_key(
              KeyId=\'string\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the customer master key (CMK).
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :returns: None
        """
        pass

    def disable_key_rotation(self, KeyId: str) -> NoReturn:
        """
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DisableKeyRotation>`_
        
        **Request Syntax** 
        ::
        
          response = client.disable_key_rotation(
              KeyId=\'string\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the customer master key (CMK).
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :returns: None
        """
        pass

    def enable_key(self, KeyId: str) -> NoReturn:
        """
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/EnableKey>`_
        
        **Request Syntax** 
        ::
        
          response = client.enable_key(
              KeyId=\'string\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the customer master key (CMK).
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :returns: None
        """
        pass

    def enable_key_rotation(self, KeyId: str) -> NoReturn:
        """
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/EnableKeyRotation>`_
        
        **Request Syntax** 
        ::
        
          response = client.enable_key_rotation(
              KeyId=\'string\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the customer master key (CMK).
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :returns: None
        """
        pass

    def encrypt(self, KeyId: str, Plaintext: bytes, EncryptionContext: Dict = None, GrantTokens: List = None) -> Dict:
        """
        Encrypts plaintext into ciphertext by using a customer master key (CMK). The ``Encrypt`` operation has two primary use cases:
        
        * You can encrypt up to 4 kilobytes (4096 bytes) of arbitrary data such as an RSA key, a database password, or other sensitive information. 
         
        * You can use the ``Encrypt`` operation to move encrypted data from one AWS region to another. In the first region, generate a data key and use the plaintext key to encrypt the data. Then, in the new region, call the ``Encrypt`` method on same plaintext data key. Now, you can safely move the encrypted data and encrypted data key to the new region, and decrypt in the new region when necessary. 
         
        You don\'t need use this operation to encrypt a data key within a region. The  GenerateDataKey and  GenerateDataKeyWithoutPlaintext operations return an encrypted data key.
        
        Also, you don\'t need to use this operation to encrypt data in your application. You can use the plaintext and encrypted data keys that the ``GenerateDataKey`` operation returns.
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        To perform this operation on a CMK in a different AWS account, specify the key ARN or alias ARN in the value of the KeyId parameter.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/Encrypt>`_
        
        **Request Syntax** 
        ::
        
          response = client.encrypt(
              KeyId=\'string\',
              Plaintext=b\'bytes\',
              EncryptionContext={
                  \'string\': \'string\'
              },
              GrantTokens=[
                  \'string\',
              ]
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the customer master key (CMK).
        
          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with ``\"alias/\"`` . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Alias name: ``alias/ExampleAlias``   
           
          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .
        
        :type Plaintext: bytes
        :param Plaintext: **[REQUIRED]** 
        
          Data to be encrypted.
        
        :type EncryptionContext: dict
        :param EncryptionContext: 
        
          Name-value pair that specifies the encryption context to be used for authenticated encryption. If used here, the same value must be supplied to the ``Decrypt`` API or decryption will fail. For more information, see `Encryption Context <http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html>`__ .
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type GrantTokens: list
        :param GrantTokens: 
        
          A list of grant tokens.
        
          For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CiphertextBlob\': b\'bytes\',
                \'KeyId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CiphertextBlob** *(bytes) --* 
        
              The encrypted plaintext. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded.
        
            - **KeyId** *(string) --* 
        
              The ID of the key used during encryption.
        
        """
        pass

    def generate_data_key(self, KeyId: str, EncryptionContext: Dict = None, NumberOfBytes: int = None, KeySpec: str = None, GrantTokens: List = None) -> Dict:
        """
        
        You must specify the customer master key (CMK) under which to generate the data key. You must also specify the length of the data key using either the ``KeySpec`` or ``NumberOfBytes`` field. You must specify one field or the other, but not both. For common key lengths (128-bit and 256-bit symmetric keys), we recommend that you use ``KeySpec`` . To perform this operation on a CMK in a different AWS account, specify the key ARN or alias ARN in the value of the KeyId parameter.
        
        This operation returns a plaintext copy of the data key in the ``Plaintext`` field of the response, and an encrypted copy of the data key in the ``CiphertextBlob`` field. The data key is encrypted under the CMK specified in the ``KeyId`` field of the request. 
        
        We recommend that you use the following pattern to encrypt data locally in your application:
        
        * Use this operation (``GenerateDataKey`` ) to get a data encryption key. 
         
        * Use the plaintext data encryption key (returned in the ``Plaintext`` field of the response) to encrypt data locally, then erase the plaintext data key from memory. 
         
        * Store the encrypted data key (returned in the ``CiphertextBlob`` field of the response) alongside the locally encrypted data. 
         
        To decrypt data locally:
        
        * Use the  Decrypt operation to decrypt the encrypted data key into a plaintext copy of the data key. 
         
        * Use the plaintext data key to decrypt data locally, then erase the plaintext data key from memory. 
         
        To return only an encrypted copy of the data key, use  GenerateDataKeyWithoutPlaintext . To return a random byte string that is cryptographically secure, use  GenerateRandom .
        
        If you use the optional ``EncryptionContext`` field, you must store at least enough information to be able to reconstruct the full encryption context when you later send the ciphertext to the  Decrypt operation. It is a good practice to choose an encryption context that you can reconstruct on the fly to better secure the ciphertext. For more information, see `Encryption Context <http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GenerateDataKey>`_
        
        **Request Syntax** 
        ::
        
          response = client.generate_data_key(
              KeyId=\'string\',
              EncryptionContext={
                  \'string\': \'string\'
              },
              NumberOfBytes=123,
              KeySpec=\'AES_256\'|\'AES_128\',
              GrantTokens=[
                  \'string\',
              ]
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          The identifier of the CMK under which to generate and encrypt the data encryption key.
        
          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with ``\"alias/\"`` . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Alias name: ``alias/ExampleAlias``   
           
          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .
        
        :type EncryptionContext: dict
        :param EncryptionContext: 
        
          A set of key-value pairs that represents additional authenticated data.
        
          For more information, see `Encryption Context <http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html>`__ in the *AWS Key Management Service Developer Guide* .
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type NumberOfBytes: integer
        :param NumberOfBytes: 
        
          The length of the data encryption key in bytes. For example, use the value 64 to generate a 512-bit data key (64 bytes is 512 bits). For common key lengths (128-bit and 256-bit symmetric keys), we recommend that you use the ``KeySpec`` field instead of this one.
        
        :type KeySpec: string
        :param KeySpec: 
        
          The length of the data encryption key. Use ``AES_128`` to generate a 128-bit symmetric key, or ``AES_256`` to generate a 256-bit symmetric key.
        
        :type GrantTokens: list
        :param GrantTokens: 
        
          A list of grant tokens.
        
          For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CiphertextBlob\': b\'bytes\',
                \'Plaintext\': b\'bytes\',
                \'KeyId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CiphertextBlob** *(bytes) --* 
        
              The encrypted data encryption key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded.
        
            - **Plaintext** *(bytes) --* 
        
              The data encryption key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded. Use this data key for local encryption and decryption, then remove it from memory as soon as possible.
        
            - **KeyId** *(string) --* 
        
              The identifier of the CMK under which the data encryption key was generated and encrypted.
        
        """
        pass

    def generate_data_key_without_plaintext(self, KeyId: str, EncryptionContext: Dict = None, KeySpec: str = None, NumberOfBytes: int = None, GrantTokens: List = None) -> Dict:
        """
        
        To perform this operation on a CMK in a different AWS account, specify the key ARN or alias ARN in the value of the KeyId parameter.
        
        This operation is useful in a system that has multiple components with different degrees of trust. For example, consider a system that stores encrypted data in containers. Each container stores the encrypted data and an encrypted copy of the data key. One component of the system, called the *control plane* , creates new containers. When it creates a new container, it uses this operation (``GenerateDataKeyWithoutPlaintext`` ) to get an encrypted data key and then stores it in the container. Later, a different component of the system, called the *data plane* , puts encrypted data into the containers. To do this, it passes the encrypted data key to the  Decrypt operation. It then uses the returned plaintext data key to encrypt data and finally stores the encrypted data in the container. In this system, the control plane never sees the plaintext data key.
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GenerateDataKeyWithoutPlaintext>`_
        
        **Request Syntax** 
        ::
        
          response = client.generate_data_key_without_plaintext(
              KeyId=\'string\',
              EncryptionContext={
                  \'string\': \'string\'
              },
              KeySpec=\'AES_256\'|\'AES_128\',
              NumberOfBytes=123,
              GrantTokens=[
                  \'string\',
              ]
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          The identifier of the customer master key (CMK) under which to generate and encrypt the data encryption key.
        
          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with ``\"alias/\"`` . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Alias name: ``alias/ExampleAlias``   
           
          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .
        
        :type EncryptionContext: dict
        :param EncryptionContext: 
        
          A set of key-value pairs that represents additional authenticated data.
        
          For more information, see `Encryption Context <http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html>`__ in the *AWS Key Management Service Developer Guide* .
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type KeySpec: string
        :param KeySpec: 
        
          The length of the data encryption key. Use ``AES_128`` to generate a 128-bit symmetric key, or ``AES_256`` to generate a 256-bit symmetric key.
        
        :type NumberOfBytes: integer
        :param NumberOfBytes: 
        
          The length of the data encryption key in bytes. For example, use the value 64 to generate a 512-bit data key (64 bytes is 512 bits). For common key lengths (128-bit and 256-bit symmetric keys), we recommend that you use the ``KeySpec`` field instead of this one.
        
        :type GrantTokens: list
        :param GrantTokens: 
        
          A list of grant tokens.
        
          For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CiphertextBlob\': b\'bytes\',
                \'KeyId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CiphertextBlob** *(bytes) --* 
        
              The encrypted data encryption key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded.
        
            - **KeyId** *(string) --* 
        
              The identifier of the CMK under which the data encryption key was generated and encrypted.
        
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

    def generate_random(self, NumberOfBytes: int = None) -> Dict:
        """
        
        For more information about entropy and random number generation, see the `AWS Key Management Service Cryptographic Details <https://d0.awsstatic.com/whitepapers/KMS-Cryptographic-Details.pdf>`__ whitepaper.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GenerateRandom>`_
        
        **Request Syntax** 
        ::
        
          response = client.generate_random(
              NumberOfBytes=123
          )
        :type NumberOfBytes: integer
        :param NumberOfBytes: 
        
          The length of the byte string.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Plaintext\': b\'bytes\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Plaintext** *(bytes) --* 
        
              The random byte string. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded.
        
        """
        pass

    def get_key_policy(self, KeyId: str, PolicyName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetKeyPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_key_policy(
              KeyId=\'string\',
              PolicyName=\'string\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the customer master key (CMK).
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :type PolicyName: string
        :param PolicyName: **[REQUIRED]** 
        
          Specifies the name of the key policy. The only valid name is ``default`` . To get the names of key policies, use  ListKeyPolicies .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Policy\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Policy** *(string) --* 
        
              A key policy document in JSON format.
        
        """
        pass

    def get_key_rotation_status(self, KeyId: str) -> Dict:
        """
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        * Disabled: The key rotation status does not change when you disable a CMK. However, while the CMK is disabled, AWS KMS does not rotate the backing key. 
         
        * Pending deletion: While a CMK is pending deletion, its key rotation status is ``false`` and AWS KMS does not rotate the backing key. If you cancel the deletion, the original key rotation status is restored. 
         
        To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the ``KeyId`` parameter.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetKeyRotationStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_key_rotation_status(
              KeyId=\'string\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the customer master key (CMK).
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'KeyRotationEnabled\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **KeyRotationEnabled** *(boolean) --* 
        
              A Boolean value that specifies whether key rotation is enabled.
        
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

    def get_parameters_for_import(self, KeyId: str, WrappingAlgorithm: str, WrappingKeySpec: str) -> Dict:
        """
        
        You must specify the key ID of the customer master key (CMK) into which you will import key material. This CMK\'s ``Origin`` must be ``EXTERNAL`` . You must also specify the wrapping algorithm and type of wrapping key (public key) that you will use to encrypt the key material. You cannot perform this operation on a CMK in a different AWS account.
        
        This operation returns a public key and an import token. Use the public key to encrypt the key material. Store the import token to send with a subsequent  ImportKeyMaterial request. The public key and import token from the same response must be used together. These items are valid for 24 hours. When they expire, they cannot be used for a subsequent  ImportKeyMaterial request. To get new ones, send another ``GetParametersForImport`` request.
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetParametersForImport>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_parameters_for_import(
              KeyId=\'string\',
              WrappingAlgorithm=\'RSAES_PKCS1_V1_5\'|\'RSAES_OAEP_SHA_1\'|\'RSAES_OAEP_SHA_256\',
              WrappingKeySpec=\'RSA_2048\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          The identifier of the CMK into which you will import key material. The CMK\'s ``Origin`` must be ``EXTERNAL`` .
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :type WrappingAlgorithm: string
        :param WrappingAlgorithm: **[REQUIRED]** 
        
          The algorithm you use to encrypt the key material before importing it with  ImportKeyMaterial . For more information, see `Encrypt the Key Material <http://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-encrypt-key-material.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        :type WrappingKeySpec: string
        :param WrappingKeySpec: **[REQUIRED]** 
        
          The type of wrapping key (public key) to return in the response. Only 2048-bit RSA public keys are supported.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'KeyId\': \'string\',
                \'ImportToken\': b\'bytes\',
                \'PublicKey\': b\'bytes\',
                \'ParametersValidTo\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **KeyId** *(string) --* 
        
              The identifier of the CMK to use in a subsequent  ImportKeyMaterial request. This is the same CMK specified in the ``GetParametersForImport`` request.
        
            - **ImportToken** *(bytes) --* 
        
              The import token to send in a subsequent  ImportKeyMaterial request.
        
            - **PublicKey** *(bytes) --* 
        
              The public key to use to encrypt the key material before importing it with  ImportKeyMaterial .
        
            - **ParametersValidTo** *(datetime) --* 
        
              The time at which the import token and public key are no longer valid. After this time, you cannot use them to make an  ImportKeyMaterial request and you must send another ``GetParametersForImport`` request to get new ones.
        
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

    def import_key_material(self, KeyId: str, ImportToken: bytes, EncryptedKeyMaterial: bytes, ValidTo: datetime = None, ExpirationModel: str = None) -> Dict:
        """
        
        Before using this operation, call  GetParametersForImport . Its response includes a public key and an import token. Use the public key to encrypt the key material. Then, submit the import token from the same ``GetParametersForImport`` response.
        
        When calling this operation, you must specify the following values:
        
        * The key ID or key ARN of a CMK with no key material. Its ``Origin`` must be ``EXTERNAL`` . To create a CMK with no key material, call  CreateKey and set the value of its ``Origin`` parameter to ``EXTERNAL`` . To get the ``Origin`` of a CMK, call  DescribeKey .) 
         
        * The encrypted key material. To get the public key to encrypt the key material, call  GetParametersForImport . 
         
        * The import token that  GetParametersForImport returned. This token and the public key used to encrypt the key material must have come from the same response. 
         
        * Whether the key material expires and if so, when. If you set an expiration date, you can change it only by reimporting the same key material and specifying a new expiration date. If the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. To use the CMK again, you must reimport the same key material. 
         
        When this operation is successful, the CMK\'s key state changes from ``PendingImport`` to ``Enabled`` , and you can use the CMK. After you successfully import key material into a CMK, you can reimport the same key material into that CMK, but you cannot import different key material.
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ImportKeyMaterial>`_
        
        **Request Syntax** 
        ::
        
          response = client.import_key_material(
              KeyId=\'string\',
              ImportToken=b\'bytes\',
              EncryptedKeyMaterial=b\'bytes\',
              ValidTo=datetime(2015, 1, 1),
              ExpirationModel=\'KEY_MATERIAL_EXPIRES\'|\'KEY_MATERIAL_DOES_NOT_EXPIRE\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          The identifier of the CMK to import the key material into. The CMK\'s ``Origin`` must be ``EXTERNAL`` .
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :type ImportToken: bytes
        :param ImportToken: **[REQUIRED]** 
        
          The import token that you received in the response to a previous  GetParametersForImport request. It must be from the same response that contained the public key that you used to encrypt the key material.
        
        :type EncryptedKeyMaterial: bytes
        :param EncryptedKeyMaterial: **[REQUIRED]** 
        
          The encrypted key material to import. It must be encrypted with the public key that you received in the response to a previous  GetParametersForImport request, using the wrapping algorithm that you specified in that request.
        
        :type ValidTo: datetime
        :param ValidTo: 
        
          The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. You must omit this parameter when the ``ExpirationModel`` parameter is set to ``KEY_MATERIAL_DOES_NOT_EXPIRE`` . Otherwise it is required.
        
        :type ExpirationModel: string
        :param ExpirationModel: 
        
          Specifies whether the key material expires. The default is ``KEY_MATERIAL_EXPIRES`` , in which case you must include the ``ValidTo`` parameter. When this parameter is set to ``KEY_MATERIAL_DOES_NOT_EXPIRE`` , you must omit the ``ValidTo`` parameter.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def list_aliases(self, KeyId: str = None, Limit: int = None, Marker: str = None) -> Dict:
        """
        
        By default, the ListAliases command returns all aliases in the account and region. To get only the aliases that point to a particular customer master key (CMK), use the ``KeyId`` parameter.
        
        The ``ListAliases`` response can include aliases that you created and associated with your customer managed CMKs, and aliases that AWS created and associated with AWS managed CMKs in your account. You can recognize AWS aliases because their names have the format ``aws/<service-name>`` , such as ``aws/dynamodb`` .
        
        The response might also include aliases that have no ``TargetKeyId`` field. These are predefined aliases that AWS has created but has not yet associated with a CMK. Aliases that AWS creates in your account, including predefined aliases, do not count against your `AWS KMS aliases limit <http://docs.aws.amazon.com/kms/latest/developerguide/limits.html#aliases-limit>`__ .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListAliases>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_aliases(
              KeyId=\'string\',
              Limit=123,
              Marker=\'string\'
          )
        :type KeyId: string
        :param KeyId: 
        
          Lists only aliases that refer to the specified CMK. The value of this parameter can be the ID or Amazon Resource Name (ARN) of a CMK in the caller\'s account and region. You cannot use an alias name or alias ARN in this value.
        
          This parameter is optional. If you omit it, ``ListAliases`` returns all aliases in the account and region.
        
        :type Limit: integer
        :param Limit: 
        
          Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
        
          This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.
        
        :type Marker: string
        :param Marker: 
        
          Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextMarker`` from the truncated response you just received.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Aliases\': [
                    {
                        \'AliasName\': \'string\',
                        \'AliasArn\': \'string\',
                        \'TargetKeyId\': \'string\'
                    },
                ],
                \'NextMarker\': \'string\',
                \'Truncated\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Aliases** *(list) --* 
        
              A list of aliases.
        
              - *(dict) --* 
        
                Contains information about an alias.
        
                - **AliasName** *(string) --* 
        
                  String that contains the alias.
        
                - **AliasArn** *(string) --* 
        
                  String that contains the key ARN.
        
                - **TargetKeyId** *(string) --* 
        
                  String that contains the key identifier referred to by the alias.
        
            - **NextMarker** *(string) --* 
        
              When ``Truncated`` is true, this element is present and contains the value to use for the ``Marker`` parameter in a subsequent request.
        
            - **Truncated** *(boolean) --* 
        
              A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.
        
        """
        pass

    def list_grants(self, KeyId: str, Limit: int = None, Marker: str = None) -> Dict:
        """
        
        To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the ``KeyId`` parameter.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListGrants>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_grants(
              Limit=123,
              Marker=\'string\',
              KeyId=\'string\'
          )
        :type Limit: integer
        :param Limit: 
        
          Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
        
          This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.
        
        :type Marker: string
        :param Marker: 
        
          Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextMarker`` from the truncated response you just received.
        
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the customer master key (CMK).
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Grants\': [
                    {
                        \'KeyId\': \'string\',
                        \'GrantId\': \'string\',
                        \'Name\': \'string\',
                        \'CreationDate\': datetime(2015, 1, 1),
                        \'GranteePrincipal\': \'string\',
                        \'RetiringPrincipal\': \'string\',
                        \'IssuingAccount\': \'string\',
                        \'Operations\': [
                            \'Decrypt\'|\'Encrypt\'|\'GenerateDataKey\'|\'GenerateDataKeyWithoutPlaintext\'|\'ReEncryptFrom\'|\'ReEncryptTo\'|\'CreateGrant\'|\'RetireGrant\'|\'DescribeKey\',
                        ],
                        \'Constraints\': {
                            \'EncryptionContextSubset\': {
                                \'string\': \'string\'
                            },
                            \'EncryptionContextEquals\': {
                                \'string\': \'string\'
                            }
                        }
                    },
                ],
                \'NextMarker\': \'string\',
                \'Truncated\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Grants** *(list) --* 
        
              A list of grants.
        
              - *(dict) --* 
        
                Contains information about an entry in a list of grants.
        
                - **KeyId** *(string) --* 
        
                  The unique identifier for the customer master key (CMK) to which the grant applies.
        
                - **GrantId** *(string) --* 
        
                  The unique identifier for the grant.
        
                - **Name** *(string) --* 
        
                  The friendly name that identifies the grant. If a name was provided in the  CreateGrant request, that name is returned. Otherwise this value is null.
        
                - **CreationDate** *(datetime) --* 
        
                  The date and time when the grant was created.
        
                - **GranteePrincipal** *(string) --* 
        
                  The principal that receives the grant\'s permissions.
        
                - **RetiringPrincipal** *(string) --* 
        
                  The principal that can retire the grant.
        
                - **IssuingAccount** *(string) --* 
        
                  The AWS account under which the grant was issued.
        
                - **Operations** *(list) --* 
        
                  The list of operations permitted by the grant.
        
                  - *(string) --* 
              
                - **Constraints** *(dict) --* 
        
                  A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows.
        
                  - **EncryptionContextSubset** *(dict) --* 
        
                    A list of key-value pairs, all of which must be present in the encryption context of certain subsequent operations that the grant allows. When certain subsequent operations allowed by the grant include encryption context that matches this list or is a superset of this list, the grant allows the operation. Otherwise, the grant does not allow the operation.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                  - **EncryptionContextEquals** *(dict) --* 
        
                    A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows. When certain subsequent operations allowed by the grant include encryption context that matches this list, the grant allows the operation. Otherwise, the grant does not allow the operation.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
            - **NextMarker** *(string) --* 
        
              When ``Truncated`` is true, this element is present and contains the value to use for the ``Marker`` parameter in a subsequent request.
        
            - **Truncated** *(boolean) --* 
        
              A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.
        
        """
        pass

    def list_key_policies(self, KeyId: str, Limit: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListKeyPolicies>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_key_policies(
              KeyId=\'string\',
              Limit=123,
              Marker=\'string\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the customer master key (CMK).
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :type Limit: integer
        :param Limit: 
        
          Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
        
          This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.
        
          Currently only 1 policy can be attached to a key.
        
        :type Marker: string
        :param Marker: 
        
          Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextMarker`` from the truncated response you just received.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PolicyNames\': [
                    \'string\',
                ],
                \'NextMarker\': \'string\',
                \'Truncated\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **PolicyNames** *(list) --* 
        
              A list of key policy names. Currently, there is only one key policy per CMK and it is always named ``default`` .
        
              - *(string) --* 
          
            - **NextMarker** *(string) --* 
        
              When ``Truncated`` is true, this element is present and contains the value to use for the ``Marker`` parameter in a subsequent request.
        
            - **Truncated** *(boolean) --* 
        
              A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.
        
        """
        pass

    def list_keys(self, Limit: int = None, Marker: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListKeys>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_keys(
              Limit=123,
              Marker=\'string\'
          )
        :type Limit: integer
        :param Limit: 
        
          Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
        
          This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.
        
        :type Marker: string
        :param Marker: 
        
          Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextMarker`` from the truncated response you just received.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Keys\': [
                    {
                        \'KeyId\': \'string\',
                        \'KeyArn\': \'string\'
                    },
                ],
                \'NextMarker\': \'string\',
                \'Truncated\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Keys** *(list) --* 
        
              A list of customer master keys (CMKs).
        
              - *(dict) --* 
        
                Contains information about each entry in the key list.
        
                - **KeyId** *(string) --* 
        
                  Unique identifier of the key.
        
                - **KeyArn** *(string) --* 
        
                  ARN of the key.
        
            - **NextMarker** *(string) --* 
        
              When ``Truncated`` is true, this element is present and contains the value to use for the ``Marker`` parameter in a subsequent request.
        
            - **Truncated** *(boolean) --* 
        
              A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.
        
        """
        pass

    def list_resource_tags(self, KeyId: str, Limit: int = None, Marker: str = None) -> Dict:
        """
        
        You cannot perform this operation on a CMK in a different AWS account.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListResourceTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_resource_tags(
              KeyId=\'string\',
              Limit=123,
              Marker=\'string\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the customer master key (CMK).
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :type Limit: integer
        :param Limit: 
        
          Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
        
          This value is optional. If you include a value, it must be between 1 and 50, inclusive. If you do not include a value, it defaults to 50.
        
        :type Marker: string
        :param Marker: 
        
          Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextMarker`` from the truncated response you just received.
        
          Do not attempt to construct this value. Use only the value of ``NextMarker`` from the truncated response you just received.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Tags\': [
                    {
                        \'TagKey\': \'string\',
                        \'TagValue\': \'string\'
                    },
                ],
                \'NextMarker\': \'string\',
                \'Truncated\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Tags** *(list) --* 
        
              A list of tags. Each tag consists of a tag key and a tag value.
        
              - *(dict) --* 
        
                A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.
        
                For information about the rules that apply to tag keys and tag values, see `User-Defined Tag Restrictions <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__ in the *AWS Billing and Cost Management User Guide* .
        
                - **TagKey** *(string) --* 
        
                  The key of the tag.
        
                - **TagValue** *(string) --* 
        
                  The value of the tag.
        
            - **NextMarker** *(string) --* 
        
              When ``Truncated`` is true, this element is present and contains the value to use for the ``Marker`` parameter in a subsequent request.
        
              Do not assume or infer any information from this value.
        
            - **Truncated** *(boolean) --* 
        
              A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.
        
        """
        pass

    def list_retirable_grants(self, RetiringPrincipal: str, Limit: int = None, Marker: str = None) -> Dict:
        """
        
        A typical use is to list all grants that you are able to retire. To retire a grant, use  RetireGrant .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListRetirableGrants>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_retirable_grants(
              Limit=123,
              Marker=\'string\',
              RetiringPrincipal=\'string\'
          )
        :type Limit: integer
        :param Limit: 
        
          Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
        
          This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.
        
        :type Marker: string
        :param Marker: 
        
          Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextMarker`` from the truncated response you just received.
        
        :type RetiringPrincipal: string
        :param RetiringPrincipal: **[REQUIRED]** 
        
          The retiring principal for which to list grants.
        
          To specify the retiring principal, use the `Amazon Resource Name (ARN) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, federated users, and assumed role users. For examples of the ARN syntax for specifying a principal, see `AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__ in the Example ARNs section of the *Amazon Web Services General Reference* .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Grants\': [
                    {
                        \'KeyId\': \'string\',
                        \'GrantId\': \'string\',
                        \'Name\': \'string\',
                        \'CreationDate\': datetime(2015, 1, 1),
                        \'GranteePrincipal\': \'string\',
                        \'RetiringPrincipal\': \'string\',
                        \'IssuingAccount\': \'string\',
                        \'Operations\': [
                            \'Decrypt\'|\'Encrypt\'|\'GenerateDataKey\'|\'GenerateDataKeyWithoutPlaintext\'|\'ReEncryptFrom\'|\'ReEncryptTo\'|\'CreateGrant\'|\'RetireGrant\'|\'DescribeKey\',
                        ],
                        \'Constraints\': {
                            \'EncryptionContextSubset\': {
                                \'string\': \'string\'
                            },
                            \'EncryptionContextEquals\': {
                                \'string\': \'string\'
                            }
                        }
                    },
                ],
                \'NextMarker\': \'string\',
                \'Truncated\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Grants** *(list) --* 
        
              A list of grants.
        
              - *(dict) --* 
        
                Contains information about an entry in a list of grants.
        
                - **KeyId** *(string) --* 
        
                  The unique identifier for the customer master key (CMK) to which the grant applies.
        
                - **GrantId** *(string) --* 
        
                  The unique identifier for the grant.
        
                - **Name** *(string) --* 
        
                  The friendly name that identifies the grant. If a name was provided in the  CreateGrant request, that name is returned. Otherwise this value is null.
        
                - **CreationDate** *(datetime) --* 
        
                  The date and time when the grant was created.
        
                - **GranteePrincipal** *(string) --* 
        
                  The principal that receives the grant\'s permissions.
        
                - **RetiringPrincipal** *(string) --* 
        
                  The principal that can retire the grant.
        
                - **IssuingAccount** *(string) --* 
        
                  The AWS account under which the grant was issued.
        
                - **Operations** *(list) --* 
        
                  The list of operations permitted by the grant.
        
                  - *(string) --* 
              
                - **Constraints** *(dict) --* 
        
                  A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows.
        
                  - **EncryptionContextSubset** *(dict) --* 
        
                    A list of key-value pairs, all of which must be present in the encryption context of certain subsequent operations that the grant allows. When certain subsequent operations allowed by the grant include encryption context that matches this list or is a superset of this list, the grant allows the operation. Otherwise, the grant does not allow the operation.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                  - **EncryptionContextEquals** *(dict) --* 
        
                    A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows. When certain subsequent operations allowed by the grant include encryption context that matches this list, the grant allows the operation. Otherwise, the grant does not allow the operation.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
            - **NextMarker** *(string) --* 
        
              When ``Truncated`` is true, this element is present and contains the value to use for the ``Marker`` parameter in a subsequent request.
        
            - **Truncated** *(boolean) --* 
        
              A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.
        
        """
        pass

    def put_key_policy(self, KeyId: str, PolicyName: str, Policy: str, BypassPolicyLockoutSafetyCheck: bool = None) -> NoReturn:
        """
        
        For more information about key policies, see `Key Policies <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/PutKeyPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_key_policy(
              KeyId=\'string\',
              PolicyName=\'string\',
              Policy=\'string\',
              BypassPolicyLockoutSafetyCheck=True|False
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the customer master key (CMK).
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :type PolicyName: string
        :param PolicyName: **[REQUIRED]** 
        
          The name of the key policy. The only valid value is ``default`` .
        
        :type Policy: string
        :param Policy: **[REQUIRED]** 
        
          The key policy to attach to the CMK.
        
          The key policy must meet the following criteria:
        
          * If you don\'t set ``BypassPolicyLockoutSafetyCheck`` to true, the key policy must allow the principal that is making the ``PutKeyPolicy`` request to make a subsequent ``PutKeyPolicy`` request on the CMK. This reduces the risk that the CMK becomes unmanageable. For more information, refer to the scenario in the `Default Key Policy <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`__ section of the *AWS Key Management Service Developer Guide* . 
           
          * Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy. The reason for this is that the new principal might not be immediately visible to AWS KMS. For more information, see `Changes that I make are not always immediately visible <http://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency>`__ in the *AWS Identity and Access Management User Guide* . 
           
          The key policy size limit is 32 kilobytes (32768 bytes).
        
        :type BypassPolicyLockoutSafetyCheck: boolean
        :param BypassPolicyLockoutSafetyCheck: 
        
          A flag to indicate whether to bypass the key policy lockout safety check.
        
          .. warning::
        
            Setting this value to true increases the risk that the CMK becomes unmanageable. Do not set this value to true indiscriminately.
        
            For more information, refer to the scenario in the `Default Key Policy <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`__ section in the *AWS Key Management Service Developer Guide* .
        
          Use this parameter only when you intend to prevent the principal that is making the request from making a subsequent ``PutKeyPolicy`` request on the CMK.
        
          The default value is false.
        
        :returns: None
        """
        pass

    def re_encrypt(self, CiphertextBlob: bytes, DestinationKeyId: str, SourceEncryptionContext: Dict = None, DestinationEncryptionContext: Dict = None, GrantTokens: List = None) -> Dict:
        """
        
        You can reencrypt data using CMKs in different AWS accounts.
        
        Unlike other operations, ``ReEncrypt`` is authorized twice, once as ``ReEncryptFrom`` on the source CMK and once as ``ReEncryptTo`` on the destination CMK. We recommend that you include the ``\"kms:ReEncrypt*\"`` permission in your `key policies <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ to permit reencryption from or to the CMK. This permission is automatically included in the key policy when you create a CMK through the console. But you must include it manually when you create a CMK programmatically or when you set a key policy with the  PutKeyPolicy operation.
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ReEncrypt>`_
        
        **Request Syntax** 
        ::
        
          response = client.re_encrypt(
              CiphertextBlob=b\'bytes\',
              SourceEncryptionContext={
                  \'string\': \'string\'
              },
              DestinationKeyId=\'string\',
              DestinationEncryptionContext={
                  \'string\': \'string\'
              },
              GrantTokens=[
                  \'string\',
              ]
          )
        :type CiphertextBlob: bytes
        :param CiphertextBlob: **[REQUIRED]** 
        
          Ciphertext of the data to reencrypt.
        
        :type SourceEncryptionContext: dict
        :param SourceEncryptionContext: 
        
          Encryption context used to encrypt and decrypt the data specified in the ``CiphertextBlob`` parameter.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type DestinationKeyId: string
        :param DestinationKeyId: **[REQUIRED]** 
        
          A unique identifier for the CMK that is used to reencrypt the data.
        
          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with ``\"alias/\"`` . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Alias name: ``alias/ExampleAlias``   
           
          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .
        
        :type DestinationEncryptionContext: dict
        :param DestinationEncryptionContext: 
        
          Encryption context to use when the data is reencrypted.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type GrantTokens: list
        :param GrantTokens: 
        
          A list of grant tokens.
        
          For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CiphertextBlob\': b\'bytes\',
                \'SourceKeyId\': \'string\',
                \'KeyId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CiphertextBlob** *(bytes) --* 
        
              The reencrypted data. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded.
        
            - **SourceKeyId** *(string) --* 
        
              Unique identifier of the CMK used to originally encrypt the data.
        
            - **KeyId** *(string) --* 
        
              Unique identifier of the CMK used to reencrypt the data.
        
        """
        pass

    def retire_grant(self, GrantToken: str = None, KeyId: str = None, GrantId: str = None) -> NoReturn:
        """
        Retires a grant. To clean up, you can retire a grant when you\'re done using it. You should revoke a grant when you intend to actively deny operations that depend on it. The following are permitted to call this API:
        
        * The AWS account (root user) under which the grant was created 
         
        * The ``RetiringPrincipal`` , if present in the grant 
         
        * The ``GranteePrincipal`` , if ``RetireGrant`` is an operation specified in the grant 
         
        You must identify the grant to retire by its grant token or by a combination of the grant ID and the Amazon Resource Name (ARN) of the customer master key (CMK). A grant token is a unique variable-length base64-encoded string. A grant ID is a 64 character unique identifier of a grant. The  CreateGrant operation returns both.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/RetireGrant>`_
        
        **Request Syntax** 
        ::
        
          response = client.retire_grant(
              GrantToken=\'string\',
              KeyId=\'string\',
              GrantId=\'string\'
          )
        :type GrantToken: string
        :param GrantToken: 
        
          Token that identifies the grant to be retired.
        
        :type KeyId: string
        :param KeyId: 
        
          The Amazon Resource Name (ARN) of the CMK associated with the grant. 
        
          For example: ``arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab``  
        
        :type GrantId: string
        :param GrantId: 
        
          Unique identifier of the grant to retire. The grant ID is returned in the response to a ``CreateGrant`` operation.
        
          * Grant ID Example - 0123456789012345678901234567890123456789012345678901234567890123 
           
        :returns: None
        """
        pass

    def revoke_grant(self, KeyId: str, GrantId: str) -> NoReturn:
        """
        
        To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the ``KeyId`` parameter.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/RevokeGrant>`_
        
        **Request Syntax** 
        ::
        
          response = client.revoke_grant(
              KeyId=\'string\',
              GrantId=\'string\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the customer master key associated with the grant.
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :type GrantId: string
        :param GrantId: **[REQUIRED]** 
        
          Identifier of the grant to be revoked.
        
        :returns: None
        """
        pass

    def schedule_key_deletion(self, KeyId: str, PendingWindowInDays: int = None) -> Dict:
        """
        
        You cannot perform this operation on a CMK in a different AWS account.
        
        .. warning::
        
          Deleting a CMK is a destructive and potentially dangerous operation. When a CMK is deleted, all data that was encrypted under the CMK is rendered unrecoverable. To restrict the use of a CMK without deleting it, use  DisableKey .
        
        For more information about scheduling a CMK for deletion, see `Deleting Customer Master Keys <http://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ScheduleKeyDeletion>`_
        
        **Request Syntax** 
        ::
        
          response = client.schedule_key_deletion(
              KeyId=\'string\',
              PendingWindowInDays=123
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          The unique identifier of the customer master key (CMK) to delete.
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :type PendingWindowInDays: integer
        :param PendingWindowInDays: 
        
          The waiting period, specified in number of days. After the waiting period ends, AWS KMS deletes the customer master key (CMK).
        
          This value is optional. If you include a value, it must be between 7 and 30, inclusive. If you do not include a value, it defaults to 30.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'KeyId\': \'string\',
                \'DeletionDate\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **KeyId** *(string) --* 
        
              The unique identifier of the customer master key (CMK) for which deletion is scheduled.
        
            - **DeletionDate** *(datetime) --* 
        
              The date and time after which AWS KMS deletes the customer master key (CMK).
        
        """
        pass

    def tag_resource(self, KeyId: str, Tags: List) -> NoReturn:
        """
        
        Each tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.
        
        You can only use a tag key once for each CMK. If you use the tag key again, AWS KMS replaces the current tag value with the specified value.
        
        For information about the rules that apply to tag keys and tag values, see `User-Defined Tag Restrictions <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__ in the *AWS Billing and Cost Management User Guide* .
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/TagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.tag_resource(
              KeyId=\'string\',
              Tags=[
                  {
                      \'TagKey\': \'string\',
                      \'TagValue\': \'string\'
                  },
              ]
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the CMK you are tagging.
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          One or more tags. Each tag consists of a tag key and a tag value.
        
          - *(dict) --* 
        
            A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.
        
            For information about the rules that apply to tag keys and tag values, see `User-Defined Tag Restrictions <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__ in the *AWS Billing and Cost Management User Guide* .
        
            - **TagKey** *(string) --* **[REQUIRED]** 
        
              The key of the tag.
        
            - **TagValue** *(string) --* **[REQUIRED]** 
        
              The value of the tag.
        
        :returns: None
        """
        pass

    def untag_resource(self, KeyId: str, TagKeys: List) -> NoReturn:
        """
        
        To remove a tag, specify the tag key. To change the tag value of an existing tag key, use  TagResource .
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UntagResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.untag_resource(
              KeyId=\'string\',
              TagKeys=[
                  \'string\',
              ]
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the CMK from which you are removing tags.
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          One or more tag keys. Specify only the tag keys, not the tag values.
        
          - *(string) --* 
        
        :returns: None
        """
        pass

    def update_alias(self, AliasName: str, TargetKeyId: str) -> NoReturn:
        """
        
        This operation works only on existing aliases. To change the alias of a CMK to a new value, use  CreateAlias to create a new alias and  DeleteAlias to delete the old alias.
        
        Because an alias is not a property of a CMK, you can create, update, and delete the aliases of a CMK without affecting the CMK. Also, aliases do not appear in the response from the  DescribeKey operation. To get the aliases of all CMKs in the account, use the  ListAliases operation. 
        
        An alias name can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). An alias must start with the word ``alias`` followed by a forward slash (``alias/`` ). The alias name can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). Alias names cannot begin with ``aws`` ; that alias name prefix is reserved by Amazon Web Services (AWS).
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UpdateAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_alias(
              AliasName=\'string\',
              TargetKeyId=\'string\'
          )
        :type AliasName: string
        :param AliasName: **[REQUIRED]** 
        
          String that contains the name of the alias to be modified. The name must start with the word \"alias\" followed by a forward slash (alias/). Aliases that begin with \"alias/aws\" are reserved.
        
        :type TargetKeyId: string
        :param TargetKeyId: **[REQUIRED]** 
        
          Unique identifier of the customer master key to be mapped to the alias.
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
          To verify that the alias is mapped to the correct CMK, use  ListAliases .
        
        :returns: None
        """
        pass

    def update_key_description(self, KeyId: str, Description: str) -> NoReturn:
        """
        
        You cannot perform this operation on a CMK in a different AWS account.
        
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UpdateKeyDescription>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_key_description(
              KeyId=\'string\',
              Description=\'string\'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]** 
        
          A unique identifier for the customer master key (CMK).
        
          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
        
          For example:
        
          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
           
          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
        
        :type Description: string
        :param Description: **[REQUIRED]** 
        
          New description for the CMK.
        
        :returns: None
        """
        pass
