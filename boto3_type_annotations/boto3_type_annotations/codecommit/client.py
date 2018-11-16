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
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_branch(self, repositoryName: str, branchName: str, commitId: str) -> NoReturn:
        pass

    def create_pull_request(self, title: str, targets: List, description: str = None, clientRequestToken: str = None) -> Dict:
        pass

    def create_repository(self, repositoryName: str, repositoryDescription: str = None) -> Dict:
        pass

    def delete_branch(self, repositoryName: str, branchName: str) -> Dict:
        pass

    def delete_comment_content(self, commentId: str) -> Dict:
        pass

    def delete_file(self, repositoryName: str, branchName: str, filePath: str, parentCommitId: str, keepEmptyFolders: bool = None, commitMessage: str = None, name: str = None, email: str = None) -> Dict:
        pass

    def delete_repository(self, repositoryName: str) -> Dict:
        pass

    def describe_pull_request_events(self, pullRequestId: str, pullRequestEventType: str = None, actorArn: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_blob(self, repositoryName: str, blobId: str) -> Dict:
        pass

    def get_branch(self, repositoryName: str = None, branchName: str = None) -> Dict:
        pass

    def get_comment(self, commentId: str) -> Dict:
        pass

    def get_comments_for_compared_commit(self, repositoryName: str, afterCommitId: str, beforeCommitId: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_comments_for_pull_request(self, pullRequestId: str, repositoryName: str = None, beforeCommitId: str = None, afterCommitId: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_commit(self, repositoryName: str, commitId: str) -> Dict:
        pass

    def get_differences(self, repositoryName: str, afterCommitSpecifier: str, beforeCommitSpecifier: str = None, beforePath: str = None, afterPath: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def get_file(self, repositoryName: str, filePath: str, commitSpecifier: str = None) -> Dict:
        pass

    def get_folder(self, repositoryName: str, folderPath: str, commitSpecifier: str = None) -> Dict:
        pass

    def get_merge_conflicts(self, repositoryName: str, destinationCommitSpecifier: str, sourceCommitSpecifier: str, mergeOption: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_pull_request(self, pullRequestId: str) -> Dict:
        pass

    def get_repository(self, repositoryName: str) -> Dict:
        pass

    def get_repository_triggers(self, repositoryName: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_branches(self, repositoryName: str, nextToken: str = None) -> Dict:
        pass

    def list_pull_requests(self, repositoryName: str, authorArn: str = None, pullRequestStatus: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def list_repositories(self, nextToken: str = None, sortBy: str = None, order: str = None) -> Dict:
        pass

    def merge_pull_request_by_fast_forward(self, pullRequestId: str, repositoryName: str, sourceCommitId: str = None) -> Dict:
        pass

    def post_comment_for_compared_commit(self, repositoryName: str, afterCommitId: str, content: str, beforeCommitId: str = None, location: Dict = None, clientRequestToken: str = None) -> Dict:
        pass

    def post_comment_for_pull_request(self, pullRequestId: str, repositoryName: str, beforeCommitId: str, afterCommitId: str, content: str, location: Dict = None, clientRequestToken: str = None) -> Dict:
        pass

    def post_comment_reply(self, inReplyTo: str, content: str, clientRequestToken: str = None) -> Dict:
        pass

    def put_file(self, repositoryName: str, branchName: str, fileContent: bytes, filePath: str, fileMode: str = None, parentCommitId: str = None, commitMessage: str = None, name: str = None, email: str = None) -> Dict:
        pass

    def put_repository_triggers(self, repositoryName: str, triggers: List) -> Dict:
        pass

    def test_repository_triggers(self, repositoryName: str, triggers: List) -> Dict:
        pass

    def update_comment(self, commentId: str, content: str) -> Dict:
        pass

    def update_default_branch(self, repositoryName: str, defaultBranchName: str) -> NoReturn:
        pass

    def update_pull_request_description(self, pullRequestId: str, description: str) -> Dict:
        pass

    def update_pull_request_status(self, pullRequestId: str, pullRequestStatus: str) -> Dict:
        pass

    def update_pull_request_title(self, pullRequestId: str, title: str) -> Dict:
        pass

    def update_repository_description(self, repositoryName: str, repositoryDescription: str = None) -> NoReturn:
        pass

    def update_repository_name(self, oldName: str, newName: str) -> NoReturn:
        pass
