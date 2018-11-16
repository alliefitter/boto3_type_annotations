from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def associate_member_account(self, memberAccountId: str):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/macie-2017-12-19/AssociateMemberAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_member_account(
              memberAccountId=\'string\'
          )
        :type memberAccountId: string
        :param memberAccountId: **[REQUIRED]** 
        
          The ID of the AWS account that you want to associate with Amazon Macie as a member account.
        
        :returns: None
        """
        pass

    def associate_s3_resources(self, s3Resources: List, memberAccountId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/macie-2017-12-19/AssociateS3Resources>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_s3_resources(
              memberAccountId=\'string\',
              s3Resources=[
                  {
                      \'bucketName\': \'string\',
                      \'prefix\': \'string\',
                      \'classificationType\': {
                          \'oneTime\': \'FULL\'|\'NONE\',
                          \'continuous\': \'FULL\'
                      }
                  },
              ]
          )
        :type memberAccountId: string
        :param memberAccountId: 
        
          The ID of the Amazon Macie member account whose resources you want to associate with Macie. 
        
        :type s3Resources: list
        :param s3Resources: **[REQUIRED]** 
        
          The S3 resources that you want to associate with Amazon Macie for monitoring and data classification. 
        
          - *(dict) --* 
        
            The S3 resources that you want to associate with Amazon Macie for monitoring and data classification. This data type is used as a request parameter in the AssociateS3Resources action and a response parameter in the ListS3Resources action. 
        
            - **bucketName** *(string) --* **[REQUIRED]** 
        
              The name of the S3 bucket that you want to associate with Amazon Macie.
        
            - **prefix** *(string) --* 
        
              The prefix of the S3 bucket that you want to associate with Amazon Macie.
        
            - **classificationType** *(dict) --* **[REQUIRED]** 
        
              The classification type that you want to specify for the resource associated with Amazon Macie. 
        
              - **oneTime** *(string) --* **[REQUIRED]** 
        
                A one-time classification of all of the existing objects in a specified S3 bucket. 
        
              - **continuous** *(string) --* **[REQUIRED]** 
        
                A continuous classification of the objects that are added to a specified S3 bucket. Amazon Macie begins performing continuous classification after a bucket is successfully associated with Amazon Macie. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'failedS3Resources\': [
                    {
                        \'failedItem\': {
                            \'bucketName\': \'string\',
                            \'prefix\': \'string\'
                        },
                        \'errorCode\': \'string\',
                        \'errorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **failedS3Resources** *(list) --* 
        
              S3 resources that couldn\'t be associated with Amazon Macie. An error code and an error message are provided for each failed item. 
        
              - *(dict) --* 
        
                Includes details about the failed S3 resources.
        
                - **failedItem** *(dict) --* 
        
                  The failed S3 resources.
        
                  - **bucketName** *(string) --* 
        
                    The name of the S3 bucket.
        
                  - **prefix** *(string) --* 
        
                    The prefix of the S3 bucket. 
        
                - **errorCode** *(string) --* 
        
                  The status code of a failed item.
        
                - **errorMessage** *(string) --* 
        
                  The error message of a failed item.
        
        """
        pass

    def can_paginate(self, operation_name: str = None):
        """
        
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

    def disassociate_member_account(self, memberAccountId: str):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/macie-2017-12-19/DisassociateMemberAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_member_account(
              memberAccountId=\'string\'
          )
        :type memberAccountId: string
        :param memberAccountId: **[REQUIRED]** 
        
          The ID of the member account that you want to remove from Amazon Macie.
        
        :returns: None
        """
        pass

    def disassociate_s3_resources(self, associatedS3Resources: List, memberAccountId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/macie-2017-12-19/DisassociateS3Resources>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_s3_resources(
              memberAccountId=\'string\',
              associatedS3Resources=[
                  {
                      \'bucketName\': \'string\',
                      \'prefix\': \'string\'
                  },
              ]
          )
        :type memberAccountId: string
        :param memberAccountId: 
        
          The ID of the Amazon Macie member account whose resources you want to remove from being monitored by Amazon Macie. 
        
        :type associatedS3Resources: list
        :param associatedS3Resources: **[REQUIRED]** 
        
          The S3 resources (buckets or prefixes) that you want to remove from being monitored and classified by Amazon Macie. 
        
          - *(dict) --* 
        
            Contains information about the S3 resource. This data type is used as a request parameter in the DisassociateS3Resources action and can be used as a response parameter in the AssociateS3Resources and UpdateS3Resources actions. 
        
            - **bucketName** *(string) --* **[REQUIRED]** 
        
              The name of the S3 bucket.
        
            - **prefix** *(string) --* 
        
              The prefix of the S3 bucket. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'failedS3Resources\': [
                    {
                        \'failedItem\': {
                            \'bucketName\': \'string\',
                            \'prefix\': \'string\'
                        },
                        \'errorCode\': \'string\',
                        \'errorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **failedS3Resources** *(list) --* 
        
              S3 resources that couldn\'t be removed from being monitored and classified by Amazon Macie. An error code and an error message are provided for each failed item. 
        
              - *(dict) --* 
        
                Includes details about the failed S3 resources.
        
                - **failedItem** *(dict) --* 
        
                  The failed S3 resources.
        
                  - **bucketName** *(string) --* 
        
                    The name of the S3 bucket.
        
                  - **prefix** *(string) --* 
        
                    The prefix of the S3 bucket. 
        
                - **errorCode** *(string) --* 
        
                  The status code of a failed item.
        
                - **errorMessage** *(string) --* 
        
                  The error message of a failed item.
        
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        """
        
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

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def list_member_accounts(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/macie-2017-12-19/ListMemberAccounts>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_member_accounts(
              nextToken=\'string\',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken: 
        
          Use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListMemberAccounts action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data. 
        
        :type maxResults: integer
        :param maxResults: 
        
          Use this parameter to indicate the maximum number of items that you want in the response. The default value is 250. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'memberAccounts\': [
                    {
                        \'accountId\': \'string\'
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **memberAccounts** *(list) --* 
        
              A list of the Amazon Macie member accounts returned by the action. The current master account is also included in this list. 
        
              - *(dict) --* 
        
                Contains information about the Amazon Macie member account.
        
                - **accountId** *(string) --* 
        
                  The AWS account ID of the Amazon Macie member account.
        
            - **nextToken** *(string) --* 
        
              When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null. 
        
        """
        pass

    def list_s3_resources(self, memberAccountId: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/macie-2017-12-19/ListS3Resources>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_s3_resources(
              memberAccountId=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
        :type memberAccountId: string
        :param memberAccountId: 
        
          The Amazon Macie member account ID whose associated S3 resources you want to list. 
        
        :type nextToken: string
        :param nextToken: 
        
          Use this parameter when paginating results. Set its value to null on your first call to the ListS3Resources action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data. 
        
        :type maxResults: integer
        :param maxResults: 
        
          Use this parameter to indicate the maximum number of items that you want in the response. The default value is 250. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'s3Resources\': [
                    {
                        \'bucketName\': \'string\',
                        \'prefix\': \'string\',
                        \'classificationType\': {
                            \'oneTime\': \'FULL\'|\'NONE\',
                            \'continuous\': \'FULL\'
                        }
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **s3Resources** *(list) --* 
        
              A list of the associated S3 resources returned by the action.
        
              - *(dict) --* 
        
                The S3 resources that you want to associate with Amazon Macie for monitoring and data classification. This data type is used as a request parameter in the AssociateS3Resources action and a response parameter in the ListS3Resources action. 
        
                - **bucketName** *(string) --* 
        
                  The name of the S3 bucket that you want to associate with Amazon Macie.
        
                - **prefix** *(string) --* 
        
                  The prefix of the S3 bucket that you want to associate with Amazon Macie.
        
                - **classificationType** *(dict) --* 
        
                  The classification type that you want to specify for the resource associated with Amazon Macie. 
        
                  - **oneTime** *(string) --* 
        
                    A one-time classification of all of the existing objects in a specified S3 bucket. 
        
                  - **continuous** *(string) --* 
        
                    A continuous classification of the objects that are added to a specified S3 bucket. Amazon Macie begins performing continuous classification after a bucket is successfully associated with Amazon Macie. 
        
            - **nextToken** *(string) --* 
        
              When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null. 
        
        """
        pass

    def update_s3_resources(self, s3ResourcesUpdate: List, memberAccountId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/macie-2017-12-19/UpdateS3Resources>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_s3_resources(
              memberAccountId=\'string\',
              s3ResourcesUpdate=[
                  {
                      \'bucketName\': \'string\',
                      \'prefix\': \'string\',
                      \'classificationTypeUpdate\': {
                          \'oneTime\': \'FULL\'|\'NONE\',
                          \'continuous\': \'FULL\'
                      }
                  },
              ]
          )
        :type memberAccountId: string
        :param memberAccountId: 
        
          The AWS ID of the Amazon Macie member account whose S3 resources\' classification types you want to update. 
        
        :type s3ResourcesUpdate: list
        :param s3ResourcesUpdate: **[REQUIRED]** 
        
          The S3 resources whose classification types you want to update.
        
          - *(dict) --* 
        
            The S3 resources whose classification types you want to update. This data type is used as a request parameter in the UpdateS3Resources action. 
        
            - **bucketName** *(string) --* **[REQUIRED]** 
        
              The name of the S3 bucket whose classification types you want to update.
        
            - **prefix** *(string) --* 
        
              The prefix of the S3 bucket whose classification types you want to update.
        
            - **classificationTypeUpdate** *(dict) --* **[REQUIRED]** 
        
              The classification type that you want to update for the resource associated with Amazon Macie. 
        
              - **oneTime** *(string) --* 
        
                A one-time classification of all of the existing objects in a specified S3 bucket. 
        
              - **continuous** *(string) --* 
        
                A continuous classification of the objects that are added to a specified S3 bucket. Amazon Macie begins performing continuous classification after a bucket is successfully associated with Amazon Macie. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'failedS3Resources\': [
                    {
                        \'failedItem\': {
                            \'bucketName\': \'string\',
                            \'prefix\': \'string\'
                        },
                        \'errorCode\': \'string\',
                        \'errorMessage\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **failedS3Resources** *(list) --* 
        
              The S3 resources whose classification types can\'t be updated. An error code and an error message are provided for each failed item. 
        
              - *(dict) --* 
        
                Includes details about the failed S3 resources.
        
                - **failedItem** *(dict) --* 
        
                  The failed S3 resources.
        
                  - **bucketName** *(string) --* 
        
                    The name of the S3 bucket.
        
                  - **prefix** *(string) --* 
        
                    The prefix of the S3 bucket. 
        
                - **errorCode** *(string) --* 
        
                  The status code of a failed item.
        
                - **errorMessage** *(string) --* 
        
                  The error message of a failed item.
        
        """
        pass
