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

    def compare_faces(self, SourceImage: Dict, TargetImage: Dict, SimilarityThreshold: float = None) -> Dict:
        pass

    def create_collection(self, CollectionId: str) -> Dict:
        pass

    def create_stream_processor(self, Input: Dict, Output: Dict, Name: str, Settings: Dict, RoleArn: str) -> Dict:
        pass

    def delete_collection(self, CollectionId: str) -> Dict:
        pass

    def delete_faces(self, CollectionId: str, FaceIds: List) -> Dict:
        pass

    def delete_stream_processor(self, Name: str) -> Dict:
        pass

    def describe_collection(self, CollectionId: str) -> Dict:
        pass

    def describe_stream_processor(self, Name: str) -> Dict:
        pass

    def detect_faces(self, Image: Dict, Attributes: List = None) -> Dict:
        pass

    def detect_labels(self, Image: Dict, MaxLabels: int = None, MinConfidence: float = None) -> Dict:
        pass

    def detect_moderation_labels(self, Image: Dict, MinConfidence: float = None) -> Dict:
        pass

    def detect_text(self, Image: Dict) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_celebrity_info(self, Id: str) -> Dict:
        pass

    def get_celebrity_recognition(self, JobId: str, MaxResults: int = None, NextToken: str = None, SortBy: str = None) -> Dict:
        pass

    def get_content_moderation(self, JobId: str, MaxResults: int = None, NextToken: str = None, SortBy: str = None) -> Dict:
        pass

    def get_face_detection(self, JobId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    def get_face_search(self, JobId: str, MaxResults: int = None, NextToken: str = None, SortBy: str = None) -> Dict:
        pass

    def get_label_detection(self, JobId: str, MaxResults: int = None, NextToken: str = None, SortBy: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_person_tracking(self, JobId: str, MaxResults: int = None, NextToken: str = None, SortBy: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def index_faces(self, CollectionId: str, Image: Dict, ExternalImageId: str = None, DetectionAttributes: List = None, MaxFaces: int = None, QualityFilter: str = None) -> Dict:
        pass

    def list_collections(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_faces(self, CollectionId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def list_stream_processors(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def recognize_celebrities(self, Image: Dict) -> Dict:
        pass

    def search_faces(self, CollectionId: str, FaceId: str, MaxFaces: int = None, FaceMatchThreshold: float = None) -> Dict:
        pass

    def search_faces_by_image(self, CollectionId: str, Image: Dict, MaxFaces: int = None, FaceMatchThreshold: float = None) -> Dict:
        pass

    def start_celebrity_recognition(self, Video: Dict, ClientRequestToken: str = None, NotificationChannel: Dict = None, JobTag: str = None) -> Dict:
        pass

    def start_content_moderation(self, Video: Dict, MinConfidence: float = None, ClientRequestToken: str = None, NotificationChannel: Dict = None, JobTag: str = None) -> Dict:
        pass

    def start_face_detection(self, Video: Dict, ClientRequestToken: str = None, NotificationChannel: Dict = None, FaceAttributes: str = None, JobTag: str = None) -> Dict:
        pass

    def start_face_search(self, Video: Dict, CollectionId: str, ClientRequestToken: str = None, FaceMatchThreshold: float = None, NotificationChannel: Dict = None, JobTag: str = None) -> Dict:
        pass

    def start_label_detection(self, Video: Dict, ClientRequestToken: str = None, MinConfidence: float = None, NotificationChannel: Dict = None, JobTag: str = None) -> Dict:
        pass

    def start_person_tracking(self, Video: Dict, ClientRequestToken: str = None, NotificationChannel: Dict = None, JobTag: str = None) -> Dict:
        pass

    def start_stream_processor(self, Name: str) -> Dict:
        pass

    def stop_stream_processor(self, Name: str) -> Dict:
        pass
