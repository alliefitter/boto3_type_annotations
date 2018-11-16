from typing import Dict
from botocore.paginate import Paginator


class DescribeDocumentVersions(Paginator):
    def paginate(self, DocumentId: str, AuthenticationToken: str = None, Include: str = None, Fields: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/DescribeDocumentVersions>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AuthenticationToken=\'string\',
              DocumentId=\'string\',
              Include=\'string\',
              Fields=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AuthenticationToken: string
        :param AuthenticationToken: 
        
          Amazon WorkDocs authentication token. Do not set this field when using administrative API actions, as in accessing the API using AWS credentials.
        
        :type DocumentId: string
        :param DocumentId: **[REQUIRED]** 
        
          The ID of the document.
        
        :type Include: string
        :param Include: 
        
          A comma-separated list of values. Specify \"INITIALIZED\" to include incomplete versions.
        
        :type Fields: string
        :param Fields: 
        
          Specify \"SOURCE\" to include initialized versions and a URL for the source document.
        
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
                \'DocumentVersions\': [
                    {
                        \'Id\': \'string\',
                        \'Name\': \'string\',
                        \'ContentType\': \'string\',
                        \'Size\': 123,
                        \'Signature\': \'string\',
                        \'Status\': \'INITIALIZED\'|\'ACTIVE\',
                        \'CreatedTimestamp\': datetime(2015, 1, 1),
                        \'ModifiedTimestamp\': datetime(2015, 1, 1),
                        \'ContentCreatedTimestamp\': datetime(2015, 1, 1),
                        \'ContentModifiedTimestamp\': datetime(2015, 1, 1),
                        \'CreatorId\': \'string\',
                        \'Thumbnail\': {
                            \'string\': \'string\'
                        },
                        \'Source\': {
                            \'string\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **DocumentVersions** *(list) --* 
        
              The document versions.
        
              - *(dict) --* 
        
                Describes a version of a document.
        
                - **Id** *(string) --* 
        
                  The ID of the version.
        
                - **Name** *(string) --* 
        
                  The name of the version.
        
                - **ContentType** *(string) --* 
        
                  The content type of the document.
        
                - **Size** *(integer) --* 
        
                  The size of the document, in bytes.
        
                - **Signature** *(string) --* 
        
                  The signature of the document.
        
                - **Status** *(string) --* 
        
                  The status of the document.
        
                - **CreatedTimestamp** *(datetime) --* 
        
                  The timestamp when the document was first uploaded.
        
                - **ModifiedTimestamp** *(datetime) --* 
        
                  The timestamp when the document was last uploaded.
        
                - **ContentCreatedTimestamp** *(datetime) --* 
        
                  The timestamp when the content of the document was originally created.
        
                - **ContentModifiedTimestamp** *(datetime) --* 
        
                  The timestamp when the content of the document was modified.
        
                - **CreatorId** *(string) --* 
        
                  The ID of the creator.
        
                - **Thumbnail** *(dict) --* 
        
                  The thumbnail of the document.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **Source** *(dict) --* 
        
                  The source of the document.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeFolderContents(Paginator):
    def paginate(self, FolderId: str, AuthenticationToken: str = None, Sort: str = None, Order: str = None, Type: str = None, Include: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/DescribeFolderContents>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AuthenticationToken=\'string\',
              FolderId=\'string\',
              Sort=\'DATE\'|\'NAME\',
              Order=\'ASCENDING\'|\'DESCENDING\',
              Type=\'ALL\'|\'DOCUMENT\'|\'FOLDER\',
              Include=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AuthenticationToken: string
        :param AuthenticationToken: 
        
          Amazon WorkDocs authentication token. Do not set this field when using administrative API actions, as in accessing the API using AWS credentials.
        
        :type FolderId: string
        :param FolderId: **[REQUIRED]** 
        
          The ID of the folder.
        
        :type Sort: string
        :param Sort: 
        
          The sorting criteria.
        
        :type Order: string
        :param Order: 
        
          The order for the contents of the folder.
        
        :type Type: string
        :param Type: 
        
          The type of items.
        
        :type Include: string
        :param Include: 
        
          The contents to include. Specify \"INITIALIZED\" to include initialized documents.
        
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
                \'Folders\': [
                    {
                        \'Id\': \'string\',
                        \'Name\': \'string\',
                        \'CreatorId\': \'string\',
                        \'ParentFolderId\': \'string\',
                        \'CreatedTimestamp\': datetime(2015, 1, 1),
                        \'ModifiedTimestamp\': datetime(2015, 1, 1),
                        \'ResourceState\': \'ACTIVE\'|\'RESTORING\'|\'RECYCLING\'|\'RECYCLED\',
                        \'Signature\': \'string\',
                        \'Labels\': [
                            \'string\',
                        ],
                        \'Size\': 123,
                        \'LatestVersionSize\': 123
                    },
                ],
                \'Documents\': [
                    {
                        \'Id\': \'string\',
                        \'CreatorId\': \'string\',
                        \'ParentFolderId\': \'string\',
                        \'CreatedTimestamp\': datetime(2015, 1, 1),
                        \'ModifiedTimestamp\': datetime(2015, 1, 1),
                        \'LatestVersionMetadata\': {
                            \'Id\': \'string\',
                            \'Name\': \'string\',
                            \'ContentType\': \'string\',
                            \'Size\': 123,
                            \'Signature\': \'string\',
                            \'Status\': \'INITIALIZED\'|\'ACTIVE\',
                            \'CreatedTimestamp\': datetime(2015, 1, 1),
                            \'ModifiedTimestamp\': datetime(2015, 1, 1),
                            \'ContentCreatedTimestamp\': datetime(2015, 1, 1),
                            \'ContentModifiedTimestamp\': datetime(2015, 1, 1),
                            \'CreatorId\': \'string\',
                            \'Thumbnail\': {
                                \'string\': \'string\'
                            },
                            \'Source\': {
                                \'string\': \'string\'
                            }
                        },
                        \'ResourceState\': \'ACTIVE\'|\'RESTORING\'|\'RECYCLING\'|\'RECYCLED\',
                        \'Labels\': [
                            \'string\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Folders** *(list) --* 
        
              The subfolders in the specified folder.
        
              - *(dict) --* 
        
                Describes a folder.
        
                - **Id** *(string) --* 
        
                  The ID of the folder.
        
                - **Name** *(string) --* 
        
                  The name of the folder.
        
                - **CreatorId** *(string) --* 
        
                  The ID of the creator.
        
                - **ParentFolderId** *(string) --* 
        
                  The ID of the parent folder.
        
                - **CreatedTimestamp** *(datetime) --* 
        
                  The time when the folder was created.
        
                - **ModifiedTimestamp** *(datetime) --* 
        
                  The time when the folder was updated.
        
                - **ResourceState** *(string) --* 
        
                  The resource state of the folder.
        
                - **Signature** *(string) --* 
        
                  The unique identifier created from the subfolders and documents of the folder.
        
                - **Labels** *(list) --* 
        
                  List of labels on the folder.
        
                  - *(string) --* 
              
                - **Size** *(integer) --* 
        
                  The size of the folder metadata.
        
                - **LatestVersionSize** *(integer) --* 
        
                  The size of the latest version of the folder metadata.
        
            - **Documents** *(list) --* 
        
              The documents in the specified folder.
        
              - *(dict) --* 
        
                Describes the document.
        
                - **Id** *(string) --* 
        
                  The ID of the document.
        
                - **CreatorId** *(string) --* 
        
                  The ID of the creator.
        
                - **ParentFolderId** *(string) --* 
        
                  The ID of the parent folder.
        
                - **CreatedTimestamp** *(datetime) --* 
        
                  The time when the document was created.
        
                - **ModifiedTimestamp** *(datetime) --* 
        
                  The time when the document was updated.
        
                - **LatestVersionMetadata** *(dict) --* 
        
                  The latest version of the document.
        
                  - **Id** *(string) --* 
        
                    The ID of the version.
        
                  - **Name** *(string) --* 
        
                    The name of the version.
        
                  - **ContentType** *(string) --* 
        
                    The content type of the document.
        
                  - **Size** *(integer) --* 
        
                    The size of the document, in bytes.
        
                  - **Signature** *(string) --* 
        
                    The signature of the document.
        
                  - **Status** *(string) --* 
        
                    The status of the document.
        
                  - **CreatedTimestamp** *(datetime) --* 
        
                    The timestamp when the document was first uploaded.
        
                  - **ModifiedTimestamp** *(datetime) --* 
        
                    The timestamp when the document was last uploaded.
        
                  - **ContentCreatedTimestamp** *(datetime) --* 
        
                    The timestamp when the content of the document was originally created.
        
                  - **ContentModifiedTimestamp** *(datetime) --* 
        
                    The timestamp when the content of the document was modified.
        
                  - **CreatorId** *(string) --* 
        
                    The ID of the creator.
        
                  - **Thumbnail** *(dict) --* 
        
                    The thumbnail of the document.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                  - **Source** *(dict) --* 
        
                    The source of the document.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                - **ResourceState** *(string) --* 
        
                  The resource state.
        
                - **Labels** *(list) --* 
        
                  List of labels on the document.
        
                  - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeUsers(Paginator):
    def paginate(self, AuthenticationToken: str = None, OrganizationId: str = None, UserIds: str = None, Query: str = None, Include: str = None, Order: str = None, Sort: str = None, Fields: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/DescribeUsers>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              AuthenticationToken=\'string\',
              OrganizationId=\'string\',
              UserIds=\'string\',
              Query=\'string\',
              Include=\'ALL\'|\'ACTIVE_PENDING\',
              Order=\'ASCENDING\'|\'DESCENDING\',
              Sort=\'USER_NAME\'|\'FULL_NAME\'|\'STORAGE_LIMIT\'|\'USER_STATUS\'|\'STORAGE_USED\',
              Fields=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type AuthenticationToken: string
        :param AuthenticationToken: 
        
          Amazon WorkDocs authentication token. Do not set this field when using administrative API actions, as in accessing the API using AWS credentials.
        
        :type OrganizationId: string
        :param OrganizationId: 
        
          The ID of the organization.
        
        :type UserIds: string
        :param UserIds: 
        
          The IDs of the users.
        
        :type Query: string
        :param Query: 
        
          A query to filter users by user name.
        
        :type Include: string
        :param Include: 
        
          The state of the users. Specify \"ALL\" to include inactive users.
        
        :type Order: string
        :param Order: 
        
          The order for the results.
        
        :type Sort: string
        :param Sort: 
        
          The sorting criteria.
        
        :type Fields: string
        :param Fields: 
        
          A comma-separated list of values. Specify \"STORAGE_METADATA\" to include the user storage quota and utilization information.
        
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
                \'Users\': [
                    {
                        \'Id\': \'string\',
                        \'Username\': \'string\',
                        \'EmailAddress\': \'string\',
                        \'GivenName\': \'string\',
                        \'Surname\': \'string\',
                        \'OrganizationId\': \'string\',
                        \'RootFolderId\': \'string\',
                        \'RecycleBinFolderId\': \'string\',
                        \'Status\': \'ACTIVE\'|\'INACTIVE\'|\'PENDING\',
                        \'Type\': \'USER\'|\'ADMIN\'|\'POWERUSER\'|\'MINIMALUSER\'|\'WORKSPACESUSER\',
                        \'CreatedTimestamp\': datetime(2015, 1, 1),
                        \'ModifiedTimestamp\': datetime(2015, 1, 1),
                        \'TimeZoneId\': \'string\',
                        \'Locale\': \'en\'|\'fr\'|\'ko\'|\'de\'|\'es\'|\'ja\'|\'ru\'|\'zh_CN\'|\'zh_TW\'|\'pt_BR\'|\'default\',
                        \'Storage\': {
                            \'StorageUtilizedInBytes\': 123,
                            \'StorageRule\': {
                                \'StorageAllocatedInBytes\': 123,
                                \'StorageType\': \'UNLIMITED\'|\'QUOTA\'
                            }
                        }
                    },
                ],
                \'TotalNumberOfUsers\': 123,
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Users** *(list) --* 
        
              The users.
        
              - *(dict) --* 
        
                Describes a user.
        
                - **Id** *(string) --* 
        
                  The ID of the user.
        
                - **Username** *(string) --* 
        
                  The login name of the user.
        
                - **EmailAddress** *(string) --* 
        
                  The email address of the user.
        
                - **GivenName** *(string) --* 
        
                  The given name of the user.
        
                - **Surname** *(string) --* 
        
                  The surname of the user.
        
                - **OrganizationId** *(string) --* 
        
                  The ID of the organization.
        
                - **RootFolderId** *(string) --* 
        
                  The ID of the root folder.
        
                - **RecycleBinFolderId** *(string) --* 
        
                  The ID of the recycle bin folder.
        
                - **Status** *(string) --* 
        
                  The status of the user.
        
                - **Type** *(string) --* 
        
                  The type of user.
        
                - **CreatedTimestamp** *(datetime) --* 
        
                  The time when the user was created.
        
                - **ModifiedTimestamp** *(datetime) --* 
        
                  The time when the user was modified.
        
                - **TimeZoneId** *(string) --* 
        
                  The time zone ID of the user.
        
                - **Locale** *(string) --* 
        
                  The locale of the user.
        
                - **Storage** *(dict) --* 
        
                  The storage for the user.
        
                  - **StorageUtilizedInBytes** *(integer) --* 
        
                    The amount of storage used, in bytes.
        
                  - **StorageRule** *(dict) --* 
        
                    The storage for a user.
        
                    - **StorageAllocatedInBytes** *(integer) --* 
        
                      The amount of storage allocated, in bytes.
        
                    - **StorageType** *(string) --* 
        
                      The type of storage.
        
            - **TotalNumberOfUsers** *(integer) --* 
        
              The total number of users included in the results.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
