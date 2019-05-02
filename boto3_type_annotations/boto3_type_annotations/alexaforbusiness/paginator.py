from typing import Dict
from typing import List
from botocore.paginate import Paginator


class ListBusinessReportSchedules(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListConferenceProviders(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDeviceEvents(Paginator):
    def paginate(self, DeviceArn: str, EventType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSkills(Paginator):
    def paginate(self, SkillGroupArn: str = None, EnablementType: str = None, SkillType: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSkillsStoreCategories(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSkillsStoreSkillsByCategory(Paginator):
    def paginate(self, CategoryId: int, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSmartHomeAppliances(Paginator):
    def paginate(self, RoomArn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListTags(Paginator):
    def paginate(self, Arn: str, PaginationConfig: Dict = None) -> Dict:
        pass


class SearchDevices(Paginator):
    def paginate(self, Filters: List = None, SortCriteria: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class SearchProfiles(Paginator):
    def paginate(self, Filters: List = None, SortCriteria: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class SearchRooms(Paginator):
    def paginate(self, Filters: List = None, SortCriteria: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class SearchSkillGroups(Paginator):
    def paginate(self, Filters: List = None, SortCriteria: List = None, PaginationConfig: Dict = None) -> Dict:
        pass


class SearchUsers(Paginator):
    def paginate(self, Filters: List = None, SortCriteria: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
