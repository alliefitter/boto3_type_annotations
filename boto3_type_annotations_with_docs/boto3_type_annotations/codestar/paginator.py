from typing import Dict
from botocore.paginate import Paginator


class ListProjects(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CodeStar.Client.list_projects`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/ListProjects>`_
        
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
                'projects': [
                    {
                        'projectId': 'string',
                        'projectArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **projects** *(list) --* 
              A list of projects.
              - *(dict) --* 
                Information about the metadata for a project.
                - **projectId** *(string) --* 
                  The ID of the project.
                - **projectArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the project.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListResources(Paginator):
    def paginate(self, projectId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CodeStar.Client.list_resources`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/ListResources>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              projectId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'resources': [
                    {
                        'id': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **resources** *(list) --* 
              An array of resources associated with the project. 
              - *(dict) --* 
                Information about a resource for a project.
                - **id** *(string) --* 
                  The Amazon Resource Name (ARN) of the resource.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type projectId: string
        :param projectId: **[REQUIRED]**
          The ID of the project.
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


class ListTeamMembers(Paginator):
    def paginate(self, projectId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CodeStar.Client.list_team_members`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/ListTeamMembers>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              projectId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'teamMembers': [
                    {
                        'userArn': 'string',
                        'projectRole': 'string',
                        'remoteAccessAllowed': True|False
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **teamMembers** *(list) --* 
              A list of team member objects for the project.
              - *(dict) --* 
                Information about a team member in a project.
                - **userArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the user in IAM.
                - **projectRole** *(string) --* 
                  The role assigned to the user in the project. Project roles have different levels of access. For more information, see `Working with Teams <http://docs.aws.amazon.com/codestar/latest/userguide/working-with-teams.html>`__ in the *AWS CodeStar User Guide* . 
                - **remoteAccessAllowed** *(boolean) --* 
                  Whether the user is allowed to remotely access project resources using an SSH public/private key pair.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type projectId: string
        :param projectId: **[REQUIRED]**
          The ID of the project for which you want to list team members.
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


class ListUserProfiles(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`CodeStar.Client.list_user_profiles`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/ListUserProfiles>`_
        
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
                'userProfiles': [
                    {
                        'userArn': 'string',
                        'displayName': 'string',
                        'emailAddress': 'string',
                        'sshPublicKey': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **userProfiles** *(list) --* 
              All the user profiles configured in AWS CodeStar for an AWS account.
              - *(dict) --* 
                Information about a user's profile in AWS CodeStar.
                - **userArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the user in IAM.
                - **displayName** *(string) --* 
                  The display name of a user in AWS CodeStar. For example, this could be set to both first and last name ("Mary Major") or a single name ("Mary"). The display name is also used to generate the initial icon associated with the user in AWS CodeStar projects. If spaces are included in the display name, the first character that appears after the space will be used as the second character in the user initial icon. The initial icon displays a maximum of two characters, so a display name with more than one space (for example "Mary Jane Major") would generate an initial icon using the first character and the first character after the space ("MJ", not "MM").
                - **emailAddress** *(string) --* 
                  The email address associated with the user.
                - **sshPublicKey** *(string) --* 
                  The SSH public key associated with the user in AWS CodeStar. If a project owner allows the user remote access to project resources, this public key will be used along with the user's private key for SSH access.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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
