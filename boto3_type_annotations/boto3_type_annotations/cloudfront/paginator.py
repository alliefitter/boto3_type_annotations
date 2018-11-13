from typing import Dict
from botocore.paginate import Paginator


class ListCloudFrontOriginAccessIdentities(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDistributions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListInvalidations(Paginator):
    def paginate(self, DistributionId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListStreamingDistributions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
