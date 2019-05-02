from typing import Dict
from datetime import datetime
from botocore.paginate import Paginator


class ListAlgorithms(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, NameContains: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCodeRepositories(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListCompilationJobs(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListEndpointConfigs(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListEndpoints(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListHyperParameterTuningJobs(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, StatusEquals: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListLabelingJobs(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, SortBy: str = None, SortOrder: str = None, StatusEquals: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListLabelingJobsForWorkteam(Paginator):
    def paginate(self, WorkteamArn: str, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, JobReferenceCodeContains: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListModelPackages(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, NameContains: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListModels(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListNotebookInstanceLifecycleConfigs(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListNotebookInstances(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None, NotebookInstanceLifecycleConfigNameContains: str = None, DefaultCodeRepositoryContains: str = None, AdditionalCodeRepositoryEquals: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSubscribedWorkteams(Paginator):
    def paginate(self, NameContains: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTags(Paginator):
    def paginate(self, ResourceArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTrainingJobs(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTrainingJobsForHyperParameterTuningJob(Paginator):
    def paginate(self, HyperParameterTuningJobName: str, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTransformJobs(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListWorkteams(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class Search(Paginator):
    def paginate(self, Resource: str, SearchExpression: Dict = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
