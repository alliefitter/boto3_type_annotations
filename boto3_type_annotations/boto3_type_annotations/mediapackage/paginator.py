from typing import Dict
from botocore.paginate import Paginator


class ListChannels(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListOriginEndpoints(Paginator):
    def paginate(self, ChannelId: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
