from typing import Dict
from botocore.paginate import Paginator


class ListMultipartUploads(Paginator):
    def paginate(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, Prefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListMultipartUploads>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Bucket=\'string\',
              Delimiter=\'string\',
              EncodingType=\'url\',
              Prefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]** 
        
        :type Delimiter: string
        :param Delimiter: 
        
          Character you use to group keys.
        
        :type EncodingType: string
        :param EncodingType: 
        
          Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.
        
        :type Prefix: string
        :param Prefix: 
        
          Lists in-progress uploads only for those keys that begin with the specified prefix.
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Bucket\': \'string\',
                \'KeyMarker\': \'string\',
                \'UploadIdMarker\': \'string\',
                \'Prefix\': \'string\',
                \'Delimiter\': \'string\',
                \'MaxUploads\': 123,
                \'IsTruncated\': True|False,
                \'Uploads\': [
                    {
                        \'UploadId\': \'string\',
                        \'Key\': \'string\',
                        \'Initiated\': datetime(2015, 1, 1),
                        \'StorageClass\': \'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
                        \'Owner\': {
                            \'DisplayName\': \'string\',
                            \'ID\': \'string\'
                        },
                        \'Initiator\': {
                            \'ID\': \'string\',
                            \'DisplayName\': \'string\'
                        }
                    },
                ],
                \'CommonPrefixes\': [
                    {
                        \'Prefix\': \'string\'
                    },
                ],
                \'EncodingType\': \'url\',
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Bucket** *(string) --* 
        
              Name of the bucket to which the multipart upload was initiated.
        
            - **KeyMarker** *(string) --* 
        
              The key at or after which the listing began.
        
            - **UploadIdMarker** *(string) --* 
        
              Upload ID after which listing began.
        
            - **Prefix** *(string) --* 
        
              When a prefix is provided in the request, this field contains the specified prefix. The result contains only keys starting with the specified prefix.
        
            - **Delimiter** *(string) --* 
            
            - **MaxUploads** *(integer) --* 
        
              Maximum number of multipart uploads that could have been included in the response.
        
            - **IsTruncated** *(boolean) --* 
        
              Indicates whether the returned list of multipart uploads is truncated. A value of true indicates that the list was truncated. The list can be truncated if the number of multipart uploads exceeds the limit allowed or specified by max uploads.
        
            - **Uploads** *(list) --* 
              
              - *(dict) --* 
                
                - **UploadId** *(string) --* 
        
                  Upload ID that identifies the multipart upload.
        
                - **Key** *(string) --* 
        
                  Key of the object for which the multipart upload was initiated.
        
                - **Initiated** *(datetime) --* 
        
                  Date and time at which the multipart upload was initiated.
        
                - **StorageClass** *(string) --* 
        
                  The class of storage used to store the object.
        
                - **Owner** *(dict) --* 
                  
                  - **DisplayName** *(string) --* 
                  
                  - **ID** *(string) --* 
              
                - **Initiator** *(dict) --* 
        
                  Identifies who initiated the multipart upload.
        
                  - **ID** *(string) --* 
        
                    If the principal is an AWS account, it provides the Canonical User ID. If the principal is an IAM User, it provides a user ARN value.
        
                  - **DisplayName** *(string) --* 
        
                    Name of the Principal.
        
            - **CommonPrefixes** *(list) --* 
              
              - *(dict) --* 
                
                - **Prefix** *(string) --* 
            
            - **EncodingType** *(string) --* 
        
              Encoding type used by Amazon S3 to encode object keys in the response.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListObjectVersions(Paginator):
    def paginate(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, Prefix: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListObjectVersions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Bucket=\'string\',
              Delimiter=\'string\',
              EncodingType=\'url\',
              Prefix=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]** 
        
        :type Delimiter: string
        :param Delimiter: 
        
          A delimiter is a character you use to group keys.
        
        :type EncodingType: string
        :param EncodingType: 
        
          Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.
        
        :type Prefix: string
        :param Prefix: 
        
          Limits the response to keys that begin with the specified prefix.
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IsTruncated\': True|False,
                \'KeyMarker\': \'string\',
                \'VersionIdMarker\': \'string\',
                \'Versions\': [
                    {
                        \'ETag\': \'string\',
                        \'Size\': 123,
                        \'StorageClass\': \'STANDARD\',
                        \'Key\': \'string\',
                        \'VersionId\': \'string\',
                        \'IsLatest\': True|False,
                        \'LastModified\': datetime(2015, 1, 1),
                        \'Owner\': {
                            \'DisplayName\': \'string\',
                            \'ID\': \'string\'
                        }
                    },
                ],
                \'DeleteMarkers\': [
                    {
                        \'Owner\': {
                            \'DisplayName\': \'string\',
                            \'ID\': \'string\'
                        },
                        \'Key\': \'string\',
                        \'VersionId\': \'string\',
                        \'IsLatest\': True|False,
                        \'LastModified\': datetime(2015, 1, 1)
                    },
                ],
                \'Name\': \'string\',
                \'Prefix\': \'string\',
                \'Delimiter\': \'string\',
                \'MaxKeys\': 123,
                \'CommonPrefixes\': [
                    {
                        \'Prefix\': \'string\'
                    },
                ],
                \'EncodingType\': \'url\',
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the search criteria. If your results were truncated, you can make a follow-up paginated request using the NextKeyMarker and NextVersionIdMarker response parameters as a starting place in another request to return the rest of the results.
        
            - **KeyMarker** *(string) --* 
        
              Marks the last Key returned in a truncated response.
        
            - **VersionIdMarker** *(string) --* 
            
            - **Versions** *(list) --* 
              
              - *(dict) --* 
                
                - **ETag** *(string) --* 
                
                - **Size** *(integer) --* 
        
                  Size in bytes of the object.
        
                - **StorageClass** *(string) --* 
        
                  The class of storage used to store the object.
        
                - **Key** *(string) --* 
        
                  The object key.
        
                - **VersionId** *(string) --* 
        
                  Version ID of an object.
        
                - **IsLatest** *(boolean) --* 
        
                  Specifies whether the object is (true) or is not (false) the latest version of an object.
        
                - **LastModified** *(datetime) --* 
        
                  Date and time the object was last modified.
        
                - **Owner** *(dict) --* 
                  
                  - **DisplayName** *(string) --* 
                  
                  - **ID** *(string) --* 
              
            - **DeleteMarkers** *(list) --* 
              
              - *(dict) --* 
                
                - **Owner** *(dict) --* 
                  
                  - **DisplayName** *(string) --* 
                  
                  - **ID** *(string) --* 
              
                - **Key** *(string) --* 
        
                  The object key.
        
                - **VersionId** *(string) --* 
        
                  Version ID of an object.
        
                - **IsLatest** *(boolean) --* 
        
                  Specifies whether the object is (true) or is not (false) the latest version of an object.
        
                - **LastModified** *(datetime) --* 
        
                  Date and time the object was last modified.
        
            - **Name** *(string) --* 
            
            - **Prefix** *(string) --* 
            
            - **Delimiter** *(string) --* 
            
            - **MaxKeys** *(integer) --* 
            
            - **CommonPrefixes** *(list) --* 
              
              - *(dict) --* 
                
                - **Prefix** *(string) --* 
            
            - **EncodingType** *(string) --* 
        
              Encoding type used by Amazon S3 to encode object keys in the response.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListObjects(Paginator):
    def paginate(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, Prefix: str = None, RequestPayer: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListObjects>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Bucket=\'string\',
              Delimiter=\'string\',
              EncodingType=\'url\',
              Prefix=\'string\',
              RequestPayer=\'requester\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]** 
        
        :type Delimiter: string
        :param Delimiter: 
        
          A delimiter is a character you use to group keys.
        
        :type EncodingType: string
        :param EncodingType: 
        
          Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some characters, such as characters with an ASCII value from 0 to 10. For characters that are not supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response.
        
        :type Prefix: string
        :param Prefix: 
        
          Limits the response to keys that begin with the specified prefix.
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the list objects request. Bucket owners need not specify this parameter in their requests.
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IsTruncated\': True|False,
                \'Marker\': \'string\',
                \'NextMarker\': \'string\',
                \'Contents\': [
                    {
                        \'Key\': \'string\',
                        \'LastModified\': datetime(2015, 1, 1),
                        \'ETag\': \'string\',
                        \'Size\': 123,
                        \'StorageClass\': \'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'GLACIER\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
                        \'Owner\': {
                            \'DisplayName\': \'string\',
                            \'ID\': \'string\'
                        }
                    },
                ],
                \'Name\': \'string\',
                \'Prefix\': \'string\',
                \'Delimiter\': \'string\',
                \'MaxKeys\': 123,
                \'CommonPrefixes\': [
                    {
                        \'Prefix\': \'string\'
                    },
                ],
                \'EncodingType\': \'url\',
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the search criteria.
        
            - **Marker** *(string) --* 
            
            - **NextMarker** *(string) --* 
        
              When response is truncated (the IsTruncated element value in the response is true), you can use the key name in this field as marker in the subsequent request to get next set of objects. Amazon S3 lists objects in alphabetical order Note: This element is returned only if you have delimiter request parameter specified. If response does not include the NextMaker and it is truncated, you can use the value of the last Key in the response as the marker in the subsequent request to get the next set of object keys.
        
            - **Contents** *(list) --* 
              
              - *(dict) --* 
                
                - **Key** *(string) --* 
                
                - **LastModified** *(datetime) --* 
                
                - **ETag** *(string) --* 
                
                - **Size** *(integer) --* 
                
                - **StorageClass** *(string) --* 
        
                  The class of storage used to store the object.
        
                - **Owner** *(dict) --* 
                  
                  - **DisplayName** *(string) --* 
                  
                  - **ID** *(string) --* 
              
            - **Name** *(string) --* 
            
            - **Prefix** *(string) --* 
            
            - **Delimiter** *(string) --* 
            
            - **MaxKeys** *(integer) --* 
            
            - **CommonPrefixes** *(list) --* 
              
              - *(dict) --* 
                
                - **Prefix** *(string) --* 
            
            - **EncodingType** *(string) --* 
        
              Encoding type used by Amazon S3 to encode object keys in the response.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListObjectsV2(Paginator):
    def paginate(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, Prefix: str = None, FetchOwner: bool = None, StartAfter: str = None, RequestPayer: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListObjectsV2>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Bucket=\'string\',
              Delimiter=\'string\',
              EncodingType=\'url\',
              Prefix=\'string\',
              FetchOwner=True|False,
              StartAfter=\'string\',
              RequestPayer=\'requester\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]** 
        
          Name of the bucket to list.
        
        :type Delimiter: string
        :param Delimiter: 
        
          A delimiter is a character you use to group keys.
        
        :type EncodingType: string
        :param EncodingType: 
        
          Encoding type used by Amazon S3 to encode object keys in the response.
        
        :type Prefix: string
        :param Prefix: 
        
          Limits the response to keys that begin with the specified prefix.
        
        :type FetchOwner: boolean
        :param FetchOwner: 
        
          The owner field is not present in listV2 by default, if you want to return owner field with each key in the result then set the fetch owner field to true
        
        :type StartAfter: string
        :param StartAfter: 
        
          StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified key. StartAfter can be any key in the bucket
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the list objects request in V2 style. Bucket owners need not specify this parameter in their requests.
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IsTruncated\': True|False,
                \'Contents\': [
                    {
                        \'Key\': \'string\',
                        \'LastModified\': datetime(2015, 1, 1),
                        \'ETag\': \'string\',
                        \'Size\': 123,
                        \'StorageClass\': \'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'GLACIER\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
                        \'Owner\': {
                            \'DisplayName\': \'string\',
                            \'ID\': \'string\'
                        }
                    },
                ],
                \'Name\': \'string\',
                \'Prefix\': \'string\',
                \'Delimiter\': \'string\',
                \'MaxKeys\': 123,
                \'CommonPrefixes\': [
                    {
                        \'Prefix\': \'string\'
                    },
                ],
                \'EncodingType\': \'url\',
                \'KeyCount\': 123,
                \'ContinuationToken\': \'string\',
                \'StartAfter\': \'string\',
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the search criteria.
        
            - **Contents** *(list) --* 
        
              Metadata about each object returned.
        
              - *(dict) --* 
                
                - **Key** *(string) --* 
                
                - **LastModified** *(datetime) --* 
                
                - **ETag** *(string) --* 
                
                - **Size** *(integer) --* 
                
                - **StorageClass** *(string) --* 
        
                  The class of storage used to store the object.
        
                - **Owner** *(dict) --* 
                  
                  - **DisplayName** *(string) --* 
                  
                  - **ID** *(string) --* 
              
            - **Name** *(string) --* 
        
              Name of the bucket to list.
        
            - **Prefix** *(string) --* 
        
              Limits the response to keys that begin with the specified prefix.
        
            - **Delimiter** *(string) --* 
        
              A delimiter is a character you use to group keys.
        
            - **MaxKeys** *(integer) --* 
        
              Sets the maximum number of keys returned in the response. The response might contain fewer keys but will never contain more.
        
            - **CommonPrefixes** *(list) --* 
        
              CommonPrefixes contains all (if there are any) keys between Prefix and the next occurrence of the string specified by delimiter
        
              - *(dict) --* 
                
                - **Prefix** *(string) --* 
            
            - **EncodingType** *(string) --* 
        
              Encoding type used by Amazon S3 to encode object keys in the response.
        
            - **KeyCount** *(integer) --* 
        
              KeyCount is the number of keys returned with this request. KeyCount will always be less than equals to MaxKeys field. Say you ask for 50 keys, your result will include less than equals 50 keys 
        
            - **ContinuationToken** *(string) --* 
        
              ContinuationToken indicates Amazon S3 that the list is being continued on this bucket with a token. ContinuationToken is obfuscated and is not a real key
        
            - **StartAfter** *(string) --* 
        
              StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified key. StartAfter can be any key in the bucket
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListParts(Paginator):
    def paginate(self, Bucket: str, Key: str, UploadId: str, RequestPayer: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListParts>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Bucket=\'string\',
              Key=\'string\',
              UploadId=\'string\',
              RequestPayer=\'requester\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]** 
        
        :type Key: string
        :param Key: **[REQUIRED]** 
        
        :type UploadId: string
        :param UploadId: **[REQUIRED]** 
        
          Upload ID identifying the multipart upload whose parts are being listed.
        
        :type RequestPayer: string
        :param RequestPayer: 
        
          Confirms that the requester knows that she or he will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AbortDate\': datetime(2015, 1, 1),
                \'AbortRuleId\': \'string\',
                \'Bucket\': \'string\',
                \'Key\': \'string\',
                \'UploadId\': \'string\',
                \'PartNumberMarker\': 123,
                \'MaxParts\': 123,
                \'IsTruncated\': True|False,
                \'Parts\': [
                    {
                        \'PartNumber\': 123,
                        \'LastModified\': datetime(2015, 1, 1),
                        \'ETag\': \'string\',
                        \'Size\': 123
                    },
                ],
                \'Initiator\': {
                    \'ID\': \'string\',
                    \'DisplayName\': \'string\'
                },
                \'Owner\': {
                    \'DisplayName\': \'string\',
                    \'ID\': \'string\'
                },
                \'StorageClass\': \'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'|\'ONEZONE_IA\',
                \'RequestCharged\': \'requester\',
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AbortDate** *(datetime) --* 
        
              Date when multipart upload will become eligible for abort operation by lifecycle.
        
            - **AbortRuleId** *(string) --* 
        
              Id of the lifecycle rule that makes a multipart upload eligible for abort operation.
        
            - **Bucket** *(string) --* 
        
              Name of the bucket to which the multipart upload was initiated.
        
            - **Key** *(string) --* 
        
              Object key for which the multipart upload was initiated.
        
            - **UploadId** *(string) --* 
        
              Upload ID identifying the multipart upload whose parts are being listed.
        
            - **PartNumberMarker** *(integer) --* 
        
              Part number after which listing begins.
        
            - **MaxParts** *(integer) --* 
        
              Maximum number of parts that were allowed in the response.
        
            - **IsTruncated** *(boolean) --* 
        
              Indicates whether the returned list of parts is truncated.
        
            - **Parts** *(list) --* 
              
              - *(dict) --* 
                
                - **PartNumber** *(integer) --* 
        
                  Part number identifying the part. This is a positive integer between 1 and 10,000.
        
                - **LastModified** *(datetime) --* 
        
                  Date and time at which the part was uploaded.
        
                - **ETag** *(string) --* 
        
                  Entity tag returned when the part was uploaded.
        
                - **Size** *(integer) --* 
        
                  Size of the uploaded part data.
        
            - **Initiator** *(dict) --* 
        
              Identifies who initiated the multipart upload.
        
              - **ID** *(string) --* 
        
                If the principal is an AWS account, it provides the Canonical User ID. If the principal is an IAM User, it provides a user ARN value.
        
              - **DisplayName** *(string) --* 
        
                Name of the Principal.
        
            - **Owner** *(dict) --* 
              
              - **DisplayName** *(string) --* 
              
              - **ID** *(string) --* 
          
            - **StorageClass** *(string) --* 
        
              The class of storage used to store the object.
        
            - **RequestCharged** *(string) --* 
        
              If present, indicates that the requester was successfully charged for the request.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
