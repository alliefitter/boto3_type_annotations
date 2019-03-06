from typing import Union
from typing import List
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Optional
from typing import Dict
from datetime import datetime
from botocore.client import BaseClient


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

    def cancel_key_deletion(self, KeyId: str) -> Dict:
        """
        Cancels the deletion of a customer master key (CMK). When this operation is successful, the CMK is set to the ``Disabled`` state. To enable a CMK, use  EnableKey . You cannot perform this operation on a CMK in a different AWS account.
        For more information about scheduling and canceling deletion of a CMK, see `Deleting Customer Master Keys <http://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html>`__ in the *AWS Key Management Service Developer Guide* .
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CancelKeyDeletion>`_
        
        **Request Syntax**
        ::
          response = client.cancel_key_deletion(
              KeyId='string'
          )
        
        **Response Syntax**
        ::
            {
                'KeyId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **KeyId** *(string) --* 
              The unique identifier of the master key for which deletion is canceled.
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
        """
        pass

    def connect_custom_key_store(self, CustomKeyStoreId: str) -> Dict:
        """
        Connects or reconnects a `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ to its associated AWS CloudHSM cluster.
        The custom key store must be connected before you can create customer master keys (CMKs) in the key store or use the CMKs it contains. You can disconnect and reconnect a custom key store at any time.
        To connect a custom key store, its associated AWS CloudHSM cluster must have at least one active HSM. To get the number of active HSMs in a cluster, use the `DescribeClusters <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters>`__ operation. To add HSMs to the cluster, use the `CreateHsm <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CreateHsm>`__ operation.
        The connection process can take an extended amount of time to complete; up to 20 minutes. This operation starts the connection process, but it does not wait for it to complete. When it succeeds, this operation quickly returns an HTTP 200 response and a JSON object with no properties. However, this response does not indicate that the custom key store is connected. To get the connection state of the custom key store, use the  DescribeCustomKeyStores operation.
        During the connection process, AWS KMS finds the AWS CloudHSM cluster that is associated with the custom key store, creates the connection infrastructure, connects to the cluster, logs into the AWS CloudHSM client as the ` ``kmsuser`` crypto user <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser>`__ (CU), and rotates its password.
        The ``ConnectCustomKeyStore`` operation might fail for various reasons. To find the reason, use the  DescribeCustomKeyStores operation and see the ``ConnectionErrorCode`` in the response. For help interpreting the ``ConnectionErrorCode`` , see  CustomKeyStoresListEntry .
        To fix the failure, use the  DisconnectCustomKeyStore operation to disconnect the custom key store, correct the error, use the  UpdateCustomKeyStore operation if necessary, and then use ``ConnectCustomKeyStore`` again.
        If you are having trouble connecting or disconnecting a custom key store, see `Troubleshooting a Custom Key Store <http://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ConnectCustomKeyStore>`_
        
        **Request Syntax**
        ::
          response = client.connect_custom_key_store(
              CustomKeyStoreId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type CustomKeyStoreId: string
        :param CustomKeyStoreId: **[REQUIRED]**
          Enter the key store ID of the custom key store that you want to connect. To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.
        :rtype: dict
        :returns:
        """
        pass

    def create_alias(self, AliasName: str, TargetKeyId: str):
        """
        Creates a display name for a customer master key (CMK). You can use an alias to identify a CMK in selected operations, such as  Encrypt and  GenerateDataKey . 
        Each CMK can have multiple aliases, but each alias points to only one CMK. The alias name must be unique in the AWS account and region. To simplify code that runs in multiple regions, use the same alias name, but point it to a different CMK in each region. 
        Because an alias is not a property of a CMK, you can delete and change the aliases of a CMK without affecting the CMK. Also, aliases do not appear in the response from the  DescribeKey operation. To get the aliases of all CMKs, use the  ListAliases operation.
        An alias must start with the word ``alias`` followed by a forward slash (``alias/`` ). The alias name can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). Alias names cannot begin with ``aws`` ; that alias name prefix is reserved by Amazon Web Services (AWS).
        The alias and the CMK it is mapped to must be in the same AWS account and the same region. You cannot perform this operation on an alias in a different AWS account.
        To map an existing alias to a different CMK, call  UpdateAlias .
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateAlias>`_
        
        **Request Syntax**
        ::
          response = client.create_alias(
              AliasName='string',
              TargetKeyId='string'
          )
        :type AliasName: string
        :param AliasName: **[REQUIRED]**
          String that contains the display name. The name must start with the word \"alias\" followed by a forward slash (alias/). Aliases that begin with \"alias/AWS\" are reserved.
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

    def create_custom_key_store(self, CustomKeyStoreName: str, CloudHsmClusterId: str, TrustAnchorCertificate: str, KeyStorePassword: str) -> Dict:
        """
        .. _http://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser: http://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser
        Creates a `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ that is associated with an `AWS CloudHSM cluster <http://docs.aws.amazon.com/cloudhsm/latest/userguide/clusters.html>`__ that you own and manage.
        This operation is part of the `Custom Key Store feature <http://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a single-tenant key store.
        When the operation completes successfully, it returns the ID of the new custom key store. Before you can use your new custom key store, you need to use the  ConnectCustomKeyStore operation to connect the new key store to its AWS CloudHSM cluster.
        The ``CreateCustomKeyStore`` operation requires the following elements.
        * You must specify an active AWS CloudHSM cluster in the same account and AWS Region as the custom key store. You can use an existing cluster or `create and activate a new AWS CloudHSM cluster <http://docs.aws.amazon.com/cloudhsm/latest/userguide/create-cluster.html>`__ for the key store. AWS KMS does not require exclusive use of the cluster. 
        * You must include the content of the *trust anchor certificate* for the cluster. You created this certificate, and saved it in the ``customerCA.crt`` file, when you `initialized the cluster <http://docs.aws.amazon.com/cloudhsm/latest/userguide/initialize-cluster.html#sign-csr>`__ . 
        * You must provide the password of the dedicated ` ``kmsuser`` crypto user <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser>`__ (CU) account in the cluster. Before you create the custom key store, use the `createUser <http://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-createUser.html>`__ command in ``cloudhsm_mgmt_util`` to create `a crypto user (CU) named ``kmsuser`` http://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser`__ in specified AWS CloudHSM cluster. AWS KMS uses the ``kmsuser`` CU account to create and manage key material on your behalf. For instructions, see `Create the kmsuser Crypto User <http://docs.aws.amazon.com/kms/latest/developerguide/create-keystore.html#before-keystore>`__ in the *AWS Key Management Service Developer Guide* . 
        The AWS CloudHSM cluster that you specify must meet the following requirements.
        * The cluster must be active and be in the same AWS account and Region as the custom key store. 
        * Each custom key store must be associated with a different AWS CloudHSM cluster. The cluster cannot be associated with another custom key store or have the same cluster certificate as a cluster that is associated with another custom key store. To view the cluster certificate, use the AWS CloudHSM `DescribeClusters <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html>`__ operation. Clusters that share a backup history have the same cluster certificate. 
        * The cluster must be configured with subnets in at least two different Availability Zones in the Region. Because AWS CloudHSM is not supported in all Availability Zones, we recommend that the cluster have subnets in all Availability Zones in the Region. 
        * The cluster must contain at least two active HSMs, each in a different Availability Zone. 
        New custom key stores are not automatically connected. After you create your custom key store, use the  ConnectCustomKeyStore operation to connect the custom key store to its associated AWS CloudHSM cluster. Even if you are not going to use your custom key store immediately, you might want to connect it to verify that all settings are correct and then disconnect it until you are ready to use it.
        If this operation succeeds, it returns the ID of the new custom key store. For help with failures, see `Troubleshoot a Custom Key Store <http://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html>`__ in the *AWS KMS Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateCustomKeyStore>`_
        
        **Request Syntax**
        ::
          response = client.create_custom_key_store(
              CustomKeyStoreName='string',
              CloudHsmClusterId='string',
              TrustAnchorCertificate='string',
              KeyStorePassword='string'
          )
        
        **Response Syntax**
        ::
            {
                'CustomKeyStoreId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CustomKeyStoreId** *(string) --* 
              A unique identifier for the new custom key store.
        :type CustomKeyStoreName: string
        :param CustomKeyStoreName: **[REQUIRED]**
          Specifies a friendly name for the custom key store. The name must be unique in your AWS account.
        :type CloudHsmClusterId: string
        :param CloudHsmClusterId: **[REQUIRED]**
          Identifies the AWS CloudHSM cluster for the custom key store. Enter the cluster ID of any active AWS CloudHSM cluster that is not already associated with a custom key store. To find the cluster ID, use the `DescribeClusters <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html>`__ operation.
        :type TrustAnchorCertificate: string
        :param TrustAnchorCertificate: **[REQUIRED]**
          Enter the content of the trust anchor certificate for the cluster. This is the content of the ``customerCA.crt`` file that you created when you `initialized the cluster <http://docs.aws.amazon.com/cloudhsm/latest/userguide/initialize-cluster.html>`__ .
        :type KeyStorePassword: string
        :param KeyStorePassword: **[REQUIRED]**
          Enter the password of the ` ``kmsuser`` crypto user (CU) account <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser>`__ in the specified AWS CloudHSM cluster. AWS KMS logs into the cluster as this user to manage key material on your behalf.
          This parameter tells AWS KMS the ``kmsuser`` account password; it does not change the password in the AWS CloudHSM cluster.
        :rtype: dict
        :returns:
        """
        pass

    def create_grant(self, KeyId: str, GranteePrincipal: str, Operations: List, RetiringPrincipal: str = None, Constraints: Dict = None, GrantTokens: List = None, Name: str = None) -> Dict:
        """
        Adds a grant to a customer master key (CMK). The grant specifies who can use the CMK and under what conditions. When setting permissions, grants are an alternative to key policies. 
        To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the ``KeyId`` parameter. For more information about grants, see `Grants <http://docs.aws.amazon.com/kms/latest/developerguide/grants.html>`__ in the *AWS Key Management Service Developer Guide* .
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateGrant>`_
        
        **Request Syntax**
        ::
          response = client.create_grant(
              KeyId='string',
              GranteePrincipal='string',
              RetiringPrincipal='string',
              Operations=[
                  'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'CreateGrant'|'RetireGrant'|'DescribeKey',
              ],
              Constraints={
                  'EncryptionContextSubset': {
                      'string': 'string'
                  },
                  'EncryptionContextEquals': {
                      'string': 'string'
                  }
              },
              GrantTokens=[
                  'string',
              ],
              Name='string'
          )
        
        **Response Syntax**
        ::
            {
                'GrantToken': 'string',
                'GrantId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **GrantToken** *(string) --* 
              The grant token.
              For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .
            - **GrantId** *(string) --* 
              The unique identifier for the grant.
              You can use the ``GrantId`` in a subsequent  RetireGrant or  RevokeGrant operation.
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
          A friendly name for identifying the grant. Use this value to prevent unintended creation of duplicate grants when retrying this request.
          When this value is absent, all ``CreateGrant`` requests result in a new grant with a unique ``GrantId`` even if all the supplied parameters are identical. This can result in unintended duplicates when you retry the ``CreateGrant`` request.
          When this value is present, you can retry a ``CreateGrant`` request with identical parameters; if the grant already exists, the original ``GrantId`` is returned without creating a new grant. Note that the returned grant token is unique with every ``CreateGrant`` request, even when a duplicate ``GrantId`` is returned. All grant tokens obtained in this way can be used interchangeably.
        :rtype: dict
        :returns:
        """
        pass

    def create_key(self, Policy: str = None, Description: str = None, KeyUsage: str = None, Origin: str = None, CustomKeyStoreId: str = None, BypassPolicyLockoutSafetyCheck: bool = None, Tags: List = None) -> Dict:
        """
        Creates a customer master key (CMK) in the caller's AWS account.
        You can use a CMK to encrypt small amounts of data (4 KiB or less) directly, but CMKs are more commonly used to encrypt data keys, which are used to encrypt raw data. For more information about data keys and the difference between CMKs and data keys, see the following:
        * The  GenerateDataKey operation 
        * `AWS Key Management Service Concepts <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ in the *AWS Key Management Service Developer Guide*   
        If you plan to `import key material <http://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ , use the ``Origin`` parameter with a value of ``EXTERNAL`` to create a CMK with no key material.
        To create a CMK in a `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ , use ``CustomKeyStoreId`` parameter to specify the custom key store. You must also use the ``Origin`` parameter with a value of ``AWS_CLOUDHSM`` . The AWS CloudHSM cluster that is associated with the custom key store must have at least two active HSMs, each in a different Availability Zone in the Region.
        You cannot use this operation to create a CMK in a different AWS account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateKey>`_
        
        **Request Syntax**
        ::
          response = client.create_key(
              Policy='string',
              Description='string',
              KeyUsage='ENCRYPT_DECRYPT',
              Origin='AWS_KMS'|'EXTERNAL'|'AWS_CLOUDHSM',
              CustomKeyStoreId='string',
              BypassPolicyLockoutSafetyCheck=True|False,
              Tags=[
                  {
                      'TagKey': 'string',
                      'TagValue': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'KeyMetadata': {
                    'AWSAccountId': 'string',
                    'KeyId': 'string',
                    'Arn': 'string',
                    'CreationDate': datetime(2015, 1, 1),
                    'Enabled': True|False,
                    'Description': 'string',
                    'KeyUsage': 'ENCRYPT_DECRYPT',
                    'KeyState': 'Enabled'|'Disabled'|'PendingDeletion'|'PendingImport'|'Unavailable',
                    'DeletionDate': datetime(2015, 1, 1),
                    'ValidTo': datetime(2015, 1, 1),
                    'Origin': 'AWS_KMS'|'EXTERNAL'|'AWS_CLOUDHSM',
                    'CustomKeyStoreId': 'string',
                    'CloudHsmClusterId': 'string',
                    'ExpirationModel': 'KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE',
                    'KeyManager': 'AWS'|'CUSTOMER'
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
                The date and time after which AWS KMS deletes the CMK. This value is present only when ``KeyState`` is ``PendingDeletion`` .
              - **ValidTo** *(datetime) --* 
                The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. This value is present only for CMKs whose ``Origin`` is ``EXTERNAL`` and whose ``ExpirationModel`` is ``KEY_MATERIAL_EXPIRES`` , otherwise this value is omitted.
              - **Origin** *(string) --* 
                The source of the CMK's key material. When this value is ``AWS_KMS`` , AWS KMS created the key material. When this value is ``EXTERNAL`` , the key material was imported from your existing key management infrastructure or the CMK lacks key material. When this value is ``AWS_CLOUDHSM`` , the key material was created in the AWS CloudHSM cluster associated with a custom key store.
              - **CustomKeyStoreId** *(string) --* 
                A unique identifier for the `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ that contains the CMK. This value is present only when the CMK is created in a custom key store.
              - **CloudHsmClusterId** *(string) --* 
                The cluster ID of the AWS CloudHSM cluster that contains the key material for the CMK. When you create a CMK in a `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ , AWS KMS creates the key material for the CMK in the associated AWS CloudHSM cluster. This value is present only when the CMK is created in a custom key store.
              - **ExpirationModel** *(string) --* 
                Specifies whether the CMK's key material expires. This value is present only when ``Origin`` is ``EXTERNAL`` , otherwise this value is omitted.
              - **KeyManager** *(string) --* 
                The CMK's manager. CMKs are either customer-managed or AWS-managed. For more information about the difference, see `Customer Master Keys <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ in the *AWS Key Management Service Developer Guide* .
        :type Policy: string
        :param Policy:
          The key policy to attach to the CMK.
          If you provide a key policy, it must meet the following criteria:
          * If you don\'t set ``BypassPolicyLockoutSafetyCheck`` to true, the key policy must allow the principal that is making the ``CreateKey`` request to make a subsequent  PutKeyPolicy request on the CMK. This reduces the risk that the CMK becomes unmanageable. For more information, refer to the scenario in the `Default Key Policy <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`__ section of the *AWS Key Management Service Developer Guide* .
          * Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to AWS KMS. For more information, see `Changes that I make are not always immediately visible <http://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency>`__ in the *AWS Identity and Access Management User Guide* .
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
          The source of the CMK\'s key material. You cannot change the origin after you create the CMK.
          The default is ``AWS_KMS`` , which means AWS KMS creates the key material in its own key store.
          When the parameter value is ``EXTERNAL`` , AWS KMS creates a CMK without key material so that you can import key material from your existing key management infrastructure. For more information about importing key material into AWS KMS, see `Importing Key Material <http://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ in the *AWS Key Management Service Developer Guide* .
          When the parameter value is ``AWS_CLOUDHSM`` , AWS KMS creates the CMK in a AWS KMS `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ and creates its key material in the associated AWS CloudHSM cluster. You must also use the ``CustomKeyStoreId`` parameter to identify the custom key store.
        :type CustomKeyStoreId: string
        :param CustomKeyStoreId:
          Creates the CMK in the specified `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ and the key material in its associated AWS CloudHSM cluster. To create a CMK in a custom key store, you must also specify the ``Origin`` parameter with a value of ``AWS_CLOUDHSM`` . The AWS CloudHSM cluster that is associated with the custom key store must have at least two active HSMs, each in a different Availability Zone in the Region.
          To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.
          The response includes the custom key store ID and the ID of the AWS CloudHSM cluster.
          This operation is part of the `Custom Key Store feature <http://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a single-tenant key store.
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
        """
        pass

    def decrypt(self, CiphertextBlob: bytes, EncryptionContext: Dict = None, GrantTokens: List = None) -> Dict:
        """
        Decrypts ciphertext. Ciphertext is plaintext that has been previously encrypted by using any of the following operations:
        *  GenerateDataKey   
        *  GenerateDataKeyWithoutPlaintext   
        *  Encrypt   
        Note that if a caller has been granted access permissions to all keys (through, for example, IAM user policies that grant ``Decrypt`` permission on all resources), then ciphertext encrypted by using keys in other accounts where the key grants access to the caller can be decrypted. To remedy this, we recommend that you do not grant ``Decrypt`` access in an IAM user policy. Instead grant ``Decrypt`` access only in key policies. If you must grant ``Decrypt`` access in an IAM user policy, you should scope the resource to specific keys or to specific trusted accounts.
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/Decrypt>`_
        
        **Request Syntax**
        ::
          response = client.decrypt(
              CiphertextBlob=b'bytes',
              EncryptionContext={
                  'string': 'string'
              },
              GrantTokens=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'KeyId': 'string',
                'Plaintext': b'bytes'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **KeyId** *(string) --* 
              ARN of the key used to perform the decryption. This value is returned if no errors are encountered during the operation.
            - **Plaintext** *(bytes) --* 
              Decrypted plaintext data. When you use the HTTP API or the AWS CLI, the value is Base64-encdoded. Otherwise, it is not encoded.
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
        """
        pass

    def delete_alias(self, AliasName: str):
        """
        Deletes the specified alias. You cannot perform this operation on an alias in a different AWS account. 
        Because an alias is not a property of a CMK, you can delete and change the aliases of a CMK without affecting the CMK. Also, aliases do not appear in the response from the  DescribeKey operation. To get the aliases of all CMKs, use the  ListAliases operation. 
        Each CMK can have multiple aliases. To change the alias of a CMK, use  DeleteAlias to delete the current alias and  CreateAlias to create a new alias. To associate an existing alias with a different customer master key (CMK), call  UpdateAlias .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DeleteAlias>`_
        
        **Request Syntax**
        ::
          response = client.delete_alias(
              AliasName='string'
          )
        :type AliasName: string
        :param AliasName: **[REQUIRED]**
          The alias to be deleted. The name must start with the word \"alias\" followed by a forward slash (alias/). Aliases that begin with \"alias/aws\" are reserved.
        :returns: None
        """
        pass

    def delete_custom_key_store(self, CustomKeyStoreId: str) -> Dict:
        """
        Deletes a `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ . This operation does not delete the AWS CloudHSM cluster that is associated with the custom key store, or affect any users or keys in the cluster.
        The custom key store that you delete cannot contain any AWS KMS `customer master keys (CMKs) <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ . Before deleting the key store, verify that you will never need to use any of the CMKs in the key store for any cryptographic operations. Then, use  ScheduleKeyDeletion to delete the AWS KMS customer master keys (CMKs) from the key store. When the scheduled waiting period expires, the ``ScheduleKeyDeletion`` operation deletes the CMKs. Then it makes a best effort to delete the key material from the associated cluster. However, you might need to manually `delete the orphaned key material <http://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html#fix-keystore-orphaned-key>`__ from the cluster and its backups.
        After all CMKs are deleted from AWS KMS, use  DisconnectCustomKeyStore to disconnect the key store from AWS KMS. Then, you can delete the custom key store.
        Instead of deleting the custom key store, consider using  DisconnectCustomKeyStore to disconnect it from AWS KMS. While the key store is disconnected, you cannot create or use the CMKs in the key store. But, you do not need to delete CMKs and you can reconnect a disconnected custom key store at any time.
        If the operation succeeds, it returns a JSON object with no properties.
        This operation is part of the `Custom Key Store feature <http://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a single-tenant key store.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DeleteCustomKeyStore>`_
        
        **Request Syntax**
        ::
          response = client.delete_custom_key_store(
              CustomKeyStoreId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type CustomKeyStoreId: string
        :param CustomKeyStoreId: **[REQUIRED]**
          Enter the ID of the custom key store you want to delete. To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.
        :rtype: dict
        :returns:
        """
        pass

    def delete_imported_key_material(self, KeyId: str):
        """
        Deletes key material that you previously imported. This operation makes the specified customer master key (CMK) unusable. For more information about importing key material into AWS KMS, see `Importing Key Material <http://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ in the *AWS Key Management Service Developer Guide* . You cannot perform this operation on a CMK in a different AWS account.
        When the specified CMK is in the ``PendingDeletion`` state, this operation does not change the CMK's state. Otherwise, it changes the CMK's state to ``PendingImport`` .
        After you delete key material, you can use  ImportKeyMaterial to reimport the same key material into the CMK.
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DeleteImportedKeyMaterial>`_
        
        **Request Syntax**
        ::
          response = client.delete_imported_key_material(
              KeyId='string'
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

    def describe_custom_key_stores(self, CustomKeyStoreId: str = None, CustomKeyStoreName: str = None, Limit: int = None, Marker: str = None) -> Dict:
        """
        Gets information about `custom key stores <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ in the account and region.
        This operation is part of the `Custom Key Store feature <http://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a single-tenant key store.
        By default, this operation returns information about all custom key stores in the account and region. To get only information about a particular custom key store, use either the ``CustomKeyStoreName`` or ``CustomKeyStoreId`` parameter (but not both).
        To determine whether the custom key store is connected to its AWS CloudHSM cluster, use the ``ConnectionState`` element in the response. If an attempt to connect the custom key store failed, the ``ConnectionState`` value is ``FAILED`` and the ``ConnectionErrorCode`` element in the response indicates the cause of the failure. For help interpreting the ``ConnectionErrorCode`` , see  CustomKeyStoresListEntry .
        Custom key stores have a ``DISCONNECTED`` connection state if the key store has never been connected or you use the  DisconnectCustomKeyStore operation to disconnect it. If your custom key store state is ``CONNECTED`` but you are having trouble using it, make sure that its associated AWS CloudHSM cluster is active and contains the minimum number of HSMs required for the operation, if any.
        For help repairing your custom key store, see the `Troubleshooting Custom Key Stores <http://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore-html>`__ topic in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DescribeCustomKeyStores>`_
        
        **Request Syntax**
        ::
          response = client.describe_custom_key_stores(
              CustomKeyStoreId='string',
              CustomKeyStoreName='string',
              Limit=123,
              Marker='string'
          )
        
        **Response Syntax**
        ::
            {
                'CustomKeyStores': [
                    {
                        'CustomKeyStoreId': 'string',
                        'CustomKeyStoreName': 'string',
                        'CloudHsmClusterId': 'string',
                        'TrustAnchorCertificate': 'string',
                        'ConnectionState': 'CONNECTED'|'CONNECTING'|'FAILED'|'DISCONNECTED'|'DISCONNECTING',
                        'ConnectionErrorCode': 'INVALID_CREDENTIALS'|'CLUSTER_NOT_FOUND'|'NETWORK_ERRORS'|'INSUFFICIENT_CLOUDHSM_HSMS'|'USER_LOCKED_OUT',
                        'CreationDate': datetime(2015, 1, 1)
                    },
                ],
                'NextMarker': 'string',
                'Truncated': True|False
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CustomKeyStores** *(list) --* 
              Contains metadata about each custom key store.
              - *(dict) --* 
                Contains information about each custom key store in the custom key store list.
                - **CustomKeyStoreId** *(string) --* 
                  A unique identifier for the custom key store.
                - **CustomKeyStoreName** *(string) --* 
                  The user-specified friendly name for the custom key store.
                - **CloudHsmClusterId** *(string) --* 
                  A unique identifier for the AWS CloudHSM cluster that is associated with the custom key store.
                - **TrustAnchorCertificate** *(string) --* 
                  The trust anchor certificate of the associated AWS CloudHSM cluster. When you `initialize the cluster <http://docs.aws.amazon.com/cloudhsm/latest/userguide/initialize-cluster.html#sign-csr>`__ , you create this certificate and save it in the ``customerCA.crt`` file.
                - **ConnectionState** *(string) --* 
                  Indicates whether the custom key store is connected to its AWS CloudHSM cluster.
                  You can create and use CMKs in your custom key stores only when its connection state is ``CONNECTED`` .
                  The value is ``DISCONNECTED`` if the key store has never been connected or you use the  DisconnectCustomKeyStore operation to disconnect it. If the value is ``CONNECTED`` but you are having trouble using the custom key store, make sure that its associated AWS CloudHSM cluster is active and contains at least one active HSM.
                  A value of ``FAILED`` indicates that an attempt to connect was unsuccessful. For help resolving a connection failure, see `Troubleshooting a Custom Key Store <http://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html>`__ in the *AWS Key Management Service Developer Guide* .
                - **ConnectionErrorCode** *(string) --* 
                  Describes the connection error. Valid values are:
                  * ``CLUSTER_NOT_FOUND`` - AWS KMS cannot find the AWS CloudHSM cluster with the specified cluster ID. 
                  * ``INSUFFICIENT_CLOUDHSM_HSMS`` - The associated AWS CloudHSM cluster does not contain any active HSMs. To connect a custom key store to its AWS CloudHSM cluster, the cluster must contain at least one active HSM. 
                  * ``INVALID_CREDENTIALS`` - AWS KMS does not have the correct password for the ``kmsuser`` crypto user in the AWS CloudHSM cluster. 
                  * ``NETWORK_ERRORS`` - Network errors are preventing AWS KMS from connecting to the custom key store. 
                  * ``USER_LOCKED_OUT`` - The ``kmsuser`` CU account is locked out of the associated AWS CloudHSM cluster due to too many failed password attempts. Before you can connect your custom key store to its AWS CloudHSM cluster, you must change the ``kmsuser`` account password and update the password value for the custom key store. 
                  For help with connection failures, see `Troubleshooting Custom Key Stores <http://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html>`__ in the *AWS Key Management Service Developer Guide* .
                - **CreationDate** *(datetime) --* 
                  The date and time when the custom key store was created.
            - **NextMarker** *(string) --* 
              When ``Truncated`` is true, this element is present and contains the value to use for the ``Marker`` parameter in a subsequent request.
            - **Truncated** *(boolean) --* 
              A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.
        :type CustomKeyStoreId: string
        :param CustomKeyStoreId:
          Gets only information about the specified custom key store. Enter the key store ID.
          By default, this operation gets information about all custom key stores in the account and region. To limit the output to a particular custom key store, you can use either the ``CustomKeyStoreId`` or ``CustomKeyStoreName`` parameter, but not both.
        :type CustomKeyStoreName: string
        :param CustomKeyStoreName:
          Gets only information about the specified custom key store. Enter the friendly name of the custom key store.
          By default, this operation gets information about all custom key stores in the account and region. To limit the output to a particular custom key store, you can use either the ``CustomKeyStoreId`` or ``CustomKeyStoreName`` parameter, but not both.
        :type Limit: integer
        :param Limit:
          Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
        :type Marker: string
        :param Marker:
          Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextMarker`` from the truncated response you just received.
        :rtype: dict
        :returns:
        """
        pass

    def describe_key(self, KeyId: str, GrantTokens: List = None) -> Dict:
        """
        Provides detailed information about the specified customer master key (CMK).
        If you use ``DescribeKey`` on a predefined AWS alias, that is, an AWS alias with no key ID, AWS KMS associates the alias with an `AWS managed CMK <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ and returns its ``KeyId`` and ``Arn`` in the response.
        To perform this operation on a CMK in a different AWS account, specify the key ARN or alias ARN in the value of the KeyId parameter.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DescribeKey>`_
        
        **Request Syntax**
        ::
          response = client.describe_key(
              KeyId='string',
              GrantTokens=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'KeyMetadata': {
                    'AWSAccountId': 'string',
                    'KeyId': 'string',
                    'Arn': 'string',
                    'CreationDate': datetime(2015, 1, 1),
                    'Enabled': True|False,
                    'Description': 'string',
                    'KeyUsage': 'ENCRYPT_DECRYPT',
                    'KeyState': 'Enabled'|'Disabled'|'PendingDeletion'|'PendingImport'|'Unavailable',
                    'DeletionDate': datetime(2015, 1, 1),
                    'ValidTo': datetime(2015, 1, 1),
                    'Origin': 'AWS_KMS'|'EXTERNAL'|'AWS_CLOUDHSM',
                    'CustomKeyStoreId': 'string',
                    'CloudHsmClusterId': 'string',
                    'ExpirationModel': 'KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE',
                    'KeyManager': 'AWS'|'CUSTOMER'
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
                The date and time after which AWS KMS deletes the CMK. This value is present only when ``KeyState`` is ``PendingDeletion`` .
              - **ValidTo** *(datetime) --* 
                The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. This value is present only for CMKs whose ``Origin`` is ``EXTERNAL`` and whose ``ExpirationModel`` is ``KEY_MATERIAL_EXPIRES`` , otherwise this value is omitted.
              - **Origin** *(string) --* 
                The source of the CMK's key material. When this value is ``AWS_KMS`` , AWS KMS created the key material. When this value is ``EXTERNAL`` , the key material was imported from your existing key management infrastructure or the CMK lacks key material. When this value is ``AWS_CLOUDHSM`` , the key material was created in the AWS CloudHSM cluster associated with a custom key store.
              - **CustomKeyStoreId** *(string) --* 
                A unique identifier for the `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ that contains the CMK. This value is present only when the CMK is created in a custom key store.
              - **CloudHsmClusterId** *(string) --* 
                The cluster ID of the AWS CloudHSM cluster that contains the key material for the CMK. When you create a CMK in a `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ , AWS KMS creates the key material for the CMK in the associated AWS CloudHSM cluster. This value is present only when the CMK is created in a custom key store.
              - **ExpirationModel** *(string) --* 
                Specifies whether the CMK's key material expires. This value is present only when ``Origin`` is ``EXTERNAL`` , otherwise this value is omitted.
              - **KeyManager** *(string) --* 
                The CMK's manager. CMKs are either customer-managed or AWS-managed. For more information about the difference, see `Customer Master Keys <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ in the *AWS Key Management Service Developer Guide* .
        :type KeyId: string
        :param KeyId: **[REQUIRED]**
          Describes the specified customer master key (CMK).
          If you specify a predefined AWS alias (an AWS alias with no key ID), KMS associates the alias with an `AWS managed CMK <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ and returns its ``KeyId`` and ``Arn`` in the response.
          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with \"alias/\". To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.
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
        """
        pass

    def disable_key(self, KeyId: str):
        """
        Sets the state of a customer master key (CMK) to disabled, thereby preventing its use for cryptographic operations. You cannot perform this operation on a CMK in a different AWS account.
        For more information about how key state affects the use of a CMK, see `How Key State Affects the Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DisableKey>`_
        
        **Request Syntax**
        ::
          response = client.disable_key(
              KeyId='string'
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

    def disable_key_rotation(self, KeyId: str):
        """
        Disables `automatic rotation of the key material <http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`__ for the specified customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DisableKeyRotation>`_
        
        **Request Syntax**
        ::
          response = client.disable_key_rotation(
              KeyId='string'
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

    def disconnect_custom_key_store(self, CustomKeyStoreId: str) -> Dict:
        """
        Disconnects the `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ from its associated AWS CloudHSM cluster. While a custom key store is disconnected, you can manage the custom key store and its customer master keys (CMKs), but you cannot create or use CMKs in the custom key store. You can reconnect the custom key store at any time.
        .. note::
          While a custom key store is disconnected, all attempts to create customer master keys (CMKs) in the custom key store or to use existing CMKs in cryptographic operations will fail. This action can prevent users from storing and accessing sensitive data.
        To find the connection state of a custom key store, use the  DescribeCustomKeyStores operation. To reconnect a custom key store, use the  ConnectCustomKeyStore operation.
        If the operation succeeds, it returns a JSON object with no properties.
        This operation is part of the `Custom Key Store feature <http://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a single-tenant key store.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DisconnectCustomKeyStore>`_
        
        **Request Syntax**
        ::
          response = client.disconnect_custom_key_store(
              CustomKeyStoreId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type CustomKeyStoreId: string
        :param CustomKeyStoreId: **[REQUIRED]**
          Enter the ID of the custom key store you want to disconnect. To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.
        :rtype: dict
        :returns:
        """
        pass

    def enable_key(self, KeyId: str):
        """
        Sets the key state of a customer master key (CMK) to enabled. This allows you to use the CMK for cryptographic operations. You cannot perform this operation on a CMK in a different AWS account.
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/EnableKey>`_
        
        **Request Syntax**
        ::
          response = client.enable_key(
              KeyId='string'
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

    def enable_key_rotation(self, KeyId: str):
        """
        Enables `automatic rotation of the key material <http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`__ for the specified customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.
        You cannot enable automatic rotation of CMKs with imported key material or CMKs in a `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ .
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/EnableKeyRotation>`_
        
        **Request Syntax**
        ::
          response = client.enable_key_rotation(
              KeyId='string'
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
        * To move encrypted data from one AWS region to another, you can use this operation to encrypt in the new region the plaintext data key that was used to encrypt the data in the original region. This provides you with an encrypted copy of the data key that can be decrypted in the new region and used there to decrypt the encrypted data. 
        To perform this operation on a CMK in a different AWS account, specify the key ARN or alias ARN in the value of the KeyId parameter.
        Unless you are moving encrypted data from one region to another, you don't use this operation to encrypt a generated data key within a region. To get data keys that are already encrypted, call the  GenerateDataKey or  GenerateDataKeyWithoutPlaintext operation. Data keys don't need to be encrypted again by calling ``Encrypt`` .
        To encrypt data locally in your application, use the  GenerateDataKey operation to return a plaintext data encryption key and a copy of the key encrypted under the CMK of your choosing.
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/Encrypt>`_
        
        **Request Syntax**
        ::
          response = client.encrypt(
              KeyId='string',
              Plaintext=b'bytes',
              EncryptionContext={
                  'string': 'string'
              },
              GrantTokens=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'CiphertextBlob': b'bytes',
                'KeyId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CiphertextBlob** *(bytes) --* 
              The encrypted plaintext. When you use the HTTP API or the AWS CLI, the value is Base64-encdoded. Otherwise, it is not encoded.
            - **KeyId** *(string) --* 
              The ID of the key used during encryption.
        :type KeyId: string
        :param KeyId: **[REQUIRED]**
          A unique identifier for the customer master key (CMK).
          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with \"alias/\". To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.
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
        """
        pass

    def generate_data_key(self, KeyId: str, EncryptionContext: Dict = None, NumberOfBytes: int = None, KeySpec: str = None, GrantTokens: List = None) -> Dict:
        """
        Returns a data encryption key that you can use in your application to encrypt data locally. 
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
              KeyId='string',
              EncryptionContext={
                  'string': 'string'
              },
              NumberOfBytes=123,
              KeySpec='AES_256'|'AES_128',
              GrantTokens=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'CiphertextBlob': b'bytes',
                'Plaintext': b'bytes',
                'KeyId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CiphertextBlob** *(bytes) --* 
              The encrypted data encryption key. When you use the HTTP API or the AWS CLI, the value is Base64-encdoded. Otherwise, it is not encoded.
            - **Plaintext** *(bytes) --* 
              The data encryption key. When you use the HTTP API or the AWS CLI, the value is Base64-encdoded. Otherwise, it is not encoded. Use this data key for local encryption and decryption, then remove it from memory as soon as possible.
            - **KeyId** *(string) --* 
              The identifier of the CMK under which the data encryption key was generated and encrypted.
        :type KeyId: string
        :param KeyId: **[REQUIRED]**
          The identifier of the CMK under which to generate and encrypt the data encryption key.
          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with \"alias/\". To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.
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
        """
        pass

    def generate_data_key_without_plaintext(self, KeyId: str, EncryptionContext: Dict = None, KeySpec: str = None, NumberOfBytes: int = None, GrantTokens: List = None) -> Dict:
        """
        Returns a data encryption key encrypted under a customer master key (CMK). This operation is identical to  GenerateDataKey but returns only the encrypted copy of the data key. 
        To perform this operation on a CMK in a different AWS account, specify the key ARN or alias ARN in the value of the KeyId parameter.
        This operation is useful in a system that has multiple components with different degrees of trust. For example, consider a system that stores encrypted data in containers. Each container stores the encrypted data and an encrypted copy of the data key. One component of the system, called the *control plane* , creates new containers. When it creates a new container, it uses this operation (``GenerateDataKeyWithoutPlaintext`` ) to get an encrypted data key and then stores it in the container. Later, a different component of the system, called the *data plane* , puts encrypted data into the containers. To do this, it passes the encrypted data key to the  Decrypt operation, then uses the returned plaintext data key to encrypt data, and finally stores the encrypted data in the container. In this system, the control plane never sees the plaintext data key.
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GenerateDataKeyWithoutPlaintext>`_
        
        **Request Syntax**
        ::
          response = client.generate_data_key_without_plaintext(
              KeyId='string',
              EncryptionContext={
                  'string': 'string'
              },
              KeySpec='AES_256'|'AES_128',
              NumberOfBytes=123,
              GrantTokens=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'CiphertextBlob': b'bytes',
                'KeyId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CiphertextBlob** *(bytes) --* 
              The encrypted data encryption key. When you use the HTTP API or the AWS CLI, the value is Base64-encdoded. Otherwise, it is not encoded.
            - **KeyId** *(string) --* 
              The identifier of the CMK under which the data encryption key was generated and encrypted.
        :type KeyId: string
        :param KeyId: **[REQUIRED]**
          The identifier of the customer master key (CMK) under which to generate and encrypt the data encryption key.
          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with \"alias/\". To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.
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

    def generate_random(self, NumberOfBytes: int = None, CustomKeyStoreId: str = None) -> Dict:
        """
        Returns a random byte string that is cryptographically secure.
        By default, the random byte string is generated in AWS KMS. To generate the byte string in the AWS CloudHSM cluster that is associated with a `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ , specify the custom key store ID.
        For more information about entropy and random number generation, see the `AWS Key Management Service Cryptographic Details <https://d0.awsstatic.com/whitepapers/KMS-Cryptographic-Details.pdf>`__ whitepaper.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GenerateRandom>`_
        
        **Request Syntax**
        ::
          response = client.generate_random(
              NumberOfBytes=123,
              CustomKeyStoreId='string'
          )
        
        **Response Syntax**
        ::
            {
                'Plaintext': b'bytes'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Plaintext** *(bytes) --* 
              The random byte string. When you use the HTTP API or the AWS CLI, the value is Base64-encdoded. Otherwise, it is not encoded.
        :type NumberOfBytes: integer
        :param NumberOfBytes:
          The length of the byte string.
        :type CustomKeyStoreId: string
        :param CustomKeyStoreId:
          Generates the random byte string in the AWS CloudHSM cluster that is associated with the specified `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ . To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.
        :rtype: dict
        :returns:
        """
        pass

    def get_key_policy(self, KeyId: str, PolicyName: str) -> Dict:
        """
        Gets a key policy attached to the specified customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetKeyPolicy>`_
        
        **Request Syntax**
        ::
          response = client.get_key_policy(
              KeyId='string',
              PolicyName='string'
          )
        
        **Response Syntax**
        ::
            {
                'Policy': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Policy** *(string) --* 
              A key policy document in JSON format.
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
        """
        pass

    def get_key_rotation_status(self, KeyId: str) -> Dict:
        """
        Gets a Boolean value that indicates whether `automatic rotation of the key material <http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`__ is enabled for the specified customer master key (CMK).
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        * Disabled: The key rotation status does not change when you disable a CMK. However, while the CMK is disabled, AWS KMS does not rotate the backing key. 
        * Pending deletion: While a CMK is pending deletion, its key rotation status is ``false`` and AWS KMS does not rotate the backing key. If you cancel the deletion, the original key rotation status is restored. 
        To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the ``KeyId`` parameter.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetKeyRotationStatus>`_
        
        **Request Syntax**
        ::
          response = client.get_key_rotation_status(
              KeyId='string'
          )
        
        **Response Syntax**
        ::
            {
                'KeyRotationEnabled': True|False
            }
        
        **Response Structure**
          - *(dict) --* 
            - **KeyRotationEnabled** *(boolean) --* 
              A Boolean value that specifies whether key rotation is enabled.
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

    def get_parameters_for_import(self, KeyId: str, WrappingAlgorithm: str, WrappingKeySpec: str) -> Dict:
        """
        Returns the items you need in order to import key material into AWS KMS from your existing key management infrastructure. For more information about importing key material into AWS KMS, see `Importing Key Material <http://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ in the *AWS Key Management Service Developer Guide* .
        You must specify the key ID of the customer master key (CMK) into which you will import key material. This CMK's ``Origin`` must be ``EXTERNAL`` . You must also specify the wrapping algorithm and type of wrapping key (public key) that you will use to encrypt the key material. You cannot perform this operation on a CMK in a different AWS account.
        This operation returns a public key and an import token. Use the public key to encrypt the key material. Store the import token to send with a subsequent  ImportKeyMaterial request. The public key and import token from the same response must be used together. These items are valid for 24 hours. When they expire, they cannot be used for a subsequent  ImportKeyMaterial request. To get new ones, send another ``GetParametersForImport`` request.
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetParametersForImport>`_
        
        **Request Syntax**
        ::
          response = client.get_parameters_for_import(
              KeyId='string',
              WrappingAlgorithm='RSAES_PKCS1_V1_5'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
              WrappingKeySpec='RSA_2048'
          )
        
        **Response Syntax**
        ::
            {
                'KeyId': 'string',
                'ImportToken': b'bytes',
                'PublicKey': b'bytes',
                'ParametersValidTo': datetime(2015, 1, 1)
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
          The algorithm you will use to encrypt the key material before importing it with  ImportKeyMaterial . For more information, see `Encrypt the Key Material <http://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-encrypt-key-material.html>`__ in the *AWS Key Management Service Developer Guide* .
        :type WrappingKeySpec: string
        :param WrappingKeySpec: **[REQUIRED]**
          The type of wrapping key (public key) to return in the response. Only 2048-bit RSA public keys are supported.
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

    def import_key_material(self, KeyId: str, ImportToken: bytes, EncryptedKeyMaterial: bytes, ValidTo: datetime = None, ExpirationModel: str = None) -> Dict:
        """
        Imports key material into an existing AWS KMS customer master key (CMK) that was created without key material. You cannot perform this operation on a CMK in a different AWS account. For more information about creating CMKs with no key material and then importing key material, see `Importing Key Material <http://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ in the *AWS Key Management Service Developer Guide* .
        Before using this operation, call  GetParametersForImport . Its response includes a public key and an import token. Use the public key to encrypt the key material. Then, submit the import token from the same ``GetParametersForImport`` response.
        When calling this operation, you must specify the following values:
        * The key ID or key ARN of a CMK with no key material. Its ``Origin`` must be ``EXTERNAL`` . To create a CMK with no key material, call  CreateKey and set the value of its ``Origin`` parameter to ``EXTERNAL`` . To get the ``Origin`` of a CMK, call  DescribeKey .) 
        * The encrypted key material. To get the public key to encrypt the key material, call  GetParametersForImport . 
        * The import token that  GetParametersForImport returned. This token and the public key used to encrypt the key material must have come from the same response. 
        * Whether the key material expires and if so, when. If you set an expiration date, you can change it only by reimporting the same key material and specifying a new expiration date. If the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. To use the CMK again, you must reimport the same key material. 
        When this operation is successful, the key state of the CMK changes from ``PendingImport`` to ``Enabled`` , and you can use the CMK. After you successfully import key material into a CMK, you can reimport the same key material into that CMK, but you cannot import different key material.
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ImportKeyMaterial>`_
        
        **Request Syntax**
        ::
          response = client.import_key_material(
              KeyId='string',
              ImportToken=b'bytes',
              EncryptedKeyMaterial=b'bytes',
              ValidTo=datetime(2015, 1, 1),
              ExpirationModel='KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
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
        """
        pass

    def list_aliases(self, KeyId: str = None, Limit: int = None, Marker: str = None) -> Dict:
        """
        Gets a list of all aliases in the caller's AWS account and region. You cannot list aliases in other accounts. For more information about aliases, see  CreateAlias .
        By default, the ``ListAliases`` command returns all aliases in the account and region. To get only the aliases that point to a particular customer master key (CMK), use the ``KeyId`` parameter.
        The ``ListAliases`` response might include several aliases have no ``TargetKeyId`` field. These are predefined aliases that AWS has created but has not yet associated with a CMK. Aliases that AWS creates in your account, including predefined aliases, do not count against your `AWS KMS aliases limit <http://docs.aws.amazon.com/kms/latest/developerguide/limits.html#aliases-limit>`__ .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListAliases>`_
        
        **Request Syntax**
        ::
          response = client.list_aliases(
              KeyId='string',
              Limit=123,
              Marker='string'
          )
        
        **Response Syntax**
        ::
            {
                'Aliases': [
                    {
                        'AliasName': 'string',
                        'AliasArn': 'string',
                        'TargetKeyId': 'string'
                    },
                ],
                'NextMarker': 'string',
                'Truncated': True|False
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
        """
        pass

    def list_grants(self, KeyId: str, Limit: int = None, Marker: str = None) -> Dict:
        """
        Gets a list of all grants for the specified customer master key (CMK).
        To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the ``KeyId`` parameter.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListGrants>`_
        
        **Request Syntax**
        ::
          response = client.list_grants(
              Limit=123,
              Marker='string',
              KeyId='string'
          )
        
        **Response Syntax**
        ::
            {
                'Grants': [
                    {
                        'KeyId': 'string',
                        'GrantId': 'string',
                        'Name': 'string',
                        'CreationDate': datetime(2015, 1, 1),
                        'GranteePrincipal': 'string',
                        'RetiringPrincipal': 'string',
                        'IssuingAccount': 'string',
                        'Operations': [
                            'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'CreateGrant'|'RetireGrant'|'DescribeKey',
                        ],
                        'Constraints': {
                            'EncryptionContextSubset': {
                                'string': 'string'
                            },
                            'EncryptionContextEquals': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'NextMarker': 'string',
                'Truncated': True|False
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
                  The principal that receives the grant's permissions.
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
        """
        pass

    def list_key_policies(self, KeyId: str, Limit: int = None, Marker: str = None) -> Dict:
        """
        Gets the names of the key policies that are attached to a customer master key (CMK). This operation is designed to get policy names that you can use in a  GetKeyPolicy operation. However, the only valid policy name is ``default`` . You cannot perform this operation on a CMK in a different AWS account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListKeyPolicies>`_
        
        **Request Syntax**
        ::
          response = client.list_key_policies(
              KeyId='string',
              Limit=123,
              Marker='string'
          )
        
        **Response Syntax**
        ::
            {
                'PolicyNames': [
                    'string',
                ],
                'NextMarker': 'string',
                'Truncated': True|False
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
        """
        pass

    def list_keys(self, Limit: int = None, Marker: str = None) -> Dict:
        """
        Gets a list of all customer master keys (CMKs) in the caller's AWS account and region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListKeys>`_
        
        **Request Syntax**
        ::
          response = client.list_keys(
              Limit=123,
              Marker='string'
          )
        
        **Response Syntax**
        ::
            {
                'Keys': [
                    {
                        'KeyId': 'string',
                        'KeyArn': 'string'
                    },
                ],
                'NextMarker': 'string',
                'Truncated': True|False
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
        :type Limit: integer
        :param Limit:
          Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
          This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.
        :type Marker: string
        :param Marker:
          Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextMarker`` from the truncated response you just received.
        :rtype: dict
        :returns:
        """
        pass

    def list_resource_tags(self, KeyId: str, Limit: int = None, Marker: str = None) -> Dict:
        """
        Returns a list of all tags for the specified customer master key (CMK).
        You cannot perform this operation on a CMK in a different AWS account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListResourceTags>`_
        
        **Request Syntax**
        ::
          response = client.list_resource_tags(
              KeyId='string',
              Limit=123,
              Marker='string'
          )
        
        **Response Syntax**
        ::
            {
                'Tags': [
                    {
                        'TagKey': 'string',
                        'TagValue': 'string'
                    },
                ],
                'NextMarker': 'string',
                'Truncated': True|False
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
        """
        pass

    def list_retirable_grants(self, RetiringPrincipal: str, Limit: int = None, Marker: str = None) -> Dict:
        """
        Returns a list of all grants for which the grant's ``RetiringPrincipal`` matches the one specified.
        A typical use is to list all grants that you are able to retire. To retire a grant, use  RetireGrant .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListRetirableGrants>`_
        
        **Request Syntax**
        ::
          response = client.list_retirable_grants(
              Limit=123,
              Marker='string',
              RetiringPrincipal='string'
          )
        
        **Response Syntax**
        ::
            {
                'Grants': [
                    {
                        'KeyId': 'string',
                        'GrantId': 'string',
                        'Name': 'string',
                        'CreationDate': datetime(2015, 1, 1),
                        'GranteePrincipal': 'string',
                        'RetiringPrincipal': 'string',
                        'IssuingAccount': 'string',
                        'Operations': [
                            'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'CreateGrant'|'RetireGrant'|'DescribeKey',
                        ],
                        'Constraints': {
                            'EncryptionContextSubset': {
                                'string': 'string'
                            },
                            'EncryptionContextEquals': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'NextMarker': 'string',
                'Truncated': True|False
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
                  The principal that receives the grant's permissions.
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
        """
        pass

    def put_key_policy(self, KeyId: str, PolicyName: str, Policy: str, BypassPolicyLockoutSafetyCheck: bool = None):
        """
        Attaches a key policy to the specified customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.
        For more information about key policies, see `Key Policies <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/PutKeyPolicy>`_
        
        **Request Syntax**
        ::
          response = client.put_key_policy(
              KeyId='string',
              PolicyName='string',
              Policy='string',
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
          * Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to AWS KMS. For more information, see `Changes that I make are not always immediately visible <http://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency>`__ in the *AWS Identity and Access Management User Guide* .
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
        Encrypts data on the server side with a new customer master key (CMK) without exposing the plaintext of the data on the client side. The data is first decrypted and then reencrypted. You can also use this operation to change the encryption context of a ciphertext. 
        You can reencrypt data using CMKs in different AWS accounts.
        Unlike other operations, ``ReEncrypt`` is authorized twice, once as ``ReEncryptFrom`` on the source CMK and once as ``ReEncryptTo`` on the destination CMK. We recommend that you include the ``"kms:ReEncrypt*"`` permission in your `key policies <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ to permit reencryption from or to the CMK. This permission is automatically included in the key policy when you create a CMK through the console, but you must include it manually when you create a CMK programmatically or when you set a key policy with the  PutKeyPolicy operation.
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ReEncrypt>`_
        
        **Request Syntax**
        ::
          response = client.re_encrypt(
              CiphertextBlob=b'bytes',
              SourceEncryptionContext={
                  'string': 'string'
              },
              DestinationKeyId='string',
              DestinationEncryptionContext={
                  'string': 'string'
              },
              GrantTokens=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'CiphertextBlob': b'bytes',
                'SourceKeyId': 'string',
                'KeyId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CiphertextBlob** *(bytes) --* 
              The reencrypted data. When you use the HTTP API or the AWS CLI, the value is Base64-encdoded. Otherwise, it is not encoded.
            - **SourceKeyId** *(string) --* 
              Unique identifier of the CMK used to originally encrypt the data.
            - **KeyId** *(string) --* 
              Unique identifier of the CMK used to reencrypt the data.
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
          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with \"alias/\". To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.
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
        """
        pass

    def retire_grant(self, GrantToken: str = None, KeyId: str = None, GrantId: str = None):
        """
        Retires a grant. To clean up, you can retire a grant when you're done using it. You should revoke a grant when you intend to actively deny operations that depend on it. The following are permitted to call this API:
        * The AWS account (root user) under which the grant was created 
        * The ``RetiringPrincipal`` , if present in the grant 
        * The ``GranteePrincipal`` , if ``RetireGrant`` is an operation specified in the grant 
        You must identify the grant to retire by its grant token or by a combination of the grant ID and the Amazon Resource Name (ARN) of the customer master key (CMK). A grant token is a unique variable-length base64-encoded string. A grant ID is a 64 character unique identifier of a grant. The  CreateGrant operation returns both.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/RetireGrant>`_
        
        **Request Syntax**
        ::
          response = client.retire_grant(
              GrantToken='string',
              KeyId='string',
              GrantId='string'
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

    def revoke_grant(self, KeyId: str, GrantId: str):
        """
        Revokes the specified grant for the specified customer master key (CMK). You can revoke a grant to actively deny operations that depend on it.
        To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the ``KeyId`` parameter.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/RevokeGrant>`_
        
        **Request Syntax**
        ::
          response = client.revoke_grant(
              KeyId='string',
              GrantId='string'
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
        Schedules the deletion of a customer master key (CMK). You may provide a waiting period, specified in days, before deletion occurs. If you do not provide a waiting period, the default period of 30 days is used. When this operation is successful, the key state of the CMK changes to ``PendingDeletion`` . Before the waiting period ends, you can use  CancelKeyDeletion to cancel the deletion of the CMK. After the waiting period ends, AWS KMS deletes the CMK and all AWS KMS data associated with it, including all aliases that refer to it.
        .. warning::
          Deleting a CMK is a destructive and potentially dangerous operation. When a CMK is deleted, all data that was encrypted under the CMK is unrecoverable. To prevent the use of a CMK without deleting it, use  DisableKey .
        If you schedule deletion of a CMK from a `custom key store <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html>`__ , when the waiting period expires, ``ScheduleKeyDeletion`` deletes the CMK from AWS KMS. Then AWS KMS makes a best effort to delete the key material from the associated AWS CloudHSM cluster. However, you might need to manually `delete the orphaned key material <http://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html#fix-keystore-orphaned-key>`__ from the cluster and its backups.
        You cannot perform this operation on a CMK in a different AWS account.
        For more information about scheduling a CMK for deletion, see `Deleting Customer Master Keys <http://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html>`__ in the *AWS Key Management Service Developer Guide* .
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ScheduleKeyDeletion>`_
        
        **Request Syntax**
        ::
          response = client.schedule_key_deletion(
              KeyId='string',
              PendingWindowInDays=123
          )
        
        **Response Syntax**
        ::
            {
                'KeyId': 'string',
                'DeletionDate': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **KeyId** *(string) --* 
              The unique identifier of the customer master key (CMK) for which deletion is scheduled.
            - **DeletionDate** *(datetime) --* 
              The date and time after which AWS KMS deletes the customer master key (CMK).
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
        """
        pass

    def tag_resource(self, KeyId: str, Tags: List):
        """
        Adds or edits tags for a customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.
        Each tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.
        You can only use a tag key once for each CMK. If you use the tag key again, AWS KMS replaces the current tag value with the specified value.
        For information about the rules that apply to tag keys and tag values, see `User-Defined Tag Restrictions <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__ in the *AWS Billing and Cost Management User Guide* .
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/TagResource>`_
        
        **Request Syntax**
        ::
          response = client.tag_resource(
              KeyId='string',
              Tags=[
                  {
                      'TagKey': 'string',
                      'TagValue': 'string'
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

    def untag_resource(self, KeyId: str, TagKeys: List):
        """
        Removes the specified tags from the specified customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.
        To remove a tag, specify the tag key. To change the tag value of an existing tag key, use  TagResource .
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UntagResource>`_
        
        **Request Syntax**
        ::
          response = client.untag_resource(
              KeyId='string',
              TagKeys=[
                  'string',
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

    def update_alias(self, AliasName: str, TargetKeyId: str):
        """
        Associates an existing alias with a different customer master key (CMK). Each CMK can have multiple aliases, but the aliases must be unique within the account and region. You cannot perform this operation on an alias in a different AWS account.
        This operation works only on existing aliases. To change the alias of a CMK to a new value, use  CreateAlias to create a new alias and  DeleteAlias to delete the old alias.
        Because an alias is not a property of a CMK, you can create, update, and delete the aliases of a CMK without affecting the CMK. Also, aliases do not appear in the response from the  DescribeKey operation. To get the aliases of all CMKs in the account, use the  ListAliases operation. 
        An alias name can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). An alias must start with the word ``alias`` followed by a forward slash (``alias/`` ). The alias name can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). Alias names cannot begin with ``aws`` ; that alias name prefix is reserved by Amazon Web Services (AWS).
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UpdateAlias>`_
        
        **Request Syntax**
        ::
          response = client.update_alias(
              AliasName='string',
              TargetKeyId='string'
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

    def update_custom_key_store(self, CustomKeyStoreId: str, NewCustomKeyStoreName: str = None, KeyStorePassword: str = None, CloudHsmClusterId: str = None) -> Dict:
        """
        Changes the properties of a custom key store. Use the ``CustomKeyStoreId`` parameter to identify the custom key store you want to edit. Use the remaining parameters to change the properties of the custom key store.
        You can only update a custom key store that is disconnected. To disconnect the custom key store, use  DisconnectCustomKeyStore . To reconnect the custom key store after the update completes, use  ConnectCustomKeyStore . To find the connection state of a custom key store, use the  DescribeCustomKeyStores operation.
        Use the ``NewCustomKeyStoreName`` parameter to change the friendly name of the custom key store to the value that you specify.
        Use the ``KeyStorePassword`` parameter tell AWS KMS the current password of the ` ``kmsuser`` crypto user (CU) <http://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser>`__ in the associated AWS CloudHSM cluster. You can use this parameter to fix connection failures that occur when AWS KMS cannot log into the associated cluster because the ``kmsuser`` password has changed. This value does not change the password in the AWS CloudHSM cluster.
        Use the ``CloudHsmClusterId`` parameter to associate the custom key store with a related AWS CloudHSM cluster, that is, a cluster that shares a backup history with the original cluster. You can use this parameter to repair a custom key store if its AWS CloudHSM cluster becomes corrupted or is deleted, or when you need to create or restore a cluster from a backup.
        The cluster ID must identify a AWS CloudHSM cluster with the following requirements.
        * The cluster must be active and be in the same AWS account and Region as the custom key store. 
        * The cluster must have the same cluster certificate as the original cluster. You cannot use this parameter to associate the custom key store with an unrelated cluster. To view the cluster certificate, use the AWS CloudHSM `DescribeClusters <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html>`__ operation. Clusters that share a backup history have the same cluster certificate. 
        * The cluster must be configured with subnets in at least two different Availability Zones in the Region. Because AWS CloudHSM is not supported in all Availability Zones, we recommend that the cluster have subnets in all Availability Zones in the Region. 
        * The cluster must contain at least two active HSMs, each in a different Availability Zone. 
        If the operation succeeds, it returns a JSON object with no properties.
        This operation is part of the `Custom Key Store feature <http://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with the isolation and control of a single-tenant key store.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UpdateCustomKeyStore>`_
        
        **Request Syntax**
        ::
          response = client.update_custom_key_store(
              CustomKeyStoreId='string',
              NewCustomKeyStoreName='string',
              KeyStorePassword='string',
              CloudHsmClusterId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type CustomKeyStoreId: string
        :param CustomKeyStoreId: **[REQUIRED]**
          Identifies the custom key store that you want to update. Enter the ID of the custom key store. To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.
        :type NewCustomKeyStoreName: string
        :param NewCustomKeyStoreName:
          Changes the friendly name of the custom key store to the value that you specify. The custom key store name must be unique in the AWS account.
        :type KeyStorePassword: string
        :param KeyStorePassword:
          Enter the current password of the ``kmsuser`` crypto user (CU) in the AWS CloudHSM cluster that is associated with the custom key store.
          This parameter tells AWS KMS the current password of the ``kmsuser`` crypto user (CU). It does not set or change the password of any users in the AWS CloudHSM cluster.
        :type CloudHsmClusterId: string
        :param CloudHsmClusterId:
          Associates the custom key store with a related AWS CloudHSM cluster.
          Enter the cluster ID of the cluster that you used to create the custom key store or a cluster that shares a backup history with the original cluster. You cannot use this parameter to associate a custom key store with a different cluster.
          Clusters that share a backup history have the same cluster certificate. To view the cluster certificate of a cluster, use the `DescribeClusters <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html>`__ operation.
        :rtype: dict
        :returns:
        """
        pass

    def update_key_description(self, KeyId: str, Description: str):
        """
        Updates the description of a customer master key (CMK). To see the decription of a CMK, use  DescribeKey . 
        You cannot perform this operation on a CMK in a different AWS account.
        The result of this operation varies with the key state of the CMK. For details, see `How Key State Affects Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UpdateKeyDescription>`_
        
        **Request Syntax**
        ::
          response = client.update_key_description(
              KeyId='string',
              Description='string'
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
