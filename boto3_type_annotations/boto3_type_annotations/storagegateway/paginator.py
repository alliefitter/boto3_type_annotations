from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeTapeArchives(Paginator):
    def paginate(self, TapeARNs: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTapeRecoveryPoints(Paginator):
    def paginate(self, GatewayARN: str, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeTapes(Paginator):
    def paginate(self, GatewayARN: str, TapeARNs: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeVTLDevices(Paginator):
    def paginate(self, GatewayARN: str, VTLDeviceARNs: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListGateways(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListVolumes(Paginator):
    def paginate(self, GatewayARN: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
