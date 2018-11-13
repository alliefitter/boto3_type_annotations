from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListSkills(Paginator):
    def paginate(self, SkillGroupArn: str = None, EnablementType: str = None, SkillType: str = None, PaginationConfig: Dict = None) -> Dict:
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
