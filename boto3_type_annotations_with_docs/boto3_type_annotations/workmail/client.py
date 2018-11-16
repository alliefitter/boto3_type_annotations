from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def associate_delegate_to_resource(self, OrganizationId: str, ResourceId: str, EntityId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/AssociateDelegateToResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_delegate_to_resource(
              OrganizationId=\'string\',
              ResourceId=\'string\',
              EntityId=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The organization under which the resource exists.
        
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The resource for which members are associated.
        
        :type EntityId: string
        :param EntityId: **[REQUIRED]** 
        
          The member (user or group) to associate to the resource.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def associate_member_to_group(self, OrganizationId: str, GroupId: str, MemberId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/AssociateMemberToGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_member_to_group(
              OrganizationId=\'string\',
              GroupId=\'string\',
              MemberId=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The organization under which the group exists.
        
        :type GroupId: string
        :param GroupId: **[REQUIRED]** 
        
          The group for which the member is associated.
        
        :type MemberId: string
        :param MemberId: **[REQUIRED]** 
        
          The member to associate to the group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
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

    def create_alias(self, OrganizationId: str, EntityId: str, Alias: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/CreateAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_alias(
              OrganizationId=\'string\',
              EntityId=\'string\',
              Alias=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The organization under which the member exists.
        
        :type EntityId: string
        :param EntityId: **[REQUIRED]** 
        
          The alias is added to this Amazon WorkMail entity.
        
        :type Alias: string
        :param Alias: **[REQUIRED]** 
        
          The alias to add to the user.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def create_group(self, OrganizationId: str, Name: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/CreateGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_group(
              OrganizationId=\'string\',
              Name=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The organization under which the group is to be created.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GroupId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **GroupId** *(string) --* 
        
              The ID of the group.
        
        """
        pass

    def create_resource(self, OrganizationId: str, Name: str, Type: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/CreateResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_resource(
              OrganizationId=\'string\',
              Name=\'string\',
              Type=\'ROOM\'|\'EQUIPMENT\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier associated with the organization for which the resource is created.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the created resource.
        
        :type Type: string
        :param Type: **[REQUIRED]** 
        
          The type of the created resource.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ResourceId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ResourceId** *(string) --* 
        
              The identifier of the created resource.
        
        """
        pass

    def create_user(self, OrganizationId: str, Name: str, DisplayName: str, Password: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/CreateUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_user(
              OrganizationId=\'string\',
              Name=\'string\',
              DisplayName=\'string\',
              Password=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier of the organization for which the user is created.
        
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name for the user to be created.
        
        :type DisplayName: string
        :param DisplayName: **[REQUIRED]** 
        
          The display name for the user to be created.
        
        :type Password: string
        :param Password: **[REQUIRED]** 
        
          The password for the user to be created.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UserId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **UserId** *(string) --* 
        
              The information regarding the newly created user.
        
        """
        pass

    def delete_alias(self, OrganizationId: str, EntityId: str, Alias: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeleteAlias>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_alias(
              OrganizationId=\'string\',
              EntityId=\'string\',
              Alias=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier for the organization under which the user exists.
        
        :type EntityId: string
        :param EntityId: **[REQUIRED]** 
        
          The identifier for the Amazon WorkMail entity to have the aliases removed.
        
        :type Alias: string
        :param Alias: **[REQUIRED]** 
        
          The aliases to be removed from the user\'s set of aliases. Duplicate entries in the list are collapsed into single entries (the list is transformed into a set).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_group(self, OrganizationId: str, GroupId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeleteGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_group(
              OrganizationId=\'string\',
              GroupId=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The organization that contains the group.
        
        :type GroupId: string
        :param GroupId: **[REQUIRED]** 
        
          The identifier of the group to be deleted.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_mailbox_permissions(self, OrganizationId: str, EntityId: str, GranteeId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeleteMailboxPermissions>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_mailbox_permissions(
              OrganizationId=\'string\',
              EntityId=\'string\',
              GranteeId=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier of the organization under which the entity (user or group) exists.
        
        :type EntityId: string
        :param EntityId: **[REQUIRED]** 
        
          The identifier of the entity (user or group) for which to delete mailbox permissions.
        
        :type GranteeId: string
        :param GranteeId: **[REQUIRED]** 
        
          The identifier of the entity (user or group) for which to delete granted permissions.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_resource(self, OrganizationId: str, ResourceId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeleteResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_resource(
              OrganizationId=\'string\',
              ResourceId=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier associated with the organization for which the resource is deleted.
        
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The identifier of the resource to be deleted.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_user(self, OrganizationId: str, UserId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeleteUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_user(
              OrganizationId=\'string\',
              UserId=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The organization that contains the user.
        
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The identifier of the user to be deleted.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def deregister_from_work_mail(self, OrganizationId: str, EntityId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeregisterFromWorkMail>`_
        
        **Request Syntax** 
        ::
        
          response = client.deregister_from_work_mail(
              OrganizationId=\'string\',
              EntityId=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier for the organization under which the Amazon WorkMail entity exists.
        
        :type EntityId: string
        :param EntityId: **[REQUIRED]** 
        
          The identifier for the entity to be updated.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_group(self, OrganizationId: str, GroupId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DescribeGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_group(
              OrganizationId=\'string\',
              GroupId=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier for the organization under which the group exists.
        
        :type GroupId: string
        :param GroupId: **[REQUIRED]** 
        
          The identifier for the group to be described.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GroupId\': \'string\',
                \'Name\': \'string\',
                \'Email\': \'string\',
                \'State\': \'ENABLED\'|\'DISABLED\'|\'DELETED\',
                \'EnabledDate\': datetime(2015, 1, 1),
                \'DisabledDate\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **GroupId** *(string) --* 
        
              The identifier of the described group.
        
            - **Name** *(string) --* 
        
              The name of the described group.
        
            - **Email** *(string) --* 
        
              The email of the described group.
        
            - **State** *(string) --* 
        
              The state of the user: enabled (registered to Amazon WorkMail) or disabled (deregistered or never registered to Amazon WorkMail).
        
            - **EnabledDate** *(datetime) --* 
        
              The date and time when a user was registered to Amazon WorkMail, in UNIX epoch time format.
        
            - **DisabledDate** *(datetime) --* 
        
              The date and time when a user was deregistered from Amazon WorkMail, in UNIX epoch time format.
        
        """
        pass

    def describe_organization(self, OrganizationId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DescribeOrganization>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_organization(
              OrganizationId=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier for the organization to be described.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OrganizationId\': \'string\',
                \'Alias\': \'string\',
                \'State\': \'string\',
                \'DirectoryId\': \'string\',
                \'DirectoryType\': \'string\',
                \'DefaultMailDomain\': \'string\',
                \'CompletedDate\': datetime(2015, 1, 1),
                \'ErrorMessage\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **OrganizationId** *(string) --* 
        
              The identifier of an organization.
        
            - **Alias** *(string) --* 
        
              The alias for an organization.
        
            - **State** *(string) --* 
        
              The state of an organization.
        
            - **DirectoryId** *(string) --* 
        
              The identifier for the directory associated with an Amazon WorkMail organization.
        
            - **DirectoryType** *(string) --* 
        
              The type of directory associated with the Amazon WorkMail organization.
        
            - **DefaultMailDomain** *(string) --* 
        
              The default mail domain associated with the organization.
        
            - **CompletedDate** *(datetime) --* 
        
              The date at which the organization became usable in the Amazon WorkMail context, in UNIX epoch time format.
        
            - **ErrorMessage** *(string) --* 
        
              The (optional) error message indicating if unexpected behavior was encountered with regards to the organization.
        
        """
        pass

    def describe_resource(self, OrganizationId: str, ResourceId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DescribeResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_resource(
              OrganizationId=\'string\',
              ResourceId=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier associated with the organization for which the resource is described.
        
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The identifier of the resource to be described.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ResourceId\': \'string\',
                \'Email\': \'string\',
                \'Name\': \'string\',
                \'Type\': \'ROOM\'|\'EQUIPMENT\',
                \'BookingOptions\': {
                    \'AutoAcceptRequests\': True|False,
                    \'AutoDeclineRecurringRequests\': True|False,
                    \'AutoDeclineConflictingRequests\': True|False
                },
                \'State\': \'ENABLED\'|\'DISABLED\'|\'DELETED\',
                \'EnabledDate\': datetime(2015, 1, 1),
                \'DisabledDate\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ResourceId** *(string) --* 
        
              The identifier of the described resource.
        
            - **Email** *(string) --* 
        
              The email of the described resource.
        
            - **Name** *(string) --* 
        
              The name of the described resource.
        
            - **Type** *(string) --* 
        
              The type of the described resource.
        
            - **BookingOptions** *(dict) --* 
        
              The booking options for the described resource.
        
              - **AutoAcceptRequests** *(boolean) --* 
        
                The resource\'s ability to automatically reply to requests. If disabled, delegates must be associated to the resource.
        
              - **AutoDeclineRecurringRequests** *(boolean) --* 
        
                The resource\'s ability to automatically decline any recurring requests.
        
              - **AutoDeclineConflictingRequests** *(boolean) --* 
        
                The resource\'s ability to automatically decline any conflicting requests.
        
            - **State** *(string) --* 
        
              The state of the resource: enabled (registered to Amazon WorkMail) or disabled (deregistered or never registered to Amazon WorkMail).
        
            - **EnabledDate** *(datetime) --* 
        
              The date and time when a resource was registered to Amazon WorkMail, in UNIX epoch time format.
        
            - **DisabledDate** *(datetime) --* 
        
              The date and time when a resource was registered from Amazon WorkMail, in UNIX epoch time format.
        
        """
        pass

    def describe_user(self, OrganizationId: str, UserId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DescribeUser>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_user(
              OrganizationId=\'string\',
              UserId=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier for the organization under which the user exists.
        
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The identifier for the user to be described.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UserId\': \'string\',
                \'Name\': \'string\',
                \'Email\': \'string\',
                \'DisplayName\': \'string\',
                \'State\': \'ENABLED\'|\'DISABLED\'|\'DELETED\',
                \'UserRole\': \'USER\'|\'RESOURCE\'|\'SYSTEM_USER\',
                \'EnabledDate\': datetime(2015, 1, 1),
                \'DisabledDate\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **UserId** *(string) --* 
        
              The identifier for the described user.
        
            - **Name** *(string) --* 
        
              The name for the user.
        
            - **Email** *(string) --* 
        
              The email of the user.
        
            - **DisplayName** *(string) --* 
        
              The display name of the user.
        
            - **State** *(string) --* 
        
              The state of a user: enabled (registered to Amazon WorkMail) or disabled (deregistered or never registered to Amazon WorkMail).
        
            - **UserRole** *(string) --* 
        
              In certain cases other entities are modeled as users. If interoperability is enabled, resources are imported into Amazon WorkMail as users. Because different Amazon WorkMail organizations rely on different directory types, administrators can distinguish between a user that is not registered to Amazon WorkMail (is disabled and has a user role) and the administrative users of the directory. The values are USER, RESOURCE, and SYSTEM_USER.
        
            - **EnabledDate** *(datetime) --* 
        
              The date and time at which the user was enabled for Amazon WorkMail usage, in UNIX epoch time format.
        
            - **DisabledDate** *(datetime) --* 
        
              The date and time at which the user was disabled for Amazon WorkMail usage, in UNIX epoch time format.
        
        """
        pass

    def disassociate_delegate_from_resource(self, OrganizationId: str, ResourceId: str, EntityId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DisassociateDelegateFromResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_delegate_from_resource(
              OrganizationId=\'string\',
              ResourceId=\'string\',
              EntityId=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier for the organization under which the resource exists.
        
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The identifier of the resource from which delegates\' set members are removed. 
        
        :type EntityId: string
        :param EntityId: **[REQUIRED]** 
        
          The identifier for the member (user, group) to be removed from the resource\'s delegates.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def disassociate_member_from_group(self, OrganizationId: str, GroupId: str, MemberId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DisassociateMemberFromGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_member_from_group(
              OrganizationId=\'string\',
              GroupId=\'string\',
              MemberId=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier for the organization under which the group exists.
        
        :type GroupId: string
        :param GroupId: **[REQUIRED]** 
        
          The identifier for the group from which members are removed.
        
        :type MemberId: string
        :param MemberId: **[REQUIRED]** 
        
          The identifier for the member to be removed to the group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
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

    def list_aliases(self, OrganizationId: str, EntityId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListAliases>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_aliases(
              OrganizationId=\'string\',
              EntityId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier for the organization under which the entity exists.
        
        :type EntityId: string
        :param EntityId: **[REQUIRED]** 
        
          The identifier for the entity for which to list the aliases.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to use to retrieve the next page of results. The first call does not contain any tokens.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Aliases\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Aliases** *(list) --* 
        
              The entity\'s paginated aliases.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next page of results. The value is \"null\" when there are no more results to return.
        
        """
        pass

    def list_group_members(self, OrganizationId: str, GroupId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListGroupMembers>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_group_members(
              OrganizationId=\'string\',
              GroupId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier for the organization under which the group exists.
        
        :type GroupId: string
        :param GroupId: **[REQUIRED]** 
        
          The identifier for the group to which the members are associated.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to use to retrieve the next page of results. The first call does not contain any tokens.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Members\': [
                    {
                        \'Id\': \'string\',
                        \'Name\': \'string\',
                        \'Type\': \'GROUP\'|\'USER\',
                        \'State\': \'ENABLED\'|\'DISABLED\'|\'DELETED\',
                        \'EnabledDate\': datetime(2015, 1, 1),
                        \'DisabledDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Members** *(list) --* 
        
              The members associated to the group.
        
              - *(dict) --* 
        
                The representation of a group member (user or group).
        
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
        
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next page of results. The first call does not contain any tokens.
        
        """
        pass

    def list_groups(self, OrganizationId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_groups(
              OrganizationId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier for the organization under which the groups exist.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to use to retrieve the next page of results. The first call does not contain any tokens.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Groups\': [
                    {
                        \'Id\': \'string\',
                        \'Email\': \'string\',
                        \'Name\': \'string\',
                        \'State\': \'ENABLED\'|\'DISABLED\'|\'DELETED\',
                        \'EnabledDate\': datetime(2015, 1, 1),
                        \'DisabledDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next page of results. The value is \"null\" when there are no more results to return.
        
        """
        pass

    def list_mailbox_permissions(self, OrganizationId: str, EntityId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListMailboxPermissions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_mailbox_permissions(
              OrganizationId=\'string\',
              EntityId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier of the organization under which the entity (user or group) exists.
        
        :type EntityId: string
        :param EntityId: **[REQUIRED]** 
        
          The identifier of the entity (user or group) for which to list mailbox permissions.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to use to retrieve the next page of results. The first call does not contain any tokens.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Permissions\': [
                    {
                        \'GranteeId\': \'string\',
                        \'GranteeType\': \'GROUP\'|\'USER\',
                        \'PermissionValues\': [
                            \'FULL_ACCESS\'|\'SEND_AS\'|\'SEND_ON_BEHALF\',
                        ]
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Permissions** *(list) --* 
        
              One page of the entity\'s mailbox permissions.
        
              - *(dict) --* 
        
                Permission granted to an entity (user, group) to access a certain aspect of another entity\'s mailbox.
        
                - **GranteeId** *(string) --* 
        
                  The identifier of the entity (user or group) to which the permissions are granted.
        
                - **GranteeType** *(string) --* 
        
                  The type of entity (user, group) of the entity referred to in GranteeId.
        
                - **PermissionValues** *(list) --* 
        
                  The permissions granted to the grantee. SEND_AS allows the grantee to send email as the owner of the mailbox (the grantee is not mentioned on these emails). SEND_ON_BEHALF allows the grantee to send email on behalf of the owner of the mailbox (the grantee is not mentioned as the physical sender of these emails). FULL_ACCESS allows the grantee full access to the mailbox, irrespective of other folder-level permissions set on the mailbox.
        
                  - *(string) --* 
              
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next page of results. The value is \"null\" when there are no more results to return.
        
        """
        pass

    def list_organizations(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListOrganizations>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_organizations(
              NextToken=\'string\',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken: 
        
          The token to use to retrieve the next page of results. The first call does not contain any tokens.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OrganizationSummaries\': [
                    {
                        \'OrganizationId\': \'string\',
                        \'Alias\': \'string\',
                        \'ErrorMessage\': \'string\',
                        \'State\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **OrganizationSummaries** *(list) --* 
        
              The overview of owned organizations presented as a list of organization summaries.
        
              - *(dict) --* 
        
                The brief overview associated with an organization.
        
                - **OrganizationId** *(string) --* 
        
                  The identifier associated with the organization.
        
                - **Alias** *(string) --* 
        
                  The alias associated with the organization.
        
                - **ErrorMessage** *(string) --* 
        
                  The error message associated with the organization. It is only present if unexpected behavior has occurred with regards to the organization. It provides insight or solutions regarding unexpected behavior.
        
                - **State** *(string) --* 
        
                  The state associated with the organization.
        
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next page of results. The value is \"null\" when there are no more results to return.
        
        """
        pass

    def list_resource_delegates(self, OrganizationId: str, ResourceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListResourceDelegates>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_resource_delegates(
              OrganizationId=\'string\',
              ResourceId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier for the organization that contains the resource for which delegates are listed.
        
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The identifier for the resource whose delegates are listed.
        
        :type NextToken: string
        :param NextToken: 
        
          The token used to paginate through the delegates associated with a resource.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The number of maximum results in a page.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Delegates\': [
                    {
                        \'Id\': \'string\',
                        \'Type\': \'GROUP\'|\'USER\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Delegates** *(list) --* 
        
              One page of the resource\'s delegates.
        
              - *(dict) --* 
        
                The name of the attribute, which is one of the values defined in the UserAttribute enumeration.
        
                - **Id** *(string) --* 
        
                  The identifier for the user or group is associated as the resource\'s delegate.
        
                - **Type** *(string) --* 
        
                  The type of the delegate: user or group.
        
            - **NextToken** *(string) --* 
        
              The token used to paginate through the delegates associated with a resource. While results are still available, it has an associated value. When the last page is reached, the token is empty. 
        
        """
        pass

    def list_resources(self, OrganizationId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListResources>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_resources(
              OrganizationId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier for the organization under which the resources exist.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to use to retrieve the next page of results. The first call does not contain any tokens.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Resources\': [
                    {
                        \'Id\': \'string\',
                        \'Email\': \'string\',
                        \'Name\': \'string\',
                        \'Type\': \'ROOM\'|\'EQUIPMENT\',
                        \'State\': \'ENABLED\'|\'DISABLED\'|\'DELETED\',
                        \'EnabledDate\': datetime(2015, 1, 1),
                        \'DisabledDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Resources** *(list) --* 
        
              One page of the organization\'s resource representation.
        
              - *(dict) --* 
        
                The overview for a resource containing relevant data regarding it.
        
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
        
            - **NextToken** *(string) --* 
        
              The token used to paginate through all the organization\'s resources. While results are still available, it has an associated value. When the last page is reached, the token is empty.
        
        """
        pass

    def list_users(self, OrganizationId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListUsers>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_users(
              OrganizationId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier for the organization under which the users exist.
        
        :type NextToken: string
        :param NextToken: 
        
          TBD
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Users\': [
                    {
                        \'Id\': \'string\',
                        \'Email\': \'string\',
                        \'Name\': \'string\',
                        \'DisplayName\': \'string\',
                        \'State\': \'ENABLED\'|\'DISABLED\'|\'DELETED\',
                        \'UserRole\': \'USER\'|\'RESOURCE\'|\'SYSTEM_USER\',
                        \'EnabledDate\': datetime(2015, 1, 1),
                        \'DisabledDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
        
        """
        pass

    def put_mailbox_permissions(self, OrganizationId: str, EntityId: str, GranteeId: str, PermissionValues: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/PutMailboxPermissions>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_mailbox_permissions(
              OrganizationId=\'string\',
              EntityId=\'string\',
              GranteeId=\'string\',
              PermissionValues=[
                  \'FULL_ACCESS\'|\'SEND_AS\'|\'SEND_ON_BEHALF\',
              ]
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier of the organization under which the entity (user or group) exists.
        
        :type EntityId: string
        :param EntityId: **[REQUIRED]** 
        
          The identifier of the entity (user or group) for which to update mailbox permissions.
        
        :type GranteeId: string
        :param GranteeId: **[REQUIRED]** 
        
          The identifier of the entity (user or group) to which to grant the permissions.
        
        :type PermissionValues: list
        :param PermissionValues: **[REQUIRED]** 
        
          The permissions granted to the grantee. SEND_AS allows the grantee to send email as the owner of the mailbox (the grantee is not mentioned on these emails). SEND_ON_BEHALF allows the grantee to send email on behalf of the owner of the mailbox (the grantee is not mentioned as the physical sender of these emails). FULL_ACCESS allows the grantee full access to the mailbox, irrespective of other folder-level permissions set on the mailbox.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def register_to_work_mail(self, OrganizationId: str, EntityId: str, Email: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/RegisterToWorkMail>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_to_work_mail(
              OrganizationId=\'string\',
              EntityId=\'string\',
              Email=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier for the organization under which the Amazon WorkMail entity exists.
        
        :type EntityId: string
        :param EntityId: **[REQUIRED]** 
        
          The identifier for the entity to be updated.
        
        :type Email: string
        :param Email: **[REQUIRED]** 
        
          The email for the entity to be updated.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def reset_password(self, OrganizationId: str, UserId: str, Password: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ResetPassword>`_
        
        **Request Syntax** 
        ::
        
          response = client.reset_password(
              OrganizationId=\'string\',
              UserId=\'string\',
              Password=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier of the organization that contains the user for which the password is reset.
        
        :type UserId: string
        :param UserId: **[REQUIRED]** 
        
          The identifier of the user for whom the password is reset.
        
        :type Password: string
        :param Password: **[REQUIRED]** 
        
          The new password for the user.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_primary_email_address(self, OrganizationId: str, EntityId: str, Email: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/UpdatePrimaryEmailAddress>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_primary_email_address(
              OrganizationId=\'string\',
              EntityId=\'string\',
              Email=\'string\'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The organization that contains the entity to update.
        
        :type EntityId: string
        :param EntityId: **[REQUIRED]** 
        
          The entity to update (user, group, or resource).
        
        :type Email: string
        :param Email: **[REQUIRED]** 
        
          The value of the email to be updated as primary.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_resource(self, OrganizationId: str, ResourceId: str, Name: str = None, BookingOptions: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/UpdateResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_resource(
              OrganizationId=\'string\',
              ResourceId=\'string\',
              Name=\'string\',
              BookingOptions={
                  \'AutoAcceptRequests\': True|False,
                  \'AutoDeclineRecurringRequests\': True|False,
                  \'AutoDeclineConflictingRequests\': True|False
              }
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]** 
        
          The identifier associated with the organization for which the resource is updated.
        
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]** 
        
          The identifier of the resource to be updated.
        
        :type Name: string
        :param Name: 
        
          The name of the resource to be updated.
        
        :type BookingOptions: dict
        :param BookingOptions: 
        
          The resource\'s booking options to be updated.
        
          - **AutoAcceptRequests** *(boolean) --* 
        
            The resource\'s ability to automatically reply to requests. If disabled, delegates must be associated to the resource.
        
          - **AutoDeclineRecurringRequests** *(boolean) --* 
        
            The resource\'s ability to automatically decline any recurring requests.
        
          - **AutoDeclineConflictingRequests** *(boolean) --* 
        
            The resource\'s ability to automatically decline any conflicting requests.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass
