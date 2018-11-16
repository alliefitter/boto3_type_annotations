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

    def cancel_rotate_secret(self, SecretId: str) -> Dict:
        pass

    def create_secret(self, Name: str, ClientRequestToken: str = None, Description: str = None, KmsKeyId: str = None, SecretBinary: bytes = None, SecretString: str = None, Tags: List = None) -> Dict:
        pass

    def delete_resource_policy(self, SecretId: str) -> Dict:
        pass

    def delete_secret(self, SecretId: str, RecoveryWindowInDays: int = None, ForceDeleteWithoutRecovery: bool = None) -> Dict:
        pass

    def describe_secret(self, SecretId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_random_password(self, PasswordLength: int = None, ExcludeCharacters: str = None, ExcludeNumbers: bool = None, ExcludePunctuation: bool = None, ExcludeUppercase: bool = None, ExcludeLowercase: bool = None, IncludeSpace: bool = None, RequireEachIncludedType: bool = None) -> Dict:
        pass

    def get_resource_policy(self, SecretId: str) -> Dict:
        pass

    def get_secret_value(self, SecretId: str, VersionId: str = None, VersionStage: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_secret_version_ids(self, SecretId: str, MaxResults: int = None, NextToken: str = None, IncludeDeprecated: bool = None) -> Dict:
        pass

    def list_secrets(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def put_resource_policy(self, SecretId: str, ResourcePolicy: str) -> Dict:
        pass

    def put_secret_value(self, SecretId: str, ClientRequestToken: str = None, SecretBinary: bytes = None, SecretString: str = None, VersionStages: List = None) -> Dict:
        pass

    def restore_secret(self, SecretId: str) -> Dict:
        pass

    def rotate_secret(self, SecretId: str, ClientRequestToken: str = None, RotationLambdaARN: str = None, RotationRules: Dict = None) -> Dict:
        pass

    def tag_resource(self, SecretId: str, Tags: List) -> NoReturn:
        pass

    def untag_resource(self, SecretId: str, TagKeys: List) -> NoReturn:
        pass

    def update_secret(self, SecretId: str, ClientRequestToken: str = None, Description: str = None, KmsKeyId: str = None, SecretBinary: bytes = None, SecretString: str = None) -> Dict:
        pass

    def update_secret_version_stage(self, SecretId: str, VersionStage: str, RemoveFromVersionId: str = None, MoveToVersionId: str = None) -> Dict:
        pass
