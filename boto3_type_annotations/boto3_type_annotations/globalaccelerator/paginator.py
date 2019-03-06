from typing import Dict
from botocore.paginate import Paginator


class ListAccelerators(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListEndpointGroups(Paginator):
    def paginate(self, ListenerArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListListeners(Paginator):
    def paginate(self, AcceleratorArn: str, PaginationConfig: Dict = None) -> Dict:
        pass
