from datetime import datetime
from typing import Union
from boto3.s3.transfer import TransferConfig
from botocore.paginate import Paginator
from typing import Callable
from typing import IO
from botocore.client import BaseClient
from typing import NoReturn
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def abort_multipart_upload(self, Bucket: str, Key: str, UploadId: str, RequestPayer: str = None) -> Dict:
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        pass

    def complete_multipart_upload(self, Bucket: str, Key: str, UploadId: str, MultipartUpload: Dict = None, RequestPayer: str = None) -> Dict:
        pass

    def copy(self, CopySource: Dict = None, Bucket: str = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, SourceClient: BaseClient = None, Config: TransferConfig = None) -> NoReturn:
        pass

    def copy_object(self, Bucket: str, CopySource: Union[str, Dict], Key: str, ACL: str = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentType: str = None, CopySourceIfMatch: str = None, CopySourceIfModifiedSince: datetime = None, CopySourceIfNoneMatch: str = None, CopySourceIfUnmodifiedSince: datetime = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, MetadataDirective: str = None, TaggingDirective: str = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, CopySourceSSECustomerAlgorithm: str = None, CopySourceSSECustomerKey: str = None, CopySourceSSECustomerKeyMD5: str = None, RequestPayer: str = None, Tagging: str = None) -> Dict:
        pass

    def create_bucket(self, Bucket: str, ACL: str = None, CreateBucketConfiguration: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None) -> Dict:
        pass

    def create_multipart_upload(self, Bucket: str, Key: str, ACL: str = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentType: str = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, RequestPayer: str = None, Tagging: str = None) -> Dict:
        pass

    def delete_bucket(self, Bucket: str) -> NoReturn:
        pass

    def delete_bucket_analytics_configuration(self, Bucket: str, Id: str) -> NoReturn:
        pass

    def delete_bucket_cors(self, Bucket: str) -> NoReturn:
        pass

    def delete_bucket_encryption(self, Bucket: str) -> NoReturn:
        pass

    def delete_bucket_inventory_configuration(self, Bucket: str, Id: str) -> NoReturn:
        pass

    def delete_bucket_lifecycle(self, Bucket: str) -> NoReturn:
        pass

    def delete_bucket_metrics_configuration(self, Bucket: str, Id: str) -> NoReturn:
        pass

    def delete_bucket_policy(self, Bucket: str) -> NoReturn:
        pass

    def delete_bucket_replication(self, Bucket: str) -> NoReturn:
        pass

    def delete_bucket_tagging(self, Bucket: str) -> NoReturn:
        pass

    def delete_bucket_website(self, Bucket: str) -> NoReturn:
        pass

    def delete_object(self, Bucket: str, Key: str, MFA: str = None, VersionId: str = None, RequestPayer: str = None) -> Dict:
        pass

    def delete_object_tagging(self, Bucket: str, Key: str, VersionId: str = None) -> Dict:
        pass

    def delete_objects(self, Bucket: str, Delete: Dict, MFA: str = None, RequestPayer: str = None) -> Dict:
        pass

    def download_file(self, Filename: str = None, Bucket: str = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None) -> NoReturn:
        pass

    def download_fileobj(self, Fileobj: IO = None, Bucket: str = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None) -> NoReturn:
        pass

    def generate_presigned_post(self, Bucket: str = None, Key: str = None, Fields: Dict = None, Conditions: List = None, ExpiresIn: int = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        pass

    def get_bucket_accelerate_configuration(self, Bucket: str) -> Dict:
        pass

    def get_bucket_acl(self, Bucket: str) -> Dict:
        pass

    def get_bucket_analytics_configuration(self, Bucket: str, Id: str) -> Dict:
        pass

    def get_bucket_cors(self, Bucket: str) -> Dict:
        pass

    def get_bucket_encryption(self, Bucket: str) -> Dict:
        pass

    def get_bucket_inventory_configuration(self, Bucket: str, Id: str) -> Dict:
        pass

    def get_bucket_lifecycle(self, Bucket: str) -> Dict:
        pass

    def get_bucket_lifecycle_configuration(self, Bucket: str) -> Dict:
        pass

    def get_bucket_location(self, Bucket: str) -> Dict:
        pass

    def get_bucket_logging(self, Bucket: str) -> Dict:
        pass

    def get_bucket_metrics_configuration(self, Bucket: str, Id: str) -> Dict:
        pass

    def get_bucket_notification(self, Bucket: str) -> Dict:
        pass

    def get_bucket_notification_configuration(self, Bucket: str) -> Dict:
        pass

    def get_bucket_policy(self, Bucket: str) -> Dict:
        pass

    def get_bucket_replication(self, Bucket: str) -> Dict:
        pass

    def get_bucket_request_payment(self, Bucket: str) -> Dict:
        pass

    def get_bucket_tagging(self, Bucket: str) -> Dict:
        pass

    def get_bucket_versioning(self, Bucket: str) -> Dict:
        pass

    def get_bucket_website(self, Bucket: str) -> Dict:
        pass

    def get_object(self, Bucket: str, Key: str, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, ResponseCacheControl: str = None, ResponseContentDisposition: str = None, ResponseContentEncoding: str = None, ResponseContentLanguage: str = None, ResponseContentType: str = None, ResponseExpires: datetime = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None) -> Dict:
        pass

    def get_object_acl(self, Bucket: str, Key: str, VersionId: str = None, RequestPayer: str = None) -> Dict:
        pass

    def get_object_tagging(self, Bucket: str, Key: str, VersionId: str = None) -> Dict:
        pass

    def get_object_torrent(self, Bucket: str, Key: str, RequestPayer: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def head_bucket(self, Bucket: str) -> NoReturn:
        pass

    def head_object(self, Bucket: str, Key: str, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None) -> Dict:
        pass

    def list_bucket_analytics_configurations(self, Bucket: str, ContinuationToken: str = None) -> Dict:
        pass

    def list_bucket_inventory_configurations(self, Bucket: str, ContinuationToken: str = None) -> Dict:
        pass

    def list_bucket_metrics_configurations(self, Bucket: str, ContinuationToken: str = None) -> Dict:
        pass

    def list_buckets(self) -> Dict:
        pass

    def list_multipart_uploads(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, KeyMarker: str = None, MaxUploads: int = None, Prefix: str = None, UploadIdMarker: str = None) -> Dict:
        pass

    def list_object_versions(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, KeyMarker: str = None, MaxKeys: int = None, Prefix: str = None, VersionIdMarker: str = None) -> Dict:
        pass

    def list_objects(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, Marker: str = None, MaxKeys: int = None, Prefix: str = None, RequestPayer: str = None) -> Dict:
        pass

    def list_objects_v2(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, MaxKeys: int = None, Prefix: str = None, ContinuationToken: str = None, FetchOwner: bool = None, StartAfter: str = None, RequestPayer: str = None) -> Dict:
        pass

    def list_parts(self, Bucket: str, Key: str, UploadId: str, MaxParts: int = None, PartNumberMarker: int = None, RequestPayer: str = None) -> Dict:
        pass

    def put_bucket_accelerate_configuration(self, Bucket: str, AccelerateConfiguration: Dict) -> NoReturn:
        pass

    def put_bucket_acl(self, Bucket: str, ACL: str = None, AccessControlPolicy: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None) -> NoReturn:
        pass

    def put_bucket_analytics_configuration(self, Bucket: str, Id: str, AnalyticsConfiguration: Dict) -> NoReturn:
        pass

    def put_bucket_cors(self, Bucket: str, CORSConfiguration: Dict) -> NoReturn:
        pass

    def put_bucket_encryption(self, Bucket: str, ServerSideEncryptionConfiguration: Dict, ContentMD5: str = None) -> NoReturn:
        pass

    def put_bucket_inventory_configuration(self, Bucket: str, Id: str, InventoryConfiguration: Dict) -> NoReturn:
        pass

    def put_bucket_lifecycle(self, Bucket: str, LifecycleConfiguration: Dict = None) -> NoReturn:
        pass

    def put_bucket_lifecycle_configuration(self, Bucket: str, LifecycleConfiguration: Dict = None) -> NoReturn:
        pass

    def put_bucket_logging(self, Bucket: str, BucketLoggingStatus: Dict) -> NoReturn:
        pass

    def put_bucket_metrics_configuration(self, Bucket: str, Id: str, MetricsConfiguration: Dict) -> NoReturn:
        pass

    def put_bucket_notification(self, Bucket: str, NotificationConfiguration: Dict) -> NoReturn:
        pass

    def put_bucket_notification_configuration(self, Bucket: str, NotificationConfiguration: Dict) -> NoReturn:
        pass

    def put_bucket_policy(self, Bucket: str, Policy: str, ConfirmRemoveSelfBucketAccess: bool = None) -> NoReturn:
        pass

    def put_bucket_replication(self, Bucket: str, ReplicationConfiguration: Dict) -> NoReturn:
        pass

    def put_bucket_request_payment(self, Bucket: str, RequestPaymentConfiguration: Dict) -> NoReturn:
        pass

    def put_bucket_tagging(self, Bucket: str, Tagging: Dict) -> NoReturn:
        pass

    def put_bucket_versioning(self, Bucket: str, VersioningConfiguration: Dict, MFA: str = None) -> NoReturn:
        pass

    def put_bucket_website(self, Bucket: str, WebsiteConfiguration: Dict) -> NoReturn:
        pass

    def put_object(self, Bucket: str, Key: str, ACL: str = None, Body: Union[bytes, IO] = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentLength: int = None, ContentMD5: str = None, ContentType: str = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, RequestPayer: str = None, Tagging: str = None) -> Dict:
        pass

    def put_object_acl(self, Bucket: str, Key: str, ACL: str = None, AccessControlPolicy: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None, RequestPayer: str = None, VersionId: str = None) -> Dict:
        pass

    def put_object_tagging(self, Bucket: str, Key: str, Tagging: Dict, VersionId: str = None, ContentMD5: str = None) -> Dict:
        pass

    def restore_object(self, Bucket: str, Key: str, VersionId: str = None, RestoreRequest: Dict = None, RequestPayer: str = None) -> Dict:
        pass

    def select_object_content(self, Bucket: str, Key: str, Expression: str, ExpressionType: str, InputSerialization: Dict, OutputSerialization: Dict, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestProgress: Dict = None) -> Dict:
        pass

    def upload_file(self, Filename: str = None, Bucket: str = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None) -> NoReturn:
        pass

    def upload_fileobj(self, Fileobj: IO = None, Bucket: str = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None) -> NoReturn:
        pass

    def upload_part(self, Bucket: str, Key: str, PartNumber: int, UploadId: str, Body: Union[bytes, IO] = None, ContentLength: int = None, ContentMD5: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None) -> Dict:
        pass

    def upload_part_copy(self, Bucket: str, CopySource: Union[str, Dict], Key: str, PartNumber: int, UploadId: str, CopySourceIfMatch: str = None, CopySourceIfModifiedSince: datetime = None, CopySourceIfNoneMatch: str = None, CopySourceIfUnmodifiedSince: datetime = None, CopySourceRange: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, CopySourceSSECustomerAlgorithm: str = None, CopySourceSSECustomerKey: str = None, CopySourceSSECustomerKeyMD5: str = None, RequestPayer: str = None) -> Dict:
        pass
