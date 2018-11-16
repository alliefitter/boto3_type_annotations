from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_vocabulary(self, VocabularyName: str, LanguageCode: str, Phrases: List) -> Dict:
        pass

    def delete_transcription_job(self, TranscriptionJobName: str):
        pass

    def delete_vocabulary(self, VocabularyName: str):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_transcription_job(self, TranscriptionJobName: str) -> Dict:
        pass

    def get_vocabulary(self, VocabularyName: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_transcription_jobs(self, Status: str = None, JobNameContains: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_vocabularies(self, NextToken: str = None, MaxResults: int = None, StateEquals: str = None, NameContains: str = None) -> Dict:
        pass

    def start_transcription_job(self, TranscriptionJobName: str, LanguageCode: str, MediaFormat: str, Media: Dict, MediaSampleRateHertz: int = None, OutputBucketName: str = None, Settings: Dict = None) -> Dict:
        pass

    def update_vocabulary(self, VocabularyName: str, LanguageCode: str, Phrases: List) -> Dict:
        pass
