from typing import Dict
from botocore.paginate import Paginator


class ListAccounts(Paginator):
    def paginate(self, Name: str = None, UserEmail: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Chime.Client.list_accounts`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListAccounts>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Name='string',
              UserEmail='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
        :type Name: string
        :param Name:
          Amazon Chime account name prefix with which to filter results.
        :type UserEmail: string
        :param UserEmail:
          User email address with which to filter results.
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


class ListUsers(Paginator):
    def paginate(self, AccountId: str, UserEmail: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Chime.Client.list_users`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/ListUsers>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AccountId='string',
              UserEmail='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Amazon Chime account ID.
        :type UserEmail: string
        :param UserEmail:
          Optional. The user email address used to filter results. Maximum 1.
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
