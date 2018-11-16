from typing import Optional
from typing import Union
from typing import Callable
from typing import IO
from boto3.resources.collection import ResourceCollection
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from typing import List
from datetime import datetime
from typing import NoReturn
from typing import Dict
from boto3.resources import base


class ServiceResource(base.ServiceResource):
    buckets: 'buckets'

    def Bucket(self, name: str = None) -> 'Bucket':
        """
        Creates a Bucket resource.::
        
          bucket = s3.Bucket(\'name\')
        
        :type name: string
        :param name: The Bucket\'s name identifier. This **must** be set.
        
        :rtype: :py:class:`S3.Bucket`
        :returns: A Bucket resource
        """
        pass

    def BucketAcl(self, bucket_name: str = None) -> 'BucketAcl':
        """
        Creates a BucketAcl resource.::
        
          bucket_acl = s3.BucketAcl(\'bucket_name\')
        
        :type bucket_name: string
        :param bucket_name: The BucketAcl\'s bucket_name identifier. This **must** be set.
        
        :rtype: :py:class:`S3.BucketAcl`
        :returns: A BucketAcl resource
        """
        pass

    def BucketCors(self, bucket_name: str = None) -> 'BucketCors':
        """
        Creates a BucketCors resource.::
        
          bucket_cors = s3.BucketCors(\'bucket_name\')
        
        :type bucket_name: string
        :param bucket_name: The BucketCors\'s bucket_name identifier. This **must** be set.
        
        :rtype: :py:class:`S3.BucketCors`
        :returns: A BucketCors resource
        """
        pass

    def BucketLifecycle(self, bucket_name: str = None) -> 'BucketLifecycle':
        """
        Creates a BucketLifecycle resource.::
        
          bucket_lifecycle = s3.BucketLifecycle(\'bucket_name\')
        
        :type bucket_name: string
        :param bucket_name: The BucketLifecycle\'s bucket_name identifier. This **must** be set.
        
        :rtype: :py:class:`S3.BucketLifecycle`
        :returns: A BucketLifecycle resource
        """
        pass

    def BucketLifecycleConfiguration(self, bucket_name: str = None) -> 'BucketLifecycleConfiguration':
        """
        Creates a BucketLifecycleConfiguration resource.::
        
          bucket_lifecycle_configuration = s3.BucketLifecycleConfiguration(\'bucket_name\')
        
        :type bucket_name: string
        :param bucket_name: The BucketLifecycleConfiguration\'s bucket_name identifier. This **must** be set.
        
        :rtype: :py:class:`S3.BucketLifecycleConfiguration`
        :returns: A BucketLifecycleConfiguration resource
        """
        pass

    def BucketLogging(self, bucket_name: str = None) -> 'BucketLogging':
        """
        Creates a BucketLogging resource.::
        
          bucket_logging = s3.BucketLogging(\'bucket_name\')
        
        :type bucket_name: string
        :param bucket_name: The BucketLogging\'s bucket_name identifier. This **must** be set.
        
        :rtype: :py:class:`S3.BucketLogging`
        :returns: A BucketLogging resource
        """
        pass

    def BucketNotification(self, bucket_name: str = None) -> 'BucketNotification':
        """
        Creates a BucketNotification resource.::
        
          bucket_notification = s3.BucketNotification(\'bucket_name\')
        
        :type bucket_name: string
        :param bucket_name: The BucketNotification\'s bucket_name identifier. This **must** be set.
        
        :rtype: :py:class:`S3.BucketNotification`
        :returns: A BucketNotification resource
        """
        pass

    def BucketPolicy(self, bucket_name: str = None) -> 'BucketPolicy':
        """
        Creates a BucketPolicy resource.::
        
          bucket_policy = s3.BucketPolicy(\'bucket_name\')
        
        :type bucket_name: string
        :param bucket_name: The BucketPolicy\'s bucket_name identifier. This **must** be set.
        
        :rtype: :py:class:`S3.BucketPolicy`
        :returns: A BucketPolicy resource
        """
        pass

    def BucketRequestPayment(self, bucket_name: str = None) -> 'BucketRequestPayment':
        """
        Creates a BucketRequestPayment resource.::
        
          bucket_request_payment = s3.BucketRequestPayment(\'bucket_name\')
        
        :type bucket_name: string
        :param bucket_name: The BucketRequestPayment\'s bucket_name identifier. This **must** be set.
        
        :rtype: :py:class:`S3.BucketRequestPayment`
        :returns: A BucketRequestPayment resource
        """
        pass

    def BucketTagging(self, bucket_name: str = None) -> 'BucketTagging':
        """
        Creates a BucketTagging resource.::
        
          bucket_tagging = s3.BucketTagging(\'bucket_name\')
        
        :type bucket_name: string
        :param bucket_name: The BucketTagging\'s bucket_name identifier. This **must** be set.
        
        :rtype: :py:class:`S3.BucketTagging`
        :returns: A BucketTagging resource
        """
        pass

    def BucketVersioning(self, bucket_name: str = None) -> 'BucketVersioning':
        """
        Creates a BucketVersioning resource.::
        
          bucket_versioning = s3.BucketVersioning(\'bucket_name\')
        
        :type bucket_name: string
        :param bucket_name: The BucketVersioning\'s bucket_name identifier. This **must** be set.
        
        :rtype: :py:class:`S3.BucketVersioning`
        :returns: A BucketVersioning resource
        """
        pass

    def BucketWebsite(self, bucket_name: str = None) -> 'BucketWebsite':
        """
        Creates a BucketWebsite resource.::
        
          bucket_website = s3.BucketWebsite(\'bucket_name\')
        
        :type bucket_name: string
        :param bucket_name: The BucketWebsite\'s bucket_name identifier. This **must** be set.
        
        :rtype: :py:class:`S3.BucketWebsite`
        :returns: A BucketWebsite resource
        """
        pass

    def MultipartUpload(self, bucket_name: str = None, object_key: str = None, id: str = None) -> 'MultipartUpload':
        """
        Creates a MultipartUpload resource.::
        
          multipart_upload = s3.MultipartUpload(\'bucket_name\',\'object_key\',\'id\')
        
        :type bucket_name: string
        :param bucket_name: The MultipartUpload\'s bucket_name identifier. This **must** be set.
        :type object_key: string
        :param object_key: The MultipartUpload\'s object_key identifier. This **must** be set.
        :type id: string
        :param id: The MultipartUpload\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`S3.MultipartUpload`
        :returns: A MultipartUpload resource
        """
        pass

    def MultipartUploadPart(self, bucket_name: str = None, object_key: str = None, multipart_upload_id: str = None, part_number: str = None) -> 'MultipartUploadPart':
        """
        Creates a MultipartUploadPart resource.::
        
          multipart_upload_part = s3.MultipartUploadPart(\'bucket_name\',\'object_key\',\'multipart_upload_id\',\'part_number\')
        
        :type bucket_name: string
        :param bucket_name: The MultipartUploadPart\'s bucket_name identifier. This **must** be set.
        :type object_key: string
        :param object_key: The MultipartUploadPart\'s object_key identifier. This **must** be set.
        :type multipart_upload_id: string
        :param multipart_upload_id: The MultipartUploadPart\'s multipart_upload_id identifier. This **must** be set.
        :type part_number: string
        :param part_number: The MultipartUploadPart\'s part_number identifier. This **must** be set.
        
        :rtype: :py:class:`S3.MultipartUploadPart`
        :returns: A MultipartUploadPart resource
        """
        pass

    def Object(self, bucket_name: str = None, key: str = None) -> 'Object':
        """
        Creates a Object resource.::
        
          object = s3.Object(\'bucket_name\',\'key\')
        
        :type bucket_name: string
        :param bucket_name: The Object\'s bucket_name identifier. This **must** be set.
        :type key: string
        :param key: The Object\'s key identifier. This **must** be set.
        
        :rtype: :py:class:`S3.Object`
        :returns: A Object resource
        """
        pass

    def ObjectAcl(self, bucket_name: str = None, object_key: str = None) -> 'ObjectAcl':
        """
        Creates a ObjectAcl resource.::
        
          object_acl = s3.ObjectAcl(\'bucket_name\',\'object_key\')
        
        :type bucket_name: string
        :param bucket_name: The ObjectAcl\'s bucket_name identifier. This **must** be set.
        :type object_key: string
        :param object_key: The ObjectAcl\'s object_key identifier. This **must** be set.
        
        :rtype: :py:class:`S3.ObjectAcl`
        :returns: A ObjectAcl resource
        """
        pass

    def ObjectSummary(self, bucket_name: str = None, key: str = None) -> 'ObjectSummary':
        """
        Creates a ObjectSummary resource.::
        
          object_summary = s3.ObjectSummary(\'bucket_name\',\'key\')
        
        :type bucket_name: string
        :param bucket_name: The ObjectSummary\'s bucket_name identifier. This **must** be set.
        :type key: string
        :param key: The ObjectSummary\'s key identifier. This **must** be set.
        
        :rtype: :py:class:`S3.ObjectSummary`
        :returns: A ObjectSummary resource
        """
        pass

    def ObjectVersion(self, bucket_name: str = None, object_key: str = None, id: str = None) -> 'ObjectVersion':
        """
        Creates a ObjectVersion resource.::
        
          object_version = s3.ObjectVersion(\'bucket_name\',\'object_key\',\'id\')
        
        :type bucket_name: string
        :param bucket_name: The ObjectVersion\'s bucket_name identifier. This **must** be set.
        :type object_key: string
        :param object_key: The ObjectVersion\'s object_key identifier. This **must** be set.
        :type id: string
        :param id: The ObjectVersion\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`S3.ObjectVersion`
        :returns: A ObjectVersion resource
        """
        pass

    def create_bucket(self, Bucket: str, ACL: str = None, CreateBucketConfiguration: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None) -> 'Bucket':
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CreateBucket>`_
        
        **Request Syntax** 
        ::
        
          bucket = s3.create_bucket(
              ACL=\'private\'|\'public-read\'|\'public-read-write\'|\'authenticated-read\',
              Bucket=\'string\',
              CreateBucketConfiguration={
                  \'LocationConstraint\': \'EU\'|\'eu-west-1\'|\'us-west-1\'|\'us-west-2\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'sa-east-1\'|\'cn-north-1\'|\'eu-central-1\'
              },
              GrantFullControl=\'string\',
              GrantRead=\'string\',
              GrantReadACP=\'string\',
              GrantWrite=\'string\',
              GrantWriteACP=\'string\'
          )
        :type ACL: string
        :param ACL: 
        
          The canned ACL to apply to the bucket.
        
        :type Bucket: string
        :param Bucket: **[REQUIRED]** 
        
        :type CreateBucketConfiguration: dict
        :param CreateBucketConfiguration: 
        
          - **LocationConstraint** *(string) --* 
        
            Specifies the region where the bucket will be created. If you don\'t specify a region, the bucket will be created in US Standard.
        
        :type GrantFullControl: string
        :param GrantFullControl: 
        
          Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.
        
        :type GrantRead: string
        :param GrantRead: 
        
          Allows grantee to list the objects in the bucket.
        
        :type GrantReadACP: string
        :param GrantReadACP: 
        
          Allows grantee to read the bucket ACL.
        
        :type GrantWrite: string
        :param GrantWrite: 
        
          Allows grantee to create, overwrite, and delete any object in the bucket.
        
        :type GrantWriteACP: string
        :param GrantWriteACP: 
        
          Allows grantee to write the ACL for the applicable bucket.
        
        :rtype: :py:class:`s3.Bucket`
        :returns: Bucket resource
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass


class Bucket(base.ServiceResource):
    creation_date: datetime
    name: str
    multipart_uploads: 'multipart_uploads'
    object_versions: 'object_versions'
    objects: 'objects'

    def copy(self, CopySource: Dict = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, SourceClient: BaseClient = None, Config: TransferConfig = None) -> NoReturn:
        """
        
        This is a managed transfer which will perform a multipart copy in
        multiple threads if necessary.
        
        Usage::
        
            import boto3
            s3 = boto3.resource(\'s3\')
            copy_source = {
                \'Bucket\': \'mybucket\',
                \'Key\': \'mykey\'
            }
            bucket = s3.Bucket(\'otherbucket\')
            bucket.copy(copy_source, \'otherkey\')
        
        :type CopySource: dict
        :param CopySource: The name of the source bucket, key name of the
            source object, and optional version ID of the source object. The
            dictionary format is:
            ``{\'Bucket\': \'bucket\', \'Key\': \'key\', \'VersionId\': \'id\'}``. Note
            that the ``VersionId`` key is optional and may be omitted.
        
        :type Key: str
        :param Key: The name of the key to copy to
        
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation
        
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the copy.
        
        :type SourceClient: botocore or boto3 Client
        :param SourceClient: The client to be used for operation that
            may happen at the source object. For example, this client is
            used for the head_object that determines the size of the copy.
            If no client is provided, the current client is used as the client
            for the source object.
        
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            copy.
        """
        pass

    def create(self, ACL: str = None, CreateBucketConfiguration: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CreateBucket>`_
        
        **Request Syntax** 
        ::
        
          response = bucket.create(
              ACL=\'private\'|\'public-read\'|\'public-read-write\'|\'authenticated-read\',
              CreateBucketConfiguration={
                  \'LocationConstraint\': \'EU\'|\'eu-west-1\'|\'us-west-1\'|\'us-west-2\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'sa-east-1\'|\'cn-north-1\'|\'eu-central-1\'
              },
              GrantFullControl=\'string\',
              GrantRead=\'string\',
              GrantReadACP=\'string\',
              GrantWrite=\'string\',
              GrantWriteACP=\'string\'
          )
        :type ACL: string
        :param ACL: 
        
          The canned ACL to apply to the bucket.
        
        :type CreateBucketConfiguration: dict
        :param CreateBucketConfiguration: 
        
          - **LocationConstraint** *(string) --* 
        
            Specifies the region where the bucket will be created. If you don\'t specify a region, the bucket will be created in US Standard.
        
        :type GrantFullControl: string
        :param GrantFullControl: 
        
          Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.
        
        :type GrantRead: string
        :param GrantRead: 
        
          Allows grantee to list the objects in the bucket.
        
        :type GrantReadACP: string
        :param GrantReadACP: 
        
          Allows grantee to read the bucket ACL.
        
        :type GrantWrite: string
        :param GrantWrite: 
        
          Allows grantee to create, overwrite, and delete any object in the bucket.
        
        :type GrantWriteACP: string
        :param GrantWriteACP: 
        
          Allows grantee to write the ACL for the applicable bucket.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Location\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Location** *(string) --* 
        """
        pass

    def delete(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucket>`_
        
        **Request Syntax** 
        ::
        
          response = bucket.delete()
          
        :returns: None
        """
        pass

    def delete_objects(self, Delete: Dict, MFA: str = None, RequestPayer: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteObjects>`_
        
        **Request Syntax** 
        ::
        
          response = bucket.delete_objects(
              Delete={
                  \'Objects\': [
                      {
                          \'Key\': \'string\',
                          \'VersionId\': \'string\'
                      },
                  ],
                  \'Quiet\': True|False
              },
              MFA=\'string\',
              RequestPayer=\'requester\'
          )
        :type Delete: dict
        :param Delete: **[REQUIRED]** 
        
          - **Objects** *(list) --* **[REQUIRED]** 
        
            - *(dict) --* 
        
              - **Key** *(string) --* **[REQUIRED]** 
        
                Key name of the object to delete.
        
              - **VersionId** *(string) --* 
        
                VersionId for the specific version of the object to delete.
        
          - **Quiet** *(boolean) --* 
        
            Element to enable quiet mode for the request. When you add this element, you must set its value to true.
        
        :type MFA: string
        :param MFA: 
        
          The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device.
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Deleted\': [
                    {
                        \'Key\': \'string\',
                        \'VersionId\': \'string\',
                        \'DeleteMarker\': True|False,
                        \'DeleteMarkerVersionId\': \'string\'
                    },
                ],
                \'RequestCharged\': \'requester\',
                \'Errors\': [
                    {
                        \'Key\': \'string\',
                        \'VersionId\': \'string\',
                        \'Code\': \'string\',
                        \'Message\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Deleted** *(list) --* 
              
              - *(dict) --* 
                
                - **Key** *(string) --* 
                
                - **VersionId** *(string) --* 
                
                - **DeleteMarker** *(boolean) --* 
                
                - **DeleteMarkerVersionId** *(string) --* 
            
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
            - **Errors** *(list) --* 
              
              - *(dict) --* 
                
                - **Key** *(string) --* 
                
                - **VersionId** *(string) --* 
                
                - **Code** *(string) --* 
                
                - **Message** *(string) --* 
            
        """
        pass

    def download_file(self, Filename: str = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None) -> NoReturn:
        """
        
        Usage::
        
            import boto3
            s3 = boto3.resource(\'s3\')
            s3.Bucket(\'mybucket\').download_file(\'hello.txt\', \'/tmp/hello.txt\')
        
        Similar behavior as S3Transfer\'s download_file() method,
        except that parameters are capitalized. Detailed examples can be found at
        :ref:`S3Transfer\'s Usage <ref_s3transfer_usage>`.
        
        :type Filename: str
        :param Filename: The path to the file to download to.
        
        :type Key: str
        :param Key: The name of the key to download from.
        
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.
        
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the download.
        
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            transfer.
        """
        pass

    def download_fileobj(self, Fileobj: IO = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None) -> NoReturn:
        """
        
        The file-like object must be in binary mode.
        
        This is a managed transfer which will perform a multipart download in
        multiple threads if necessary.
        
        Usage::
        
            import boto3
            s3 = boto3.resource(\'s3\')
            bucket = s3.Bucket(\'mybucket\')
        
            with open(\'filename\', \'wb\') as data:
                bucket.download_fileobj(\'mykey\', data)
        
        :type Fileobj: a file-like object
        :param Fileobj: A file-like object to download into. At a minimum, it must
            implement the `write` method and must accept bytes.
        
        :type Key: str
        :param Key: The name of the key to download from.
        
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.
        
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the download.
        
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            download.
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self) -> NoReturn:
        """
        resource.
        """
        pass

    def put_object(self, Key: str, ACL: str = None, Body: Union[bytes, IO] = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentLength: int = None, ContentMD5: str = None, ContentType: str = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, RequestPayer: str = None, Tagging: str = None) -> 'Object':
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObject>`_
        
        **Request Syntax** 
        ::
        
          object = bucket.put_object(
              ACL=\'private\'|\'public-read\'|\'public-read-write\'|\'authenticated-read\'|\'aws-exec-read\'|\'bucket-owner-read\'|\'bucket-owner-full-control\',
              Body=b\'bytes\'|file,
              CacheControl=\'string\',
              ContentDisposition=\'string\',
              ContentEncoding=\'string\',
              ContentLanguage=\'string\',
              ContentLength=123,
              ContentMD5=\'string\',
              ContentType=\'string\',
              Expires=datetime(2015, 1, 1),
              GrantFullControl=\'string\',
              GrantRead=\'string\',
              GrantReadACP=\'string\',
              GrantWriteACP=\'string\',
              Key=\'string\',
              Metadata={
                  \'string\': \'string\'
              },
              ServerSideEncryption=\'AES256\'|\'aws:kms\',
              StorageClass=\'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
              WebsiteRedirectLocation=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              SSEKMSKeyId=\'string\',
              RequestPayer=\'requester\',
              Tagging=\'string\'
          )
        :type ACL: string
        :param ACL: 
        
          The canned ACL to apply to the object.
        
        :type Body: bytes or seekable file-like object
        :param Body: 
        
          Object data.
        
        :type CacheControl: string
        :param CacheControl: 
        
          Specifies caching behavior along the request/reply chain.
        
        :type ContentDisposition: string
        :param ContentDisposition: 
        
          Specifies presentational information for the object.
        
        :type ContentEncoding: string
        :param ContentEncoding: 
        
          Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        
        :type ContentLanguage: string
        :param ContentLanguage: 
        
          The language the content is in.
        
        :type ContentLength: integer
        :param ContentLength: 
        
          Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically.
        
        :type ContentMD5: string
        :param ContentMD5: 
        
          The base64-encoded 128-bit MD5 digest of the part data.
        
        :type ContentType: string
        :param ContentType: 
        
          A standard MIME type describing the format of the object data.
        
        :type Expires: datetime
        :param Expires: 
        
          The date and time at which the object is no longer cacheable.
        
        :type GrantFullControl: string
        :param GrantFullControl: 
        
          Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
        
        :type GrantRead: string
        :param GrantRead: 
        
          Allows grantee to read the object data and its metadata.
        
        :type GrantReadACP: string
        :param GrantReadACP: 
        
          Allows grantee to read the object ACL.
        
        :type GrantWriteACP: string
        :param GrantWriteACP: 
        
          Allows grantee to write the ACL for the applicable object.
        
        :type Key: string
        :param Key: **[REQUIRED]** 
        
          Object key for which the PUT operation was initiated.
        
        :type Metadata: dict
        :param Metadata: 
        
          A map of metadata to store with the object in S3.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type ServerSideEncryption: string
        :param ServerSideEncryption: 
        
          The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
        :type StorageClass: string
        :param StorageClass: 
        
          The type of storage to use for the object. Defaults to \'STANDARD\'.
        
        :type WebsiteRedirectLocation: string
        :param WebsiteRedirectLocation: 
        
          If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type SSEKMSKeyId: string
        :param SSEKMSKeyId: 
        
          Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type Tagging: string
        :param Tagging: 
        
          The tag-set for the object. The tag-set must be encoded as URL Query parameters
        
        :rtype: :py:class:`s3.Object`
        :returns: Object resource
        """
        pass

    def upload_file(self, Filename: str = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None) -> NoReturn:
        """
        
        Usage::
        
            import boto3
            s3 = boto3.resource(\'s3\')
            s3.Bucket(\'mybucket\').upload_file(\'/tmp/hello.txt\', \'hello.txt\')
        
        Similar behavior as S3Transfer\'s upload_file() method,
        except that parameters are capitalized. Detailed examples can be found at
        :ref:`S3Transfer\'s Usage <ref_s3transfer_usage>`.
        
        :type Filename: str
        :param Filename: The path to the file to upload.
        
        :type Key: str
        :param Key: The name of the key to upload to.
        
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.
        
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the upload.
        
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            transfer.
        """
        pass

    def upload_fileobj(self, Fileobj: IO = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None) -> NoReturn:
        """
        
        The file-like object must be in binary mode.
        
        This is a managed transfer which will perform a multipart upload in
        multiple threads if necessary.
        
        Usage::
        
            import boto3
            s3 = boto3.resource(\'s3\')
            bucket = s3.Bucket(\'mybucket\')
        
            with open(\'filename\', \'rb\') as data:
                bucket.upload_fileobj(data, \'mykey\')
        
        :type Fileobj: a file-like object
        :param Fileobj: A file-like object to upload. At a minimum, it must
            implement the `read` method, and must return bytes.
        
        :type Key: str
        :param Key: The name of the key to upload to.
        
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.
        
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the upload.
        
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            upload.
        """
        pass

    def wait_until_exists(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadBucket>`_
        
        **Request Syntax** 
        ::
        
          bucket.wait_until_exists()
          
        :returns: None
        """
        pass

    def wait_until_not_exists(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadBucket>`_
        
        **Request Syntax** 
        ::
        
          bucket.wait_until_not_exists()
          
        :returns: None
        """
        pass


class BucketAcl(base.ServiceResource):
    owner: Dict
    grants: List
    bucket_name: str

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_acl.load()
        :returns: None
        """
        pass

    def put(self, ACL: str = None, AccessControlPolicy: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketAcl>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_acl.put(
              ACL=\'private\'|\'public-read\'|\'public-read-write\'|\'authenticated-read\',
              AccessControlPolicy={
                  \'Grants\': [
                      {
                          \'Grantee\': {
                              \'DisplayName\': \'string\',
                              \'EmailAddress\': \'string\',
                              \'ID\': \'string\',
                              \'Type\': \'CanonicalUser\'|\'AmazonCustomerByEmail\'|\'Group\',
                              \'URI\': \'string\'
                          },
                          \'Permission\': \'FULL_CONTROL\'|\'WRITE\'|\'WRITE_ACP\'|\'READ\'|\'READ_ACP\'
                      },
                  ],
                  \'Owner\': {
                      \'DisplayName\': \'string\',
                      \'ID\': \'string\'
                  }
              },
              GrantFullControl=\'string\',
              GrantRead=\'string\',
              GrantReadACP=\'string\',
              GrantWrite=\'string\',
              GrantWriteACP=\'string\'
          )
        :type ACL: string
        :param ACL: 
        
          The canned ACL to apply to the bucket.
        
        :type AccessControlPolicy: dict
        :param AccessControlPolicy: 
        
          - **Grants** *(list) --* 
        
            A list of grants.
        
            - *(dict) --* 
        
              - **Grantee** *(dict) --* 
        
                - **DisplayName** *(string) --* 
        
                  Screen name of the grantee.
        
                - **EmailAddress** *(string) --* 
        
                  Email address of the grantee.
        
                - **ID** *(string) --* 
        
                  The canonical user ID of the grantee.
        
                - **Type** *(string) --* **[REQUIRED]** 
        
                  Type of grantee
        
                - **URI** *(string) --* 
        
                  URI of the grantee group.
        
              - **Permission** *(string) --* 
        
                Specifies the permission given to the grantee.
        
          - **Owner** *(dict) --* 
        
            - **DisplayName** *(string) --* 
        
            - **ID** *(string) --* 
        
        :type GrantFullControl: string
        :param GrantFullControl: 
        
          Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.
        
        :type GrantRead: string
        :param GrantRead: 
        
          Allows grantee to list the objects in the bucket.
        
        :type GrantReadACP: string
        :param GrantReadACP: 
        
          Allows grantee to read the bucket ACL.
        
        :type GrantWrite: string
        :param GrantWrite: 
        
          Allows grantee to create, overwrite, and delete any object in the bucket.
        
        :type GrantWriteACP: string
        :param GrantWriteACP: 
        
          Allows grantee to write the ACL for the applicable bucket.
        
        :returns: None
        """
        pass

    def reload(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_acl.load()
        :returns: None
        """
        pass


class BucketCors(base.ServiceResource):
    cors_rules: List
    bucket_name: str

    def delete(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketCors>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_cors.delete()
          
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_cors.load()
        :returns: None
        """
        pass

    def put(self, CORSConfiguration: Dict) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketCors>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_cors.put(
              CORSConfiguration={
                  \'CORSRules\': [
                      {
                          \'AllowedHeaders\': [
                              \'string\',
                          ],
                          \'AllowedMethods\': [
                              \'string\',
                          ],
                          \'AllowedOrigins\': [
                              \'string\',
                          ],
                          \'ExposeHeaders\': [
                              \'string\',
                          ],
                          \'MaxAgeSeconds\': 123
                      },
                  ]
              },
              
          )
        :type CORSConfiguration: dict
        :param CORSConfiguration: **[REQUIRED]** 
        
          - **CORSRules** *(list) --* **[REQUIRED]** 
        
            - *(dict) --* 
        
              - **AllowedHeaders** *(list) --* 
        
                Specifies which headers are allowed in a pre-flight OPTIONS request.
        
                - *(string) --* 
        
              - **AllowedMethods** *(list) --* **[REQUIRED]** 
        
                Identifies HTTP methods that the domain/origin specified in the rule is allowed to execute.
        
                - *(string) --* 
        
              - **AllowedOrigins** *(list) --* **[REQUIRED]** 
        
                One or more origins you want customers to be able to access the bucket from.
        
                - *(string) --* 
        
              - **ExposeHeaders** *(list) --* 
        
                One or more headers in the response that you want customers to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).
        
                - *(string) --* 
        
              - **MaxAgeSeconds** *(integer) --* 
        
                The time in seconds that your browser is to cache the preflight response for the specified resource.
        
        :returns: None
        """
        pass

    def reload(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_cors.load()
        :returns: None
        """
        pass


class BucketLifecycle(base.ServiceResource):
    rules: List
    bucket_name: str

    def delete(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketLifecycle>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_lifecycle.delete()
          
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_lifecycle.load()
        :returns: None
        """
        pass

    def put(self, LifecycleConfiguration: Dict = None) -> NoReturn:
        """
        
        .. danger::
        
            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketLifecycle>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_lifecycle.put(
              LifecycleConfiguration={
                  \'Rules\': [
                      {
                          \'Expiration\': {
                              \'Date\': datetime(2015, 1, 1),
                              \'Days\': 123,
                              \'ExpiredObjectDeleteMarker\': True|False
                          },
                          \'ID\': \'string\',
                          \'Prefix\': \'string\',
                          \'Status\': \'Enabled\'|\'Disabled\',
                          \'Transition\': {
                              \'Date\': datetime(2015, 1, 1),
                              \'Days\': 123,
                              \'StorageClass\': \'GLACIER\'|\'STANDARD_IA\'|\'ONEZONE_IA\'
                          },
                          \'NoncurrentVersionTransition\': {
                              \'NoncurrentDays\': 123,
                              \'StorageClass\': \'GLACIER\'|\'STANDARD_IA\'|\'ONEZONE_IA\'
                          },
                          \'NoncurrentVersionExpiration\': {
                              \'NoncurrentDays\': 123
                          },
                          \'AbortIncompleteMultipartUpload\': {
                              \'DaysAfterInitiation\': 123
                          }
                      },
                  ]
              }
          )
        :type LifecycleConfiguration: dict
        :param LifecycleConfiguration: 
        
          - **Rules** *(list) --* **[REQUIRED]** 
        
            - *(dict) --* 
        
              - **Expiration** *(dict) --* 
        
                - **Date** *(datetime) --* 
        
                  Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.
        
                - **Days** *(integer) --* 
        
                  Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
        
                - **ExpiredObjectDeleteMarker** *(boolean) --* 
        
                  Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.
        
              - **ID** *(string) --* 
        
                Unique identifier for the rule. The value cannot be longer than 255 characters.
        
              - **Prefix** *(string) --* **[REQUIRED]** 
        
                Prefix identifying one or more objects to which the rule applies.
        
              - **Status** *(string) --* **[REQUIRED]** 
        
                If \'Enabled\', the rule is currently being applied. If \'Disabled\', the rule is not currently being applied.
        
              - **Transition** *(dict) --* 
        
                - **Date** *(datetime) --* 
        
                  Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.
        
                - **Days** *(integer) --* 
        
                  Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
        
                - **StorageClass** *(string) --* 
        
                  The class of storage used to store the object.
        
              - **NoncurrentVersionTransition** *(dict) --* 
        
                Container for the transition rule that describes when noncurrent objects transition to the STANDARD_IA, ONEZONE_IA or GLACIER storage class. If your bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to the STANDARD_IA, ONEZONE_IA or GLACIER storage class at a specific period in the object\'s lifetime.
        
                - **NoncurrentDays** *(integer) --* 
        
                  Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see `How Amazon S3 Calculates When an Object Became Noncurrent <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the Amazon Simple Storage Service Developer Guide.
        
                - **StorageClass** *(string) --* 
        
                  The class of storage used to store the object.
        
              - **NoncurrentVersionExpiration** *(dict) --* 
        
                Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes the noncurrent object versions. You set this lifecycle configuration action on a bucket that has versioning enabled (or suspended) to request that Amazon S3 delete noncurrent object versions at a specific period in the object\'s lifetime.
        
                - **NoncurrentDays** *(integer) --* 
        
                  Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see `How Amazon S3 Calculates When an Object Became Noncurrent <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the Amazon Simple Storage Service Developer Guide.
        
              - **AbortIncompleteMultipartUpload** *(dict) --* 
        
                Specifies the days since the initiation of an Incomplete Multipart Upload that Lifecycle will wait before permanently removing all parts of the upload.
        
                - **DaysAfterInitiation** *(integer) --* 
        
                  Indicates the number of days that must pass since initiation for Lifecycle to abort an Incomplete Multipart Upload.
        
        :returns: None
        """
        pass

    def reload(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_lifecycle.load()
        :returns: None
        """
        pass


class BucketLifecycleConfiguration(base.ServiceResource):
    rules: List
    bucket_name: str

    def delete(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketLifecycle>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_lifecycle_configuration.delete()
          
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_lifecycle_configuration.load()
        :returns: None
        """
        pass

    def put(self, LifecycleConfiguration: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketLifecycleConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_lifecycle_configuration.put(
              LifecycleConfiguration={
                  \'Rules\': [
                      {
                          \'Expiration\': {
                              \'Date\': datetime(2015, 1, 1),
                              \'Days\': 123,
                              \'ExpiredObjectDeleteMarker\': True|False
                          },
                          \'ID\': \'string\',
                          \'Prefix\': \'string\',
                          \'Filter\': {
                              \'Prefix\': \'string\',
                              \'Tag\': {
                                  \'Key\': \'string\',
                                  \'Value\': \'string\'
                              },
                              \'And\': {
                                  \'Prefix\': \'string\',
                                  \'Tags\': [
                                      {
                                          \'Key\': \'string\',
                                          \'Value\': \'string\'
                                      },
                                  ]
                              }
                          },
                          \'Status\': \'Enabled\'|\'Disabled\',
                          \'Transitions\': [
                              {
                                  \'Date\': datetime(2015, 1, 1),
                                  \'Days\': 123,
                                  \'StorageClass\': \'GLACIER\'|\'STANDARD_IA\'|\'ONEZONE_IA\'
                              },
                          ],
                          \'NoncurrentVersionTransitions\': [
                              {
                                  \'NoncurrentDays\': 123,
                                  \'StorageClass\': \'GLACIER\'|\'STANDARD_IA\'|\'ONEZONE_IA\'
                              },
                          ],
                          \'NoncurrentVersionExpiration\': {
                              \'NoncurrentDays\': 123
                          },
                          \'AbortIncompleteMultipartUpload\': {
                              \'DaysAfterInitiation\': 123
                          }
                      },
                  ]
              }
          )
        :type LifecycleConfiguration: dict
        :param LifecycleConfiguration: 
        
          - **Rules** *(list) --* **[REQUIRED]** 
        
            - *(dict) --* 
        
              - **Expiration** *(dict) --* 
        
                - **Date** *(datetime) --* 
        
                  Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.
        
                - **Days** *(integer) --* 
        
                  Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
        
                - **ExpiredObjectDeleteMarker** *(boolean) --* 
        
                  Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.
        
              - **ID** *(string) --* 
        
                Unique identifier for the rule. The value cannot be longer than 255 characters.
        
              - **Prefix** *(string) --* 
        
                Prefix identifying one or more objects to which the rule applies. This is deprecated; use Filter instead.
        
              - **Filter** *(dict) --* 
        
                The Filter is used to identify objects that a Lifecycle Rule applies to. A Filter must have exactly one of Prefix, Tag, or And specified.
        
                - **Prefix** *(string) --* 
        
                  Prefix identifying one or more objects to which the rule applies.
        
                - **Tag** *(dict) --* 
        
                  This tag must exist in the object\'s tag set in order for the rule to apply.
        
                  - **Key** *(string) --* **[REQUIRED]** 
        
                    Name of the tag.
        
                  - **Value** *(string) --* **[REQUIRED]** 
        
                    Value of the tag.
        
                - **And** *(dict) --* 
        
                  This is used in a Lifecycle Rule Filter to apply a logical AND to two or more predicates. The Lifecycle Rule will apply to any object matching all of the predicates configured inside the And operator.
        
                  - **Prefix** *(string) --* 
        
                  - **Tags** *(list) --* 
        
                    All of these tags must exist in the object\'s tag set in order for the rule to apply.
        
                    - *(dict) --* 
        
                      - **Key** *(string) --* **[REQUIRED]** 
        
                        Name of the tag.
        
                      - **Value** *(string) --* **[REQUIRED]** 
        
                        Value of the tag.
        
              - **Status** *(string) --* **[REQUIRED]** 
        
                If \'Enabled\', the rule is currently being applied. If \'Disabled\', the rule is not currently being applied.
        
              - **Transitions** *(list) --* 
        
                - *(dict) --* 
        
                  - **Date** *(datetime) --* 
        
                    Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format.
        
                  - **Days** *(integer) --* 
        
                    Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
        
                  - **StorageClass** *(string) --* 
        
                    The class of storage used to store the object.
        
              - **NoncurrentVersionTransitions** *(list) --* 
        
                - *(dict) --* 
        
                  Container for the transition rule that describes when noncurrent objects transition to the STANDARD_IA, ONEZONE_IA or GLACIER storage class. If your bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to the STANDARD_IA, ONEZONE_IA or GLACIER storage class at a specific period in the object\'s lifetime.
        
                  - **NoncurrentDays** *(integer) --* 
        
                    Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see `How Amazon S3 Calculates When an Object Became Noncurrent <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the Amazon Simple Storage Service Developer Guide.
        
                  - **StorageClass** *(string) --* 
        
                    The class of storage used to store the object.
        
              - **NoncurrentVersionExpiration** *(dict) --* 
        
                Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes the noncurrent object versions. You set this lifecycle configuration action on a bucket that has versioning enabled (or suspended) to request that Amazon S3 delete noncurrent object versions at a specific period in the object\'s lifetime.
        
                - **NoncurrentDays** *(integer) --* 
        
                  Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see `How Amazon S3 Calculates When an Object Became Noncurrent <http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the Amazon Simple Storage Service Developer Guide.
        
              - **AbortIncompleteMultipartUpload** *(dict) --* 
        
                Specifies the days since the initiation of an Incomplete Multipart Upload that Lifecycle will wait before permanently removing all parts of the upload.
        
                - **DaysAfterInitiation** *(integer) --* 
        
                  Indicates the number of days that must pass since initiation for Lifecycle to abort an Incomplete Multipart Upload.
        
        :returns: None
        """
        pass

    def reload(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_lifecycle_configuration.load()
        :returns: None
        """
        pass


class BucketLogging(base.ServiceResource):
    logging_enabled: Dict
    bucket_name: str

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_logging.load()
        :returns: None
        """
        pass

    def put(self, BucketLoggingStatus: Dict) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketLogging>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_logging.put(
              BucketLoggingStatus={
                  \'LoggingEnabled\': {
                      \'TargetBucket\': \'string\',
                      \'TargetGrants\': [
                          {
                              \'Grantee\': {
                                  \'DisplayName\': \'string\',
                                  \'EmailAddress\': \'string\',
                                  \'ID\': \'string\',
                                  \'Type\': \'CanonicalUser\'|\'AmazonCustomerByEmail\'|\'Group\',
                                  \'URI\': \'string\'
                              },
                              \'Permission\': \'FULL_CONTROL\'|\'READ\'|\'WRITE\'
                          },
                      ],
                      \'TargetPrefix\': \'string\'
                  }
              },
              
          )
        :type BucketLoggingStatus: dict
        :param BucketLoggingStatus: **[REQUIRED]** 
        
          - **LoggingEnabled** *(dict) --* 
        
            Container for logging information. Presence of this element indicates that logging is enabled. Parameters TargetBucket and TargetPrefix are required in this case.
        
            - **TargetBucket** *(string) --* **[REQUIRED]** 
        
              Specifies the bucket where you want Amazon S3 to store server access logs. You can have your logs delivered to any bucket that you own, including the same bucket that is being logged. You can also configure multiple buckets to deliver their logs to the same target bucket. In this case you should choose a different TargetPrefix for each source bucket so that the delivered log files can be distinguished by key.
        
            - **TargetGrants** *(list) --* 
        
              - *(dict) --* 
        
                - **Grantee** *(dict) --* 
        
                  - **DisplayName** *(string) --* 
        
                    Screen name of the grantee.
        
                  - **EmailAddress** *(string) --* 
        
                    Email address of the grantee.
        
                  - **ID** *(string) --* 
        
                    The canonical user ID of the grantee.
        
                  - **Type** *(string) --* **[REQUIRED]** 
        
                    Type of grantee
        
                  - **URI** *(string) --* 
        
                    URI of the grantee group.
        
                - **Permission** *(string) --* 
        
                  Logging permissions assigned to the Grantee for the bucket.
        
            - **TargetPrefix** *(string) --* **[REQUIRED]** 
        
              This element lets you specify a prefix for the keys that the log files will be stored under.
        
        :returns: None
        """
        pass

    def reload(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_logging.load()
        :returns: None
        """
        pass


class BucketNotification(base.ServiceResource):
    topic_configurations: List
    queue_configurations: List
    lambda_function_configurations: List
    bucket_name: str

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_notification.load()
        :returns: None
        """
        pass

    def put(self, NotificationConfiguration: Dict) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketNotificationConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_notification.put(
              NotificationConfiguration={
                  \'TopicConfigurations\': [
                      {
                          \'Id\': \'string\',
                          \'TopicArn\': \'string\',
                          \'Events\': [
                              \'s3:ReducedRedundancyLostObject\'|\'s3:ObjectCreated:*\'|\'s3:ObjectCreated:Put\'|\'s3:ObjectCreated:Post\'|\'s3:ObjectCreated:Copy\'|\'s3:ObjectCreated:CompleteMultipartUpload\'|\'s3:ObjectRemoved:*\'|\'s3:ObjectRemoved:Delete\'|\'s3:ObjectRemoved:DeleteMarkerCreated\',
                          ],
                          \'Filter\': {
                              \'Key\': {
                                  \'FilterRules\': [
                                      {
                                          \'Name\': \'prefix\'|\'suffix\',
                                          \'Value\': \'string\'
                                      },
                                  ]
                              }
                          }
                      },
                  ],
                  \'QueueConfigurations\': [
                      {
                          \'Id\': \'string\',
                          \'QueueArn\': \'string\',
                          \'Events\': [
                              \'s3:ReducedRedundancyLostObject\'|\'s3:ObjectCreated:*\'|\'s3:ObjectCreated:Put\'|\'s3:ObjectCreated:Post\'|\'s3:ObjectCreated:Copy\'|\'s3:ObjectCreated:CompleteMultipartUpload\'|\'s3:ObjectRemoved:*\'|\'s3:ObjectRemoved:Delete\'|\'s3:ObjectRemoved:DeleteMarkerCreated\',
                          ],
                          \'Filter\': {
                              \'Key\': {
                                  \'FilterRules\': [
                                      {
                                          \'Name\': \'prefix\'|\'suffix\',
                                          \'Value\': \'string\'
                                      },
                                  ]
                              }
                          }
                      },
                  ],
                  \'LambdaFunctionConfigurations\': [
                      {
                          \'Id\': \'string\',
                          \'LambdaFunctionArn\': \'string\',
                          \'Events\': [
                              \'s3:ReducedRedundancyLostObject\'|\'s3:ObjectCreated:*\'|\'s3:ObjectCreated:Put\'|\'s3:ObjectCreated:Post\'|\'s3:ObjectCreated:Copy\'|\'s3:ObjectCreated:CompleteMultipartUpload\'|\'s3:ObjectRemoved:*\'|\'s3:ObjectRemoved:Delete\'|\'s3:ObjectRemoved:DeleteMarkerCreated\',
                          ],
                          \'Filter\': {
                              \'Key\': {
                                  \'FilterRules\': [
                                      {
                                          \'Name\': \'prefix\'|\'suffix\',
                                          \'Value\': \'string\'
                                      },
                                  ]
                              }
                          }
                      },
                  ]
              }
          )
        :type NotificationConfiguration: dict
        :param NotificationConfiguration: **[REQUIRED]** 
        
          Container for specifying the notification configuration of the bucket. If this element is empty, notifications are turned off on the bucket.
        
          - **TopicConfigurations** *(list) --* 
        
            - *(dict) --* 
        
              Container for specifying the configuration when you want Amazon S3 to publish events to an Amazon Simple Notification Service (Amazon SNS) topic.
        
              - **Id** *(string) --* 
        
                Optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.
        
              - **TopicArn** *(string) --* **[REQUIRED]** 
        
                Amazon SNS topic ARN to which Amazon S3 will publish a message when it detects events of specified type.
        
              - **Events** *(list) --* **[REQUIRED]** 
        
                - *(string) --* 
        
                  Bucket event for which to send notifications.
        
              - **Filter** *(dict) --* 
        
                Container for object key name filtering rules. For information about key name filtering, go to `Configuring Event Notifications <http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the Amazon Simple Storage Service Developer Guide.
        
                - **Key** *(dict) --* 
        
                  Container for object key name prefix and suffix filtering rules.
        
                  - **FilterRules** *(list) --* 
        
                    A list of containers for key value pair that defines the criteria for the filter rule.
        
                    - *(dict) --* 
        
                      Container for key value pair that defines the criteria for the filter rule.
        
                      - **Name** *(string) --* 
        
                        Object key name prefix or suffix identifying one or more objects to which the filtering rule applies. Maximum prefix length can be up to 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, go to `Configuring Event Notifications <http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the Amazon Simple Storage Service Developer Guide.
        
                      - **Value** *(string) --* 
        
          - **QueueConfigurations** *(list) --* 
        
            - *(dict) --* 
        
              Container for specifying an configuration when you want Amazon S3 to publish events to an Amazon Simple Queue Service (Amazon SQS) queue.
        
              - **Id** *(string) --* 
        
                Optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.
        
              - **QueueArn** *(string) --* **[REQUIRED]** 
        
                Amazon SQS queue ARN to which Amazon S3 will publish a message when it detects events of specified type.
        
              - **Events** *(list) --* **[REQUIRED]** 
        
                - *(string) --* 
        
                  Bucket event for which to send notifications.
        
              - **Filter** *(dict) --* 
        
                Container for object key name filtering rules. For information about key name filtering, go to `Configuring Event Notifications <http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the Amazon Simple Storage Service Developer Guide.
        
                - **Key** *(dict) --* 
        
                  Container for object key name prefix and suffix filtering rules.
        
                  - **FilterRules** *(list) --* 
        
                    A list of containers for key value pair that defines the criteria for the filter rule.
        
                    - *(dict) --* 
        
                      Container for key value pair that defines the criteria for the filter rule.
        
                      - **Name** *(string) --* 
        
                        Object key name prefix or suffix identifying one or more objects to which the filtering rule applies. Maximum prefix length can be up to 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, go to `Configuring Event Notifications <http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the Amazon Simple Storage Service Developer Guide.
        
                      - **Value** *(string) --* 
        
          - **LambdaFunctionConfigurations** *(list) --* 
        
            - *(dict) --* 
        
              Container for specifying the AWS Lambda notification configuration.
        
              - **Id** *(string) --* 
        
                Optional unique identifier for configurations in a notification configuration. If you don\'t provide one, Amazon S3 will assign an ID.
        
              - **LambdaFunctionArn** *(string) --* **[REQUIRED]** 
        
                Lambda cloud function ARN that Amazon S3 can invoke when it detects events of the specified type.
        
              - **Events** *(list) --* **[REQUIRED]** 
        
                - *(string) --* 
        
                  Bucket event for which to send notifications.
        
              - **Filter** *(dict) --* 
        
                Container for object key name filtering rules. For information about key name filtering, go to `Configuring Event Notifications <http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the Amazon Simple Storage Service Developer Guide.
        
                - **Key** *(dict) --* 
        
                  Container for object key name prefix and suffix filtering rules.
        
                  - **FilterRules** *(list) --* 
        
                    A list of containers for key value pair that defines the criteria for the filter rule.
        
                    - *(dict) --* 
        
                      Container for key value pair that defines the criteria for the filter rule.
        
                      - **Name** *(string) --* 
        
                        Object key name prefix or suffix identifying one or more objects to which the filtering rule applies. Maximum prefix length can be up to 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, go to `Configuring Event Notifications <http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the Amazon Simple Storage Service Developer Guide.
        
                      - **Value** *(string) --* 
        
        :returns: None
        """
        pass

    def reload(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_notification.load()
        :returns: None
        """
        pass


class BucketPolicy(base.ServiceResource):
    policy: str
    bucket_name: str

    def delete(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_policy.delete()
          
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_policy.load()
        :returns: None
        """
        pass

    def put(self, Policy: str, ConfirmRemoveSelfBucketAccess: bool = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_policy.put(
              ConfirmRemoveSelfBucketAccess=True|False,
              Policy=\'string\'
          )
        :type ConfirmRemoveSelfBucketAccess: boolean
        :param ConfirmRemoveSelfBucketAccess: 
        
          Set this parameter to true to confirm that you want to remove your permissions to change this bucket policy in the future.
        
        :type Policy: string
        :param Policy: **[REQUIRED]** 
        
          The bucket policy as a JSON document.
        
        :returns: None
        """
        pass

    def reload(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_policy.load()
        :returns: None
        """
        pass


class BucketRequestPayment(base.ServiceResource):
    payer: str
    bucket_name: str

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_request_payment.load()
        :returns: None
        """
        pass

    def put(self, RequestPaymentConfiguration: Dict) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketRequestPayment>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_request_payment.put(
              RequestPaymentConfiguration={
                  \'Payer\': \'Requester\'|\'BucketOwner\'
              }
          )
        :type RequestPaymentConfiguration: dict
        :param RequestPaymentConfiguration: **[REQUIRED]** 
        
          - **Payer** *(string) --* **[REQUIRED]** 
        
            Specifies who pays for the download and request fees.
        
        :returns: None
        """
        pass

    def reload(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_request_payment.load()
        :returns: None
        """
        pass


class BucketTagging(base.ServiceResource):
    tag_set: List
    bucket_name: str

    def delete(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketTagging>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_tagging.delete()
          
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_tagging.load()
        :returns: None
        """
        pass

    def put(self, Tagging: Dict) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketTagging>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_tagging.put(
              Tagging={
                  \'TagSet\': [
                      {
                          \'Key\': \'string\',
                          \'Value\': \'string\'
                      },
                  ]
              }
          )
        :type Tagging: dict
        :param Tagging: **[REQUIRED]** 
        
          - **TagSet** *(list) --* **[REQUIRED]** 
        
            - *(dict) --* 
        
              - **Key** *(string) --* **[REQUIRED]** 
        
                Name of the tag.
        
              - **Value** *(string) --* **[REQUIRED]** 
        
                Value of the tag.
        
        :returns: None
        """
        pass

    def reload(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_tagging.load()
        :returns: None
        """
        pass


class BucketVersioning(base.ServiceResource):
    status: str
    mfa_delete: str
    bucket_name: str

    def enable(self, MFA: str = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketVersioning>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_versioning.enable(
              MFA=\'string\',
              
          )
        :type MFA: string
        :param MFA: 
        
          The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device.
        
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_versioning.load()
        :returns: None
        """
        pass

    def put(self, VersioningConfiguration: Dict, MFA: str = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketVersioning>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_versioning.put(
              MFA=\'string\',
              VersioningConfiguration={
                  \'MFADelete\': \'Enabled\'|\'Disabled\',
                  \'Status\': \'Enabled\'|\'Suspended\'
              }
          )
        :type MFA: string
        :param MFA: 
        
          The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device.
        
        :type VersioningConfiguration: dict
        :param VersioningConfiguration: **[REQUIRED]** 
        
          - **MFADelete** *(string) --* 
        
            Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned.
        
          - **Status** *(string) --* 
        
            The versioning state of the bucket.
        
        :returns: None
        """
        pass

    def reload(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_versioning.load()
        :returns: None
        """
        pass

    def suspend(self, MFA: str = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketVersioning>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_versioning.suspend(
              MFA=\'string\',
              
          )
        :type MFA: string
        :param MFA: 
        
          The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device.
        
        :returns: None
        """
        pass


class BucketWebsite(base.ServiceResource):
    redirect_all_requests_to: Dict
    index_document: Dict
    error_document: Dict
    routing_rules: List
    bucket_name: str

    def delete(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketWebsite>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_website.delete()
          
        :returns: None
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_website.load()
        :returns: None
        """
        pass

    def put(self, WebsiteConfiguration: Dict) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketWebsite>`_
        
        **Request Syntax** 
        ::
        
          response = bucket_website.put(
              WebsiteConfiguration={
                  \'ErrorDocument\': {
                      \'Key\': \'string\'
                  },
                  \'IndexDocument\': {
                      \'Suffix\': \'string\'
                  },
                  \'RedirectAllRequestsTo\': {
                      \'HostName\': \'string\',
                      \'Protocol\': \'http\'|\'https\'
                  },
                  \'RoutingRules\': [
                      {
                          \'Condition\': {
                              \'HttpErrorCodeReturnedEquals\': \'string\',
                              \'KeyPrefixEquals\': \'string\'
                          },
                          \'Redirect\': {
                              \'HostName\': \'string\',
                              \'HttpRedirectCode\': \'string\',
                              \'Protocol\': \'http\'|\'https\',
                              \'ReplaceKeyPrefixWith\': \'string\',
                              \'ReplaceKeyWith\': \'string\'
                          }
                      },
                  ]
              }
          )
        :type WebsiteConfiguration: dict
        :param WebsiteConfiguration: **[REQUIRED]** 
        
          - **ErrorDocument** *(dict) --* 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The object key name to use when a 4XX class error occurs.
        
          - **IndexDocument** *(dict) --* 
        
            - **Suffix** *(string) --* **[REQUIRED]** 
        
              A suffix that is appended to a request that is for a directory on the website endpoint (e.g. if the suffix is index.html and you make a request to samplebucket/images/ the data that is returned will be for the object with the key name images/index.html) The suffix must not be empty and must not include a slash character.
        
          - **RedirectAllRequestsTo** *(dict) --* 
        
            - **HostName** *(string) --* **[REQUIRED]** 
        
              Name of the host where requests will be redirected.
        
            - **Protocol** *(string) --* 
        
              Protocol to use (http, https) when redirecting requests. The default is the protocol that is used in the original request.
        
          - **RoutingRules** *(list) --* 
        
            - *(dict) --* 
        
              - **Condition** *(dict) --* 
        
                A container for describing a condition that must be met for the specified redirect to apply. For example, 1. If request is for pages in the /docs folder, redirect to the /documents folder. 2. If request results in HTTP error 4xx, redirect request to another host where you might process the error.
        
                - **HttpErrorCodeReturnedEquals** *(string) --* 
        
                  The HTTP error code when the redirect is applied. In the event of an error, if the error code equals this value, then the specified redirect is applied. Required when parent element Condition is specified and sibling KeyPrefixEquals is not specified. If both are specified, then both must be true for the redirect to be applied.
        
                - **KeyPrefixEquals** *(string) --* 
        
                  The object key name prefix when the redirect is applied. For example, to redirect requests for ExamplePage.html, the key prefix will be ExamplePage.html. To redirect request for all pages with the prefix docs/, the key prefix will be /docs, which identifies all objects in the docs/ folder. Required when the parent element Condition is specified and sibling HttpErrorCodeReturnedEquals is not specified. If both conditions are specified, both must be true for the redirect to be applied.
        
              - **Redirect** *(dict) --* **[REQUIRED]** 
        
                Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can can specify a different error code to return.
        
                - **HostName** *(string) --* 
        
                  The host name to use in the redirect request.
        
                - **HttpRedirectCode** *(string) --* 
        
                  The HTTP redirect code to use on the response. Not required if one of the siblings is present.
        
                - **Protocol** *(string) --* 
        
                  Protocol to use (http, https) when redirecting requests. The default is the protocol that is used in the original request.
        
                - **ReplaceKeyPrefixWith** *(string) --* 
        
                  The object key prefix to use in the redirect request. For example, to redirect requests for all pages with prefix docs/ (objects in the docs/ folder) to documents/, you can set a condition block with KeyPrefixEquals set to docs/ and in the Redirect set ReplaceKeyPrefixWith to /documents. Not required if one of the siblings is present. Can be present only if ReplaceKeyWith is not provided.
        
                - **ReplaceKeyWith** *(string) --* 
        
                  The specific object key to use in the redirect request. For example, redirect request to error.html. Not required if one of the sibling is present. Can be present only if ReplaceKeyPrefixWith is not provided.
        
        :returns: None
        """
        pass

    def reload(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_website.load()
        :returns: None
        """
        pass


class MultipartUpload(base.ServiceResource):
    upload_id: str
    key: str
    initiated: datetime
    storage_class: str
    owner: Dict
    initiator: Dict
    bucket_name: str
    object_key: str
    id: str
    parts: 'parts'

    def abort(self, RequestPayer: str = None) -> Dict:
        """
        
        To verify that all parts have been removed, so you don\'t get charged for the part storage, you should call the List Parts operation and ensure the parts list is empty.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/AbortMultipartUpload>`_
        
        **Request Syntax** 
        ::
        
          response = multipart_upload.abort(
              RequestPayer=\'requester\'
          )
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RequestCharged\': \'requester\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
        """
        pass

    def complete(self, MultipartUpload: Dict = None, RequestPayer: str = None) -> 'Object':
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CompleteMultipartUpload>`_
        
        **Request Syntax** 
        ::
        
          object = multipart_upload.complete(
              MultipartUpload={
                  \'Parts\': [
                      {
                          \'ETag\': \'string\',
                          \'PartNumber\': 123
                      },
                  ]
              },
              RequestPayer=\'requester\'
          )
        :type MultipartUpload: dict
        :param MultipartUpload: 
        
          - **Parts** *(list) --* 
        
            - *(dict) --* 
        
              - **ETag** *(string) --* 
        
                Entity tag returned when the part was uploaded.
        
              - **PartNumber** *(integer) --* 
        
                Part number that identifies the part. This is a positive integer between 1 and 10,000.
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :rtype: :py:class:`s3.Object`
        :returns: Object resource
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass


class MultipartUploadPart(base.ServiceResource):
    last_modified: datetime
    e_tag: str
    size: int
    bucket_name: str
    object_key: str
    multipart_upload_id: str
    part_number: str

    def copy_from(self, CopySource: Union[str, Dict], CopySourceIfMatch: str = None, CopySourceIfModifiedSince: datetime = None, CopySourceIfNoneMatch: str = None, CopySourceIfUnmodifiedSince: datetime = None, CopySourceRange: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, CopySourceSSECustomerAlgorithm: str = None, CopySourceSSECustomerKey: str = None, CopySourceSSECustomerKeyMD5: str = None, RequestPayer: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/UploadPartCopy>`_
        
        **Request Syntax** 
        ::
        
          response = multipart_upload_part.copy_from(
              CopySource=\'string\' or {\'Bucket\': \'string\', \'Key\': \'string\', \'VersionId\': \'string\'},
              CopySourceIfMatch=\'string\',
              CopySourceIfModifiedSince=datetime(2015, 1, 1),
              CopySourceIfNoneMatch=\'string\',
              CopySourceIfUnmodifiedSince=datetime(2015, 1, 1),
              CopySourceRange=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              CopySourceSSECustomerAlgorithm=\'string\',
              CopySourceSSECustomerKey=\'string\',
              RequestPayer=\'requester\'
          )
        :type CopySource: str or dict
        :param CopySource: **[REQUIRED]** The name of the source bucket, key name of the source object, and optional version ID of the source object.  You can either provide this value as a string or a dictionary.  The string form is {bucket}/{key} or {bucket}/{key}?versionId={versionId} if you want to copy a specific version.  You can also provide this value as a dictionary.  The dictionary format is recommended over the string format because it is more explicit.  The dictionary format is: {\'Bucket\': \'bucket\', \'Key\': \'key\', \'VersionId\': \'id\'}.  Note that the VersionId key is optional and may be omitted.
        
        :type CopySourceIfMatch: string
        :param CopySourceIfMatch: 
        
          Copies the object if its entity tag (ETag) matches the specified tag.
        
        :type CopySourceIfModifiedSince: datetime
        :param CopySourceIfModifiedSince: 
        
          Copies the object if it has been modified since the specified time.
        
        :type CopySourceIfNoneMatch: string
        :param CopySourceIfNoneMatch: 
        
          Copies the object if its entity tag (ETag) is different than the specified ETag.
        
        :type CopySourceIfUnmodifiedSince: datetime
        :param CopySourceIfUnmodifiedSince: 
        
          Copies the object if it hasn\'t been modified since the specified time.
        
        :type CopySourceRange: string
        :param CopySourceRange: 
        
          The range of bytes to copy from the source object. The range value must use the form bytes=first-last, where the first and last are the zero-based byte offsets to copy. For example, bytes=0-9 indicates that you want to copy the first ten bytes of the source. You can copy a range only if the source object is greater than 5 GB.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header. This must be the same encryption key specified in the initiate multipart upload request.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type CopySourceSSECustomerAlgorithm: string
        :param CopySourceSSECustomerAlgorithm: 
        
          Specifies the algorithm to use when decrypting the source object (e.g., AES256).
        
        :type CopySourceSSECustomerKey: string
        :param CopySourceSSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.
        
        :type CopySourceSSECustomerKeyMD5: string
        :param CopySourceSSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CopySourceVersionId\': \'string\',
                \'CopyPartResult\': {
                    \'ETag\': \'string\',
                    \'LastModified\': datetime(2015, 1, 1)
                },
                \'ServerSideEncryption\': \'AES256\'|\'aws:kms\',
                \'SSECustomerAlgorithm\': \'string\',
                \'SSECustomerKeyMD5\': \'string\',
                \'SSEKMSKeyId\': \'string\',
                \'RequestCharged\': \'requester\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CopySourceVersionId** *(string) --* 
        
              The version of the source object that was copied, if you have enabled versioning on the source bucket.
        
            - **CopyPartResult** *(dict) --* 
              
              - **ETag** *(string) --* 
        
                Entity tag of the object.
        
              - **LastModified** *(datetime) --* 
        
                Date and time at which the object was uploaded.
        
            - **ServerSideEncryption** *(string) --* 
        
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
            - **SSECustomerAlgorithm** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
        
            - **SSECustomerKeyMD5** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
        
            - **SSEKMSKeyId** *(string) --* 
        
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
        
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def upload(self, Body: Union[bytes, IO] = None, ContentLength: int = None, ContentMD5: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None) -> Dict:
        """
        
         **Note:** After you initiate multipart upload and upload one or more parts, you must either complete or abort multipart upload in order to stop getting charged for storage of the uploaded parts. Only after you either complete or abort multipart upload, Amazon S3 frees up the parts storage and stops charging you for the parts storage.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/UploadPart>`_
        
        **Request Syntax** 
        ::
        
          response = multipart_upload_part.upload(
              Body=b\'bytes\'|file,
              ContentLength=123,
              ContentMD5=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              RequestPayer=\'requester\'
          )
        :type Body: bytes or seekable file-like object
        :param Body: 
        
          Object data.
        
        :type ContentLength: integer
        :param ContentLength: 
        
          Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically.
        
        :type ContentMD5: string
        :param ContentMD5: 
        
          The base64-encoded 128-bit MD5 digest of the part data.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header. This must be the same encryption key specified in the initiate multipart upload request.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ServerSideEncryption\': \'AES256\'|\'aws:kms\',
                \'ETag\': \'string\',
                \'SSECustomerAlgorithm\': \'string\',
                \'SSECustomerKeyMD5\': \'string\',
                \'SSEKMSKeyId\': \'string\',
                \'RequestCharged\': \'requester\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ServerSideEncryption** *(string) --* 
        
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
            - **ETag** *(string) --* 
        
              Entity tag for the uploaded object.
        
            - **SSECustomerAlgorithm** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
        
            - **SSECustomerKeyMD5** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
        
            - **SSEKMSKeyId** *(string) --* 
        
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
        
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
        """
        pass


class Object(base.ServiceResource):
    delete_marker: bool
    accept_ranges: str
    expiration: str
    restore: str
    last_modified: datetime
    content_length: int
    e_tag: str
    missing_meta: int
    version_id: str
    cache_control: str
    content_disposition: str
    content_encoding: str
    content_language: str
    content_type: str
    expires: datetime
    website_redirect_location: str
    server_side_encryption: str
    metadata: Dict
    sse_customer_algorithm: str
    sse_customer_key_md5: str
    ssekms_key_id: str
    storage_class: str
    request_charged: str
    replication_status: str
    parts_count: int
    bucket_name: str
    key: str

    def copy(self, CopySource: Dict = None, ExtraArgs: Dict = None, Callback: Callable = None, SourceClient: BaseClient = None, Config: TransferConfig = None) -> NoReturn:
        """
        
        This is a managed transfer which will perform a multipart copy in
        multiple threads if necessary.
        
        Usage::
        
            import boto3
            s3 = boto3.resource(\'s3\')
            copy_source = {
                \'Bucket\': \'mybucket\',
                \'Key\': \'mykey\'
            }
            bucket = s3.Bucket(\'otherbucket\')
            obj = bucket.Object(\'otherkey\')
            obj.copy(copy_source)
        
        :type CopySource: dict
        :param CopySource: The name of the source bucket, key name of the
            source object, and optional version ID of the source object. The
            dictionary format is:
            ``{\'Bucket\': \'bucket\', \'Key\': \'key\', \'VersionId\': \'id\'}``. Note
            that the ``VersionId`` key is optional and may be omitted.
        
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation
        
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the copy.
        
        :type SourceClient: botocore or boto3 Client
        :param SourceClient: The client to be used for operation that
            may happen at the source object. For example, this client is
            used for the head_object that determines the size of the copy.
            If no client is provided, the current client is used as the client
            for the source object.
        
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            copy.
        """
        pass

    def copy_from(self, CopySource: Union[str, Dict], ACL: str = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentType: str = None, CopySourceIfMatch: str = None, CopySourceIfModifiedSince: datetime = None, CopySourceIfNoneMatch: str = None, CopySourceIfUnmodifiedSince: datetime = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, MetadataDirective: str = None, TaggingDirective: str = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, CopySourceSSECustomerAlgorithm: str = None, CopySourceSSECustomerKey: str = None, CopySourceSSECustomerKeyMD5: str = None, RequestPayer: str = None, Tagging: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CopyObject>`_
        
        **Request Syntax** 
        ::
        
          response = object.copy_from(
              ACL=\'private\'|\'public-read\'|\'public-read-write\'|\'authenticated-read\'|\'aws-exec-read\'|\'bucket-owner-read\'|\'bucket-owner-full-control\',
              CacheControl=\'string\',
              ContentDisposition=\'string\',
              ContentEncoding=\'string\',
              ContentLanguage=\'string\',
              ContentType=\'string\',
              CopySource=\'string\' or {\'Bucket\': \'string\', \'Key\': \'string\', \'VersionId\': \'string\'},
              CopySourceIfMatch=\'string\',
              CopySourceIfModifiedSince=datetime(2015, 1, 1),
              CopySourceIfNoneMatch=\'string\',
              CopySourceIfUnmodifiedSince=datetime(2015, 1, 1),
              Expires=datetime(2015, 1, 1),
              GrantFullControl=\'string\',
              GrantRead=\'string\',
              GrantReadACP=\'string\',
              GrantWriteACP=\'string\',
              Metadata={
                  \'string\': \'string\'
              },
              MetadataDirective=\'COPY\'|\'REPLACE\',
              TaggingDirective=\'COPY\'|\'REPLACE\',
              ServerSideEncryption=\'AES256\'|\'aws:kms\',
              StorageClass=\'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
              WebsiteRedirectLocation=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              SSEKMSKeyId=\'string\',
              CopySourceSSECustomerAlgorithm=\'string\',
              CopySourceSSECustomerKey=\'string\',
              RequestPayer=\'requester\',
              Tagging=\'string\'
          )
        :type ACL: string
        :param ACL: 
        
          The canned ACL to apply to the object.
        
        :type CacheControl: string
        :param CacheControl: 
        
          Specifies caching behavior along the request/reply chain.
        
        :type ContentDisposition: string
        :param ContentDisposition: 
        
          Specifies presentational information for the object.
        
        :type ContentEncoding: string
        :param ContentEncoding: 
        
          Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        
        :type ContentLanguage: string
        :param ContentLanguage: 
        
          The language the content is in.
        
        :type ContentType: string
        :param ContentType: 
        
          A standard MIME type describing the format of the object data.
        
        :type CopySource: str or dict
        :param CopySource: **[REQUIRED]** The name of the source bucket, key name of the source object, and optional version ID of the source object.  You can either provide this value as a string or a dictionary.  The string form is {bucket}/{key} or {bucket}/{key}?versionId={versionId} if you want to copy a specific version.  You can also provide this value as a dictionary.  The dictionary format is recommended over the string format because it is more explicit.  The dictionary format is: {\'Bucket\': \'bucket\', \'Key\': \'key\', \'VersionId\': \'id\'}.  Note that the VersionId key is optional and may be omitted.
        
        :type CopySourceIfMatch: string
        :param CopySourceIfMatch: 
        
          Copies the object if its entity tag (ETag) matches the specified tag.
        
        :type CopySourceIfModifiedSince: datetime
        :param CopySourceIfModifiedSince: 
        
          Copies the object if it has been modified since the specified time.
        
        :type CopySourceIfNoneMatch: string
        :param CopySourceIfNoneMatch: 
        
          Copies the object if its entity tag (ETag) is different than the specified ETag.
        
        :type CopySourceIfUnmodifiedSince: datetime
        :param CopySourceIfUnmodifiedSince: 
        
          Copies the object if it hasn\'t been modified since the specified time.
        
        :type Expires: datetime
        :param Expires: 
        
          The date and time at which the object is no longer cacheable.
        
        :type GrantFullControl: string
        :param GrantFullControl: 
        
          Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
        
        :type GrantRead: string
        :param GrantRead: 
        
          Allows grantee to read the object data and its metadata.
        
        :type GrantReadACP: string
        :param GrantReadACP: 
        
          Allows grantee to read the object ACL.
        
        :type GrantWriteACP: string
        :param GrantWriteACP: 
        
          Allows grantee to write the ACL for the applicable object.
        
        :type Metadata: dict
        :param Metadata: 
        
          A map of metadata to store with the object in S3.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type MetadataDirective: string
        :param MetadataDirective: 
        
          Specifies whether the metadata is copied from the source object or replaced with metadata provided in the request.
        
        :type TaggingDirective: string
        :param TaggingDirective: 
        
          Specifies whether the object tag-set are copied from the source object or replaced with tag-set provided in the request.
        
        :type ServerSideEncryption: string
        :param ServerSideEncryption: 
        
          The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
        :type StorageClass: string
        :param StorageClass: 
        
          The type of storage to use for the object. Defaults to \'STANDARD\'.
        
        :type WebsiteRedirectLocation: string
        :param WebsiteRedirectLocation: 
        
          If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type SSEKMSKeyId: string
        :param SSEKMSKeyId: 
        
          Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version
        
        :type CopySourceSSECustomerAlgorithm: string
        :param CopySourceSSECustomerAlgorithm: 
        
          Specifies the algorithm to use when decrypting the source object (e.g., AES256).
        
        :type CopySourceSSECustomerKey: string
        :param CopySourceSSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.
        
        :type CopySourceSSECustomerKeyMD5: string
        :param CopySourceSSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type Tagging: string
        :param Tagging: 
        
          The tag-set for the object destination object this value must be used in conjunction with the TaggingDirective. The tag-set must be encoded as URL Query parameters
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CopyObjectResult\': {
                    \'ETag\': \'string\',
                    \'LastModified\': datetime(2015, 1, 1)
                },
                \'Expiration\': \'string\',
                \'CopySourceVersionId\': \'string\',
                \'VersionId\': \'string\',
                \'ServerSideEncryption\': \'AES256\'|\'aws:kms\',
                \'SSECustomerAlgorithm\': \'string\',
                \'SSECustomerKeyMD5\': \'string\',
                \'SSEKMSKeyId\': \'string\',
                \'RequestCharged\': \'requester\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CopyObjectResult** *(dict) --* 
              
              - **ETag** *(string) --* 
              
              - **LastModified** *(datetime) --* 
          
            - **Expiration** *(string) --* 
        
              If the object expiration is configured, the response includes this header.
        
            - **CopySourceVersionId** *(string) --* 
            
            - **VersionId** *(string) --* 
        
              Version ID of the newly created copy.
        
            - **ServerSideEncryption** *(string) --* 
        
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
            - **SSECustomerAlgorithm** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
        
            - **SSECustomerKeyMD5** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
        
            - **SSEKMSKeyId** *(string) --* 
        
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
        
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
        """
        pass

    def delete(self, MFA: str = None, VersionId: str = None, RequestPayer: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteObject>`_
        
        **Request Syntax** 
        ::
        
          response = object.delete(
              MFA=\'string\',
              VersionId=\'string\',
              RequestPayer=\'requester\'
          )
        :type MFA: string
        :param MFA: 
        
          The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device.
        
        :type VersionId: string
        :param VersionId: 
        
          VersionId used to reference a specific version of the object.
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeleteMarker\': True|False,
                \'VersionId\': \'string\',
                \'RequestCharged\': \'requester\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DeleteMarker** *(boolean) --* 
        
              Specifies whether the versioned object that was permanently deleted was (true) or was not (false) a delete marker.
        
            - **VersionId** *(string) --* 
        
              Returns the version ID of the delete marker created as a result of the DELETE operation.
        
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
        """
        pass

    def download_file(self, Filename: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None) -> NoReturn:
        """
        
        Usage::
        
            import boto3
            s3 = boto3.resource(\'s3\')
            s3.Object(\'mybucket\', \'hello.txt\').download_file(\'/tmp/hello.txt\')
        
        Similar behavior as S3Transfer\'s download_file() method,
        except that parameters are capitalized. Detailed examples can be found at
        :ref:`S3Transfer\'s Usage <ref_s3transfer_usage>`.
        
        :type Filename: str
        :param Filename: The path to the file to download to.
        
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.
        
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the download.
        
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            transfer.
        """
        pass

    def download_fileobj(self, Fileobj: IO = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None) -> NoReturn:
        """
        
        The file-like object must be in binary mode.
        
        This is a managed transfer which will perform a multipart download in
        multiple threads if necessary.
        
        Usage::
        
            import boto3
            s3 = boto3.resource(\'s3\')
            bucket = s3.Bucket(\'mybucket\')
            obj = bucket.Object(\'mykey\')
        
            with open(\'filename\', \'wb\') as data:
                obj.download_fileobj(data)
        
        :type Fileobj: a file-like object
        :param Fileobj: A file-like object to download into. At a minimum, it must
            implement the `write` method and must accept bytes.
        
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.
        
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the download.
        
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            download.
        """
        pass

    def get(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, ResponseCacheControl: str = None, ResponseContentDisposition: str = None, ResponseContentEncoding: str = None, ResponseContentLanguage: str = None, ResponseContentType: str = None, ResponseExpires: datetime = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObject>`_
        
        **Request Syntax** 
        ::
        
          response = object.get(
              IfMatch=\'string\',
              IfModifiedSince=datetime(2015, 1, 1),
              IfNoneMatch=\'string\',
              IfUnmodifiedSince=datetime(2015, 1, 1),
              Range=\'string\',
              ResponseCacheControl=\'string\',
              ResponseContentDisposition=\'string\',
              ResponseContentEncoding=\'string\',
              ResponseContentLanguage=\'string\',
              ResponseContentType=\'string\',
              ResponseExpires=datetime(2015, 1, 1),
              VersionId=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              RequestPayer=\'requester\',
              PartNumber=123
          )
        :type IfMatch: string
        :param IfMatch: 
        
          Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).
        
        :type IfModifiedSince: datetime
        :param IfModifiedSince: 
        
          Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).
        
        :type IfNoneMatch: string
        :param IfNoneMatch: 
        
          Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).
        
        :type IfUnmodifiedSince: datetime
        :param IfUnmodifiedSince: 
        
          Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).
        
        :type Range: string
        :param Range: 
        
          Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
        
        :type ResponseCacheControl: string
        :param ResponseCacheControl: 
        
          Sets the Cache-Control header of the response.
        
        :type ResponseContentDisposition: string
        :param ResponseContentDisposition: 
        
          Sets the Content-Disposition header of the response
        
        :type ResponseContentEncoding: string
        :param ResponseContentEncoding: 
        
          Sets the Content-Encoding header of the response.
        
        :type ResponseContentLanguage: string
        :param ResponseContentLanguage: 
        
          Sets the Content-Language header of the response.
        
        :type ResponseContentType: string
        :param ResponseContentType: 
        
          Sets the Content-Type header of the response.
        
        :type ResponseExpires: datetime
        :param ResponseExpires: 
        
          Sets the Expires header of the response.
        
        :type VersionId: string
        :param VersionId: 
        
          VersionId used to reference a specific version of the object.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type PartNumber: integer
        :param PartNumber: 
        
          Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a \'ranged\' GET request for the part specified. Useful for downloading just a part of an object.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Body\': StreamingBody(),
                \'DeleteMarker\': True|False,
                \'AcceptRanges\': \'string\',
                \'Expiration\': \'string\',
                \'Restore\': \'string\',
                \'LastModified\': datetime(2015, 1, 1),
                \'ContentLength\': 123,
                \'ETag\': \'string\',
                \'MissingMeta\': 123,
                \'VersionId\': \'string\',
                \'CacheControl\': \'string\',
                \'ContentDisposition\': \'string\',
                \'ContentEncoding\': \'string\',
                \'ContentLanguage\': \'string\',
                \'ContentRange\': \'string\',
                \'ContentType\': \'string\',
                \'Expires\': datetime(2015, 1, 1),
                \'WebsiteRedirectLocation\': \'string\',
                \'ServerSideEncryption\': \'AES256\'|\'aws:kms\',
                \'Metadata\': {
                    \'string\': \'string\'
                },
                \'SSECustomerAlgorithm\': \'string\',
                \'SSECustomerKeyMD5\': \'string\',
                \'SSEKMSKeyId\': \'string\',
                \'StorageClass\': \'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
                \'RequestCharged\': \'requester\',
                \'ReplicationStatus\': \'COMPLETE\'|\'PENDING\'|\'FAILED\'|\'REPLICA\',
                \'PartsCount\': 123,
                \'TagCount\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Body** (:class:`.StreamingBody`) -- 
        
              Object data.
        
            - **DeleteMarker** *(boolean) --* 
        
              Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If false, this response header does not appear in the response.
        
            - **AcceptRanges** *(string) --* 
            
            - **Expiration** *(string) --* 
        
              If the object expiration is configured (see PUT Bucket lifecycle), the response includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.
        
            - **Restore** *(string) --* 
        
              Provides information about object restoration operation and expiration time of the restored object copy.
        
            - **LastModified** *(datetime) --* 
        
              Last modified date of the object
        
            - **ContentLength** *(integer) --* 
        
              Size of the body in bytes.
        
            - **ETag** *(string) --* 
        
              An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL
        
            - **MissingMeta** *(integer) --* 
        
              This is set to the number of metadata entries not returned in x-amz-meta headers. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.
        
            - **VersionId** *(string) --* 
        
              Version of the object.
        
            - **CacheControl** *(string) --* 
        
              Specifies caching behavior along the request/reply chain.
        
            - **ContentDisposition** *(string) --* 
        
              Specifies presentational information for the object.
        
            - **ContentEncoding** *(string) --* 
        
              Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        
            - **ContentLanguage** *(string) --* 
        
              The language the content is in.
        
            - **ContentRange** *(string) --* 
        
              The portion of the object returned in the response.
        
            - **ContentType** *(string) --* 
        
              A standard MIME type describing the format of the object data.
        
            - **Expires** *(datetime) --* 
        
              The date and time at which the object is no longer cacheable.
        
            - **WebsiteRedirectLocation** *(string) --* 
        
              If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        
            - **ServerSideEncryption** *(string) --* 
        
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
            - **Metadata** *(dict) --* 
        
              A map of metadata to store with the object in S3.
        
              - *(string) --* 
                
                - *(string) --* 
          
            - **SSECustomerAlgorithm** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
        
            - **SSECustomerKeyMD5** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
        
            - **SSEKMSKeyId** *(string) --* 
        
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
        
            - **StorageClass** *(string) --* 
            
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
            - **ReplicationStatus** *(string) --* 
            
            - **PartsCount** *(integer) --* 
        
              The count of parts this object has.
        
            - **TagCount** *(integer) --* 
        
              The number of tags, if any, on the object.
        
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def initiate_multipart_upload(self, ACL: str = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentType: str = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, RequestPayer: str = None, Tagging: str = None) -> 'MultipartUpload':
        """
        
         **Note:** After you initiate multipart upload and upload one or more parts, you must either complete or abort multipart upload in order to stop getting charged for storage of the uploaded parts. Only after you either complete or abort multipart upload, Amazon S3 frees up the parts storage and stops charging you for the parts storage.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CreateMultipartUpload>`_
        
        **Request Syntax** 
        ::
        
          multipart_upload = object.initiate_multipart_upload(
              ACL=\'private\'|\'public-read\'|\'public-read-write\'|\'authenticated-read\'|\'aws-exec-read\'|\'bucket-owner-read\'|\'bucket-owner-full-control\',
              CacheControl=\'string\',
              ContentDisposition=\'string\',
              ContentEncoding=\'string\',
              ContentLanguage=\'string\',
              ContentType=\'string\',
              Expires=datetime(2015, 1, 1),
              GrantFullControl=\'string\',
              GrantRead=\'string\',
              GrantReadACP=\'string\',
              GrantWriteACP=\'string\',
              Metadata={
                  \'string\': \'string\'
              },
              ServerSideEncryption=\'AES256\'|\'aws:kms\',
              StorageClass=\'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
              WebsiteRedirectLocation=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              SSEKMSKeyId=\'string\',
              RequestPayer=\'requester\',
              Tagging=\'string\'
          )
        :type ACL: string
        :param ACL: 
        
          The canned ACL to apply to the object.
        
        :type CacheControl: string
        :param CacheControl: 
        
          Specifies caching behavior along the request/reply chain.
        
        :type ContentDisposition: string
        :param ContentDisposition: 
        
          Specifies presentational information for the object.
        
        :type ContentEncoding: string
        :param ContentEncoding: 
        
          Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        
        :type ContentLanguage: string
        :param ContentLanguage: 
        
          The language the content is in.
        
        :type ContentType: string
        :param ContentType: 
        
          A standard MIME type describing the format of the object data.
        
        :type Expires: datetime
        :param Expires: 
        
          The date and time at which the object is no longer cacheable.
        
        :type GrantFullControl: string
        :param GrantFullControl: 
        
          Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
        
        :type GrantRead: string
        :param GrantRead: 
        
          Allows grantee to read the object data and its metadata.
        
        :type GrantReadACP: string
        :param GrantReadACP: 
        
          Allows grantee to read the object ACL.
        
        :type GrantWriteACP: string
        :param GrantWriteACP: 
        
          Allows grantee to write the ACL for the applicable object.
        
        :type Metadata: dict
        :param Metadata: 
        
          A map of metadata to store with the object in S3.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type ServerSideEncryption: string
        :param ServerSideEncryption: 
        
          The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
        :type StorageClass: string
        :param StorageClass: 
        
          The type of storage to use for the object. Defaults to \'STANDARD\'.
        
        :type WebsiteRedirectLocation: string
        :param WebsiteRedirectLocation: 
        
          If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type SSEKMSKeyId: string
        :param SSEKMSKeyId: 
        
          Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type Tagging: string
        :param Tagging: 
        
          The tag-set for the object. The tag-set must be encoded as URL Query parameters
        
        :rtype: :py:class:`s3.MultipartUpload`
        :returns: MultipartUpload resource
        """
        pass

    def load(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          object.load()
        :returns: None
        """
        pass

    def put(self, ACL: str = None, Body: Union[bytes, IO] = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentLength: int = None, ContentMD5: str = None, ContentType: str = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, RequestPayer: str = None, Tagging: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObject>`_
        
        **Request Syntax** 
        ::
        
          response = object.put(
              ACL=\'private\'|\'public-read\'|\'public-read-write\'|\'authenticated-read\'|\'aws-exec-read\'|\'bucket-owner-read\'|\'bucket-owner-full-control\',
              Body=b\'bytes\'|file,
              CacheControl=\'string\',
              ContentDisposition=\'string\',
              ContentEncoding=\'string\',
              ContentLanguage=\'string\',
              ContentLength=123,
              ContentMD5=\'string\',
              ContentType=\'string\',
              Expires=datetime(2015, 1, 1),
              GrantFullControl=\'string\',
              GrantRead=\'string\',
              GrantReadACP=\'string\',
              GrantWriteACP=\'string\',
              Metadata={
                  \'string\': \'string\'
              },
              ServerSideEncryption=\'AES256\'|\'aws:kms\',
              StorageClass=\'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
              WebsiteRedirectLocation=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              SSEKMSKeyId=\'string\',
              RequestPayer=\'requester\',
              Tagging=\'string\'
          )
        :type ACL: string
        :param ACL: 
        
          The canned ACL to apply to the object.
        
        :type Body: bytes or seekable file-like object
        :param Body: 
        
          Object data.
        
        :type CacheControl: string
        :param CacheControl: 
        
          Specifies caching behavior along the request/reply chain.
        
        :type ContentDisposition: string
        :param ContentDisposition: 
        
          Specifies presentational information for the object.
        
        :type ContentEncoding: string
        :param ContentEncoding: 
        
          Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        
        :type ContentLanguage: string
        :param ContentLanguage: 
        
          The language the content is in.
        
        :type ContentLength: integer
        :param ContentLength: 
        
          Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically.
        
        :type ContentMD5: string
        :param ContentMD5: 
        
          The base64-encoded 128-bit MD5 digest of the part data.
        
        :type ContentType: string
        :param ContentType: 
        
          A standard MIME type describing the format of the object data.
        
        :type Expires: datetime
        :param Expires: 
        
          The date and time at which the object is no longer cacheable.
        
        :type GrantFullControl: string
        :param GrantFullControl: 
        
          Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
        
        :type GrantRead: string
        :param GrantRead: 
        
          Allows grantee to read the object data and its metadata.
        
        :type GrantReadACP: string
        :param GrantReadACP: 
        
          Allows grantee to read the object ACL.
        
        :type GrantWriteACP: string
        :param GrantWriteACP: 
        
          Allows grantee to write the ACL for the applicable object.
        
        :type Metadata: dict
        :param Metadata: 
        
          A map of metadata to store with the object in S3.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type ServerSideEncryption: string
        :param ServerSideEncryption: 
        
          The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
        :type StorageClass: string
        :param StorageClass: 
        
          The type of storage to use for the object. Defaults to \'STANDARD\'.
        
        :type WebsiteRedirectLocation: string
        :param WebsiteRedirectLocation: 
        
          If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type SSEKMSKeyId: string
        :param SSEKMSKeyId: 
        
          Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type Tagging: string
        :param Tagging: 
        
          The tag-set for the object. The tag-set must be encoded as URL Query parameters
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Expiration\': \'string\',
                \'ETag\': \'string\',
                \'ServerSideEncryption\': \'AES256\'|\'aws:kms\',
                \'VersionId\': \'string\',
                \'SSECustomerAlgorithm\': \'string\',
                \'SSECustomerKeyMD5\': \'string\',
                \'SSEKMSKeyId\': \'string\',
                \'RequestCharged\': \'requester\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Expiration** *(string) --* 
        
              If the object expiration is configured, this will contain the expiration date (expiry-date) and rule ID (rule-id). The value of rule-id is URL encoded.
        
            - **ETag** *(string) --* 
        
              Entity tag for the uploaded object.
        
            - **ServerSideEncryption** *(string) --* 
        
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
            - **VersionId** *(string) --* 
        
              Version of the object.
        
            - **SSECustomerAlgorithm** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
        
            - **SSECustomerKeyMD5** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
        
            - **SSEKMSKeyId** *(string) --* 
        
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
        
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
        """
        pass

    def reload(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          object.load()
        :returns: None
        """
        pass

    def restore_object(self, VersionId: str = None, RestoreRequest: Dict = None, RequestPayer: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/RestoreObject>`_
        
        **Request Syntax** 
        ::
        
          response = object.restore_object(
              VersionId=\'string\',
              RestoreRequest={
                  \'Days\': 123,
                  \'GlacierJobParameters\': {
                      \'Tier\': \'Standard\'|\'Bulk\'|\'Expedited\'
                  },
                  \'Type\': \'SELECT\',
                  \'Tier\': \'Standard\'|\'Bulk\'|\'Expedited\',
                  \'Description\': \'string\',
                  \'SelectParameters\': {
                      \'InputSerialization\': {
                          \'CSV\': {
                              \'FileHeaderInfo\': \'USE\'|\'IGNORE\'|\'NONE\',
                              \'Comments\': \'string\',
                              \'QuoteEscapeCharacter\': \'string\',
                              \'RecordDelimiter\': \'string\',
                              \'FieldDelimiter\': \'string\',
                              \'QuoteCharacter\': \'string\',
                              \'AllowQuotedRecordDelimiter\': True|False
                          },
                          \'CompressionType\': \'NONE\'|\'GZIP\'|\'BZIP2\',
                          \'JSON\': {
                              \'Type\': \'DOCUMENT\'|\'LINES\'
                          },
                          \'Parquet\': {}
                          
                      },
                      \'ExpressionType\': \'SQL\',
                      \'Expression\': \'string\',
                      \'OutputSerialization\': {
                          \'CSV\': {
                              \'QuoteFields\': \'ALWAYS\'|\'ASNEEDED\',
                              \'QuoteEscapeCharacter\': \'string\',
                              \'RecordDelimiter\': \'string\',
                              \'FieldDelimiter\': \'string\',
                              \'QuoteCharacter\': \'string\'
                          },
                          \'JSON\': {
                              \'RecordDelimiter\': \'string\'
                          }
                      }
                  },
                  \'OutputLocation\': {
                      \'S3\': {
                          \'BucketName\': \'string\',
                          \'Prefix\': \'string\',
                          \'Encryption\': {
                              \'EncryptionType\': \'AES256\'|\'aws:kms\',
                              \'KMSKeyId\': \'string\',
                              \'KMSContext\': \'string\'
                          },
                          \'CannedACL\': \'private\'|\'public-read\'|\'public-read-write\'|\'authenticated-read\'|\'aws-exec-read\'|\'bucket-owner-read\'|\'bucket-owner-full-control\',
                          \'AccessControlList\': [
                              {
                                  \'Grantee\': {
                                      \'DisplayName\': \'string\',
                                      \'EmailAddress\': \'string\',
                                      \'ID\': \'string\',
                                      \'Type\': \'CanonicalUser\'|\'AmazonCustomerByEmail\'|\'Group\',
                                      \'URI\': \'string\'
                                  },
                                  \'Permission\': \'FULL_CONTROL\'|\'WRITE\'|\'WRITE_ACP\'|\'READ\'|\'READ_ACP\'
                              },
                          ],
                          \'Tagging\': {
                              \'TagSet\': [
                                  {
                                      \'Key\': \'string\',
                                      \'Value\': \'string\'
                                  },
                              ]
                          },
                          \'UserMetadata\': [
                              {
                                  \'Name\': \'string\',
                                  \'Value\': \'string\'
                              },
                          ],
                          \'StorageClass\': \'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\'
                      }
                  }
              },
              RequestPayer=\'requester\'
          )
        :type VersionId: string
        :param VersionId: 
        
        :type RestoreRequest: dict
        :param RestoreRequest: 
        
          Container for restore job parameters.
        
          - **Days** *(integer) --* 
        
            Lifetime of the active copy in days. Do not use with restores that specify OutputLocation.
        
          - **GlacierJobParameters** *(dict) --* 
        
            Glacier related parameters pertaining to this job. Do not use with restores that specify OutputLocation.
        
            - **Tier** *(string) --* **[REQUIRED]** 
        
              Glacier retrieval tier at which the restore will be processed.
        
          - **Type** *(string) --* 
        
            Type of restore request.
        
          - **Tier** *(string) --* 
        
            Glacier retrieval tier at which the restore will be processed.
        
          - **Description** *(string) --* 
        
            The optional description for the job.
        
          - **SelectParameters** *(dict) --* 
        
            Describes the parameters for Select job types.
        
            - **InputSerialization** *(dict) --* **[REQUIRED]** 
        
              Describes the serialization format of the object.
        
              - **CSV** *(dict) --* 
        
                Describes the serialization of a CSV-encoded object.
        
                - **FileHeaderInfo** *(string) --* 
        
                  Describes the first line of input. Valid values: None, Ignore, Use.
        
                - **Comments** *(string) --* 
        
                  Single character used to indicate a row should be ignored when present at the start of a row.
        
                - **QuoteEscapeCharacter** *(string) --* 
        
                  Single character used for escaping the quote character inside an already escaped value.
        
                - **RecordDelimiter** *(string) --* 
        
                  Value used to separate individual records.
        
                - **FieldDelimiter** *(string) --* 
        
                  Value used to separate individual fields in a record.
        
                - **QuoteCharacter** *(string) --* 
        
                  Value used for escaping where the field delimiter is part of the value.
        
                - **AllowQuotedRecordDelimiter** *(boolean) --* 
        
                  Specifies that CSV field values may contain quoted record delimiters and such records should be allowed. Default value is FALSE. Setting this value to TRUE may lower performance.
        
              - **CompressionType** *(string) --* 
        
                Specifies object\'s compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE.
        
              - **JSON** *(dict) --* 
        
                Specifies JSON as object\'s input serialization format.
        
                - **Type** *(string) --* 
        
                  The type of JSON. Valid values: Document, Lines.
        
              - **Parquet** *(dict) --* 
        
                Specifies Parquet as object\'s input serialization format.
        
            - **ExpressionType** *(string) --* **[REQUIRED]** 
        
              The type of the provided expression (e.g., SQL).
        
            - **Expression** *(string) --* **[REQUIRED]** 
        
              The expression that is used to query the object.
        
            - **OutputSerialization** *(dict) --* **[REQUIRED]** 
        
              Describes how the results of the Select job are serialized.
        
              - **CSV** *(dict) --* 
        
                Describes the serialization of CSV-encoded Select results.
        
                - **QuoteFields** *(string) --* 
        
                  Indicates whether or not all output fields should be quoted.
        
                - **QuoteEscapeCharacter** *(string) --* 
        
                  Single character used for escaping the quote character inside an already escaped value.
        
                - **RecordDelimiter** *(string) --* 
        
                  Value used to separate individual records.
        
                - **FieldDelimiter** *(string) --* 
        
                  Value used to separate individual fields in a record.
        
                - **QuoteCharacter** *(string) --* 
        
                  Value used for escaping where the field delimiter is part of the value.
        
              - **JSON** *(dict) --* 
        
                Specifies JSON as request\'s output serialization format.
        
                - **RecordDelimiter** *(string) --* 
        
                  The value used to separate individual records in the output.
        
          - **OutputLocation** *(dict) --* 
        
            Describes the location where the restore job\'s output is stored.
        
            - **S3** *(dict) --* 
        
              Describes an S3 location that will receive the results of the restore request.
        
              - **BucketName** *(string) --* **[REQUIRED]** 
        
                The name of the bucket where the restore results will be placed.
        
              - **Prefix** *(string) --* **[REQUIRED]** 
        
                The prefix that is prepended to the restore results for this request.
        
              - **Encryption** *(dict) --* 
        
                Describes the server-side encryption that will be applied to the restore results.
        
                - **EncryptionType** *(string) --* **[REQUIRED]** 
        
                  The server-side encryption algorithm used when storing job results in Amazon S3 (e.g., AES256, aws:kms).
        
                - **KMSKeyId** *(string) --* 
        
                  If the encryption type is aws:kms, this optional value specifies the AWS KMS key ID to use for encryption of job results.
        
                - **KMSContext** *(string) --* 
        
                  If the encryption type is aws:kms, this optional value can be used to specify the encryption context for the restore results.
        
              - **CannedACL** *(string) --* 
        
                The canned ACL to apply to the restore results.
        
              - **AccessControlList** *(list) --* 
        
                A list of grants that control access to the staged results.
        
                - *(dict) --* 
        
                  - **Grantee** *(dict) --* 
        
                    - **DisplayName** *(string) --* 
        
                      Screen name of the grantee.
        
                    - **EmailAddress** *(string) --* 
        
                      Email address of the grantee.
        
                    - **ID** *(string) --* 
        
                      The canonical user ID of the grantee.
        
                    - **Type** *(string) --* **[REQUIRED]** 
        
                      Type of grantee
        
                    - **URI** *(string) --* 
        
                      URI of the grantee group.
        
                  - **Permission** *(string) --* 
        
                    Specifies the permission given to the grantee.
        
              - **Tagging** *(dict) --* 
        
                The tag-set that is applied to the restore results.
        
                - **TagSet** *(list) --* **[REQUIRED]** 
        
                  - *(dict) --* 
        
                    - **Key** *(string) --* **[REQUIRED]** 
        
                      Name of the tag.
        
                    - **Value** *(string) --* **[REQUIRED]** 
        
                      Value of the tag.
        
              - **UserMetadata** *(list) --* 
        
                A list of metadata to store with the restore results in S3.
        
                - *(dict) --* 
        
                  A metadata key-value pair to store with an object.
        
                  - **Name** *(string) --* 
        
                  - **Value** *(string) --* 
        
              - **StorageClass** *(string) --* 
        
                The class of storage used to store the restore results.
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RequestCharged\': \'requester\',
                \'RestoreOutputPath\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
            - **RestoreOutputPath** *(string) --* 
        
              Indicates the path in the provided S3 output location where Select results will be restored to.
        
        """
        pass

    def upload_file(self, Filename: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None) -> NoReturn:
        """
        
        Usage::
        
            import boto3
            s3 = boto3.resource(\'s3\')
            s3.Object(\'mybucket\', \'hello.txt\').upload_file(\'/tmp/hello.txt\')
        
        Similar behavior as S3Transfer\'s upload_file() method,
        except that parameters are capitalized. Detailed examples can be found at
        :ref:`S3Transfer\'s Usage <ref_s3transfer_usage>`.
        
        :type Filename: str
        :param Filename: The path to the file to upload.
        
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.
        
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the upload.
        
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            transfer.
        """
        pass

    def upload_fileobj(self, Fileobj: IO = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None) -> NoReturn:
        """
        
        The file-like object must be in binary mode.
        
        This is a managed transfer which will perform a multipart upload in
        multiple threads if necessary.
        
        Usage::
        
            import boto3
            s3 = boto3.resource(\'s3\')
            bucket = s3.Bucket(\'mybucket\')
            obj = bucket.Object(\'mykey\')
        
            with open(\'filename\', \'rb\') as data:
                obj.upload_fileobj(data)
        
        :type Fileobj: a file-like object
        :param Fileobj: A file-like object to upload. At a minimum, it must
            implement the `read` method, and must return bytes.
        
        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.
        
        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the upload.
        
        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            upload.
        """
        pass

    def wait_until_exists(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadObject>`_
        
        **Request Syntax** 
        ::
        
          object.wait_until_exists(
              IfMatch=\'string\',
              IfModifiedSince=datetime(2015, 1, 1),
              IfNoneMatch=\'string\',
              IfUnmodifiedSince=datetime(2015, 1, 1),
              Range=\'string\',
              VersionId=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              RequestPayer=\'requester\',
              PartNumber=123
          )
        :type IfMatch: string
        :param IfMatch: 
        
          Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).
        
        :type IfModifiedSince: datetime
        :param IfModifiedSince: 
        
          Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).
        
        :type IfNoneMatch: string
        :param IfNoneMatch: 
        
          Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).
        
        :type IfUnmodifiedSince: datetime
        :param IfUnmodifiedSince: 
        
          Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).
        
        :type Range: string
        :param Range: 
        
          Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
        
        :type VersionId: string
        :param VersionId: 
        
          VersionId used to reference a specific version of the object.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type PartNumber: integer
        :param PartNumber: 
        
          Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a \'ranged\' HEAD request for the part specified. Useful querying about the size of the part and the number of parts in this object.
        
        :returns: None
        """
        pass

    def wait_until_not_exists(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadObject>`_
        
        **Request Syntax** 
        ::
        
          object.wait_until_not_exists(
              IfMatch=\'string\',
              IfModifiedSince=datetime(2015, 1, 1),
              IfNoneMatch=\'string\',
              IfUnmodifiedSince=datetime(2015, 1, 1),
              Range=\'string\',
              VersionId=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              RequestPayer=\'requester\',
              PartNumber=123
          )
        :type IfMatch: string
        :param IfMatch: 
        
          Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).
        
        :type IfModifiedSince: datetime
        :param IfModifiedSince: 
        
          Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).
        
        :type IfNoneMatch: string
        :param IfNoneMatch: 
        
          Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).
        
        :type IfUnmodifiedSince: datetime
        :param IfUnmodifiedSince: 
        
          Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).
        
        :type Range: string
        :param Range: 
        
          Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
        
        :type VersionId: string
        :param VersionId: 
        
          VersionId used to reference a specific version of the object.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type PartNumber: integer
        :param PartNumber: 
        
          Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a \'ranged\' HEAD request for the part specified. Useful querying about the size of the part and the number of parts in this object.
        
        :returns: None
        """
        pass


class ObjectAcl(base.ServiceResource):
    owner: Dict
    grants: List
    request_charged: str
    bucket_name: str
    object_key: str

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def load(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          object_acl.load()
        :returns: None
        """
        pass

    def put(self, ACL: str = None, AccessControlPolicy: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None, RequestPayer: str = None, VersionId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObjectAcl>`_
        
        **Request Syntax** 
        ::
        
          response = object_acl.put(
              ACL=\'private\'|\'public-read\'|\'public-read-write\'|\'authenticated-read\'|\'aws-exec-read\'|\'bucket-owner-read\'|\'bucket-owner-full-control\',
              AccessControlPolicy={
                  \'Grants\': [
                      {
                          \'Grantee\': {
                              \'DisplayName\': \'string\',
                              \'EmailAddress\': \'string\',
                              \'ID\': \'string\',
                              \'Type\': \'CanonicalUser\'|\'AmazonCustomerByEmail\'|\'Group\',
                              \'URI\': \'string\'
                          },
                          \'Permission\': \'FULL_CONTROL\'|\'WRITE\'|\'WRITE_ACP\'|\'READ\'|\'READ_ACP\'
                      },
                  ],
                  \'Owner\': {
                      \'DisplayName\': \'string\',
                      \'ID\': \'string\'
                  }
              },
              GrantFullControl=\'string\',
              GrantRead=\'string\',
              GrantReadACP=\'string\',
              GrantWrite=\'string\',
              GrantWriteACP=\'string\',
              RequestPayer=\'requester\',
              VersionId=\'string\'
          )
        :type ACL: string
        :param ACL: 
        
          The canned ACL to apply to the object.
        
        :type AccessControlPolicy: dict
        :param AccessControlPolicy: 
        
          - **Grants** *(list) --* 
        
            A list of grants.
        
            - *(dict) --* 
        
              - **Grantee** *(dict) --* 
        
                - **DisplayName** *(string) --* 
        
                  Screen name of the grantee.
        
                - **EmailAddress** *(string) --* 
        
                  Email address of the grantee.
        
                - **ID** *(string) --* 
        
                  The canonical user ID of the grantee.
        
                - **Type** *(string) --* **[REQUIRED]** 
        
                  Type of grantee
        
                - **URI** *(string) --* 
        
                  URI of the grantee group.
        
              - **Permission** *(string) --* 
        
                Specifies the permission given to the grantee.
        
          - **Owner** *(dict) --* 
        
            - **DisplayName** *(string) --* 
        
            - **ID** *(string) --* 
        
        :type GrantFullControl: string
        :param GrantFullControl: 
        
          Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.
        
        :type GrantRead: string
        :param GrantRead: 
        
          Allows grantee to list the objects in the bucket.
        
        :type GrantReadACP: string
        :param GrantReadACP: 
        
          Allows grantee to read the bucket ACL.
        
        :type GrantWrite: string
        :param GrantWrite: 
        
          Allows grantee to create, overwrite, and delete any object in the bucket.
        
        :type GrantWriteACP: string
        :param GrantWriteACP: 
        
          Allows grantee to write the ACL for the applicable bucket.
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type VersionId: string
        :param VersionId: 
        
          VersionId used to reference a specific version of the object.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RequestCharged\': \'requester\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
        """
        pass

    def reload(self) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          object_acl.load()
        :returns: None
        """
        pass


class ObjectSummary(base.ServiceResource):
    last_modified: datetime
    e_tag: str
    size: int
    storage_class: str
    owner: Dict
    bucket_name: str
    key: str

    def copy_from(self, CopySource: Union[str, Dict], ACL: str = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentType: str = None, CopySourceIfMatch: str = None, CopySourceIfModifiedSince: datetime = None, CopySourceIfNoneMatch: str = None, CopySourceIfUnmodifiedSince: datetime = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, MetadataDirective: str = None, TaggingDirective: str = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, CopySourceSSECustomerAlgorithm: str = None, CopySourceSSECustomerKey: str = None, CopySourceSSECustomerKeyMD5: str = None, RequestPayer: str = None, Tagging: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CopyObject>`_
        
        **Request Syntax** 
        ::
        
          response = object_summary.copy_from(
              ACL=\'private\'|\'public-read\'|\'public-read-write\'|\'authenticated-read\'|\'aws-exec-read\'|\'bucket-owner-read\'|\'bucket-owner-full-control\',
              CacheControl=\'string\',
              ContentDisposition=\'string\',
              ContentEncoding=\'string\',
              ContentLanguage=\'string\',
              ContentType=\'string\',
              CopySource=\'string\' or {\'Bucket\': \'string\', \'Key\': \'string\', \'VersionId\': \'string\'},
              CopySourceIfMatch=\'string\',
              CopySourceIfModifiedSince=datetime(2015, 1, 1),
              CopySourceIfNoneMatch=\'string\',
              CopySourceIfUnmodifiedSince=datetime(2015, 1, 1),
              Expires=datetime(2015, 1, 1),
              GrantFullControl=\'string\',
              GrantRead=\'string\',
              GrantReadACP=\'string\',
              GrantWriteACP=\'string\',
              Metadata={
                  \'string\': \'string\'
              },
              MetadataDirective=\'COPY\'|\'REPLACE\',
              TaggingDirective=\'COPY\'|\'REPLACE\',
              ServerSideEncryption=\'AES256\'|\'aws:kms\',
              StorageClass=\'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
              WebsiteRedirectLocation=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              SSEKMSKeyId=\'string\',
              CopySourceSSECustomerAlgorithm=\'string\',
              CopySourceSSECustomerKey=\'string\',
              RequestPayer=\'requester\',
              Tagging=\'string\'
          )
        :type ACL: string
        :param ACL: 
        
          The canned ACL to apply to the object.
        
        :type CacheControl: string
        :param CacheControl: 
        
          Specifies caching behavior along the request/reply chain.
        
        :type ContentDisposition: string
        :param ContentDisposition: 
        
          Specifies presentational information for the object.
        
        :type ContentEncoding: string
        :param ContentEncoding: 
        
          Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        
        :type ContentLanguage: string
        :param ContentLanguage: 
        
          The language the content is in.
        
        :type ContentType: string
        :param ContentType: 
        
          A standard MIME type describing the format of the object data.
        
        :type CopySource: str or dict
        :param CopySource: **[REQUIRED]** The name of the source bucket, key name of the source object, and optional version ID of the source object.  You can either provide this value as a string or a dictionary.  The string form is {bucket}/{key} or {bucket}/{key}?versionId={versionId} if you want to copy a specific version.  You can also provide this value as a dictionary.  The dictionary format is recommended over the string format because it is more explicit.  The dictionary format is: {\'Bucket\': \'bucket\', \'Key\': \'key\', \'VersionId\': \'id\'}.  Note that the VersionId key is optional and may be omitted.
        
        :type CopySourceIfMatch: string
        :param CopySourceIfMatch: 
        
          Copies the object if its entity tag (ETag) matches the specified tag.
        
        :type CopySourceIfModifiedSince: datetime
        :param CopySourceIfModifiedSince: 
        
          Copies the object if it has been modified since the specified time.
        
        :type CopySourceIfNoneMatch: string
        :param CopySourceIfNoneMatch: 
        
          Copies the object if its entity tag (ETag) is different than the specified ETag.
        
        :type CopySourceIfUnmodifiedSince: datetime
        :param CopySourceIfUnmodifiedSince: 
        
          Copies the object if it hasn\'t been modified since the specified time.
        
        :type Expires: datetime
        :param Expires: 
        
          The date and time at which the object is no longer cacheable.
        
        :type GrantFullControl: string
        :param GrantFullControl: 
        
          Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
        
        :type GrantRead: string
        :param GrantRead: 
        
          Allows grantee to read the object data and its metadata.
        
        :type GrantReadACP: string
        :param GrantReadACP: 
        
          Allows grantee to read the object ACL.
        
        :type GrantWriteACP: string
        :param GrantWriteACP: 
        
          Allows grantee to write the ACL for the applicable object.
        
        :type Metadata: dict
        :param Metadata: 
        
          A map of metadata to store with the object in S3.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type MetadataDirective: string
        :param MetadataDirective: 
        
          Specifies whether the metadata is copied from the source object or replaced with metadata provided in the request.
        
        :type TaggingDirective: string
        :param TaggingDirective: 
        
          Specifies whether the object tag-set are copied from the source object or replaced with tag-set provided in the request.
        
        :type ServerSideEncryption: string
        :param ServerSideEncryption: 
        
          The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
        :type StorageClass: string
        :param StorageClass: 
        
          The type of storage to use for the object. Defaults to \'STANDARD\'.
        
        :type WebsiteRedirectLocation: string
        :param WebsiteRedirectLocation: 
        
          If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type SSEKMSKeyId: string
        :param SSEKMSKeyId: 
        
          Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version
        
        :type CopySourceSSECustomerAlgorithm: string
        :param CopySourceSSECustomerAlgorithm: 
        
          Specifies the algorithm to use when decrypting the source object (e.g., AES256).
        
        :type CopySourceSSECustomerKey: string
        :param CopySourceSSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.
        
        :type CopySourceSSECustomerKeyMD5: string
        :param CopySourceSSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type Tagging: string
        :param Tagging: 
        
          The tag-set for the object destination object this value must be used in conjunction with the TaggingDirective. The tag-set must be encoded as URL Query parameters
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CopyObjectResult\': {
                    \'ETag\': \'string\',
                    \'LastModified\': datetime(2015, 1, 1)
                },
                \'Expiration\': \'string\',
                \'CopySourceVersionId\': \'string\',
                \'VersionId\': \'string\',
                \'ServerSideEncryption\': \'AES256\'|\'aws:kms\',
                \'SSECustomerAlgorithm\': \'string\',
                \'SSECustomerKeyMD5\': \'string\',
                \'SSEKMSKeyId\': \'string\',
                \'RequestCharged\': \'requester\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CopyObjectResult** *(dict) --* 
              
              - **ETag** *(string) --* 
              
              - **LastModified** *(datetime) --* 
          
            - **Expiration** *(string) --* 
        
              If the object expiration is configured, the response includes this header.
        
            - **CopySourceVersionId** *(string) --* 
            
            - **VersionId** *(string) --* 
        
              Version ID of the newly created copy.
        
            - **ServerSideEncryption** *(string) --* 
        
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
            - **SSECustomerAlgorithm** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
        
            - **SSECustomerKeyMD5** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
        
            - **SSEKMSKeyId** *(string) --* 
        
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
        
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
        """
        pass

    def delete(self, MFA: str = None, VersionId: str = None, RequestPayer: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteObject>`_
        
        **Request Syntax** 
        ::
        
          response = object_summary.delete(
              MFA=\'string\',
              VersionId=\'string\',
              RequestPayer=\'requester\'
          )
        :type MFA: string
        :param MFA: 
        
          The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device.
        
        :type VersionId: string
        :param VersionId: 
        
          VersionId used to reference a specific version of the object.
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeleteMarker\': True|False,
                \'VersionId\': \'string\',
                \'RequestCharged\': \'requester\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DeleteMarker** *(boolean) --* 
        
              Specifies whether the versioned object that was permanently deleted was (true) or was not (false) a delete marker.
        
            - **VersionId** *(string) --* 
        
              Returns the version ID of the delete marker created as a result of the DELETE operation.
        
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
        """
        pass

    def get(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, ResponseCacheControl: str = None, ResponseContentDisposition: str = None, ResponseContentEncoding: str = None, ResponseContentLanguage: str = None, ResponseContentType: str = None, ResponseExpires: datetime = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObject>`_
        
        **Request Syntax** 
        ::
        
          response = object_summary.get(
              IfMatch=\'string\',
              IfModifiedSince=datetime(2015, 1, 1),
              IfNoneMatch=\'string\',
              IfUnmodifiedSince=datetime(2015, 1, 1),
              Range=\'string\',
              ResponseCacheControl=\'string\',
              ResponseContentDisposition=\'string\',
              ResponseContentEncoding=\'string\',
              ResponseContentLanguage=\'string\',
              ResponseContentType=\'string\',
              ResponseExpires=datetime(2015, 1, 1),
              VersionId=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              RequestPayer=\'requester\',
              PartNumber=123
          )
        :type IfMatch: string
        :param IfMatch: 
        
          Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).
        
        :type IfModifiedSince: datetime
        :param IfModifiedSince: 
        
          Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).
        
        :type IfNoneMatch: string
        :param IfNoneMatch: 
        
          Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).
        
        :type IfUnmodifiedSince: datetime
        :param IfUnmodifiedSince: 
        
          Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).
        
        :type Range: string
        :param Range: 
        
          Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
        
        :type ResponseCacheControl: string
        :param ResponseCacheControl: 
        
          Sets the Cache-Control header of the response.
        
        :type ResponseContentDisposition: string
        :param ResponseContentDisposition: 
        
          Sets the Content-Disposition header of the response
        
        :type ResponseContentEncoding: string
        :param ResponseContentEncoding: 
        
          Sets the Content-Encoding header of the response.
        
        :type ResponseContentLanguage: string
        :param ResponseContentLanguage: 
        
          Sets the Content-Language header of the response.
        
        :type ResponseContentType: string
        :param ResponseContentType: 
        
          Sets the Content-Type header of the response.
        
        :type ResponseExpires: datetime
        :param ResponseExpires: 
        
          Sets the Expires header of the response.
        
        :type VersionId: string
        :param VersionId: 
        
          VersionId used to reference a specific version of the object.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type PartNumber: integer
        :param PartNumber: 
        
          Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a \'ranged\' GET request for the part specified. Useful for downloading just a part of an object.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Body\': StreamingBody(),
                \'DeleteMarker\': True|False,
                \'AcceptRanges\': \'string\',
                \'Expiration\': \'string\',
                \'Restore\': \'string\',
                \'LastModified\': datetime(2015, 1, 1),
                \'ContentLength\': 123,
                \'ETag\': \'string\',
                \'MissingMeta\': 123,
                \'VersionId\': \'string\',
                \'CacheControl\': \'string\',
                \'ContentDisposition\': \'string\',
                \'ContentEncoding\': \'string\',
                \'ContentLanguage\': \'string\',
                \'ContentRange\': \'string\',
                \'ContentType\': \'string\',
                \'Expires\': datetime(2015, 1, 1),
                \'WebsiteRedirectLocation\': \'string\',
                \'ServerSideEncryption\': \'AES256\'|\'aws:kms\',
                \'Metadata\': {
                    \'string\': \'string\'
                },
                \'SSECustomerAlgorithm\': \'string\',
                \'SSECustomerKeyMD5\': \'string\',
                \'SSEKMSKeyId\': \'string\',
                \'StorageClass\': \'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
                \'RequestCharged\': \'requester\',
                \'ReplicationStatus\': \'COMPLETE\'|\'PENDING\'|\'FAILED\'|\'REPLICA\',
                \'PartsCount\': 123,
                \'TagCount\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Body** (:class:`.StreamingBody`) -- 
        
              Object data.
        
            - **DeleteMarker** *(boolean) --* 
        
              Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If false, this response header does not appear in the response.
        
            - **AcceptRanges** *(string) --* 
            
            - **Expiration** *(string) --* 
        
              If the object expiration is configured (see PUT Bucket lifecycle), the response includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.
        
            - **Restore** *(string) --* 
        
              Provides information about object restoration operation and expiration time of the restored object copy.
        
            - **LastModified** *(datetime) --* 
        
              Last modified date of the object
        
            - **ContentLength** *(integer) --* 
        
              Size of the body in bytes.
        
            - **ETag** *(string) --* 
        
              An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL
        
            - **MissingMeta** *(integer) --* 
        
              This is set to the number of metadata entries not returned in x-amz-meta headers. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.
        
            - **VersionId** *(string) --* 
        
              Version of the object.
        
            - **CacheControl** *(string) --* 
        
              Specifies caching behavior along the request/reply chain.
        
            - **ContentDisposition** *(string) --* 
        
              Specifies presentational information for the object.
        
            - **ContentEncoding** *(string) --* 
        
              Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        
            - **ContentLanguage** *(string) --* 
        
              The language the content is in.
        
            - **ContentRange** *(string) --* 
        
              The portion of the object returned in the response.
        
            - **ContentType** *(string) --* 
        
              A standard MIME type describing the format of the object data.
        
            - **Expires** *(datetime) --* 
        
              The date and time at which the object is no longer cacheable.
        
            - **WebsiteRedirectLocation** *(string) --* 
        
              If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        
            - **ServerSideEncryption** *(string) --* 
        
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
            - **Metadata** *(dict) --* 
        
              A map of metadata to store with the object in S3.
        
              - *(string) --* 
                
                - *(string) --* 
          
            - **SSECustomerAlgorithm** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
        
            - **SSECustomerKeyMD5** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
        
            - **SSEKMSKeyId** *(string) --* 
        
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
        
            - **StorageClass** *(string) --* 
            
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
            - **ReplicationStatus** *(string) --* 
            
            - **PartsCount** *(integer) --* 
        
              The count of parts this object has.
        
            - **TagCount** *(integer) --* 
        
              The number of tags, if any, on the object.
        
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def initiate_multipart_upload(self, ACL: str = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentType: str = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, RequestPayer: str = None, Tagging: str = None) -> 'MultipartUpload':
        """
        
         **Note:** After you initiate multipart upload and upload one or more parts, you must either complete or abort multipart upload in order to stop getting charged for storage of the uploaded parts. Only after you either complete or abort multipart upload, Amazon S3 frees up the parts storage and stops charging you for the parts storage.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CreateMultipartUpload>`_
        
        **Request Syntax** 
        ::
        
          multipart_upload = object_summary.initiate_multipart_upload(
              ACL=\'private\'|\'public-read\'|\'public-read-write\'|\'authenticated-read\'|\'aws-exec-read\'|\'bucket-owner-read\'|\'bucket-owner-full-control\',
              CacheControl=\'string\',
              ContentDisposition=\'string\',
              ContentEncoding=\'string\',
              ContentLanguage=\'string\',
              ContentType=\'string\',
              Expires=datetime(2015, 1, 1),
              GrantFullControl=\'string\',
              GrantRead=\'string\',
              GrantReadACP=\'string\',
              GrantWriteACP=\'string\',
              Metadata={
                  \'string\': \'string\'
              },
              ServerSideEncryption=\'AES256\'|\'aws:kms\',
              StorageClass=\'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
              WebsiteRedirectLocation=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              SSEKMSKeyId=\'string\',
              RequestPayer=\'requester\',
              Tagging=\'string\'
          )
        :type ACL: string
        :param ACL: 
        
          The canned ACL to apply to the object.
        
        :type CacheControl: string
        :param CacheControl: 
        
          Specifies caching behavior along the request/reply chain.
        
        :type ContentDisposition: string
        :param ContentDisposition: 
        
          Specifies presentational information for the object.
        
        :type ContentEncoding: string
        :param ContentEncoding: 
        
          Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        
        :type ContentLanguage: string
        :param ContentLanguage: 
        
          The language the content is in.
        
        :type ContentType: string
        :param ContentType: 
        
          A standard MIME type describing the format of the object data.
        
        :type Expires: datetime
        :param Expires: 
        
          The date and time at which the object is no longer cacheable.
        
        :type GrantFullControl: string
        :param GrantFullControl: 
        
          Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
        
        :type GrantRead: string
        :param GrantRead: 
        
          Allows grantee to read the object data and its metadata.
        
        :type GrantReadACP: string
        :param GrantReadACP: 
        
          Allows grantee to read the object ACL.
        
        :type GrantWriteACP: string
        :param GrantWriteACP: 
        
          Allows grantee to write the ACL for the applicable object.
        
        :type Metadata: dict
        :param Metadata: 
        
          A map of metadata to store with the object in S3.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type ServerSideEncryption: string
        :param ServerSideEncryption: 
        
          The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
        :type StorageClass: string
        :param StorageClass: 
        
          The type of storage to use for the object. Defaults to \'STANDARD\'.
        
        :type WebsiteRedirectLocation: string
        :param WebsiteRedirectLocation: 
        
          If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type SSEKMSKeyId: string
        :param SSEKMSKeyId: 
        
          Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type Tagging: string
        :param Tagging: 
        
          The tag-set for the object. The tag-set must be encoded as URL Query parameters
        
        :rtype: :py:class:`s3.MultipartUpload`
        :returns: MultipartUpload resource
        """
        pass

    def load(self) -> NoReturn:
        """
        resource.
        """
        pass

    def put(self, ACL: str = None, Body: Union[bytes, IO] = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentLength: int = None, ContentMD5: str = None, ContentType: str = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, RequestPayer: str = None, Tagging: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObject>`_
        
        **Request Syntax** 
        ::
        
          response = object_summary.put(
              ACL=\'private\'|\'public-read\'|\'public-read-write\'|\'authenticated-read\'|\'aws-exec-read\'|\'bucket-owner-read\'|\'bucket-owner-full-control\',
              Body=b\'bytes\'|file,
              CacheControl=\'string\',
              ContentDisposition=\'string\',
              ContentEncoding=\'string\',
              ContentLanguage=\'string\',
              ContentLength=123,
              ContentMD5=\'string\',
              ContentType=\'string\',
              Expires=datetime(2015, 1, 1),
              GrantFullControl=\'string\',
              GrantRead=\'string\',
              GrantReadACP=\'string\',
              GrantWriteACP=\'string\',
              Metadata={
                  \'string\': \'string\'
              },
              ServerSideEncryption=\'AES256\'|\'aws:kms\',
              StorageClass=\'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
              WebsiteRedirectLocation=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              SSEKMSKeyId=\'string\',
              RequestPayer=\'requester\',
              Tagging=\'string\'
          )
        :type ACL: string
        :param ACL: 
        
          The canned ACL to apply to the object.
        
        :type Body: bytes or seekable file-like object
        :param Body: 
        
          Object data.
        
        :type CacheControl: string
        :param CacheControl: 
        
          Specifies caching behavior along the request/reply chain.
        
        :type ContentDisposition: string
        :param ContentDisposition: 
        
          Specifies presentational information for the object.
        
        :type ContentEncoding: string
        :param ContentEncoding: 
        
          Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        
        :type ContentLanguage: string
        :param ContentLanguage: 
        
          The language the content is in.
        
        :type ContentLength: integer
        :param ContentLength: 
        
          Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically.
        
        :type ContentMD5: string
        :param ContentMD5: 
        
          The base64-encoded 128-bit MD5 digest of the part data.
        
        :type ContentType: string
        :param ContentType: 
        
          A standard MIME type describing the format of the object data.
        
        :type Expires: datetime
        :param Expires: 
        
          The date and time at which the object is no longer cacheable.
        
        :type GrantFullControl: string
        :param GrantFullControl: 
        
          Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.
        
        :type GrantRead: string
        :param GrantRead: 
        
          Allows grantee to read the object data and its metadata.
        
        :type GrantReadACP: string
        :param GrantReadACP: 
        
          Allows grantee to read the object ACL.
        
        :type GrantWriteACP: string
        :param GrantWriteACP: 
        
          Allows grantee to write the ACL for the applicable object.
        
        :type Metadata: dict
        :param Metadata: 
        
          A map of metadata to store with the object in S3.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type ServerSideEncryption: string
        :param ServerSideEncryption: 
        
          The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
        :type StorageClass: string
        :param StorageClass: 
        
          The type of storage to use for the object. Defaults to \'STANDARD\'.
        
        :type WebsiteRedirectLocation: string
        :param WebsiteRedirectLocation: 
        
          If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type SSEKMSKeyId: string
        :param SSEKMSKeyId: 
        
          Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type Tagging: string
        :param Tagging: 
        
          The tag-set for the object. The tag-set must be encoded as URL Query parameters
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Expiration\': \'string\',
                \'ETag\': \'string\',
                \'ServerSideEncryption\': \'AES256\'|\'aws:kms\',
                \'VersionId\': \'string\',
                \'SSECustomerAlgorithm\': \'string\',
                \'SSECustomerKeyMD5\': \'string\',
                \'SSEKMSKeyId\': \'string\',
                \'RequestCharged\': \'requester\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Expiration** *(string) --* 
        
              If the object expiration is configured, this will contain the expiration date (expiry-date) and rule ID (rule-id). The value of rule-id is URL encoded.
        
            - **ETag** *(string) --* 
        
              Entity tag for the uploaded object.
        
            - **ServerSideEncryption** *(string) --* 
        
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
            - **VersionId** *(string) --* 
        
              Version of the object.
        
            - **SSECustomerAlgorithm** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
        
            - **SSECustomerKeyMD5** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
        
            - **SSEKMSKeyId** *(string) --* 
        
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
        
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
        """
        pass

    def restore_object(self, VersionId: str = None, RestoreRequest: Dict = None, RequestPayer: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/RestoreObject>`_
        
        **Request Syntax** 
        ::
        
          response = object_summary.restore_object(
              VersionId=\'string\',
              RestoreRequest={
                  \'Days\': 123,
                  \'GlacierJobParameters\': {
                      \'Tier\': \'Standard\'|\'Bulk\'|\'Expedited\'
                  },
                  \'Type\': \'SELECT\',
                  \'Tier\': \'Standard\'|\'Bulk\'|\'Expedited\',
                  \'Description\': \'string\',
                  \'SelectParameters\': {
                      \'InputSerialization\': {
                          \'CSV\': {
                              \'FileHeaderInfo\': \'USE\'|\'IGNORE\'|\'NONE\',
                              \'Comments\': \'string\',
                              \'QuoteEscapeCharacter\': \'string\',
                              \'RecordDelimiter\': \'string\',
                              \'FieldDelimiter\': \'string\',
                              \'QuoteCharacter\': \'string\',
                              \'AllowQuotedRecordDelimiter\': True|False
                          },
                          \'CompressionType\': \'NONE\'|\'GZIP\'|\'BZIP2\',
                          \'JSON\': {
                              \'Type\': \'DOCUMENT\'|\'LINES\'
                          },
                          \'Parquet\': {}
                          
                      },
                      \'ExpressionType\': \'SQL\',
                      \'Expression\': \'string\',
                      \'OutputSerialization\': {
                          \'CSV\': {
                              \'QuoteFields\': \'ALWAYS\'|\'ASNEEDED\',
                              \'QuoteEscapeCharacter\': \'string\',
                              \'RecordDelimiter\': \'string\',
                              \'FieldDelimiter\': \'string\',
                              \'QuoteCharacter\': \'string\'
                          },
                          \'JSON\': {
                              \'RecordDelimiter\': \'string\'
                          }
                      }
                  },
                  \'OutputLocation\': {
                      \'S3\': {
                          \'BucketName\': \'string\',
                          \'Prefix\': \'string\',
                          \'Encryption\': {
                              \'EncryptionType\': \'AES256\'|\'aws:kms\',
                              \'KMSKeyId\': \'string\',
                              \'KMSContext\': \'string\'
                          },
                          \'CannedACL\': \'private\'|\'public-read\'|\'public-read-write\'|\'authenticated-read\'|\'aws-exec-read\'|\'bucket-owner-read\'|\'bucket-owner-full-control\',
                          \'AccessControlList\': [
                              {
                                  \'Grantee\': {
                                      \'DisplayName\': \'string\',
                                      \'EmailAddress\': \'string\',
                                      \'ID\': \'string\',
                                      \'Type\': \'CanonicalUser\'|\'AmazonCustomerByEmail\'|\'Group\',
                                      \'URI\': \'string\'
                                  },
                                  \'Permission\': \'FULL_CONTROL\'|\'WRITE\'|\'WRITE_ACP\'|\'READ\'|\'READ_ACP\'
                              },
                          ],
                          \'Tagging\': {
                              \'TagSet\': [
                                  {
                                      \'Key\': \'string\',
                                      \'Value\': \'string\'
                                  },
                              ]
                          },
                          \'UserMetadata\': [
                              {
                                  \'Name\': \'string\',
                                  \'Value\': \'string\'
                              },
                          ],
                          \'StorageClass\': \'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\'
                      }
                  }
              },
              RequestPayer=\'requester\'
          )
        :type VersionId: string
        :param VersionId: 
        
        :type RestoreRequest: dict
        :param RestoreRequest: 
        
          Container for restore job parameters.
        
          - **Days** *(integer) --* 
        
            Lifetime of the active copy in days. Do not use with restores that specify OutputLocation.
        
          - **GlacierJobParameters** *(dict) --* 
        
            Glacier related parameters pertaining to this job. Do not use with restores that specify OutputLocation.
        
            - **Tier** *(string) --* **[REQUIRED]** 
        
              Glacier retrieval tier at which the restore will be processed.
        
          - **Type** *(string) --* 
        
            Type of restore request.
        
          - **Tier** *(string) --* 
        
            Glacier retrieval tier at which the restore will be processed.
        
          - **Description** *(string) --* 
        
            The optional description for the job.
        
          - **SelectParameters** *(dict) --* 
        
            Describes the parameters for Select job types.
        
            - **InputSerialization** *(dict) --* **[REQUIRED]** 
        
              Describes the serialization format of the object.
        
              - **CSV** *(dict) --* 
        
                Describes the serialization of a CSV-encoded object.
        
                - **FileHeaderInfo** *(string) --* 
        
                  Describes the first line of input. Valid values: None, Ignore, Use.
        
                - **Comments** *(string) --* 
        
                  Single character used to indicate a row should be ignored when present at the start of a row.
        
                - **QuoteEscapeCharacter** *(string) --* 
        
                  Single character used for escaping the quote character inside an already escaped value.
        
                - **RecordDelimiter** *(string) --* 
        
                  Value used to separate individual records.
        
                - **FieldDelimiter** *(string) --* 
        
                  Value used to separate individual fields in a record.
        
                - **QuoteCharacter** *(string) --* 
        
                  Value used for escaping where the field delimiter is part of the value.
        
                - **AllowQuotedRecordDelimiter** *(boolean) --* 
        
                  Specifies that CSV field values may contain quoted record delimiters and such records should be allowed. Default value is FALSE. Setting this value to TRUE may lower performance.
        
              - **CompressionType** *(string) --* 
        
                Specifies object\'s compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE.
        
              - **JSON** *(dict) --* 
        
                Specifies JSON as object\'s input serialization format.
        
                - **Type** *(string) --* 
        
                  The type of JSON. Valid values: Document, Lines.
        
              - **Parquet** *(dict) --* 
        
                Specifies Parquet as object\'s input serialization format.
        
            - **ExpressionType** *(string) --* **[REQUIRED]** 
        
              The type of the provided expression (e.g., SQL).
        
            - **Expression** *(string) --* **[REQUIRED]** 
        
              The expression that is used to query the object.
        
            - **OutputSerialization** *(dict) --* **[REQUIRED]** 
        
              Describes how the results of the Select job are serialized.
        
              - **CSV** *(dict) --* 
        
                Describes the serialization of CSV-encoded Select results.
        
                - **QuoteFields** *(string) --* 
        
                  Indicates whether or not all output fields should be quoted.
        
                - **QuoteEscapeCharacter** *(string) --* 
        
                  Single character used for escaping the quote character inside an already escaped value.
        
                - **RecordDelimiter** *(string) --* 
        
                  Value used to separate individual records.
        
                - **FieldDelimiter** *(string) --* 
        
                  Value used to separate individual fields in a record.
        
                - **QuoteCharacter** *(string) --* 
        
                  Value used for escaping where the field delimiter is part of the value.
        
              - **JSON** *(dict) --* 
        
                Specifies JSON as request\'s output serialization format.
        
                - **RecordDelimiter** *(string) --* 
        
                  The value used to separate individual records in the output.
        
          - **OutputLocation** *(dict) --* 
        
            Describes the location where the restore job\'s output is stored.
        
            - **S3** *(dict) --* 
        
              Describes an S3 location that will receive the results of the restore request.
        
              - **BucketName** *(string) --* **[REQUIRED]** 
        
                The name of the bucket where the restore results will be placed.
        
              - **Prefix** *(string) --* **[REQUIRED]** 
        
                The prefix that is prepended to the restore results for this request.
        
              - **Encryption** *(dict) --* 
        
                Describes the server-side encryption that will be applied to the restore results.
        
                - **EncryptionType** *(string) --* **[REQUIRED]** 
        
                  The server-side encryption algorithm used when storing job results in Amazon S3 (e.g., AES256, aws:kms).
        
                - **KMSKeyId** *(string) --* 
        
                  If the encryption type is aws:kms, this optional value specifies the AWS KMS key ID to use for encryption of job results.
        
                - **KMSContext** *(string) --* 
        
                  If the encryption type is aws:kms, this optional value can be used to specify the encryption context for the restore results.
        
              - **CannedACL** *(string) --* 
        
                The canned ACL to apply to the restore results.
        
              - **AccessControlList** *(list) --* 
        
                A list of grants that control access to the staged results.
        
                - *(dict) --* 
        
                  - **Grantee** *(dict) --* 
        
                    - **DisplayName** *(string) --* 
        
                      Screen name of the grantee.
        
                    - **EmailAddress** *(string) --* 
        
                      Email address of the grantee.
        
                    - **ID** *(string) --* 
        
                      The canonical user ID of the grantee.
        
                    - **Type** *(string) --* **[REQUIRED]** 
        
                      Type of grantee
        
                    - **URI** *(string) --* 
        
                      URI of the grantee group.
        
                  - **Permission** *(string) --* 
        
                    Specifies the permission given to the grantee.
        
              - **Tagging** *(dict) --* 
        
                The tag-set that is applied to the restore results.
        
                - **TagSet** *(list) --* **[REQUIRED]** 
        
                  - *(dict) --* 
        
                    - **Key** *(string) --* **[REQUIRED]** 
        
                      Name of the tag.
        
                    - **Value** *(string) --* **[REQUIRED]** 
        
                      Value of the tag.
        
              - **UserMetadata** *(list) --* 
        
                A list of metadata to store with the restore results in S3.
        
                - *(dict) --* 
        
                  A metadata key-value pair to store with an object.
        
                  - **Name** *(string) --* 
        
                  - **Value** *(string) --* 
        
              - **StorageClass** *(string) --* 
        
                The class of storage used to store the restore results.
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'RequestCharged\': \'requester\',
                \'RestoreOutputPath\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
            - **RestoreOutputPath** *(string) --* 
        
              Indicates the path in the provided S3 output location where Select results will be restored to.
        
        """
        pass

    def wait_until_exists(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadObject>`_
        
        **Request Syntax** 
        ::
        
          object_summary.wait_until_exists(
              IfMatch=\'string\',
              IfModifiedSince=datetime(2015, 1, 1),
              IfNoneMatch=\'string\',
              IfUnmodifiedSince=datetime(2015, 1, 1),
              Range=\'string\',
              VersionId=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              RequestPayer=\'requester\',
              PartNumber=123
          )
        :type IfMatch: string
        :param IfMatch: 
        
          Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).
        
        :type IfModifiedSince: datetime
        :param IfModifiedSince: 
        
          Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).
        
        :type IfNoneMatch: string
        :param IfNoneMatch: 
        
          Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).
        
        :type IfUnmodifiedSince: datetime
        :param IfUnmodifiedSince: 
        
          Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).
        
        :type Range: string
        :param Range: 
        
          Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
        
        :type VersionId: string
        :param VersionId: 
        
          VersionId used to reference a specific version of the object.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type PartNumber: integer
        :param PartNumber: 
        
          Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a \'ranged\' HEAD request for the part specified. Useful querying about the size of the part and the number of parts in this object.
        
        :returns: None
        """
        pass

    def wait_until_not_exists(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadObject>`_
        
        **Request Syntax** 
        ::
        
          object_summary.wait_until_not_exists(
              IfMatch=\'string\',
              IfModifiedSince=datetime(2015, 1, 1),
              IfNoneMatch=\'string\',
              IfUnmodifiedSince=datetime(2015, 1, 1),
              Range=\'string\',
              VersionId=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              RequestPayer=\'requester\',
              PartNumber=123
          )
        :type IfMatch: string
        :param IfMatch: 
        
          Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).
        
        :type IfModifiedSince: datetime
        :param IfModifiedSince: 
        
          Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).
        
        :type IfNoneMatch: string
        :param IfNoneMatch: 
        
          Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).
        
        :type IfUnmodifiedSince: datetime
        :param IfUnmodifiedSince: 
        
          Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).
        
        :type Range: string
        :param Range: 
        
          Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
        
        :type VersionId: string
        :param VersionId: 
        
          VersionId used to reference a specific version of the object.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type PartNumber: integer
        :param PartNumber: 
        
          Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a \'ranged\' HEAD request for the part specified. Useful querying about the size of the part and the number of parts in this object.
        
        :returns: None
        """
        pass


class ObjectVersion(base.ServiceResource):
    e_tag: str
    size: int
    storage_class: str
    key: str
    version_id: str
    is_latest: bool
    last_modified: datetime
    owner: Dict
    bucket_name: str
    object_key: str
    id: str

    def delete(self, MFA: str = None, RequestPayer: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteObject>`_
        
        **Request Syntax** 
        ::
        
          response = object_version.delete(
              MFA=\'string\',
              RequestPayer=\'requester\'
          )
        :type MFA: string
        :param MFA: 
        
          The concatenation of the authentication device\'s serial number, a space, and the value that is displayed on your authentication device.
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeleteMarker\': True|False,
                \'VersionId\': \'string\',
                \'RequestCharged\': \'requester\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DeleteMarker** *(boolean) --* 
        
              Specifies whether the versioned object that was permanently deleted was (true) or was not (false) a delete marker.
        
            - **VersionId** *(string) --* 
        
              Returns the version ID of the delete marker created as a result of the DELETE operation.
        
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
        """
        pass

    def get(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, ResponseCacheControl: str = None, ResponseContentDisposition: str = None, ResponseContentEncoding: str = None, ResponseContentLanguage: str = None, ResponseContentType: str = None, ResponseExpires: datetime = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObject>`_
        
        **Request Syntax** 
        ::
        
          response = object_version.get(
              IfMatch=\'string\',
              IfModifiedSince=datetime(2015, 1, 1),
              IfNoneMatch=\'string\',
              IfUnmodifiedSince=datetime(2015, 1, 1),
              Range=\'string\',
              ResponseCacheControl=\'string\',
              ResponseContentDisposition=\'string\',
              ResponseContentEncoding=\'string\',
              ResponseContentLanguage=\'string\',
              ResponseContentType=\'string\',
              ResponseExpires=datetime(2015, 1, 1),
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              RequestPayer=\'requester\',
              PartNumber=123
          )
        :type IfMatch: string
        :param IfMatch: 
        
          Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).
        
        :type IfModifiedSince: datetime
        :param IfModifiedSince: 
        
          Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).
        
        :type IfNoneMatch: string
        :param IfNoneMatch: 
        
          Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).
        
        :type IfUnmodifiedSince: datetime
        :param IfUnmodifiedSince: 
        
          Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).
        
        :type Range: string
        :param Range: 
        
          Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
        
        :type ResponseCacheControl: string
        :param ResponseCacheControl: 
        
          Sets the Cache-Control header of the response.
        
        :type ResponseContentDisposition: string
        :param ResponseContentDisposition: 
        
          Sets the Content-Disposition header of the response
        
        :type ResponseContentEncoding: string
        :param ResponseContentEncoding: 
        
          Sets the Content-Encoding header of the response.
        
        :type ResponseContentLanguage: string
        :param ResponseContentLanguage: 
        
          Sets the Content-Language header of the response.
        
        :type ResponseContentType: string
        :param ResponseContentType: 
        
          Sets the Content-Type header of the response.
        
        :type ResponseExpires: datetime
        :param ResponseExpires: 
        
          Sets the Expires header of the response.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type PartNumber: integer
        :param PartNumber: 
        
          Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a \'ranged\' GET request for the part specified. Useful for downloading just a part of an object.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Body\': StreamingBody(),
                \'DeleteMarker\': True|False,
                \'AcceptRanges\': \'string\',
                \'Expiration\': \'string\',
                \'Restore\': \'string\',
                \'LastModified\': datetime(2015, 1, 1),
                \'ContentLength\': 123,
                \'ETag\': \'string\',
                \'MissingMeta\': 123,
                \'VersionId\': \'string\',
                \'CacheControl\': \'string\',
                \'ContentDisposition\': \'string\',
                \'ContentEncoding\': \'string\',
                \'ContentLanguage\': \'string\',
                \'ContentRange\': \'string\',
                \'ContentType\': \'string\',
                \'Expires\': datetime(2015, 1, 1),
                \'WebsiteRedirectLocation\': \'string\',
                \'ServerSideEncryption\': \'AES256\'|\'aws:kms\',
                \'Metadata\': {
                    \'string\': \'string\'
                },
                \'SSECustomerAlgorithm\': \'string\',
                \'SSECustomerKeyMD5\': \'string\',
                \'SSEKMSKeyId\': \'string\',
                \'StorageClass\': \'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
                \'RequestCharged\': \'requester\',
                \'ReplicationStatus\': \'COMPLETE\'|\'PENDING\'|\'FAILED\'|\'REPLICA\',
                \'PartsCount\': 123,
                \'TagCount\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Body** (:class:`.StreamingBody`) -- 
        
              Object data.
        
            - **DeleteMarker** *(boolean) --* 
        
              Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If false, this response header does not appear in the response.
        
            - **AcceptRanges** *(string) --* 
            
            - **Expiration** *(string) --* 
        
              If the object expiration is configured (see PUT Bucket lifecycle), the response includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.
        
            - **Restore** *(string) --* 
        
              Provides information about object restoration operation and expiration time of the restored object copy.
        
            - **LastModified** *(datetime) --* 
        
              Last modified date of the object
        
            - **ContentLength** *(integer) --* 
        
              Size of the body in bytes.
        
            - **ETag** *(string) --* 
        
              An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL
        
            - **MissingMeta** *(integer) --* 
        
              This is set to the number of metadata entries not returned in x-amz-meta headers. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.
        
            - **VersionId** *(string) --* 
        
              Version of the object.
        
            - **CacheControl** *(string) --* 
        
              Specifies caching behavior along the request/reply chain.
        
            - **ContentDisposition** *(string) --* 
        
              Specifies presentational information for the object.
        
            - **ContentEncoding** *(string) --* 
        
              Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        
            - **ContentLanguage** *(string) --* 
        
              The language the content is in.
        
            - **ContentRange** *(string) --* 
        
              The portion of the object returned in the response.
        
            - **ContentType** *(string) --* 
        
              A standard MIME type describing the format of the object data.
        
            - **Expires** *(datetime) --* 
        
              The date and time at which the object is no longer cacheable.
        
            - **WebsiteRedirectLocation** *(string) --* 
        
              If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        
            - **ServerSideEncryption** *(string) --* 
        
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
            - **Metadata** *(dict) --* 
        
              A map of metadata to store with the object in S3.
        
              - *(string) --* 
                
                - *(string) --* 
          
            - **SSECustomerAlgorithm** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
        
            - **SSECustomerKeyMD5** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
        
            - **SSEKMSKeyId** *(string) --* 
        
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
        
            - **StorageClass** *(string) --* 
            
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
            - **ReplicationStatus** *(string) --* 
            
            - **PartsCount** *(integer) --* 
        
              The count of parts this object has.
        
            - **TagCount** *(integer) --* 
        
              The number of tags, if any, on the object.
        
        """
        pass

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def head(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadObject>`_
        
        **Request Syntax** 
        ::
        
          response = object_version.head(
              IfMatch=\'string\',
              IfModifiedSince=datetime(2015, 1, 1),
              IfNoneMatch=\'string\',
              IfUnmodifiedSince=datetime(2015, 1, 1),
              Range=\'string\',
              SSECustomerAlgorithm=\'string\',
              SSECustomerKey=\'string\',
              RequestPayer=\'requester\',
              PartNumber=123
          )
        :type IfMatch: string
        :param IfMatch: 
        
          Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).
        
        :type IfModifiedSince: datetime
        :param IfModifiedSince: 
        
          Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).
        
        :type IfNoneMatch: string
        :param IfNoneMatch: 
        
          Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).
        
        :type IfUnmodifiedSince: datetime
        :param IfUnmodifiedSince: 
        
          Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).
        
        :type Range: string
        :param Range: 
        
          Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.
        
        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm: 
        
          Specifies the algorithm to use to when encrypting the object (e.g., AES256).
        
        :type SSECustomerKey: string
        :param SSECustomerKey: 
        
          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.
        
        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5: 
        
          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type PartNumber: integer
        :param PartNumber: 
        
          Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a \'ranged\' HEAD request for the part specified. Useful querying about the size of the part and the number of parts in this object.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeleteMarker\': True|False,
                \'AcceptRanges\': \'string\',
                \'Expiration\': \'string\',
                \'Restore\': \'string\',
                \'LastModified\': datetime(2015, 1, 1),
                \'ContentLength\': 123,
                \'ETag\': \'string\',
                \'MissingMeta\': 123,
                \'VersionId\': \'string\',
                \'CacheControl\': \'string\',
                \'ContentDisposition\': \'string\',
                \'ContentEncoding\': \'string\',
                \'ContentLanguage\': \'string\',
                \'ContentType\': \'string\',
                \'Expires\': datetime(2015, 1, 1),
                \'WebsiteRedirectLocation\': \'string\',
                \'ServerSideEncryption\': \'AES256\'|\'aws:kms\',
                \'Metadata\': {
                    \'string\': \'string\'
                },
                \'SSECustomerAlgorithm\': \'string\',
                \'SSECustomerKeyMD5\': \'string\',
                \'SSEKMSKeyId\': \'string\',
                \'StorageClass\': \'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
                \'RequestCharged\': \'requester\',
                \'ReplicationStatus\': \'COMPLETE\'|\'PENDING\'|\'FAILED\'|\'REPLICA\',
                \'PartsCount\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DeleteMarker** *(boolean) --* 
        
              Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If false, this response header does not appear in the response.
        
            - **AcceptRanges** *(string) --* 
            
            - **Expiration** *(string) --* 
        
              If the object expiration is configured (see PUT Bucket lifecycle), the response includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.
        
            - **Restore** *(string) --* 
        
              Provides information about object restoration operation and expiration time of the restored object copy.
        
            - **LastModified** *(datetime) --* 
        
              Last modified date of the object
        
            - **ContentLength** *(integer) --* 
        
              Size of the body in bytes.
        
            - **ETag** *(string) --* 
        
              An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL
        
            - **MissingMeta** *(integer) --* 
        
              This is set to the number of metadata entries not returned in x-amz-meta headers. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.
        
            - **VersionId** *(string) --* 
        
              Version of the object.
        
            - **CacheControl** *(string) --* 
        
              Specifies caching behavior along the request/reply chain.
        
            - **ContentDisposition** *(string) --* 
        
              Specifies presentational information for the object.
        
            - **ContentEncoding** *(string) --* 
        
              Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        
            - **ContentLanguage** *(string) --* 
        
              The language the content is in.
        
            - **ContentType** *(string) --* 
        
              A standard MIME type describing the format of the object data.
        
            - **Expires** *(datetime) --* 
        
              The date and time at which the object is no longer cacheable.
        
            - **WebsiteRedirectLocation** *(string) --* 
        
              If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        
            - **ServerSideEncryption** *(string) --* 
        
              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).
        
            - **Metadata** *(dict) --* 
        
              A map of metadata to store with the object in S3.
        
              - *(string) --* 
                
                - *(string) --* 
          
            - **SSECustomerAlgorithm** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header confirming the encryption algorithm used.
        
            - **SSECustomerKeyMD5** *(string) --* 
        
              If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide round trip message integrity verification of the customer-provided encryption key.
        
            - **SSEKMSKeyId** *(string) --* 
        
              If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key that was used for the object.
        
            - **StorageClass** *(string) --* 
            
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
            - **ReplicationStatus** *(string) --* 
            
            - **PartsCount** *(integer) --* 
        
              The count of parts this object has.
        
        """
        pass


class buckets(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Bucket']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListBuckets>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_iterator = s3.buckets.all()
        :rtype: list(:py:class:`s3.Bucket`)
        :returns: A list of Bucket resources
        """
        pass

    
    @classmethod
    def filter(cls) -> List['Bucket']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListBuckets>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_iterator = s3.buckets.filter()
        :rtype: list(:py:class:`s3.Bucket`)
        :returns: A list of Bucket resources
        """
        pass

    
    @classmethod
    def iterator(cls) -> ResourceCollection:
        """
        
        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """
        pass

    
    @classmethod
    def limit(cls) -> List['Bucket']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListBuckets>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_iterator = s3.buckets.limit()
        :rtype: list(:py:class:`s3.Bucket`)
        :returns: A list of Bucket resources
        """
        pass

    
    @classmethod
    def page_size(cls) -> List['Bucket']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListBuckets>`_
        
        **Request Syntax** 
        
        ::
        
          bucket_iterator = s3.buckets.page_size()
        :rtype: list(:py:class:`s3.Bucket`)
        :returns: A list of Bucket resources
        """
        pass

    
    @classmethod
    def pages(cls) -> List[base.ServiceResource]:
        """
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.
        
        Page size, item limit, and filter parameters are applied
        if they have previously been set.
        
            >>> bucket = s3.Bucket(\'boto3\')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...     for obj in page:
            ...         print(obj.key)
            \'key1\'
            \'key2\'
        
        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
        pass
