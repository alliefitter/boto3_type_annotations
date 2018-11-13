from typing import Dict
from botocore.paginate import Paginator


class ListMultipartUploads(Paginator):
    def paginate(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, Prefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListObjectVersions(Paginator):
    def paginate(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, Prefix: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListObjects(Paginator):
    def paginate(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, Prefix: str = None, RequestPayer: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListObjectsV2(Paginator):
    def paginate(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, Prefix: str = None, FetchOwner: bool = None, StartAfter: str = None, RequestPayer: str = None, PaginationConfig: Dict = None) -> Dict:
        pass


class ListParts(Paginator):
    def paginate(self, Bucket: str, Key: str, UploadId: str, RequestPayer: str = None, PaginationConfig: Dict = None) -> Dict:
        pass
