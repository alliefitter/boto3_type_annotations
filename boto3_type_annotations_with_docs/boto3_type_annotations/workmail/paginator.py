from typing import Dict
from botocore.paginate import Paginator


class ListAliases(Paginator):
    def paginate(self, OrganizationId: str, EntityId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkMail.Client.list_aliases`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListAliases>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              OrganizationId='string',
              EntityId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Aliases': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Aliases** *(list) --* 
              The entity's paginated aliases.
              - *(string) --* 
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**
          The identifier for the organization under which the entity exists.
        :type EntityId: string
        :param EntityId: **[REQUIRED]**
          The identifier for the entity for which to list the aliases.
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


class ListGroupMembers(Paginator):
    def paginate(self, OrganizationId: str, GroupId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkMail.Client.list_group_members`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListGroupMembers>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              OrganizationId='string',
              GroupId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Members': [
                    {
                        'Id': 'string',
                        'Name': 'string',
                        'Type': 'GROUP'|'USER',
                        'State': 'ENABLED'|'DISABLED'|'DELETED',
                        'EnabledDate': datetime(2015, 1, 1),
                        'DisabledDate': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Members** *(list) --* 
              The members associated to the group.
              - *(dict) --* 
                The representation of a user or group.
                - **Id** *(string) --* 
                  The identifier of the member.
                - **Name** *(string) --* 
                  The name of the member.
                - **Type** *(string) --* 
                  A member can be a user or group.
                - **State** *(string) --* 
                  The state of the member, which can be ENABLED, DISABLED, or DELETED.
                - **EnabledDate** *(datetime) --* 
                  The date indicating when the member was enabled for Amazon WorkMail use.
                - **DisabledDate** *(datetime) --* 
                  The date indicating when the member was disabled from Amazon WorkMail use.
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**
          The identifier for the organization under which the group exists.
        :type GroupId: string
        :param GroupId: **[REQUIRED]**
          The identifier for the group to which the members (users or groups) are associated.
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


class ListGroups(Paginator):
    def paginate(self, OrganizationId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkMail.Client.list_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListGroups>`_
        
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
                'Groups': [
                    {
                        'Id': 'string',
                        'Email': 'string',
                        'Name': 'string',
                        'State': 'ENABLED'|'DISABLED'|'DELETED',
                        'EnabledDate': datetime(2015, 1, 1),
                        'DisabledDate': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Groups** *(list) --* 
              The overview of groups for an organization.
              - *(dict) --* 
                The representation of an Amazon WorkMail group.
                - **Id** *(string) --* 
                  The identifier of the group.
                - **Email** *(string) --* 
                  The email of the group.
                - **Name** *(string) --* 
                  The name of the group.
                - **State** *(string) --* 
                  The state of the group, which can be ENABLED, DISABLED, or DELETED.
                - **EnabledDate** *(datetime) --* 
                  The date indicating when the group was enabled for Amazon WorkMail use.
                - **DisabledDate** *(datetime) --* 
                  The date indicating when the group was disabled from Amazon WorkMail use.
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**
          The identifier for the organization under which the groups exist.
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


class ListMailboxPermissions(Paginator):
    def paginate(self, OrganizationId: str, EntityId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkMail.Client.list_mailbox_permissions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListMailboxPermissions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              OrganizationId='string',
              EntityId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Permissions': [
                    {
                        'GranteeId': 'string',
                        'GranteeType': 'GROUP'|'USER',
                        'PermissionValues': [
                            'FULL_ACCESS'|'SEND_AS'|'SEND_ON_BEHALF',
                        ]
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Permissions** *(list) --* 
              One page of the user, group, or resource mailbox permissions.
              - *(dict) --* 
                Permission granted to a user, group, or resource to access a certain aspect of another user, group, or resource mailbox.
                - **GranteeId** *(string) --* 
                  The identifier of the user, group, or resource to which the permissions are granted.
                - **GranteeType** *(string) --* 
                  The type of user, group, or resource referred to in GranteeId.
                - **PermissionValues** *(list) --* 
                  The permissions granted to the grantee. SEND_AS allows the grantee to send email as the owner of the mailbox (the grantee is not mentioned on these emails). SEND_ON_BEHALF allows the grantee to send email on behalf of the owner of the mailbox (the grantee is not mentioned as the physical sender of these emails). FULL_ACCESS allows the grantee full access to the mailbox, irrespective of other folder-level permissions set on the mailbox.
                  - *(string) --* 
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**
          The identifier of the organization under which the user, group, or resource exists.
        :type EntityId: string
        :param EntityId: **[REQUIRED]**
          The identifier of the user, group, or resource for which to list mailbox permissions.
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


class ListOrganizations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkMail.Client.list_organizations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListOrganizations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'OrganizationSummaries': [
                    {
                        'OrganizationId': 'string',
                        'Alias': 'string',
                        'ErrorMessage': 'string',
                        'State': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **OrganizationSummaries** *(list) --* 
              The overview of owned organizations presented as a list of organization summaries.
              - *(dict) --* 
                The representation of an organization.
                - **OrganizationId** *(string) --* 
                  The identifier associated with the organization.
                - **Alias** *(string) --* 
                  The alias associated with the organization.
                - **ErrorMessage** *(string) --* 
                  The error message associated with the organization. It is only present if unexpected behavior has occurred with regards to the organization. It provides insight or solutions regarding unexpected behavior.
                - **State** *(string) --* 
                  The state associated with the organization.
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


class ListResourceDelegates(Paginator):
    def paginate(self, OrganizationId: str, ResourceId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkMail.Client.list_resource_delegates`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListResourceDelegates>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              OrganizationId='string',
              ResourceId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Delegates': [
                    {
                        'Id': 'string',
                        'Type': 'GROUP'|'USER'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Delegates** *(list) --* 
              One page of the resource's delegates.
              - *(dict) --* 
                The name of the attribute, which is one of the values defined in the UserAttribute enumeration.
                - **Id** *(string) --* 
                  The identifier for the user or group associated as the resource's delegate.
                - **Type** *(string) --* 
                  The type of the delegate: user or group.
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**
          The identifier for the organization that contains the resource for which delegates are listed.
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**
          The identifier for the resource whose delegates are listed.
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


class ListResources(Paginator):
    def paginate(self, OrganizationId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkMail.Client.list_resources`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListResources>`_
        
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
                'Resources': [
                    {
                        'Id': 'string',
                        'Email': 'string',
                        'Name': 'string',
                        'Type': 'ROOM'|'EQUIPMENT',
                        'State': 'ENABLED'|'DISABLED'|'DELETED',
                        'EnabledDate': datetime(2015, 1, 1),
                        'DisabledDate': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Resources** *(list) --* 
              One page of the organization's resource representation.
              - *(dict) --* 
                The representation of a resource.
                - **Id** *(string) --* 
                  The identifier of the resource.
                - **Email** *(string) --* 
                  The email of the resource.
                - **Name** *(string) --* 
                  The name of the resource.
                - **Type** *(string) --* 
                  The type of the resource: equipment or room.
                - **State** *(string) --* 
                  The state of the resource, which can be ENABLED, DISABLED, or DELETED.
                - **EnabledDate** *(datetime) --* 
                  The date indicating when the resource was enabled for Amazon WorkMail use.
                - **DisabledDate** *(datetime) --* 
                  The date indicating when the resource was disabled from Amazon WorkMail use.
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**
          The identifier for the organization under which the resources exist.
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


class ListUsers(Paginator):
    def paginate(self, OrganizationId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WorkMail.Client.list_users`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListUsers>`_
        
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
                'Users': [
                    {
                        'Id': 'string',
                        'Email': 'string',
                        'Name': 'string',
                        'DisplayName': 'string',
                        'State': 'ENABLED'|'DISABLED'|'DELETED',
                        'UserRole': 'USER'|'RESOURCE'|'SYSTEM_USER',
                        'EnabledDate': datetime(2015, 1, 1),
                        'DisabledDate': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Users** *(list) --* 
              The overview of users for an organization.
              - *(dict) --* 
                The representation of an Amazon WorkMail user.
                - **Id** *(string) --* 
                  The identifier of the user.
                - **Email** *(string) --* 
                  The email of the user.
                - **Name** *(string) --* 
                  The name of the user.
                - **DisplayName** *(string) --* 
                  The display name of the user.
                - **State** *(string) --* 
                  The state of the user, which can be ENABLED, DISABLED, or DELETED.
                - **UserRole** *(string) --* 
                  The role of the user.
                - **EnabledDate** *(datetime) --* 
                  The date indicating when the user was enabled for Amazon WorkMail use.
                - **DisabledDate** *(datetime) --* 
                  The date indicating when the user was disabled from Amazon WorkMail use.
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**
          The identifier for the organization under which the users exist.
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
