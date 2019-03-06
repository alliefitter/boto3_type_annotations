from typing import Dict
from botocore.paginate import Paginator


class DescribeBackups(Paginator):
    def paginate(self, BackupId: str = None, ServerName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeEvents(Paginator):
    def paginate(self, ServerName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeServers(Paginator):
    def paginate(self, ServerName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
