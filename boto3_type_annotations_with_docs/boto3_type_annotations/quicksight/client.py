from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Union


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

    def create_group(self, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None) -> Dict:
        """
        Creates an Amazon QuickSight group.
        The permissions resource is ``arn:aws:quicksight:us-east-1:*<relevant-aws-account-id>* :group/default/*<group-name>* `` .
        The response is a group object.
        
        **CLI Sample:**
         ``aws quicksight create-group --aws-account-id=111122223333 --namespace=default --group-name="Sales-Management" --description="Sales Management - Forecasting"``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/CreateGroup>`_
        
        **Request Syntax**
        ::
          response = client.create_group(
              GroupName='string',
              Description='string',
              AwsAccountId='string',
              Namespace='string'
          )
        
        **Response Syntax**
        ::
            {
                'Group': {
                    'Arn': 'string',
                    'GroupName': 'string',
                    'Description': 'string',
                    'PrincipalId': 'string'
                },
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            The response object for this operation.
            - **Group** *(dict) --* 
              The name of the group.
              - **Arn** *(string) --* 
                The Amazon Resource Name (ARN) for the group.
              - **GroupName** *(string) --* 
                The name of the group.
              - **Description** *(string) --* 
                The group description.
              - **PrincipalId** *(string) --* 
                The principal ID of the group.
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The http status of the request.
        :type GroupName: string
        :param GroupName: **[REQUIRED]**
          A name for the group that you want to create.
        :type Description: string
        :param Description:
          A description for the group that you want to create.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
        :rtype: dict
        :returns:
        """
        pass

    def create_group_membership(self, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str) -> Dict:
        """
        Adds an Amazon QuickSight user to an Amazon QuickSight group. 
        The permissions resource is ``arn:aws:quicksight:us-east-1:*<aws-account-id>* :group/default/*<group-name>* `` .
        The condition resource is the user name.
        The condition key is ``quicksight:UserName`` .
        The response is the group member object.
        
        **CLI Sample:**
         ``aws quicksight create-group-membership --aws-account-id=111122223333 --namespace=default --group-name=Sales --member-name=Pat``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/CreateGroupMembership>`_
        
        **Request Syntax**
        ::
          response = client.create_group_membership(
              MemberName='string',
              GroupName='string',
              AwsAccountId='string',
              Namespace='string'
          )
        
        **Response Syntax**
        ::
            {
                'GroupMember': {
                    'Arn': 'string',
                    'MemberName': 'string'
                },
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **GroupMember** *(dict) --* 
              The group member.
              - **Arn** *(string) --* 
                The Amazon Resource Name (ARN) for the group member (user).
              - **MemberName** *(string) --* 
                The name of the group member (user).
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The http status of the request.
        :type MemberName: string
        :param MemberName: **[REQUIRED]**
          The name of the user that you want to add to the group membership.
        :type GroupName: string
        :param GroupName: **[REQUIRED]**
          The name of the group that you want to add the user to.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
        :rtype: dict
        :returns:
        """
        pass

    def delete_group(self, GroupName: str, AwsAccountId: str, Namespace: str) -> Dict:
        """
        Removes a user group from Amazon QuickSight. 
        The permissions resource is ``arn:aws:quicksight:us-east-1:*<aws-account-id>* :group/default/*<group-name>* `` .
        
        **CLI Sample:**
         ``aws quicksight delete-group -\-aws-account-id=111122223333 -\-namespace=default -\-group-name=Sales-Management``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/DeleteGroup>`_
        
        **Request Syntax**
        ::
          response = client.delete_group(
              GroupName='string',
              AwsAccountId='string',
              Namespace='string'
          )
        
        **Response Syntax**
        ::
            {
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The http status of the request.
        :type GroupName: string
        :param GroupName: **[REQUIRED]**
          The name of the group that you want to delete.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
        :rtype: dict
        :returns:
        """
        pass

    def delete_group_membership(self, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str) -> Dict:
        """
        Removes a user from a group so that the user is no longer a member of the group.
        The permissions resource is ``arn:aws:quicksight:us-east-1:*<aws-account-id>* :group/default/*<group-name>* `` .
        The condition resource is the user name.
        The condition key is ``quicksight:UserName`` .
        
        **CLI Sample:**
         ``aws quicksight delete-group-membership --aws-account-id=111122223333 --namespace=default --group-name=Sales-Management --member-name=Charlie``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/DeleteGroupMembership>`_
        
        **Request Syntax**
        ::
          response = client.delete_group_membership(
              MemberName='string',
              GroupName='string',
              AwsAccountId='string',
              Namespace='string'
          )
        
        **Response Syntax**
        ::
            {
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The http status of the request.
        :type MemberName: string
        :param MemberName: **[REQUIRED]**
          The name of the user that you want to delete from the group membership.
        :type GroupName: string
        :param GroupName: **[REQUIRED]**
          The name of the group that you want to delete the user from.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
        :rtype: dict
        :returns:
        """
        pass

    def delete_user(self, UserName: str, AwsAccountId: str, Namespace: str) -> Dict:
        """
        Deletes the Amazon QuickSight user that is associated with the identity of the AWS Identity and Access Management (IAM) user or role that's making the call. The IAM user isn't deleted as a result of this call. 
        The permission resource is ``arn:aws:quicksight:us-east-1:*<aws-account-id>* :user/default/*<user-name>* `` .
        
        **CLI Sample:**
         ``aws quicksight delete-user --aws-account-id=111122223333 --namespace=default --user-name=Pat``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/DeleteUser>`_
        
        **Request Syntax**
        ::
          response = client.delete_user(
              UserName='string',
              AwsAccountId='string',
              Namespace='string'
          )
        
        **Response Syntax**
        ::
            {
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The http status of the request.
        :type UserName: string
        :param UserName: **[REQUIRED]**
          The name of the user that you want to delete.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
        :rtype: dict
        :returns:
        """
        pass

    def delete_user_by_principal_id(self, PrincipalId: str, AwsAccountId: str, Namespace: str) -> Dict:
        """
        Deletes a user after locating the user by its principal ID.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/DeleteUserByPrincipalId>`_
        
        **Request Syntax**
        ::
          response = client.delete_user_by_principal_id(
              PrincipalId='string',
              AwsAccountId='string',
              Namespace='string'
          )
        
        **Response Syntax**
        ::
            {
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The http status of the request.
        :type PrincipalId: string
        :param PrincipalId: **[REQUIRED]**
          The principal ID of the user.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_group(self, GroupName: str, AwsAccountId: str, Namespace: str) -> Dict:
        """
        Returns an Amazon QuickSight group's description and Amazon Resource Name (ARN). 
        The permissions resource is ``arn:aws:quicksight:us-east-1:*<relevant-aws-account-id>* :group/default/*<group-name>* `` .
        The response is the group object. 
        
        **CLI Sample:**
         ``aws quicksight describe-group -\-aws-account-id=11112222333 -\-namespace=default -\-group-name=Sales``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/DescribeGroup>`_
        
        **Request Syntax**
        ::
          response = client.describe_group(
              GroupName='string',
              AwsAccountId='string',
              Namespace='string'
          )
        
        **Response Syntax**
        ::
            {
                'Group': {
                    'Arn': 'string',
                    'GroupName': 'string',
                    'Description': 'string',
                    'PrincipalId': 'string'
                },
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Group** *(dict) --* 
              The name of the group.
              - **Arn** *(string) --* 
                The Amazon Resource Name (ARN) for the group.
              - **GroupName** *(string) --* 
                The name of the group.
              - **Description** *(string) --* 
                The group description.
              - **PrincipalId** *(string) --* 
                The principal ID of the group.
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The http status of the request.
        :type GroupName: string
        :param GroupName: **[REQUIRED]**
          The name of the group that you want to describe.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_user(self, UserName: str, AwsAccountId: str, Namespace: str) -> Dict:
        """
        Returns information about a user, given the user name. 
        The permission resource is ``arn:aws:quicksight:us-east-1:*<aws-account-id>* :user/default/*<user-name>* `` . 
        The response is a user object that contains the user's Amazon Resource Name (ARN), AWS Identity and Access Management (IAM) role, and email address. 
        
        **CLI Sample:**
         ``aws quicksight describe-user --aws-account-id=111122223333 --namespace=default --user-name=Pat``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/DescribeUser>`_
        
        **Request Syntax**
        ::
          response = client.describe_user(
              UserName='string',
              AwsAccountId='string',
              Namespace='string'
          )
        
        **Response Syntax**
        ::
            {
                'User': {
                    'Arn': 'string',
                    'UserName': 'string',
                    'Email': 'string',
                    'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
                    'IdentityType': 'IAM'|'QUICKSIGHT',
                    'Active': True|False,
                    'PrincipalId': 'string'
                },
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **User** *(dict) --* 
              The user name.
              - **Arn** *(string) --* 
                The Amazon Resource Name (ARN) for the user.
              - **UserName** *(string) --* 
                The user's user name.
              - **Email** *(string) --* 
                The user's email address.
              - **Role** *(string) --* 
                The Amazon QuickSight role for the user.
              - **IdentityType** *(string) --* 
                The type of identity authentication used by the user.
              - **Active** *(boolean) --* 
                Active status of user. When you create an Amazon QuickSight user that’s not an IAM user or an AD user, that user is inactive until they sign in and provide a password
              - **PrincipalId** *(string) --* 
                The principal ID of the user.
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The http status of the request.
        :type UserName: string
        :param UserName: **[REQUIRED]**
          The name of the user that you want to describe.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
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

    def get_dashboard_embed_url(self, AwsAccountId: str, DashboardId: str, IdentityType: str, SessionLifetimeInMinutes: int = None, UndoRedoDisabled: bool = None, ResetDisabled: bool = None) -> Dict:
        """
        Generates a server-side embeddable URL and authorization code. Before this can work properly, first you need to configure the dashboards and user permissions. For more information, see `Embedding Amazon QuickSight Dashboards <https://docs.aws.amazon.com/en_us/quicksight/latest/user/embedding.html>`__ .
        Currently, you can use ``GetDashboardEmbedURL`` only from the server, not from the user’s browser.
        
        **CLI Sample:**
        Assume the role with permissions enabled for actions: ``quickSight:RegisterUser`` and ``quicksight:GetDashboardEmbedURL`` . You can use assume-role, assume-role-with-web-identity, or assume-role-with-saml. 
         ``aws sts assume-role --role-arn "arn:aws:iam::111122223333:role/embedding_quicksight_dashboard_role" --role-session-name embeddingsession``  
        If the user does not exist in QuickSight, register the user:
         ``aws quicksight register-user --aws-account-id 111122223333 --namespace default --identity-type IAM --iam-arn "arn:aws:iam::111122223333:role/embedding_quicksight_dashboard_role" --user-role READER --session-name "embeddingsession" --email user123@example.com --region us-east-1``  
        Get the URL for the embedded dashboard
         ``aws quicksight get-dashboard-embed-url --aws-account-id 111122223333 --dashboard-id 1a1ac2b2-3fc3-4b44-5e5d-c6db6778df89 --identity-type IAM``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/GetDashboardEmbedUrl>`_
        
        **Request Syntax**
        ::
          response = client.get_dashboard_embed_url(
              AwsAccountId='string',
              DashboardId='string',
              IdentityType='IAM'|'QUICKSIGHT',
              SessionLifetimeInMinutes=123,
              UndoRedoDisabled=True|False,
              ResetDisabled=True|False
          )
        
        **Response Syntax**
        ::
            {
                'EmbedUrl': 'string',
                'Status': 123,
                'RequestId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EmbedUrl** *(string) --* 
              URL that you can put into your server-side webpage to embed your dashboard. This URL is valid for 5 minutes, and the resulting session is valid for 10 hours. The API provides the URL with an auth_code that enables a single-signon session. 
            - **Status** *(integer) --* 
              The http status of the request.
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          AWS account ID that contains the dashboard you are embedding.
        :type DashboardId: string
        :param DashboardId: **[REQUIRED]**
          The ID for the dashboard, also added to IAM policy
        :type IdentityType: string
        :param IdentityType: **[REQUIRED]**
          The authentication method the user uses to sign in (IAM only).
        :type SessionLifetimeInMinutes: integer
        :param SessionLifetimeInMinutes:
          How many minutes the session is valid. The session lifetime must be between 15 and 600 minutes.
        :type UndoRedoDisabled: boolean
        :param UndoRedoDisabled:
          Remove the undo/redo button on embedded dashboard. The default is FALSE, which enables the undo/redo button.
        :type ResetDisabled: boolean
        :param ResetDisabled:
          Remove the reset button on embedded dashboard. The default is FALSE, which allows the reset button.
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

    def list_group_memberships(self, GroupName: str, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Lists member users in a group.
        The permissions resource is ``arn:aws:quicksight:us-east-1:*<aws-account-id>* :group/default/*<group-name>* `` .
        The response is a list of group member objects.
        
        **CLI Sample:**
         ``aws quicksight list-group-memberships -\-aws-account-id=111122223333 -\-namespace=default``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/ListGroupMemberships>`_
        
        **Request Syntax**
        ::
          response = client.list_group_memberships(
              GroupName='string',
              NextToken='string',
              MaxResults=123,
              AwsAccountId='string',
              Namespace='string'
          )
        
        **Response Syntax**
        ::
            {
                'GroupMemberList': [
                    {
                        'Arn': 'string',
                        'MemberName': 'string'
                    },
                ],
                'NextToken': 'string',
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **GroupMemberList** *(list) --* 
              The list of the members of the group.
              - *(dict) --* 
                A member of an Amazon QuickSight group. Currently, group members must be users. Groups can't be members of another group. 
                - **Arn** *(string) --* 
                  The Amazon Resource Name (ARN) for the group member (user).
                - **MemberName** *(string) --* 
                  The name of the group member (user).
            - **NextToken** *(string) --* 
              A pagination token that can be used in a subsequent request.
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The http status of the request.
        :type GroupName: string
        :param GroupName: **[REQUIRED]**
          The name of the group that you want to see a membership list of.
        :type NextToken: string
        :param NextToken:
          A pagination token that can be used in a subsequent request.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return from this request.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
        :rtype: dict
        :returns:
        """
        pass

    def list_groups(self, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Lists all user groups in Amazon QuickSight. 
        The permissions resource is ``arn:aws:quicksight:us-east-1:*<aws-account-id>* :group/default/*`` .
        The response is a list of group objects. 
        
        **CLI Sample:**
         ``aws quicksight list-groups -\-aws-account-id=111122223333 -\-namespace=default``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/ListGroups>`_
        
        **Request Syntax**
        ::
          response = client.list_groups(
              AwsAccountId='string',
              NextToken='string',
              MaxResults=123,
              Namespace='string'
          )
        
        **Response Syntax**
        ::
            {
                'GroupList': [
                    {
                        'Arn': 'string',
                        'GroupName': 'string',
                        'Description': 'string',
                        'PrincipalId': 'string'
                    },
                ],
                'NextToken': 'string',
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **GroupList** *(list) --* 
              The list of the groups.
              - *(dict) --* 
                A *group* in Amazon QuickSight consists of a set of users. You can use groups to make it easier to manage access and security. Currently, an Amazon QuickSight subscription can't contain more than 500 Amazon QuickSight groups.
                - **Arn** *(string) --* 
                  The Amazon Resource Name (ARN) for the group.
                - **GroupName** *(string) --* 
                  The name of the group.
                - **Description** *(string) --* 
                  The group description.
                - **PrincipalId** *(string) --* 
                  The principal ID of the group.
            - **NextToken** *(string) --* 
              A pagination token that can be used in a subsequent request.
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The http status of the request.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type NextToken: string
        :param NextToken:
          A pagination token that can be used in a subsequent request.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
        :rtype: dict
        :returns:
        """
        pass

    def list_user_groups(self, UserName: str, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Lists the Amazon QuickSight groups that an Amazon QuickSight user is a member of.
        The permission resource is ``arn:aws:quicksight:us-east-1:*<aws-account-id>* :user/default/*<user-name>* `` . 
        The response is a one or more group objects. 
        
        **CLI Sample:**
         ``aws quicksight list-user-groups -\-user-name=Pat -\-aws-account-id=111122223333 -\-namespace=default -\-region=us-east-1``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/ListUserGroups>`_
        
        **Request Syntax**
        ::
          response = client.list_user_groups(
              UserName='string',
              AwsAccountId='string',
              Namespace='string',
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'GroupList': [
                    {
                        'Arn': 'string',
                        'GroupName': 'string',
                        'Description': 'string',
                        'PrincipalId': 'string'
                    },
                ],
                'NextToken': 'string',
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **GroupList** *(list) --* 
              The list of groups the user is a member of.
              - *(dict) --* 
                A *group* in Amazon QuickSight consists of a set of users. You can use groups to make it easier to manage access and security. Currently, an Amazon QuickSight subscription can't contain more than 500 Amazon QuickSight groups.
                - **Arn** *(string) --* 
                  The Amazon Resource Name (ARN) for the group.
                - **GroupName** *(string) --* 
                  The name of the group.
                - **Description** *(string) --* 
                  The group description.
                - **PrincipalId** *(string) --* 
                  The principal ID of the group.
            - **NextToken** *(string) --* 
              A pagination token that can be used in a subsequent request.
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The HTTP status of the request.
        :type UserName: string
        :param UserName: **[REQUIRED]**
          The Amazon QuickSight user name that you want to list group memberships for.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The AWS Account ID that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
        :type NextToken: string
        :param NextToken:
          A pagination token that can be used in a subsequent request.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return from this request.
        :rtype: dict
        :returns:
        """
        pass

    def list_users(self, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Returns a list of all of the Amazon QuickSight users belonging to this account. 
        The permission resource is ``arn:aws:quicksight:us-east-1:*<aws-account-id>* :user/default/*`` .
        The response is a list of user objects, containing each user's Amazon Resource Name (ARN), AWS Identity and Access Management (IAM) role, and email address. 
        
        **CLI Sample:**
         ``aws quicksight list-users --aws-account-id=111122223333 --namespace=default``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/ListUsers>`_
        
        **Request Syntax**
        ::
          response = client.list_users(
              AwsAccountId='string',
              NextToken='string',
              MaxResults=123,
              Namespace='string'
          )
        
        **Response Syntax**
        ::
            {
                'UserList': [
                    {
                        'Arn': 'string',
                        'UserName': 'string',
                        'Email': 'string',
                        'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
                        'IdentityType': 'IAM'|'QUICKSIGHT',
                        'Active': True|False,
                        'PrincipalId': 'string'
                    },
                ],
                'NextToken': 'string',
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **UserList** *(list) --* 
              The list of users.
              - *(dict) --* 
                A registered user of Amazon QuickSight. Currently, an Amazon QuickSight subscription can't contain more than 20 million users.
                - **Arn** *(string) --* 
                  The Amazon Resource Name (ARN) for the user.
                - **UserName** *(string) --* 
                  The user's user name.
                - **Email** *(string) --* 
                  The user's email address.
                - **Role** *(string) --* 
                  The Amazon QuickSight role for the user.
                - **IdentityType** *(string) --* 
                  The type of identity authentication used by the user.
                - **Active** *(boolean) --* 
                  Active status of user. When you create an Amazon QuickSight user that’s not an IAM user or an AD user, that user is inactive until they sign in and provide a password
                - **PrincipalId** *(string) --* 
                  The principal ID of the user.
            - **NextToken** *(string) --* 
              A pagination token that can be used in a subsequent request.
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The http status of the request.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type NextToken: string
        :param NextToken:
          A pagination token that can be used in a subsequent request.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to return from this request.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
        :rtype: dict
        :returns:
        """
        pass

    def register_user(self, IdentityType: str, Email: str, UserRole: str, AwsAccountId: str, Namespace: str, IamArn: str = None, SessionName: str = None, UserName: str = None) -> Dict:
        """
        .. _https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html: https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html
        Creates an Amazon QuickSight user, whose identity is associated with the AWS Identity and Access Management (IAM) identity or role specified in the request. 
        The permission resource is ``arn:aws:quicksight:us-east-1:*<aws-account-id>* :user/default/*<user-name>* `` .
        The condition resource is the Amazon Resource Name (ARN) for the IAM user or role, and the session name. 
        The condition keys are ``quicksight:IamArn`` and ``quicksight:SessionName`` . 
        
        **CLI Sample:**
         ``aws quicksight register-user -\-aws-account-id=111122223333 -\-namespace=default -\-email=pat@example.com -\-identity-type=IAM -\-user-role=AUTHOR -\-iam-arn=arn:aws:iam::111122223333:user/Pat``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/RegisterUser>`_
        
        **Request Syntax**
        ::
          response = client.register_user(
              IdentityType='IAM'|'QUICKSIGHT',
              Email='string',
              UserRole='ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
              IamArn='string',
              SessionName='string',
              AwsAccountId='string',
              Namespace='string',
              UserName='string'
          )
        
        **Response Syntax**
        ::
            {
                'User': {
                    'Arn': 'string',
                    'UserName': 'string',
                    'Email': 'string',
                    'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
                    'IdentityType': 'IAM'|'QUICKSIGHT',
                    'Active': True|False,
                    'PrincipalId': 'string'
                },
                'UserInvitationUrl': 'string',
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **User** *(dict) --* 
              The user name.
              - **Arn** *(string) --* 
                The Amazon Resource Name (ARN) for the user.
              - **UserName** *(string) --* 
                The user's user name.
              - **Email** *(string) --* 
                The user's email address.
              - **Role** *(string) --* 
                The Amazon QuickSight role for the user.
              - **IdentityType** *(string) --* 
                The type of identity authentication used by the user.
              - **Active** *(boolean) --* 
                Active status of user. When you create an Amazon QuickSight user that’s not an IAM user or an AD user, that user is inactive until they sign in and provide a password
              - **PrincipalId** *(string) --* 
                The principal ID of the user.
            - **UserInvitationUrl** *(string) --* 
              The URL the user visits to complete registration and provide a password. This is returned only for users with an identity type of ``QUICKSIGHT`` .
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The http status of the request.
        :type IdentityType: string
        :param IdentityType: **[REQUIRED]**
          Amazon QuickSight supports several ways of managing the identity of users. This parameter accepts two values:
          * ``IAM`` : A user whose identity maps to an existing IAM user or role.
          * ``QUICKSIGHT`` : A user whose identity is owned and managed internally by Amazon QuickSight.
        :type Email: string
        :param Email: **[REQUIRED]**
          The email address of the user that you want to register.
        :type UserRole: string
        :param UserRole: **[REQUIRED]**
          The Amazon QuickSight role of the user. The user role can be one of the following:
          * ``READER`` : A user who has read-only access to dashboards.
          * ``AUTHOR`` : A user who can create data sources, data sets, analyses, and dashboards.
          * ``ADMIN`` : A user who is an author, who can also manage Amazon QuickSight settings.
        :type IamArn: string
        :param IamArn:
          The ARN of the IAM user or role that you are registering with Amazon QuickSight.
        :type SessionName: string
        :param SessionName:
          The name of the session with the assumed IAM role. By using this parameter, you can register multiple users with the same IAM role, provided that each has a different session name. For more information on assuming IAM roles, see ` ``assume-role`` https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html`__ in the *AWS CLI Reference.*
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
        :type UserName: string
        :param UserName:
          The Amazon QuickSight user name that you want to create for the user you are registering.
        :rtype: dict
        :returns:
        """
        pass

    def update_group(self, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None) -> Dict:
        """
        Changes a group description. 
        The permissions resource is ``arn:aws:quicksight:us-east-1:*<aws-account-id>* :group/default/*<group-name>* `` .
        The response is a group object.
        
        **CLI Sample:**
         ``aws quicksight update-group --aws-account-id=111122223333 --namespace=default --group-name=Sales --description="Sales BI Dashboards"``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/UpdateGroup>`_
        
        **Request Syntax**
        ::
          response = client.update_group(
              GroupName='string',
              Description='string',
              AwsAccountId='string',
              Namespace='string'
          )
        
        **Response Syntax**
        ::
            {
                'Group': {
                    'Arn': 'string',
                    'GroupName': 'string',
                    'Description': 'string',
                    'PrincipalId': 'string'
                },
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Group** *(dict) --* 
              The name of the group.
              - **Arn** *(string) --* 
                The Amazon Resource Name (ARN) for the group.
              - **GroupName** *(string) --* 
                The name of the group.
              - **Description** *(string) --* 
                The group description.
              - **PrincipalId** *(string) --* 
                The principal ID of the group.
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The http status of the request.
        :type GroupName: string
        :param GroupName: **[REQUIRED]**
          The name of the group that you want to update.
        :type Description: string
        :param Description:
          The description for the group that you want to update.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
        :rtype: dict
        :returns:
        """
        pass

    def update_user(self, UserName: str, AwsAccountId: str, Namespace: str, Email: str, Role: str) -> Dict:
        """
        Updates an Amazon QuickSight user.
        The permission resource is ``arn:aws:quicksight:us-east-1:*<aws-account-id>* :user/default/*<user-name>* `` . 
        The response is a user object that contains the user's Amazon QuickSight user name, email address, active or inactive status in Amazon QuickSight, Amazon QuickSight role, and Amazon Resource Name (ARN). 
        
        **CLI Sample:**
         ``aws quicksight update-user --user-name=Pat --role=ADMIN --email=new_address@amazon.com --aws-account-id=111122223333 --namespace=default --region=us-east-1``  
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/UpdateUser>`_
        
        **Request Syntax**
        ::
          response = client.update_user(
              UserName='string',
              AwsAccountId='string',
              Namespace='string',
              Email='string',
              Role='ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER'
          )
        
        **Response Syntax**
        ::
            {
                'User': {
                    'Arn': 'string',
                    'UserName': 'string',
                    'Email': 'string',
                    'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
                    'IdentityType': 'IAM'|'QUICKSIGHT',
                    'Active': True|False,
                    'PrincipalId': 'string'
                },
                'RequestId': 'string',
                'Status': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **User** *(dict) --* 
              The Amazon QuickSight user.
              - **Arn** *(string) --* 
                The Amazon Resource Name (ARN) for the user.
              - **UserName** *(string) --* 
                The user's user name.
              - **Email** *(string) --* 
                The user's email address.
              - **Role** *(string) --* 
                The Amazon QuickSight role for the user.
              - **IdentityType** *(string) --* 
                The type of identity authentication used by the user.
              - **Active** *(boolean) --* 
                Active status of user. When you create an Amazon QuickSight user that’s not an IAM user or an AD user, that user is inactive until they sign in and provide a password
              - **PrincipalId** *(string) --* 
                The principal ID of the user.
            - **RequestId** *(string) --* 
              The AWS request ID for this operation.
            - **Status** *(integer) --* 
              The http status of the request.
        :type UserName: string
        :param UserName: **[REQUIRED]**
          The Amazon QuickSight user name that you want to update.
        :type AwsAccountId: string
        :param AwsAccountId: **[REQUIRED]**
          The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
        :type Namespace: string
        :param Namespace: **[REQUIRED]**
          The namespace. Currently, you should set this to ``default`` .
        :type Email: string
        :param Email: **[REQUIRED]**
          The email address of the user that you want to update.
        :type Role: string
        :param Role: **[REQUIRED]**
          The Amazon QuickSight role of the user. The user role can be one of the following:
          * ``READER`` : A user who has read-only access to dashboards.
          * ``AUTHOR`` : A user who can create data sources, data sets, analyses, and dashboards.
          * ``ADMIN`` : A user who is an author, who can also manage Amazon QuickSight settings.
        :rtype: dict
        :returns:
        """
        pass
