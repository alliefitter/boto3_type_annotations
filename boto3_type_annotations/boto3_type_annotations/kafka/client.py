from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_cluster(self, BrokerNodeGroupInfo: Dict, ClusterName: str, KafkaVersion: str, NumberOfBrokerNodes: int, EncryptionInfo: Dict = None, EnhancedMonitoring: str = None) -> Dict:
        pass

    def delete_cluster(self, ClusterArn: str, CurrentVersion: str = None) -> Dict:
        pass

    def describe_cluster(self, ClusterArn: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_bootstrap_brokers(self, ClusterArn: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_clusters(self, ClusterNameFilter: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_nodes(self, ClusterArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        pass

    def tag_resource(self, ResourceArn: str, Tags: Dict):
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List):
        pass
