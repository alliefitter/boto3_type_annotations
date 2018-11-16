from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_hls_streaming_session_url(self, StreamName: str = None, StreamARN: str = None, PlaybackMode: str = None, HLSFragmentSelector: Dict = None, DiscontinuityMode: str = None, Expires: int = None, MaxMediaPlaylistFragmentResults: int = None) -> Dict:
        pass

    def get_media_for_fragment_list(self, StreamName: str, Fragments: List) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_fragments(self, StreamName: str, MaxResults: int = None, NextToken: str = None, FragmentSelector: Dict = None) -> Dict:
        pass
