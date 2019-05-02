from typing import Dict
from datetime import datetime
from botocore.paginate import Paginator


class ListChannels(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDatasetContents(Paginator):
    def paginate(self, datasetName: str, scheduledOnOrAfter: datetime = None, scheduledBefore: datetime = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDatasets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDatastores(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class ListPipelines(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
