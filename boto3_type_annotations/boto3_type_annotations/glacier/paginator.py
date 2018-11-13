from typing import Dict
from botocore.paginate import Paginator


class ListJobs(Paginator):
    def paginate(self, vaultName: str, accountId: str = None, statuscode: str = None, completed: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListMultipartUploads(Paginator):
    def paginate(self, vaultName: str, accountId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListParts(Paginator):
    def paginate(self, vaultName: str, uploadId: str, accountId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListVaults(Paginator):
    def paginate(self, accountId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
