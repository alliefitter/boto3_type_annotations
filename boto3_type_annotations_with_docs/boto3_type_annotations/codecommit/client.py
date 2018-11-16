from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def batch_get_repositories(self, repositoryNames: List) -> Dict:
        """
        
        .. note::
        
          The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a web page could expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a web page.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/BatchGetRepositories>`_
        
        **Request Syntax** 
        ::
        
          response = client.batch_get_repositories(
              repositoryNames=[
                  \'string\',
              ]
          )
        :type repositoryNames: list
        :param repositoryNames: **[REQUIRED]** 
        
          The names of the repositories to get information about.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'repositories\': [
                    {
                        \'accountId\': \'string\',
                        \'repositoryId\': \'string\',
                        \'repositoryName\': \'string\',
                        \'repositoryDescription\': \'string\',
                        \'defaultBranch\': \'string\',
                        \'lastModifiedDate\': datetime(2015, 1, 1),
                        \'creationDate\': datetime(2015, 1, 1),
                        \'cloneUrlHttp\': \'string\',
                        \'cloneUrlSsh\': \'string\',
                        \'Arn\': \'string\'
                    },
                ],
                \'repositoriesNotFound\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a batch get repositories operation.
        
            - **repositories** *(list) --* 
        
              A list of repositories returned by the batch get repositories operation.
        
              - *(dict) --* 
        
                Information about a repository.
        
                - **accountId** *(string) --* 
        
                  The ID of the AWS account associated with the repository.
        
                - **repositoryId** *(string) --* 
        
                  The ID of the repository.
        
                - **repositoryName** *(string) --* 
        
                  The repository\'s name.
        
                - **repositoryDescription** *(string) --* 
        
                  A comment or description about the repository.
        
                - **defaultBranch** *(string) --* 
        
                  The repository\'s default branch name.
        
                - **lastModifiedDate** *(datetime) --* 
        
                  The date and time the repository was last modified, in timestamp format.
        
                - **creationDate** *(datetime) --* 
        
                  The date and time the repository was created, in timestamp format.
        
                - **cloneUrlHttp** *(string) --* 
        
                  The URL to use for cloning the repository over HTTPS.
        
                - **cloneUrlSsh** *(string) --* 
        
                  The URL to use for cloning the repository over SSH.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the repository.
        
            - **repositoriesNotFound** *(list) --* 
        
              Returns a list of repository names for which information could not be found.
        
              - *(string) --* 
          
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

    def create_branch(self, repositoryName: str, branchName: str, commitId: str) -> NoReturn:
        """
        
        .. note::
        
          Calling the create branch operation does not set a repository\'s default branch. To do this, call the update default branch operation.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/CreateBranch>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_branch(
              repositoryName=\'string\',
              branchName=\'string\',
              commitId=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository in which you want to create the new branch.
        
        :type branchName: string
        :param branchName: **[REQUIRED]** 
        
          The name of the new branch to create.
        
        :type commitId: string
        :param commitId: **[REQUIRED]** 
        
          The ID of the commit to point the new branch to.
        
        :returns: None
        """
        pass

    def create_pull_request(self, title: str, targets: List, description: str = None, clientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/CreatePullRequest>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_pull_request(
              title=\'string\',
              description=\'string\',
              targets=[
                  {
                      \'repositoryName\': \'string\',
                      \'sourceReference\': \'string\',
                      \'destinationReference\': \'string\'
                  },
              ],
              clientRequestToken=\'string\'
          )
        :type title: string
        :param title: **[REQUIRED]** 
        
          The title of the pull request. This title will be used to identify the pull request to other users in the repository.
        
        :type description: string
        :param description: 
        
          A description of the pull request.
        
        :type targets: list
        :param targets: **[REQUIRED]** 
        
          The targets for the pull request, including the source of the code to be reviewed (the source branch), and the destination where the creator of the pull request intends the code to be merged after the pull request is closed (the destination branch).
        
          - *(dict) --* 
        
            Returns information about a target for a pull request.
        
            - **repositoryName** *(string) --* **[REQUIRED]** 
        
              The name of the repository that contains the pull request.
        
            - **sourceReference** *(string) --* **[REQUIRED]** 
        
              The branch of the repository that contains the changes for the pull request. Also known as the source branch.
        
            - **destinationReference** *(string) --* 
        
              The branch of the repository where the pull request changes will be merged into. Also known as the destination branch.
        
        :type clientRequestToken: string
        :param clientRequestToken: 
        
          A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
          .. note::
        
            The AWS SDKs prepopulate client request tokens. If using an AWS SDK, you do not have to generate an idempotency token, as this will be done for you.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pullRequest\': {
                    \'pullRequestId\': \'string\',
                    \'title\': \'string\',
                    \'description\': \'string\',
                    \'lastActivityDate\': datetime(2015, 1, 1),
                    \'creationDate\': datetime(2015, 1, 1),
                    \'pullRequestStatus\': \'OPEN\'|\'CLOSED\',
                    \'authorArn\': \'string\',
                    \'pullRequestTargets\': [
                        {
                            \'repositoryName\': \'string\',
                            \'sourceReference\': \'string\',
                            \'destinationReference\': \'string\',
                            \'destinationCommit\': \'string\',
                            \'sourceCommit\': \'string\',
                            \'mergeBase\': \'string\',
                            \'mergeMetadata\': {
                                \'isMerged\': True|False,
                                \'mergedBy\': \'string\'
                            }
                        },
                    ],
                    \'clientRequestToken\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **pullRequest** *(dict) --* 
        
              Information about the newly created pull request.
        
              - **pullRequestId** *(string) --* 
        
                The system-generated ID of the pull request. 
        
              - **title** *(string) --* 
        
                The user-defined title of the pull request. This title is displayed in the list of pull requests to other users of the repository.
        
              - **description** *(string) --* 
        
                The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.
        
              - **lastActivityDate** *(datetime) --* 
        
                The day and time of the last user or system activity on the pull request, in timestamp format.
        
              - **creationDate** *(datetime) --* 
        
                The date and time the pull request was originally created, in timestamp format.
        
              - **pullRequestStatus** *(string) --* 
        
                The status of the pull request. Pull request status can only change from ``OPEN`` to ``CLOSED`` .
        
              - **authorArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the user who created the pull request.
        
              - **pullRequestTargets** *(list) --* 
        
                The targets of the pull request, including the source branch and destination branch for the pull request.
        
                - *(dict) --* 
        
                  Returns information about a pull request target.
        
                  - **repositoryName** *(string) --* 
        
                    The name of the repository that contains the pull request source and destination branches.
        
                  - **sourceReference** *(string) --* 
        
                    The branch of the repository that contains the changes for the pull request. Also known as the source branch.
        
                  - **destinationReference** *(string) --* 
        
                    The branch of the repository where the pull request changes will be merged into. Also known as the destination branch. 
        
                  - **destinationCommit** *(string) --* 
        
                    The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.
        
                  - **sourceCommit** *(string) --* 
        
                    The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID will change to reflect the new tip of the branch.
        
                  - **mergeBase** *(string) --* 
        
                    The commit ID of the most recent commit that the source branch and the destination branch have in common.
        
                  - **mergeMetadata** *(dict) --* 
        
                    Returns metadata about the state of the merge, including whether the merge has been made.
        
                    - **isMerged** *(boolean) --* 
        
                      A Boolean value indicating whether the merge has been made.
        
                    - **mergedBy** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the user who merged the branches.
        
              - **clientRequestToken** *(string) --* 
        
                A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
        """
        pass

    def create_repository(self, repositoryName: str, repositoryDescription: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/CreateRepository>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_repository(
              repositoryName=\'string\',
              repositoryDescription=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the new repository to be created.
        
          .. note::
        
            The repository name must be unique across the calling AWS account. In addition, repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. For a full description of the limits on repository names, see `Limits <http://docs.aws.amazon.com/codecommit/latest/userguide/limits.html>`__ in the AWS CodeCommit User Guide. The suffix \".git\" is prohibited.
        
        :type repositoryDescription: string
        :param repositoryDescription: 
        
          A comment or description about the new repository.
        
          .. note::
        
            The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a web page could expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a web page.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'repositoryMetadata\': {
                    \'accountId\': \'string\',
                    \'repositoryId\': \'string\',
                    \'repositoryName\': \'string\',
                    \'repositoryDescription\': \'string\',
                    \'defaultBranch\': \'string\',
                    \'lastModifiedDate\': datetime(2015, 1, 1),
                    \'creationDate\': datetime(2015, 1, 1),
                    \'cloneUrlHttp\': \'string\',
                    \'cloneUrlSsh\': \'string\',
                    \'Arn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a create repository operation.
        
            - **repositoryMetadata** *(dict) --* 
        
              Information about the newly created repository.
        
              - **accountId** *(string) --* 
        
                The ID of the AWS account associated with the repository.
        
              - **repositoryId** *(string) --* 
        
                The ID of the repository.
        
              - **repositoryName** *(string) --* 
        
                The repository\'s name.
        
              - **repositoryDescription** *(string) --* 
        
                A comment or description about the repository.
        
              - **defaultBranch** *(string) --* 
        
                The repository\'s default branch name.
        
              - **lastModifiedDate** *(datetime) --* 
        
                The date and time the repository was last modified, in timestamp format.
        
              - **creationDate** *(datetime) --* 
        
                The date and time the repository was created, in timestamp format.
        
              - **cloneUrlHttp** *(string) --* 
        
                The URL to use for cloning the repository over HTTPS.
        
              - **cloneUrlSsh** *(string) --* 
        
                The URL to use for cloning the repository over SSH.
        
              - **Arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the repository.
        
        """
        pass

    def delete_branch(self, repositoryName: str, branchName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DeleteBranch>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_branch(
              repositoryName=\'string\',
              branchName=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository that contains the branch to be deleted.
        
        :type branchName: string
        :param branchName: **[REQUIRED]** 
        
          The name of the branch to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'deletedBranch\': {
                    \'branchName\': \'string\',
                    \'commitId\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a delete branch operation.
        
            - **deletedBranch** *(dict) --* 
        
              Information about the branch deleted by the operation, including the branch name and the commit ID that was the tip of the branch.
        
              - **branchName** *(string) --* 
        
                The name of the branch.
        
              - **commitId** *(string) --* 
        
                The ID of the last commit made to the branch.
        
        """
        pass

    def delete_comment_content(self, commentId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DeleteCommentContent>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_comment_content(
              commentId=\'string\'
          )
        :type commentId: string
        :param commentId: **[REQUIRED]** 
        
          The unique, system-generated ID of the comment. To get this ID, use  GetCommentsForComparedCommit or  GetCommentsForPullRequest .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'comment\': {
                    \'commentId\': \'string\',
                    \'content\': \'string\',
                    \'inReplyTo\': \'string\',
                    \'creationDate\': datetime(2015, 1, 1),
                    \'lastModifiedDate\': datetime(2015, 1, 1),
                    \'authorArn\': \'string\',
                    \'deleted\': True|False,
                    \'clientRequestToken\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **comment** *(dict) --* 
        
              Information about the comment you just deleted.
        
              - **commentId** *(string) --* 
        
                The system-generated comment ID.
        
              - **content** *(string) --* 
        
                The content of the comment.
        
              - **inReplyTo** *(string) --* 
        
                The ID of the comment for which this comment is a reply, if any.
        
              - **creationDate** *(datetime) --* 
        
                The date and time the comment was created, in timestamp format.
        
              - **lastModifiedDate** *(datetime) --* 
        
                The date and time the comment was most recently modified, in timestamp format.
        
              - **authorArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the person who posted the comment.
        
              - **deleted** *(boolean) --* 
        
                A Boolean value indicating whether the comment has been deleted.
        
              - **clientRequestToken** *(string) --* 
        
                A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
        """
        pass

    def delete_file(self, repositoryName: str, branchName: str, filePath: str, parentCommitId: str, keepEmptyFolders: bool = None, commitMessage: str = None, name: str = None, email: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DeleteFile>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_file(
              repositoryName=\'string\',
              branchName=\'string\',
              filePath=\'string\',
              parentCommitId=\'string\',
              keepEmptyFolders=True|False,
              commitMessage=\'string\',
              name=\'string\',
              email=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository that contains the file to delete.
        
        :type branchName: string
        :param branchName: **[REQUIRED]** 
        
          The name of the branch where the commit will be made deleting the file.
        
        :type filePath: string
        :param filePath: **[REQUIRED]** 
        
          The fully-qualified path to the file that will be deleted, including the full name and extension of that file. For example, /examples/file.md is a fully qualified path to a file named file.md in a folder named examples.
        
        :type parentCommitId: string
        :param parentCommitId: **[REQUIRED]** 
        
          The ID of the commit that is the tip of the branch where you want to create the commit that will delete the file. This must be the HEAD commit for the branch. The commit that deletes the file will be created from this commit ID.
        
        :type keepEmptyFolders: boolean
        :param keepEmptyFolders: 
        
          Specifies whether to delete the folder or directory that contains the file you want to delete if that file is the only object in the folder or directory. By default, empty folders will be deleted. This includes empty folders that are part of the directory structure. For example, if the path to a file is dir1/dir2/dir3/dir4, and dir2 and dir3 are empty, deleting the last file in dir4 will also delete the empty folders dir4, dir3, and dir2.
        
        :type commitMessage: string
        :param commitMessage: 
        
          The commit message you want to include as part of deleting the file. Commit messages are limited to 256 KB. If no message is specified, a default message will be used.
        
        :type name: string
        :param name: 
        
          The name of the author of the commit that deletes the file. If no name is specified, the user\'s ARN will be used as the author name and committer name.
        
        :type email: string
        :param email: 
        
          The email address for the commit that deletes the file. If no email address is specified, the email address will be left blank.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'commitId\': \'string\',
                \'blobId\': \'string\',
                \'treeId\': \'string\',
                \'filePath\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **commitId** *(string) --* 
        
              The full commit ID of the commit that contains the change that deletes the file.
        
            - **blobId** *(string) --* 
        
              The blob ID removed from the tree as part of deleting the file.
        
            - **treeId** *(string) --* 
        
              The full SHA-1 pointer of the tree information for the commit that contains the delete file change.
        
            - **filePath** *(string) --* 
        
              The fully-qualified path to the file that will be deleted, including the full name and extension of that file.
        
        """
        pass

    def delete_repository(self, repositoryName: str) -> Dict:
        """
        
        .. warning::
        
          Deleting a repository also deletes all associated objects and metadata. After a repository is deleted, all future push calls to the deleted repository will fail.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DeleteRepository>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_repository(
              repositoryName=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'repositoryId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a delete repository operation.
        
            - **repositoryId** *(string) --* 
        
              The ID of the repository that was deleted.
        
        """
        pass

    def describe_pull_request_events(self, pullRequestId: str, pullRequestEventType: str = None, actorArn: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DescribePullRequestEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_pull_request_events(
              pullRequestId=\'string\',
              pullRequestEventType=\'PULL_REQUEST_CREATED\'|\'PULL_REQUEST_STATUS_CHANGED\'|\'PULL_REQUEST_SOURCE_REFERENCE_UPDATED\'|\'PULL_REQUEST_MERGE_STATE_CHANGED\',
              actorArn=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]** 
        
          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .
        
        :type pullRequestEventType: string
        :param pullRequestEventType: 
        
          Optional. The pull request event type about which you want to return information.
        
        :type actorArn: string
        :param actorArn: 
        
          The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples include updating the pull request with additional commits or changing the status of a pull request.
        
        :type nextToken: string
        :param nextToken: 
        
          An enumeration token that when provided in a request, returns the next batch of the results.
        
        :type maxResults: integer
        :param maxResults: 
        
          A non-negative integer used to limit the number of returned results. The default is 100 events, which is also the maximum number of events that can be returned in a result.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pullRequestEvents\': [
                    {
                        \'pullRequestId\': \'string\',
                        \'eventDate\': datetime(2015, 1, 1),
                        \'pullRequestEventType\': \'PULL_REQUEST_CREATED\'|\'PULL_REQUEST_STATUS_CHANGED\'|\'PULL_REQUEST_SOURCE_REFERENCE_UPDATED\'|\'PULL_REQUEST_MERGE_STATE_CHANGED\',
                        \'actorArn\': \'string\',
                        \'pullRequestCreatedEventMetadata\': {
                            \'repositoryName\': \'string\',
                            \'sourceCommitId\': \'string\',
                            \'destinationCommitId\': \'string\',
                            \'mergeBase\': \'string\'
                        },
                        \'pullRequestStatusChangedEventMetadata\': {
                            \'pullRequestStatus\': \'OPEN\'|\'CLOSED\'
                        },
                        \'pullRequestSourceReferenceUpdatedEventMetadata\': {
                            \'repositoryName\': \'string\',
                            \'beforeCommitId\': \'string\',
                            \'afterCommitId\': \'string\',
                            \'mergeBase\': \'string\'
                        },
                        \'pullRequestMergedStateChangedEventMetadata\': {
                            \'repositoryName\': \'string\',
                            \'destinationReference\': \'string\',
                            \'mergeMetadata\': {
                                \'isMerged\': True|False,
                                \'mergedBy\': \'string\'
                            }
                        }
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **pullRequestEvents** *(list) --* 
        
              Information about the pull request events.
        
              - *(dict) --* 
        
                Returns information about a pull request event.
        
                - **pullRequestId** *(string) --* 
        
                  The system-generated ID of the pull request.
        
                - **eventDate** *(datetime) --* 
        
                  The day and time of the pull request event, in timestamp format.
        
                - **pullRequestEventType** *(string) --* 
        
                  The type of the pull request event, for example a status change event (PULL_REQUEST_STATUS_CHANGED) or update event (PULL_REQUEST_SOURCE_REFERENCE_UPDATED).
        
                - **actorArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples include updating the pull request with additional commits or changing the status of a pull request.
        
                - **pullRequestCreatedEventMetadata** *(dict) --* 
        
                  Information about the source and destination branches for the pull request.
        
                  - **repositoryName** *(string) --* 
        
                    The name of the repository where the pull request was created.
        
                  - **sourceCommitId** *(string) --* 
        
                    The commit ID on the source branch used when the pull request was created.
        
                  - **destinationCommitId** *(string) --* 
        
                    The commit ID of the tip of the branch specified as the destination branch when the pull request was created.
        
                  - **mergeBase** *(string) --* 
        
                    The commit ID of the most recent commit that the source branch and the destination branch have in common.
        
                - **pullRequestStatusChangedEventMetadata** *(dict) --* 
        
                  Information about the change in status for the pull request event.
        
                  - **pullRequestStatus** *(string) --* 
        
                    The changed status of the pull request.
        
                - **pullRequestSourceReferenceUpdatedEventMetadata** *(dict) --* 
        
                  Information about the updated source branch for the pull request event. 
        
                  - **repositoryName** *(string) --* 
        
                    The name of the repository where the pull request was updated.
        
                  - **beforeCommitId** *(string) --* 
        
                    The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was updated.
        
                  - **afterCommitId** *(string) --* 
        
                    The full commit ID of the commit in the source branch that was the tip of the branch at the time the pull request was updated.
        
                  - **mergeBase** *(string) --* 
        
                    The commit ID of the most recent commit that the source branch and the destination branch have in common.
        
                - **pullRequestMergedStateChangedEventMetadata** *(dict) --* 
        
                  Information about the change in mergability state for the pull request event.
        
                  - **repositoryName** *(string) --* 
        
                    The name of the repository where the pull request was created.
        
                  - **destinationReference** *(string) --* 
        
                    The name of the branch that the pull request will be merged into.
        
                  - **mergeMetadata** *(dict) --* 
        
                    Information about the merge state change event.
        
                    - **isMerged** *(boolean) --* 
        
                      A Boolean value indicating whether the merge has been made.
        
                    - **mergedBy** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the user who merged the branches.
        
            - **nextToken** *(string) --* 
        
              An enumeration token that can be used in a request to return the next batch of the results.
        
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

    def get_blob(self, repositoryName: str, blobId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetBlob>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_blob(
              repositoryName=\'string\',
              blobId=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository that contains the blob.
        
        :type blobId: string
        :param blobId: **[REQUIRED]** 
        
          The ID of the blob, which is its SHA-1 pointer.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'content\': b\'bytes\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a get blob operation.
        
            - **content** *(bytes) --* 
        
              The content of the blob, usually a file.
        
        """
        pass

    def get_branch(self, repositoryName: str = None, branchName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetBranch>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_branch(
              repositoryName=\'string\',
              branchName=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: 
        
          The name of the repository that contains the branch for which you want to retrieve information.
        
        :type branchName: string
        :param branchName: 
        
          The name of the branch for which you want to retrieve information.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'branch\': {
                    \'branchName\': \'string\',
                    \'commitId\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a get branch operation.
        
            - **branch** *(dict) --* 
        
              The name of the branch.
        
              - **branchName** *(string) --* 
        
                The name of the branch.
        
              - **commitId** *(string) --* 
        
                The ID of the last commit made to the branch.
        
        """
        pass

    def get_comment(self, commentId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetComment>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_comment(
              commentId=\'string\'
          )
        :type commentId: string
        :param commentId: **[REQUIRED]** 
        
          The unique, system-generated ID of the comment. To get this ID, use  GetCommentsForComparedCommit or  GetCommentsForPullRequest .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'comment\': {
                    \'commentId\': \'string\',
                    \'content\': \'string\',
                    \'inReplyTo\': \'string\',
                    \'creationDate\': datetime(2015, 1, 1),
                    \'lastModifiedDate\': datetime(2015, 1, 1),
                    \'authorArn\': \'string\',
                    \'deleted\': True|False,
                    \'clientRequestToken\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **comment** *(dict) --* 
        
              The contents of the comment.
        
              - **commentId** *(string) --* 
        
                The system-generated comment ID.
        
              - **content** *(string) --* 
        
                The content of the comment.
        
              - **inReplyTo** *(string) --* 
        
                The ID of the comment for which this comment is a reply, if any.
        
              - **creationDate** *(datetime) --* 
        
                The date and time the comment was created, in timestamp format.
        
              - **lastModifiedDate** *(datetime) --* 
        
                The date and time the comment was most recently modified, in timestamp format.
        
              - **authorArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the person who posted the comment.
        
              - **deleted** *(boolean) --* 
        
                A Boolean value indicating whether the comment has been deleted.
        
              - **clientRequestToken** *(string) --* 
        
                A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
        """
        pass

    def get_comments_for_compared_commit(self, repositoryName: str, afterCommitId: str, beforeCommitId: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetCommentsForComparedCommit>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_comments_for_compared_commit(
              repositoryName=\'string\',
              beforeCommitId=\'string\',
              afterCommitId=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository where you want to compare commits.
        
        :type beforeCommitId: string
        :param beforeCommitId: 
        
          To establish the directionality of the comparison, the full commit ID of the \'before\' commit.
        
        :type afterCommitId: string
        :param afterCommitId: **[REQUIRED]** 
        
          To establish the directionality of the comparison, the full commit ID of the \'after\' commit.
        
        :type nextToken: string
        :param nextToken: 
        
          An enumeration token that when provided in a request, returns the next batch of the results. 
        
        :type maxResults: integer
        :param maxResults: 
        
          A non-negative integer used to limit the number of returned results. The default is 100 comments, and is configurable up to 500.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'commentsForComparedCommitData\': [
                    {
                        \'repositoryName\': \'string\',
                        \'beforeCommitId\': \'string\',
                        \'afterCommitId\': \'string\',
                        \'beforeBlobId\': \'string\',
                        \'afterBlobId\': \'string\',
                        \'location\': {
                            \'filePath\': \'string\',
                            \'filePosition\': 123,
                            \'relativeFileVersion\': \'BEFORE\'|\'AFTER\'
                        },
                        \'comments\': [
                            {
                                \'commentId\': \'string\',
                                \'content\': \'string\',
                                \'inReplyTo\': \'string\',
                                \'creationDate\': datetime(2015, 1, 1),
                                \'lastModifiedDate\': datetime(2015, 1, 1),
                                \'authorArn\': \'string\',
                                \'deleted\': True|False,
                                \'clientRequestToken\': \'string\'
                            },
                        ]
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **commentsForComparedCommitData** *(list) --* 
        
              A list of comment objects on the compared commit.
        
              - *(dict) --* 
        
                Returns information about comments on the comparison between two commits.
        
                - **repositoryName** *(string) --* 
        
                  The name of the repository that contains the compared commits.
        
                - **beforeCommitId** *(string) --* 
        
                  The full commit ID of the commit used to establish the \'before\' of the comparison.
        
                - **afterCommitId** *(string) --* 
        
                  The full commit ID of the commit used to establish the \'after\' of the comparison.
        
                - **beforeBlobId** *(string) --* 
        
                  The full blob ID of the commit used to establish the \'before\' of the comparison.
        
                - **afterBlobId** *(string) --* 
        
                  The full blob ID of the commit used to establish the \'after\' of the comparison.
        
                - **location** *(dict) --* 
        
                  Location information about the comment on the comparison, including the file name, line number, and whether the version of the file where the comment was made is \'BEFORE\' or \'AFTER\'.
        
                  - **filePath** *(string) --* 
        
                    The name of the file being compared, including its extension and subdirectory, if any.
        
                  - **filePosition** *(integer) --* 
        
                    The position of a change within a compared file, in line number format.
        
                  - **relativeFileVersion** *(string) --* 
        
                    In a comparison of commits or a pull request, whether the change is in the \'before\' or \'after\' of that comparison.
        
                - **comments** *(list) --* 
        
                  An array of comment objects. Each comment object contains information about a comment on the comparison between commits.
        
                  - *(dict) --* 
        
                    Returns information about a specific comment.
        
                    - **commentId** *(string) --* 
        
                      The system-generated comment ID.
        
                    - **content** *(string) --* 
        
                      The content of the comment.
        
                    - **inReplyTo** *(string) --* 
        
                      The ID of the comment for which this comment is a reply, if any.
        
                    - **creationDate** *(datetime) --* 
        
                      The date and time the comment was created, in timestamp format.
        
                    - **lastModifiedDate** *(datetime) --* 
        
                      The date and time the comment was most recently modified, in timestamp format.
        
                    - **authorArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the person who posted the comment.
        
                    - **deleted** *(boolean) --* 
        
                      A Boolean value indicating whether the comment has been deleted.
        
                    - **clientRequestToken** *(string) --* 
        
                      A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
            - **nextToken** *(string) --* 
        
              An enumeration token that can be used in a request to return the next batch of the results.
        
        """
        pass

    def get_comments_for_pull_request(self, pullRequestId: str, repositoryName: str = None, beforeCommitId: str = None, afterCommitId: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetCommentsForPullRequest>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_comments_for_pull_request(
              pullRequestId=\'string\',
              repositoryName=\'string\',
              beforeCommitId=\'string\',
              afterCommitId=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]** 
        
          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .
        
        :type repositoryName: string
        :param repositoryName: 
        
          The name of the repository that contains the pull request.
        
        :type beforeCommitId: string
        :param beforeCommitId: 
        
          The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was created.
        
        :type afterCommitId: string
        :param afterCommitId: 
        
          The full commit ID of the commit in the source branch that was the tip of the branch at the time the comment was made.
        
        :type nextToken: string
        :param nextToken: 
        
          An enumeration token that when provided in a request, returns the next batch of the results.
        
        :type maxResults: integer
        :param maxResults: 
        
          A non-negative integer used to limit the number of returned results. The default is 100 comments. You can return up to 500 comments with a single request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'commentsForPullRequestData\': [
                    {
                        \'pullRequestId\': \'string\',
                        \'repositoryName\': \'string\',
                        \'beforeCommitId\': \'string\',
                        \'afterCommitId\': \'string\',
                        \'beforeBlobId\': \'string\',
                        \'afterBlobId\': \'string\',
                        \'location\': {
                            \'filePath\': \'string\',
                            \'filePosition\': 123,
                            \'relativeFileVersion\': \'BEFORE\'|\'AFTER\'
                        },
                        \'comments\': [
                            {
                                \'commentId\': \'string\',
                                \'content\': \'string\',
                                \'inReplyTo\': \'string\',
                                \'creationDate\': datetime(2015, 1, 1),
                                \'lastModifiedDate\': datetime(2015, 1, 1),
                                \'authorArn\': \'string\',
                                \'deleted\': True|False,
                                \'clientRequestToken\': \'string\'
                            },
                        ]
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **commentsForPullRequestData** *(list) --* 
        
              An array of comment objects on the pull request.
        
              - *(dict) --* 
        
                Returns information about comments on a pull request.
        
                - **pullRequestId** *(string) --* 
        
                  The system-generated ID of the pull request.
        
                - **repositoryName** *(string) --* 
        
                  The name of the repository that contains the pull request.
        
                - **beforeCommitId** *(string) --* 
        
                  The full commit ID of the commit that was the tip of the destination branch when the pull request was created. This commit will be superceded by the after commit in the source branch when and if you merge the source branch into the destination branch.
        
                - **afterCommitId** *(string) --* 
        
                  he full commit ID of the commit that was the tip of the source branch at the time the comment was made. 
        
                - **beforeBlobId** *(string) --* 
        
                  The full blob ID of the file on which you want to comment on the destination commit.
        
                - **afterBlobId** *(string) --* 
        
                  The full blob ID of the file on which you want to comment on the source commit.
        
                - **location** *(dict) --* 
        
                  Location information about the comment on the pull request, including the file name, line number, and whether the version of the file where the comment was made is \'BEFORE\' (destination branch) or \'AFTER\' (source branch).
        
                  - **filePath** *(string) --* 
        
                    The name of the file being compared, including its extension and subdirectory, if any.
        
                  - **filePosition** *(integer) --* 
        
                    The position of a change within a compared file, in line number format.
        
                  - **relativeFileVersion** *(string) --* 
        
                    In a comparison of commits or a pull request, whether the change is in the \'before\' or \'after\' of that comparison.
        
                - **comments** *(list) --* 
        
                  An array of comment objects. Each comment object contains information about a comment on the pull request.
        
                  - *(dict) --* 
        
                    Returns information about a specific comment.
        
                    - **commentId** *(string) --* 
        
                      The system-generated comment ID.
        
                    - **content** *(string) --* 
        
                      The content of the comment.
        
                    - **inReplyTo** *(string) --* 
        
                      The ID of the comment for which this comment is a reply, if any.
        
                    - **creationDate** *(datetime) --* 
        
                      The date and time the comment was created, in timestamp format.
        
                    - **lastModifiedDate** *(datetime) --* 
        
                      The date and time the comment was most recently modified, in timestamp format.
        
                    - **authorArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the person who posted the comment.
        
                    - **deleted** *(boolean) --* 
        
                      A Boolean value indicating whether the comment has been deleted.
        
                    - **clientRequestToken** *(string) --* 
        
                      A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
            - **nextToken** *(string) --* 
        
              An enumeration token that can be used in a request to return the next batch of the results.
        
        """
        pass

    def get_commit(self, repositoryName: str, commitId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetCommit>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_commit(
              repositoryName=\'string\',
              commitId=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository to which the commit was made.
        
        :type commitId: string
        :param commitId: **[REQUIRED]** 
        
          The commit ID. Commit IDs are the full SHA of the commit.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'commit\': {
                    \'commitId\': \'string\',
                    \'treeId\': \'string\',
                    \'parents\': [
                        \'string\',
                    ],
                    \'message\': \'string\',
                    \'author\': {
                        \'name\': \'string\',
                        \'email\': \'string\',
                        \'date\': \'string\'
                    },
                    \'committer\': {
                        \'name\': \'string\',
                        \'email\': \'string\',
                        \'date\': \'string\'
                    },
                    \'additionalData\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a get commit operation.
        
            - **commit** *(dict) --* 
        
              A commit data type object that contains information about the specified commit.
        
              - **commitId** *(string) --* 
        
                The full SHA of the specified commit. 
        
              - **treeId** *(string) --* 
        
                Tree information for the specified commit.
        
              - **parents** *(list) --* 
        
                A list of parent commits for the specified commit. Each parent commit ID is the full commit ID.
        
                - *(string) --* 
            
              - **message** *(string) --* 
        
                The commit message associated with the specified commit.
        
              - **author** *(dict) --* 
        
                Information about the author of the specified commit. Information includes the date in timestamp format with GMT offset, the name of the author, and the email address for the author, as configured in Git.
        
                - **name** *(string) --* 
        
                  The name of the user who made the specified commit.
        
                - **email** *(string) --* 
        
                  The email address associated with the user who made the commit, if any.
        
                - **date** *(string) --* 
        
                  The date when the specified commit was commited, in timestamp format with GMT offset.
        
              - **committer** *(dict) --* 
        
                Information about the person who committed the specified commit, also known as the committer. Information includes the date in timestamp format with GMT offset, the name of the committer, and the email address for the committer, as configured in Git.
        
                For more information about the difference between an author and a committer in Git, see `Viewing the Commit History <http://git-scm.com/book/ch2-3.html>`__ in Pro Git by Scott Chacon and Ben Straub.
        
                - **name** *(string) --* 
        
                  The name of the user who made the specified commit.
        
                - **email** *(string) --* 
        
                  The email address associated with the user who made the commit, if any.
        
                - **date** *(string) --* 
        
                  The date when the specified commit was commited, in timestamp format with GMT offset.
        
              - **additionalData** *(string) --* 
        
                Any additional data associated with the specified commit.
        
        """
        pass

    def get_differences(self, repositoryName: str, afterCommitSpecifier: str, beforeCommitSpecifier: str = None, beforePath: str = None, afterPath: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetDifferences>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_differences(
              repositoryName=\'string\',
              beforeCommitSpecifier=\'string\',
              afterCommitSpecifier=\'string\',
              beforePath=\'string\',
              afterPath=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository where you want to get differences.
        
        :type beforeCommitSpecifier: string
        :param beforeCommitSpecifier: 
        
          The branch, tag, HEAD, or other fully qualified reference used to identify a commit. For example, the full commit ID. Optional. If not specified, all changes prior to the ``afterCommitSpecifier`` value will be shown. If you do not use ``beforeCommitSpecifier`` in your request, consider limiting the results with ``maxResults`` .
        
        :type afterCommitSpecifier: string
        :param afterCommitSpecifier: **[REQUIRED]** 
        
          The branch, tag, HEAD, or other fully qualified reference used to identify a commit.
        
        :type beforePath: string
        :param beforePath: 
        
          The file path in which to check for differences. Limits the results to this path. Can also be used to specify the previous name of a directory or folder. If ``beforePath`` and ``afterPath`` are not specified, differences will be shown for all paths.
        
        :type afterPath: string
        :param afterPath: 
        
          The file path in which to check differences. Limits the results to this path. Can also be used to specify the changed name of a directory or folder, if it has changed. If not specified, differences will be shown for all paths.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          A non-negative integer used to limit the number of returned results.
        
        :type NextToken: string
        :param NextToken: 
        
          An enumeration token that when provided in a request, returns the next batch of the results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'differences\': [
                    {
                        \'beforeBlob\': {
                            \'blobId\': \'string\',
                            \'path\': \'string\',
                            \'mode\': \'string\'
                        },
                        \'afterBlob\': {
                            \'blobId\': \'string\',
                            \'path\': \'string\',
                            \'mode\': \'string\'
                        },
                        \'changeType\': \'A\'|\'M\'|\'D\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **differences** *(list) --* 
        
              A differences data type object that contains information about the differences, including whether the difference is added, modified, or deleted (A, D, M).
        
              - *(dict) --* 
        
                Returns information about a set of differences for a commit specifier.
        
                - **beforeBlob** *(dict) --* 
        
                  Information about a ``beforeBlob`` data type object, including the ID, the file mode permission code, and the path.
        
                  - **blobId** *(string) --* 
        
                    The full ID of the blob.
        
                  - **path** *(string) --* 
        
                    The path to the blob and any associated file name, if any.
        
                  - **mode** *(string) --* 
        
                    The file mode permissions of the blob. File mode permission codes include:
        
                    * ``100644`` indicates read/write 
                     
                    * ``100755`` indicates read/write/execute 
                     
                    * ``160000`` indicates a submodule 
                     
                    * ``120000`` indicates a symlink 
                     
                - **afterBlob** *(dict) --* 
        
                  Information about an ``afterBlob`` data type object, including the ID, the file mode permission code, and the path.
        
                  - **blobId** *(string) --* 
        
                    The full ID of the blob.
        
                  - **path** *(string) --* 
        
                    The path to the blob and any associated file name, if any.
        
                  - **mode** *(string) --* 
        
                    The file mode permissions of the blob. File mode permission codes include:
        
                    * ``100644`` indicates read/write 
                     
                    * ``100755`` indicates read/write/execute 
                     
                    * ``160000`` indicates a submodule 
                     
                    * ``120000`` indicates a symlink 
                     
                - **changeType** *(string) --* 
        
                  Whether the change type of the difference is an addition (A), deletion (D), or modification (M).
        
            - **NextToken** *(string) --* 
        
              An enumeration token that can be used in a request to return the next batch of the results.
        
        """
        pass

    def get_file(self, repositoryName: str, filePath: str, commitSpecifier: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetFile>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_file(
              repositoryName=\'string\',
              commitSpecifier=\'string\',
              filePath=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository that contains the file.
        
        :type commitSpecifier: string
        :param commitSpecifier: 
        
          The fully-quaified reference that identifies the commit that contains the file. For example, you could specify a full commit ID, a tag, a branch name, or a reference such as refs/heads/master. If none is provided, then the head commit will be used.
        
        :type filePath: string
        :param filePath: **[REQUIRED]** 
        
          The fully-qualified path to the file, including the full name and extension of the file. For example, /examples/file.md is the fully-qualified path to a file named file.md in a folder named examples.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'commitId\': \'string\',
                \'blobId\': \'string\',
                \'filePath\': \'string\',
                \'fileMode\': \'EXECUTABLE\'|\'NORMAL\'|\'SYMLINK\',
                \'fileSize\': 123,
                \'fileContent\': b\'bytes\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **commitId** *(string) --* 
        
              The full commit ID of the commit that contains the content returned by GetFile.
        
            - **blobId** *(string) --* 
        
              The blob ID of the object that represents the file content.
        
            - **filePath** *(string) --* 
        
              The fully qualified path to the specified file. This returns the name and extension of the file.
        
            - **fileMode** *(string) --* 
        
              The extrapolated file mode permissions of the blob. Valid values include strings such as EXECUTABLE and not numeric values.
        
              .. note::
        
                The file mode permissions returned by this API are not the standard file mode permission values, such as 100644, but rather extrapolated values. See below for a full list of supported return values.
        
            - **fileSize** *(integer) --* 
        
              The size of the contents of the file, in bytes.
        
            - **fileContent** *(bytes) --* 
        
              The base-64 encoded binary data object that represents the content of the file.
        
        """
        pass

    def get_folder(self, repositoryName: str, folderPath: str, commitSpecifier: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetFolder>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_folder(
              repositoryName=\'string\',
              commitSpecifier=\'string\',
              folderPath=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository.
        
        :type commitSpecifier: string
        :param commitSpecifier: 
        
          A fully-qualified reference used to identify a commit that contains the version of the folder\'s content to return. A fully-qualified reference can be a commit ID, branch name, tag, or reference such as HEAD. If no specifier is provided, the folder content will be returned as it exists in the HEAD commit.
        
        :type folderPath: string
        :param folderPath: **[REQUIRED]** 
        
          The fully-qualified path to the folder whose contents will be returned, including the folder name. For example, /examples is a fully-qualified path to a folder named examples that was created off of the root directory (/) of a repository. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'commitId\': \'string\',
                \'folderPath\': \'string\',
                \'treeId\': \'string\',
                \'subFolders\': [
                    {
                        \'treeId\': \'string\',
                        \'absolutePath\': \'string\',
                        \'relativePath\': \'string\'
                    },
                ],
                \'files\': [
                    {
                        \'blobId\': \'string\',
                        \'absolutePath\': \'string\',
                        \'relativePath\': \'string\',
                        \'fileMode\': \'EXECUTABLE\'|\'NORMAL\'|\'SYMLINK\'
                    },
                ],
                \'symbolicLinks\': [
                    {
                        \'blobId\': \'string\',
                        \'absolutePath\': \'string\',
                        \'relativePath\': \'string\',
                        \'fileMode\': \'EXECUTABLE\'|\'NORMAL\'|\'SYMLINK\'
                    },
                ],
                \'subModules\': [
                    {
                        \'commitId\': \'string\',
                        \'absolutePath\': \'string\',
                        \'relativePath\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **commitId** *(string) --* 
        
              The full commit ID used as a reference for which version of the folder content is returned.
        
            - **folderPath** *(string) --* 
        
              The fully-qualified path of the folder whose contents are returned.
        
            - **treeId** *(string) --* 
        
              The full SHA-1 pointer of the tree information for the commit that contains the folder.
        
            - **subFolders** *(list) --* 
        
              The list of folders that exist beneath the specified folder, if any.
        
              - *(dict) --* 
        
                Returns information about a folder in a repository.
        
                - **treeId** *(string) --* 
        
                  The full SHA-1 pointer of the tree information for the commit that contains the folder.
        
                - **absolutePath** *(string) --* 
        
                  The fully-qualified path of the folder in the repository.
        
                - **relativePath** *(string) --* 
        
                  The relative path of the specified folder from the folder where the query originated.
        
            - **files** *(list) --* 
        
              The list of files that exist in the specified folder, if any.
        
              - *(dict) --* 
        
                Returns information about a file in a repository.
        
                - **blobId** *(string) --* 
        
                  The blob ID that contains the file information.
        
                - **absolutePath** *(string) --* 
        
                  The fully-qualified path to the file in the repository.
        
                - **relativePath** *(string) --* 
        
                  The relative path of the file from the folder where the query originated.
        
                - **fileMode** *(string) --* 
        
                  The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.
        
            - **symbolicLinks** *(list) --* 
        
              The list of symbolic links to other files and folders that exist in the specified folder, if any.
        
              - *(dict) --* 
        
                Returns information about a symbolic link in a repository folder.
        
                - **blobId** *(string) --* 
        
                  The blob ID that contains the information about the symbolic link.
        
                - **absolutePath** *(string) --* 
        
                  The fully-qualified path to the folder that contains the symbolic link.
        
                - **relativePath** *(string) --* 
        
                  The relative path of the symbolic link from the folder where the query originated.
        
                - **fileMode** *(string) --* 
        
                  The file mode permissions of the blob that cotains information about the symbolic link.
        
            - **subModules** *(list) --* 
        
              The list of submodules that exist in the specified folder, if any.
        
              - *(dict) --* 
        
                Returns information about a submodule reference in a repository folder.
        
                - **commitId** *(string) --* 
        
                  The commit ID that contains the reference to the submodule.
        
                - **absolutePath** *(string) --* 
        
                  The fully qualified path to the folder that contains the reference to the submodule.
        
                - **relativePath** *(string) --* 
        
                  The relative path of the submodule from the folder where the query originated.
        
        """
        pass

    def get_merge_conflicts(self, repositoryName: str, destinationCommitSpecifier: str, sourceCommitSpecifier: str, mergeOption: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetMergeConflicts>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_merge_conflicts(
              repositoryName=\'string\',
              destinationCommitSpecifier=\'string\',
              sourceCommitSpecifier=\'string\',
              mergeOption=\'FAST_FORWARD_MERGE\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository where the pull request was created.
        
        :type destinationCommitSpecifier: string
        :param destinationCommitSpecifier: **[REQUIRED]** 
        
          The branch, tag, HEAD, or other fully qualified reference used to identify a commit. For example, a branch name or a full commit ID.
        
        :type sourceCommitSpecifier: string
        :param sourceCommitSpecifier: **[REQUIRED]** 
        
          The branch, tag, HEAD, or other fully qualified reference used to identify a commit. For example, a branch name or a full commit ID.
        
        :type mergeOption: string
        :param mergeOption: **[REQUIRED]** 
        
          The merge option or strategy you want to use to merge the code. The only valid value is FAST_FORWARD_MERGE.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'mergeable\': True|False,
                \'destinationCommitId\': \'string\',
                \'sourceCommitId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **mergeable** *(boolean) --* 
        
              A Boolean value that indicates whether the code is mergable by the specified merge option.
        
            - **destinationCommitId** *(string) --* 
        
              The commit ID of the destination commit specifier that was used in the merge evaluation.
        
            - **sourceCommitId** *(string) --* 
        
              The commit ID of the source commit specifier that was used in the merge evaluation.
        
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

    def get_pull_request(self, pullRequestId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetPullRequest>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_pull_request(
              pullRequestId=\'string\'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]** 
        
          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pullRequest\': {
                    \'pullRequestId\': \'string\',
                    \'title\': \'string\',
                    \'description\': \'string\',
                    \'lastActivityDate\': datetime(2015, 1, 1),
                    \'creationDate\': datetime(2015, 1, 1),
                    \'pullRequestStatus\': \'OPEN\'|\'CLOSED\',
                    \'authorArn\': \'string\',
                    \'pullRequestTargets\': [
                        {
                            \'repositoryName\': \'string\',
                            \'sourceReference\': \'string\',
                            \'destinationReference\': \'string\',
                            \'destinationCommit\': \'string\',
                            \'sourceCommit\': \'string\',
                            \'mergeBase\': \'string\',
                            \'mergeMetadata\': {
                                \'isMerged\': True|False,
                                \'mergedBy\': \'string\'
                            }
                        },
                    ],
                    \'clientRequestToken\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **pullRequest** *(dict) --* 
        
              Information about the specified pull request.
        
              - **pullRequestId** *(string) --* 
        
                The system-generated ID of the pull request. 
        
              - **title** *(string) --* 
        
                The user-defined title of the pull request. This title is displayed in the list of pull requests to other users of the repository.
        
              - **description** *(string) --* 
        
                The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.
        
              - **lastActivityDate** *(datetime) --* 
        
                The day and time of the last user or system activity on the pull request, in timestamp format.
        
              - **creationDate** *(datetime) --* 
        
                The date and time the pull request was originally created, in timestamp format.
        
              - **pullRequestStatus** *(string) --* 
        
                The status of the pull request. Pull request status can only change from ``OPEN`` to ``CLOSED`` .
        
              - **authorArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the user who created the pull request.
        
              - **pullRequestTargets** *(list) --* 
        
                The targets of the pull request, including the source branch and destination branch for the pull request.
        
                - *(dict) --* 
        
                  Returns information about a pull request target.
        
                  - **repositoryName** *(string) --* 
        
                    The name of the repository that contains the pull request source and destination branches.
        
                  - **sourceReference** *(string) --* 
        
                    The branch of the repository that contains the changes for the pull request. Also known as the source branch.
        
                  - **destinationReference** *(string) --* 
        
                    The branch of the repository where the pull request changes will be merged into. Also known as the destination branch. 
        
                  - **destinationCommit** *(string) --* 
        
                    The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.
        
                  - **sourceCommit** *(string) --* 
        
                    The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID will change to reflect the new tip of the branch.
        
                  - **mergeBase** *(string) --* 
        
                    The commit ID of the most recent commit that the source branch and the destination branch have in common.
        
                  - **mergeMetadata** *(dict) --* 
        
                    Returns metadata about the state of the merge, including whether the merge has been made.
        
                    - **isMerged** *(boolean) --* 
        
                      A Boolean value indicating whether the merge has been made.
        
                    - **mergedBy** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the user who merged the branches.
        
              - **clientRequestToken** *(string) --* 
        
                A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
        """
        pass

    def get_repository(self, repositoryName: str) -> Dict:
        """
        
        .. note::
        
          The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a web page could expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a web page.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetRepository>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_repository(
              repositoryName=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository to get information about.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'repositoryMetadata\': {
                    \'accountId\': \'string\',
                    \'repositoryId\': \'string\',
                    \'repositoryName\': \'string\',
                    \'repositoryDescription\': \'string\',
                    \'defaultBranch\': \'string\',
                    \'lastModifiedDate\': datetime(2015, 1, 1),
                    \'creationDate\': datetime(2015, 1, 1),
                    \'cloneUrlHttp\': \'string\',
                    \'cloneUrlSsh\': \'string\',
                    \'Arn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a get repository operation.
        
            - **repositoryMetadata** *(dict) --* 
        
              Information about the repository.
        
              - **accountId** *(string) --* 
        
                The ID of the AWS account associated with the repository.
        
              - **repositoryId** *(string) --* 
        
                The ID of the repository.
        
              - **repositoryName** *(string) --* 
        
                The repository\'s name.
        
              - **repositoryDescription** *(string) --* 
        
                A comment or description about the repository.
        
              - **defaultBranch** *(string) --* 
        
                The repository\'s default branch name.
        
              - **lastModifiedDate** *(datetime) --* 
        
                The date and time the repository was last modified, in timestamp format.
        
              - **creationDate** *(datetime) --* 
        
                The date and time the repository was created, in timestamp format.
        
              - **cloneUrlHttp** *(string) --* 
        
                The URL to use for cloning the repository over HTTPS.
        
              - **cloneUrlSsh** *(string) --* 
        
                The URL to use for cloning the repository over SSH.
        
              - **Arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the repository.
        
        """
        pass

    def get_repository_triggers(self, repositoryName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetRepositoryTriggers>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_repository_triggers(
              repositoryName=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository for which the trigger is configured.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'configurationId\': \'string\',
                \'triggers\': [
                    {
                        \'name\': \'string\',
                        \'destinationArn\': \'string\',
                        \'customData\': \'string\',
                        \'branches\': [
                            \'string\',
                        ],
                        \'events\': [
                            \'all\'|\'updateReference\'|\'createReference\'|\'deleteReference\',
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a get repository triggers operation.
        
            - **configurationId** *(string) --* 
        
              The system-generated unique ID for the trigger.
        
            - **triggers** *(list) --* 
        
              The JSON block of configuration information for each trigger.
        
              - *(dict) --* 
        
                Information about a trigger for a repository.
        
                - **name** *(string) --* 
        
                  The name of the trigger.
        
                - **destinationArn** *(string) --* 
        
                  The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).
        
                - **customData** *(string) --* 
        
                  Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.
        
                - **branches** *(list) --* 
        
                  The branches that will be included in the trigger configuration. If you specify an empty array, the trigger will apply to all branches.
        
                  .. note::
        
                    While no content is required in the array, you must include the array itself.
        
                  - *(string) --* 
              
                - **events** *(list) --* 
        
                  The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS). 
        
                  .. note::
        
                    The valid value \"all\" cannot be used with any other values.
        
                  - *(string) --* 
              
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

    def list_branches(self, repositoryName: str, nextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/ListBranches>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_branches(
              repositoryName=\'string\',
              nextToken=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository that contains the branches.
        
        :type nextToken: string
        :param nextToken: 
        
          An enumeration token that allows the operation to batch the results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'branches\': [
                    \'string\',
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a list branches operation.
        
            - **branches** *(list) --* 
        
              The list of branch names.
        
              - *(string) --* 
          
            - **nextToken** *(string) --* 
        
              An enumeration token that returns the batch of the results.
        
        """
        pass

    def list_pull_requests(self, repositoryName: str, authorArn: str = None, pullRequestStatus: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/ListPullRequests>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_pull_requests(
              repositoryName=\'string\',
              authorArn=\'string\',
              pullRequestStatus=\'OPEN\'|\'CLOSED\',
              nextToken=\'string\',
              maxResults=123
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository for which you want to list pull requests.
        
        :type authorArn: string
        :param authorArn: 
        
          Optional. The Amazon Resource Name (ARN) of the user who created the pull request. If used, this filters the results to pull requests created by that user.
        
        :type pullRequestStatus: string
        :param pullRequestStatus: 
        
          Optional. The status of the pull request. If used, this refines the results to the pull requests that match the specified status.
        
        :type nextToken: string
        :param nextToken: 
        
          An enumeration token that when provided in a request, returns the next batch of the results.
        
        :type maxResults: integer
        :param maxResults: 
        
          A non-negative integer used to limit the number of returned results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pullRequestIds\': [
                    \'string\',
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **pullRequestIds** *(list) --* 
        
              The system-generated IDs of the pull requests.
        
              - *(string) --* 
          
            - **nextToken** *(string) --* 
        
              An enumeration token that when provided in a request, returns the next batch of the results.
        
        """
        pass

    def list_repositories(self, nextToken: str = None, sortBy: str = None, order: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/ListRepositories>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_repositories(
              nextToken=\'string\',
              sortBy=\'repositoryName\'|\'lastModifiedDate\',
              order=\'ascending\'|\'descending\'
          )
        :type nextToken: string
        :param nextToken: 
        
          An enumeration token that allows the operation to batch the results of the operation. Batch sizes are 1,000 for list repository operations. When the client sends the token back to AWS CodeCommit, another page of 1,000 records is retrieved.
        
        :type sortBy: string
        :param sortBy: 
        
          The criteria used to sort the results of a list repositories operation.
        
        :type order: string
        :param order: 
        
          The order in which to sort the results of a list repositories operation.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'repositories\': [
                    {
                        \'repositoryName\': \'string\',
                        \'repositoryId\': \'string\'
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a list repositories operation.
        
            - **repositories** *(list) --* 
        
              Lists the repositories called by the list repositories operation.
        
              - *(dict) --* 
        
                Information about a repository name and ID.
        
                - **repositoryName** *(string) --* 
        
                  The name associated with the repository.
        
                - **repositoryId** *(string) --* 
        
                  The ID associated with the repository.
        
            - **nextToken** *(string) --* 
        
              An enumeration token that allows the operation to batch the results of the operation. Batch sizes are 1,000 for list repository operations. When the client sends the token back to AWS CodeCommit, another page of 1,000 records is retrieved.
        
        """
        pass

    def merge_pull_request_by_fast_forward(self, pullRequestId: str, repositoryName: str, sourceCommitId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/MergePullRequestByFastForward>`_
        
        **Request Syntax** 
        ::
        
          response = client.merge_pull_request_by_fast_forward(
              pullRequestId=\'string\',
              repositoryName=\'string\',
              sourceCommitId=\'string\'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]** 
        
          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository where the pull request was created.
        
        :type sourceCommitId: string
        :param sourceCommitId: 
        
          The full commit ID of the original or updated commit in the pull request source branch. Pass this value if you want an exception thrown if the current commit ID of the tip of the source branch does not match this commit ID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pullRequest\': {
                    \'pullRequestId\': \'string\',
                    \'title\': \'string\',
                    \'description\': \'string\',
                    \'lastActivityDate\': datetime(2015, 1, 1),
                    \'creationDate\': datetime(2015, 1, 1),
                    \'pullRequestStatus\': \'OPEN\'|\'CLOSED\',
                    \'authorArn\': \'string\',
                    \'pullRequestTargets\': [
                        {
                            \'repositoryName\': \'string\',
                            \'sourceReference\': \'string\',
                            \'destinationReference\': \'string\',
                            \'destinationCommit\': \'string\',
                            \'sourceCommit\': \'string\',
                            \'mergeBase\': \'string\',
                            \'mergeMetadata\': {
                                \'isMerged\': True|False,
                                \'mergedBy\': \'string\'
                            }
                        },
                    ],
                    \'clientRequestToken\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **pullRequest** *(dict) --* 
        
              Information about the specified pull request, including information about the merge.
        
              - **pullRequestId** *(string) --* 
        
                The system-generated ID of the pull request. 
        
              - **title** *(string) --* 
        
                The user-defined title of the pull request. This title is displayed in the list of pull requests to other users of the repository.
        
              - **description** *(string) --* 
        
                The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.
        
              - **lastActivityDate** *(datetime) --* 
        
                The day and time of the last user or system activity on the pull request, in timestamp format.
        
              - **creationDate** *(datetime) --* 
        
                The date and time the pull request was originally created, in timestamp format.
        
              - **pullRequestStatus** *(string) --* 
        
                The status of the pull request. Pull request status can only change from ``OPEN`` to ``CLOSED`` .
        
              - **authorArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the user who created the pull request.
        
              - **pullRequestTargets** *(list) --* 
        
                The targets of the pull request, including the source branch and destination branch for the pull request.
        
                - *(dict) --* 
        
                  Returns information about a pull request target.
        
                  - **repositoryName** *(string) --* 
        
                    The name of the repository that contains the pull request source and destination branches.
        
                  - **sourceReference** *(string) --* 
        
                    The branch of the repository that contains the changes for the pull request. Also known as the source branch.
        
                  - **destinationReference** *(string) --* 
        
                    The branch of the repository where the pull request changes will be merged into. Also known as the destination branch. 
        
                  - **destinationCommit** *(string) --* 
        
                    The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.
        
                  - **sourceCommit** *(string) --* 
        
                    The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID will change to reflect the new tip of the branch.
        
                  - **mergeBase** *(string) --* 
        
                    The commit ID of the most recent commit that the source branch and the destination branch have in common.
        
                  - **mergeMetadata** *(dict) --* 
        
                    Returns metadata about the state of the merge, including whether the merge has been made.
        
                    - **isMerged** *(boolean) --* 
        
                      A Boolean value indicating whether the merge has been made.
        
                    - **mergedBy** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the user who merged the branches.
        
              - **clientRequestToken** *(string) --* 
        
                A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
        """
        pass

    def post_comment_for_compared_commit(self, repositoryName: str, afterCommitId: str, content: str, beforeCommitId: str = None, location: Dict = None, clientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/PostCommentForComparedCommit>`_
        
        **Request Syntax** 
        ::
        
          response = client.post_comment_for_compared_commit(
              repositoryName=\'string\',
              beforeCommitId=\'string\',
              afterCommitId=\'string\',
              location={
                  \'filePath\': \'string\',
                  \'filePosition\': 123,
                  \'relativeFileVersion\': \'BEFORE\'|\'AFTER\'
              },
              content=\'string\',
              clientRequestToken=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository where you want to post a comment on the comparison between commits.
        
        :type beforeCommitId: string
        :param beforeCommitId: 
        
          To establish the directionality of the comparison, the full commit ID of the \'before\' commit.
        
        :type afterCommitId: string
        :param afterCommitId: **[REQUIRED]** 
        
          To establish the directionality of the comparison, the full commit ID of the \'after\' commit.
        
        :type location: dict
        :param location: 
        
          The location of the comparison where you want to comment.
        
          - **filePath** *(string) --* 
        
            The name of the file being compared, including its extension and subdirectory, if any.
        
          - **filePosition** *(integer) --* 
        
            The position of a change within a compared file, in line number format.
        
          - **relativeFileVersion** *(string) --* 
        
            In a comparison of commits or a pull request, whether the change is in the \'before\' or \'after\' of that comparison.
        
        :type content: string
        :param content: **[REQUIRED]** 
        
          The content of the comment you want to make.
        
        :type clientRequestToken: string
        :param clientRequestToken: 
        
          A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'repositoryName\': \'string\',
                \'beforeCommitId\': \'string\',
                \'afterCommitId\': \'string\',
                \'beforeBlobId\': \'string\',
                \'afterBlobId\': \'string\',
                \'location\': {
                    \'filePath\': \'string\',
                    \'filePosition\': 123,
                    \'relativeFileVersion\': \'BEFORE\'|\'AFTER\'
                },
                \'comment\': {
                    \'commentId\': \'string\',
                    \'content\': \'string\',
                    \'inReplyTo\': \'string\',
                    \'creationDate\': datetime(2015, 1, 1),
                    \'lastModifiedDate\': datetime(2015, 1, 1),
                    \'authorArn\': \'string\',
                    \'deleted\': True|False,
                    \'clientRequestToken\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **repositoryName** *(string) --* 
        
              The name of the repository where you posted a comment on the comparison between commits.
        
            - **beforeCommitId** *(string) --* 
        
              In the directionality you established, the full commit ID of the \'before\' commit.
        
            - **afterCommitId** *(string) --* 
        
              In the directionality you established, the full commit ID of the \'after\' commit.
        
            - **beforeBlobId** *(string) --* 
        
              In the directionality you established, the blob ID of the \'before\' blob.
        
            - **afterBlobId** *(string) --* 
        
              In the directionality you established, the blob ID of the \'after\' blob.
        
            - **location** *(dict) --* 
        
              The location of the comment in the comparison between the two commits.
        
              - **filePath** *(string) --* 
        
                The name of the file being compared, including its extension and subdirectory, if any.
        
              - **filePosition** *(integer) --* 
        
                The position of a change within a compared file, in line number format.
        
              - **relativeFileVersion** *(string) --* 
        
                In a comparison of commits or a pull request, whether the change is in the \'before\' or \'after\' of that comparison.
        
            - **comment** *(dict) --* 
        
              The content of the comment you posted.
        
              - **commentId** *(string) --* 
        
                The system-generated comment ID.
        
              - **content** *(string) --* 
        
                The content of the comment.
        
              - **inReplyTo** *(string) --* 
        
                The ID of the comment for which this comment is a reply, if any.
        
              - **creationDate** *(datetime) --* 
        
                The date and time the comment was created, in timestamp format.
        
              - **lastModifiedDate** *(datetime) --* 
        
                The date and time the comment was most recently modified, in timestamp format.
        
              - **authorArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the person who posted the comment.
        
              - **deleted** *(boolean) --* 
        
                A Boolean value indicating whether the comment has been deleted.
        
              - **clientRequestToken** *(string) --* 
        
                A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
        """
        pass

    def post_comment_for_pull_request(self, pullRequestId: str, repositoryName: str, beforeCommitId: str, afterCommitId: str, content: str, location: Dict = None, clientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/PostCommentForPullRequest>`_
        
        **Request Syntax** 
        ::
        
          response = client.post_comment_for_pull_request(
              pullRequestId=\'string\',
              repositoryName=\'string\',
              beforeCommitId=\'string\',
              afterCommitId=\'string\',
              location={
                  \'filePath\': \'string\',
                  \'filePosition\': 123,
                  \'relativeFileVersion\': \'BEFORE\'|\'AFTER\'
              },
              content=\'string\',
              clientRequestToken=\'string\'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]** 
        
          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .
        
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository where you want to post a comment on a pull request.
        
        :type beforeCommitId: string
        :param beforeCommitId: **[REQUIRED]** 
        
          The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was created.
        
        :type afterCommitId: string
        :param afterCommitId: **[REQUIRED]** 
        
          The full commit ID of the commit in the source branch that is the current tip of the branch for the pull request when you post the comment.
        
        :type location: dict
        :param location: 
        
          The location of the change where you want to post your comment. If no location is provided, the comment will be posted as a general comment on the pull request difference between the before commit ID and the after commit ID.
        
          - **filePath** *(string) --* 
        
            The name of the file being compared, including its extension and subdirectory, if any.
        
          - **filePosition** *(integer) --* 
        
            The position of a change within a compared file, in line number format.
        
          - **relativeFileVersion** *(string) --* 
        
            In a comparison of commits or a pull request, whether the change is in the \'before\' or \'after\' of that comparison.
        
        :type content: string
        :param content: **[REQUIRED]** 
        
          The content of your comment on the change.
        
        :type clientRequestToken: string
        :param clientRequestToken: 
        
          A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'repositoryName\': \'string\',
                \'pullRequestId\': \'string\',
                \'beforeCommitId\': \'string\',
                \'afterCommitId\': \'string\',
                \'beforeBlobId\': \'string\',
                \'afterBlobId\': \'string\',
                \'location\': {
                    \'filePath\': \'string\',
                    \'filePosition\': 123,
                    \'relativeFileVersion\': \'BEFORE\'|\'AFTER\'
                },
                \'comment\': {
                    \'commentId\': \'string\',
                    \'content\': \'string\',
                    \'inReplyTo\': \'string\',
                    \'creationDate\': datetime(2015, 1, 1),
                    \'lastModifiedDate\': datetime(2015, 1, 1),
                    \'authorArn\': \'string\',
                    \'deleted\': True|False,
                    \'clientRequestToken\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **repositoryName** *(string) --* 
        
              The name of the repository where you posted a comment on a pull request.
        
            - **pullRequestId** *(string) --* 
        
              The system-generated ID of the pull request. 
        
            - **beforeCommitId** *(string) --* 
        
              The full commit ID of the commit in the source branch used to create the pull request, or in the case of an updated pull request, the full commit ID of the commit used to update the pull request.
        
            - **afterCommitId** *(string) --* 
        
              The full commit ID of the commit in the destination branch where the pull request will be merged.
        
            - **beforeBlobId** *(string) --* 
        
              In the directionality of the pull request, the blob ID of the \'before\' blob.
        
            - **afterBlobId** *(string) --* 
        
              In the directionality of the pull request, the blob ID of the \'after\' blob.
        
            - **location** *(dict) --* 
        
              The location of the change where you posted your comment.
        
              - **filePath** *(string) --* 
        
                The name of the file being compared, including its extension and subdirectory, if any.
        
              - **filePosition** *(integer) --* 
        
                The position of a change within a compared file, in line number format.
        
              - **relativeFileVersion** *(string) --* 
        
                In a comparison of commits or a pull request, whether the change is in the \'before\' or \'after\' of that comparison.
        
            - **comment** *(dict) --* 
        
              The content of the comment you posted.
        
              - **commentId** *(string) --* 
        
                The system-generated comment ID.
        
              - **content** *(string) --* 
        
                The content of the comment.
        
              - **inReplyTo** *(string) --* 
        
                The ID of the comment for which this comment is a reply, if any.
        
              - **creationDate** *(datetime) --* 
        
                The date and time the comment was created, in timestamp format.
        
              - **lastModifiedDate** *(datetime) --* 
        
                The date and time the comment was most recently modified, in timestamp format.
        
              - **authorArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the person who posted the comment.
        
              - **deleted** *(boolean) --* 
        
                A Boolean value indicating whether the comment has been deleted.
        
              - **clientRequestToken** *(string) --* 
        
                A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
        """
        pass

    def post_comment_reply(self, inReplyTo: str, content: str, clientRequestToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/PostCommentReply>`_
        
        **Request Syntax** 
        ::
        
          response = client.post_comment_reply(
              inReplyTo=\'string\',
              clientRequestToken=\'string\',
              content=\'string\'
          )
        :type inReplyTo: string
        :param inReplyTo: **[REQUIRED]** 
        
          The system-generated ID of the comment to which you want to reply. To get this ID, use  GetCommentsForComparedCommit or  GetCommentsForPullRequest .
        
        :type clientRequestToken: string
        :param clientRequestToken: 
        
          A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
          This field is autopopulated if not provided.
        
        :type content: string
        :param content: **[REQUIRED]** 
        
          The contents of your reply to a comment.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'comment\': {
                    \'commentId\': \'string\',
                    \'content\': \'string\',
                    \'inReplyTo\': \'string\',
                    \'creationDate\': datetime(2015, 1, 1),
                    \'lastModifiedDate\': datetime(2015, 1, 1),
                    \'authorArn\': \'string\',
                    \'deleted\': True|False,
                    \'clientRequestToken\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **comment** *(dict) --* 
        
              Information about the reply to a comment.
        
              - **commentId** *(string) --* 
        
                The system-generated comment ID.
        
              - **content** *(string) --* 
        
                The content of the comment.
        
              - **inReplyTo** *(string) --* 
        
                The ID of the comment for which this comment is a reply, if any.
        
              - **creationDate** *(datetime) --* 
        
                The date and time the comment was created, in timestamp format.
        
              - **lastModifiedDate** *(datetime) --* 
        
                The date and time the comment was most recently modified, in timestamp format.
        
              - **authorArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the person who posted the comment.
        
              - **deleted** *(boolean) --* 
        
                A Boolean value indicating whether the comment has been deleted.
        
              - **clientRequestToken** *(string) --* 
        
                A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
        """
        pass

    def put_file(self, repositoryName: str, branchName: str, fileContent: bytes, filePath: str, fileMode: str = None, parentCommitId: str = None, commitMessage: str = None, name: str = None, email: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/PutFile>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_file(
              repositoryName=\'string\',
              branchName=\'string\',
              fileContent=b\'bytes\',
              filePath=\'string\',
              fileMode=\'EXECUTABLE\'|\'NORMAL\'|\'SYMLINK\',
              parentCommitId=\'string\',
              commitMessage=\'string\',
              name=\'string\',
              email=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository where you want to add or update the file.
        
        :type branchName: string
        :param branchName: **[REQUIRED]** 
        
          The name of the branch where you want to add or update the file. If this is an empty repository, this branch will be created.
        
        :type fileContent: bytes
        :param fileContent: **[REQUIRED]** 
        
          The content of the file, in binary object format. 
        
        :type filePath: string
        :param filePath: **[REQUIRED]** 
        
          The name of the file you want to add or update, including the relative path to the file in the repository.
        
          .. note::
        
            If the path does not currently exist in the repository, the path will be created as part of adding the file.
        
        :type fileMode: string
        :param fileMode: 
        
          The file mode permissions of the blob. Valid file mode permissions are listed below.
        
        :type parentCommitId: string
        :param parentCommitId: 
        
          The full commit ID of the head commit in the branch where you want to add or update the file. If this is an empty repository, no commit ID is required. If this is not an empty repository, a commit ID is required. 
        
          The commit ID must match the ID of the head commit at the time of the operation, or an error will occur, and the file will not be added or updated.
        
        :type commitMessage: string
        :param commitMessage: 
        
          A message about why this file was added or updated. While optional, adding a message is strongly encouraged in order to provide a more useful commit history for your repository.
        
        :type name: string
        :param name: 
        
          The name of the person adding or updating the file. While optional, adding a name is strongly encouraged in order to provide a more useful commit history for your repository.
        
        :type email: string
        :param email: 
        
          An email address for the person adding or updating the file.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'commitId\': \'string\',
                \'blobId\': \'string\',
                \'treeId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **commitId** *(string) --* 
        
              The full SHA of the commit that contains this file change.
        
            - **blobId** *(string) --* 
        
              The ID of the blob, which is its SHA-1 pointer.
        
            - **treeId** *(string) --* 
        
              The full SHA-1 pointer of the tree information for the commit that contains this file change.
        
        """
        pass

    def put_repository_triggers(self, repositoryName: str, triggers: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/PutRepositoryTriggers>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_repository_triggers(
              repositoryName=\'string\',
              triggers=[
                  {
                      \'name\': \'string\',
                      \'destinationArn\': \'string\',
                      \'customData\': \'string\',
                      \'branches\': [
                          \'string\',
                      ],
                      \'events\': [
                          \'all\'|\'updateReference\'|\'createReference\'|\'deleteReference\',
                      ]
                  },
              ]
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository where you want to create or update the trigger.
        
        :type triggers: list
        :param triggers: **[REQUIRED]** 
        
          The JSON block of configuration information for each trigger.
        
          - *(dict) --* 
        
            Information about a trigger for a repository.
        
            - **name** *(string) --* **[REQUIRED]** 
        
              The name of the trigger.
        
            - **destinationArn** *(string) --* **[REQUIRED]** 
        
              The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).
        
            - **customData** *(string) --* 
        
              Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.
        
            - **branches** *(list) --* 
        
              The branches that will be included in the trigger configuration. If you specify an empty array, the trigger will apply to all branches.
        
              .. note::
        
                While no content is required in the array, you must include the array itself.
        
              - *(string) --* 
        
            - **events** *(list) --* **[REQUIRED]** 
        
              The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS). 
        
              .. note::
        
                The valid value \"all\" cannot be used with any other values.
        
              - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'configurationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a put repository triggers operation.
        
            - **configurationId** *(string) --* 
        
              The system-generated unique ID for the create or update operation.
        
        """
        pass

    def test_repository_triggers(self, repositoryName: str, triggers: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/TestRepositoryTriggers>`_
        
        **Request Syntax** 
        ::
        
          response = client.test_repository_triggers(
              repositoryName=\'string\',
              triggers=[
                  {
                      \'name\': \'string\',
                      \'destinationArn\': \'string\',
                      \'customData\': \'string\',
                      \'branches\': [
                          \'string\',
                      ],
                      \'events\': [
                          \'all\'|\'updateReference\'|\'createReference\'|\'deleteReference\',
                      ]
                  },
              ]
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository in which to test the triggers.
        
        :type triggers: list
        :param triggers: **[REQUIRED]** 
        
          The list of triggers to test.
        
          - *(dict) --* 
        
            Information about a trigger for a repository.
        
            - **name** *(string) --* **[REQUIRED]** 
        
              The name of the trigger.
        
            - **destinationArn** *(string) --* **[REQUIRED]** 
        
              The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).
        
            - **customData** *(string) --* 
        
              Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.
        
            - **branches** *(list) --* 
        
              The branches that will be included in the trigger configuration. If you specify an empty array, the trigger will apply to all branches.
        
              .. note::
        
                While no content is required in the array, you must include the array itself.
        
              - *(string) --* 
        
            - **events** *(list) --* **[REQUIRED]** 
        
              The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS). 
        
              .. note::
        
                The valid value \"all\" cannot be used with any other values.
        
              - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'successfulExecutions\': [
                    \'string\',
                ],
                \'failedExecutions\': [
                    {
                        \'trigger\': \'string\',
                        \'failureMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Represents the output of a test repository triggers operation.
        
            - **successfulExecutions** *(list) --* 
        
              The list of triggers that were successfully tested. This list provides the names of the triggers that were successfully tested, separated by commas.
        
              - *(string) --* 
          
            - **failedExecutions** *(list) --* 
        
              The list of triggers that were not able to be tested. This list provides the names of the triggers that could not be tested, separated by commas.
        
              - *(dict) --* 
        
                A trigger failed to run.
        
                - **trigger** *(string) --* 
        
                  The name of the trigger that did not run.
        
                - **failureMessage** *(string) --* 
        
                  Additional message information about the trigger that did not run.
        
        """
        pass

    def update_comment(self, commentId: str, content: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdateComment>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_comment(
              commentId=\'string\',
              content=\'string\'
          )
        :type commentId: string
        :param commentId: **[REQUIRED]** 
        
          The system-generated ID of the comment you want to update. To get this ID, use  GetCommentsForComparedCommit or  GetCommentsForPullRequest .
        
        :type content: string
        :param content: **[REQUIRED]** 
        
          The updated content with which you want to replace the existing content of the comment.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'comment\': {
                    \'commentId\': \'string\',
                    \'content\': \'string\',
                    \'inReplyTo\': \'string\',
                    \'creationDate\': datetime(2015, 1, 1),
                    \'lastModifiedDate\': datetime(2015, 1, 1),
                    \'authorArn\': \'string\',
                    \'deleted\': True|False,
                    \'clientRequestToken\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **comment** *(dict) --* 
        
              Information about the updated comment.
        
              - **commentId** *(string) --* 
        
                The system-generated comment ID.
        
              - **content** *(string) --* 
        
                The content of the comment.
        
              - **inReplyTo** *(string) --* 
        
                The ID of the comment for which this comment is a reply, if any.
        
              - **creationDate** *(datetime) --* 
        
                The date and time the comment was created, in timestamp format.
        
              - **lastModifiedDate** *(datetime) --* 
        
                The date and time the comment was most recently modified, in timestamp format.
        
              - **authorArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the person who posted the comment.
        
              - **deleted** *(boolean) --* 
        
                A Boolean value indicating whether the comment has been deleted.
        
              - **clientRequestToken** *(string) --* 
        
                A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
        """
        pass

    def update_default_branch(self, repositoryName: str, defaultBranchName: str) -> NoReturn:
        """
        
        .. note::
        
          If you use this operation to change the default branch name to the current default branch name, a success message is returned even though the default branch did not change.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdateDefaultBranch>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_default_branch(
              repositoryName=\'string\',
              defaultBranchName=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository to set or change the default branch for.
        
        :type defaultBranchName: string
        :param defaultBranchName: **[REQUIRED]** 
        
          The name of the branch to set as the default.
        
        :returns: None
        """
        pass

    def update_pull_request_description(self, pullRequestId: str, description: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdatePullRequestDescription>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_pull_request_description(
              pullRequestId=\'string\',
              description=\'string\'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]** 
        
          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .
        
        :type description: string
        :param description: **[REQUIRED]** 
        
          The updated content of the description for the pull request. This content will replace the existing description.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pullRequest\': {
                    \'pullRequestId\': \'string\',
                    \'title\': \'string\',
                    \'description\': \'string\',
                    \'lastActivityDate\': datetime(2015, 1, 1),
                    \'creationDate\': datetime(2015, 1, 1),
                    \'pullRequestStatus\': \'OPEN\'|\'CLOSED\',
                    \'authorArn\': \'string\',
                    \'pullRequestTargets\': [
                        {
                            \'repositoryName\': \'string\',
                            \'sourceReference\': \'string\',
                            \'destinationReference\': \'string\',
                            \'destinationCommit\': \'string\',
                            \'sourceCommit\': \'string\',
                            \'mergeBase\': \'string\',
                            \'mergeMetadata\': {
                                \'isMerged\': True|False,
                                \'mergedBy\': \'string\'
                            }
                        },
                    ],
                    \'clientRequestToken\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **pullRequest** *(dict) --* 
        
              Information about the updated pull request.
        
              - **pullRequestId** *(string) --* 
        
                The system-generated ID of the pull request. 
        
              - **title** *(string) --* 
        
                The user-defined title of the pull request. This title is displayed in the list of pull requests to other users of the repository.
        
              - **description** *(string) --* 
        
                The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.
        
              - **lastActivityDate** *(datetime) --* 
        
                The day and time of the last user or system activity on the pull request, in timestamp format.
        
              - **creationDate** *(datetime) --* 
        
                The date and time the pull request was originally created, in timestamp format.
        
              - **pullRequestStatus** *(string) --* 
        
                The status of the pull request. Pull request status can only change from ``OPEN`` to ``CLOSED`` .
        
              - **authorArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the user who created the pull request.
        
              - **pullRequestTargets** *(list) --* 
        
                The targets of the pull request, including the source branch and destination branch for the pull request.
        
                - *(dict) --* 
        
                  Returns information about a pull request target.
        
                  - **repositoryName** *(string) --* 
        
                    The name of the repository that contains the pull request source and destination branches.
        
                  - **sourceReference** *(string) --* 
        
                    The branch of the repository that contains the changes for the pull request. Also known as the source branch.
        
                  - **destinationReference** *(string) --* 
        
                    The branch of the repository where the pull request changes will be merged into. Also known as the destination branch. 
        
                  - **destinationCommit** *(string) --* 
        
                    The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.
        
                  - **sourceCommit** *(string) --* 
        
                    The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID will change to reflect the new tip of the branch.
        
                  - **mergeBase** *(string) --* 
        
                    The commit ID of the most recent commit that the source branch and the destination branch have in common.
        
                  - **mergeMetadata** *(dict) --* 
        
                    Returns metadata about the state of the merge, including whether the merge has been made.
        
                    - **isMerged** *(boolean) --* 
        
                      A Boolean value indicating whether the merge has been made.
        
                    - **mergedBy** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the user who merged the branches.
        
              - **clientRequestToken** *(string) --* 
        
                A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
        """
        pass

    def update_pull_request_status(self, pullRequestId: str, pullRequestStatus: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdatePullRequestStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_pull_request_status(
              pullRequestId=\'string\',
              pullRequestStatus=\'OPEN\'|\'CLOSED\'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]** 
        
          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .
        
        :type pullRequestStatus: string
        :param pullRequestStatus: **[REQUIRED]** 
        
          The status of the pull request. The only valid operations are to update the status from ``OPEN`` to ``OPEN`` , ``OPEN`` to ``CLOSED`` or from from ``CLOSED`` to ``CLOSED`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pullRequest\': {
                    \'pullRequestId\': \'string\',
                    \'title\': \'string\',
                    \'description\': \'string\',
                    \'lastActivityDate\': datetime(2015, 1, 1),
                    \'creationDate\': datetime(2015, 1, 1),
                    \'pullRequestStatus\': \'OPEN\'|\'CLOSED\',
                    \'authorArn\': \'string\',
                    \'pullRequestTargets\': [
                        {
                            \'repositoryName\': \'string\',
                            \'sourceReference\': \'string\',
                            \'destinationReference\': \'string\',
                            \'destinationCommit\': \'string\',
                            \'sourceCommit\': \'string\',
                            \'mergeBase\': \'string\',
                            \'mergeMetadata\': {
                                \'isMerged\': True|False,
                                \'mergedBy\': \'string\'
                            }
                        },
                    ],
                    \'clientRequestToken\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **pullRequest** *(dict) --* 
        
              Information about the pull request.
        
              - **pullRequestId** *(string) --* 
        
                The system-generated ID of the pull request. 
        
              - **title** *(string) --* 
        
                The user-defined title of the pull request. This title is displayed in the list of pull requests to other users of the repository.
        
              - **description** *(string) --* 
        
                The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.
        
              - **lastActivityDate** *(datetime) --* 
        
                The day and time of the last user or system activity on the pull request, in timestamp format.
        
              - **creationDate** *(datetime) --* 
        
                The date and time the pull request was originally created, in timestamp format.
        
              - **pullRequestStatus** *(string) --* 
        
                The status of the pull request. Pull request status can only change from ``OPEN`` to ``CLOSED`` .
        
              - **authorArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the user who created the pull request.
        
              - **pullRequestTargets** *(list) --* 
        
                The targets of the pull request, including the source branch and destination branch for the pull request.
        
                - *(dict) --* 
        
                  Returns information about a pull request target.
        
                  - **repositoryName** *(string) --* 
        
                    The name of the repository that contains the pull request source and destination branches.
        
                  - **sourceReference** *(string) --* 
        
                    The branch of the repository that contains the changes for the pull request. Also known as the source branch.
        
                  - **destinationReference** *(string) --* 
        
                    The branch of the repository where the pull request changes will be merged into. Also known as the destination branch. 
        
                  - **destinationCommit** *(string) --* 
        
                    The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.
        
                  - **sourceCommit** *(string) --* 
        
                    The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID will change to reflect the new tip of the branch.
        
                  - **mergeBase** *(string) --* 
        
                    The commit ID of the most recent commit that the source branch and the destination branch have in common.
        
                  - **mergeMetadata** *(dict) --* 
        
                    Returns metadata about the state of the merge, including whether the merge has been made.
        
                    - **isMerged** *(boolean) --* 
        
                      A Boolean value indicating whether the merge has been made.
        
                    - **mergedBy** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the user who merged the branches.
        
              - **clientRequestToken** *(string) --* 
        
                A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
        """
        pass

    def update_pull_request_title(self, pullRequestId: str, title: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdatePullRequestTitle>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_pull_request_title(
              pullRequestId=\'string\',
              title=\'string\'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]** 
        
          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .
        
        :type title: string
        :param title: **[REQUIRED]** 
        
          The updated title of the pull request. This will replace the existing title.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'pullRequest\': {
                    \'pullRequestId\': \'string\',
                    \'title\': \'string\',
                    \'description\': \'string\',
                    \'lastActivityDate\': datetime(2015, 1, 1),
                    \'creationDate\': datetime(2015, 1, 1),
                    \'pullRequestStatus\': \'OPEN\'|\'CLOSED\',
                    \'authorArn\': \'string\',
                    \'pullRequestTargets\': [
                        {
                            \'repositoryName\': \'string\',
                            \'sourceReference\': \'string\',
                            \'destinationReference\': \'string\',
                            \'destinationCommit\': \'string\',
                            \'sourceCommit\': \'string\',
                            \'mergeBase\': \'string\',
                            \'mergeMetadata\': {
                                \'isMerged\': True|False,
                                \'mergedBy\': \'string\'
                            }
                        },
                    ],
                    \'clientRequestToken\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **pullRequest** *(dict) --* 
        
              Information about the updated pull request.
        
              - **pullRequestId** *(string) --* 
        
                The system-generated ID of the pull request. 
        
              - **title** *(string) --* 
        
                The user-defined title of the pull request. This title is displayed in the list of pull requests to other users of the repository.
        
              - **description** *(string) --* 
        
                The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.
        
              - **lastActivityDate** *(datetime) --* 
        
                The day and time of the last user or system activity on the pull request, in timestamp format.
        
              - **creationDate** *(datetime) --* 
        
                The date and time the pull request was originally created, in timestamp format.
        
              - **pullRequestStatus** *(string) --* 
        
                The status of the pull request. Pull request status can only change from ``OPEN`` to ``CLOSED`` .
        
              - **authorArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the user who created the pull request.
        
              - **pullRequestTargets** *(list) --* 
        
                The targets of the pull request, including the source branch and destination branch for the pull request.
        
                - *(dict) --* 
        
                  Returns information about a pull request target.
        
                  - **repositoryName** *(string) --* 
        
                    The name of the repository that contains the pull request source and destination branches.
        
                  - **sourceReference** *(string) --* 
        
                    The branch of the repository that contains the changes for the pull request. Also known as the source branch.
        
                  - **destinationReference** *(string) --* 
        
                    The branch of the repository where the pull request changes will be merged into. Also known as the destination branch. 
        
                  - **destinationCommit** *(string) --* 
        
                    The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.
        
                  - **sourceCommit** *(string) --* 
        
                    The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID will change to reflect the new tip of the branch.
        
                  - **mergeBase** *(string) --* 
        
                    The commit ID of the most recent commit that the source branch and the destination branch have in common.
        
                  - **mergeMetadata** *(dict) --* 
        
                    Returns metadata about the state of the merge, including whether the merge has been made.
        
                    - **isMerged** *(boolean) --* 
        
                      A Boolean value indicating whether the merge has been made.
        
                    - **mergedBy** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the user who merged the branches.
        
              - **clientRequestToken** *(string) --* 
        
                A unique, client-generated idempotency token that when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request will return information about the initial request that used that token.
        
        """
        pass

    def update_repository_description(self, repositoryName: str, repositoryDescription: str = None) -> NoReturn:
        """
        
        .. note::
        
          The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a web page could expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a web page.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdateRepositoryDescription>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_repository_description(
              repositoryName=\'string\',
              repositoryDescription=\'string\'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]** 
        
          The name of the repository to set or change the comment or description for.
        
        :type repositoryDescription: string
        :param repositoryDescription: 
        
          The new comment or description for the specified repository. Repository descriptions are limited to 1,000 characters.
        
        :returns: None
        """
        pass

    def update_repository_name(self, oldName: str, newName: str) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdateRepositoryName>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_repository_name(
              oldName=\'string\',
              newName=\'string\'
          )
        :type oldName: string
        :param oldName: **[REQUIRED]** 
        
          The existing name of the repository.
        
        :type newName: string
        :param newName: **[REQUIRED]** 
        
          The new name for the repository.
        
        :returns: None
        """
        pass
