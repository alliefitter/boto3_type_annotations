from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def create_delivery_stream(self, DeliveryStreamName: str, DeliveryStreamType: str = None, KinesisStreamSourceConfiguration: Dict = None, S3DestinationConfiguration: Dict = None, ExtendedS3DestinationConfiguration: Dict = None, RedshiftDestinationConfiguration: Dict = None, ElasticsearchDestinationConfiguration: Dict = None, SplunkDestinationConfiguration: Dict = None, Tags: List = None) -> Dict:
        pass

    def delete_delivery_stream(self, DeliveryStreamName: str) -> Dict:
        pass

    def describe_delivery_stream(self, DeliveryStreamName: str, Limit: int = None, ExclusiveStartDestinationId: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_delivery_streams(self, Limit: int = None, DeliveryStreamType: str = None, ExclusiveStartDeliveryStreamName: str = None) -> Dict:
        pass

    def list_tags_for_delivery_stream(self, DeliveryStreamName: str, ExclusiveStartTagKey: str = None, Limit: int = None) -> Dict:
        pass

    def put_record(self, DeliveryStreamName: str, Record: Dict) -> Dict:
        pass

    def put_record_batch(self, DeliveryStreamName: str, Records: List) -> Dict:
        pass

    def start_delivery_stream_encryption(self, DeliveryStreamName: str) -> Dict:
        pass

    def stop_delivery_stream_encryption(self, DeliveryStreamName: str) -> Dict:
        pass

    def tag_delivery_stream(self, DeliveryStreamName: str, Tags: List) -> Dict:
        pass

    def untag_delivery_stream(self, DeliveryStreamName: str, TagKeys: List) -> Dict:
        pass

    def update_destination(self, DeliveryStreamName: str, CurrentDeliveryStreamVersionId: str, DestinationId: str, S3DestinationUpdate: Dict = None, ExtendedS3DestinationUpdate: Dict = None, RedshiftDestinationUpdate: Dict = None, ElasticsearchDestinationUpdate: Dict = None, SplunkDestinationUpdate: Dict = None) -> Dict:
        pass
