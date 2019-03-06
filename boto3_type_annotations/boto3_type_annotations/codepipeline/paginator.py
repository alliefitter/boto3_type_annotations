from typing import Dict
from botocore.paginate import Paginator


class ListActionTypes(Paginator):
    def paginate(self, actionOwnerFilter: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPipelineExecutions(Paginator):
    def paginate(self, pipelineName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPipelines(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListWebhooks(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
