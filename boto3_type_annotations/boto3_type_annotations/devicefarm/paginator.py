from typing import Dict
from botocore.paginate import Paginator


class GetOfferingStatus(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListArtifacts(Paginator):
    def paginate(self, arn: str, type: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDevicePools(Paginator):
    def paginate(self, arn: str, type: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDevices(Paginator):
    def paginate(self, arn: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListJobs(Paginator):
    def paginate(self, arn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListOfferingTransactions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListOfferings(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListProjects(Paginator):
    def paginate(self, arn: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListRuns(Paginator):
    def paginate(self, arn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSamples(Paginator):
    def paginate(self, arn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSuites(Paginator):
    def paginate(self, arn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTests(Paginator):
    def paginate(self, arn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListUniqueProblems(Paginator):
    def paginate(self, arn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListUploads(Paginator):
    def paginate(self, arn: str, type: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
