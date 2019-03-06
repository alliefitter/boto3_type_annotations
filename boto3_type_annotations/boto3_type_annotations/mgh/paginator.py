from typing import Dict
from botocore.paginate import Paginator


class ListCreatedArtifacts(Paginator):
    def paginate(self, ProgressUpdateStream: str, MigrationTaskName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListDiscoveredResources(Paginator):
    def paginate(self, ProgressUpdateStream: str, MigrationTaskName: str, PaginationConfig: Dict = None) -> Dict:
        pass


class ListMigrationTasks(Paginator):
    def paginate(self, ResourceName: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListProgressUpdateStreams(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass
