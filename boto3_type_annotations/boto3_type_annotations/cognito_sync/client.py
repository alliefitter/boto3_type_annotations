from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def bulk_publish(self, IdentityPoolId: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def delete_dataset(self, IdentityPoolId: str, IdentityId: str, DatasetName: str) -> Dict:
        pass

    def describe_dataset(self, IdentityPoolId: str, IdentityId: str, DatasetName: str) -> Dict:
        pass

    def describe_identity_pool_usage(self, IdentityPoolId: str) -> Dict:
        pass

    def describe_identity_usage(self, IdentityPoolId: str, IdentityId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_bulk_publish_details(self, IdentityPoolId: str) -> Dict:
        pass

    def get_cognito_events(self, IdentityPoolId: str) -> Dict:
        pass

    def get_identity_pool_configuration(self, IdentityPoolId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_datasets(self, IdentityPoolId: str, IdentityId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_identity_pool_usage(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_records(self, IdentityPoolId: str, IdentityId: str, DatasetName: str, LastSyncCount: int = None, NextToken: str = None, MaxResults: int = None, SyncSessionToken: str = None) -> Dict:
        pass

    def register_device(self, IdentityPoolId: str, IdentityId: str, Platform: str, Token: str) -> Dict:
        pass

    def set_cognito_events(self, IdentityPoolId: str, Events: Dict) -> NoReturn:
        pass

    def set_identity_pool_configuration(self, IdentityPoolId: str, PushSync: Dict = None, CognitoStreams: Dict = None) -> Dict:
        pass

    def subscribe_to_dataset(self, IdentityPoolId: str, IdentityId: str, DatasetName: str, DeviceId: str) -> Dict:
        pass

    def unsubscribe_from_dataset(self, IdentityPoolId: str, IdentityId: str, DatasetName: str, DeviceId: str) -> Dict:
        pass

    def update_records(self, IdentityPoolId: str, IdentityId: str, DatasetName: str, SyncSessionToken: str, DeviceId: str = None, RecordPatches: List = None, ClientContext: str = None) -> Dict:
        pass
