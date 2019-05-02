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

    def delete_terminology(self, Name: str):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_terminology(self, Name: str, TerminologyDataFormat: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def import_terminology(self, Name: str, MergeStrategy: str, TerminologyData: Dict, Description: str = None, EncryptionKey: Dict = None) -> Dict:
        pass

    def list_terminologies(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def translate_text(self, Text: str, SourceLanguageCode: str, TargetLanguageCode: str, TerminologyNames: List = None) -> Dict:
        pass
