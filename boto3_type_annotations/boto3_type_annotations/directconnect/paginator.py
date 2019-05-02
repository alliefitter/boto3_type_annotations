from typing import Dict
from botocore.paginate import Paginator


class DescribeDirectConnectGatewayAssociations(Paginator):
    def paginate(self, associationId: str = None, associatedGatewayId: str = None, directConnectGatewayId: str = None, virtualGatewayId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDirectConnectGatewayAttachments(Paginator):
    def paginate(self, directConnectGatewayId: str = None, virtualInterfaceId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeDirectConnectGateways(Paginator):
    def paginate(self, directConnectGatewayId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
