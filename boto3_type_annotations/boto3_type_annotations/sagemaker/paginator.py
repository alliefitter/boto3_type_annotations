from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class ListEndpointConfigs(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListEndpoints(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListModels(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListNotebookInstances(Paginator):
    def paginate(self, SortBy: str = None, SortOrder: str = None, NameContains: str = None, CreationTimeBefore: datetime = None, CreationTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, StatusEquals: str = None, NotebookInstanceLifecycleConfigNameContains: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTags(Paginator):
    def paginate(self, ResourceArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTrainingJobs(Paginator):
    def paginate(self, CreationTimeAfter: datetime = None, CreationTimeBefore: datetime = None, LastModifiedTimeAfter: datetime = None, LastModifiedTimeBefore: datetime = None, NameContains: str = None, StatusEquals: str = None, SortBy: str = None, SortOrder: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
