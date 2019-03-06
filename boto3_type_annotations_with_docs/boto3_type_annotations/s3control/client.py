from typing import Union
from botocore.client import BaseClient
from botocore.paginate import Paginator
from typing import Dict
from botocore.waiter import Waiter
from typing import Optional


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        """
        Check if an operation can be paginated.
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """
        pass

    def delete_public_access_block(self, AccountId: str):
        """
        Removes the Public Access Block configuration for an Amazon Web Services account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/DeletePublicAccessBlock>`_
        
        **Request Syntax**
        ::
          response = client.delete_public_access_block(
              AccountId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Account ID for the Amazon Web Services account whose Public Access Block configuration you want to remove.
        :returns: None
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        """
        Generate a presigned url given a client, its method, and arguments
        :type ClientMethod: string
        :param ClientMethod: The client method to presign for
        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.
        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method\'s model.
        :returns: The presigned url
        """
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        Create a paginator for an operation.
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.
        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """
        pass

    def get_public_access_block(self, AccountId: str) -> Dict:
        """
        Retrieves the Public Access Block configuration for an Amazon Web Services account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/GetPublicAccessBlock>`_
        
        **Request Syntax**
        ::
          response = client.get_public_access_block(
              AccountId='string'
          )
        
        **Response Syntax**
        ::
            {
                'PublicAccessBlockConfiguration': {
                    'BlockPublicAcls': True|False,
                    'IgnorePublicAcls': True|False,
                    'BlockPublicPolicy': True|False,
                    'RestrictPublicBuckets': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **PublicAccessBlockConfiguration** *(dict) --* 
              The Public Access Block configuration currently in effect for this Amazon Web Services account.
              - **BlockPublicAcls** *(boolean) --* 
                Specifies whether Amazon S3 should block public ACLs for buckets in this account. Setting this element to ``TRUE`` causes the following behavior:
                * PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access. 
                * PUT Object calls will fail if the request includes an object ACL. 
                Note that enabling this setting doesn't affect existing policies or ACLs.
              - **IgnorePublicAcls** *(boolean) --* 
                Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting this element to ``TRUE`` causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain. 
                Note that enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set.
              - **BlockPublicPolicy** *(boolean) --* 
                Specifies whether Amazon S3 should block public bucket policies for buckets in this account. Setting this element to ``TRUE`` causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access. 
                Note that enabling this setting doesn't affect existing bucket policies.
              - **RestrictPublicBuckets** *(boolean) --* 
                Specifies whether Amazon S3 should restrict public bucket policies for buckets in this account. If this element is set to ``TRUE`` , then only the bucket owner and AWS Services can access buckets with public policies.
                Note that enabling this setting doesn't affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. 
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Account ID for the Amazon Web Services account whose Public Access Block configuration you want to retrieve.
        :rtype: dict
        :returns:
        """
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        Returns an object that can wait for some condition.
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def put_public_access_block(self, PublicAccessBlockConfiguration: Dict, AccountId: str):
        """
        Creates or modifies the Public Access Block configuration for an Amazon Web Services account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/PutPublicAccessBlock>`_
        
        **Request Syntax**
        ::
          response = client.put_public_access_block(
              PublicAccessBlockConfiguration={
                  'BlockPublicAcls': True|False,
                  'IgnorePublicAcls': True|False,
                  'BlockPublicPolicy': True|False,
                  'RestrictPublicBuckets': True|False
              },
              AccountId='string'
          )
        :type PublicAccessBlockConfiguration: dict
        :param PublicAccessBlockConfiguration: **[REQUIRED]**
          The Public Access Block configuration that you want to apply to this Amazon Web Services account.
          - **BlockPublicAcls** *(boolean) --*
            Specifies whether Amazon S3 should block public ACLs for buckets in this account. Setting this element to ``TRUE`` causes the following behavior:
            * PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
            * PUT Object calls will fail if the request includes an object ACL.
            Note that enabling this setting doesn\'t affect existing policies or ACLs.
          - **IgnorePublicAcls** *(boolean) --*
            Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting this element to ``TRUE`` causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain.
            Note that enabling this setting doesn\'t affect the persistence of any existing ACLs and doesn\'t prevent new public ACLs from being set.
          - **BlockPublicPolicy** *(boolean) --*
            Specifies whether Amazon S3 should block public bucket policies for buckets in this account. Setting this element to ``TRUE`` causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.
            Note that enabling this setting doesn\'t affect existing bucket policies.
          - **RestrictPublicBuckets** *(boolean) --*
            Specifies whether Amazon S3 should restrict public bucket policies for buckets in this account. If this element is set to ``TRUE`` , then only the bucket owner and AWS Services can access buckets with public policies.
            Note that enabling this setting doesn\'t affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.
        :type AccountId: string
        :param AccountId: **[REQUIRED]**
          The Account ID for the Amazon Web Services account whose Public Access Block configuration you want to set.
        :returns: None
        """
        pass
