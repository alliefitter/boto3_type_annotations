from typing import Dict
from botocore.paginate import Paginator


class DescribeSchedule(Paginator):
    def paginate(self, ChannelId: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListChannels(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListInputSecurityGroups(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListInputs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListOfferings(Paginator):
    def paginate(self, ChannelConfiguration: str = None, Codec: str = None, MaximumBitrate: str = None, MaximumFramerate: str = None, Resolution: str = None, ResourceType: str = None, SpecialFeature: str = None, VideoQuality: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListReservations(Paginator):
    def paginate(self, Codec: str = None, MaximumBitrate: str = None, MaximumFramerate: str = None, Resolution: str = None, ResourceType: str = None, SpecialFeature: str = None, VideoQuality: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
