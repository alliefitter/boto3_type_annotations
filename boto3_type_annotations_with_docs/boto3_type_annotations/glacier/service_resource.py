from typing import Optional
from typing import Union
from boto3.resources.collection import ResourceCollection
from typing import List
from typing import Dict
from typing import IO
from boto3.resources import base


class ServiceResource(base.ServiceResource):
    vaults: 'vaults'

    def Account(self, id: str = None) -> 'Account':
        """
        Creates a Account resource.::
        
          account = glacier.Account(\'id\')
        
        :type id: string
        :param id: The Account\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`Glacier.Account`
        :returns: A Account resource
        """
        pass

    def Archive(self, account_id: str = None, vault_name: str = None, id: str = None) -> 'Archive':
        """
        Creates a Archive resource.::
        
          archive = glacier.Archive(\'account_id\',\'vault_name\',\'id\')
        
        :type account_id: string
        :param account_id: The Archive\'s account_id identifier. This **must** be set.
        :type vault_name: string
        :param vault_name: The Archive\'s vault_name identifier. This **must** be set.
        :type id: string
        :param id: The Archive\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`Glacier.Archive`
        :returns: A Archive resource
        """
        pass

    def Job(self, account_id: str = None, vault_name: str = None, id: str = None) -> 'Job':
        """
        Creates a Job resource.::
        
          job = glacier.Job(\'account_id\',\'vault_name\',\'id\')
        
        :type account_id: string
        :param account_id: The Job\'s account_id identifier. This **must** be set.
        :type vault_name: string
        :param vault_name: The Job\'s vault_name identifier. This **must** be set.
        :type id: string
        :param id: The Job\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`Glacier.Job`
        :returns: A Job resource
        """
        pass

    def MultipartUpload(self, account_id: str = None, vault_name: str = None, id: str = None) -> 'MultipartUpload':
        """
        Creates a MultipartUpload resource.::
        
          multipart_upload = glacier.MultipartUpload(\'account_id\',\'vault_name\',\'id\')
        
        :type account_id: string
        :param account_id: The MultipartUpload\'s account_id identifier. This **must** be set.
        :type vault_name: string
        :param vault_name: The MultipartUpload\'s vault_name identifier. This **must** be set.
        :type id: string
        :param id: The MultipartUpload\'s id identifier. This **must** be set.
        
        :rtype: :py:class:`Glacier.MultipartUpload`
        :returns: A MultipartUpload resource
        """
        pass

    def Notification(self, account_id: str = None, vault_name: str = None) -> 'Notification':
        """
        Creates a Notification resource.::
        
          notification = glacier.Notification(\'account_id\',\'vault_name\')
        
        :type account_id: string
        :param account_id: The Notification\'s account_id identifier. This **must** be set.
        :type vault_name: string
        :param vault_name: The Notification\'s vault_name identifier. This **must** be set.
        
        :rtype: :py:class:`Glacier.Notification`
        :returns: A Notification resource
        """
        pass

    def Vault(self, account_id: str = None, name: str = None) -> 'Vault':
        """
        Creates a Vault resource.::
        
          vault = glacier.Vault(\'account_id\',\'name\')
        
        :type account_id: string
        :param account_id: The Vault\'s account_id identifier. This **must** be set.
        :type name: string
        :param name: The Vault\'s name identifier. This **must** be set.
        
        :rtype: :py:class:`Glacier.Vault`
        :returns: A Vault resource
        """
        pass

    def create_vault(self, vaultName: str) -> 'Vault':
        """
        
        You must use the following guidelines when naming a vault.
        
        * Names can be between 1 and 255 characters long. 
         
        * Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (hyphen), and \'.\' (period). 
         
        This operation is idempotent.
        
        An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .
        
        For conceptual information and underlying REST API, see `Creating a Vault in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults.html>`__ and `Create Vault <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-put.html>`__ in the *Amazon Glacier Developer Guide* . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/CreateVault>`_
        
        **Request Syntax** 
        ::
        
          vault = glacier.create_vault(
              vaultName=\'string\'
          )
        :type vaultName: string
        :param vaultName: **[REQUIRED]** 
        
          The name of the vault.
        
        :rtype: :py:class:`glacier.Vault`
        :returns: Vault resource
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


class Account(base.ServiceResource):
    id: str
    vaults: 'vaults'

    def create_vault(self, vaultName: str) -> 'Vault':
        """
        
        You must use the following guidelines when naming a vault.
        
        * Names can be between 1 and 255 characters long. 
         
        * Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (hyphen), and \'.\' (period). 
         
        This operation is idempotent.
        
        An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .
        
        For conceptual information and underlying REST API, see `Creating a Vault in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults.html>`__ and `Create Vault <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-put.html>`__ in the *Amazon Glacier Developer Guide* . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/CreateVault>`_
        
        **Request Syntax** 
        ::
        
          vault = account.create_vault(
              vaultName=\'string\'
          )
        :type vaultName: string
        :param vaultName: **[REQUIRED]** 
        
          The name of the vault.
        
        :rtype: :py:class:`glacier.Vault`
        :returns: Vault resource
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


class Archive(base.ServiceResource):
    account_id: str
    vault_name: str
    id: str

    def delete(self):
        """
        This operation deletes an archive from a vault. Subsequent requests to initiate a retrieval of this archive will fail. Archive retrievals that are in progress for this archive ID may or may not succeed according to the following scenarios:
        
        * If the archive retrieval job is actively preparing the data for download when Amazon Glacier receives the delete archive request, the archival retrieval operation might fail. 
         
        * If the archive retrieval job has successfully prepared the archive for download when Amazon Glacier receives the delete archive request, you will be able to download the output. 
         
        This operation is idempotent. Attempting to delete an already-deleted archive does not result in an error.
        
        An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .
        
        For conceptual information and underlying REST API, see `Deleting an Archive in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive.html>`__ and `Delete Archive <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-delete.html>`__ in the *Amazon Glacier Developer Guide* . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DeleteArchive>`_
        
        **Request Syntax** 
        ::
        
          response = archive.delete()
          
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

    def initiate_archive_retrieval(self) -> 'Job':
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/InitiateJob>`_
        
        **Request Syntax** 
        ::
        
          job = archive.initiate_archive_retrieval()
          
        :rtype: :py:class:`glacier.Job`
        :returns: Job resource
        """
        pass


class Job(base.ServiceResource):
    job_id: str
    job_description: str
    action: str
    archive_id: str
    vault_arn: str
    creation_date: str
    completed: bool
    status_code: str
    status_message: str
    archive_size_in_bytes: int
    inventory_size_in_bytes: int
    sns_topic: str
    completion_date: str
    sha256_tree_hash: str
    archive_sha256_tree_hash: str
    retrieval_byte_range: str
    tier: str
    inventory_retrieval_parameters: Dict
    job_output_path: str
    select_parameters: Dict
    output_location: Dict
    account_id: str
    vault_name: str
    id: str

    def get_available_subresources(self) -> List[str]:
        """
        Resource.
        
        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """
        pass

    def get_output(self, range: str = None) -> Dict:
        """
        
        You can download all the job output or download a portion of the output by specifying a byte range. In the case of an archive retrieval job, depending on the byte range you specify, Amazon Glacier returns the checksum for the portion of the data. You can compute the checksum on the client and verify that the values match to ensure the portion you downloaded is the correct data.
        
        A job ID will not expire for at least 24 hours after Amazon Glacier completes the job. That a byte range. For both archive and inventory retrieval jobs, you should verify the downloaded size against the size returned in the headers from the **Get Job Output** response.
        
        For archive retrieval jobs, you should also verify that the size is what you expected. If you download a portion of the output, the expected size is based on the range of bytes you specified. For example, if you specify a range of ``bytes=0-1048575`` , you should verify your download size is 1,048,576 bytes. If you download an entire archive, the expected size is the size of the archive when you uploaded it to Amazon Glacier The expected size is also returned in the headers from the **Get Job Output** response.
        
        In the case of an archive retrieval job, depending on the byte range you specify, Amazon Glacier returns the checksum for the portion of the data. To ensure the portion you downloaded is the correct data, compute the checksum on the client, verify that the values match, and verify that the size is what you expected.
        
        A job ID does not expire for at least 24 hours after Amazon Glacier completes the job. That is, you can download the job output within the 24 hours period after Amazon Glacier completes the job.
        
        An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .
        
        For conceptual information and the underlying REST API, see `Downloading a Vault Inventory <http://docs.aws.amazon.com/amazonglacier/latest/dev/vault-inventory.html>`__ , `Downloading an Archive <http://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive.html>`__ , and `Get Job Output <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-job-output-get.html>`__  
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/GetJobOutput>`_
        
        **Request Syntax** 
        ::
        
          response = job.get_output(
              range=\'string\'
          )
        :type range: string
        :param range: 
        
          The range of bytes to retrieve from the output. For example, if you want to download the first 1,048,576 bytes, specify the range as ``bytes=0-1048575`` . By default, this operation downloads the entire output.
        
          If the job output is large, then you can use a range to retrieve a portion of the output. This allows you to download the entire output in smaller chunks of bytes. For example, suppose you have 1 GB of job output you want to download and you decide to download 128 MB chunks of data at a time, which is a total of eight Get Job Output requests. You use the following process to download the job output:
        
          * Download a 128 MB chunk of output by specifying the appropriate byte range. Verify that all 128 MB of data was received. 
           
          * Along with the data, the response includes a SHA256 tree hash of the payload. You compute the checksum of the payload on the client and compare it with the checksum you received in the response to ensure you received all the expected data. 
           
          * Repeat steps 1 and 2 for all the eight 128 MB chunks of output data, each time specifying the appropriate byte range. 
           
          * After downloading all the parts of the job output, you have a list of eight checksum values. Compute the tree hash of these values to find the checksum of the entire output. Using the  DescribeJob API, obtain job information of the job that provided you the output. The response includes the checksum of the entire archive stored in Amazon Glacier. You compare this value with the checksum you computed to ensure you have downloaded the entire archive content with no errors.  
           
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'body\': StreamingBody(),
                \'checksum\': \'string\',
                \'status\': 123,
                \'contentRange\': \'string\',
                \'acceptRanges\': \'string\',
                \'contentType\': \'string\',
                \'archiveDescription\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the Amazon Glacier response to your request.
        
            - **body** (:class:`.StreamingBody`) -- 
        
              The job data, either archive data or inventory data.
        
            - **checksum** *(string) --* 
        
              The checksum of the data in the response. This header is returned only when retrieving the output for an archive retrieval job. Furthermore, this header appears only under the following conditions:
        
              * You get the entire range of the archive. 
               
              * You request a range to return of the archive that starts and ends on a multiple of 1 MB. For example, if you have an 3.1 MB archive and you specify a range to return that starts at 1 MB and ends at 2 MB, then the x-amz-sha256-tree-hash is returned as a response header. 
               
              * You request a range of the archive to return that starts on a multiple of 1 MB and goes to the end of the archive. For example, if you have a 3.1 MB archive and you specify a range that starts at 2 MB and ends at 3.1 MB (the end of the archive), then the x-amz-sha256-tree-hash is returned as a response header. 
               
            - **status** *(integer) --* 
        
              The HTTP response code for a job output request. The value depends on whether a range was specified in the request.
        
            - **contentRange** *(string) --* 
        
              The range of bytes returned by Amazon Glacier. If only partial output is downloaded, the response provides the range of bytes Amazon Glacier returned. For example, bytes 0-1048575/8388608 returns the first 1 MB from 8 MB.
        
            - **acceptRanges** *(string) --* 
        
              Indicates the range units accepted. For more information, see `RFC2616 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`__ . 
        
            - **contentType** *(string) --* 
        
              The Content-Type depends on whether the job output is an archive or a vault inventory. For archive data, the Content-Type is application/octet-stream. For vault inventory, if you requested CSV format when you initiated the job, the Content-Type is text/csv. Otherwise, by default, vault inventory is returned as JSON, and the Content-Type is application/json.
        
            - **archiveDescription** *(string) --* 
        
              The description of an archive.
        
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          job.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          job.load()
        :returns: None
        """
        pass


class MultipartUpload(base.ServiceResource):
    multipart_upload_id: str
    vault_arn: str
    archive_description: str
    part_size_in_bytes: int
    creation_date: str
    account_id: str
    vault_name: str
    id: str

    def abort(self):
        """
        
        After the Abort Multipart Upload request succeeds, you cannot upload any more parts to the multipart upload or complete the multipart upload. Aborting a completed upload fails. However, aborting an already-aborted upload will succeed, for a short time. For more information about uploading a part and completing a multipart upload, see  UploadMultipartPart and  CompleteMultipartUpload .
        
        This operation is idempotent.
        
        An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .
        
        For conceptual information and underlying REST API, see `Working with Archives in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ and `Abort Multipart Upload <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-abort-upload.html>`__ in the *Amazon Glacier Developer Guide* . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/AbortMultipartUpload>`_
        
        **Request Syntax** 
        ::
        
          response = multipart_upload.abort()
          
        :returns: None
        """
        pass

    def complete(self, archiveSize: str = None, checksum: str = None) -> Dict:
        """
        
        In the request, you must include the computed SHA256 tree hash of the entire archive you have uploaded. For information about computing a SHA256 tree hash, see `Computing Checksums <http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html>`__ . On the server side, Amazon Glacier also constructs the SHA256 tree hash of the assembled archive. If the values match, Amazon Glacier saves the archive to the vault; otherwise, it returns an error, and the operation fails. The  ListParts operation returns a list of parts uploaded for a specific multipart upload. It includes checksum information for each uploaded part that can be used to debug a bad checksum issue.
        
        Additionally, Amazon Glacier also checks for any missing content ranges when assembling the archive, if missing content ranges are found, Amazon Glacier returns an error and the operation fails.
        
        Complete Multipart Upload is an idempotent operation. After your first successful complete multipart upload, if you call the operation again within a short period, the operation will succeed and return the same archive ID. This is useful in the event you experience a network issue that causes an aborted connection or receive a 500 server error, in which case you can repeat your Complete Multipart Upload request and get the same archive ID without creating duplicate archives. Note, however, that after the multipart upload completes, you cannot call the List Parts operation and the multipart upload will not appear in List Multipart Uploads response, even if idempotent complete is possible.
        
        An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .
        
        For conceptual information and underlying REST API, see `Uploading Large Archives in Parts (Multipart Upload) <http://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html>`__ and `Complete Multipart Upload <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-complete-upload.html>`__ in the *Amazon Glacier Developer Guide* . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/CompleteMultipartUpload>`_
        
        **Request Syntax** 
        ::
        
          response = multipart_upload.complete(
              archiveSize=\'string\',
              checksum=\'string\'
          )
        :type archiveSize: string
        :param archiveSize: 
        
          The total size, in bytes, of the entire archive. This value should be the sum of all the sizes of the individual parts that you uploaded.
        
        :type checksum: string
        :param checksum: 
        
          The SHA256 tree hash of the entire archive. It is the tree hash of SHA256 tree hash of the individual parts. If the value you specify in the request does not match the SHA256 tree hash of the final assembled archive as computed by Amazon Glacier, Amazon Glacier returns an error and the request fails.
        
                This is a required field.
        
                Ideally you will want to compute this value with checksums from
                previous uploaded parts, using the algorithm described in
                `Glacier documentation <http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html>`_.
        
                But if you prefer, you can also use botocore.utils.calculate_tree_hash()
                to compute it from raw file by::
        
                    checksum = calculate_tree_hash(open(\'your_file.txt\', \'rb\'))
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'location\': \'string\',
                \'checksum\': \'string\',
                \'archiveId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the Amazon Glacier response to your request.
        
            For information about the underlying REST API, see `Upload Archive <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html>`__ . For conceptual information, see `Working with Archives in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ .
        
            - **location** *(string) --* 
        
              The relative URI path of the newly added archive resource.
        
            - **checksum** *(string) --* 
        
              The checksum of the archive computed by Amazon Glacier.
        
            - **archiveId** *(string) --* 
        
              The ID of the archive. This value is also included as part of the location.
        
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

    def parts(self, marker: str = None, limit: str = None) -> Dict:
        """
        
        The List Parts operation supports pagination. By default, this operation returns up to 50 uploaded parts in the response. You should always check the response for a ``marker`` at which to continue the list; if there are no more items the ``marker`` is ``null`` . To return a list of parts that begins at a specific part, set the ``marker`` request parameter to the value you obtained from a previous List Parts request. You can also limit the number of parts returned in the response by specifying the ``limit`` parameter in the request. 
        
        An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .
        
        For conceptual information and the underlying REST API, see `Working with Archives in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ and `List Parts <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-list-parts.html>`__ in the *Amazon Glacier Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListParts>`_
        
        **Request Syntax** 
        ::
        
          response = multipart_upload.parts(
              marker=\'string\',
              limit=\'string\'
          )
        :type marker: string
        :param marker: 
        
          An opaque string used for pagination. This value specifies the part at which the listing of parts should begin. Get the marker value from the response of a previous List Parts response. You need only include the marker if you are continuing the pagination of results started in a previous List Parts request.
        
        :type limit: string
        :param limit: 
        
          The maximum number of parts to be returned. The default limit is 50. The number of parts returned might be fewer than the specified limit, but the number of returned parts never exceeds the limit.
        
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
                \'Marker\': \'string\'
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
        
            - **Marker** *(string) --* 
        
              An opaque string that represents where to continue pagination of the results. You use the marker in a new List Parts request to obtain more jobs in the list. If there are no more parts, this value is ``null`` .
        
        """
        pass

    def upload_part(self, checksum: str = None, range: str = None, body: Union[bytes, IO] = None) -> Dict:
        """
        
        Amazon Glacier rejects your upload part request if any of the following conditions is true:
        
        * **SHA256 tree hash does not match** To ensure that part data is not corrupted in transmission, you compute a SHA256 tree hash of the part and include it in your request. Upon receiving the part data, Amazon Glacier also computes a SHA256 tree hash. If these hash values don\'t match, the operation fails. For information about computing a SHA256 tree hash, see `Computing Checksums <http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html>`__ . 
         
        * **Part size does not match** The size of each part except the last must match the size specified in the corresponding  InitiateMultipartUpload request. The size of the last part must be the same size as, or smaller than, the specified size. 
        
        .. note::
        
           If you upload a part whose size is smaller than the part size you specified in your initiate multipart upload request and that part is not the last part, then the upload part request will succeed. However, the subsequent Complete Multipart Upload request will fail. 
        
        * **Range does not align** The byte range value in the request does not align with the part size specified in the corresponding initiate request. For example, if you specify a part size of 4194304 bytes (4 MB), then 0 to 4194303 bytes (4 MB - 1) and 4194304 (4 MB) to 8388607 (8 MB - 1) are valid part ranges. However, if you set a range value of 2 MB to 6 MB, the range does not align with the part size and the upload will fail.  
         
        This operation is idempotent. If you upload the same part multiple times, the data included in the most recent request overwrites the previously uploaded data.
        
        An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .
        
        For conceptual information and underlying REST API, see `Uploading Large Archives in Parts (Multipart Upload) <http://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html>`__ and `Upload Part <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-upload-part.html>`__ in the *Amazon Glacier Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/UploadMultipartPart>`_
        
        **Request Syntax** 
        ::
        
          response = multipart_upload.upload_part(
              range=\'string\',
              body=b\'bytes\'|file
          )
        :type checksum: string
        :param checksum: 
        
          The SHA256 tree hash of the data being uploaded.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type range: string
        :param range: 
        
          Identifies the range of bytes in the assembled archive that will be uploaded in this part. Amazon Glacier uses this information to assemble the archive in the proper sequence. The format of this header follows RFC 2616. An example header is Content-Range:bytes 0-4194303/*.
        
        :type body: bytes or seekable file-like object
        :param body: 
        
          The data to upload.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'checksum\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the Amazon Glacier response to your request.
        
            - **checksum** *(string) --* 
        
              The SHA256 tree hash that Amazon Glacier computed for the uploaded part.
        
        """
        pass


class Notification(base.ServiceResource):
    sns_topic: str
    events: List
    account_id: str
    vault_name: str

    def delete(self):
        """
        
        An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .
        
        For conceptual information and underlying REST API, see `Configuring Vault Notifications in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html>`__ and `Delete Vault Notification Configuration <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-delete.html>`__ in the Amazon Glacier Developer Guide. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DeleteVaultNotifications>`_
        
        **Request Syntax** 
        ::
        
          response = notification.delete()
          
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

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          notification.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          notification.load()
        :returns: None
        """
        pass

    def set(self, vaultNotificationConfig: Dict = None):
        """
        
        To configure vault notifications, send a PUT request to the ``notification-configuration`` subresource of the vault. The request should include a JSON document that provides an Amazon SNS topic and specific events for which you want Amazon Glacier to send notifications to the topic.
        
        Amazon SNS topics must grant permission to the vault to be allowed to publish notifications to the topic. You can configure a vault to publish a notification for the following vault events:
        
        * **ArchiveRetrievalCompleted** This event occurs when a job that was initiated for an archive retrieval is completed ( InitiateJob ). The status of the completed job can be \"Succeeded\" or \"Failed\". The notification sent to the SNS topic is the same output as returned from  DescribeJob .  
         
        * **InventoryRetrievalCompleted** This event occurs when a job that was initiated for an inventory retrieval is completed ( InitiateJob ). The status of the completed job can be \"Succeeded\" or \"Failed\". The notification sent to the SNS topic is the same output as returned from  DescribeJob .  
         
        An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .
        
        For conceptual information and underlying REST API, see `Configuring Vault Notifications in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html>`__ and `Set Vault Notification Configuration <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-put.html>`__ in the *Amazon Glacier Developer Guide* . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/SetVaultNotifications>`_
        
        **Request Syntax** 
        ::
        
          response = notification.set(
              vaultNotificationConfig={
                  \'SNSTopic\': \'string\',
                  \'Events\': [
                      \'string\',
                  ]
              }
          )
        :type vaultNotificationConfig: dict
        :param vaultNotificationConfig: 
        
          Provides options for specifying notification configuration.
        
          - **SNSTopic** *(string) --* 
        
            The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).
        
          - **Events** *(list) --* 
        
            A list of one or more events for which Amazon Glacier will send a notification to the specified Amazon SNS topic.
        
            - *(string) --* 
        
        :returns: None
        """
        pass


class Vault(base.ServiceResource):
    vault_arn: str
    vault_name: str
    creation_date: str
    last_inventory_date: str
    number_of_archives: int
    size_in_bytes: int
    account_id: str
    name: str
    completed_jobs: 'completed_jobs'
    failed_jobs: 'failed_jobs'
    jobs: 'jobs'
    jobs_in_progress: 'jobs_in_progress'
    multipart_uplaods: 'multipart_uplaods'
    multipart_uploads: 'multipart_uploads'
    succeeded_jobs: 'succeeded_jobs'

    def create(self) -> Dict:
        """
        
        You must use the following guidelines when naming a vault.
        
        * Names can be between 1 and 255 characters long. 
         
        * Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (hyphen), and \'.\' (period). 
         
        This operation is idempotent.
        
        An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .
        
        For conceptual information and underlying REST API, see `Creating a Vault in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults.html>`__ and `Create Vault <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-put.html>`__ in the *Amazon Glacier Developer Guide* . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/CreateVault>`_
        
        **Request Syntax** 
        ::
        
          response = vault.create()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'location\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the Amazon Glacier response to your request.
        
            - **location** *(string) --* 
        
              The URI of the vault that was created.
        
        """
        pass

    def delete(self):
        """
        
        This operation is idempotent.
        
        An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .
        
        For conceptual information and underlying REST API, see `Deleting a Vault in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-vaults.html>`__ and `Delete Vault <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-delete.html>`__ in the *Amazon Glacier Developer Guide* . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DeleteVault>`_
        
        **Request Syntax** 
        ::
        
          response = vault.delete()
          
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

    def initiate_inventory_retrieval(self) -> 'Job':
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/InitiateJob>`_
        
        **Request Syntax** 
        ::
        
          job = vault.initiate_inventory_retrieval()
          
        :rtype: :py:class:`glacier.Job`
        :returns: Job resource
        """
        pass

    def initiate_multipart_upload(self, archiveDescription: str = None, partSize: str = None) -> 'MultipartUpload':
        """
        
        When you initiate a multipart upload, you specify the part size in number of bytes. The part size must be a megabyte (1024 KB) multiplied by a power of 2-for example, 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB.
        
        Every part you upload to this resource (see  UploadMultipartPart ), except the last one, must have the same size. The last one can be the same size or smaller. For example, suppose you want to upload a 16.2 MB file. If you initiate the multipart upload with a part size of 4 MB, you will upload four parts of 4 MB each and one part of 0.2 MB. 
        
        .. note::
        
          You don\'t need to know the size of the archive when you start a multipart upload because Amazon Glacier does not require you to specify the overall archive size.
        
        After you complete the multipart upload, Amazon Glacier removes the multipart upload resource referenced by the ID. Amazon Glacier also removes the multipart upload resource if you cancel the multipart upload or it may be removed if there is no activity for a period of 24 hours.
        
        An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .
        
        For conceptual information and underlying REST API, see `Uploading Large Archives in Parts (Multipart Upload) <http://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html>`__ and `Initiate Multipart Upload <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-initiate-upload.html>`__ in the *Amazon Glacier Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/InitiateMultipartUpload>`_
        
        **Request Syntax** 
        ::
        
          multipart_upload = vault.initiate_multipart_upload(
              archiveDescription=\'string\',
              partSize=\'string\'
          )
        :type archiveDescription: string
        :param archiveDescription: 
        
          The archive description that you are uploading in parts.
        
          The part size must be a megabyte (1024 KB) multiplied by a power of 2, for example 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB (4096 MB).
        
        :type partSize: string
        :param partSize: 
        
          The size of each part except the last, in bytes. The last part can be smaller than this part size.
        
        :rtype: :py:class:`glacier.MultipartUpload`
        :returns: MultipartUpload resource
        """
        pass

    def load(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          vault.load()
        :returns: None
        """
        pass

    def reload(self):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/None>`_
        
        **Request Syntax** 
        
        ::
        
          vault.load()
        :returns: None
        """
        pass

    def upload_archive(self, archiveDescription: str = None, checksum: str = None, body: Union[bytes, IO] = None) -> 'Archive':
        """
        
        You must use the archive ID to access your data in Amazon Glacier. After you upload an archive, you should save the archive ID returned so that you can retrieve or delete the archive later. Besides saving the archive ID, you can also index it and give it a friendly name to allow for better searching. You can also use the optional archive description field to specify how the archive is referred to in an external index of archives, such as you might create in Amazon DynamoDB. You can also get the vault inventory to obtain a list of archive IDs in a vault. For more information, see  InitiateJob . 
        
        You must provide a SHA256 tree hash of the data you are uploading. For information about computing a SHA256 tree hash, see `Computing Checksums <http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html>`__ . 
        
        You can optionally specify an archive description of up to 1,024 printable ASCII characters. You can get the archive description when you either retrieve the archive or get the vault inventory. For more information, see  InitiateJob . Amazon Glacier does not interpret the description in any way. An archive description does not need to be unique. You cannot use the description to retrieve or sort the archive list. 
        
        Archives are immutable. After you upload an archive, you cannot edit the archive or its description.
        
        An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don\'t have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .
        
        For conceptual information and underlying REST API, see `Uploading an Archive in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive.html>`__ and `Upload Archive <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html>`__ in the *Amazon Glacier Developer Guide* . 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/UploadArchive>`_
        
        **Request Syntax** 
        ::
        
          archive = vault.upload_archive(
              archiveDescription=\'string\',
              body=b\'bytes\'|file
          )
        :type archiveDescription: string
        :param archiveDescription: 
        
          The optional description of the archive you are uploading.
        
        :type checksum: string
        :param checksum: 
        
          The SHA256 tree hash of the data being uploaded.
        
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
        
        :type body: bytes or seekable file-like object
        :param body: 
        
          The data to upload.
        
        :rtype: :py:class:`glacier.Archive`
        :returns: Archive resource
        """
        pass


class vaults(ResourceCollection):
    
    @classmethod
    def all(cls) -> List['Vault']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_
        
        **Request Syntax** 
        ::
        
          vault_iterator = glacier.vaults.all()
          
        :rtype: list(:py:class:`glacier.Vault`)
        :returns: A list of Vault resources
        """
        pass

    
    @classmethod
    def filter(cls, marker: str = None, limit: str = None) -> List['Vault']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_
        
        **Request Syntax** 
        ::
        
          vault_iterator = glacier.vaults.filter(
              marker=\'string\',
              limit=\'string\'
          )
        :type marker: string
        :param marker: 
        
          A string used for pagination. The marker specifies the vault ARN after which the listing of vaults should begin.
        
        :type limit: string
        :param limit: 
        
          The maximum number of vaults to be returned. The default limit is 10. The number of vaults returned might be fewer than the specified limit, but the number of returned vaults never exceeds the limit.
        
        :rtype: list(:py:class:`glacier.Vault`)
        :returns: A list of Vault resources
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
    def limit(cls, count: int = None) -> List['Vault']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_
        
        **Request Syntax** 
        ::
        
          vault_iterator = glacier.vaults.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.
        
        :rtype: list(:py:class:`glacier.Vault`)
        :returns: A list of Vault resources
        """
        pass

    
    @classmethod
    def page_size(cls, count: int = None) -> List['Vault']:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_
        
        **Request Syntax** 
        ::
        
          vault_iterator = glacier.vaults.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call
        
        :rtype: list(:py:class:`glacier.Vault`)
        :returns: A list of Vault resources
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
