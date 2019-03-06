from typing import Dict
from botocore.paginate import Paginator


class DescribeVoices(Paginator):
    def paginate(self, LanguageCode: str = None, IncludeAdditionalLanguageCodes: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListLexicons(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListSpeechSynthesisTasks(Paginator):
    def paginate(self, Status: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
