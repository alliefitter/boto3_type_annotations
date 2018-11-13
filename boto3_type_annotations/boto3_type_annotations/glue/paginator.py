from typing import List
from typing import Dict
from botocore.paginate import Paginator


class GetClassifiers(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetConnections(Paginator):
    def paginate(self, CatalogId: str = None, Filter: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetCrawlerMetrics(Paginator):
    def paginate(self, CrawlerNameList: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetCrawlers(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetDatabases(Paginator):
    def paginate(self, CatalogId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetDevEndpoints(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetJobRuns(Paginator):
    def paginate(self, JobName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class GetJobs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class GetPartitions(Paginator):
    def paginate(self, DatabaseName: str, TableName: str, CatalogId: str = None, Expression: str = None, Segment: Dict = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetTableVersions(Paginator):
    def paginate(self, DatabaseName: str, TableName: str, CatalogId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetTables(Paginator):
    def paginate(self, DatabaseName: str, CatalogId: str = None, Expression: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetTriggers(Paginator):
    def paginate(self, DependentJobName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class GetUserDefinedFunctions(Paginator):
    def paginate(self, DatabaseName: str, Pattern: str, CatalogId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
