from typing import Dict
from botocore.paginate import Paginator


class ListJobs(Paginator):
    def paginate(self, vaultName: str, accountId: str = None, statuscode: str = None, completed: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              vaultName=\'string\',
              statuscode=\'string\',
              completed=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type accountId: string
        :param accountId: 
        
          The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'``-`` \' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID. 
        
            Note: this parameter is set to \"-\" bydefault if no value is not specified.
        
        :type vaultName: string
        :param vaultName: **[REQUIRED]** 
        
          The name of the vault.
        
        :type statuscode: string
        :param statuscode: 
        
          The type of job status to return. You can specify the following values: ``InProgress`` , ``Succeeded`` , or ``Failed`` .
        
        :type completed: string
        :param completed: 
        
          The state of the jobs to return. You can specify ``true`` or ``false`` .
        
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
                \'JobList\': [
                    {
                        \'JobId\': \'string\',
                        \'JobDescription\': \'string\',
                        \'Action\': \'ArchiveRetrieval\'|\'InventoryRetrieval\'|\'Select\',
                        \'ArchiveId\': \'string\',
                        \'VaultARN\': \'string\',
                        \'CreationDate\': \'string\',
                        \'Completed\': True|False,
                        \'StatusCode\': \'InProgress\'|\'Succeeded\'|\'Failed\',
                        \'StatusMessage\': \'string\',
                        \'ArchiveSizeInBytes\': 123,
                        \'InventorySizeInBytes\': 123,
                        \'SNSTopic\': \'string\',
                        \'CompletionDate\': \'string\',
                        \'SHA256TreeHash\': \'string\',
                        \'ArchiveSHA256TreeHash\': \'string\',
                        \'RetrievalByteRange\': \'string\',
                        \'Tier\': \'string\',
                        \'InventoryRetrievalParameters\': {
                            \'Format\': \'string\',
                            \'StartDate\': \'string\',
                            \'EndDate\': \'string\',
                            \'Limit\': \'string\',
                            \'Marker\': \'string\'
                        },
                        \'JobOutputPath\': \'string\',
                        \'SelectParameters\': {
                            \'InputSerialization\': {
                                \'csv\': {
                                    \'FileHeaderInfo\': \'USE\'|\'IGNORE\'|\'NONE\',
                                    \'Comments\': \'string\',
                                    \'QuoteEscapeCharacter\': \'string\',
                                    \'RecordDelimiter\': \'string\',
                                    \'FieldDelimiter\': \'string\',
                                    \'QuoteCharacter\': \'string\'
                                }
                            },
                            \'ExpressionType\': \'SQL\',
                            \'Expression\': \'string\',
                            \'OutputSerialization\': {
                                \'csv\': {
                                    \'QuoteFields\': \'ALWAYS\'|\'ASNEEDED\',
                                    \'QuoteEscapeCharacter\': \'string\',
                                    \'RecordDelimiter\': \'string\',
                                    \'FieldDelimiter\': \'string\',
                                    \'QuoteCharacter\': \'string\'
                                }
                            }
                        },
                        \'OutputLocation\': {
                            \'S3\': {
                                \'BucketName\': \'string\',
                                \'Prefix\': \'string\',
                                \'Encryption\': {
                                    \'EncryptionType\': \'aws:kms\'|\'AES256\',
                                    \'KMSKeyId\': \'string\',
                                    \'KMSContext\': \'string\'
                                },
                                \'CannedACL\': \'private\'|\'public-read\'|\'public-read-write\'|\'aws-exec-read\'|\'authenticated-read\'|\'bucket-owner-read\'|\'bucket-owner-full-control\',
                                \'AccessControlList\': [
                                    {
                                        \'Grantee\': {
                                            \'Type\': \'AmazonCustomerByEmail\'|\'CanonicalUser\'|\'Group\',
                                            \'DisplayName\': \'string\',
                                            \'URI\': \'string\',
                                            \'ID\': \'string\',
                                            \'EmailAddress\': \'string\'
                                        },
                                        \'Permission\': \'FULL_CONTROL\'|\'WRITE\'|\'WRITE_ACP\'|\'READ\'|\'READ_ACP\'
                                    },
                                ],
                                \'Tagging\': {
                                    \'string\': \'string\'
                                },
                                \'UserMetadata\': {
                                    \'string\': \'string\'
                                },
                                \'StorageClass\': \'STANDARD\'|\'REDUCED_REDUNDANCY\'|\'STANDARD_IA\'
                            }
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the Amazon Glacier response to your request.
        
            - **JobList** *(list) --* 
        
              A list of job objects. Each job object contains metadata describing the job.
        
              - *(dict) --* 
        
                Contains the description of an Amazon Glacier job.
        
                - **JobId** *(string) --* 
        
                  An opaque string that identifies an Amazon Glacier job.
        
                - **JobDescription** *(string) --* 
        
                  The job description provided when initiating the job.
        
                - **Action** *(string) --* 
        
                  The job type. This value is either ``ArchiveRetrieval`` , ``InventoryRetrieval`` , or ``Select`` . 
        
                - **ArchiveId** *(string) --* 
        
                  The archive ID requested for a select job or archive retrieval. Otherwise, this field is null.
        
                - **VaultARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the vault from which an archive retrieval was requested.
        
                - **CreationDate** *(string) --* 
        
                  The UTC date when the job was created. This value is a string representation of ISO 8601 date format, for example ``\"2012-03-20T17:03:43.221Z\"`` .
        
                - **Completed** *(boolean) --* 
        
                  The job status. When a job is completed, you get the job\'s output using Get Job Output (GET output).
        
                - **StatusCode** *(string) --* 
        
                  The status code can be ``InProgress`` , ``Succeeded`` , or ``Failed`` , and indicates the status of the job.
        
                - **StatusMessage** *(string) --* 
        
                  A friendly message that describes the job status.
        
                - **ArchiveSizeInBytes** *(integer) --* 
        
                  For an archive retrieval job, this value is the size in bytes of the archive being requested for download. For an inventory retrieval or select job, this value is null.
        
                - **InventorySizeInBytes** *(integer) --* 
        
                  For an inventory retrieval job, this value is the size in bytes of the inventory requested for download. For an archive retrieval or select job, this value is null.
        
                - **SNSTopic** *(string) --* 
        
                  An Amazon SNS topic that receives notification.
        
                - **CompletionDate** *(string) --* 
        
                  The UTC time that the job request completed. While the job is in progress, the value is null.
        
                - **SHA256TreeHash** *(string) --* 
        
                  For an archive retrieval job, this value is the checksum of the archive. Otherwise, this value is null.
        
                  The SHA256 tree hash value for the requested range of an archive. If the **InitiateJob** request for an archive specified a tree-hash aligned range, then this field returns a value.
        
                  If the whole archive is retrieved, this value is the same as the ArchiveSHA256TreeHash value.
        
                  This field is null for the following:
        
                  * Archive retrieval jobs that specify a range that is not tree-hash aligned 
                   
                  * Archival jobs that specify a range that is equal to the whole archive, when the job status is ``InProgress``   
                   
                  * Inventory jobs 
                   
                  * Select jobs 
                   
                - **ArchiveSHA256TreeHash** *(string) --* 
        
                  The SHA256 tree hash of the entire archive for an archive retrieval. For inventory retrieval or select jobs, this field is null.
        
                - **RetrievalByteRange** *(string) --* 
        
                  The retrieved byte range for archive retrieval jobs in the form *StartByteValue* -*EndByteValue* . If no range was specified in the archive retrieval, then the whole archive is retrieved. In this case, *StartByteValue* equals 0 and *EndByteValue* equals the size of the archive minus 1. For inventory retrieval or select jobs, this field is null. 
        
                - **Tier** *(string) --* 
        
                  The tier to use for a select or an archive retrieval. Valid values are ``Expedited`` , ``Standard`` , or ``Bulk`` . ``Standard`` is the default.
        
                - **InventoryRetrievalParameters** *(dict) --* 
        
                  Parameters used for range inventory retrieval.
        
                  - **Format** *(string) --* 
        
                    The output format for the vault inventory list, which is set by the **InitiateJob** request when initiating a job to retrieve a vault inventory. Valid values are ``CSV`` and ``JSON`` .
        
                  - **StartDate** *(string) --* 
        
                    The start of the date range in Universal Coordinated Time (UTC) for vault inventory retrieval that includes archives created on or after this date. This value should be a string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .
        
                  - **EndDate** *(string) --* 
        
                    The end of the date range in UTC for vault inventory retrieval that includes archives created before this date. This value should be a string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .
        
                  - **Limit** *(string) --* 
        
                    The maximum number of inventory items returned per vault inventory retrieval request. This limit is set when initiating the job with the a **InitiateJob** request. 
        
                  - **Marker** *(string) --* 
        
                    An opaque string that represents where to continue pagination of the vault inventory retrieval results. You use the marker in a new **InitiateJob** request to obtain additional inventory items. If there are no more inventory items, this value is ``null`` . For more information, see `Range Inventory Retrieval <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering>`__ .
        
                - **JobOutputPath** *(string) --* 
        
                  Contains the job output location.
        
                - **SelectParameters** *(dict) --* 
        
                  Contains the parameters used for a select.
        
                  - **InputSerialization** *(dict) --* 
        
                    Describes the serialization format of the object.
        
                    - **csv** *(dict) --* 
        
                      Describes the serialization of a CSV-encoded object.
        
                      - **FileHeaderInfo** *(string) --* 
        
                        Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and ``Use`` .
        
                      - **Comments** *(string) --* 
        
                        A single character used to indicate that a row should be ignored when the character is present at the start of that row.
        
                      - **QuoteEscapeCharacter** *(string) --* 
        
                        A single character used for escaping the quotation-mark character inside an already escaped value.
        
                      - **RecordDelimiter** *(string) --* 
        
                        A value used to separate individual records from each other.
        
                      - **FieldDelimiter** *(string) --* 
        
                        A value used to separate individual fields from each other within a record.
        
                      - **QuoteCharacter** *(string) --* 
        
                        A value used as an escape character where the field delimiter is part of the value.
        
                  - **ExpressionType** *(string) --* 
        
                    The type of the provided expression, for example ``SQL`` .
        
                  - **Expression** *(string) --* 
        
                    The expression that is used to select the object.
        
                  - **OutputSerialization** *(dict) --* 
        
                    Describes how the results of the select job are serialized.
        
                    - **csv** *(dict) --* 
        
                      Describes the serialization of CSV-encoded query results.
        
                      - **QuoteFields** *(string) --* 
        
                        A value that indicates whether all output fields should be contained within quotation marks.
        
                      - **QuoteEscapeCharacter** *(string) --* 
        
                        A single character used for escaping the quotation-mark character inside an already escaped value.
        
                      - **RecordDelimiter** *(string) --* 
        
                        A value used to separate individual records from each other.
        
                      - **FieldDelimiter** *(string) --* 
        
                        A value used to separate individual fields from each other within a record.
        
                      - **QuoteCharacter** *(string) --* 
        
                        A value used as an escape character where the field delimiter is part of the value.
        
                - **OutputLocation** *(dict) --* 
        
                  Contains the location where the data from the select job is stored.
        
                  - **S3** *(dict) --* 
        
                    Describes an S3 location that will receive the results of the job request.
        
                    - **BucketName** *(string) --* 
        
                      The name of the Amazon S3 bucket where the job results are stored.
        
                    - **Prefix** *(string) --* 
        
                      The prefix that is prepended to the results for this request.
        
                    - **Encryption** *(dict) --* 
        
                      Contains information about the encryption used to store the job results in Amazon S3.
        
                      - **EncryptionType** *(string) --* 
        
                        The server-side encryption algorithm used when storing job results in Amazon S3, for example ``AES256`` or ``aws:kms`` .
        
                      - **KMSKeyId** *(string) --* 
        
                        The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature Version 4. 
        
                      - **KMSContext** *(string) --* 
        
                        Optional. If the encryption type is ``aws:kms`` , you can use this value to specify the encryption context for the job results.
        
                    - **CannedACL** *(string) --* 
        
                      The canned access control list (ACL) to apply to the job results.
        
                    - **AccessControlList** *(list) --* 
        
                      A list of grants that control access to the staged results.
        
                      - *(dict) --* 
        
                        Contains information about a grant.
        
                        - **Grantee** *(dict) --* 
        
                          The grantee.
        
                          - **Type** *(string) --* 
        
                            Type of grantee
        
                          - **DisplayName** *(string) --* 
        
                            Screen name of the grantee.
        
                          - **URI** *(string) --* 
        
                            URI of the grantee group.
        
                          - **ID** *(string) --* 
        
                            The canonical user ID of the grantee.
        
                          - **EmailAddress** *(string) --* 
        
                            Email address of the grantee.
        
                        - **Permission** *(string) --* 
        
                          Specifies the permission given to the grantee. 
        
                    - **Tagging** *(dict) --* 
        
                      The tag-set that is applied to the job results.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
                    - **UserMetadata** *(dict) --* 
        
                      A map of metadata to store with the job results in Amazon S3.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
                    - **StorageClass** *(string) --* 
        
                      The storage class used to store the job results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListMultipartUploads(Paginator):
    def paginate(self, vaultName: str, accountId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListMultipartUploads>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              vaultName=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type accountId: string
        :param accountId: 
        
          The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'``-`` \' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID. 
        
            Note: this parameter is set to \"-\" bydefault if no value is not specified.
        
        :type vaultName: string
        :param vaultName: **[REQUIRED]** 
        
          The name of the vault.
        
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
                \'UploadsList\': [
                    {
                        \'MultipartUploadId\': \'string\',
                        \'VaultARN\': \'string\',
                        \'ArchiveDescription\': \'string\',
                        \'PartSizeInBytes\': 123,
                        \'CreationDate\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the Amazon Glacier response to your request.
        
            - **UploadsList** *(list) --* 
        
              A list of in-progress multipart uploads.
        
              - *(dict) --* 
        
                A list of in-progress multipart uploads for a vault.
        
                - **MultipartUploadId** *(string) --* 
        
                  The ID of a multipart upload.
        
                - **VaultARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the vault that contains the archive.
        
                - **ArchiveDescription** *(string) --* 
        
                  The description of the archive that was specified in the Initiate Multipart Upload request.
        
                - **PartSizeInBytes** *(integer) --* 
        
                  The part size, in bytes, specified in the Initiate Multipart Upload request. This is the size of all the parts in the upload except the last part, which may be smaller than this size.
        
                - **CreationDate** *(string) --* 
        
                  The UTC time at which the multipart upload was initiated.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListParts(Paginator):
    def paginate(self, vaultName: str, uploadId: str, accountId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListParts>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              vaultName=\'string\',
              uploadId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type accountId: string
        :param accountId: 
        
          The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single \'``-`` \' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (\'-\') in the ID. 
        
            Note: this parameter is set to \"-\" bydefault if no value is not specified.
        
        :type vaultName: string
        :param vaultName: **[REQUIRED]** 
        
          The name of the vault.
        
        :type uploadId: string
        :param uploadId: **[REQUIRED]** 
        
          The upload ID of the multipart upload.
        
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
                \'MultipartUploadId\': \'string\',
                \'VaultARN\': \'string\',
                \'ArchiveDescription\': \'string\',
                \'PartSizeInBytes\': 123,
                \'CreationDate\': \'string\',
                \'Parts\': [
                    {
                        \'RangeInBytes\': \'string\',
                        \'SHA256TreeHash\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the Amazon Glacier response to your request.
        
            - **MultipartUploadId** *(string) --* 
        
              The ID of the upload to which the parts are associated.
        
            - **VaultARN** *(string) --* 
        
              The Amazon Resource Name (ARN) of the vault to which the multipart upload was initiated.
        
            - **ArchiveDescription** *(string) --* 
        
              The description of the archive that was specified in the Initiate Multipart Upload request.
        
            - **PartSizeInBytes** *(integer) --* 
        
              The part size in bytes. This is the same value that you specified in the Initiate Multipart Upload request.
        
            - **CreationDate** *(string) --* 
        
              The UTC time at which the multipart upload was initiated.
        
            - **Parts** *(list) --* 
        
              A list of the part sizes of the multipart upload. Each object in the array contains a ``RangeBytes`` and ``sha256-tree-hash`` name/value pair.
        
              - *(dict) --* 
        
                A list of the part sizes of the multipart upload.
        
                - **RangeInBytes** *(string) --* 
        
                  The byte range of a part, inclusive of the upper value of the range.
        
                - **SHA256TreeHash** *(string) --* 
        
                  The SHA256 tree hash value that Amazon Glacier calculated for the part. This field is never ``null`` .
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListVaults(Paginator):
    def paginate(self, accountId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type accountId: string
        :param accountId: 
        
          The ``AccountId`` value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single \'``-`` \' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (\'-\') in the ID.
        
            Note: this parameter is set to \"-\" bydefault if no value is not specified.
        
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
                \'VaultList\': [
                    {
                        \'VaultARN\': \'string\',
                        \'VaultName\': \'string\',
                        \'CreationDate\': \'string\',
                        \'LastInventoryDate\': \'string\',
                        \'NumberOfArchives\': 123,
                        \'SizeInBytes\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the Amazon Glacier response to your request.
        
            - **VaultList** *(list) --* 
        
              List of vaults.
        
              - *(dict) --* 
        
                Contains the Amazon Glacier response to your request.
        
                - **VaultARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the vault.
        
                - **VaultName** *(string) --* 
        
                  The name of the vault.
        
                - **CreationDate** *(string) --* 
        
                  The Universal Coordinated Time (UTC) date when the vault was created. This value should be a string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .
        
                - **LastInventoryDate** *(string) --* 
        
                  The Universal Coordinated Time (UTC) date when Amazon Glacier completed the last vault inventory. This value should be a string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .
        
                - **NumberOfArchives** *(integer) --* 
        
                  The number of archives in the vault as of the last inventory date. This field will return ``null`` if an inventory has not yet run on the vault, for example if you just created the vault.
        
                - **SizeInBytes** *(integer) --* 
        
                  Total size, in bytes, of the archives in the vault as of the last inventory date. This field will return null if an inventory has not yet run on the vault, for example if you just created the vault.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
