from typing import Dict
from botocore.paginate import Paginator


class DescribeVoices(Paginator):
    def paginate(self, LanguageCode: str = None, IncludeAdditionalLanguageCodes: bool = None, PaginationConfig: Dict = None) -> Dict:
        pass
