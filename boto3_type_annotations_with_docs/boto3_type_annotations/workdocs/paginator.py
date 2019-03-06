from typing import Dict
from datetime import datetime
from botocore.paginate import Paginator


class DescribeActivities(Paginator):
    def paginate(self, AuthenticationToken: str = None, StartTime: datetime = None, EndTime: datetime = None, OrganizationId: str = None, ActivityTypes: str = None, ResourceId: str = None, UserId: str = None, IncludeIndirectActivities: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkDocs.Client.describe_activities`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/DescribeActivities>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AuthenticationToken='string',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              OrganizationId='string',
              ActivityTypes='string',
              ResourceId='string',
              UserId='string',
              IncludeIndirectActivities=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'UserActivities': [
                    {
                        'Type': 'DOCUMENT_CHECKED_IN'|'DOCUMENT_CHECKED_OUT'|'DOCUMENT_RENAMED'|'DOCUMENT_VERSION_UPLOADED'|'DOCUMENT_VERSION_DELETED'|'DOCUMENT_VERSION_VIEWED'|'DOCUMENT_VERSION_DOWNLOADED'|'DOCUMENT_RECYCLED'|'DOCUMENT_RESTORED'|'DOCUMENT_REVERTED'|'DOCUMENT_SHARED'|'DOCUMENT_UNSHARED'|'DOCUMENT_SHARE_PERMISSION_CHANGED'|'DOCUMENT_SHAREABLE_LINK_CREATED'|'DOCUMENT_SHAREABLE_LINK_REMOVED'|'DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED'|'DOCUMENT_MOVED'|'DOCUMENT_COMMENT_ADDED'|'DOCUMENT_COMMENT_DELETED'|'DOCUMENT_ANNOTATION_ADDED'|'DOCUMENT_ANNOTATION_DELETED'|'FOLDER_CREATED'|'FOLDER_DELETED'|'FOLDER_RENAMED'|'FOLDER_RECYCLED'|'FOLDER_RESTORED'|'FOLDER_SHARED'|'FOLDER_UNSHARED'|'FOLDER_SHARE_PERMISSION_CHANGED'|'FOLDER_SHAREABLE_LINK_CREATED'|'FOLDER_SHAREABLE_LINK_REMOVED'|'FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED'|'FOLDER_MOVED',
                        'TimeStamp': datetime(2015, 1, 1),
                        'IsIndirectActivity': True|False,
                        'OrganizationId': 'string',
                        'Initiator': {
                            'Id': 'string',
                            'Username': 'string',
                            'GivenName': 'string',
                            'Surname': 'string',
                            'EmailAddress': 'string'
                        },
                        'Participants': {
                            'Users': [
                                {
                                    'Id': 'string',
                                    'Username': 'string',
                                    'GivenName': 'string',
                                    'Surname': 'string',
                                    'EmailAddress': 'string'
                                },
                            ],
                            'Groups': [
                                {
                                    'Id': 'string',
                                    'Name': 'string'
                                },
                            ]
                        },
                        'ResourceMetadata': {
                            'Type': 'FOLDER'|'DOCUMENT',
                            'Name': 'string',
                            'OriginalName': 'string',
                            'Id': 'string',
                            'VersionId': 'string',
                            'Owner': {
                                'Id': 'string',
                                'Username': 'string',
                                'GivenName': 'string',
                                'Surname': 'string',
                                'EmailAddress': 'string'
                            },
                            'ParentId': 'string'
                        },
                        'OriginalParent': {
                            'Type': 'FOLDER'|'DOCUMENT',
                            'Name': 'string',
                            'OriginalName': 'string',
                            'Id': 'string',
                            'VersionId': 'string',
                            'Owner': {
                                'Id': 'string',
                                'Username': 'string',
                                'GivenName': 'string',
                                'Surname': 'string',
                                'EmailAddress': 'string'
                            },
                            'ParentId': 'string'
                        },
                        'CommentMetadata': {
                            'CommentId': 'string',
                            'Contributor': {
                                'Id': 'string',
                                'Username': 'string',
                                'EmailAddress': 'string',
                                'GivenName': 'string',
                                'Surname': 'string',
                                'OrganizationId': 'string',
                                'RootFolderId': 'string',
                                'RecycleBinFolderId': 'string',
                                'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
                                'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
                                'CreatedTimestamp': datetime(2015, 1, 1),
                                'ModifiedTimestamp': datetime(2015, 1, 1),
                                'TimeZoneId': 'string',
                                'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
                                'Storage': {
                                    'StorageUtilizedInBytes': 123,
                                    'StorageRule': {
                                        'StorageAllocatedInBytes': 123,
                                        'StorageType': 'UNLIMITED'|'QUOTA'
                                    }
                                }
                            },
                            'CreatedTimestamp': datetime(2015, 1, 1),
                            'CommentStatus': 'DRAFT'|'PUBLISHED'|'DELETED',
                            'RecipientId': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **UserActivities** *(list) --* 
              The list of activities for the specified user and time period.
              - *(dict) --* 
                Describes the activity information.
                - **Type** *(string) --* 
                  The activity type.
                - **TimeStamp** *(datetime) --* 
                  The timestamp when the action was performed.
                - **IsIndirectActivity** *(boolean) --* 
                  Indicates whether an activity is indirect or direct. An indirect activity results from a direct activity performed on a parent resource. For example, sharing a parent folder (the direct activity) shares all of the subfolders and documents within the parent folder (the indirect activity).
                - **OrganizationId** *(string) --* 
                  The ID of the organization.
                - **Initiator** *(dict) --* 
                  The user who performed the action.
                  - **Id** *(string) --* 
                    The ID of the user.
                  - **Username** *(string) --* 
                    The name of the user.
                  - **GivenName** *(string) --* 
                    The given name of the user before a rename operation.
                  - **Surname** *(string) --* 
                    The surname of the user.
                  - **EmailAddress** *(string) --* 
                    The email address of the user.
                - **Participants** *(dict) --* 
                  The list of users or groups impacted by this action. This is an optional field and is filled for the following sharing activities: DOCUMENT_SHARED, DOCUMENT_SHARED, DOCUMENT_UNSHARED, FOLDER_SHARED, FOLDER_UNSHARED.
                  - **Users** *(list) --* 
                    The list of users.
                    - *(dict) --* 
                      Describes the metadata of the user.
                      - **Id** *(string) --* 
                        The ID of the user.
                      - **Username** *(string) --* 
                        The name of the user.
                      - **GivenName** *(string) --* 
                        The given name of the user before a rename operation.
                      - **Surname** *(string) --* 
                        The surname of the user.
                      - **EmailAddress** *(string) --* 
                        The email address of the user.
                  - **Groups** *(list) --* 
                    The list of user groups.
                    - *(dict) --* 
                      Describes the metadata of a user group.
                      - **Id** *(string) --* 
                        The ID of the user group.
                      - **Name** *(string) --* 
                        The name of the group.
                - **ResourceMetadata** *(dict) --* 
                  The metadata of the resource involved in the user action.
                  - **Type** *(string) --* 
                    The type of resource.
                  - **Name** *(string) --* 
                    The name of the resource.
                  - **OriginalName** *(string) --* 
                    The original name of the resource before a rename operation.
                  - **Id** *(string) --* 
                    The ID of the resource.
                  - **VersionId** *(string) --* 
                    The version ID of the resource. This is an optional field and is filled for action on document version.
                  - **Owner** *(dict) --* 
                    The owner of the resource.
                    - **Id** *(string) --* 
                      The ID of the user.
                    - **Username** *(string) --* 
                      The name of the user.
                    - **GivenName** *(string) --* 
                      The given name of the user before a rename operation.
                    - **Surname** *(string) --* 
                      The surname of the user.
                    - **EmailAddress** *(string) --* 
                      The email address of the user.
                  - **ParentId** *(string) --* 
                    The parent ID of the resource before a rename operation.
                - **OriginalParent** *(dict) --* 
                  The original parent of the resource. This is an optional field and is filled for move activities.
                  - **Type** *(string) --* 
                    The type of resource.
                  - **Name** *(string) --* 
                    The name of the resource.
                  - **OriginalName** *(string) --* 
                    The original name of the resource before a rename operation.
                  - **Id** *(string) --* 
                    The ID of the resource.
                  - **VersionId** *(string) --* 
                    The version ID of the resource. This is an optional field and is filled for action on document version.
                  - **Owner** *(dict) --* 
                    The owner of the resource.
                    - **Id** *(string) --* 
                      The ID of the user.
                    - **Username** *(string) --* 
                      The name of the user.
                    - **GivenName** *(string) --* 
                      The given name of the user before a rename operation.
                    - **Surname** *(string) --* 
                      The surname of the user.
                    - **EmailAddress** *(string) --* 
                      The email address of the user.
                  - **ParentId** *(string) --* 
                    The parent ID of the resource before a rename operation.
                - **CommentMetadata** *(dict) --* 
                  Metadata of the commenting activity. This is an optional field and is filled for commenting activities.
                  - **CommentId** *(string) --* 
                    The ID of the comment.
                  - **Contributor** *(dict) --* 
                    The user who made the comment.
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
                  - **CreatedTimestamp** *(datetime) --* 
                    The timestamp that the comment was created.
                  - **CommentStatus** *(string) --* 
                    The status of the comment.
                  - **RecipientId** *(string) --* 
                    The ID of the user being replied to.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type AuthenticationToken: string
        :param AuthenticationToken:
          Amazon WorkDocs authentication token. Do not set this field when using administrative API actions, as in accessing the API using AWS credentials.
        :type StartTime: datetime
        :param StartTime:
          The timestamp that determines the starting time of the activities. The response includes the activities performed after the specified timestamp.
        :type EndTime: datetime
        :param EndTime:
          The timestamp that determines the end time of the activities. The response includes the activities performed before the specified timestamp.
        :type OrganizationId: string
        :param OrganizationId:
          The ID of the organization. This is a mandatory parameter when using administrative API (SigV4) requests.
        :type ActivityTypes: string
        :param ActivityTypes:
          Specifies which activity types to include in the response. If this field is left empty, all activity types are returned.
        :type ResourceId: string
        :param ResourceId:
          The document or folder ID for which to describe activity types.
        :type UserId: string
        :param UserId:
          The ID of the user who performed the action. The response includes activities pertaining to this user. This is an optional parameter and is only applicable for administrative API (SigV4) requests.
        :type IncludeIndirectActivities: boolean
        :param IncludeIndirectActivities:
          Includes indirect activities. An indirect activity results from a direct activity performed on a parent resource. For example, sharing a parent folder (the direct activity) shares all of the subfolders and documents within the parent folder (the indirect activity).
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
        """
        pass


class DescribeComments(Paginator):
    def paginate(self, DocumentId: str, VersionId: str, AuthenticationToken: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkDocs.Client.describe_comments`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/DescribeComments>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AuthenticationToken='string',
              DocumentId='string',
              VersionId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Comments': [
                    {
                        'CommentId': 'string',
                        'ParentId': 'string',
                        'ThreadId': 'string',
                        'Text': 'string',
                        'Contributor': {
                            'Id': 'string',
                            'Username': 'string',
                            'EmailAddress': 'string',
                            'GivenName': 'string',
                            'Surname': 'string',
                            'OrganizationId': 'string',
                            'RootFolderId': 'string',
                            'RecycleBinFolderId': 'string',
                            'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
                            'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
                            'CreatedTimestamp': datetime(2015, 1, 1),
                            'ModifiedTimestamp': datetime(2015, 1, 1),
                            'TimeZoneId': 'string',
                            'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
                            'Storage': {
                                'StorageUtilizedInBytes': 123,
                                'StorageRule': {
                                    'StorageAllocatedInBytes': 123,
                                    'StorageType': 'UNLIMITED'|'QUOTA'
                                }
                            }
                        },
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'Status': 'DRAFT'|'PUBLISHED'|'DELETED',
                        'Visibility': 'PUBLIC'|'PRIVATE',
                        'RecipientId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Comments** *(list) --* 
              The list of comments for the specified document version.
              - *(dict) --* 
                Describes a comment.
                - **CommentId** *(string) --* 
                  The ID of the comment.
                - **ParentId** *(string) --* 
                  The ID of the parent comment.
                - **ThreadId** *(string) --* 
                  The ID of the root comment in the thread.
                - **Text** *(string) --* 
                  The text of the comment.
                - **Contributor** *(dict) --* 
                  The details of the user who made the comment.
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
                - **CreatedTimestamp** *(datetime) --* 
                  The time that the comment was created.
                - **Status** *(string) --* 
                  The status of the comment.
                - **Visibility** *(string) --* 
                  The visibility of the comment. Options are either PRIVATE, where the comment is visible only to the comment author and document owner and co-owners, or PUBLIC, where the comment is visible to document owners, co-owners, and contributors.
                - **RecipientId** *(string) --* 
                  If the comment is a reply to another user's comment, this field contains the user ID of the user being replied to.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type AuthenticationToken: string
        :param AuthenticationToken:
          Amazon WorkDocs authentication token. Do not set this field when using administrative API actions, as in accessing the API using AWS credentials.
        :type DocumentId: string
        :param DocumentId: **[REQUIRED]**
          The ID of the document.
        :type VersionId: string
        :param VersionId: **[REQUIRED]**
          The ID of the document version.
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
        """
        pass


class DescribeDocumentVersions(Paginator):
    def paginate(self, DocumentId: str, AuthenticationToken: str = None, Include: str = None, Fields: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkDocs.Client.describe_document_versions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/DescribeDocumentVersions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AuthenticationToken='string',
              DocumentId='string',
              Include='string',
              Fields='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'DocumentVersions': [
                    {
                        'Id': 'string',
                        'Name': 'string',
                        'ContentType': 'string',
                        'Size': 123,
                        'Signature': 'string',
                        'Status': 'INITIALIZED'|'ACTIVE',
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'ModifiedTimestamp': datetime(2015, 1, 1),
                        'ContentCreatedTimestamp': datetime(2015, 1, 1),
                        'ContentModifiedTimestamp': datetime(2015, 1, 1),
                        'CreatorId': 'string',
                        'Thumbnail': {
                            'string': 'string'
                        },
                        'Source': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
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
        """
        pass


class DescribeFolderContents(Paginator):
    def paginate(self, FolderId: str, AuthenticationToken: str = None, Sort: str = None, Order: str = None, Type: str = None, Include: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkDocs.Client.describe_folder_contents`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/DescribeFolderContents>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AuthenticationToken='string',
              FolderId='string',
              Sort='DATE'|'NAME',
              Order='ASCENDING'|'DESCENDING',
              Type='ALL'|'DOCUMENT'|'FOLDER',
              Include='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Folders': [
                    {
                        'Id': 'string',
                        'Name': 'string',
                        'CreatorId': 'string',
                        'ParentFolderId': 'string',
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'ModifiedTimestamp': datetime(2015, 1, 1),
                        'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
                        'Signature': 'string',
                        'Labels': [
                            'string',
                        ],
                        'Size': 123,
                        'LatestVersionSize': 123
                    },
                ],
                'Documents': [
                    {
                        'Id': 'string',
                        'CreatorId': 'string',
                        'ParentFolderId': 'string',
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'ModifiedTimestamp': datetime(2015, 1, 1),
                        'LatestVersionMetadata': {
                            'Id': 'string',
                            'Name': 'string',
                            'ContentType': 'string',
                            'Size': 123,
                            'Signature': 'string',
                            'Status': 'INITIALIZED'|'ACTIVE',
                            'CreatedTimestamp': datetime(2015, 1, 1),
                            'ModifiedTimestamp': datetime(2015, 1, 1),
                            'ContentCreatedTimestamp': datetime(2015, 1, 1),
                            'ContentModifiedTimestamp': datetime(2015, 1, 1),
                            'CreatorId': 'string',
                            'Thumbnail': {
                                'string': 'string'
                            },
                            'Source': {
                                'string': 'string'
                            }
                        },
                        'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
                        'Labels': [
                            'string',
                        ]
                    },
                ],
                'NextToken': 'string'
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
        """
        pass


class DescribeGroups(Paginator):
    def paginate(self, SearchQuery: str, AuthenticationToken: str = None, OrganizationId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkDocs.Client.describe_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/DescribeGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AuthenticationToken='string',
              SearchQuery='string',
              OrganizationId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Groups': [
                    {
                        'Id': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Groups** *(list) --* 
              The list of groups.
              - *(dict) --* 
                Describes the metadata of a user group.
                - **Id** *(string) --* 
                  The ID of the user group.
                - **Name** *(string) --* 
                  The name of the group.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type AuthenticationToken: string
        :param AuthenticationToken:
          Amazon WorkDocs authentication token. Do not set this field when using administrative API actions, as in accessing the API using AWS credentials.
        :type SearchQuery: string
        :param SearchQuery: **[REQUIRED]**
          A query to describe groups by group name.
        :type OrganizationId: string
        :param OrganizationId:
          The ID of the organization.
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
        """
        pass


class DescribeNotificationSubscriptions(Paginator):
    def paginate(self, OrganizationId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkDocs.Client.describe_notification_subscriptions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/DescribeNotificationSubscriptions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              OrganizationId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Subscriptions': [
                    {
                        'SubscriptionId': 'string',
                        'EndPoint': 'string',
                        'Protocol': 'HTTPS'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Subscriptions** *(list) --* 
              The subscriptions.
              - *(dict) --* 
                Describes a subscription.
                - **SubscriptionId** *(string) --* 
                  The ID of the subscription.
                - **EndPoint** *(string) --* 
                  The endpoint of the subscription.
                - **Protocol** *(string) --* 
                  The protocol of the subscription.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**
          The ID of the organization.
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
        """
        pass


class DescribeResourcePermissions(Paginator):
    def paginate(self, ResourceId: str, AuthenticationToken: str = None, PrincipalId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkDocs.Client.describe_resource_permissions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/DescribeResourcePermissions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AuthenticationToken='string',
              ResourceId='string',
              PrincipalId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Principals': [
                    {
                        'Id': 'string',
                        'Type': 'USER'|'GROUP'|'INVITE'|'ANONYMOUS'|'ORGANIZATION',
                        'Roles': [
                            {
                                'Role': 'VIEWER'|'CONTRIBUTOR'|'OWNER'|'COOWNER',
                                'Type': 'DIRECT'|'INHERITED'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Principals** *(list) --* 
              The principals.
              - *(dict) --* 
                Describes a resource.
                - **Id** *(string) --* 
                  The ID of the resource.
                - **Type** *(string) --* 
                  The type of resource.
                - **Roles** *(list) --* 
                  The permission information for the resource.
                  - *(dict) --* 
                    Describes the permissions.
                    - **Role** *(string) --* 
                      The role of the user.
                    - **Type** *(string) --* 
                      The type of permissions.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type AuthenticationToken: string
        :param AuthenticationToken:
          Amazon WorkDocs authentication token. Do not set this field when using administrative API actions, as in accessing the API using AWS credentials.
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**
          The ID of the resource.
        :type PrincipalId: string
        :param PrincipalId:
          The ID of the principal to filter permissions by.
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
        """
        pass


class DescribeRootFolders(Paginator):
    def paginate(self, AuthenticationToken: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkDocs.Client.describe_root_folders`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/DescribeRootFolders>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AuthenticationToken='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Folders': [
                    {
                        'Id': 'string',
                        'Name': 'string',
                        'CreatorId': 'string',
                        'ParentFolderId': 'string',
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'ModifiedTimestamp': datetime(2015, 1, 1),
                        'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
                        'Signature': 'string',
                        'Labels': [
                            'string',
                        ],
                        'Size': 123,
                        'LatestVersionSize': 123
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Folders** *(list) --* 
              The user's special folders.
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type AuthenticationToken: string
        :param AuthenticationToken: **[REQUIRED]**
          Amazon WorkDocs authentication token. Do not set this field when using administrative API actions, as in accessing the API using AWS credentials.
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
        """
        pass


class DescribeUsers(Paginator):
    def paginate(self, AuthenticationToken: str = None, OrganizationId: str = None, UserIds: str = None, Query: str = None, Include: str = None, Order: str = None, Sort: str = None, Fields: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkDocs.Client.describe_users`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/DescribeUsers>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AuthenticationToken='string',
              OrganizationId='string',
              UserIds='string',
              Query='string',
              Include='ALL'|'ACTIVE_PENDING',
              Order='ASCENDING'|'DESCENDING',
              Sort='USER_NAME'|'FULL_NAME'|'STORAGE_LIMIT'|'USER_STATUS'|'STORAGE_USED',
              Fields='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Users': [
                    {
                        'Id': 'string',
                        'Username': 'string',
                        'EmailAddress': 'string',
                        'GivenName': 'string',
                        'Surname': 'string',
                        'OrganizationId': 'string',
                        'RootFolderId': 'string',
                        'RecycleBinFolderId': 'string',
                        'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
                        'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'ModifiedTimestamp': datetime(2015, 1, 1),
                        'TimeZoneId': 'string',
                        'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
                        'Storage': {
                            'StorageUtilizedInBytes': 123,
                            'StorageRule': {
                                'StorageAllocatedInBytes': 123,
                                'StorageType': 'UNLIMITED'|'QUOTA'
                            }
                        }
                    },
                ],
                'TotalNumberOfUsers': 123,
                'NextToken': 'string'
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
        """
        pass
