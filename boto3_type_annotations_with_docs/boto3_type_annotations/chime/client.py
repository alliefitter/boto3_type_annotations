from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def batch_suspend_user(self, AccountId: str, UserIdList: List) -> Dict:
        """
        
        Users suspended from a ``Team`` account are dissociated from the account, but they can continue to use Amazon Chime as free users. To remove the suspension from suspended ``Team`` account users, invite them to the ``Team`` account again. You can use the  InviteUsers action to do so.
        
        Users suspended from an ``EnterpriseLWA`` account are immediately signed out of Amazon Chime and are no longer able to sign in. To remove the suspension from suspended ``EnterpriseLWA`` account users, use the  BatchUnsuspendUser action. 
        
        To sign out users without suspending them, use the  LogoutUser action.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/BatchSuspendUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_suspend_user(
              AccountId=\'string\',
              UserIdList=[
                  \'string\',
              ]
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]** 
        
          The Amazon Chime account ID.
        
        :type UserIdList: list
        :param UserIdList: **[REQUIRED]** 
        
          The request containing the user IDs to suspend.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UserErrors\': [
                    {
                        \'UserId\': \'string\',
                        \'ErrorCode\': \'Unauthorized\'|\'Forbidden\'|\'NotFound\'|\'BadRequest\'|\'Conflict\'|\'ServiceFailure\'|\'ServiceUnavailable\'|\'Unprocessable\'|\'Throttled\'|\'PreconditionFailed\',
                        \'ErrorMessage\': \'string\'
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
        
        """
        pass

    def batch_unsuspend_user(self, AccountId: str, UserIdList: List) -> Dict:
        """
        
        Previously suspended users who are unsuspended using this action are returned to ``Registered`` status. Users who are not previously suspended are ignored.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/BatchUnsuspendUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_unsuspend_user(
              AccountId=\'string\',
              UserIdList=[
                  \'string\',
              ]
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]** 
        
          The Amazon Chime account ID.
        
        :type UserIdList: list
        :param UserIdList: **[REQUIRED]** 
        
          The request containing the user IDs to unsuspend.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UserErrors\': [
                    {
                        \'UserId\': \'string\',
                        \'ErrorCode\': \'Unauthorized\'|\'Forbidden\'|\'NotFound\'|\'BadRequest\'|\'Conflict\'|\'ServiceFailure\'|\'ServiceUnavailable\'|\'Unprocessable\'|\'Throttled\'|\'PreconditionFailed\',
                        \'ErrorMessage\': \'string\'
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
        
        """
        pass

    def batch_update_user(self, AccountId: str, UpdateUserRequestItems: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/BatchUpdateUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_update_user(
              AccountId=\'string\',
              UpdateUserRequestItems=[
                  {
                      \'UserId\': \'string\',
                      \'LicenseType\': \'Basic\'|\'Plus\'|\'Pro\'|\'ProTrial\'
                  },
              ]
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'UserErrors\': [
                    {
                        \'UserId\': \'string\',
                        \'ErrorCode\': \'Unauthorized\'|\'Forbidden\'|\'NotFound\'|\'BadRequest\'|\'Conflict\'|\'ServiceFailure\'|\'ServiceUnavailable\'|\'Unprocessable\'|\'Throttled\'|\'PreconditionFailed\',
                        \'ErrorMessage\': \'string\'
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

    def create_account(self, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/CreateAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_account(
              Name=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the Amazon Chime account.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Account\': {
                    \'AwsAccountId\': \'string\',
                    \'AccountId\': \'string\',
                    \'Name\': \'string\',
                    \'AccountType\': \'Team\'|\'EnterpriseDirectory\'|\'EnterpriseLWA\'|\'EnterpriseOIDC\',
                    \'CreatedTimestamp\': datetime(2015, 1, 1),
                    \'DefaultLicense\': \'Basic\'|\'Plus\'|\'Pro\'|\'ProTrial\',
                    \'SupportedLicenses\': [
                        \'Basic\'|\'Plus\'|\'Pro\'|\'ProTrial\',
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
        
                The Amazon Chime account type. For more information about different account types, see `Managing Your Amazon Chime Accounts <http://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon Chime Administration Guide* .
        
              - **CreatedTimestamp** *(datetime) --* 
        
                The Amazon Chime account creation timestamp, in ISO 8601 format.
        
              - **DefaultLicense** *(string) --* 
        
                The default license for the Amazon Chime account.
        
              - **SupportedLicenses** *(list) --* 
        
                Supported licenses for the Amazon Chime account.
        
                - *(string) --* 
            
        """
        pass

    def delete_account(self, AccountId: str) -> Dict:
        """
        
        For ``EnterpriseLWA`` and ``EnterpriseAD`` accounts, you must release the claimed domains for your Amazon Chime account before deletion. As soon as you release the domain, all users under that account are suspended.
        
        Deleted accounts appear in your ``Disabled`` accounts list for 90 days. To restore a deleted account from your ``Disabled`` accounts list, you must contact AWS Support.
        
        After 90 days, deleted accounts are permanently removed from your ``Disabled`` accounts list.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/DeleteAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_account(
              AccountId=\'string\'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]** 
        
          The Amazon Chime account ID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
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

    def get_account(self, AccountId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_account(
              AccountId=\'string\'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]** 
        
          The Amazon Chime account ID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Account\': {
                    \'AwsAccountId\': \'string\',
                    \'AccountId\': \'string\',
                    \'Name\': \'string\',
                    \'AccountType\': \'Team\'|\'EnterpriseDirectory\'|\'EnterpriseLWA\'|\'EnterpriseOIDC\',
                    \'CreatedTimestamp\': datetime(2015, 1, 1),
                    \'DefaultLicense\': \'Basic\'|\'Plus\'|\'Pro\'|\'ProTrial\',
                    \'SupportedLicenses\': [
                        \'Basic\'|\'Plus\'|\'Pro\'|\'ProTrial\',
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
        
                The Amazon Chime account type. For more information about different account types, see `Managing Your Amazon Chime Accounts <http://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon Chime Administration Guide* .
        
              - **CreatedTimestamp** *(datetime) --* 
        
                The Amazon Chime account creation timestamp, in ISO 8601 format.
        
              - **DefaultLicense** *(string) --* 
        
                The default license for the Amazon Chime account.
        
              - **SupportedLicenses** *(list) --* 
        
                Supported licenses for the Amazon Chime account.
        
                - *(string) --* 
            
        """
        pass

    def get_account_settings(self, AccountId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetAccountSettings>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_account_settings(
              AccountId=\'string\'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]** 
        
          The Amazon Chime account ID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AccountSettings\': {
                    \'DisableRemoteControl\': True|False,
                    \'EnableDialOut\': True|False
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AccountSettings** *(dict) --* 
        
              The Amazon Chime account settings.
        
              - **DisableRemoteControl** *(boolean) --* 
        
                Setting that stops or starts remote control of shared screens during meetings.
        
              - **EnableDialOut** *(boolean) --* 
        
                Setting that allows meeting participants to choose the **Call me at a phone number** option. For more information, see `Join a Meeting without the Amazon Chime App <http://docs.aws.amazon.com/chime/latest/ug/chime-join-meeting.html>`__ .
        
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

    def get_user(self, AccountId: str, UserId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/GetUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_user(
              AccountId=\'string\',
              UserId=\'string\'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]** 
        
          The Amazon Chime account ID.
        
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The user ID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'User\': {
                    \'UserId\': \'string\',
                    \'AccountId\': \'string\',
                    \'PrimaryEmail\': \'string\',
                    \'DisplayName\': \'string\',
                    \'LicenseType\': \'Basic\'|\'Plus\'|\'Pro\'|\'ProTrial\',
                    \'UserRegistrationStatus\': \'Unregistered\'|\'Registered\'|\'Suspended\',
                    \'UserInvitationStatus\': \'Pending\'|\'Accepted\'|\'Failed\',
                    \'RegisteredOn\': datetime(2015, 1, 1),
                    \'InvitedOn\': datetime(2015, 1, 1),
                    \'PersonalPIN\': \'string\'
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
        
                The user\'s personal meeting PIN.
        
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

    def invite_users(self, AccountId: str, UserEmailList: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/InviteUsers>`_
        
        **Request Syntax** 
        ::
        
          response = client.invite_users(
              AccountId=\'string\',
              UserEmailList=[
                  \'string\',
              ]
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]** 
        
          The Amazon Chime account ID.
        
        :type UserEmailList: list
        :param UserEmailList: **[REQUIRED]** 
        
          The user email addresses to which to send the invite.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Invites\': [
                    {
                        \'InviteId\': \'string\',
                        \'Status\': \'Pending\'|\'Accepted\'|\'Failed\',
                        \'EmailAddress\': \'string\',
                        \'EmailStatus\': \'NotSent\'|\'Sent\'|\'Failed\'
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
        
        """
        pass

    def list_accounts(self, Name: str = None, UserEmail: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListAccounts>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_accounts(
              Name=\'string\',
              UserEmail=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Accounts\': [
                    {
                        \'AwsAccountId\': \'string\',
                        \'AccountId\': \'string\',
                        \'Name\': \'string\',
                        \'AccountType\': \'Team\'|\'EnterpriseDirectory\'|\'EnterpriseLWA\'|\'EnterpriseOIDC\',
                        \'CreatedTimestamp\': datetime(2015, 1, 1),
                        \'DefaultLicense\': \'Basic\'|\'Plus\'|\'Pro\'|\'ProTrial\',
                        \'SupportedLicenses\': [
                            \'Basic\'|\'Plus\'|\'Pro\'|\'ProTrial\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  The Amazon Chime account type. For more information about different account types, see `Managing Your Amazon Chime Accounts <http://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon Chime Administration Guide* .
        
                - **CreatedTimestamp** *(datetime) --* 
        
                  The Amazon Chime account creation timestamp, in ISO 8601 format.
        
                - **DefaultLicense** *(string) --* 
        
                  The default license for the Amazon Chime account.
        
                - **SupportedLicenses** *(list) --* 
        
                  Supported licenses for the Amazon Chime account.
        
                  - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next page of results.
        
        """
        pass

    def list_users(self, AccountId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListUsers>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_users(
              AccountId=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]** 
        
          The Amazon Chime account ID.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. Defaults to 100.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to use to retrieve the next page of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Users\': [
                    {
                        \'UserId\': \'string\',
                        \'AccountId\': \'string\',
                        \'PrimaryEmail\': \'string\',
                        \'DisplayName\': \'string\',
                        \'LicenseType\': \'Basic\'|\'Plus\'|\'Pro\'|\'ProTrial\',
                        \'UserRegistrationStatus\': \'Unregistered\'|\'Registered\'|\'Suspended\',
                        \'UserInvitationStatus\': \'Pending\'|\'Accepted\'|\'Failed\',
                        \'RegisteredOn\': datetime(2015, 1, 1),
                        \'InvitedOn\': datetime(2015, 1, 1),
                        \'PersonalPIN\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  The user\'s personal meeting PIN.
        
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next page of results.
        
        """
        pass

    def logout_user(self, AccountId: str, UserId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/LogoutUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.logout_user(
              AccountId=\'string\',
              UserId=\'string\'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]** 
        
          The Amazon Chime account ID.
        
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The user ID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def reset_personal_pin(self, AccountId: str, UserId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ResetPersonalPIN>`_
        
        **Request Syntax** 
        ::
        
          response = client.reset_personal_pin(
              AccountId=\'string\',
              UserId=\'string\'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]** 
        
          The Amazon Chime account ID.
        
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The user ID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'User\': {
                    \'UserId\': \'string\',
                    \'AccountId\': \'string\',
                    \'PrimaryEmail\': \'string\',
                    \'DisplayName\': \'string\',
                    \'LicenseType\': \'Basic\'|\'Plus\'|\'Pro\'|\'ProTrial\',
                    \'UserRegistrationStatus\': \'Unregistered\'|\'Registered\'|\'Suspended\',
                    \'UserInvitationStatus\': \'Pending\'|\'Accepted\'|\'Failed\',
                    \'RegisteredOn\': datetime(2015, 1, 1),
                    \'InvitedOn\': datetime(2015, 1, 1),
                    \'PersonalPIN\': \'string\'
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
        
                The user\'s personal meeting PIN.
        
        """
        pass

    def update_account(self, AccountId: str, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_account(
              AccountId=\'string\',
              Name=\'string\'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]** 
        
          The Amazon Chime account ID.
        
        :type Name: string
        :param Name: 
        
          The new name for the specified Amazon Chime account.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Account\': {
                    \'AwsAccountId\': \'string\',
                    \'AccountId\': \'string\',
                    \'Name\': \'string\',
                    \'AccountType\': \'Team\'|\'EnterpriseDirectory\'|\'EnterpriseLWA\'|\'EnterpriseOIDC\',
                    \'CreatedTimestamp\': datetime(2015, 1, 1),
                    \'DefaultLicense\': \'Basic\'|\'Plus\'|\'Pro\'|\'ProTrial\',
                    \'SupportedLicenses\': [
                        \'Basic\'|\'Plus\'|\'Pro\'|\'ProTrial\',
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
        
                The Amazon Chime account type. For more information about different account types, see `Managing Your Amazon Chime Accounts <http://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html>`__ in the *Amazon Chime Administration Guide* .
        
              - **CreatedTimestamp** *(datetime) --* 
        
                The Amazon Chime account creation timestamp, in ISO 8601 format.
        
              - **DefaultLicense** *(string) --* 
        
                The default license for the Amazon Chime account.
        
              - **SupportedLicenses** *(list) --* 
        
                Supported licenses for the Amazon Chime account.
        
                - *(string) --* 
            
        """
        pass

    def update_account_settings(self, AccountId: str, AccountSettings: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateAccountSettings>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_account_settings(
              AccountId=\'string\',
              AccountSettings={
                  \'DisableRemoteControl\': True|False,
                  \'EnableDialOut\': True|False
              }
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]** 
        
          The Amazon Chime account ID.
        
        :type AccountSettings: dict
        :param AccountSettings: **[REQUIRED]** 
        
          The Amazon Chime account settings to update.
        
          - **DisableRemoteControl** *(boolean) --* 
        
            Setting that stops or starts remote control of shared screens during meetings.
        
          - **EnableDialOut** *(boolean) --* 
        
            Setting that allows meeting participants to choose the **Call me at a phone number** option. For more information, see `Join a Meeting without the Amazon Chime App <http://docs.aws.amazon.com/chime/latest/ug/chime-join-meeting.html>`__ .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_user(self, AccountId: str, UserId: str, LicenseType: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_user(
              AccountId=\'string\',
              UserId=\'string\',
              LicenseType=\'Basic\'|\'Plus\'|\'Pro\'|\'ProTrial\'
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'User\': {
                    \'UserId\': \'string\',
                    \'AccountId\': \'string\',
                    \'PrimaryEmail\': \'string\',
                    \'DisplayName\': \'string\',
                    \'LicenseType\': \'Basic\'|\'Plus\'|\'Pro\'|\'ProTrial\',
                    \'UserRegistrationStatus\': \'Unregistered\'|\'Registered\'|\'Suspended\',
                    \'UserInvitationStatus\': \'Pending\'|\'Accepted\'|\'Failed\',
                    \'RegisteredOn\': datetime(2015, 1, 1),
                    \'InvitedOn\': datetime(2015, 1, 1),
                    \'PersonalPIN\': \'string\'
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
        
                The user\'s personal meeting PIN.
        
        """
        pass
