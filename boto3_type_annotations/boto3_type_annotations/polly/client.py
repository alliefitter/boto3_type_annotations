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

    def delete_lexicon(self, Name: str) -> Dict:
        pass

    def describe_voices(self, LanguageCode: str = None, IncludeAdditionalLanguageCodes: bool = None, NextToken: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_lexicon(self, Name: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_speech_synthesis_task(self, TaskId: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_lexicons(self, NextToken: str = None) -> Dict:
        pass

    def list_speech_synthesis_tasks(self, MaxResults: int = None, NextToken: str = None, Status: str = None) -> Dict:
        pass

    def put_lexicon(self, Name: str, Content: str) -> Dict:
        pass

    def start_speech_synthesis_task(self, OutputFormat: str, OutputS3BucketName: str, Text: str, VoiceId: str, LexiconNames: List = None, OutputS3KeyPrefix: str = None, SampleRate: str = None, SnsTopicArn: str = None, SpeechMarkTypes: List = None, TextType: str = None, LanguageCode: str = None) -> Dict:
        pass

    def synthesize_speech(self, OutputFormat: str, Text: str, VoiceId: str, LexiconNames: List = None, SampleRate: str = None, SpeechMarkTypes: List = None, TextType: str = None, LanguageCode: str = None) -> Dict:
        pass
