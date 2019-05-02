from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def analyze_document(self, Document: Dict, FeatureTypes: List) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def detect_document_text(self, Document: Dict) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_document_analysis(self, JobId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def get_document_text_detection(self, JobId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def start_document_analysis(self, DocumentLocation: Dict, FeatureTypes: List, ClientRequestToken: str = None, JobTag: str = None, NotificationChannel: Dict = None) -> Dict:
        pass

    def start_document_text_detection(self, DocumentLocation: Dict, ClientRequestToken: str = None, JobTag: str = None, NotificationChannel: Dict = None) -> Dict:
        pass
