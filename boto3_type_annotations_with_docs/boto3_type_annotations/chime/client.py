from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
    def associate_phone_number_with_user(self, AccountId: str, UserId: str, E164PhoneNumber: str) -> Dict:
        """
        Associates a phone number with the specified Amazon Chime user.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/AssociatePhoneNumberWithUser>`_
        
        **Request Syntax**
        ::
          response = client.associate_phone_number_with_user(
              AccountId='string',
              UserId='string',
              E164PhoneNumber='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type UserId: string
        :param UserId: **[REQUIRED]**
          The user ID.
        :type E164PhoneNumber: string
        :param E164PhoneNumber: **[REQUIRED]**
          The phone number, in E.164 format.
        :rtype: dict
        :returns:
        """
        pass

    def associate_phone_numbers_with_voice_connector(self, VoiceConnectorId: str, E164PhoneNumbers: List = None) -> Dict:
        """
        Associates a phone number with the specified Amazon Chime Voice Connector.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/AssociatePhoneNumbersWithVoiceConnector>`_
        
        **Request Syntax**
        ::
          response = client.associate_phone_numbers_with_voice_connector(
              VoiceConnectorId='string',
              E164PhoneNumbers=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'PhoneNumberErrors': [
                    {
                        'PhoneNumberId': 'string',
                        'ErrorCode': 'Unauthorized'|'Forbidden'|'NotFound'|'BadRequest'|'Conflict'|'ServiceFailure'|'ServiceUnavailable'|'Unprocessable'|'Throttled'|'PreconditionFailed',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PhoneNumberErrors** *(list) --* 
              If the action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.
              - *(dict) --* 
                If the phone number action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.
                - **PhoneNumberId** *(string) --* 
                  The phone number ID for which the action failed.
                - **ErrorCode** *(string) --* 
                  The error code.
                - **ErrorMessage** *(string) --* 
                  The error message.
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
        :type E164PhoneNumbers: list
        :param E164PhoneNumbers:
          List of phone numbers, in E.164 format.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def batch_delete_phone_number(self, PhoneNumberIds: List) -> Dict:
        """
        Moves phone numbers into the **Deletion queue** . Phone numbers must be disassociated from any users or Amazon Chime Voice Connectors before they can be deleted.
        Phone numbers remain in the **Deletion queue** for 7 days before they are deleted permanently.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/BatchDeletePhoneNumber>`_
        
        **Request Syntax**
        ::
          response = client.batch_delete_phone_number(
              PhoneNumberIds=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'PhoneNumberErrors': [
                    {
                        'PhoneNumberId': 'string',
                        'ErrorCode': 'Unauthorized'|'Forbidden'|'NotFound'|'BadRequest'|'Conflict'|'ServiceFailure'|'ServiceUnavailable'|'Unprocessable'|'Throttled'|'PreconditionFailed',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PhoneNumberErrors** *(list) --* 
              If the action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.
              - *(dict) --* 
                If the phone number action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.
                - **PhoneNumberId** *(string) --* 
                  The phone number ID for which the action failed.
                - **ErrorCode** *(string) --* 
                  The error code.
                - **ErrorMessage** *(string) --* 
                  The error message.
        :type PhoneNumberIds: list
        :param PhoneNumberIds: **[REQUIRED]**
          List of phone number IDs.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def batch_suspend_user(self, AccountId: str, UserIdList: List) -> Dict:
        """
        Suspends up to 50 users from a ``Team`` or ``EnterpriseLWA`` Amazon Chime account. For more information about different account types, see `Managing Your Amazon Chime Accounts <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon Chime Administration Guide* .
        Users suspended from a ``Team`` account are dissociated from the account, but they can continue to use Amazon Chime as free users. To remove the suspension from suspended ``Team`` account users, invite them to the ``Team`` account again. You can use the  InviteUsers action to do so.
        Users suspended from an ``EnterpriseLWA`` account are immediately signed out of Amazon Chime and can no longer sign in. To remove the suspension from suspended ``EnterpriseLWA`` account users, use the  BatchUnsuspendUser action. 
        To sign out users without suspending them, use the  LogoutUser action.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/BatchSuspendUser>`_
        
        **Request Syntax**
        ::
          response = client.batch_suspend_user(
              AccountId='string',
              UserIdList=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'UserErrors': [
                    {
                        'UserId': 'string',
                        'ErrorCode': 'Unauthorized'|'Forbidden'|'NotFound'|'BadRequest'|'Conflict'|'ServiceFailure'|'ServiceUnavailable'|'Unprocessable'|'Throttled'|'PreconditionFailed',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **UserErrors** *(list) --* 
              If the  BatchSuspendUser action fails for one or more of the user IDs in the request, a list of the user IDs is returned, along with error codes and error messages.
              - *(dict) --* 
                The list of errors returned when errors are encountered during the  BatchSuspendUser ,  BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and error messages.
                - **UserId** *(string) --* 
                  The user ID for which the action failed.
                - **ErrorCode** *(string) --* 
                  The error code.
                - **ErrorMessage** *(string) --* 
                  The error message.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type UserIdList: list
        :param UserIdList: **[REQUIRED]**
          The request containing the user IDs to suspend.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def batch_unsuspend_user(self, AccountId: str, UserIdList: List) -> Dict:
        """
        Removes the suspension from up to 50 previously suspended users for the specified Amazon Chime ``EnterpriseLWA`` account. Only users on ``EnterpriseLWA`` accounts can be unsuspended using this action. For more information about different account types, see `Managing Your Amazon Chime Accounts <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon Chime Administration Guide* .
        Previously suspended users who are unsuspended using this action are returned to ``Registered`` status. Users who are not previously suspended are ignored.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/BatchUnsuspendUser>`_
        
        **Request Syntax**
        ::
          response = client.batch_unsuspend_user(
              AccountId='string',
              UserIdList=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'UserErrors': [
                    {
                        'UserId': 'string',
                        'ErrorCode': 'Unauthorized'|'Forbidden'|'NotFound'|'BadRequest'|'Conflict'|'ServiceFailure'|'ServiceUnavailable'|'Unprocessable'|'Throttled'|'PreconditionFailed',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **UserErrors** *(list) --* 
              If the  BatchUnsuspendUser action fails for one or more of the user IDs in the request, a list of the user IDs is returned, along with error codes and error messages.
              - *(dict) --* 
                The list of errors returned when errors are encountered during the  BatchSuspendUser ,  BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and error messages.
                - **UserId** *(string) --* 
                  The user ID for which the action failed.
                - **ErrorCode** *(string) --* 
                  The error code.
                - **ErrorMessage** *(string) --* 
                  The error message.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type UserIdList: list
        :param UserIdList: **[REQUIRED]**
          The request containing the user IDs to unsuspend.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def batch_update_phone_number(self, UpdatePhoneNumberRequestItems: List) -> Dict:
        """
        Updates phone number product types. Choose from Amazon Chime Business Calling and Amazon Chime Voice Connector product types.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/BatchUpdatePhoneNumber>`_
        
        **Request Syntax**
        ::
          response = client.batch_update_phone_number(
              UpdatePhoneNumberRequestItems=[
                  {
                      'PhoneNumberId': 'string',
                      'ProductType': 'BusinessCalling'|'VoiceConnector'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'PhoneNumberErrors': [
                    {
                        'PhoneNumberId': 'string',
                        'ErrorCode': 'Unauthorized'|'Forbidden'|'NotFound'|'BadRequest'|'Conflict'|'ServiceFailure'|'ServiceUnavailable'|'Unprocessable'|'Throttled'|'PreconditionFailed',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PhoneNumberErrors** *(list) --* 
              If the action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.
              - *(dict) --* 
                If the phone number action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.
                - **PhoneNumberId** *(string) --* 
                  The phone number ID for which the action failed.
                - **ErrorCode** *(string) --* 
                  The error code.
                - **ErrorMessage** *(string) --* 
                  The error message.
        :type UpdatePhoneNumberRequestItems: list
        :param UpdatePhoneNumberRequestItems: **[REQUIRED]**
          The request containing the phone number IDs and product types to update.
          - *(dict) --*
            The phone number ID and product type fields to update, used with the  BatchUpdatePhoneNumber and  UpdatePhoneNumber actions.
            - **PhoneNumberId** *(string) --* **[REQUIRED]**
              The phone number ID to update.
            - **ProductType** *(string) --*
              The product type to update.
        :rtype: dict
        :returns:
        """
        pass

    def batch_update_user(self, AccountId: str, UpdateUserRequestItems: List) -> Dict:
        """
        Updates user details within the  UpdateUserRequestItem object for up to 20 users for the specified Amazon Chime account. Currently, only ``LicenseType`` updates are supported for this action.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/BatchUpdateUser>`_
        
        **Request Syntax**
        ::
          response = client.batch_update_user(
              AccountId='string',
              UpdateUserRequestItems=[
                  {
                      'UserId': 'string',
                      'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'UserErrors': [
                    {
                        'UserId': 'string',
                        'ErrorCode': 'Unauthorized'|'Forbidden'|'NotFound'|'BadRequest'|'Conflict'|'ServiceFailure'|'ServiceUnavailable'|'Unprocessable'|'Throttled'|'PreconditionFailed',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **UserErrors** *(list) --* 
              If the  BatchUpdateUser action fails for one or more of the user IDs in the request, a list of the user IDs is returned, along with error codes and error messages.
              - *(dict) --* 
                The list of errors returned when errors are encountered during the  BatchSuspendUser ,  BatchUnsuspendUser , or  BatchUpdateUser actions. This includes user IDs, error codes, and error messages.
                - **UserId** *(string) --* 
                  The user ID for which the action failed.
                - **ErrorCode** *(string) --* 
                  The error code.
                - **ErrorMessage** *(string) --* 
                  The error message.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type UpdateUserRequestItems: list
        :param UpdateUserRequestItems: **[REQUIRED]**
          The request containing the user IDs and details to update.
          - *(dict) --*
            The user ID and user fields to update, used with the  BatchUpdateUser action.
            - **UserId** *(string) --* **[REQUIRED]**
              The user ID.
            - **LicenseType** *(string) --*
              The user license type.
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

    def create_account(self, Name: str) -> Dict:
        """
        Creates an Amazon Chime account under the administrator's AWS account. Only ``Team`` account types are currently supported for this action. For more information about different account types, see `Managing Your Amazon Chime Accounts <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon Chime Administration Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/CreateAccount>`_
        
        **Request Syntax**
        ::
          response = client.create_account(
              Name='string'
          )
        
        **Response Syntax**
        ::
            {
                'Account': {
                    'AwsAccountId': 'string',
                    'AccountId': 'string',
                    'Name': 'string',
                    'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
                    'SupportedLicenses': [
                        'Basic'|'Plus'|'Pro'|'ProTrial',
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Account** *(dict) --* 
              The Amazon Chime account details.
              - **AwsAccountId** *(string) --* 
                The AWS account ID.
              - **AccountId** *(string) --* 
                The Amazon Chime account ID.
              - **Name** *(string) --* 
                The Amazon Chime account name.
              - **AccountType** *(string) --* 
                The Amazon Chime account type. For more information about different account types, see `Managing Your Amazon Chime Accounts <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon Chime Administration Guide* .
              - **CreatedTimestamp** *(datetime) --* 
                The Amazon Chime account creation timestamp, in ISO 8601 format.
              - **DefaultLicense** *(string) --* 
                The default license for the Amazon Chime account.
              - **SupportedLicenses** *(list) --* 
                Supported licenses for the Amazon Chime account.
                - *(string) --* 
        :type Name: string
        :param Name: **[REQUIRED]**
          The name of the Amazon Chime account.
        :rtype: dict
        :returns:
        """
        pass

    def create_phone_number_order(self, ProductType: str, E164PhoneNumbers: List) -> Dict:
        """
        Creates an order for phone numbers to be provisioned. Choose from Amazon Chime Business Calling and Amazon Chime Voice Connector product types.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/CreatePhoneNumberOrder>`_
        
        **Request Syntax**
        ::
          response = client.create_phone_number_order(
              ProductType='BusinessCalling'|'VoiceConnector',
              E164PhoneNumbers=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'PhoneNumberOrder': {
                    'PhoneNumberOrderId': 'string',
                    'ProductType': 'BusinessCalling'|'VoiceConnector',
                    'Status': 'Processing'|'Successful'|'Failed'|'Partial',
                    'OrderedPhoneNumbers': [
                        {
                            'E164PhoneNumber': 'string',
                            'Status': 'Processing'|'Acquired'|'Failed'
                        },
                    ],
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PhoneNumberOrder** *(dict) --* 
              The phone number order details.
              - **PhoneNumberOrderId** *(string) --* 
                The phone number order ID.
              - **ProductType** *(string) --* 
                The phone number order product type.
              - **Status** *(string) --* 
                The status of the phone number order.
              - **OrderedPhoneNumbers** *(list) --* 
                The ordered phone number details, such as the phone number in E.164 format and the phone number status.
                - *(dict) --* 
                  A phone number for which an order has been placed.
                  - **E164PhoneNumber** *(string) --* 
                    The phone number, in E.164 format.
                  - **Status** *(string) --* 
                    The phone number status.
              - **CreatedTimestamp** *(datetime) --* 
                The phone number order creation timestamp, in ISO 8601 format.
              - **UpdatedTimestamp** *(datetime) --* 
                The updated phone number order timestamp, in ISO 8601 format.
        :type ProductType: string
        :param ProductType: **[REQUIRED]**
          The phone number product type.
        :type E164PhoneNumbers: list
        :param E164PhoneNumbers: **[REQUIRED]**
          List of phone numbers, in E.164 format.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def create_voice_connector(self, Name: str, RequireEncryption: bool) -> Dict:
        """
        Creates an Amazon Chime Voice Connector under the administrator's AWS account. Enabling  CreateVoiceConnectorRequest$RequireEncryption configures your Amazon Chime Voice Connector to use TLS transport for SIP signaling and Secure RTP (SRTP) for media. Inbound calls use TLS transport, and unencrypted outbound calls are blocked.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/CreateVoiceConnector>`_
        
        **Request Syntax**
        ::
          response = client.create_voice_connector(
              Name='string',
              RequireEncryption=True|False
          )
        
        **Response Syntax**
        ::
            {
                'VoiceConnector': {
                    'VoiceConnectorId': 'string',
                    'Name': 'string',
                    'OutboundHostName': 'string',
                    'RequireEncryption': True|False,
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **VoiceConnector** *(dict) --* 
              The Amazon Chime Voice Connector details.
              - **VoiceConnectorId** *(string) --* 
                The Amazon Chime Voice Connector ID.
              - **Name** *(string) --* 
                The name of the Amazon Chime Voice Connector.
              - **OutboundHostName** *(string) --* 
                The outbound host name for the Amazon Chime Voice Connector.
              - **RequireEncryption** *(boolean) --* 
                Designates whether encryption is required for the Amazon Chime Voice Connector.
              - **CreatedTimestamp** *(datetime) --* 
                The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.
              - **UpdatedTimestamp** *(datetime) --* 
                The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.
        :type Name: string
        :param Name: **[REQUIRED]**
          The name of the Amazon Chime Voice Connector.
        :type RequireEncryption: boolean
        :param RequireEncryption: **[REQUIRED]**
          When enabled, requires encryption for the Amazon Chime Voice Connector.
        :rtype: dict
        :returns:
        """
        pass

    def delete_account(self, AccountId: str) -> Dict:
        """
        Deletes the specified Amazon Chime account. You must suspend all users before deleting a ``Team`` account. You can use the  BatchSuspendUser action to do so.
        For ``EnterpriseLWA`` and ``EnterpriseAD`` accounts, you must release the claimed domains for your Amazon Chime account before deletion. As soon as you release the domain, all users under that account are suspended.
        Deleted accounts appear in your ``Disabled`` accounts list for 90 days. To restore a deleted account from your ``Disabled`` accounts list, you must contact AWS Support.
        After 90 days, deleted accounts are permanently removed from your ``Disabled`` accounts list.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteAccount>`_
        
        **Request Syntax**
        ::
          response = client.delete_account(
              AccountId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :rtype: dict
        :returns:
        """
        pass

    def delete_phone_number(self, PhoneNumberId: str):
        """
        Moves the specified phone number into the **Deletion queue** . A phone number must be disassociated from any users or Amazon Chime Voice Connectors before it can be deleted.
        Deleted phone numbers remain in the **Deletion queue** for 7 days before they are deleted permanently.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeletePhoneNumber>`_
        
        **Request Syntax**
        ::
          response = client.delete_phone_number(
              PhoneNumberId='string'
          )
        :type PhoneNumberId: string
        :param PhoneNumberId: **[REQUIRED]**
          The phone number ID.
        :returns: None
        """
        pass

    def delete_voice_connector(self, VoiceConnectorId: str):
        """
        Deletes the specified Amazon Chime Voice Connector. Any phone numbers assigned to the Amazon Chime Voice Connector must be unassigned from it before it can be deleted.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteVoiceConnector>`_
        
        **Request Syntax**
        ::
          response = client.delete_voice_connector(
              VoiceConnectorId='string'
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
        :returns: None
        """
        pass

    def delete_voice_connector_origination(self, VoiceConnectorId: str):
        """
        Deletes the origination settings for the specified Amazon Chime Voice Connector.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteVoiceConnectorOrigination>`_
        
        **Request Syntax**
        ::
          response = client.delete_voice_connector_origination(
              VoiceConnectorId='string'
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
        :returns: None
        """
        pass

    def delete_voice_connector_termination(self, VoiceConnectorId: str):
        """
        Deletes the termination settings for the specified Amazon Chime Voice Connector.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteVoiceConnectorTermination>`_
        
        **Request Syntax**
        ::
          response = client.delete_voice_connector_termination(
              VoiceConnectorId='string'
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
        :returns: None
        """
        pass

    def delete_voice_connector_termination_credentials(self, VoiceConnectorId: str, Usernames: List = None):
        """
        Deletes the specified SIP credentials used by your equipment to authenticate during call termination.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteVoiceConnectorTerminationCredentials>`_
        
        **Request Syntax**
        ::
          response = client.delete_voice_connector_termination_credentials(
              VoiceConnectorId='string',
              Usernames=[
                  'string',
              ]
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
        :type Usernames: list
        :param Usernames:
          The RFC2617 compliant username associated with the SIP credentials, in US-ASCII format.
          - *(string) --*
        :returns: None
        """
        pass

    def disassociate_phone_number_from_user(self, AccountId: str, UserId: str) -> Dict:
        """
        Disassociates the primary provisioned phone number from the specified Amazon Chime user.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DisassociatePhoneNumberFromUser>`_
        
        **Request Syntax**
        ::
          response = client.disassociate_phone_number_from_user(
              AccountId='string',
              UserId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type UserId: string
        :param UserId: **[REQUIRED]**
          The user ID.
        :rtype: dict
        :returns:
        """
        pass

    def disassociate_phone_numbers_from_voice_connector(self, VoiceConnectorId: str, E164PhoneNumbers: List = None) -> Dict:
        """
        Disassociates the specified phone number from the specified Amazon Chime Voice Connector.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DisassociatePhoneNumbersFromVoiceConnector>`_
        
        **Request Syntax**
        ::
          response = client.disassociate_phone_numbers_from_voice_connector(
              VoiceConnectorId='string',
              E164PhoneNumbers=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'PhoneNumberErrors': [
                    {
                        'PhoneNumberId': 'string',
                        'ErrorCode': 'Unauthorized'|'Forbidden'|'NotFound'|'BadRequest'|'Conflict'|'ServiceFailure'|'ServiceUnavailable'|'Unprocessable'|'Throttled'|'PreconditionFailed',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PhoneNumberErrors** *(list) --* 
              If the action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.
              - *(dict) --* 
                If the phone number action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.
                - **PhoneNumberId** *(string) --* 
                  The phone number ID for which the action failed.
                - **ErrorCode** *(string) --* 
                  The error code.
                - **ErrorMessage** *(string) --* 
                  The error message.
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
        :type E164PhoneNumbers: list
        :param E164PhoneNumbers:
          List of phone numbers, in E.164 format.
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

    def get_account(self, AccountId: str) -> Dict:
        """
        Retrieves details for the specified Amazon Chime account, such as account type and supported licenses.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetAccount>`_
        
        **Request Syntax**
        ::
          response = client.get_account(
              AccountId='string'
          )
        
        **Response Syntax**
        ::
            {
                'Account': {
                    'AwsAccountId': 'string',
                    'AccountId': 'string',
                    'Name': 'string',
                    'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
                    'SupportedLicenses': [
                        'Basic'|'Plus'|'Pro'|'ProTrial',
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Account** *(dict) --* 
              The Amazon Chime account details.
              - **AwsAccountId** *(string) --* 
                The AWS account ID.
              - **AccountId** *(string) --* 
                The Amazon Chime account ID.
              - **Name** *(string) --* 
                The Amazon Chime account name.
              - **AccountType** *(string) --* 
                The Amazon Chime account type. For more information about different account types, see `Managing Your Amazon Chime Accounts <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon Chime Administration Guide* .
              - **CreatedTimestamp** *(datetime) --* 
                The Amazon Chime account creation timestamp, in ISO 8601 format.
              - **DefaultLicense** *(string) --* 
                The default license for the Amazon Chime account.
              - **SupportedLicenses** *(list) --* 
                Supported licenses for the Amazon Chime account.
                - *(string) --* 
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_account_settings(self, AccountId: str) -> Dict:
        """
        Retrieves account settings for the specified Amazon Chime account ID, such as remote control and dial out settings. For more information about these settings, see `Use the Policies Page <https://docs.aws.amazon.com/chime/latest/ag/policies.html>`__ in the *Amazon Chime Administration Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetAccountSettings>`_
        
        **Request Syntax**
        ::
          response = client.get_account_settings(
              AccountId='string'
          )
        
        **Response Syntax**
        ::
            {
                'AccountSettings': {
                    'DisableRemoteControl': True|False,
                    'EnableDialOut': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AccountSettings** *(dict) --* 
              The Amazon Chime account settings.
              - **DisableRemoteControl** *(boolean) --* 
                Setting that stops or starts remote control of shared screens during meetings.
              - **EnableDialOut** *(boolean) --* 
                Setting that allows meeting participants to choose the **Call me at a phone number** option. For more information, see `Join a Meeting without the Amazon Chime App <https://docs.aws.amazon.com/chime/latest/ug/chime-join-meeting.html>`__ .
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_global_settings(self) -> Dict:
        """
        Retrieves global settings for the administrator's AWS account, such as Amazon Chime Business Calling and Amazon Chime Voice Connector settings.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetGlobalSettings>`_
        
        **Request Syntax**
        ::
          response = client.get_global_settings()
        
        **Response Syntax**
        ::
            {
                'BusinessCalling': {
                    'CdrBucket': 'string'
                },
                'VoiceConnector': {
                    'CdrBucket': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **BusinessCalling** *(dict) --* 
              The Amazon Chime Business Calling settings.
              - **CdrBucket** *(string) --* 
                The Amazon S3 bucket designated for call detail record storage.
            - **VoiceConnector** *(dict) --* 
              The Amazon Chime Voice Connector settings.
              - **CdrBucket** *(string) --* 
                The Amazon S3 bucket designated for call detail record storage.
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

    def get_phone_number(self, PhoneNumberId: str) -> Dict:
        """
        Retrieves details for the specified phone number ID, such as associations, capabilities, and product type.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetPhoneNumber>`_
        
        **Request Syntax**
        ::
          response = client.get_phone_number(
              PhoneNumberId='string'
          )
        
        **Response Syntax**
        ::
            {
                'PhoneNumber': {
                    'PhoneNumberId': 'string',
                    'E164PhoneNumber': 'string',
                    'ProductType': 'BusinessCalling'|'VoiceConnector',
                    'Status': 'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'|'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
                    'Capabilities': {
                        'InboundCall': True|False,
                        'OutboundCall': True|False,
                        'InboundSMS': True|False,
                        'OutboundSMS': True|False,
                        'InboundMMS': True|False,
                        'OutboundMMS': True|False
                    },
                    'Associations': [
                        {
                            'Value': 'string',
                            'Name': 'AccountId'|'UserId'|'VoiceConnectorId',
                            'AssociatedTimestamp': datetime(2015, 1, 1)
                        },
                    ],
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1),
                    'DeletionTimestamp': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PhoneNumber** *(dict) --* 
              The phone number details.
              - **PhoneNumberId** *(string) --* 
                The phone number ID.
              - **E164PhoneNumber** *(string) --* 
                The phone number, in E.164 format.
              - **ProductType** *(string) --* 
                The phone number product type.
              - **Status** *(string) --* 
                The phone number status.
              - **Capabilities** *(dict) --* 
                The phone number capabilities.
                - **InboundCall** *(boolean) --* 
                  Allows or denies inbound calling for the specified phone number.
                - **OutboundCall** *(boolean) --* 
                  Allows or denies outbound calling for the specified phone number.
                - **InboundSMS** *(boolean) --* 
                  Allows or denies inbound SMS messaging for the specified phone number.
                - **OutboundSMS** *(boolean) --* 
                  Allows or denies outbound SMS messaging for the specified phone number.
                - **InboundMMS** *(boolean) --* 
                  Allows or denies inbound MMS messaging for the specified phone number.
                - **OutboundMMS** *(boolean) --* 
                  Allows or denies outbound MMS messaging for the specified phone number.
              - **Associations** *(list) --* 
                The phone number associations.
                - *(dict) --* 
                  The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID, or Amazon Chime Voice Connector ID.
                  - **Value** *(string) --* 
                    Contains the ID for the entity specified in Name.
                  - **Name** *(string) --* 
                    Defines the association with an Amazon Chime account ID, user ID, or Amazon Chime Voice Connector ID.
                  - **AssociatedTimestamp** *(datetime) --* 
                    The timestamp of the phone number association, in ISO 8601 format.
              - **CreatedTimestamp** *(datetime) --* 
                The phone number creation timestamp, in ISO 8601 format.
              - **UpdatedTimestamp** *(datetime) --* 
                The updated phone number timestamp, in ISO 8601 format.
              - **DeletionTimestamp** *(datetime) --* 
                The deleted phone number timestamp, in ISO 8601 format.
        :type PhoneNumberId: string
        :param PhoneNumberId: **[REQUIRED]**
          The phone number ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_phone_number_order(self, PhoneNumberOrderId: str) -> Dict:
        """
        Retrieves details for the specified phone number order, such as order creation timestamp, phone numbers in E.164 format, product type, and order status.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetPhoneNumberOrder>`_
        
        **Request Syntax**
        ::
          response = client.get_phone_number_order(
              PhoneNumberOrderId='string'
          )
        
        **Response Syntax**
        ::
            {
                'PhoneNumberOrder': {
                    'PhoneNumberOrderId': 'string',
                    'ProductType': 'BusinessCalling'|'VoiceConnector',
                    'Status': 'Processing'|'Successful'|'Failed'|'Partial',
                    'OrderedPhoneNumbers': [
                        {
                            'E164PhoneNumber': 'string',
                            'Status': 'Processing'|'Acquired'|'Failed'
                        },
                    ],
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PhoneNumberOrder** *(dict) --* 
              The phone number order details.
              - **PhoneNumberOrderId** *(string) --* 
                The phone number order ID.
              - **ProductType** *(string) --* 
                The phone number order product type.
              - **Status** *(string) --* 
                The status of the phone number order.
              - **OrderedPhoneNumbers** *(list) --* 
                The ordered phone number details, such as the phone number in E.164 format and the phone number status.
                - *(dict) --* 
                  A phone number for which an order has been placed.
                  - **E164PhoneNumber** *(string) --* 
                    The phone number, in E.164 format.
                  - **Status** *(string) --* 
                    The phone number status.
              - **CreatedTimestamp** *(datetime) --* 
                The phone number order creation timestamp, in ISO 8601 format.
              - **UpdatedTimestamp** *(datetime) --* 
                The updated phone number order timestamp, in ISO 8601 format.
        :type PhoneNumberOrderId: string
        :param PhoneNumberOrderId: **[REQUIRED]**
          The ID for the phone number order.
        :rtype: dict
        :returns:
        """
        pass

    def get_user(self, AccountId: str, UserId: str) -> Dict:
        """
        Retrieves details for the specified user ID, such as primary email address, license type, and personal meeting PIN.
        To retrieve user details with an email address instead of a user ID, use the  ListUsers action, and then filter by email address.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetUser>`_
        
        **Request Syntax**
        ::
          response = client.get_user(
              AccountId='string',
              UserId='string'
          )
        
        **Response Syntax**
        ::
            {
                'User': {
                    'UserId': 'string',
                    'AccountId': 'string',
                    'PrimaryEmail': 'string',
                    'PrimaryProvisionedNumber': 'string',
                    'DisplayName': 'string',
                    'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
                    'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
                    'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
                    'RegisteredOn': datetime(2015, 1, 1),
                    'InvitedOn': datetime(2015, 1, 1),
                    'PersonalPIN': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **User** *(dict) --* 
              The user details.
              - **UserId** *(string) --* 
                The user ID.
              - **AccountId** *(string) --* 
                The Amazon Chime account ID.
              - **PrimaryEmail** *(string) --* 
                The primary email address of the user.
              - **PrimaryProvisionedNumber** *(string) --* 
                The primary phone number associated with the user.
              - **DisplayName** *(string) --* 
                The display name of the user.
              - **LicenseType** *(string) --* 
                The license type for the user.
              - **UserRegistrationStatus** *(string) --* 
                The user registration status.
              - **UserInvitationStatus** *(string) --* 
                The user invite status.
              - **RegisteredOn** *(datetime) --* 
                Date and time when the user is registered, in ISO 8601 format.
              - **InvitedOn** *(datetime) --* 
                Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.
              - **PersonalPIN** *(string) --* 
                The user's personal meeting PIN.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type UserId: string
        :param UserId: **[REQUIRED]**
          The user ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_user_settings(self, AccountId: str, UserId: str) -> Dict:
        """
        Retrieves settings for the specified user ID, such as any associated phone number settings.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetUserSettings>`_
        
        **Request Syntax**
        ::
          response = client.get_user_settings(
              AccountId='string',
              UserId='string'
          )
        
        **Response Syntax**
        ::
            {
                'UserSettings': {
                    'Telephony': {
                        'InboundCalling': True|False,
                        'OutboundCalling': True|False,
                        'SMS': True|False
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **UserSettings** *(dict) --* 
              The user settings.
              - **Telephony** *(dict) --* 
                The telephony settings associated with the user.
                - **InboundCalling** *(boolean) --* 
                  Allows or denies inbound calling.
                - **OutboundCalling** *(boolean) --* 
                  Allows or denies outbound calling.
                - **SMS** *(boolean) --* 
                  Allows or denies SMS messaging.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type UserId: string
        :param UserId: **[REQUIRED]**
          The user ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_voice_connector(self, VoiceConnectorId: str) -> Dict:
        """
        Retrieves details for the specified Amazon Chime Voice Connector, such as timestamps, name, outbound host, and encryption requirements.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetVoiceConnector>`_
        
        **Request Syntax**
        ::
          response = client.get_voice_connector(
              VoiceConnectorId='string'
          )
        
        **Response Syntax**
        ::
            {
                'VoiceConnector': {
                    'VoiceConnectorId': 'string',
                    'Name': 'string',
                    'OutboundHostName': 'string',
                    'RequireEncryption': True|False,
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **VoiceConnector** *(dict) --* 
              The Amazon Chime Voice Connector details.
              - **VoiceConnectorId** *(string) --* 
                The Amazon Chime Voice Connector ID.
              - **Name** *(string) --* 
                The name of the Amazon Chime Voice Connector.
              - **OutboundHostName** *(string) --* 
                The outbound host name for the Amazon Chime Voice Connector.
              - **RequireEncryption** *(boolean) --* 
                Designates whether encryption is required for the Amazon Chime Voice Connector.
              - **CreatedTimestamp** *(datetime) --* 
                The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.
              - **UpdatedTimestamp** *(datetime) --* 
                The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_voice_connector_origination(self, VoiceConnectorId: str) -> Dict:
        """
        Retrieves origination setting details for the specified Amazon Chime Voice Connector.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetVoiceConnectorOrigination>`_
        
        **Request Syntax**
        ::
          response = client.get_voice_connector_origination(
              VoiceConnectorId='string'
          )
        
        **Response Syntax**
        ::
            {
                'Origination': {
                    'Routes': [
                        {
                            'Host': 'string',
                            'Port': 123,
                            'Protocol': 'TCP'|'UDP',
                            'Priority': 123,
                            'Weight': 123
                        },
                    ],
                    'Disabled': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Origination** *(dict) --* 
              The origination setting details.
              - **Routes** *(list) --* 
                The call distribution properties defined for your SIP hosts. Valid range: Minimum value of 1. Maximum value of 20.
                - *(dict) --* 
                  Origination routes define call distribution properties for your SIP hosts to receive inbound calls using your Amazon Chime Voice Connector. Limit: 10 origination routes per Amazon Chime Voice Connector.
                  - **Host** *(string) --* 
                    The FODN or IP address to contact for origination traffic.
                  - **Port** *(integer) --* 
                    The designated origination route port. Defaults to 5060.
                  - **Protocol** *(string) --* 
                    The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice Connectors use TCP protocol by default.
                  - **Priority** *(integer) --* 
                    The priority associated with the host, with 1 being the highest priority. Higher priority hosts are attempted first.
                  - **Weight** *(integer) --* 
                    The weight associated with the host. If hosts are equal in priority, calls are distributed among them based on their relative weight.
              - **Disabled** *(boolean) --* 
                When origination settings are disabled, inbound calls are not enabled for your Amazon Chime Voice Connector.
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_voice_connector_termination(self, VoiceConnectorId: str) -> Dict:
        """
        Retrieves termination setting details for the specified Amazon Chime Voice Connector.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetVoiceConnectorTermination>`_
        
        **Request Syntax**
        ::
          response = client.get_voice_connector_termination(
              VoiceConnectorId='string'
          )
        
        **Response Syntax**
        ::
            {
                'Termination': {
                    'CpsLimit': 123,
                    'DefaultPhoneNumber': 'string',
                    'CallingRegions': [
                        'string',
                    ],
                    'CidrAllowedList': [
                        'string',
                    ],
                    'Disabled': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Termination** *(dict) --* 
              The termination setting details.
              - **CpsLimit** *(integer) --* 
                The limit on calls per second. Max value based on account service limit. Default value of 1.
              - **DefaultPhoneNumber** *(string) --* 
                The default caller ID phone number.
              - **CallingRegions** *(list) --* 
                The countries to which calls are allowed.
                - *(string) --* 
              - **CidrAllowedList** *(list) --* 
                The IP addresses allowed to make calls, in CIDR format.
                - *(string) --* 
              - **Disabled** *(boolean) --* 
                When termination settings are disabled, outbound calls can not be made.
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
        :rtype: dict
        :returns:
        """
        pass

    def get_voice_connector_termination_health(self, VoiceConnectorId: str) -> Dict:
        """
        Retrieves information about the last time a SIP ``OPTIONS`` ping was received from your SIP infrastructure for the specified Amazon Chime Voice Connector.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetVoiceConnectorTerminationHealth>`_
        
        **Request Syntax**
        ::
          response = client.get_voice_connector_termination_health(
              VoiceConnectorId='string'
          )
        
        **Response Syntax**
        ::
            {
                'TerminationHealth': {
                    'Timestamp': datetime(2015, 1, 1),
                    'Source': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TerminationHealth** *(dict) --* 
              The termination health details.
              - **Timestamp** *(datetime) --* 
                The timestamp, in ISO 8601 format.
              - **Source** *(string) --* 
                The source IP address.
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
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

    def invite_users(self, AccountId: str, UserEmailList: List) -> Dict:
        """
        Sends email invites to as many as 50 users, inviting them to the specified Amazon Chime ``Team`` account. Only ``Team`` account types are currently supported for this action. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/InviteUsers>`_
        
        **Request Syntax**
        ::
          response = client.invite_users(
              AccountId='string',
              UserEmailList=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'Invites': [
                    {
                        'InviteId': 'string',
                        'Status': 'Pending'|'Accepted'|'Failed',
                        'EmailAddress': 'string',
                        'EmailStatus': 'NotSent'|'Sent'|'Failed'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Invites** *(list) --* 
              The invite details.
              - *(dict) --* 
                Invitation object returned after emailing users to invite them to join the Amazon Chime ``Team`` account.
                - **InviteId** *(string) --* 
                  The invite ID.
                - **Status** *(string) --* 
                  The status of the invite.
                - **EmailAddress** *(string) --* 
                  The email address to which the invite is sent.
                - **EmailStatus** *(string) --* 
                  The status of the invite email.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type UserEmailList: list
        :param UserEmailList: **[REQUIRED]**
          The user email addresses to which to send the invite.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def list_accounts(self, Name: str = None, UserEmail: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Lists the Amazon Chime accounts under the administrator's AWS account. You can filter accounts by account name prefix. To find out which Amazon Chime account a user belongs to, you can filter by the user's email address, which returns one account result.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListAccounts>`_
        
        **Request Syntax**
        ::
          response = client.list_accounts(
              Name='string',
              UserEmail='string',
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'Accounts': [
                    {
                        'AwsAccountId': 'string',
                        'AccountId': 'string',
                        'Name': 'string',
                        'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
                        'SupportedLicenses': [
                            'Basic'|'Plus'|'Pro'|'ProTrial',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Accounts** *(list) --* 
              List of Amazon Chime accounts and account details.
              - *(dict) --* 
                The Amazon Chime account details. An AWS account can have multiple Amazon Chime accounts.
                - **AwsAccountId** *(string) --* 
                  The AWS account ID.
                - **AccountId** *(string) --* 
                  The Amazon Chime account ID.
                - **Name** *(string) --* 
                  The Amazon Chime account name.
                - **AccountType** *(string) --* 
                  The Amazon Chime account type. For more information about different account types, see `Managing Your Amazon Chime Accounts <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon Chime Administration Guide* .
                - **CreatedTimestamp** *(datetime) --* 
                  The Amazon Chime account creation timestamp, in ISO 8601 format.
                - **DefaultLicense** *(string) --* 
                  The default license for the Amazon Chime account.
                - **SupportedLicenses** *(list) --* 
                  Supported licenses for the Amazon Chime account.
                  - *(string) --* 
            - **NextToken** *(string) --* 
              The token to use to retrieve the next page of results.
        :type Name: string
        :param Name:
          Amazon Chime account name prefix with which to filter results.
        :type UserEmail: string
        :param UserEmail:
          User email address with which to filter results.
        :type NextToken: string
        :param NextToken:
          The token to use to retrieve the next page of results.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return in a single call. Defaults to 100.
        :rtype: dict
        :returns:
        """
        pass

    def list_phone_number_orders(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Lists the phone number orders for the administrator's Amazon Chime account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListPhoneNumberOrders>`_
        
        **Request Syntax**
        ::
          response = client.list_phone_number_orders(
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'PhoneNumberOrders': [
                    {
                        'PhoneNumberOrderId': 'string',
                        'ProductType': 'BusinessCalling'|'VoiceConnector',
                        'Status': 'Processing'|'Successful'|'Failed'|'Partial',
                        'OrderedPhoneNumbers': [
                            {
                                'E164PhoneNumber': 'string',
                                'Status': 'Processing'|'Acquired'|'Failed'
                            },
                        ],
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'UpdatedTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PhoneNumberOrders** *(list) --* 
              The phone number order details.
              - *(dict) --* 
                The details of a phone number order created for Amazon Chime.
                - **PhoneNumberOrderId** *(string) --* 
                  The phone number order ID.
                - **ProductType** *(string) --* 
                  The phone number order product type.
                - **Status** *(string) --* 
                  The status of the phone number order.
                - **OrderedPhoneNumbers** *(list) --* 
                  The ordered phone number details, such as the phone number in E.164 format and the phone number status.
                  - *(dict) --* 
                    A phone number for which an order has been placed.
                    - **E164PhoneNumber** *(string) --* 
                      The phone number, in E.164 format.
                    - **Status** *(string) --* 
                      The phone number status.
                - **CreatedTimestamp** *(datetime) --* 
                  The phone number order creation timestamp, in ISO 8601 format.
                - **UpdatedTimestamp** *(datetime) --* 
                  The updated phone number order timestamp, in ISO 8601 format.
            - **NextToken** *(string) --* 
              The token to use to retrieve the next page of results.
        :type NextToken: string
        :param NextToken:
          The token to use to retrieve the next page of results.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return in a single call.
        :rtype: dict
        :returns:
        """
        pass

    def list_phone_numbers(self, Status: str = None, ProductType: str = None, FilterName: str = None, FilterValue: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Lists the phone numbers for the specified Amazon Chime account, Amazon Chime user, or Amazon Chime Voice Connector.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListPhoneNumbers>`_
        
        **Request Syntax**
        ::
          response = client.list_phone_numbers(
              Status='AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'|'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
              ProductType='BusinessCalling'|'VoiceConnector',
              FilterName='AccountId'|'UserId'|'VoiceConnectorId',
              FilterValue='string',
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'PhoneNumbers': [
                    {
                        'PhoneNumberId': 'string',
                        'E164PhoneNumber': 'string',
                        'ProductType': 'BusinessCalling'|'VoiceConnector',
                        'Status': 'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'|'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
                        'Capabilities': {
                            'InboundCall': True|False,
                            'OutboundCall': True|False,
                            'InboundSMS': True|False,
                            'OutboundSMS': True|False,
                            'InboundMMS': True|False,
                            'OutboundMMS': True|False
                        },
                        'Associations': [
                            {
                                'Value': 'string',
                                'Name': 'AccountId'|'UserId'|'VoiceConnectorId',
                                'AssociatedTimestamp': datetime(2015, 1, 1)
                            },
                        ],
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'UpdatedTimestamp': datetime(2015, 1, 1),
                        'DeletionTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PhoneNumbers** *(list) --* 
              The phone number details.
              - *(dict) --* 
                A phone number used for Amazon Chime Business Calling or an Amazon Chime Voice Connector.
                - **PhoneNumberId** *(string) --* 
                  The phone number ID.
                - **E164PhoneNumber** *(string) --* 
                  The phone number, in E.164 format.
                - **ProductType** *(string) --* 
                  The phone number product type.
                - **Status** *(string) --* 
                  The phone number status.
                - **Capabilities** *(dict) --* 
                  The phone number capabilities.
                  - **InboundCall** *(boolean) --* 
                    Allows or denies inbound calling for the specified phone number.
                  - **OutboundCall** *(boolean) --* 
                    Allows or denies outbound calling for the specified phone number.
                  - **InboundSMS** *(boolean) --* 
                    Allows or denies inbound SMS messaging for the specified phone number.
                  - **OutboundSMS** *(boolean) --* 
                    Allows or denies outbound SMS messaging for the specified phone number.
                  - **InboundMMS** *(boolean) --* 
                    Allows or denies inbound MMS messaging for the specified phone number.
                  - **OutboundMMS** *(boolean) --* 
                    Allows or denies outbound MMS messaging for the specified phone number.
                - **Associations** *(list) --* 
                  The phone number associations.
                  - *(dict) --* 
                    The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID, or Amazon Chime Voice Connector ID.
                    - **Value** *(string) --* 
                      Contains the ID for the entity specified in Name.
                    - **Name** *(string) --* 
                      Defines the association with an Amazon Chime account ID, user ID, or Amazon Chime Voice Connector ID.
                    - **AssociatedTimestamp** *(datetime) --* 
                      The timestamp of the phone number association, in ISO 8601 format.
                - **CreatedTimestamp** *(datetime) --* 
                  The phone number creation timestamp, in ISO 8601 format.
                - **UpdatedTimestamp** *(datetime) --* 
                  The updated phone number timestamp, in ISO 8601 format.
                - **DeletionTimestamp** *(datetime) --* 
                  The deleted phone number timestamp, in ISO 8601 format.
            - **NextToken** *(string) --* 
              The token to use to retrieve the next page of results.
        :type Status: string
        :param Status:
          The phone number status.
        :type ProductType: string
        :param ProductType:
          The phone number product type.
        :type FilterName: string
        :param FilterName:
          The filter to use to limit the number of results.
        :type FilterValue: string
        :param FilterValue:
          The value to use for the filter.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return in a single call.
        :type NextToken: string
        :param NextToken:
          The token to use to retrieve the next page of results.
        :rtype: dict
        :returns:
        """
        pass

    def list_users(self, AccountId: str, UserEmail: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Lists the users that belong to the specified Amazon Chime account. You can specify an email address to list only the user that the email address belongs to.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListUsers>`_
        
        **Request Syntax**
        ::
          response = client.list_users(
              AccountId='string',
              UserEmail='string',
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Users': [
                    {
                        'UserId': 'string',
                        'AccountId': 'string',
                        'PrimaryEmail': 'string',
                        'PrimaryProvisionedNumber': 'string',
                        'DisplayName': 'string',
                        'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
                        'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
                        'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
                        'RegisteredOn': datetime(2015, 1, 1),
                        'InvitedOn': datetime(2015, 1, 1),
                        'PersonalPIN': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Users** *(list) --* 
              List of users and user details.
              - *(dict) --* 
                The user on the Amazon Chime account.
                - **UserId** *(string) --* 
                  The user ID.
                - **AccountId** *(string) --* 
                  The Amazon Chime account ID.
                - **PrimaryEmail** *(string) --* 
                  The primary email address of the user.
                - **PrimaryProvisionedNumber** *(string) --* 
                  The primary phone number associated with the user.
                - **DisplayName** *(string) --* 
                  The display name of the user.
                - **LicenseType** *(string) --* 
                  The license type for the user.
                - **UserRegistrationStatus** *(string) --* 
                  The user registration status.
                - **UserInvitationStatus** *(string) --* 
                  The user invite status.
                - **RegisteredOn** *(datetime) --* 
                  Date and time when the user is registered, in ISO 8601 format.
                - **InvitedOn** *(datetime) --* 
                  Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.
                - **PersonalPIN** *(string) --* 
                  The user's personal meeting PIN.
            - **NextToken** *(string) --* 
              The token to use to retrieve the next page of results.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type UserEmail: string
        :param UserEmail:
          Optional. The user email address used to filter results. Maximum 1.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return in a single call. Defaults to 100.
        :type NextToken: string
        :param NextToken:
          The token to use to retrieve the next page of results.
        :rtype: dict
        :returns:
        """
        pass

    def list_voice_connector_termination_credentials(self, VoiceConnectorId: str) -> Dict:
        """
        Lists the SIP credentials for the specified Amazon Chime Voice Connector.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListVoiceConnectorTerminationCredentials>`_
        
        **Request Syntax**
        ::
          response = client.list_voice_connector_termination_credentials(
              VoiceConnectorId='string'
          )
        
        **Response Syntax**
        ::
            {
                'Usernames': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Usernames** *(list) --* 
              A list of user names.
              - *(string) --* 
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
        :rtype: dict
        :returns:
        """
        pass

    def list_voice_connectors(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Lists the Amazon Chime Voice Connectors for the administrator's AWS account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListVoiceConnectors>`_
        
        **Request Syntax**
        ::
          response = client.list_voice_connectors(
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'VoiceConnectors': [
                    {
                        'VoiceConnectorId': 'string',
                        'Name': 'string',
                        'OutboundHostName': 'string',
                        'RequireEncryption': True|False,
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'UpdatedTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **VoiceConnectors** *(list) --* 
              The details of the Amazon Chime Voice Connectors.
              - *(dict) --* 
                The Amazon Chime Voice Connector configuration, including outbound host name and encryption settings.
                - **VoiceConnectorId** *(string) --* 
                  The Amazon Chime Voice Connector ID.
                - **Name** *(string) --* 
                  The name of the Amazon Chime Voice Connector.
                - **OutboundHostName** *(string) --* 
                  The outbound host name for the Amazon Chime Voice Connector.
                - **RequireEncryption** *(boolean) --* 
                  Designates whether encryption is required for the Amazon Chime Voice Connector.
                - **CreatedTimestamp** *(datetime) --* 
                  The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.
                - **UpdatedTimestamp** *(datetime) --* 
                  The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.
            - **NextToken** *(string) --* 
              The token to use to retrieve the next page of results.
        :type NextToken: string
        :param NextToken:
          The token to use to retrieve the next page of results.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return in a single call.
        :rtype: dict
        :returns:
        """
        pass

    def logout_user(self, AccountId: str, UserId: str) -> Dict:
        """
        Logs out the specified user from all of the devices they are currently logged into.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/LogoutUser>`_
        
        **Request Syntax**
        ::
          response = client.logout_user(
              AccountId='string',
              UserId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type UserId: string
        :param UserId: **[REQUIRED]**
          The user ID.
        :rtype: dict
        :returns:
        """
        pass

    def put_voice_connector_origination(self, VoiceConnectorId: str, Origination: Dict) -> Dict:
        """
        Adds origination settings for the specified Amazon Chime Voice Connector.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/PutVoiceConnectorOrigination>`_
        
        **Request Syntax**
        ::
          response = client.put_voice_connector_origination(
              VoiceConnectorId='string',
              Origination={
                  'Routes': [
                      {
                          'Host': 'string',
                          'Port': 123,
                          'Protocol': 'TCP'|'UDP',
                          'Priority': 123,
                          'Weight': 123
                      },
                  ],
                  'Disabled': True|False
              }
          )
        
        **Response Syntax**
        ::
            {
                'Origination': {
                    'Routes': [
                        {
                            'Host': 'string',
                            'Port': 123,
                            'Protocol': 'TCP'|'UDP',
                            'Priority': 123,
                            'Weight': 123
                        },
                    ],
                    'Disabled': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Origination** *(dict) --* 
              The updated origination setting details.
              - **Routes** *(list) --* 
                The call distribution properties defined for your SIP hosts. Valid range: Minimum value of 1. Maximum value of 20.
                - *(dict) --* 
                  Origination routes define call distribution properties for your SIP hosts to receive inbound calls using your Amazon Chime Voice Connector. Limit: 10 origination routes per Amazon Chime Voice Connector.
                  - **Host** *(string) --* 
                    The FODN or IP address to contact for origination traffic.
                  - **Port** *(integer) --* 
                    The designated origination route port. Defaults to 5060.
                  - **Protocol** *(string) --* 
                    The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice Connectors use TCP protocol by default.
                  - **Priority** *(integer) --* 
                    The priority associated with the host, with 1 being the highest priority. Higher priority hosts are attempted first.
                  - **Weight** *(integer) --* 
                    The weight associated with the host. If hosts are equal in priority, calls are distributed among them based on their relative weight.
              - **Disabled** *(boolean) --* 
                When origination settings are disabled, inbound calls are not enabled for your Amazon Chime Voice Connector.
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
        :type Origination: dict
        :param Origination: **[REQUIRED]**
          The origination setting details to add.
          - **Routes** *(list) --*
            The call distribution properties defined for your SIP hosts. Valid range: Minimum value of 1. Maximum value of 20.
            - *(dict) --*
              Origination routes define call distribution properties for your SIP hosts to receive inbound calls using your Amazon Chime Voice Connector. Limit: 10 origination routes per Amazon Chime Voice Connector.
              - **Host** *(string) --*
                The FODN or IP address to contact for origination traffic.
              - **Port** *(integer) --*
                The designated origination route port. Defaults to 5060.
              - **Protocol** *(string) --*
                The protocol to use for the origination route. Encryption-enabled Amazon Chime Voice Connectors use TCP protocol by default.
              - **Priority** *(integer) --*
                The priority associated with the host, with 1 being the highest priority. Higher priority hosts are attempted first.
              - **Weight** *(integer) --*
                The weight associated with the host. If hosts are equal in priority, calls are distributed among them based on their relative weight.
          - **Disabled** *(boolean) --*
            When origination settings are disabled, inbound calls are not enabled for your Amazon Chime Voice Connector.
        :rtype: dict
        :returns:
        """
        pass

    def put_voice_connector_termination(self, VoiceConnectorId: str, Termination: Dict) -> Dict:
        """
        Adds termination settings for the specified Amazon Chime Voice Connector.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/PutVoiceConnectorTermination>`_
        
        **Request Syntax**
        ::
          response = client.put_voice_connector_termination(
              VoiceConnectorId='string',
              Termination={
                  'CpsLimit': 123,
                  'DefaultPhoneNumber': 'string',
                  'CallingRegions': [
                      'string',
                  ],
                  'CidrAllowedList': [
                      'string',
                  ],
                  'Disabled': True|False
              }
          )
        
        **Response Syntax**
        ::
            {
                'Termination': {
                    'CpsLimit': 123,
                    'DefaultPhoneNumber': 'string',
                    'CallingRegions': [
                        'string',
                    ],
                    'CidrAllowedList': [
                        'string',
                    ],
                    'Disabled': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Termination** *(dict) --* 
              The updated termination setting details.
              - **CpsLimit** *(integer) --* 
                The limit on calls per second. Max value based on account service limit. Default value of 1.
              - **DefaultPhoneNumber** *(string) --* 
                The default caller ID phone number.
              - **CallingRegions** *(list) --* 
                The countries to which calls are allowed.
                - *(string) --* 
              - **CidrAllowedList** *(list) --* 
                The IP addresses allowed to make calls, in CIDR format.
                - *(string) --* 
              - **Disabled** *(boolean) --* 
                When termination settings are disabled, outbound calls can not be made.
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
        :type Termination: dict
        :param Termination: **[REQUIRED]**
          The termination setting details to add.
          - **CpsLimit** *(integer) --*
            The limit on calls per second. Max value based on account service limit. Default value of 1.
          - **DefaultPhoneNumber** *(string) --*
            The default caller ID phone number.
          - **CallingRegions** *(list) --*
            The countries to which calls are allowed.
            - *(string) --*
          - **CidrAllowedList** *(list) --*
            The IP addresses allowed to make calls, in CIDR format.
            - *(string) --*
          - **Disabled** *(boolean) --*
            When termination settings are disabled, outbound calls can not be made.
        :rtype: dict
        :returns:
        """
        pass

    def put_voice_connector_termination_credentials(self, VoiceConnectorId: str, Credentials: List = None):
        """
        Adds termination SIP credentials for the specified Amazon Chime Voice Connector.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/PutVoiceConnectorTerminationCredentials>`_
        
        **Request Syntax**
        ::
          response = client.put_voice_connector_termination_credentials(
              VoiceConnectorId='string',
              Credentials=[
                  {
                      'Username': 'string',
                      'Password': 'string'
                  },
              ]
          )
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
        :type Credentials: list
        :param Credentials:
          The termination SIP credentials.
          - *(dict) --*
            The SIP credentials used to authenticate requests to your Amazon Chime Voice Connector.
            - **Username** *(string) --*
              The RFC2617 compliant user name associated with the SIP credentials, in US-ASCII format.
            - **Password** *(string) --*
              The RFC2617 compliant password associated with the SIP credentials, in US-ASCII format.
        :returns: None
        """
        pass

    def reset_personal_pin(self, AccountId: str, UserId: str) -> Dict:
        """
        Resets the personal meeting PIN for the specified user on an Amazon Chime account. Returns the  User object with the updated personal meeting PIN.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ResetPersonalPIN>`_
        
        **Request Syntax**
        ::
          response = client.reset_personal_pin(
              AccountId='string',
              UserId='string'
          )
        
        **Response Syntax**
        ::
            {
                'User': {
                    'UserId': 'string',
                    'AccountId': 'string',
                    'PrimaryEmail': 'string',
                    'PrimaryProvisionedNumber': 'string',
                    'DisplayName': 'string',
                    'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
                    'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
                    'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
                    'RegisteredOn': datetime(2015, 1, 1),
                    'InvitedOn': datetime(2015, 1, 1),
                    'PersonalPIN': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **User** *(dict) --* 
              The user details and new personal meeting PIN.
              - **UserId** *(string) --* 
                The user ID.
              - **AccountId** *(string) --* 
                The Amazon Chime account ID.
              - **PrimaryEmail** *(string) --* 
                The primary email address of the user.
              - **PrimaryProvisionedNumber** *(string) --* 
                The primary phone number associated with the user.
              - **DisplayName** *(string) --* 
                The display name of the user.
              - **LicenseType** *(string) --* 
                The license type for the user.
              - **UserRegistrationStatus** *(string) --* 
                The user registration status.
              - **UserInvitationStatus** *(string) --* 
                The user invite status.
              - **RegisteredOn** *(datetime) --* 
                Date and time when the user is registered, in ISO 8601 format.
              - **InvitedOn** *(datetime) --* 
                Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.
              - **PersonalPIN** *(string) --* 
                The user's personal meeting PIN.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type UserId: string
        :param UserId: **[REQUIRED]**
          The user ID.
        :rtype: dict
        :returns:
        """
        pass

    def restore_phone_number(self, PhoneNumberId: str) -> Dict:
        """
        Moves a phone number from the **Deletion queue** back into the phone number **Inventory** .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/RestorePhoneNumber>`_
        
        **Request Syntax**
        ::
          response = client.restore_phone_number(
              PhoneNumberId='string'
          )
        
        **Response Syntax**
        ::
            {
                'PhoneNumber': {
                    'PhoneNumberId': 'string',
                    'E164PhoneNumber': 'string',
                    'ProductType': 'BusinessCalling'|'VoiceConnector',
                    'Status': 'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'|'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
                    'Capabilities': {
                        'InboundCall': True|False,
                        'OutboundCall': True|False,
                        'InboundSMS': True|False,
                        'OutboundSMS': True|False,
                        'InboundMMS': True|False,
                        'OutboundMMS': True|False
                    },
                    'Associations': [
                        {
                            'Value': 'string',
                            'Name': 'AccountId'|'UserId'|'VoiceConnectorId',
                            'AssociatedTimestamp': datetime(2015, 1, 1)
                        },
                    ],
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1),
                    'DeletionTimestamp': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PhoneNumber** *(dict) --* 
              The phone number details.
              - **PhoneNumberId** *(string) --* 
                The phone number ID.
              - **E164PhoneNumber** *(string) --* 
                The phone number, in E.164 format.
              - **ProductType** *(string) --* 
                The phone number product type.
              - **Status** *(string) --* 
                The phone number status.
              - **Capabilities** *(dict) --* 
                The phone number capabilities.
                - **InboundCall** *(boolean) --* 
                  Allows or denies inbound calling for the specified phone number.
                - **OutboundCall** *(boolean) --* 
                  Allows or denies outbound calling for the specified phone number.
                - **InboundSMS** *(boolean) --* 
                  Allows or denies inbound SMS messaging for the specified phone number.
                - **OutboundSMS** *(boolean) --* 
                  Allows or denies outbound SMS messaging for the specified phone number.
                - **InboundMMS** *(boolean) --* 
                  Allows or denies inbound MMS messaging for the specified phone number.
                - **OutboundMMS** *(boolean) --* 
                  Allows or denies outbound MMS messaging for the specified phone number.
              - **Associations** *(list) --* 
                The phone number associations.
                - *(dict) --* 
                  The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID, or Amazon Chime Voice Connector ID.
                  - **Value** *(string) --* 
                    Contains the ID for the entity specified in Name.
                  - **Name** *(string) --* 
                    Defines the association with an Amazon Chime account ID, user ID, or Amazon Chime Voice Connector ID.
                  - **AssociatedTimestamp** *(datetime) --* 
                    The timestamp of the phone number association, in ISO 8601 format.
              - **CreatedTimestamp** *(datetime) --* 
                The phone number creation timestamp, in ISO 8601 format.
              - **UpdatedTimestamp** *(datetime) --* 
                The updated phone number timestamp, in ISO 8601 format.
              - **DeletionTimestamp** *(datetime) --* 
                The deleted phone number timestamp, in ISO 8601 format.
        :type PhoneNumberId: string
        :param PhoneNumberId: **[REQUIRED]**
          The phone number.
        :rtype: dict
        :returns:
        """
        pass

    def search_available_phone_numbers(self, AreaCode: str = None, City: str = None, Country: str = None, State: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Searches phone numbers that can be ordered.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/SearchAvailablePhoneNumbers>`_
        
        **Request Syntax**
        ::
          response = client.search_available_phone_numbers(
              AreaCode='string',
              City='string',
              Country='string',
              State='string',
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'E164PhoneNumbers': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **E164PhoneNumbers** *(list) --* 
              List of phone numbers, in E.164 format.
              - *(string) --* 
        :type AreaCode: string
        :param AreaCode:
          The area code used to filter results.
        :type City: string
        :param City:
          The city used to filter results.
        :type Country: string
        :param Country:
          The country used to filter results.
        :type State: string
        :param State:
          The state used to filter results.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return in a single call.
        :type NextToken: string
        :param NextToken:
          The token to use to retrieve the next page of results.
        :rtype: dict
        :returns:
        """
        pass

    def update_account(self, AccountId: str, Name: str = None) -> Dict:
        """
        Updates account details for the specified Amazon Chime account. Currently, only account name updates are supported for this action.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateAccount>`_
        
        **Request Syntax**
        ::
          response = client.update_account(
              AccountId='string',
              Name='string'
          )
        
        **Response Syntax**
        ::
            {
                'Account': {
                    'AwsAccountId': 'string',
                    'AccountId': 'string',
                    'Name': 'string',
                    'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
                    'SupportedLicenses': [
                        'Basic'|'Plus'|'Pro'|'ProTrial',
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Account** *(dict) --* 
              The updated Amazon Chime account details.
              - **AwsAccountId** *(string) --* 
                The AWS account ID.
              - **AccountId** *(string) --* 
                The Amazon Chime account ID.
              - **Name** *(string) --* 
                The Amazon Chime account name.
              - **AccountType** *(string) --* 
                The Amazon Chime account type. For more information about different account types, see `Managing Your Amazon Chime Accounts <https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon Chime Administration Guide* .
              - **CreatedTimestamp** *(datetime) --* 
                The Amazon Chime account creation timestamp, in ISO 8601 format.
              - **DefaultLicense** *(string) --* 
                The default license for the Amazon Chime account.
              - **SupportedLicenses** *(list) --* 
                Supported licenses for the Amazon Chime account.
                - *(string) --* 
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type Name: string
        :param Name:
          The new name for the specified Amazon Chime account.
        :rtype: dict
        :returns:
        """
        pass

    def update_account_settings(self, AccountId: str, AccountSettings: Dict) -> Dict:
        """
        Updates the settings for the specified Amazon Chime account. You can update settings for remote control of shared screens, or for the dial-out option. For more information about these settings, see `Use the Policies Page <https://docs.aws.amazon.com/chime/latest/ag/policies.html>`__ in the *Amazon Chime Administration Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateAccountSettings>`_
        
        **Request Syntax**
        ::
          response = client.update_account_settings(
              AccountId='string',
              AccountSettings={
                  'DisableRemoteControl': True|False,
                  'EnableDialOut': True|False
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type AccountSettings: dict
        :param AccountSettings: **[REQUIRED]**
          The Amazon Chime account settings to update.
          - **DisableRemoteControl** *(boolean) --*
            Setting that stops or starts remote control of shared screens during meetings.
          - **EnableDialOut** *(boolean) --*
            Setting that allows meeting participants to choose the **Call me at a phone number** option. For more information, see `Join a Meeting without the Amazon Chime App <https://docs.aws.amazon.com/chime/latest/ug/chime-join-meeting.html>`__ .
        :rtype: dict
        :returns:
        """
        pass

    def update_global_settings(self, BusinessCalling: Dict, VoiceConnector: Dict):
        """
        Updates global settings for the administrator's AWS account, such as Amazon Chime Business Calling and Amazon Chime Voice Connector settings.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateGlobalSettings>`_
        
        **Request Syntax**
        ::
          response = client.update_global_settings(
              BusinessCalling={
                  'CdrBucket': 'string'
              },
              VoiceConnector={
                  'CdrBucket': 'string'
              }
          )
        :type BusinessCalling: dict
        :param BusinessCalling: **[REQUIRED]**
          The Amazon Chime Business Calling settings.
          - **CdrBucket** *(string) --*
            The Amazon S3 bucket designated for call detail record storage.
        :type VoiceConnector: dict
        :param VoiceConnector: **[REQUIRED]**
          The Amazon Chime Voice Connector settings.
          - **CdrBucket** *(string) --*
            The Amazon S3 bucket designated for call detail record storage.
        :returns: None
        """
        pass

    def update_phone_number(self, PhoneNumberId: str, ProductType: str = None) -> Dict:
        """
        Updates phone number details, such as product type, for the specified phone number ID.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdatePhoneNumber>`_
        
        **Request Syntax**
        ::
          response = client.update_phone_number(
              PhoneNumberId='string',
              ProductType='BusinessCalling'|'VoiceConnector'
          )
        
        **Response Syntax**
        ::
            {
                'PhoneNumber': {
                    'PhoneNumberId': 'string',
                    'E164PhoneNumber': 'string',
                    'ProductType': 'BusinessCalling'|'VoiceConnector',
                    'Status': 'AcquireInProgress'|'AcquireFailed'|'Unassigned'|'Assigned'|'ReleaseInProgress'|'DeleteInProgress'|'ReleaseFailed'|'DeleteFailed',
                    'Capabilities': {
                        'InboundCall': True|False,
                        'OutboundCall': True|False,
                        'InboundSMS': True|False,
                        'OutboundSMS': True|False,
                        'InboundMMS': True|False,
                        'OutboundMMS': True|False
                    },
                    'Associations': [
                        {
                            'Value': 'string',
                            'Name': 'AccountId'|'UserId'|'VoiceConnectorId',
                            'AssociatedTimestamp': datetime(2015, 1, 1)
                        },
                    ],
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1),
                    'DeletionTimestamp': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PhoneNumber** *(dict) --* 
              The updated phone number details.
              - **PhoneNumberId** *(string) --* 
                The phone number ID.
              - **E164PhoneNumber** *(string) --* 
                The phone number, in E.164 format.
              - **ProductType** *(string) --* 
                The phone number product type.
              - **Status** *(string) --* 
                The phone number status.
              - **Capabilities** *(dict) --* 
                The phone number capabilities.
                - **InboundCall** *(boolean) --* 
                  Allows or denies inbound calling for the specified phone number.
                - **OutboundCall** *(boolean) --* 
                  Allows or denies outbound calling for the specified phone number.
                - **InboundSMS** *(boolean) --* 
                  Allows or denies inbound SMS messaging for the specified phone number.
                - **OutboundSMS** *(boolean) --* 
                  Allows or denies outbound SMS messaging for the specified phone number.
                - **InboundMMS** *(boolean) --* 
                  Allows or denies inbound MMS messaging for the specified phone number.
                - **OutboundMMS** *(boolean) --* 
                  Allows or denies outbound MMS messaging for the specified phone number.
              - **Associations** *(list) --* 
                The phone number associations.
                - *(dict) --* 
                  The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID, or Amazon Chime Voice Connector ID.
                  - **Value** *(string) --* 
                    Contains the ID for the entity specified in Name.
                  - **Name** *(string) --* 
                    Defines the association with an Amazon Chime account ID, user ID, or Amazon Chime Voice Connector ID.
                  - **AssociatedTimestamp** *(datetime) --* 
                    The timestamp of the phone number association, in ISO 8601 format.
              - **CreatedTimestamp** *(datetime) --* 
                The phone number creation timestamp, in ISO 8601 format.
              - **UpdatedTimestamp** *(datetime) --* 
                The updated phone number timestamp, in ISO 8601 format.
              - **DeletionTimestamp** *(datetime) --* 
                The deleted phone number timestamp, in ISO 8601 format.
        :type PhoneNumberId: string
        :param PhoneNumberId: **[REQUIRED]**
          The phone number ID.
        :type ProductType: string
        :param ProductType:
          The product type.
        :rtype: dict
        :returns:
        """
        pass

    def update_user(self, AccountId: str, UserId: str, LicenseType: str = None) -> Dict:
        """
        Updates user details for a specified user ID. Currently, only ``LicenseType`` updates are supported for this action.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateUser>`_
        
        **Request Syntax**
        ::
          response = client.update_user(
              AccountId='string',
              UserId='string',
              LicenseType='Basic'|'Plus'|'Pro'|'ProTrial'
          )
        
        **Response Syntax**
        ::
            {
                'User': {
                    'UserId': 'string',
                    'AccountId': 'string',
                    'PrimaryEmail': 'string',
                    'PrimaryProvisionedNumber': 'string',
                    'DisplayName': 'string',
                    'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
                    'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
                    'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
                    'RegisteredOn': datetime(2015, 1, 1),
                    'InvitedOn': datetime(2015, 1, 1),
                    'PersonalPIN': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **User** *(dict) --* 
              The updated user details.
              - **UserId** *(string) --* 
                The user ID.
              - **AccountId** *(string) --* 
                The Amazon Chime account ID.
              - **PrimaryEmail** *(string) --* 
                The primary email address of the user.
              - **PrimaryProvisionedNumber** *(string) --* 
                The primary phone number associated with the user.
              - **DisplayName** *(string) --* 
                The display name of the user.
              - **LicenseType** *(string) --* 
                The license type for the user.
              - **UserRegistrationStatus** *(string) --* 
                The user registration status.
              - **UserInvitationStatus** *(string) --* 
                The user invite status.
              - **RegisteredOn** *(datetime) --* 
                Date and time when the user is registered, in ISO 8601 format.
              - **InvitedOn** *(datetime) --* 
                Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.
              - **PersonalPIN** *(string) --* 
                The user's personal meeting PIN.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type UserId: string
        :param UserId: **[REQUIRED]**
          The user ID.
        :type LicenseType: string
        :param LicenseType:
          The user license type to update. This must be a supported license type for the Amazon Chime account that the user belongs to.
        :rtype: dict
        :returns:
        """
        pass

    def update_user_settings(self, AccountId: str, UserId: str, UserSettings: Dict):
        """
        Updates the settings for the specified user, such as phone number settings.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateUserSettings>`_
        
        **Request Syntax**
        ::
          response = client.update_user_settings(
              AccountId='string',
              UserId='string',
              UserSettings={
                  'Telephony': {
                      'InboundCalling': True|False,
                      'OutboundCalling': True|False,
                      'SMS': True|False
                  }
              }
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type UserId: string
        :param UserId: **[REQUIRED]**
          The user ID.
        :type UserSettings: dict
        :param UserSettings: **[REQUIRED]**
          The user settings to update.
          - **Telephony** *(dict) --* **[REQUIRED]**
            The telephony settings associated with the user.
            - **InboundCalling** *(boolean) --* **[REQUIRED]**
              Allows or denies inbound calling.
            - **OutboundCalling** *(boolean) --* **[REQUIRED]**
              Allows or denies outbound calling.
            - **SMS** *(boolean) --* **[REQUIRED]**
              Allows or denies SMS messaging.
        :returns: None
        """
        pass

    def update_voice_connector(self, VoiceConnectorId: str, Name: str, RequireEncryption: bool) -> Dict:
        """
        Updates details for the specified Amazon Chime Voice Connector.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateVoiceConnector>`_
        
        **Request Syntax**
        ::
          response = client.update_voice_connector(
              VoiceConnectorId='string',
              Name='string',
              RequireEncryption=True|False
          )
        
        **Response Syntax**
        ::
            {
                'VoiceConnector': {
                    'VoiceConnectorId': 'string',
                    'Name': 'string',
                    'OutboundHostName': 'string',
                    'RequireEncryption': True|False,
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'UpdatedTimestamp': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **VoiceConnector** *(dict) --* 
              The Amazon Chime Voice Connector details.
              - **VoiceConnectorId** *(string) --* 
                The Amazon Chime Voice Connector ID.
              - **Name** *(string) --* 
                The name of the Amazon Chime Voice Connector.
              - **OutboundHostName** *(string) --* 
                The outbound host name for the Amazon Chime Voice Connector.
              - **RequireEncryption** *(boolean) --* 
                Designates whether encryption is required for the Amazon Chime Voice Connector.
              - **CreatedTimestamp** *(datetime) --* 
                The Amazon Chime Voice Connector creation timestamp, in ISO 8601 format.
              - **UpdatedTimestamp** *(datetime) --* 
                The updated Amazon Chime Voice Connector timestamp, in ISO 8601 format.
        :type VoiceConnectorId: string
        :param VoiceConnectorId: **[REQUIRED]**
          The Amazon Chime Voice Connector ID.
        :type Name: string
        :param Name: **[REQUIRED]**
          The name of the Amazon Chime Voice Connector.
        :type RequireEncryption: boolean
        :param RequireEncryption: **[REQUIRED]**
          When enabled, requires encryption for the Amazon Chime Voice Connector.
        :rtype: dict
        :returns:
        """
        pass
