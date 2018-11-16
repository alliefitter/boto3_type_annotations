from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def batch_detect_dominant_language(self, TextList: List) -> Dict:
        pass

    def batch_detect_entities(self, TextList: List, LanguageCode: str) -> Dict:
        pass

    def batch_detect_key_phrases(self, TextList: List, LanguageCode: str) -> Dict:
        pass

    def batch_detect_sentiment(self, TextList: List, LanguageCode: str) -> Dict:
        pass

    def batch_detect_syntax(self, TextList: List, LanguageCode: str) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None):
        pass

    def describe_dominant_language_detection_job(self, JobId: str) -> Dict:
        pass

    def describe_entities_detection_job(self, JobId: str) -> Dict:
        pass

    def describe_key_phrases_detection_job(self, JobId: str) -> Dict:
        pass

    def describe_sentiment_detection_job(self, JobId: str) -> Dict:
        pass

    def describe_topics_detection_job(self, JobId: str) -> Dict:
        pass

    def detect_dominant_language(self, Text: str) -> Dict:
        pass

    def detect_entities(self, Text: str, LanguageCode: str) -> Dict:
        pass

    def detect_key_phrases(self, Text: str, LanguageCode: str) -> Dict:
        pass

    def detect_sentiment(self, Text: str, LanguageCode: str) -> Dict:
        pass

    def detect_syntax(self, Text: str, LanguageCode: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_dominant_language_detection_jobs(self, Filter: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_entities_detection_jobs(self, Filter: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_key_phrases_detection_jobs(self, Filter: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_sentiment_detection_jobs(self, Filter: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_topics_detection_jobs(self, Filter: Dict = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def start_dominant_language_detection_job(self, InputDataConfig: Dict, OutputDataConfig: Dict, DataAccessRoleArn: str, JobName: str = None, ClientRequestToken: str = None) -> Dict:
        pass

    def start_entities_detection_job(self, InputDataConfig: Dict, OutputDataConfig: Dict, DataAccessRoleArn: str, LanguageCode: str, JobName: str = None, ClientRequestToken: str = None) -> Dict:
        pass

    def start_key_phrases_detection_job(self, InputDataConfig: Dict, OutputDataConfig: Dict, DataAccessRoleArn: str, LanguageCode: str, JobName: str = None, ClientRequestToken: str = None) -> Dict:
        pass

    def start_sentiment_detection_job(self, InputDataConfig: Dict, OutputDataConfig: Dict, DataAccessRoleArn: str, LanguageCode: str, JobName: str = None, ClientRequestToken: str = None) -> Dict:
        pass

    def start_topics_detection_job(self, InputDataConfig: Dict, OutputDataConfig: Dict, DataAccessRoleArn: str, JobName: str = None, NumberOfTopics: int = None, ClientRequestToken: str = None) -> Dict:
        pass

    def stop_dominant_language_detection_job(self, JobId: str) -> Dict:
        pass

    def stop_entities_detection_job(self, JobId: str) -> Dict:
        pass

    def stop_key_phrases_detection_job(self, JobId: str) -> Dict:
        pass

    def stop_sentiment_detection_job(self, JobId: str) -> Dict:
        pass
