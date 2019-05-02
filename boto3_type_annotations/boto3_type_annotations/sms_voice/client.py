from typing import Optional
from botocore.client import BaseClient
from botocore.waiter import Waiter
from typing import Union
from typing import Dict
from botocore.paginate import Paginator


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_configuration_set(self, ConfigurationSetName: str = None) -> Dict:
        pass

    def create_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestination: Dict = None, EventDestinationName: str = None) -> Dict:
        pass

    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict:
        pass

    def delete_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestinationName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_configuration_set_event_destinations(self, ConfigurationSetName: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_configuration_sets(self, NextToken: str = None, PageSize: str = None) -> Dict:
        pass

    def send_voice_message(self, CallerId: str = None, ConfigurationSetName: str = None, Content: Dict = None, DestinationPhoneNumber: str = None, OriginationPhoneNumber: str = None) -> Dict:
        pass

    def update_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestinationName: str, EventDestination: Dict = None) -> Dict:
        pass
