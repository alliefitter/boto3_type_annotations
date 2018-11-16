from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def bulk_publish(self, IdentityPoolId: str) -> Dict:
        """
        
        This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/BulkPublish>`_
        
        **Request Syntax** 
        ::
        
          response = client.bulk_publish(
              IdentityPoolId=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityPoolId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* The output for the BulkPublish operation.
            
            - **IdentityPoolId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
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

    def delete_dataset(self, IdentityPoolId: str, IdentityId: str, DatasetName: str) -> Dict:
        """
        
        This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/DeleteDataset>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_dataset(
              IdentityPoolId=\'string\',
              IdentityId=\'string\',
              DatasetName=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :type IdentityId: string
        :param IdentityId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :type DatasetName: string
        :param DatasetName: **[REQUIRED]** A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Dataset\': {
                    \'IdentityId\': \'string\',
                    \'DatasetName\': \'string\',
                    \'CreationDate\': datetime(2015, 1, 1),
                    \'LastModifiedDate\': datetime(2015, 1, 1),
                    \'LastModifiedBy\': \'string\',
                    \'DataStorage\': 123,
                    \'NumRecords\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* Response to a successful DeleteDataset request.
            
            - **Dataset** *(dict) --* A collection of data for an identity pool. An identity pool can have multiple datasets. A dataset is per identity and can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don\'t exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.
              
              - **IdentityId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
              
              - **DatasetName** *(string) --* A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).
              
              - **CreationDate** *(datetime) --* Date on which the dataset was created.
              
              - **LastModifiedDate** *(datetime) --* Date when the dataset was last modified.
              
              - **LastModifiedBy** *(string) --* The device that made the last change to this dataset.
              
              - **DataStorage** *(integer) --* Total size in bytes of the records in this dataset.
              
              - **NumRecords** *(integer) --* Number of records in this dataset.
          
        """
        pass

    def describe_dataset(self, IdentityPoolId: str, IdentityId: str, DatasetName: str) -> Dict:
        """
        
        This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use Cognito Identity credentials to make this API call.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/DescribeDataset>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_dataset(
              IdentityPoolId=\'string\',
              IdentityId=\'string\',
              DatasetName=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :type IdentityId: string
        :param IdentityId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :type DatasetName: string
        :param DatasetName: **[REQUIRED]** A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Dataset\': {
                    \'IdentityId\': \'string\',
                    \'DatasetName\': \'string\',
                    \'CreationDate\': datetime(2015, 1, 1),
                    \'LastModifiedDate\': datetime(2015, 1, 1),
                    \'LastModifiedBy\': \'string\',
                    \'DataStorage\': 123,
                    \'NumRecords\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* Response to a successful DescribeDataset request.
            
            - **Dataset** *(dict) --* Meta data for a collection of data for an identity. An identity can have multiple datasets. A dataset can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don\'t exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.
              
              - **IdentityId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
              
              - **DatasetName** *(string) --* A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).
              
              - **CreationDate** *(datetime) --* Date on which the dataset was created.
              
              - **LastModifiedDate** *(datetime) --* Date when the dataset was last modified.
              
              - **LastModifiedBy** *(string) --* The device that made the last change to this dataset.
              
              - **DataStorage** *(integer) --* Total size in bytes of the records in this dataset.
              
              - **NumRecords** *(integer) --* Number of records in this dataset.
          
        """
        pass

    def describe_identity_pool_usage(self, IdentityPoolId: str) -> Dict:
        """
        
        This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/DescribeIdentityPoolUsage>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_identity_pool_usage(
              IdentityPoolId=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityPoolUsage\': {
                    \'IdentityPoolId\': \'string\',
                    \'SyncSessionsCount\': 123,
                    \'DataStorage\': 123,
                    \'LastModifiedDate\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* Response to a successful DescribeIdentityPoolUsage request.
            
            - **IdentityPoolUsage** *(dict) --* Information about the usage of the identity pool.
              
              - **IdentityPoolId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
              
              - **SyncSessionsCount** *(integer) --* Number of sync sessions for the identity pool.
              
              - **DataStorage** *(integer) --* Data storage information for the identity pool.
              
              - **LastModifiedDate** *(datetime) --* Date on which the identity pool was last modified.
          
        """
        pass

    def describe_identity_usage(self, IdentityPoolId: str, IdentityId: str) -> Dict:
        """
        
        This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/DescribeIdentityUsage>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_identity_usage(
              IdentityPoolId=\'string\',
              IdentityId=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :type IdentityId: string
        :param IdentityId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityUsage\': {
                    \'IdentityId\': \'string\',
                    \'IdentityPoolId\': \'string\',
                    \'LastModifiedDate\': datetime(2015, 1, 1),
                    \'DatasetCount\': 123,
                    \'DataStorage\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* The response to a successful DescribeIdentityUsage request.
            
            - **IdentityUsage** *(dict) --* Usage information for the identity.
              
              - **IdentityId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
              
              - **IdentityPoolId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
              
              - **LastModifiedDate** *(datetime) --* Date on which the identity was last modified.
              
              - **DatasetCount** *(integer) --* Number of datasets for the identity.
              
              - **DataStorage** *(integer) --* Total data storage for this identity.
          
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

    def get_bulk_publish_details(self, IdentityPoolId: str) -> Dict:
        """
        
        This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/GetBulkPublishDetails>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_bulk_publish_details(
              IdentityPoolId=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityPoolId\': \'string\',
                \'BulkPublishStartTime\': datetime(2015, 1, 1),
                \'BulkPublishCompleteTime\': datetime(2015, 1, 1),
                \'BulkPublishStatus\': \'NOT_STARTED\'|\'IN_PROGRESS\'|\'FAILED\'|\'SUCCEEDED\',
                \'FailureMessage\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* The output for the GetBulkPublishDetails operation.
            
            - **IdentityPoolId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            
            - **BulkPublishStartTime** *(datetime) --* The date/time at which the last bulk publish was initiated.
            
            - **BulkPublishCompleteTime** *(datetime) --* If BulkPublishStatus is SUCCEEDED, the time the last bulk publish operation completed.
            
            - **BulkPublishStatus** *(string) --* Status of the last bulk publish operation, valid values are: 
        
              NOT_STARTED - No bulk publish has been requested for this identity pool
        
              IN_PROGRESS - Data is being published to the configured stream
        
              SUCCEEDED - All data for the identity pool has been published to the configured stream
        
              FAILED - Some portion of the data has failed to publish, check FailureMessage for the cause.
        
            - **FailureMessage** *(string) --* If BulkPublishStatus is FAILED this field will contain the error message that caused the bulk publish to fail.
        """
        pass

    def get_cognito_events(self, IdentityPoolId: str) -> Dict:
        """
        
        This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/GetCognitoEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_cognito_events(
              IdentityPoolId=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          The Cognito Identity Pool ID for the request
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Events\': {
                    \'string\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The response from the GetCognitoEvents request
        
            - **Events** *(dict) --* 
        
              The Cognito Events returned from the GetCognitoEvents request
        
              - *(string) --* 
                
                - *(string) --* 
          
        """
        pass

    def get_identity_pool_configuration(self, IdentityPoolId: str) -> Dict:
        """
        
        This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/GetIdentityPoolConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_identity_pool_configuration(
              IdentityPoolId=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool for which to return a configuration.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityPoolId\': \'string\',
                \'PushSync\': {
                    \'ApplicationArns\': [
                        \'string\',
                    ],
                    \'RoleArn\': \'string\'
                },
                \'CognitoStreams\': {
                    \'StreamName\': \'string\',
                    \'RoleArn\': \'string\',
                    \'StreamingStatus\': \'ENABLED\'|\'DISABLED\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for the GetIdentityPoolConfiguration operation.
        
            - **IdentityPoolId** *(string) --* 
        
              A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
        
            - **PushSync** *(dict) --* 
        
              Options to apply to this identity pool for push synchronization.
        
              - **ApplicationArns** *(list) --* 
        
                List of SNS platform application ARNs that could be used by clients.
        
                - *(string) --* 
            
              - **RoleArn** *(string) --* 
        
                A role configured to allow Cognito to call SNS on behalf of the developer.
        
            - **CognitoStreams** *(dict) --* Options to apply to this identity pool for Amazon Cognito streams.
              
              - **StreamName** *(string) --* The name of the Cognito stream to receive updates. This stream must be in the developers account and in the same region as the identity pool.
              
              - **RoleArn** *(string) --* The ARN of the role Amazon Cognito can assume in order to publish to the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke PutRecord on your Cognito stream.
              
              - **StreamingStatus** *(string) --* Status of the Cognito streams. Valid values are: 
        
                ENABLED - Streaming of updates to identity pool is enabled.
        
                DISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail if StreamingStatus is DISABLED.
        
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

    def list_datasets(self, IdentityPoolId: str, IdentityId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        ListDatasets can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use the Cognito Identity credentials to make this API call.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/ListDatasets>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_datasets(
              IdentityPoolId=\'string\',
              IdentityId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :type IdentityId: string
        :param IdentityId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :type NextToken: string
        :param NextToken: A pagination token for obtaining the next page of results.
        
        :type MaxResults: integer
        :param MaxResults: The maximum number of results to be returned.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Datasets\': [
                    {
                        \'IdentityId\': \'string\',
                        \'DatasetName\': \'string\',
                        \'CreationDate\': datetime(2015, 1, 1),
                        \'LastModifiedDate\': datetime(2015, 1, 1),
                        \'LastModifiedBy\': \'string\',
                        \'DataStorage\': 123,
                        \'NumRecords\': 123
                    },
                ],
                \'Count\': 123,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Returned for a successful ListDatasets request.
            
            - **Datasets** *(list) --* A set of datasets.
              
              - *(dict) --* A collection of data for an identity pool. An identity pool can have multiple datasets. A dataset is per identity and can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don\'t exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs.
                
                - **IdentityId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
                
                - **DatasetName** *(string) --* A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).
                
                - **CreationDate** *(datetime) --* Date on which the dataset was created.
                
                - **LastModifiedDate** *(datetime) --* Date when the dataset was last modified.
                
                - **LastModifiedBy** *(string) --* The device that made the last change to this dataset.
                
                - **DataStorage** *(integer) --* Total size in bytes of the records in this dataset.
                
                - **NumRecords** *(integer) --* Number of records in this dataset.
            
            - **Count** *(integer) --* Number of datasets returned.
            
            - **NextToken** *(string) --* A pagination token for obtaining the next page of results.
        """
        pass

    def list_identity_pool_usage(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        ListIdentityPoolUsage can only be called with developer credentials. You cannot make this API call with the temporary user credentials provided by Cognito Identity.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/ListIdentityPoolUsage>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_identity_pool_usage(
              NextToken=\'string\',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken: A pagination token for obtaining the next page of results.
        
        :type MaxResults: integer
        :param MaxResults: The maximum number of results to be returned.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityPoolUsages\': [
                    {
                        \'IdentityPoolId\': \'string\',
                        \'SyncSessionsCount\': 123,
                        \'DataStorage\': 123,
                        \'LastModifiedDate\': datetime(2015, 1, 1)
                    },
                ],
                \'MaxResults\': 123,
                \'Count\': 123,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Returned for a successful ListIdentityPoolUsage request.
            
            - **IdentityPoolUsages** *(list) --* Usage information for the identity pools.
              
              - *(dict) --* Usage information for the identity pool.
                
                - **IdentityPoolId** *(string) --* A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
                
                - **SyncSessionsCount** *(integer) --* Number of sync sessions for the identity pool.
                
                - **DataStorage** *(integer) --* Data storage information for the identity pool.
                
                - **LastModifiedDate** *(datetime) --* Date on which the identity pool was last modified.
            
            - **MaxResults** *(integer) --* The maximum number of results to be returned.
            
            - **Count** *(integer) --* Total number of identities for the identity pool.
            
            - **NextToken** *(string) --* A pagination token for obtaining the next page of results.
        """
        pass

    def list_records(self, IdentityPoolId: str, IdentityId: str, DatasetName: str, LastSyncCount: int = None, NextToken: str = None, MaxResults: int = None, SyncSessionToken: str = None) -> Dict:
        """
        
        ListRecords can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use Cognito Identity credentials to make this API call.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/ListRecords>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_records(
              IdentityPoolId=\'string\',
              IdentityId=\'string\',
              DatasetName=\'string\',
              LastSyncCount=123,
              NextToken=\'string\',
              MaxResults=123,
              SyncSessionToken=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :type IdentityId: string
        :param IdentityId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :type DatasetName: string
        :param DatasetName: **[REQUIRED]** A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).
        
        :type LastSyncCount: integer
        :param LastSyncCount: The last server sync count for this record.
        
        :type NextToken: string
        :param NextToken: A pagination token for obtaining the next page of results.
        
        :type MaxResults: integer
        :param MaxResults: The maximum number of results to be returned.
        
        :type SyncSessionToken: string
        :param SyncSessionToken: A token containing a session ID, identity ID, and expiration.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Records\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\',
                        \'SyncCount\': 123,
                        \'LastModifiedDate\': datetime(2015, 1, 1),
                        \'LastModifiedBy\': \'string\',
                        \'DeviceLastModifiedDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\',
                \'Count\': 123,
                \'DatasetSyncCount\': 123,
                \'LastModifiedBy\': \'string\',
                \'MergedDatasetNames\': [
                    \'string\',
                ],
                \'DatasetExists\': True|False,
                \'DatasetDeletedAfterRequestedSyncCount\': True|False,
                \'SyncSessionToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Returned for a successful ListRecordsRequest.
            
            - **Records** *(list) --* A list of all records.
              
              - *(dict) --* The basic data structure of a dataset.
                
                - **Key** *(string) --* The key for the record.
                
                - **Value** *(string) --* The value for the record.
                
                - **SyncCount** *(integer) --* The server sync count for this record.
                
                - **LastModifiedDate** *(datetime) --* The date on which the record was last modified.
                
                - **LastModifiedBy** *(string) --* The user/device that made the last change to this record.
                
                - **DeviceLastModifiedDate** *(datetime) --* The last modified date of the client device.
            
            - **NextToken** *(string) --* A pagination token for obtaining the next page of results.
            
            - **Count** *(integer) --* Total number of records.
            
            - **DatasetSyncCount** *(integer) --* Server sync count for this dataset.
            
            - **LastModifiedBy** *(string) --* The user/device that made the last change to this record.
            
            - **MergedDatasetNames** *(list) --* Names of merged datasets.
              
              - *(string) --* 
          
            - **DatasetExists** *(boolean) --* Indicates whether the dataset exists.
            
            - **DatasetDeletedAfterRequestedSyncCount** *(boolean) --* A boolean value specifying whether to delete the dataset locally.
            
            - **SyncSessionToken** *(string) --* A token containing a session ID, identity ID, and expiration.
        """
        pass

    def register_device(self, IdentityPoolId: str, IdentityId: str, Platform: str, Token: str) -> Dict:
        """
        
        This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/RegisterDevice>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_device(
              IdentityPoolId=\'string\',
              IdentityId=\'string\',
              Platform=\'APNS\'|\'APNS_SANDBOX\'|\'GCM\'|\'ADM\',
              Token=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. Here, the ID of the pool that the identity belongs to.
        
        :type IdentityId: string
        :param IdentityId: **[REQUIRED]** 
        
          The unique ID for this identity.
        
        :type Platform: string
        :param Platform: **[REQUIRED]** 
        
          The SNS platform type (e.g. GCM, SDM, APNS, APNS_SANDBOX).
        
        :type Token: string
        :param Token: **[REQUIRED]** 
        
          The push token.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeviceId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Response to a RegisterDevice request.
        
            - **DeviceId** *(string) --* 
        
              The unique ID generated for this device by Cognito.
        
        """
        pass

    def set_cognito_events(self, IdentityPoolId: str, Events: Dict):
        """
        
        This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/SetCognitoEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.set_cognito_events(
              IdentityPoolId=\'string\',
              Events={
                  \'string\': \'string\'
              }
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          The Cognito Identity Pool to use when configuring Cognito Events
        
        :type Events: dict
        :param Events: **[REQUIRED]** 
        
          The events to configure
        
          - *(string) --* 
        
            - *(string) --* 
        
        :returns: None
        """
        pass

    def set_identity_pool_configuration(self, IdentityPoolId: str, PushSync: Dict = None, CognitoStreams: Dict = None) -> Dict:
        """
        
        This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/SetIdentityPoolConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.set_identity_pool_configuration(
              IdentityPoolId=\'string\',
              PushSync={
                  \'ApplicationArns\': [
                      \'string\',
                  ],
                  \'RoleArn\': \'string\'
              },
              CognitoStreams={
                  \'StreamName\': \'string\',
                  \'RoleArn\': \'string\',
                  \'StreamingStatus\': \'ENABLED\'|\'DISABLED\'
              }
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool to modify.
        
        :type PushSync: dict
        :param PushSync: 
        
          Options to apply to this identity pool for push synchronization.
        
          - **ApplicationArns** *(list) --* 
        
            List of SNS platform application ARNs that could be used by clients.
        
            - *(string) --* 
        
          - **RoleArn** *(string) --* 
        
            A role configured to allow Cognito to call SNS on behalf of the developer.
        
        :type CognitoStreams: dict
        :param CognitoStreams: Options to apply to this identity pool for Amazon Cognito streams.
        
          - **StreamName** *(string) --* The name of the Cognito stream to receive updates. This stream must be in the developers account and in the same region as the identity pool.
        
          - **RoleArn** *(string) --* The ARN of the role Amazon Cognito can assume in order to publish to the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke PutRecord on your Cognito stream.
        
          - **StreamingStatus** *(string) --* Status of the Cognito streams. Valid values are: 
        
            ENABLED - Streaming of updates to identity pool is enabled.
        
            DISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail if StreamingStatus is DISABLED.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IdentityPoolId\': \'string\',
                \'PushSync\': {
                    \'ApplicationArns\': [
                        \'string\',
                    ],
                    \'RoleArn\': \'string\'
                },
                \'CognitoStreams\': {
                    \'StreamName\': \'string\',
                    \'RoleArn\': \'string\',
                    \'StreamingStatus\': \'ENABLED\'|\'DISABLED\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The output for the SetIdentityPoolConfiguration operation
        
            - **IdentityPoolId** *(string) --* 
        
              A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
        
            - **PushSync** *(dict) --* 
        
              Options to apply to this identity pool for push synchronization.
        
              - **ApplicationArns** *(list) --* 
        
                List of SNS platform application ARNs that could be used by clients.
        
                - *(string) --* 
            
              - **RoleArn** *(string) --* 
        
                A role configured to allow Cognito to call SNS on behalf of the developer.
        
            - **CognitoStreams** *(dict) --* Options to apply to this identity pool for Amazon Cognito streams.
              
              - **StreamName** *(string) --* The name of the Cognito stream to receive updates. This stream must be in the developers account and in the same region as the identity pool.
              
              - **RoleArn** *(string) --* The ARN of the role Amazon Cognito can assume in order to publish to the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke PutRecord on your Cognito stream.
              
              - **StreamingStatus** *(string) --* Status of the Cognito streams. Valid values are: 
        
                ENABLED - Streaming of updates to identity pool is enabled.
        
                DISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail if StreamingStatus is DISABLED.
        
        """
        pass

    def subscribe_to_dataset(self, IdentityPoolId: str, IdentityId: str, DatasetName: str, DeviceId: str) -> Dict:
        """
        
        This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/SubscribeToDataset>`_
        
        **Request Syntax** 
        ::
        
          response = client.subscribe_to_dataset(
              IdentityPoolId=\'string\',
              IdentityId=\'string\',
              DatasetName=\'string\',
              DeviceId=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which the identity belongs.
        
        :type IdentityId: string
        :param IdentityId: **[REQUIRED]** 
        
          Unique ID for this identity.
        
        :type DatasetName: string
        :param DatasetName: **[REQUIRED]** 
        
          The name of the dataset to subcribe to.
        
        :type DeviceId: string
        :param DeviceId: **[REQUIRED]** 
        
          The unique ID generated for this device by Cognito.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Response to a SubscribeToDataset request.
        
        """
        pass

    def unsubscribe_from_dataset(self, IdentityPoolId: str, IdentityId: str, DatasetName: str, DeviceId: str) -> Dict:
        """
        
        This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/UnsubscribeFromDataset>`_
        
        **Request Syntax** 
        ::
        
          response = client.unsubscribe_from_dataset(
              IdentityPoolId=\'string\',
              IdentityId=\'string\',
              DatasetName=\'string\',
              DeviceId=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** 
        
          A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which this identity belongs.
        
        :type IdentityId: string
        :param IdentityId: **[REQUIRED]** 
        
          Unique ID for this identity.
        
        :type DatasetName: string
        :param DatasetName: **[REQUIRED]** 
        
          The name of the dataset from which to unsubcribe.
        
        :type DeviceId: string
        :param DeviceId: **[REQUIRED]** 
        
          The unique ID generated for this device by Cognito.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Response to an UnsubscribeFromDataset request.
        
        """
        pass

    def update_records(self, IdentityPoolId: str, IdentityId: str, DatasetName: str, SyncSessionToken: str, DeviceId: str = None, RecordPatches: List = None, ClientContext: str = None) -> Dict:
        """
        
        The sync count in the record patch is your last known sync count for that record. The server will reject an UpdateRecords request with a ResourceConflictException if you try to patch a record with a new value but a stale sync count.
        
        For example, if the sync count on the server is 5 for a key called highScore and you try and submit a new highScore with sync count of 4, the request will be rejected. To obtain the current sync count for a record, call ListRecords. On a successful update of the record, the response returns the new sync count for that record. You should present that sync count the next time you try to update that same record. When the record does not exist, specify the sync count as 0.
        
        This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cognito-sync-2014-06-30/UpdateRecords>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_records(
              IdentityPoolId=\'string\',
              IdentityId=\'string\',
              DatasetName=\'string\',
              DeviceId=\'string\',
              RecordPatches=[
                  {
                      \'Op\': \'replace\'|\'remove\',
                      \'Key\': \'string\',
                      \'Value\': \'string\',
                      \'SyncCount\': 123,
                      \'DeviceLastModifiedDate\': datetime(2015, 1, 1)
                  },
              ],
              SyncSessionToken=\'string\',
              ClientContext=\'string\'
          )
        :type IdentityPoolId: string
        :param IdentityPoolId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :type IdentityId: string
        :param IdentityId: **[REQUIRED]** A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        
        :type DatasetName: string
        :param DatasetName: **[REQUIRED]** A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, \'_\' (underscore), \'-\' (dash), and \'.\' (dot).
        
        :type DeviceId: string
        :param DeviceId: 
        
          The unique ID generated for this device by Cognito.
        
        :type RecordPatches: list
        :param RecordPatches: A list of patch operations.
        
          - *(dict) --* An update operation for a record.
        
            - **Op** *(string) --* **[REQUIRED]** An operation, either replace or remove.
        
            - **Key** *(string) --* **[REQUIRED]** The key associated with the record patch.
        
            - **Value** *(string) --* The value associated with the record patch.
        
            - **SyncCount** *(integer) --* **[REQUIRED]** Last known server sync count for this record. Set to 0 if unknown.
        
            - **DeviceLastModifiedDate** *(datetime) --* The last modified date of the client device.
        
        :type SyncSessionToken: string
        :param SyncSessionToken: **[REQUIRED]** The SyncSessionToken returned by a previous call to ListRecords for this dataset and identity.
        
        :type ClientContext: string
        :param ClientContext: Intended to supply a device ID that will populate the lastModifiedBy field referenced in other methods. The ClientContext field is not yet implemented.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Records\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\',
                        \'SyncCount\': 123,
                        \'LastModifiedDate\': datetime(2015, 1, 1),
                        \'LastModifiedBy\': \'string\',
                        \'DeviceLastModifiedDate\': datetime(2015, 1, 1)
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* Returned for a successful UpdateRecordsRequest.
            
            - **Records** *(list) --* A list of records that have been updated.
              
              - *(dict) --* The basic data structure of a dataset.
                
                - **Key** *(string) --* The key for the record.
                
                - **Value** *(string) --* The value for the record.
                
                - **SyncCount** *(integer) --* The server sync count for this record.
                
                - **LastModifiedDate** *(datetime) --* The date on which the record was last modified.
                
                - **LastModifiedBy** *(string) --* The user/device that made the last change to this record.
                
                - **DeviceLastModifiedDate** *(datetime) --* The last modified date of the client device.
            
        """
        pass
