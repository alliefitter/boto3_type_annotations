from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def add_application_cloud_watch_logging_option(self, ApplicationName: str, CurrentApplicationVersionId: int, CloudWatchLoggingOption: Dict) -> Dict:
        pass

    def add_application_input(self, ApplicationName: str, CurrentApplicationVersionId: int, Input: Dict) -> Dict:
        pass

    def add_application_input_processing_configuration(self, ApplicationName: str, CurrentApplicationVersionId: int, InputId: str, InputProcessingConfiguration: Dict) -> Dict:
        pass

    def add_application_output(self, ApplicationName: str, CurrentApplicationVersionId: int, Output: Dict) -> Dict:
        pass

    def add_application_reference_data_source(self, ApplicationName: str, CurrentApplicationVersionId: int, ReferenceDataSource: Dict) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def create_application(self, ApplicationName: str, ApplicationDescription: str = None, Inputs: List = None, Outputs: List = None, CloudWatchLoggingOptions: List = None, ApplicationCode: str = None) -> Dict:
        pass

    def delete_application(self, ApplicationName: str, CreateTimestamp: datetime) -> Dict:
        pass

    def delete_application_cloud_watch_logging_option(self, ApplicationName: str, CurrentApplicationVersionId: int, CloudWatchLoggingOptionId: str) -> Dict:
        pass

    def delete_application_input_processing_configuration(self, ApplicationName: str, CurrentApplicationVersionId: int, InputId: str) -> Dict:
        pass

    def delete_application_output(self, ApplicationName: str, CurrentApplicationVersionId: int, OutputId: str) -> Dict:
        pass

    def delete_application_reference_data_source(self, ApplicationName: str, CurrentApplicationVersionId: int, ReferenceId: str) -> Dict:
        pass

    def describe_application(self, ApplicationName: str) -> Dict:
        pass

    def discover_input_schema(self, ResourceARN: str = None, RoleARN: str = None, InputStartingPositionConfiguration: Dict = None, S3Configuration: Dict = None, InputProcessingConfiguration: Dict = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_applications(self, Limit: int = None, ExclusiveStartApplicationName: str = None) -> Dict:
        pass

    def start_application(self, ApplicationName: str, InputConfigurations: List) -> Dict:
        pass

    def stop_application(self, ApplicationName: str) -> Dict:
        pass

    def update_application(self, ApplicationName: str, CurrentApplicationVersionId: int, ApplicationUpdate: Dict) -> Dict:
        pass
