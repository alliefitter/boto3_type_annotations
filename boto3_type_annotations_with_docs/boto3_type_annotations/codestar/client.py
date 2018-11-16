from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def associate_team_member(self, projectId: str, userArn: str, projectRole: str, clientRequestToken: str = None, remoteAccessAllowed: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/AssociateTeamMember>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_team_member(
              projectId=\'string\',
              clientRequestToken=\'string\',
              userArn=\'string\',
              projectRole=\'string\',
              remoteAccessAllowed=True|False
          )
        :type projectId: string
        :param projectId: **[REQUIRED]** 
        
          The ID of the project to which you will add the IAM user.
        
        :type clientRequestToken: string
        :param clientRequestToken: 
        
          A user- or system-generated token that identifies the entity that requested the team member association to the project. This token can be used to repeat the request.
        
        :type userArn: string
        :param userArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) for the IAM user you want to add to the AWS CodeStar project.
        
        :type projectRole: string
        :param projectRole: **[REQUIRED]** 
        
          The AWS CodeStar project role that will apply to this user. This role determines what actions a user can take in an AWS CodeStar project.
        
        :type remoteAccessAllowed: boolean
        :param remoteAccessAllowed: 
        
          Whether the team member is allowed to use an SSH public/private key pair to remotely access project resources, for example Amazon EC2 instances.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'clientRequestToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **clientRequestToken** *(string) --* 
        
              The user- or system-generated token from the initial request that can be used to repeat the request.
        
        """
        pass

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

    def create_project(self, name: str, id: str, description: str = None, clientRequestToken: str = None, sourceCode: List = None, toolchain: Dict = None, tags: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/CreateProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_project(
              name=\'string\',
              id=\'string\',
              description=\'string\',
              clientRequestToken=\'string\',
              sourceCode=[
                  {
                      \'source\': {
                          \'s3\': {
                              \'bucketName\': \'string\',
                              \'bucketKey\': \'string\'
                          }
                      },
                      \'destination\': {
                          \'codeCommit\': {
                              \'name\': \'string\'
                          },
                          \'gitHub\': {
                              \'name\': \'string\',
                              \'description\': \'string\',
                              \'type\': \'string\',
                              \'owner\': \'string\',
                              \'privateRepository\': True|False,
                              \'issuesEnabled\': True|False,
                              \'token\': \'string\'
                          }
                      }
                  },
              ],
              toolchain={
                  \'source\': {
                      \'s3\': {
                          \'bucketName\': \'string\',
                          \'bucketKey\': \'string\'
                      }
                  },
                  \'roleArn\': \'string\',
                  \'stackParameters\': {
                      \'string\': \'string\'
                  }
              },
              tags={
                  \'string\': \'string\'
              }
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The display name for the project to be created in AWS CodeStar.
        
        :type id: string
        :param id: **[REQUIRED]** 
        
          The ID of the project to be created in AWS CodeStar.
        
        :type description: string
        :param description: 
        
          The description of the project, if any.
        
        :type clientRequestToken: string
        :param clientRequestToken: 
        
          A user- or system-generated token that identifies the entity that requested project creation. This token can be used to repeat the request.
        
        :type sourceCode: list
        :param sourceCode: 
        
          A list of the Code objects submitted with the project request. If this parameter is specified, the request must also include the toolchain parameter.
        
          - *(dict) --* 
        
            Location and destination information about the source code files provided with the project request. The source code is uploaded to the new project source repository after project creation.
        
            - **source** *(dict) --* **[REQUIRED]** 
        
              The location where the source code files provided with the project request are stored. AWS CodeStar retrieves the files during project creation.
        
              - **s3** *(dict) --* **[REQUIRED]** 
        
                Information about the Amazon S3 location where the source code files provided with the project request are stored. 
        
                - **bucketName** *(string) --* 
        
                  The Amazon S3 bucket name where the source code files provided with the project request are stored.
        
                - **bucketKey** *(string) --* 
        
                  The Amazon S3 object key where the source code files provided with the project request are stored.
        
            - **destination** *(dict) --* **[REQUIRED]** 
        
              The repository to be created in AWS CodeStar. Valid values are AWS CodeCommit or GitHub. After AWS CodeStar provisions the new repository, the source code files provided with the project request are placed in the repository.
        
              - **codeCommit** *(dict) --* 
        
                Information about the AWS CodeCommit repository to be created in AWS CodeStar. This is where the source code files provided with the project request will be uploaded after project creation.
        
                - **name** *(string) --* **[REQUIRED]** 
        
                  The name of the AWS CodeCommit repository to be created in AWS CodeStar.
        
              - **gitHub** *(dict) --* 
        
                Information about the GitHub repository to be created in AWS CodeStar. This is where the source code files provided with the project request will be uploaded after project creation.
        
                - **name** *(string) --* **[REQUIRED]** 
        
                  Name of the GitHub repository to be created in AWS CodeStar.
        
                - **description** *(string) --* 
        
                  Description for the GitHub repository to be created in AWS CodeStar. This description displays in GitHub after the repository is created.
        
                - **type** *(string) --* **[REQUIRED]** 
        
                  The type of GitHub repository to be created in AWS CodeStar. Valid values are User or Organization.
        
                - **owner** *(string) --* **[REQUIRED]** 
        
                  The GitHub username for the owner of the GitHub repository to be created in AWS CodeStar. If this repository should be owned by a GitHub organization, provide its name.
        
                - **privateRepository** *(boolean) --* **[REQUIRED]** 
        
                  Whether the GitHub repository is to be a private repository.
        
                - **issuesEnabled** *(boolean) --* **[REQUIRED]** 
        
                  Whether to enable issues for the GitHub repository.
        
                - **token** *(string) --* **[REQUIRED]** 
        
                  The GitHub user\'s personal access token for the GitHub repository.
        
        :type toolchain: dict
        :param toolchain: 
        
          The name of the toolchain template file submitted with the project request. If this parameter is specified, the request must also include the sourceCode parameter.
        
          - **source** *(dict) --* **[REQUIRED]** 
        
            The Amazon S3 location where the toolchain template file provided with the project request is stored. AWS CodeStar retrieves the file during project creation.
        
            - **s3** *(dict) --* **[REQUIRED]** 
        
              The Amazon S3 bucket where the toolchain template file provided with the project request is stored.
        
              - **bucketName** *(string) --* 
        
                The Amazon S3 bucket name where the source code files provided with the project request are stored.
        
              - **bucketKey** *(string) --* 
        
                The Amazon S3 object key where the source code files provided with the project request are stored.
        
          - **roleArn** *(string) --* 
        
            The service role ARN for AWS CodeStar to use for the toolchain template during stack provisioning.
        
          - **stackParameters** *(dict) --* 
        
            The list of parameter overrides to be passed into the toolchain template during stack provisioning, if any.
        
            - *(string) --* 
        
              - *(string) --* 
        
        :type tags: dict
        :param tags: 
        
          The tags created for the project.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'id\': \'string\',
                \'arn\': \'string\',
                \'clientRequestToken\': \'string\',
                \'projectTemplateId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **id** *(string) --* 
        
              The ID of the project.
        
            - **arn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the created project.
        
            - **clientRequestToken** *(string) --* 
        
              A user- or system-generated token that identifies the entity that requested project creation.
        
            - **projectTemplateId** *(string) --* 
        
              Reserved for future use.
        
        """
        pass

    def create_user_profile(self, userArn: str, displayName: str, emailAddress: str, sshPublicKey: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/CreateUserProfile>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_user_profile(
              userArn=\'string\',
              displayName=\'string\',
              emailAddress=\'string\',
              sshPublicKey=\'string\'
          )
        :type userArn: string
        :param userArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the user in IAM.
        
        :type displayName: string
        :param displayName: **[REQUIRED]** 
        
          The name that will be displayed as the friendly name for the user in AWS CodeStar. 
        
        :type emailAddress: string
        :param emailAddress: **[REQUIRED]** 
        
          The email address that will be displayed as part of the user\'s profile in AWS CodeStar.
        
        :type sshPublicKey: string
        :param sshPublicKey: 
        
          The SSH public key associated with the user in AWS CodeStar. If a project owner allows the user remote access to project resources, this public key will be used along with the user\'s private key for SSH access.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'userArn\': \'string\',
                \'displayName\': \'string\',
                \'emailAddress\': \'string\',
                \'sshPublicKey\': \'string\',
                \'createdTimestamp\': datetime(2015, 1, 1),
                \'lastModifiedTimestamp\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **userArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the user in IAM.
        
            - **displayName** *(string) --* 
        
              The name that is displayed as the friendly name for the user in AWS CodeStar.
        
            - **emailAddress** *(string) --* 
        
              The email address that is displayed as part of the user\'s profile in AWS CodeStar.
        
            - **sshPublicKey** *(string) --* 
        
              The SSH public key associated with the user in AWS CodeStar. This is the public portion of the public/private keypair the user can use to access project resources if a project owner allows the user remote access to those resources.
        
            - **createdTimestamp** *(datetime) --* 
        
              The date the user profile was created, in timestamp format.
        
            - **lastModifiedTimestamp** *(datetime) --* 
        
              The date the user profile was last modified, in timestamp format.
        
        """
        pass

    def delete_project(self, id: str, clientRequestToken: str = None, deleteStack: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/DeleteProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_project(
              id=\'string\',
              clientRequestToken=\'string\',
              deleteStack=True|False
          )
        :type id: string
        :param id: **[REQUIRED]** 
        
          The ID of the project to be deleted in AWS CodeStar.
        
        :type clientRequestToken: string
        :param clientRequestToken: 
        
          A user- or system-generated token that identifies the entity that requested project deletion. This token can be used to repeat the request. 
        
        :type deleteStack: boolean
        :param deleteStack: 
        
          Whether to send a delete request for the primary stack in AWS CloudFormation originally used to generate the project and its resources. This option will delete all AWS resources for the project (except for any buckets in Amazon S3) as well as deleting the project itself. Recommended for most use cases.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'stackId\': \'string\',
                \'projectArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **stackId** *(string) --* 
        
              The ID of the primary stack in AWS CloudFormation that will be deleted as part of deleting the project and its resources.
        
            - **projectArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the deleted project.
        
        """
        pass

    def delete_user_profile(self, userArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/DeleteUserProfile>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_user_profile(
              userArn=\'string\'
          )
        :type userArn: string
        :param userArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the user to delete from AWS CodeStar.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'userArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **userArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the user deleted from AWS CodeStar.
        
        """
        pass

    def describe_project(self, id: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/DescribeProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_project(
              id=\'string\'
          )
        :type id: string
        :param id: **[REQUIRED]** 
        
          The ID of the project.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'name\': \'string\',
                \'id\': \'string\',
                \'arn\': \'string\',
                \'description\': \'string\',
                \'clientRequestToken\': \'string\',
                \'createdTimeStamp\': datetime(2015, 1, 1),
                \'stackId\': \'string\',
                \'projectTemplateId\': \'string\',
                \'status\': {
                    \'state\': \'string\',
                    \'reason\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **name** *(string) --* 
        
              The display name for the project.
        
            - **id** *(string) --* 
        
              The ID of the project.
        
            - **arn** *(string) --* 
        
              The Amazon Resource Name (ARN) for the project.
        
            - **description** *(string) --* 
        
              The description of the project, if any.
        
            - **clientRequestToken** *(string) --* 
        
              A user- or system-generated token that identifies the entity that requested project creation. 
        
            - **createdTimeStamp** *(datetime) --* 
        
              The date and time the project was created, in timestamp format.
        
            - **stackId** *(string) --* 
        
              The ID of the primary stack in AWS CloudFormation used to generate resources for the project.
        
            - **projectTemplateId** *(string) --* 
        
              The ID for the AWS CodeStar project template used to create the project.
        
            - **status** *(dict) --* 
        
              The project creation or deletion status.
        
              - **state** *(string) --* 
        
                The phase of completion for a project creation or deletion.
        
              - **reason** *(string) --* 
        
                In the case of a project creation or deletion failure, a reason for the failure.
        
        """
        pass

    def describe_user_profile(self, userArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/DescribeUserProfile>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_user_profile(
              userArn=\'string\'
          )
        :type userArn: string
        :param userArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the user.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'userArn\': \'string\',
                \'displayName\': \'string\',
                \'emailAddress\': \'string\',
                \'sshPublicKey\': \'string\',
                \'createdTimestamp\': datetime(2015, 1, 1),
                \'lastModifiedTimestamp\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **userArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the user.
        
            - **displayName** *(string) --* 
        
              The display name shown for the user in AWS CodeStar projects. For example, this could be set to both first and last name (\"Mary Major\") or a single name (\"Mary\"). The display name is also used to generate the initial icon associated with the user in AWS CodeStar projects. If spaces are included in the display name, the first character that appears after the space will be used as the second character in the user initial icon. The initial icon displays a maximum of two characters, so a display name with more than one space (for example \"Mary Jane Major\") would generate an initial icon using the first character and the first character after the space (\"MJ\", not \"MM\").
        
            - **emailAddress** *(string) --* 
        
              The email address for the user. Optional.
        
            - **sshPublicKey** *(string) --* 
        
              The SSH public key associated with the user. This SSH public key is associated with the user profile, and can be used in conjunction with the associated private key for access to project resources, such as Amazon EC2 instances, if a project owner grants remote access to those resources.
        
            - **createdTimestamp** *(datetime) --* 
        
              The date and time when the user profile was created in AWS CodeStar, in timestamp format.
        
            - **lastModifiedTimestamp** *(datetime) --* 
        
              The date and time when the user profile was last modified, in timestamp format.
        
        """
        pass

    def disassociate_team_member(self, projectId: str, userArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/DisassociateTeamMember>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_team_member(
              projectId=\'string\',
              userArn=\'string\'
          )
        :type projectId: string
        :param projectId: **[REQUIRED]** 
        
          The ID of the AWS CodeStar project from which you want to remove a team member.
        
        :type userArn: string
        :param userArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the IAM user or group whom you want to remove from the project.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
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

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_projects(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/ListProjects>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_projects(
              nextToken=\'string\',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken: 
        
          The continuation token to be used to return the next set of results, if the results cannot be returned in one response.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum amount of data that can be contained in a single set of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'projects\': [
                    {
                        \'projectId\': \'string\',
                        \'projectArn\': \'string\'
                    },
                ],
                \'nextToken\': \'string\'
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
        
            - **nextToken** *(string) --* 
        
              The continuation token to use when requesting the next set of results, if there are more results to be returned.
        
        """
        pass

    def list_resources(self, projectId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/ListResources>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_resources(
              projectId=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
        :type projectId: string
        :param projectId: **[REQUIRED]** 
        
          The ID of the project.
        
        :type nextToken: string
        :param nextToken: 
        
          The continuation token for the next set of results, if the results cannot be returned in one response.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum amount of data that can be contained in a single set of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'resources\': [
                    {
                        \'id\': \'string\'
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **resources** *(list) --* 
        
              An array of resources associated with the project. 
        
              - *(dict) --* 
        
                Information about a resource for a project.
        
                - **id** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the resource.
        
            - **nextToken** *(string) --* 
        
              The continuation token to use when requesting the next set of results, if there are more results to be returned.
        
        """
        pass

    def list_tags_for_project(self, id: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/ListTagsForProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags_for_project(
              id=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
        :type id: string
        :param id: **[REQUIRED]** 
        
          The ID of the project to get tags for.
        
        :type nextToken: string
        :param nextToken: 
        
          Reserved for future use.
        
        :type maxResults: integer
        :param maxResults: 
        
          Reserved for future use.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'tags\': {
                    \'string\': \'string\'
                },
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **tags** *(dict) --* 
        
              The tags for the project.
        
              - *(string) --* 
                
                - *(string) --* 
          
            - **nextToken** *(string) --* 
        
              Reserved for future use.
        
        """
        pass

    def list_team_members(self, projectId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/ListTeamMembers>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_team_members(
              projectId=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
        :type projectId: string
        :param projectId: **[REQUIRED]** 
        
          The ID of the project for which you want to list team members.
        
        :type nextToken: string
        :param nextToken: 
        
          The continuation token for the next set of results, if the results cannot be returned in one response.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of team members you want returned in a response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'teamMembers\': [
                    {
                        \'userArn\': \'string\',
                        \'projectRole\': \'string\',
                        \'remoteAccessAllowed\': True|False
                    },
                ],
                \'nextToken\': \'string\'
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
        
            - **nextToken** *(string) --* 
        
              The continuation token to use when requesting the next set of results, if there are more results to be returned.
        
        """
        pass

    def list_user_profiles(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/ListUserProfiles>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_user_profiles(
              nextToken=\'string\',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken: 
        
          The continuation token for the next set of results, if the results cannot be returned in one response.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of results to return in a response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'userProfiles\': [
                    {
                        \'userArn\': \'string\',
                        \'displayName\': \'string\',
                        \'emailAddress\': \'string\',
                        \'sshPublicKey\': \'string\'
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **userProfiles** *(list) --* 
        
              All the user profiles configured in AWS CodeStar for an AWS account.
        
              - *(dict) --* 
        
                Information about a user\'s profile in AWS CodeStar.
        
                - **userArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the user in IAM.
        
                - **displayName** *(string) --* 
        
                  The display name of a user in AWS CodeStar. For example, this could be set to both first and last name (\"Mary Major\") or a single name (\"Mary\"). The display name is also used to generate the initial icon associated with the user in AWS CodeStar projects. If spaces are included in the display name, the first character that appears after the space will be used as the second character in the user initial icon. The initial icon displays a maximum of two characters, so a display name with more than one space (for example \"Mary Jane Major\") would generate an initial icon using the first character and the first character after the space (\"MJ\", not \"MM\").
        
                - **emailAddress** *(string) --* 
        
                  The email address associated with the user.
        
                - **sshPublicKey** *(string) --* 
        
                  The SSH public key associated with the user in AWS CodeStar. If a project owner allows the user remote access to project resources, this public key will be used along with the user\'s private key for SSH access.
        
            - **nextToken** *(string) --* 
        
              The continuation token to use when requesting the next set of results, if there are more results to be returned.
        
        """
        pass

    def tag_project(self, id: str, tags: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/TagProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.tag_project(
              id=\'string\',
              tags={
                  \'string\': \'string\'
              }
          )
        :type id: string
        :param id: **[REQUIRED]** 
        
          The ID of the project you want to add a tag to.
        
        :type tags: dict
        :param tags: **[REQUIRED]** 
        
          The tags you want to add to the project.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'tags\': {
                    \'string\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **tags** *(dict) --* 
        
              The tags for the project.
        
              - *(string) --* 
                
                - *(string) --* 
          
        """
        pass

    def untag_project(self, id: str, tags: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/UntagProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.untag_project(
              id=\'string\',
              tags=[
                  \'string\',
              ]
          )
        :type id: string
        :param id: **[REQUIRED]** 
        
          The ID of the project to remove tags from.
        
        :type tags: list
        :param tags: **[REQUIRED]** 
        
          The tags to remove from the project.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_project(self, id: str, name: str = None, description: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/UpdateProject>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_project(
              id=\'string\',
              name=\'string\',
              description=\'string\'
          )
        :type id: string
        :param id: **[REQUIRED]** 
        
          The ID of the project you want to update.
        
        :type name: string
        :param name: 
        
          The name of the project you want to update.
        
        :type description: string
        :param description: 
        
          The description of the project, if any.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_team_member(self, projectId: str, userArn: str, projectRole: str = None, remoteAccessAllowed: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/UpdateTeamMember>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_team_member(
              projectId=\'string\',
              userArn=\'string\',
              projectRole=\'string\',
              remoteAccessAllowed=True|False
          )
        :type projectId: string
        :param projectId: **[REQUIRED]** 
        
          The ID of the project.
        
        :type userArn: string
        :param userArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the user for whom you want to change team membership attributes.
        
        :type projectRole: string
        :param projectRole: 
        
          The role assigned to the user in the project. Project roles have different levels of access. For more information, see `Working with Teams <http://docs.aws.amazon.com/codestar/latest/userguide/working-with-teams.html>`__ in the *AWS CodeStar User Guide* .
        
        :type remoteAccessAllowed: boolean
        :param remoteAccessAllowed: 
        
          Whether a team member is allowed to remotely access project resources using the SSH public key associated with the user\'s profile. Even if this is set to True, the user must associate a public key with their profile before the user can access resources.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'userArn\': \'string\',
                \'projectRole\': \'string\',
                \'remoteAccessAllowed\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **userArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the user whose team membership attributes were updated.
        
            - **projectRole** *(string) --* 
        
              The project role granted to the user.
        
            - **remoteAccessAllowed** *(boolean) --* 
        
              Whether a team member is allowed to remotely access project resources using the SSH public key associated with the user\'s profile.
        
        """
        pass

    def update_user_profile(self, userArn: str, displayName: str = None, emailAddress: str = None, sshPublicKey: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codestar-2017-04-19/UpdateUserProfile>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_user_profile(
              userArn=\'string\',
              displayName=\'string\',
              emailAddress=\'string\',
              sshPublicKey=\'string\'
          )
        :type userArn: string
        :param userArn: **[REQUIRED]** 
        
          The name that will be displayed as the friendly name for the user in AWS CodeStar.
        
        :type displayName: string
        :param displayName: 
        
          The name that is displayed as the friendly name for the user in AWS CodeStar.
        
        :type emailAddress: string
        :param emailAddress: 
        
          The email address that is displayed as part of the user\'s profile in AWS CodeStar.
        
        :type sshPublicKey: string
        :param sshPublicKey: 
        
          The SSH public key associated with the user in AWS CodeStar. If a project owner allows the user remote access to project resources, this public key will be used along with the user\'s private key for SSH access.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'userArn\': \'string\',
                \'displayName\': \'string\',
                \'emailAddress\': \'string\',
                \'sshPublicKey\': \'string\',
                \'createdTimestamp\': datetime(2015, 1, 1),
                \'lastModifiedTimestamp\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **userArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the user in IAM.
        
            - **displayName** *(string) --* 
        
              The name that is displayed as the friendly name for the user in AWS CodeStar.
        
            - **emailAddress** *(string) --* 
        
              The email address that is displayed as part of the user\'s profile in AWS CodeStar.
        
            - **sshPublicKey** *(string) --* 
        
              The SSH public key associated with the user in AWS CodeStar. This is the public portion of the public/private keypair the user can use to access project resources if a project owner allows the user remote access to those resources.
        
            - **createdTimestamp** *(datetime) --* 
        
              The date the user profile was created, in timestamp format.
        
            - **lastModifiedTimestamp** *(datetime) --* 
        
              The date the user profile was last modified, in timestamp format.
        
        """
        pass
