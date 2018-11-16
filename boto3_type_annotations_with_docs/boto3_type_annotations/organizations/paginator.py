from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListAWSServiceAccessForOrganization(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListAWSServiceAccessForOrganization>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'EnabledServicePrincipals\': [
                    {
                        \'ServicePrincipal\': \'string\',
                        \'DateEnabled\': datetime(2015, 1, 1)
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **EnabledServicePrincipals** *(list) --* 
        
              A list of the service principals for the services that are enabled to integrate with your organization. Each principal is a structure that includes the name and the date that it was enabled for integration with AWS Organizations.
        
              - *(dict) --* 
        
                A structure that contains details of a service principal that is enabled to integrate with AWS Organizations.
        
                - **ServicePrincipal** *(string) --* 
        
                  The name of the service principal. This is typically in the form of a URL, such as: `` *servicename* .amazonaws.com`` .
        
                - **DateEnabled** *(datetime) --* 
        
                  The date that the service principal was enabled for integration with AWS Organizations.
        
        """
        pass


class ListAccounts(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListAccounts>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Accounts\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Email\': \'string\',
                        \'Name\': \'string\',
                        \'Status\': \'ACTIVE\'|\'SUSPENDED\',
                        \'JoinedMethod\': \'INVITED\'|\'CREATED\',
                        \'JoinedTimestamp\': datetime(2015, 1, 1)
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Accounts** *(list) --* 
        
              A list of objects in the organization.
        
              - *(dict) --* 
        
                Contains information about an AWS account that is a member of an organization.
        
                - **Id** *(string) --* 
        
                  The unique identifier (ID) of the account.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the account.
        
                  For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .
        
                - **Email** *(string) --* 
        
                  The email address associated with the AWS account.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of characters that represents a standard Internet email address.
        
                - **Name** *(string) --* 
        
                  The friendly name of the account.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.
        
                - **Status** *(string) --* 
        
                  The status of the account in the organization.
        
                - **JoinedMethod** *(string) --* 
        
                  The method by which the account joined the organization.
        
                - **JoinedTimestamp** *(datetime) --* 
        
                  The date the account became a part of the organization.
        
        """
        pass


class ListAccountsForParent(Paginator):
    def paginate(self, ParentId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListAccountsForParent>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ParentId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ParentId: string
        :param ParentId: **[REQUIRED]** 
        
          The unique identifier (ID) for the parent root or organization unit (OU) whose accounts you want to list.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Accounts\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Email\': \'string\',
                        \'Name\': \'string\',
                        \'Status\': \'ACTIVE\'|\'SUSPENDED\',
                        \'JoinedMethod\': \'INVITED\'|\'CREATED\',
                        \'JoinedTimestamp\': datetime(2015, 1, 1)
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Accounts** *(list) --* 
        
              A list of the accounts in the specified root or OU.
        
              - *(dict) --* 
        
                Contains information about an AWS account that is a member of an organization.
        
                - **Id** *(string) --* 
        
                  The unique identifier (ID) of the account.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the account.
        
                  For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .
        
                - **Email** *(string) --* 
        
                  The email address associated with the AWS account.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of characters that represents a standard Internet email address.
        
                - **Name** *(string) --* 
        
                  The friendly name of the account.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.
        
                - **Status** *(string) --* 
        
                  The status of the account in the organization.
        
                - **JoinedMethod** *(string) --* 
        
                  The method by which the account joined the organization.
        
                - **JoinedTimestamp** *(datetime) --* 
        
                  The date the account became a part of the organization.
        
        """
        pass


class ListChildren(Paginator):
    def paginate(self, ParentId: str, ChildType: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListChildren>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ParentId=\'string\',
              ChildType=\'ACCOUNT\'|\'ORGANIZATIONAL_UNIT\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ParentId: string
        :param ParentId: **[REQUIRED]** 
        
          The unique identifier (ID) for the parent root or OU whose children you want to list.
        
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires one of the following:
        
          * Root: a string that begins with \"r-\" followed by from 4 to 32 lower-case letters or digits. 
           
          * Organizational unit (OU): a string that begins with \"ou-\" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second \"-\" dash and from 8 to 32 additional lower-case letters or digits. 
           
        :type ChildType: string
        :param ChildType: **[REQUIRED]** 
        
          Filters the output to include only the specified child type.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Children\': [
                    {
                        \'Id\': \'string\',
                        \'Type\': \'ACCOUNT\'|\'ORGANIZATIONAL_UNIT\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Children** *(list) --* 
        
              The list of children of the specified parent container.
        
              - *(dict) --* 
        
                Contains a list of child entities, either OUs or accounts.
        
                - **Id** *(string) --* 
        
                  The unique identifier (ID) of this child entity.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a child ID string requires one of the following:
        
                  * Account: a string that consists of exactly 12 digits. 
                   
                  * Organizational unit (OU): a string that begins with \"ou-\" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second \"-\" dash and from 8 to 32 additional lower-case letters or digits. 
                   
                - **Type** *(string) --* 
        
                  The type of this child entity.
        
        """
        pass


class ListCreateAccountStatus(Paginator):
    def paginate(self, States: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListCreateAccountStatus>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              States=[
                  \'IN_PROGRESS\'|\'SUCCEEDED\'|\'FAILED\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type States: list
        :param States: 
        
          A list of one or more states that you want included in the response. If this parameter is not present, then all requests are included in the response.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'CreateAccountStatuses\': [
                    {
                        \'Id\': \'string\',
                        \'AccountName\': \'string\',
                        \'State\': \'IN_PROGRESS\'|\'SUCCEEDED\'|\'FAILED\',
                        \'RequestedTimestamp\': datetime(2015, 1, 1),
                        \'CompletedTimestamp\': datetime(2015, 1, 1),
                        \'AccountId\': \'string\',
                        \'FailureReason\': \'ACCOUNT_LIMIT_EXCEEDED\'|\'EMAIL_ALREADY_EXISTS\'|\'INVALID_ADDRESS\'|\'INVALID_EMAIL\'|\'CONCURRENT_ACCOUNT_MODIFICATION\'|\'INTERNAL_FAILURE\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CreateAccountStatuses** *(list) --* 
        
              A list of objects with details about the requests. Certain elements, such as the accountId number, are present in the output only after the account has been successfully created.
        
              - *(dict) --* 
        
                Contains the status about a  CreateAccount request to create an AWS account in an organization.
        
                - **Id** *(string) --* 
        
                  The unique identifier (ID) that references this request. You get this value from the response of the initial  CreateAccount request to create the account.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID string requires \"car-\" followed by from 8 to 32 lower-case letters or digits.
        
                - **AccountName** *(string) --* 
        
                  The account name given to the account when it was created.
        
                - **State** *(string) --* 
        
                  The status of the request.
        
                - **RequestedTimestamp** *(datetime) --* 
        
                  The date and time that the request was made for the account creation.
        
                - **CompletedTimestamp** *(datetime) --* 
        
                  The date and time that the account was created and the request completed.
        
                - **AccountId** *(string) --* 
        
                  If the account was created successfully, the unique identifier (ID) of the new account.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.
        
                - **FailureReason** *(string) --* 
        
                  If the request failed, a description of the reason for the failure.
        
                  * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the limit on the number of accounts in your organization. 
                   
                  * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with that email address already exists. 
                   
                  * INVALID_ADDRESS: The account could not be created because the address you provided is not valid. 
                   
                  * INVALID_EMAIL: The account could not be created because the email address you provided is not valid. 
                   
                  * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Customer Support. 
                   
        """
        pass


class ListHandshakesForAccount(Paginator):
    def paginate(self, Filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListHandshakesForAccount>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filter={
                  \'ActionType\': \'INVITE\'|\'ENABLE_ALL_FEATURES\'|\'APPROVE_ALL_FEATURES\'|\'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE\',
                  \'ParentHandshakeId\': \'string\'
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filter: dict
        :param Filter: 
        
          Filters the handshakes that you want included in the response. The default is all types. Use the ``ActionType`` element to limit the output to only a specified type, such as ``INVITE`` , ``ENABLE-FULL-CONTROL`` , or ``APPROVE-FULL-CONTROL`` . Alternatively, for the ``ENABLE-FULL-CONTROL`` handshake that generates a separate child handshake for each member account, you can specify ``ParentHandshakeId`` to see only the handshakes that were generated by that parent request.
        
          - **ActionType** *(string) --* 
        
            Specifies the type of handshake action.
        
            If you specify ``ActionType`` , you cannot also specify ``ParentHandshakeId`` .
        
          - **ParentHandshakeId** *(string) --* 
        
            Specifies the parent handshake. Only used for handshake types that are a child of another type.
        
            If you specify ``ParentHandshakeId`` , you cannot also specify ``ActionType`` .
        
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires \"h-\" followed by from 8 to 32 lower-case letters or digits.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Handshakes\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Parties\': [
                            {
                                \'Id\': \'string\',
                                \'Type\': \'ACCOUNT\'|\'ORGANIZATION\'|\'EMAIL\'
                            },
                        ],
                        \'State\': \'REQUESTED\'|\'OPEN\'|\'CANCELED\'|\'ACCEPTED\'|\'DECLINED\'|\'EXPIRED\',
                        \'RequestedTimestamp\': datetime(2015, 1, 1),
                        \'ExpirationTimestamp\': datetime(2015, 1, 1),
                        \'Action\': \'INVITE\'|\'ENABLE_ALL_FEATURES\'|\'APPROVE_ALL_FEATURES\'|\'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE\',
                        \'Resources\': [
                            {
                                \'Value\': \'string\',
                                \'Type\': \'ACCOUNT\'|\'ORGANIZATION\'|\'ORGANIZATION_FEATURE_SET\'|\'EMAIL\'|\'MASTER_EMAIL\'|\'MASTER_NAME\'|\'NOTES\'|\'PARENT_HANDSHAKE\',
                                \'Resources\': {\'... recursive ...\'}
                            },
                        ]
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Handshakes** *(list) --* 
        
              A list of  Handshake objects with details about each of the handshakes that is associated with the specified account.
        
              - *(dict) --* 
        
                Contains information that must be exchanged to securely establish a relationship between two accounts (an *originator* and a *recipient* ). For example, when a master account (the originator) invites another account (the recipient) to join its organization, the two accounts exchange information as a series of handshake requests and responses.
        
                 **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30 days after entering that state After that they are deleted.
        
                - **Id** *(string) --* 
        
                  The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires \"h-\" followed by from 8 to 32 lower-case letters or digits.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of a handshake.
        
                  For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .
        
                - **Parties** *(list) --* 
        
                  Information about the two accounts that are participating in the handshake.
        
                  - *(dict) --* 
        
                    Identifies a participant in a handshake.
        
                    - **Id** *(string) --* 
        
                      The unique identifier (ID) for the party.
        
                      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires \"h-\" followed by from 8 to 32 lower-case letters or digits.
        
                    - **Type** *(string) --* 
        
                      The type of party.
        
                - **State** *(string) --* 
        
                  The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:
        
                  * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond. 
                   
                  * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action. 
                   
                  * **CANCELED** : This handshake is no longer active because it was canceled by the originating account. 
                   
                  * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient. 
                   
                  * **DECLINED** : This handshake is no longer active because it was declined by the recipient account. 
                   
                  * **EXPIRED** : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days). 
                   
                - **RequestedTimestamp** *(datetime) --* 
        
                  The date and time that the handshake request was made.
        
                - **ExpirationTimestamp** *(datetime) --* 
        
                  The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.
        
                - **Action** *(string) --* 
        
                  The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:
        
                  * **INVITE** : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts. 
                   
                  * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only *invited* member accounts. Created accounts do not receive this because those accounts were created by the organization\'s master account and approval is inferred. 
                   
                  * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features. 
                   
                - **Resources** *(list) --* 
        
                  Additional information that is needed to process the handshake.
        
                  - *(dict) --* 
        
                    Contains additional data that is needed to process a handshake.
        
                    - **Value** *(string) --* 
        
                      The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.
        
                    - **Type** *(string) --* 
        
                      The type of information being passed, specifying how the value is to be interpreted by the other party:
        
                      * ``ACCOUNT`` - Specifies an AWS account ID number. 
                       
                      * ``ORGANIZATION`` - Specifies an organization ID number. 
                       
                      * ``EMAIL`` - Specifies the email address that is associated with the account that receives the handshake.  
                       
                      * ``OWNER_EMAIL`` - Specifies the email address associated with the master account. Included as information about an organization.  
                       
                      * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as information about an organization.  
                       
                      * ``NOTES`` - Additional text provided by the handshake initiator and intended for the recipient to read. 
                       
                    - **Resources** *(list) --* 
        
                      When needed, contains an additional array of ``HandshakeResource`` objects.
        
        """
        pass


class ListHandshakesForOrganization(Paginator):
    def paginate(self, Filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListHandshakesForOrganization>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filter={
                  \'ActionType\': \'INVITE\'|\'ENABLE_ALL_FEATURES\'|\'APPROVE_ALL_FEATURES\'|\'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE\',
                  \'ParentHandshakeId\': \'string\'
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filter: dict
        :param Filter: 
        
          A filter of the handshakes that you want included in the response. The default is all types. Use the ``ActionType`` element to limit the output to only a specified type, such as ``INVITE`` , ``ENABLE-ALL-FEATURES`` , or ``APPROVE-ALL-FEATURES`` . Alternatively, for the ``ENABLE-ALL-FEATURES`` handshake that generates a separate child handshake for each member account, you can specify the ``ParentHandshakeId`` to see only the handshakes that were generated by that parent request.
        
          - **ActionType** *(string) --* 
        
            Specifies the type of handshake action.
        
            If you specify ``ActionType`` , you cannot also specify ``ParentHandshakeId`` .
        
          - **ParentHandshakeId** *(string) --* 
        
            Specifies the parent handshake. Only used for handshake types that are a child of another type.
        
            If you specify ``ParentHandshakeId`` , you cannot also specify ``ActionType`` .
        
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires \"h-\" followed by from 8 to 32 lower-case letters or digits.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Handshakes\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Parties\': [
                            {
                                \'Id\': \'string\',
                                \'Type\': \'ACCOUNT\'|\'ORGANIZATION\'|\'EMAIL\'
                            },
                        ],
                        \'State\': \'REQUESTED\'|\'OPEN\'|\'CANCELED\'|\'ACCEPTED\'|\'DECLINED\'|\'EXPIRED\',
                        \'RequestedTimestamp\': datetime(2015, 1, 1),
                        \'ExpirationTimestamp\': datetime(2015, 1, 1),
                        \'Action\': \'INVITE\'|\'ENABLE_ALL_FEATURES\'|\'APPROVE_ALL_FEATURES\'|\'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE\',
                        \'Resources\': [
                            {
                                \'Value\': \'string\',
                                \'Type\': \'ACCOUNT\'|\'ORGANIZATION\'|\'ORGANIZATION_FEATURE_SET\'|\'EMAIL\'|\'MASTER_EMAIL\'|\'MASTER_NAME\'|\'NOTES\'|\'PARENT_HANDSHAKE\',
                                \'Resources\': {\'... recursive ...\'}
                            },
                        ]
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Handshakes** *(list) --* 
        
              A list of  Handshake objects with details about each of the handshakes that are associated with an organization.
        
              - *(dict) --* 
        
                Contains information that must be exchanged to securely establish a relationship between two accounts (an *originator* and a *recipient* ). For example, when a master account (the originator) invites another account (the recipient) to join its organization, the two accounts exchange information as a series of handshake requests and responses.
        
                 **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30 days after entering that state After that they are deleted.
        
                - **Id** *(string) --* 
        
                  The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires \"h-\" followed by from 8 to 32 lower-case letters or digits.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of a handshake.
        
                  For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .
        
                - **Parties** *(list) --* 
        
                  Information about the two accounts that are participating in the handshake.
        
                  - *(dict) --* 
        
                    Identifies a participant in a handshake.
        
                    - **Id** *(string) --* 
        
                      The unique identifier (ID) for the party.
        
                      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires \"h-\" followed by from 8 to 32 lower-case letters or digits.
        
                    - **Type** *(string) --* 
        
                      The type of party.
        
                - **State** *(string) --* 
        
                  The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:
        
                  * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond. 
                   
                  * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action. 
                   
                  * **CANCELED** : This handshake is no longer active because it was canceled by the originating account. 
                   
                  * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient. 
                   
                  * **DECLINED** : This handshake is no longer active because it was declined by the recipient account. 
                   
                  * **EXPIRED** : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days). 
                   
                - **RequestedTimestamp** *(datetime) --* 
        
                  The date and time that the handshake request was made.
        
                - **ExpirationTimestamp** *(datetime) --* 
        
                  The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.
        
                - **Action** *(string) --* 
        
                  The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:
        
                  * **INVITE** : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts. 
                   
                  * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only *invited* member accounts. Created accounts do not receive this because those accounts were created by the organization\'s master account and approval is inferred. 
                   
                  * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features. 
                   
                - **Resources** *(list) --* 
        
                  Additional information that is needed to process the handshake.
        
                  - *(dict) --* 
        
                    Contains additional data that is needed to process a handshake.
        
                    - **Value** *(string) --* 
        
                      The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.
        
                    - **Type** *(string) --* 
        
                      The type of information being passed, specifying how the value is to be interpreted by the other party:
        
                      * ``ACCOUNT`` - Specifies an AWS account ID number. 
                       
                      * ``ORGANIZATION`` - Specifies an organization ID number. 
                       
                      * ``EMAIL`` - Specifies the email address that is associated with the account that receives the handshake.  
                       
                      * ``OWNER_EMAIL`` - Specifies the email address associated with the master account. Included as information about an organization.  
                       
                      * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as information about an organization.  
                       
                      * ``NOTES`` - Additional text provided by the handshake initiator and intended for the recipient to read. 
                       
                    - **Resources** *(list) --* 
        
                      When needed, contains an additional array of ``HandshakeResource`` objects.
        
        """
        pass


class ListOrganizationalUnitsForParent(Paginator):
    def paginate(self, ParentId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListOrganizationalUnitsForParent>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ParentId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ParentId: string
        :param ParentId: **[REQUIRED]** 
        
          The unique identifier (ID) of the root or OU whose child OUs you want to list.
        
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires one of the following:
        
          * Root: a string that begins with \"r-\" followed by from 4 to 32 lower-case letters or digits. 
           
          * Organizational unit (OU): a string that begins with \"ou-\" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second \"-\" dash and from 8 to 32 additional lower-case letters or digits. 
           
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'OrganizationalUnits\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **OrganizationalUnits** *(list) --* 
        
              A list of the OUs in the specified root or parent OU.
        
              - *(dict) --* 
        
                Contains details about an organizational unit (OU). An OU is a container of AWS accounts within a root of an organization. Policies that are attached to an OU apply to all accounts contained in that OU and in any child OUs.
        
                - **Id** *(string) --* 
        
                  The unique identifier (ID) associated with this OU.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID string requires \"ou-\" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second \"-\" dash and from 8 to 32 additional lower-case letters or digits.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of this OU.
        
                  For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .
        
                - **Name** *(string) --* 
        
                  The friendly name of this OU.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.
        
        """
        pass


class ListParents(Paginator):
    def paginate(self, ChildId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListParents>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ChildId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ChildId: string
        :param ChildId: **[REQUIRED]** 
        
          The unique identifier (ID) of the OU or account whose parent containers you want to list. Do not specify a root.
        
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a child ID string requires one of the following:
        
          * Account: a string that consists of exactly 12 digits. 
           
          * Organizational unit (OU): a string that begins with \"ou-\" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second \"-\" dash and from 8 to 32 additional lower-case letters or digits. 
           
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Parents\': [
                    {
                        \'Id\': \'string\',
                        \'Type\': \'ROOT\'|\'ORGANIZATIONAL_UNIT\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Parents** *(list) --* 
        
              A list of parents for the specified child account or OU.
        
              - *(dict) --* 
        
                Contains information about either a root or an organizational unit (OU) that can contain OUs or accounts in an organization.
        
                - **Id** *(string) --* 
        
                  The unique identifier (ID) of the parent entity.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires one of the following:
        
                  * Root: a string that begins with \"r-\" followed by from 4 to 32 lower-case letters or digits. 
                   
                  * Organizational unit (OU): a string that begins with \"ou-\" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second \"-\" dash and from 8 to 32 additional lower-case letters or digits. 
                   
                - **Type** *(string) --* 
        
                  The type of the parent entity.
        
        """
        pass


class ListPolicies(Paginator):
    def paginate(self, Filter: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListPolicies>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Filter=\'SERVICE_CONTROL_POLICY\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Filter: string
        :param Filter: **[REQUIRED]** 
        
          Specifies the type of policy that you want to include in the response.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Policies\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\',
                        \'Description\': \'string\',
                        \'Type\': \'SERVICE_CONTROL_POLICY\',
                        \'AwsManaged\': True|False
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Policies** *(list) --* 
        
              A list of policies that match the filter criteria in the request. The output list does not include the policy contents. To see the content for a policy, see  DescribePolicy .
        
              - *(dict) --* 
        
                Contains information about a policy, but does not include the content. To see the content of a policy, see  DescribePolicy .
        
                - **Id** *(string) --* 
        
                  The unique identifier (ID) of the policy.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires \"p-\" followed by from 8 to 128 lower-case letters or digits.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the policy.
        
                  For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .
        
                - **Name** *(string) --* 
        
                  The friendly name of the policy.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.
        
                - **Description** *(string) --* 
        
                  The description of the policy.
        
                - **Type** *(string) --* 
        
                  The type of policy.
        
                - **AwsManaged** *(boolean) --* 
        
                  A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
        
        """
        pass


class ListPoliciesForTarget(Paginator):
    def paginate(self, TargetId: str, Filter: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListPoliciesForTarget>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              TargetId=\'string\',
              Filter=\'SERVICE_CONTROL_POLICY\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type TargetId: string
        :param TargetId: **[REQUIRED]** 
        
          The unique identifier (ID) of the root, organizational unit, or account whose policies you want to list.
        
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires one of the following:
        
          * Root: a string that begins with \"r-\" followed by from 4 to 32 lower-case letters or digits. 
           
          * Account: a string that consists of exactly 12 digits. 
           
          * Organizational unit (OU): a string that begins with \"ou-\" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second \"-\" dash and from 8 to 32 additional lower-case letters or digits. 
           
        :type Filter: string
        :param Filter: **[REQUIRED]** 
        
          The type of policy that you want to include in the returned list.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Policies\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\',
                        \'Description\': \'string\',
                        \'Type\': \'SERVICE_CONTROL_POLICY\',
                        \'AwsManaged\': True|False
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Policies** *(list) --* 
        
              The list of policies that match the criteria in the request.
        
              - *(dict) --* 
        
                Contains information about a policy, but does not include the content. To see the content of a policy, see  DescribePolicy .
        
                - **Id** *(string) --* 
        
                  The unique identifier (ID) of the policy.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires \"p-\" followed by from 8 to 128 lower-case letters or digits.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the policy.
        
                  For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .
        
                - **Name** *(string) --* 
        
                  The friendly name of the policy.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.
        
                - **Description** *(string) --* 
        
                  The description of the policy.
        
                - **Type** *(string) --* 
        
                  The type of policy.
        
                - **AwsManaged** *(boolean) --* 
        
                  A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
        
        """
        pass


class ListRoots(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListRoots>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Roots\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\',
                        \'PolicyTypes\': [
                            {
                                \'Type\': \'SERVICE_CONTROL_POLICY\',
                                \'Status\': \'ENABLED\'|\'PENDING_ENABLE\'|\'PENDING_DISABLE\'
                            },
                        ]
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Roots** *(list) --* 
        
              A list of roots that are defined in an organization.
        
              - *(dict) --* 
        
                Contains details about a root. A root is a top-level parent node in the hierarchy of an organization that can contain organizational units (OUs) and accounts. Every root contains every AWS account in the organization. Each root enables the accounts to be organized in a different way and to have different policy types enabled for use in that root.
        
                - **Id** *(string) --* 
        
                  The unique identifier (ID) for the root.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires \"r-\" followed by from 4 to 32 lower-case letters or digits.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the root.
        
                  For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .
        
                - **Name** *(string) --* 
        
                  The friendly name of the root.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.
        
                - **PolicyTypes** *(list) --* 
        
                  The types of policies that are currently enabled for the root and therefore can be attached to the root or to its OUs or accounts.
        
                  .. note::
        
                    Even if a policy type is shown as available in the organization, you can separately enable and disable them at the root level by using  EnablePolicyType and  DisablePolicyType . Use  DescribeOrganization to see the availability of the policy types in that organization.
        
                  - *(dict) --* 
        
                    Contains information about a policy type and its status in the associated root.
        
                    - **Type** *(string) --* 
        
                      The name of the policy type.
        
                    - **Status** *(string) --* 
        
                      The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.
        
        """
        pass


class ListTargetsForPolicy(Paginator):
    def paginate(self, PolicyId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListTargetsForPolicy>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PolicyId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type PolicyId: string
        :param PolicyId: **[REQUIRED]** 
        
          The unique identifier (ID) of the policy for which you want to know its attachments.
        
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires \"p-\" followed by from 8 to 128 lower-case letters or digits.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Targets\': [
                    {
                        \'TargetId\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\',
                        \'Type\': \'ACCOUNT\'|\'ORGANIZATIONAL_UNIT\'|\'ROOT\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Targets** *(list) --* 
        
              A list of structures, each of which contains details about one of the entities to which the specified policy is attached.
        
              - *(dict) --* 
        
                Contains information about a root, OU, or account that a policy is attached to.
        
                - **TargetId** *(string) --* 
        
                  The unique identifier (ID) of the policy target.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires one of the following:
        
                  * Root: a string that begins with \"r-\" followed by from 4 to 32 lower-case letters or digits. 
                   
                  * Account: a string that consists of exactly 12 digits. 
                   
                  * Organizational unit (OU): a string that begins with \"ou-\" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second \"-\" dash and from 8 to 32 additional lower-case letters or digits. 
                   
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the policy target.
        
                  For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .
        
                - **Name** *(string) --* 
        
                  The friendly name of the policy target.
        
                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.
        
                - **Type** *(string) --* 
        
                  The type of the policy target.
        
        """
        pass
