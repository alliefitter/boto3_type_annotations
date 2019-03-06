from typing import Dict
from botocore.paginate import Paginator


class ListSigningJobs(Paginator):
    def paginate(self, status: str = None, platformId: str = None, requestedBy: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSigningPlatforms(Paginator):
    def paginate(self, category: str = None, partner: str = None, target: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSigningProfiles(Paginator):
    def paginate(self, includeCanceled: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass
