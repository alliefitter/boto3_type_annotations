from typing import Dict
from botocore.paginate import Paginator


class DescribePullRequestEvents(Paginator):
    def paginate(self, pullRequestId: str, pullRequestEventType: str = None, actorArn: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetCommentsForComparedCommit(Paginator):
    def paginate(self, repositoryName: str, afterCommitId: str, beforeCommitId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetCommentsForPullRequest(Paginator):
    def paginate(self, pullRequestId: str, repositoryName: str = None, beforeCommitId: str = None, afterCommitId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetDifferences(Paginator):
    def paginate(self, repositoryName: str, afterCommitSpecifier: str, beforeCommitSpecifier: str = None, beforePath: str = None, afterPath: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListBranches(Paginator):
    def paginate(self, repositoryName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPullRequests(Paginator):
    def paginate(self, repositoryName: str, authorArn: str = None, pullRequestStatus: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRepositories(Paginator):
    def paginate(self, sortBy: str = None, order: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
