from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeCases(Paginator):
    def paginate(self, caseIdList: List = None, displayId: str = None, afterTime: str = None, beforeTime: str = None, includeResolvedCases: bool = None, language: str = None, includeCommunications: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeCommunications(Paginator):
    def paginate(self, caseId: str, beforeTime: str = None, afterTime: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
