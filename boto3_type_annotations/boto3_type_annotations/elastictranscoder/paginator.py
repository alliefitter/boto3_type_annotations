from typing import Dict
from botocore.paginate import Paginator


class ListJobsByPipeline(Paginator):
    def paginate(self, PipelineId: str, Ascending: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListJobsByStatus(Paginator):
    def paginate(self, Status: str, Ascending: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPipelines(Paginator):
    def paginate(self, Ascending: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPresets(Paginator):
    def paginate(self, Ascending: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
